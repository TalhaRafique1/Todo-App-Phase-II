from sqlmodel import SQLModel
from sqlalchemy import create_engine

# Base class for all models
class Base(SQLModel):
    pass

# Create engine for database connection
# This will be configured in database.py