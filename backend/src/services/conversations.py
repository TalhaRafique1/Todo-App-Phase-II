from typing import List, Optional
from sqlmodel import Session, select
from ..models.conversation import Conversation, ConversationCreate
from ..models.message import Message, MessageCreate


class ConversationsService:
    """
    Service for managing conversations and messages.
    """

    def create_conversation(self, db: Session, conversation_data: ConversationCreate) -> Conversation:
        """
        Create a new conversation.
        """
        conversation = Conversation(
            user_id=conversation_data.user_id
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        return conversation

    def get_conversation_by_id(self, db: Session, conversation_id: str, user_id: str) -> Optional[Conversation]:
        """
        Get a conversation by ID for a specific user (enforcing user isolation).
        """
        statement = select(Conversation).where(
            Conversation.id == conversation_id,
            Conversation.user_id == user_id
        )
        return db.exec(statement).first()

    def get_conversations_by_user(self, db: Session, user_id: str) -> List[Conversation]:
        """
        Get all conversations for a specific user.
        """
        statement = select(Conversation).where(Conversation.user_id == user_id)
        return db.exec(statement).all()

    def create_message(self, db: Session, message_data: MessageCreate) -> Message:
        """
        Create a new message in a conversation.
        """
        message = Message(
            user_id=message_data.user_id,
            conversation_id=message_data.conversation_id,
            role=message_data.role,
            content=message_data.content
        )
        db.add(message)
        db.commit()
        db.refresh(message)
        return message

    def get_messages_by_conversation(self, db: Session, conversation_id: str, user_id: str) -> List[Message]:
        """
        Get all messages for a conversation, enforcing user isolation.
        """
        statement = select(Message).where(
            Message.conversation_id == conversation_id,
            Message.user_id == user_id  # This ensures user owns the messages
        )
        return db.exec(statement).all()


# Global instance
conversations_service = ConversationsService()