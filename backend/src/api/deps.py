"""Dependency injection functions for API endpoints."""

from typing import Generator
from sqlmodel import Session
from fastapi import Depends
from ..database import SessionLocal
from ..middleware.auth import get_current_user
from ..models.user import UserResponse


def get_db() -> Generator[Session, None, None]:
    """Dependency to get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Re-export the current user dependency
CurrentActiveUser = Depends(get_current_user)