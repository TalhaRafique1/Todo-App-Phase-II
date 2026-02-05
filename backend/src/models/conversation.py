from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, DateTime
import uuid


class ConversationBase(SQLModel):
    user_id: str = Field(index=True)


class Conversation(ConversationBase, table=True):
    """
    Represents a conversation thread between a user and the AI assistant.
    """
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    created_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow)

    # Relationship with Message model
    # messages: List["Message"] = Relationship(back_populates="conversation")


class ConversationCreate(ConversationBase):
    pass


class ConversationRead(ConversationBase):
    id: str
    created_at: datetime
    updated_at: datetime