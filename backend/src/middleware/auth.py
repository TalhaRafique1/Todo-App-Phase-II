"""JWT authentication middleware for FastAPI."""

from datetime import datetime
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..utils.jwt import decode_token, get_user_id_from_token
from ..models.user import UserResponse


security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> UserResponse:
    """Dependency to get current authenticated user from JWT token."""
    token = credentials.credentials

    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        email = payload.get("email")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing user ID",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return UserResponse(
            id=user_id,
            email=email,
            created_at=datetime.utcnow()  # Placeholder
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def verify_user_access(
    user_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> bool:
    """Verify that the authenticated user matches the requested resource owner."""
    token = credentials.credentials
    token_user_id = get_user_id_from_token(token)

    if token_user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this resource",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return True


def create_unauthorized_error(message: str = "Not authenticated") -> HTTPException:
    """Create a standard unauthorized error."""
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=message,
        headers={"WWW-Authenticate": "Bearer"},
    )
