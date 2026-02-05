---
id: 1
title: Update Hackathon Phase III
stage: constitution
date: 2026-01-20
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: Shoaib Computers
command: /sp.constitution
labels: [constitution, hackathon, phase-iii, ai-todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
$ARGUMENTS

Project: AI-Powered Full-Stack Todo Application (Hackathon Phase III)

Core principles:
- Strict Spec-Driven Development (Spec → Plan → Tasks → AI Implementation)
- Stateless server architecture with persistent state
- Clear separation of concerns (UI, API, AI logic, MCP tools)
- Security-first design (authenticated, user-isolated access)
- Deterministic AI behavior through explicit tool usage
- Reproducibility and traceability of agent actions
Key standards:
- All AI behavior must be defined through written specifications
- AI agents must use MCP tools for all task operations (no direct DB access)
- MCP tools must be stateless and persist state only via database
- Chat endpoint must be stateless across requests
- Conversation context must be reconstructed from database on each request
- Authentication must be enforced on all chat and MCP interactions
- Clear logging of tool calls and agent responses
Technology constraints:
- Frontend: OpenAI ChatKit
- Backend: Python FastAPI
- AI Framework: OpenAI Agents SDK
- MCP Server: Official MCP SDK
- ORM: SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT
- Architecture: Frontend ↔ FastAPI ↔ Agents ↔ MCP ↔ Database
Functional requirements:
- Natural-language Todo management (create, list, update, complete, delete)
- Stateless chat API endpoint: POST /api/{user_id}/chat
- Persistent conversation and message history
- MCP server exposing task operations as tools
- AI agent selects correct tools based on user intent
- Friendly confirmations after every action
- Graceful error handling (task not found, invalid input, auth failure)
- Conversation continuity after server restart

Security requirements:
- All chat requests require valid JWT token
- User identity must be verified and matched with request user_id
- MCP tools must enforce user ownership
- No cross-user data access
- No in-memory session storage

Constraints:
- No manual coding outside Claude Code execution
- No hidden state inside agents or MCP server
- No direct database access by AI agent
- All tool definitions must be explicit and versioned
- Backend must remain horizontally scalable
Not in scope:
- Voice input/output
- Multi-agent collaboration
- Streaming responses
- External integrations beyond MCP tools
- Advanced analytics or recommendations
Success criteria:
- Users can manage todos using natural language
- AI agent reliably invokes correct MCP tools
- All chat interactions are stateless and resumable
- Task operations remain consistent with Phase I & II
- Authentication and user isolation are preserved
- System passes hackathon review for correctness, architecture, and spec discipline
```

## Response snapshot

Updated the project constitution to reflect the requirements for the AI-Powered Full-Stack Todo Application (Hackathon Phase III). The updated constitution includes:

- Enhanced core principles focusing on statelessness with persistent state, deterministic AI behavior, and scalability
- Updated technology stack to reflect OpenAI ChatKit frontend, Python FastAPI backend, OpenAI Agents SDK, and MCP SDK
- Detailed functional requirements for natural-language todo management and stateless chat API
- Comprehensive security requirements for JWT authentication and user data isolation
- Quality standards emphasizing statelessness and traceability
- Governance provisions specific to the AI-powered application architecture

The constitution version has been incremented from 1.0.0 to 2.0.0 to reflect the significant architectural changes for Phase III.

## Outcome

- ✅ Impact: High - Updated constitution to guide AI-powered todo application development for Hackathon Phase III
- 🧪 Tests: None required for constitution update
- 📁 Files: Modified .specify/memory/constitution.md
- 🔁 Next prompts: Continue with specification, planning, and task breakdown for the AI-powered todo application
- 🧠 Reflection: Constitution now properly reflects the advanced architecture requirements for the AI-powered application

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Begin specification phase for the AI-powered todo application