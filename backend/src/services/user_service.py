"""User service for user-related operations."""

from sqlmodel import Session, select
from typing import Optional
from ..models.user import User


class UserService:
    """Service class for user operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get a user by ID."""
        user = self.db.get(User, user_id)
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get a user by email."""
        user = self.db.exec(
            select(User).where(User.email == email)
        ).first()
        return user


def create_user_service(db: Session) -> UserService:
    """Factory function to create a UserService instance."""
    return UserService(db)