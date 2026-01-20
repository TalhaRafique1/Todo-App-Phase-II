---
id: 1
title: AI Chatbot Backend Spec
stage: spec
date: 2026-01-20
surface: agent
model: claude-sonnet-4-5-20250929
feature: ai-chatbot-backend
branch: 004-ai-chatbot-backend
user: Shoaib Computers
command: /sp.specify
labels: [spec, ai-chatbot, backend, mcp, openai-agents]
links:
  spec: specs/004-ai-chatbot-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/004-ai-chatbot-backend/spec.md
 - specs/004-ai-chatbot-backend/checklists/requirements.md
tests:
 - none
---

## Prompt

```
Todo AI Chatbot Backend & Frontend Integration (Spec-4)

Target audience:
- Hackathon judges evaluating AI-native architecture and system integration
- Developers reviewing OpenAI Agents + MCP backend design
- Students learning stateless AI backend patterns

Focus:
- Build an AI-powered chatbot backend using OpenAI Agents SDK and MCP
- Expose a secure, stateless chat API consumable by frontend UI
- Ensure seamless integration between frontend chat interface and AI agent backend
- Maintain strict separation between UI, API, agent logic, MCP tools, and database
Success criteria:
- Frontend can send natural language messages to backend chat endpoint
- Backend processes messages using AI agent and MCP tools
- AI responses are returned in frontend-consumable format
- Conversation state is persisted and correctly resumed across requests
- Task actions triggered via chat reflect immediately in frontend
- System works end-to-end after server restart
- Tool calls are surfaced for debugging and review

Core requirements:
- FastAPI backend exposes chat endpoint:
  POST /api/{user_id}/chat
- Endpoint accepts requests from frontend chat UI (ChatKit)
- Request payload:
  - conversation_id (optional)
  - message (required)
- Response payload:
  - conversation_id
  - response (assistant message)
  - tool_calls (list of MCP tools invoked)
Agent & Backend Integration:
- Backend acts as orchestration layer between frontend and AI agent
- Backend:
  - Fetches conversation history from database
  - Builds message array for agent
  - Executes agent via OpenAI Agents SDK
  - Passes MCP tool definitions to agent
  - Captures tool invocations and responses
- Backend returns clean, frontend-ready response

MCP Integration:
- MCP server implemented using Official MCP SDK
- MCP tools exposed:
  - add_task
  - list_tasks
  - complete_task
  - delete_task
  - update_task
- MCP tools:
  - Are stateless
  - Persist state via SQLModel + Neon PostgreSQL
  - Enforce user ownership on every operation
Database models:
- Task:
  user_id, id, title, description, completed, created_at, updated_at
- Conversation:
  user_id, id, created_at, updated_at
- Message:
  user_id, id, conversation_id, role (user/assistant), content, created_at

Conversation flow (stateless request cycle):
1. Frontend sends message to chat endpoint
2. Backend verifies JWT and user identity
3. Conversation history is fetched from database
4. User message is stored
5. Agent is executed with history + new message
6. Agent invokes MCP tools if needed
7. Assistant response is stored
8. Backend returns response to frontend
9. Server holds no in-memory state

Agent behavior rules:
- Detect user intent from natural language
- Use MCP tools for all task operations
- Never access database directly
- Always confirm task actions in response
- Gracefully handle errors and missing tasks

Security constraints:
- JWT authentication required for chat endpoint
- Authenticated user must match {user_id} in URL
- Frontend must include Authorization Bearer token
- MCP tools must enforce user isolation
- No cross-user data access

Frontend integration constraints:
- Backend response must be compatible with ChatKit UI
- No frontend business logic inside agent
- Frontend remains thin client
- Backend is single source of truth
Not building:
- Streaming responses
- Voice interaction
- Multi-agent coordination
- Non-task conversational features
- External APIs beyond MCP

Timeline:
- Must be completed within Phase-III Spec-4 window
```

## Response snapshot

Created a comprehensive specification for the AI Chatbot Backend & Frontend Integration feature. The specification includes:

- User scenarios prioritized by importance (P1-P2) with acceptance criteria
- Functional requirements (FR-001 through FR-010) covering the core functionality
- Key entities (Task, Conversation, Message) with their attributes
- Success criteria (SC-001 through SC-006) with measurable outcomes
- Edge cases addressing potential error conditions

The specification adheres to the stateless architecture requirements with JWT authentication, MCP tool integration, and proper user data isolation. It covers the complete flow from frontend chat interaction to AI processing and MCP tool invocation.

## Outcome

- ✅ Impact: High - Created detailed specification for AI-powered chatbot backend with MCP integration
- 🧪 Tests: None required for specification creation
- 📁 Files: Created spec at specs/001-ai-chatbot-backend/spec.md and checklist at specs/001-ai-chatbot-backend/checklists/requirements.md
- 🔁 Next prompts: Ready for planning phase (/sp.plan) to design implementation
- 🧠 Reflection: Specification comprehensively covers all requirements while maintaining focus on user value

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Begin planning phase for implementation