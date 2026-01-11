"""JWT token creation and verification utilities."""

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from ..config import settings


def create_access_token(user_id: str, email: str, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT access token for a user."""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=settings.jwt_expiry_hours)

    to_encode = {
        "sub": user_id,
        "email": email,
        "exp": expire,
        "iat": datetime.utcnow(),
    }

    encoded_jwt = jwt.encode(
        to_encode,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm
    )
    return encoded_jwt


def decode_token(token: str) -> dict:
    """Decode and verify a JWT token."""
    payload = jwt.decode(
        token,
        settings.jwt_secret,
        algorithms=[settings.jwt_algorithm]
    )
    return payload


def get_user_id_from_token(token: str) -> Optional[str]:
    """Extract user_id from JWT token."""
    try:
        payload = decode_token(token)
        return payload.get("sub")
    except JWTError:
        return None


def get_email_from_token(token: str) -> Optional[str]:
    """Extract email from JWT token."""
    try:
        payload = decode_token(token)
        return payload.get("email")
    except JWTError:
        return None
