#!/usr/bin/env python3
"""Script to initialize the database tables."""

import os
from backend.src.database import init_db

if __name__ == "__main__":
    print("Initializing database tables...")
    init_db()
    print("Database tables created successfully!")