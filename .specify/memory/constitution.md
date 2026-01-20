# AI-Powered Full-Stack Todo Application Constitution (Hackathon Phase III)

## Core Principles

### I. Strict Spec-Driven Development
All development MUST follow the Agentic Dev Stack workflow exclusively:
- Write Spec → Generate Plan → Break into Tasks → Implement with Claude Code
- No manual coding is permitted; all code must originate from AI-assisted implementation
- Every feature MUST originate from a written specification document
- The workflow MUST be followed for every feature increment

**Rationale**: Ensures consistency, traceability, and reviewability of all changes through structured artifacts.

### II. Statelessness with Persistent State
The system MUST maintain stateless server architecture while ensuring persistent data:
- All AI behavior MUST be defined through written specifications
- AI agents MUST use MCP tools for all task operations (no direct DB access)
- MCP tools MUST be stateless and persist state only via database
- Chat endpoint MUST be stateless across requests
- Conversation context MUST be reconstructed from database on each request
- All tool definitions MUST be explicit and versioned

**Rationale**: Ensures horizontal scalability while maintaining data persistence and deterministic AI behavior.

### III. Security-First Design
The system MUST implement proper authentication and user data isolation:
- All chat requests MUST require valid JWT token
- User identity MUST be verified and matched with request user_id
- MCP tools MUST enforce user ownership
- No cross-user data access MUST be allowed
- No in-memory session storage is permitted
- All API endpoints MUST require a valid JWT token for access
- Requests without a valid token MUST return 401 Unauthorized
- User ownership enforcement MUST be applied on every API operation
- Each user MUST only access their own tasks and data
- JWT secret MUST be shared between frontend and backend via environment variable only

**Rationale**: Multi-user applications require strict security boundaries to protect user data and ensure compliance with privacy regulations.

### IV. Deterministic AI Behavior
The AI system MUST exhibit predictable and reproducible behavior:
- AI agents MUST select correct MCP tools based on user intent
- Natural-language processing MUST reliably map to appropriate task operations
- Tool calls MUST be logged clearly for debugging and traceability
- Conversation continuity MUST be maintained after server restart
- MCP server MUST expose task operations as tools in a consistent manner

**Rationale**: Predictable AI behavior is essential for user trust and system reliability.

### V. Scalability and Production Readiness
The architecture MUST be production capable and horizontally scalable:
- Separate frontend and backend services with clear API contracts
- RESTful API standards MUST be followed for all endpoints (stateless chat API: POST /api/{user_id}/chat)
- Database schema MUST support future growth and feature additions
- Code organization MUST facilitate maintenance and extension
- No hidden state inside agents or MCP server
- No direct database access by AI agent
- Backend MUST remain horizontally scalable

**Rationale**: Applications built with scalability in mind can grow with user needs without complete rewrites.

### VI. Clarity and Traceability
All artifacts MUST be well-structured and navigable:
- Specifications MUST clearly state requirements and acceptance criteria
- Plans MUST document technical decisions and trade-offs
- Tasks MUST be atomic, testable, and independently implementable
- Implementation MUST include inline documentation for complex logic
- All chat interactions MUST be stateless and resumable
- Task operations MUST remain consistent with Phase I & II
- Clear logging of tool calls and agent responses

**Rationale**: Clear documentation enables effective review, iteration, and knowledge transfer.

## Technology Constraints

This project uses a strictly defined technology stack:

| Layer | Technology |
|-------|------------|
| Frontend | OpenAI ChatKit |
| Backend | Python FastAPI |
| AI Framework | OpenAI Agents SDK |
| MCP Server | Official MCP SDK |
| ORM | SQLModel |
| Database | Neon Serverless PostgreSQL |
| Authentication | Better Auth with JWT token issuance + verification |
| Architecture | Frontend ↔ FastAPI ↔ Agents ↔ MCP ↔ Database |

**Rationale**: Prevents technology sprawl and ensures consistent implementation across all agents.

## Functional Requirements

The system MUST implement:

1. **Natural-Language Todo Management**: Users can create, list, update, complete, and delete tasks using natural language
2. **Stateless Chat API Endpoint**: POST /api/{user_id}/chat with proper authentication
3. **Persistent Conversation and Message History**: All conversations stored in database
4. **MCP Server with Task Operations**: Exposing task operations as tools to AI agents
5. **AI Agent Tool Selection**: Reliable selection of correct tools based on user intent
6. **Friendly Confirmations**: Appropriate feedback after every action
7. **Graceful Error Handling**: Proper responses for task not found, invalid input, auth failure
8. **Conversation Continuity**: Maintaining context after server restart
9. **Responsive Modern UI**: Frontend consuming backend API with user-friendly interface
10. **User Authentication**: Signup and Login using Better Auth
11. **JWT Validation Middleware**: Backend validates tokens on every request
12. **User Task Isolation**: Backend filters data to return only authenticated user's tasks

**Rationale**: These requirements define the minimum viable product for the Hackathon evaluation while maintaining consistency with previous phases.

## Security Requirements

- All chat requests require valid JWT token in `Authorization: Bearer <token>` header
- Invalid or missing tokens result in 401 Unauthorized response
- JWT tokens MUST have an expiry strategy to limit exposure
- Shared JWT secret stored in `.env` file, never hardcoded
- User ownership verified on every database query operation
- User identity must be verified and matched with request user_id
- MCP tools must enforce user ownership
- No cross-user data access permitted
- All chat and MCP interactions require authentication

**Rationale**: Security requirements protect user data and demonstrate production-quality implementation with proper user isolation.

## Development Workflow

All development MUST follow this sequence:

1. **Specification Phase** (`/sp.spec`): Document feature requirements, user stories, and acceptance criteria
2. **Planning Phase** (`/sp.plan`): Generate architectural plan with technology decisions and project structure
3. **Task Breakdown** (`/sp.tasks`): Create atomic, testable tasks from the plan
4. **Implementation Phase**: Execute tasks using Claude Code with Red-Green-Refactor cycle
5. **Documentation**: Record all prompts, decisions, and iterations in PHR format

**Rationale**: The structured workflow ensures comprehensive coverage and reviewable artifacts.

## Quality Standards

- **Code Quality**: Follow language-specific best practices; no hardcoded values except in `.env`
- **Error Handling**: All error paths MUST be handled with appropriate messages
- **Testing**: Each task MUST have verifiable acceptance criteria
- **Responsiveness**: UI MUST work on mobile, tablet, and desktop viewports
- **API Design**: RESTful conventions MUST be followed (proper HTTP methods, status codes)
- **Statelessness**: Backend services MUST remain stateless across requests
- **Authentication**: All interactions MUST enforce proper authentication
- **Traceability**: All AI interactions and tool calls MUST be logged clearly

**Rationale**: Quality standards ensure the application meets professional development expectations while maintaining the required stateless architecture.

## Governance

This constitution SUPERSEDES all other development practices for this project.

**Amendment Process**: Changes require documentation of rationale, impact assessment, and migration plan.

**Compliance Review**: All pull requests and implementations MUST verify compliance with constitution principles.

**Constitution Check**: Before Phase 0 research and after Phase 1 design, verify:
- Technology stack compliance
- Security requirements addressed
- User isolation enforced
- Documentation artifacts generated
- Statelessness requirements met
- AI behavior determinism maintained
- Horizontal scalability preserved

**Version**: 2.0.0 | **Ratified**: 2025-01-08 | **Last Amended**: 2026-01-20
