"""Authentication service for user registration and login."""

from sqlmodel import Session, select
from typing import Optional
from ..models.user import User, UserCreate
from ..utils.jwt import verify_password, get_password_hash
from jose import JWTError


class AuthService:
    """Service class for authentication operations."""

    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_create: UserCreate) -> Optional[User]:
        """Register a new user."""
        # Check if user already exists
        existing_user = self.db.exec(
            select(User).where(User.email == user_create.email)
        ).first()

        if existing_user:
            return None  # User already exists

        # Create new user
        hashed_password = get_password_hash(user_create.password)
        db_user = User(
            email=user_create.email,
            hashed_password=hashed_password
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password."""
        user = self.db.exec(
            select(User).where(User.email == email)
        ).first()

        if not user or not verify_password(password, user.hashed_password):
            return None

        return user


def create_auth_service(db: Session) -> AuthService:
    """Factory function to create an AuthService instance."""
    return AuthService(db)