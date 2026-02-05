from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional, Dict, Any
from sqlmodel import Session
from pydantic import BaseModel
import uuid

from ..database import get_db
from ..services.conversations import conversations_service
from ..services.ai_agent import ai_agent_service
from ..middleware.auth import get_current_user
from ..models.user import User
from ..models.conversation import ConversationCreate
from ..models.message import MessageCreate


router = APIRouter(prefix="/api", tags=["chat"])


class ChatRequest(BaseModel):
    conversation_id: Optional[str] = None
    message: str


class ChatResponse(BaseModel):
    conversation_id: str
    response: str
    tool_calls: list[Dict[str, Any]]


@router.post("/{user_id}/chat", response_model=ChatResponse)
async def chat_endpoint(
    user_id: str,
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> ChatResponse:
    """
    Chat endpoint for AI-powered interactions.
    Accepts natural language messages and returns AI-generated responses with task operations.
    """
    # Verify JWT token and ensure user identity matches URL user_id
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User ID in token doesn't match path parameter"
        )

    # Validate inputs
    if not request.message or not request.message.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Message is required"
        )

    # Load conversation history (or create new conversation if none provided)
    conversation = None
    if request.conversation_id:
        # Verify the conversation belongs to the user
        conversation = conversations_service.get_conversation_by_id(
            db=db,
            conversation_id=request.conversation_id,
            user_id=user_id
        )
        if not conversation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Conversation not found or access denied"
            )
    else:
        # Create a new conversation
        conversation_data = ConversationCreate(user_id=user_id)
        conversation = conversations_service.create_conversation(
            db=db,
            conversation_data=conversation_data
        )

    # Store the incoming user message
    message_data = MessageCreate(
        user_id=user_id,
        conversation_id=conversation.id,
        role="user",
        content=request.message
    )
    user_message = conversations_service.create_message(
        db=db,
        message_data=message_data
    )

    # Get conversation history for the AI agent
    conversation_history = conversations_service.get_messages_by_conversation(
        db=db,
        conversation_id=conversation.id,
        user_id=user_id
    )

    # Format history for AI agent (excluding the current message which was just added)
    history_for_ai = []
    for msg in conversation_history[:-1]:  # Exclude the current user message
        history_for_ai.append({
            "role": msg.role,
            "content": msg.content
        })

    # Execute AI agent with message history
    ai_result = ai_agent_service.process_message(
        user_message=request.message,
        conversation_history=history_for_ai,
        user_id=user_id
    )

    # Store the assistant's response
    assistant_message_data = MessageCreate(
        user_id=user_id,  # The assistant is acting on behalf of the system for the user
        conversation_id=conversation.id,
        role="assistant",
        content=ai_result["response"]
    )
    assistant_message = conversations_service.create_message(
        db=db,
        message_data=assistant_message_data
    )

    # Return response in ChatKit-compatible format
    return ChatResponse(
        conversation_id=conversation.id,
        response=ai_result["response"],
        tool_calls=ai_result["tool_calls"]
    )


# Additional endpoint to get conversation history if needed
@router.get("/{user_id}/conversations/{conversation_id}")
async def get_conversation(
    user_id: str,
    conversation_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get a specific conversation for a user.
    """
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User ID in token doesn't match path parameter"
        )

    conversation = conversations_service.get_conversation_by_id(
        db=db,
        conversation_id=conversation_id,
        user_id=user_id
    )

    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found or access denied"
        )

    return conversation