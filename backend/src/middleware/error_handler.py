"""Error handling middleware for FastAPI."""

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class AppException(Exception):
    """Custom application exception."""

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


async def app_exception_handler(request: Request, exc: AppException):
    """Handle custom application exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
        headers=exc.headers,
    )


async def validation_exception_handler(request: Request, exc):
    """Handle Pydantic validation errors."""
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"],
        })

    return JSONResponse(
        status_code=422,
        content={"detail": "Validation error", "errors": errors},
    )


# Error response schemas
class ErrorResponse:
    """Schema for error responses."""

    def __init__(self, detail: str, errors: list | None = None):
        self.detail = detail
        self.errors = errors


def create_error_response(message: str, status_code: int = 400) -> dict:
    """Create a standardized error response."""
    return {
        "detail": message,
        "status_code": status_code,
    }


# Common error responses
UNAUTHORIZED = create_error_response("Not authenticated", 401)
FORBIDDEN = create_error_response("Not authorized", 403)
NOT_FOUND = create_error_response("Resource not found", 404)
VALIDATION_ERROR = create_error_response("Validation error", 422)
INTERNAL_ERROR = create_error_response("Internal server error", 500)
