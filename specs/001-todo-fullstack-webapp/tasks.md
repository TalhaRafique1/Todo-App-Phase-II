---
description: "Task list for Full-Stack Todo Web Application implementation"
---

# Tasks: Full-Stack Todo Web Application

**Input**: Design documents from `/mnt/c/Users/Shoaib Computers/Desktop/Hackathon -2/Phase -II/specs/001-todo-fullstack-webapp/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/openapi.yaml

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/src/`
- **Frontend**: `frontend/src/`
- **Tests**: `backend/tests/`, `frontend/src/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create backend directory structure per plan.md
- [ ] T002 Create requirements.txt with FastAPI, SQLModel, Pydantic, python-jose, bcrypt, psycopg dependencies
- [ ] T003 Create frontend directory structure per plan.md using npx create-next-app@latest
- [ ] T004 Configure package.json with TypeScript, Better Auth, and necessary frontend dependencies
- [ ] T005 Create backend .env.example with DATABASE_URL, JWT_SECRET, BETTER_AUTH_SECRET
- [ ] T006 Create frontend .env.local.example with NEXT_PUBLIC_API_URL and auth secrets

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 [P] Create User model in backend/src/models/user.py with SQLModel table definition
- [ ] T008 [P] Create Task model in backend/src/models/todo.py with SQLModel table definition
- [ ] T009 [P] Export models from backend/src/models/__init__.py
- [ ] T010 Create database connection in backend/src/database.py with SQLModel engine
- [ ] T011 Create init_db() function to auto-create tables on startup
- [ ] T012 [P] Implement JWT utilities in backend/src/utils/jwt.py (encode, decode functions)
- [ ] T013 Create password hashing utilities in backend/src/utils/auth.py (bcrypt hash/verify)
- [ ] T014 Create JWT verification middleware in backend/src/middleware/auth.py
- [ ] T015 Create get_current_user dependency in backend/src/middleware/auth.py
- [ ] T016 Create UserService in backend/src/services/user_service.py (CRUD operations)
- [ ] T017 Create TaskService in backend/src/services/todo_service.py (CRUD with user isolation)
- [ ] T018 Create backend/src/api/__init__.py with router exports
- [ ] T019 Create main FastAPI app in backend/src/main.py with CORS and lifespan events
- [ ] T020 Call init_db() in main.py lifespan to create tables on startup

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - User Account Management (Priority: P1) MVP

**Goal**: Users can register new accounts with email and password

**Independent Test**: POST to /auth/register creates user and returns 201 with token

### Backend Implementation for User Story 1

- [ ] T021 [P] [US1] Create UserCreate schema in backend/src/models/user.py
- [ ] T022 [P] [US1] Create UserResponse schema in backend/src/models/user.py
- [ ] T023 [P] [US1] Create registration endpoint in backend/src/api/auth.py
- [ ] T024 [US1] Implement user registration logic with email uniqueness check
- [ ] T025 [US1] Return JWT token on successful registration

---

## Phase 4: User Story 2 - User Authentication (Priority: P1)

**Goal**: Users can log in and receive JWT tokens

**Independent Test**: POST to /auth/login with valid credentials returns 200 with token

### Backend Implementation for User Story 2

- [ ] T026 [P] [US2] Create Token schema in backend/src/models/user.py
- [ ] T027 [P] [US2] Create login endpoint in backend/src/api/auth.py
- [ ] T028 [US2] Implement login logic with password verification
- [ ] T029 [US2] Return JWT token containing user_id on successful login

---

## Phase 5: User Story 3 - Create Tasks (Priority: P1)

**Goal**: Authenticated users can create new tasks

**Independent Test**: POST to /api/{user_id}/tasks creates task and returns 201

### Backend Implementation for User Story 3

- [ ] T030 [P] [US3] Create TaskCreate schema in backend/src/models/todo.py
- [ ] T031 [P] [US3] Create TaskResponse schema in backend/src/models/todo.py
- [ ] T032 [P] [US3] Create create task endpoint in backend/src/api/todos.py
- [ ] T033 [US3] Implement task creation with user_id from JWT and title validation
- [ ] T034 [US3] Enforce user isolation - only create tasks for authenticated user

---

## Phase 6: User Story 4 - View Tasks (Priority: P1)

**Goal**: Authenticated users can view their task list

**Independent Test**: GET to /api/{user_id}/tasks returns only authenticated user's tasks

### Backend Implementation for User Story 4

- [ ] T035 [P] [US4] Create list tasks endpoint in backend/src/api/todos.py
- [ ] T036 [US4] Implement task listing filtered by user_id from JWT
- [ ] T037 [US4] Handle empty list with appropriate response
- [ ] T038 [P] [US4] Create get single task endpoint in backend/src/api/todos.py
- [ ] T039 [US4] Implement single task retrieval with ownership verification

---

## Phase 7: User Story 5 - Update Tasks (Priority: P1)

**Goal**: Authenticated users can edit task titles

**Independent Test**: PUT to /api/{user_id}/tasks/{id} updates task title

### Backend Implementation for User Story 5

- [ ] T040 [P] [US5] Create TaskUpdate schema in backend/src/models/todo.py
- [ ] T041 [P] [US5] Create update task endpoint in backend/src/api/todos.py
- [ ] T042 [US5] Implement update with title validation and ownership verification
- [ ] T043 [US5] Return 404 if task not found, 403 if not owner

---

## Phase 8: User Story 6 - Toggle Task Completion (Priority: P1)

**Goal**: Authenticated users can toggle task completion status

**Independent Test**: PATCH to /api/{user_id}/tasks/{id}/complete toggles status

### Backend Implementation for User Story 6

- [ ] T044 [P] [US6] Create toggle completion endpoint in backend/src/api/todos.py
- [ ] T045 [US6] Implement completion status toggle with ownership verification
- [ ] T046 [US6] Return updated task with new completion status

---

## Phase 9: User Story 7 - Delete Tasks (Priority: P2)

**Goal**: Authenticated users can delete their tasks

**Independent Test**: DELETE to /api/{user_id}/tasks/{id} removes task

### Backend Implementation for User Story 7

- [ ] T047 [P] [US7] Create delete task endpoint in backend/src/api/todos.py
- [ ] T048 [US7] Implement task deletion with ownership verification
- [ ] T049 [US7] Return 204 on successful deletion, 404 if not found

---

## Phase 10: Frontend Authentication UI

**Goal**: Login and signup pages with Better Auth integration

- [ ] T050 [P] Configure Better Auth in frontend/src/lib/auth.ts
- [ ] T051 [P] Create API client in frontend/src/lib/api.ts with JWT handling
- [ ] T052 [P] Create TypeScript types in frontend/src/types/index.ts
- [ ] T053 Create login page in frontend/src/app/login/page.tsx
- [ ] T054 Create signup page in frontend/src/app/signup/page.tsx
- [ ] T055 [P] Create AuthForm component in frontend/src/components/AuthForm.tsx
- [ ] T056 Create auth callback handling and redirect logic

---

## Phase 11: Frontend Dashboard UI

**Goal**: Task management dashboard with full CRUD UI

- [ ] T057 Create dashboard layout in frontend/src/app/dashboard/layout.tsx
- [ ] T058 Create dashboard page in frontend/src/app/dashboard/page.tsx
- [ ] T059 [P] Create TaskList component in frontend/src/components/TaskList.tsx
- [ ] T060 [P] Create TaskItem component in frontend/src/components/TaskItem.tsx
- [ ] T061 [P] Create TaskForm component in frontend/src/components/TaskForm.tsx
- [ ] T062 [P] Create Header component with logout in frontend/src/components/Header.tsx
- [ ] T063 Implement task creation UI with API integration
- [ ] T064 Implement task list display with completion toggle
- [ ] T065 Implement task editing UI
- [ ] T066 Implement task deletion UI
- [ ] T067 Add responsive CSS in frontend/src/app/globals.css
- [ ] T068 Add loading and error state handling UX

---

## Phase 12: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T069 Add input validation feedback on all forms
- [ ] T070 Add loading spinners during API calls
- [ ] T071 Add error toasts/messages for failed operations
- [ ] T072 Ensure mobile responsiveness across all pages
- [ ] T073 Add empty state messages for new users
- [ ] T074 Create health check endpoint at GET /health
- [ ] T075 Verify database tables exist after init_db()
- [ ] T076 Test user isolation - ensure User A cannot access User B tasks

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-9)**: All depend on Foundational phase completion
  - User stories can proceed in parallel after Phase 2
- **Frontend (Phase 10-11)**: Depends on corresponding backend endpoints
- **Polish (Final Phase)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (Registration)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (Login)**: Can start after Foundational (Phase 2) - Can test independently
- **User Stories 3-6 (Task CRUD)**: Can start after Foundational (Phase 2) - Can test independently
- **User Story 7 (Delete)**: Can start after Foundational (Phase 2) - Can test independently

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational is done, all user stories can start in parallel
- Models within a story marked [P] can run in parallel
- Backend and frontend work can run in parallel after foundational

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "T021 [P] [US1] Create UserCreate schema in backend/src/models/user.py"
Task: "T022 [P] [US1] Create UserResponse schema in backend/src/models/user.py"

# Launch registration endpoint:
Task: "T023 [P] [US1] Create registration endpoint in backend/src/api/auth.py"

# Launch implementation (depends on schemas):
Task: "T024 [US1] Implement user registration logic with email uniqueness check"
```

---

## Implementation Strategy

### MVP First (User Stories 1-2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Registration)
4. Complete Phase 4: User Story 2 (Login)
5. **STOP and VALIDATE**: Test registration and login flow

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test registration → Deploy/Demo
3. Add User Story 2 → Test login → Deploy/Demo
4. Add User Stories 3-6 → Test task CRUD → Deploy/Demo
5. Add User Story 7 → Test delete → Deploy/Demo
6. Add Frontend → Full UI experience → Final Demo

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1-2 (Auth)
   - Developer B: User Stories 3-6 (Task CRUD)
   - Developer C: User Story 7 + Frontend
3. Stories complete and integrate independently

---

## Task Summary

| Category | Count |
|----------|-------|
| Setup | 6 |
| Foundational | 14 |
| User Story 1 | 5 |
| User Story 2 | 4 |
| User Story 3 | 4 |
| User Story 4 | 4 |
| User Story 5 | 4 |
| User Story 6 | 3 |
| User Story 7 | 3 |
| Frontend Auth | 7 |
| Frontend Dashboard | 12 |
| Polish | 8 |
| **Total** | **76** |

### Independent Test Criteria per Story

| Story | Independent Test |
|-------|-----------------|
| US1 | POST /auth/register creates user, returns 201 with token |
| US2 | POST /auth/login returns 200 with valid token for correct credentials |
| US3 | POST /api/{user_id}/tasks creates task, returns 201 |
| US4 | GET /api/{user_id}/tasks returns only authenticated user's tasks |
| US5 | PUT /api/{user_id}/tasks/{id} updates title, returns 200 |
| US6 | PATCH /api/{user_id}/tasks/{id}/complete toggles status |
| US7 | DELETE /api/{user_id}/tasks/{id} returns 204 |

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
