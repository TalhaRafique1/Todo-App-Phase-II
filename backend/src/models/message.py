from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime
import uuid


class MessageBase(SQLModel):
    user_id: str = Field(index=True)
    conversation_id: str = Field(index=True)
    role: str = Field(regex="^(user|assistant)$")  # Enum: "user" or "assistant"
    content: str = Field(min_length=1)


class Message(MessageBase, table=True):
    """
    Represents individual messages within a conversation.
    """
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    created_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow)

    # Relationship with Conversation model
    # conversation: Optional["Conversation"] = Relationship(back_populates="messages")


class MessageCreate(MessageBase):
    pass


class MessageRead(MessageBase):
    id: str
    created_at: datetime