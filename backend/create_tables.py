"""Script to create database tables manually."""

import sys
import os

# Add backend src to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import engine, init_db
from sqlmodel import SQLModel

def main():
    print("Creating database tables...")
    init_db()
    print("Tables created successfully!")

    # Print table names
    print("\nRegistered tables:")
    for table in SQLModel.metadata.tables.values():
        print(f"  - {table.name}")

if __name__ == "__main__":
    main()
