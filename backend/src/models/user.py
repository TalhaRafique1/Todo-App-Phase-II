"""User model for SQLModel with PostgreSQL."""

from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    """User entity with email and authentication data."""

    id: Optional[str] = Field(
        default_factory=lambda: str(uuid4()),
        primary_key=True,
        max_length=36
    )
    email: str = Field(max_length=255, unique=True, index=True)
    hashed_password: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to todos
    tasks: List["Task"] = Relationship(back_populates="user")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "id": "550e8400-e29b-41d4-a716-446655440000"
            }
        }


class UserCreate(SQLModel):
    """Schema for creating a new user."""

    email: str = Field(max_length=255)
    password: str = Field(min_length=8, max_length=255)


class UserResponse(SQLModel):
    """Schema for user response."""

    id: str
    email: str
    created_at: datetime


class Token(SQLModel):
    """Schema for JWT token response."""

    access_token: str
    token_type: str = "bearer"
    user: UserResponse
