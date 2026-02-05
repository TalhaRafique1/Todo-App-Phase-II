# Quickstart Guide: AI Chatbot Backend & Agent Integration

## Overview
Quick start guide for setting up and running the AI chatbot backend with MCP integration.

## Prerequisites
- Python 3.11+
- Node.js 18+ (for frontend)
- Access to OpenAI API
- PostgreSQL-compatible database (Neon Serverless PostgreSQL recommended)

## Environment Variables
Create a `.env` file in the backend directory with the following variables:

```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Database Configuration
DATABASE_URL=postgresql://username:password@host:port/database_name

# JWT Secret for Authentication
BETTER_AUTH_SECRET=your_jwt_secret_here

# Better Auth Configuration
BETTER_AUTH_URL=http://localhost:8000
```

## Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Update requirements.txt to include:
   ```
   openai>=1.0.0
   mcp-server>=0.0.1  # Or whatever MCP SDK is available
   ```

3. Set up the database:
   ```bash
   python create_tables.py
   ```

4. Start the MCP server:
   ```bash
   cd mcp-server
   python main.py
   ```

5. Start the main backend server:
   ```bash
   cd backend
   uvicorn src.main:app --reload --port 8000
   ```

## Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## API Usage
Once running, you can interact with the chat endpoint:

```bash
curl -X POST http://localhost:8000/api/{user_id}/chat \
  -H "Authorization: Bearer {jwt_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": "optional_conversation_uuid",
    "message": "Add a task to buy groceries"
  }'
```

## MCP Tools Available
The MCP server exposes these tools to the AI agent:
- `add_task`: Creates a new task
- `list_tasks`: Lists existing tasks for the user
- `complete_task`: Marks a task as completed
- `delete_task`: Deletes a task
- `update_task`: Updates task details

## Development Workflow
1. Make changes to the code
2. Backend server auto-reloads with `--reload` flag
3. Frontend server auto-reloads when files change
4. Run tests to ensure functionality:
   ```bash
   cd backend
   pytest tests/
   ```

## Troubleshooting
- If the MCP server doesn't start, ensure the OpenAI API key is correctly configured
- If authentication fails, verify the JWT token and user_id match
- If database connections fail, check the DATABASE_URL configuration