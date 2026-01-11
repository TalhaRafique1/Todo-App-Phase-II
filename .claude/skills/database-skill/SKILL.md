---
name: database-skill
description: Design and manage database schemas, create tables, and write migrations efficiently. Use for backend and full-stack projects.
---

# Database Skill

## Instructions

1. **Schema Design**
   - Plan tables with proper normalization
   - Define primary and foreign keys
   - Use appropriate data types for each column

2. **Table Creation**
   - Write SQL or ORM-based table definitions
   - Include constraints (NOT NULL, UNIQUE, DEFAULT)
   - Handle relationships (one-to-one, one-to-many, many-to-many)

3. **Migrations**
   - Generate migration scripts for schema changes
   - Apply migrations safely in development and production
   - Rollback changes when necessary

4. **Best Practices**
   - Name tables and columns clearly and consistently
   - Avoid redundant data
   - Optimize indexes for queries
   - Maintain a versioned migration history

## Example Structure

```sql
-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Posts Table
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    title VARCHAR(100) NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
