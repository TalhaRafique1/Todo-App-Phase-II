# Implementation Plan: AI Chatbot Backend & Agent Integration

**Branch**: `004-ai-chatbot-backend` | **Date**: 2026-01-20 | **Spec**: specs/004-ai-chatbot-backend/spec.md
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a stateless AI-powered chatbot backend that integrates OpenAI Agents SDK and MCP tools, exposes a secure chat API to the frontend, and persists conversation context in the database while maintaining strict user isolation. The solution extends the existing FastAPI backend with a new chat endpoint that orchestrates between the frontend, AI agent, and MCP tools for task management operations.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, OpenAI Agents SDK, Official MCP SDK, SQLModel, Neon PostgreSQL, Better Auth
**Storage**: Neon Serverless PostgreSQL via SQLModel ORM
**Testing**: pytest for backend testing
**Target Platform**: Linux server (deployable to Vercel)
**Project Type**: web (separate frontend and backend)
**Performance Goals**: <5 second response time for AI chat interactions
**Constraints**: Stateless server architecture with database persistence, JWT authentication required, user isolation enforced
**Scale/Scope**: Multi-user support with individual task and conversation isolation

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Technology stack compliance: Uses specified stack (FastAPI, OpenAI Agents SDK, MCP SDK, SQLModel, Neon PostgreSQL, Better Auth)
- ✅ Security requirements addressed: JWT authentication required for all endpoints, user isolation enforced
- ✅ User isolation enforced: Each user only accesses their own tasks and conversations
- ✅ Documentation artifacts generated: Spec, plan, and upcoming tasks documents
- ✅ Statelessness requirements met: Server holds no in-memory state, all data persisted in database
- ✅ AI behavior determinism maintained: AI agent follows deterministic rules for tool usage
- ✅ Horizontal scalability preserved: Stateless design enables horizontal scaling

## Project Structure

### Documentation (this feature)

```text
specs/004-ai-chatbot-backend/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── task.py
│   │   ├── conversation.py          # New: Conversation model
│   │   └── message.py               # New: Message model
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── tasks.py
│   │   ├── conversations.py         # New: Conversation service
│   │   └── ai_agent.py              # New: AI agent orchestration
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── todos.py
│   │   ├── chat.py                  # New: Chat endpoint implementation
│   │   └── v1/
│   ├── middleware/
│   │   └── auth.py
│   ├── utils/
│   │   └── jwt.py
│   ├── database.py
│   ├── config.py
│   └── main.py                      # Updated: Include chat router
├── requirements.txt                 # Updated: Add OpenAI, MCP SDK dependencies
├── create_tables.py
└── tests/

frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── chat/                   # Updated: Chat interface
│   │   │   └── page.tsx
│   │   └── api/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   ├── services/
│   │   └── api.ts
│   └── types/
├── package.json                     # Updated: If needed for chat features
└── next.config.ts

mcp-server/                          # New directory for MCP server
├── src/
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── task_tools.py            # MCP tools: add_task, list_tasks, etc.
│   │   └── validation.py
│   ├── server.py                    # MCP server implementation
│   └── config.py
├── requirements.txt
└── main.py
```

**Structure Decision**: The implementation extends the existing web application structure with:
1. New backend components for chat functionality and conversation management
2. MCP server as a separate service to handle task operations
3. Updates to frontend to support chat interface
4. New data models for conversations and messages while maintaining existing task structure

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Additional service (MCP server) | Required by architecture specification for proper separation of concerns | Direct database access from AI agent violates statelessness principle |
