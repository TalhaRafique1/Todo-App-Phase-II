---
id: 2
title: AI Chatbot Backend Plan
stage: plan
date: 2026-01-20
surface: agent
model: claude-sonnet-4-5-20250929
feature: ai-chatbot-backend
branch: 004-ai-chatbot-backend
user: Shoaib Computers
command: /sp.plan
labels: [plan, ai-chatbot, backend, mcp, openai-agents]
links:
  spec: specs/004-ai-chatbot-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/004-ai-chatbot-backend/plan.md
 - specs/004-ai-chatbot-backend/research.md
 - specs/004-ai-chatbot-backend/data-model.md
 - specs/004-ai-chatbot-backend/quickstart.md
 - specs/004-ai-chatbot-backend/contracts/chat-api.yaml
tests:
 - none
---

## Prompt

```
before planing first you can review the frontend and backend folders after that  generate plan here is plan                                               Todo AI Chatbot Backend & Agent Integration (Spec-4)

Execution Strategy:
Implement a stateless AI-powered chatbot backend that integrates OpenAI Agents SDK and MCP tools, exposes a secure chat API to the frontend, and persists conversation context in the database while maintaining strict user isolation.

Plan Phases:

Phase 1 — Backend & Environment Setup
- Extend existing FastAPI backend from Phase I & II
- Configure environment variables:
  - OPENAI_API_KEY
  - BETTER_AUTH_SECRET
- Add required dependencies:
  - OpenAI Agents SDK
  - Official MCP SDK
- Verify JWT authentication middleware is active for chat routes
Phase 2 — Database Models for Conversations
- Define SQLModel models:
  - Conversation
  - Message
- Link Conversation → Message relationship
- Ensure user_id is present on all models
- Create migration scripts for new tables
- Verify persistence in Neon PostgreSQL

Phase 3 — MCP Server Implementation
- Initialize MCP server using Official MCP SDK
- Define stateless MCP tools:
  - add_task
  - list_tasks
  - complete_task
  - delete_task
  - update_task
- Implement each tool:
  - Validate inputs
  - Enforce authenticated user ownership
  - Perform DB operations via SQLModel
  - Return structured tool responses
- Ensure MCP server holds no in-memory state
Phase 4 — AI Agent Configuration
- Define AI agent using OpenAI Agents SDK
- Register MCP tools with agent
- Configure agent instructions:
  - Detect task-related intents
  - Use MCP tools for all task operations
  - Provide friendly confirmations
  - Handle errors gracefully
- Ensure agent never accesses database directly

Phase 5 — Chat API Endpoint Implementation
- Implement POST /api/{user_id}/chat endpoint
- Endpoint responsibilities:
  - Verify JWT token
  - Match token user_id with URL user_id
  - Load conversation history (or create new)
  - Store incoming user message
  - Execute AI agent with message history
  - Capture MCP tool calls
  - Store assistant response
  - Return frontend-ready response payload
Phase 6 — Frontend Integration Readiness
- Validate request/response schema compatibility with ChatKit
- Ensure response includes:
  - conversation_id
  - assistant response text
  - MCP tool calls (if any)
- Confirm Authorization header handling
- Ensure backend remains UI-agnostic


Phase 7 — Statelessness & Resilience Validation
- Restart backend and verify conversation resumes correctly
- Confirm no in-memory session dependency
- Validate database-only state reconstruction
- Test concurrent chat requests

Phase 8 — Security & Error Handling Tests
- Test without JWT → 401 Unauthorized
- Test mismatched user_id → access denied
- Test invalid MCP tool invocation
- Test missing task scenarios
- Ensure friendly error responses
Final Verification:
- Natural language commands correctly trigger MCP tools
- All task operations work via chat
- Conversation context persists across requests
- Frontend can consume responses cleanly
- System remains stateless and scalable
- Spec-Driven workflow is clearly demonstrable
```

## Response snapshot

Successfully created a comprehensive implementation plan for the AI Chatbot Backend & Agent Integration (Spec-4). The plan includes:

1. **Technical Context**: Defined the Python 3.11, FastAPI, OpenAI Agents SDK, MCP SDK, SQLModel, and Neon PostgreSQL stack
2. **Constitution Check**: Verified compliance with all constitutional requirements including statelessness, security, and scalability
3. **Project Structure**: Outlined detailed directory structure for backend, frontend, and new MCP server components
4. **Research**: Completed research on OpenAI Agents SDK implementation, MCP server architecture, and conversation state management
5. **Data Model**: Designed Conversation and Message models that integrate with existing Task system
6. **API Contracts**: Created detailed contract for the chat API endpoint
7. **Quickstart Guide**: Provided comprehensive setup instructions

The plan follows the Spec-Driven Development workflow and maintains consistency with the existing architecture while adding the AI chatbot functionality. All constitutional requirements are satisfied, including statelessness, security-first design, and user isolation.

## Outcome

- ✅ Impact: High - Complete implementation plan created with all required artifacts
- 🧪 Tests: None required for planning phase
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and contracts/chat-api.yaml
- 🔁 Next prompts: Ready for task breakdown phase (/sp.tasks) to create implementation tasks
- 🧠 Reflection: Plan comprehensively addresses all requirements while maintaining architectural integrity

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Begin task breakdown for implementation