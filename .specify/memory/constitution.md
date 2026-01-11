# Full-Stack Spec-Driven Todo Web Application Constitution

## Core Principles

### I. Strict Spec-Driven Development
All development MUST follow the Agentic Dev Stack workflow exclusively:
- Write Spec → Generate Plan → Break into Tasks → Implement with Claude Code
- No manual coding is permitted; all code must originate from AI-assisted implementation
- Every feature MUST originate from a written specification document
- The workflow MUST be followed for every feature increment

**Rationale**: Ensures consistency, traceability, and reviewability of all changes through structured artifacts.

### II. Reliability
The application MUST run end-to-end without breaks:
- All REST endpoints MUST be operational and return appropriate responses
- Backend and frontend MUST fully integrate without runtime failures
- Database connections MUST handle connection pooling and retries gracefully
- Proper error handling MUST be implemented at every layer

**Rationale**: Users expect a working application; reliability builds trust and enables meaningful evaluation.

### III. Security
The system MUST implement proper authentication and user data isolation:
- All API endpoints MUST require a valid JWT token for access
- Requests without a valid token MUST return 401 Unauthorized
- User ownership enforcement MUST be applied on every API operation
- Each user MUST only access their own tasks and data
- JWT secret MUST be shared between frontend and backend via environment variable only

**Rationale**: Multi-user applications require strict security boundaries to protect user data.

### IV. Scalability Readiness
The architecture MUST be production capable:
- Separate frontend and backend services with clear API contracts
- RESTful API standards MUST be followed for all endpoints
- Database schema MUST support future growth and feature additions
- Code organization MUST facilitate maintenance and extension

**Rationale**: Applications built with scalability in mind can grow with user needs without complete rewrites.

### V. Clarity
All artifacts MUST be well-structured and navigable:
- Specifications MUST clearly state requirements and acceptance criteria
- Plans MUST document technical decisions and trade-offs
- Tasks MUST be atomic, testable, and independently implementable
- Implementation MUST include inline documentation for complex logic

**Rationale**: Clear documentation enables effective review, iteration, and knowledge transfer.

## Technology Constraints

This project uses a strictly defined technology stack:

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 16+ (App Router) |
| Backend | Python FastAPI |
| ORM | SQLModel |
| Database | Neon Serverless PostgreSQL |
| Authentication | Better Auth with JWT token issuance + verification |

**Rationale**: Prevents technology sprawl and ensures consistent implementation across all agents.

## Functional Requirements

The system MUST implement:

1. **Full Todo Web App (Multi-user)**: Users can create, read, update, and delete their own tasks
2. **Complete REST API**: CRUD operations plus completion toggle functionality
3. **Persistent Storage**: All data stored in Neon Serverless PostgreSQL
4. **User Authentication**: Signup and Login using Better Auth
5. **JWT Validation Middleware**: Backend validates tokens on every request
6. **User Task Isolation**: Backend filters data to return only authenticated user's tasks
7. **Responsive Modern UI**: Frontend consuming backend API with user-friendly interface

**Rationale**: These requirements define the minimum viable product for the Hackathon evaluation.

## Security Requirements

- All endpoints require valid JWT token in `Authorization: Bearer <token>` header
- Invalid or missing tokens result in 401 Unauthorized response
- JWT tokens MUST have an expiry strategy to limit exposure
- Shared JWT secret stored in `.env` file, never hardcoded
- User ownership verified on every database query operation

**Rationale**: Security requirements protect user data and demonstrate production-quality implementation.

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

**Rationale**: Quality standards ensure the application meets professional development expectations.

## Governance

This constitution SUPERSEDES all other development practices for this project.

**Amendment Process**: Changes require documentation of rationale, impact assessment, and migration plan.

**Compliance Review**: All pull requests and implementations MUST verify compliance with constitution principles.

**Constitution Check**: Before Phase 0 research and after Phase 1 design, verify:
- Technology stack compliance
- Security requirements addressed
- User isolation enforced
- Documentation artifacts generated

**Version**: 1.0.0 | **Ratified**: 2025-01-08 | **Last Amended**: 2025-01-08
