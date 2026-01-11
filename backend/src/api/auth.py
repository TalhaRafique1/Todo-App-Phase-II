"""Authentication API endpoints for user registration and login."""

from datetime import datetime
from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session, select
from ..database import get_db
from ..models.user import User, UserCreate, UserResponse, Token
from ..utils.auth import hash_password, verify_password
from ..utils.jwt import create_access_token
from ..middleware.auth import get_current_user


router = APIRouter(prefix="/api/auth", tags=["authentication"])


@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user with email and password."""

    # Check if email already exists
    existing = db.exec(select(User).where(User.email == user_data.email)).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Create new user
    hashed = hash_password(user_data.password)
    new_user = User(
        email=user_data.email,
        hashed_password=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create JWT token
    token = create_access_token(user_id=new_user.id, email=new_user.email)

    return Token(
        access_token=token,
        user=UserResponse(
            id=new_user.id,
            email=new_user.email,
            created_at=new_user.created_at
        )
    )


@router.post("/login", response_model=Token)
async def login(user_data: UserCreate, db: Session = Depends(get_db)):
    """Authenticate user and return JWT token."""

    # Find user by email
    user = db.exec(select(User).where(User.email == user_data.email)).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Create JWT token
    token = create_access_token(user_id=user.id, email=user.email)

    return Token(
        access_token=token,
        user=UserResponse(
            id=user.id,
            email=user.email,
            created_at=user.created_at
        )
    )


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: UserResponse = Depends(get_current_user)):
    """Get current authenticated user info."""
    return current_user


@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout():
    """Logout user and invalidate session."""
    # In a stateless JWT system, the client is responsible for removing the token
    # The server doesn't maintain session state to invalidate
    return {"success": True, "message": "Logged out successfully"}
