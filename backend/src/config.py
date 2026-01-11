"""Configuration management with environment variable loading."""

import os
from typing import Optional
from pydantic import BaseModel


class Settings(BaseModel):
    """Application settings loaded from environment variables."""

    # Database
    database_url: str = "postgresql+psycopg://user:password@host/database"

    # JWT
    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expiry_hours: int = 24

    # Better Auth
    better_auth_secret: str = "change-me-in-production"

    # API
    api_url: str = "http://localhost:8000"
    frontend_url: str = "http://localhost:3000"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    """Get application settings."""
    return Settings()


# Global settings instance
settings = get_settings()
