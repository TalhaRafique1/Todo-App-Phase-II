# Implementation Plan: Full-Stack Todo Web Application

**Branch**: `001-todo-fullstack-webapp` | **Date**: 2026-01-08 | **Spec**: [spec.md](./spec.md)

## Summary

Transform a console Todo application into a fully functional modern multi-user full-stack web application with secure REST API, persistent database storage, JWT-based authentication, and responsive frontend UI.

## Technical Context

**Language/Version**: Python 3.12 (FastAPI backend), TypeScript (Next.js 16+ frontend)
**Primary Dependencies**: FastAPI, SQLModel, Pydantic, Next.js 16+, Better Auth
**Storage**: Neon Serverless PostgreSQL with SQLModel ORM
**Testing**: pytest (backend), Jest/React Testing Library (frontend)
**Target Platform**: Web browser (desktop, tablet, mobile)
**Project Type**: Full-stack web application with separate frontend and backend
**Performance Goals**: API responses under 2 seconds, user isolation enforced 100% of time
**Constraints**: JWT authentication required for all endpoints, user data isolation mandatory
**Scale/Scope**: Single-tenant database, multi-user application, hackathon timeline

## Constitution Check

**GATE**: Must pass before Phase 0 research. Re-check after Phase 1 design.

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Technology stack compliance | PASS | Spec mandates Next.js 16+ App Router, FastAPI, SQLModel, Neon PostgreSQL, Better Auth + JWT |
| Security requirements addressed | PASS | JWT authentication, user isolation, 401 for invalid tokens defined in spec |
| User isolation enforced | PASS | All FRs require authenticated user, FR-006 and FR-010 explicitly enforce user-only access |
| Documentation artifacts generated | PASS | Created: research.md, data-model.md, contracts/openapi.yaml, quickstart.md |
| No manual coding requirement | PASS | Implementation will follow Agentic Dev Stack workflow exclusively |

**Overall Gate Status**: PASS - All checks complete

## Post-Design Constitution Check

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Technology stack compliance | PASS | Plan specifies Next.js 16+ App Router, FastAPI, SQLModel, Neon PostgreSQL, Better Auth + JWT |
| Security requirements addressed | PASS | JWT authentication, user isolation via foreign key + query filtering, 401/403 responses defined |
| User isolation enforced | PASS | All task endpoints filter by user_id from JWT, middleware verifies ownership |
| Documentation artifacts generated | PASS | research.md, data-model.md, contracts/openapi.yaml, quickstart.md all created |
| No manual coding requirement | PASS | Implementation will follow Agentic Dev Stack workflow via /sp.tasks |

## Phase 0: Research

### Unknowns to Resolve

1. **Better Auth integration with Next.js App Router** - Need to research proper configuration patterns
2. **JWT verification in FastAPI middleware** - Need to confirm shared secret handling approach
3. **SQLModel with Neon Serverless PostgreSQL** - Need to verify connection patterns and pool settings

### Research Tasks

- Research Better Auth Next.js App Router integration patterns
- Research FastAPI JWT verification middleware best practices
- Research SQLModel Neon PostgreSQL connection and table creation patterns

## Phase 1: Data Model Design

### Entities

#### User

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key | Unique user identifier |
| email | String(255) | Unique, Index, Not Null | User email address |
| hashed_password | String(255) | Not Null | Bcrypt hashed password |
| created_at | DateTime | Default now | Account creation timestamp |
| updated_at | DateTime | Default now | Last update timestamp |

#### Task

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key | Unique task identifier |
| user_id | UUID | Foreign Key, Index, Not Null | Owner user identifier |
| title | String(255) | Not Null, Min 1 char | Task title |
| completed | Boolean | Default False | Completion status |
| created_at | DateTime | Default now | Task creation timestamp |
| updated_at | DateTime | Default now | Last update timestamp |

### Relationships

- User 1:N Task (one user can have many tasks, each task belongs to one user)

## Phase 2: API Contracts

### Authentication Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | /api/auth/register | Create new user account |
| POST | /api/auth/login | Authenticate user and return JWT token |

### Task Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /api/{user_id}/tasks | List all tasks for user |
| POST | /api/{user_id}/tasks | Create new task for user |
| GET | /api/{user_id}/tasks/{id} | Get specific task |
| PUT | /api/{user_id}/tasks/{id} | Update task title |
| PATCH | /api/{user_id}/tasks/{id}/complete | Toggle completion status |
| DELETE | /api/{user_id}/tasks/{id} | Delete task |

### Error Responses

| Status | Description |
|--------|-------------|
| 401 | Missing or invalid JWT token |
| 403 | Attempt to access another user's resources |
| 404 | Resource not found |
| 422 | Validation error |
| 500 | Internal server error |

## Project Structure

### Backend

```text
backend/
├── src/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry
│   ├── config.py               # Configuration management
│   ├── database.py             # SQLModel engine and session
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py             # Authentication endpoints
│   │   └── todos.py            # Task CRUD endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py             # User model
│   │   └── todo.py             # Task model
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py     # Authentication logic
│   │   └── todo_service.py     # Task business logic
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── auth.py             # JWT verification middleware
│   └── utils/
│       ├── __init__.py
│       └── jwt.py              # JWT encoding/decoding
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_todos.py
├── .env                        # Environment variables
├── requirements.txt
└── run.py                      # Application runner
```

### Frontend

```text
frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx          # Root layout with providers
│   │   ├── page.tsx            # Home page (redirect to dashboard or login)
│   │   ├── globals.css         # Global styles
│   │   ├── login/
│   │   │   └── page.tsx        # Login page
│   │   ├── signup/
│   │   │   └── page.tsx        # Signup page
│   │   └── dashboard/
│   │       ├── layout.tsx      # Dashboard layout with auth check
│   │       └── page.tsx        # Task list and management
│   ├── components/
│   │   ├── AuthForm.tsx        # Login/Signup form component
│   │   ├── TaskList.tsx        # Task list component
│   │   ├── TaskItem.tsx        # Individual task component
│   │   ├── TaskForm.tsx        # Create/edit task form
│   │   └── Header.tsx          # App header with logout
│   ├── lib/
│   │   ├── api.ts              # API client with JWT handling
│   │   └── auth.ts             # Better Auth configuration
│   └── types/
│       └── index.ts            # TypeScript type definitions
├── .env.local                  # Environment variables
├── package.json
└── next.config.js
```

## Complexity Tracking

> This section documents deviations from the standard project structure justified by the feature requirements.

| Deviation | Justification | Simpler Alternative Rejected Because |
|-----------|---------------|--------------------------------------|
| Separate frontend/backend directories | Required by technology stack (Next.js + FastAPI) | N/A - architecture mandated by constitution |
| JWT middleware for all endpoints | Security requirement - user isolation mandatory | N/A - security requirement from constitution |
| Better Auth integration | Required by constitution for authentication | N/A - authentication method mandated |

## Execution Phases

### Phase 1: Backend Foundation
1. Set up FastAPI project structure
2. Configure SQLModel with Neon PostgreSQL
3. Create User and Task models
4. Implement authentication endpoints
5. Implement JWT middleware
6. Implement task CRUD endpoints
7. Add validation and error handling

### Phase 2: Frontend Foundation
1. Set up Next.js 16+ project
2. Configure Better Auth
3. Build authentication pages (login/signup)
4. Build dashboard with task list
5. Implement task CRUD UI
6. Add responsive styling
7. Integrate with backend API

### Phase 3: Integration and Polish
1. End-to-end testing
2. User isolation verification
3. Performance optimization
4. UI polish and error handling
5. Final review against success criteria

## Quickstart

### Prerequisites
- Python 3.12+
- Node.js 18+
- Neon PostgreSQL database URL

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
# Configure .env with DATABASE_URL and JWT_SECRET
uvicorn src.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
# Configure .env.local with API_URL and auth secrets
npm run dev
```

### Verify
- Backend health: `GET http://localhost:8000/health`
- Frontend: `http://localhost:3000`
