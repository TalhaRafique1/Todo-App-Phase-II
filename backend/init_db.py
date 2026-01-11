#!/usr/bin/env python3
"""Script to initialize the database tables."""

import sys
import os

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.database import init_db

if __name__ == "__main__":
    print("Initializing database tables...")
    try:
        init_db()
        print("Database tables created successfully!")
        print("Tables created: user, task")
    except Exception as e:
        print(f"Error initializing database: {e}")
        print("Please check your DATABASE_URL in the .env file.")
        print("Make sure to replace 'your_actual_neon_database_url_here' with your actual Neon PostgreSQL connection string.")