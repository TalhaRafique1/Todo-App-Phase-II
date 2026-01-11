"""Database connection and session management for SQLModel with Neon PostgreSQL."""

import os
from typing import Generator
from sqlmodel import SQLModel, create_engine, Session

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

# Import models to register them with SQLModel metadata
from .models import User, Task  # noqa: F401

# Database URL from environment variable
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://user:password@host/database"
)

# Ensure we're using the psycopg driver
if "postgresql://" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://")
elif "postgres://" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://")

# Create SQLModel engine
engine = create_engine(DATABASE_URL, echo=False)


def get_db() -> Generator[Session, None, None]:
    """Dependency to get database session."""
    with Session(engine) as session:
        yield session


def init_db() -> None:
    """Initialize database tables."""
    SQLModel.metadata.create_all(engine)
