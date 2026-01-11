"""Todo model for SQLModel with PostgreSQL."""

from datetime import datetime
from typing import Optional
from uuid import uuid4
from sqlmodel import SQLModel, Field, Relationship


class Task(SQLModel, table=True):
    """Todo task entity owned by a user."""

    id: Optional[str] = Field(
        default_factory=lambda: str(uuid4()),
        primary_key=True,
        max_length=36
    )
    user_id: str = Field(max_length=36, foreign_key="user.id", index=True)
    title: str = Field(max_length=255, nullable=False)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to user
    user: "User" = Relationship(back_populates="tasks")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Buy groceries",
                "completed": False,
                "id": "550e8400-e29b-41d4-a716-446655440000"
            }
        }


class TaskCreate(SQLModel):
    """Schema for creating a new task."""

    title: str = Field(min_length=1, max_length=255)


class TaskUpdate(SQLModel):
    """Schema for updating a task."""

    title: Optional[str] = Field(None, min_length=1, max_length=255)
    completed: Optional[bool] = None


class TaskResponse(SQLModel):
    """Schema for task response."""

    id: str
    user_id: str
    title: str
    completed: bool
    created_at: datetime
    updated_at: datetime
