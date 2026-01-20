# Tasks: AI Chatbot Backend & Agent Integration

**Feature**: 004-ai-chatbot-backend
**Generated**: 2026-01-20
**Based on**: spec.md, plan.md, data-model.md, contracts/chat-api.yaml

## Phase 1: Setup Tasks

**Goal**: Prepare environment and dependencies for AI chatbot implementation

- [X] T001 Create MCP server directory structure at mcp-server/
- [X] T002 Update backend requirements.txt with OpenAI and MCP SDK dependencies
- [X] T003 Update frontend package.json if needed for chat features
- [X] T004 Create MCP server requirements.txt with MCP SDK dependencies

## Phase 2: Foundational Tasks

**Goal**: Implement foundational components needed by all user stories

- [X] T005 Create Conversation model at backend/src/models/conversation.py
- [X] T006 Create Message model at backend/src/models/message.py
- [X] T007 Update database schema to include conversation and message tables
- [X] T008 Create conversations service at backend/src/services/conversations.py
- [X] T009 Create AI agent service at backend/src/services/ai_agent.py
- [X] T010 Create MCP server structure at mcp-server/src/
- [X] T011 Implement MCP tool validation at mcp-server/src/tools/validation.py

## Phase 3: [US1] Natural Language Task Management via Chat (P1)

**Goal**: Enable users to interact with AI chatbot to manage tasks using natural language

**Independent Test**: Send natural language command to chat endpoint and verify appropriate task is created in database, demonstrating AI's understanding and tool usage.

- [X] T012 [P] [US1] Create task tools for MCP server at mcp-server/src/tools/task_tools.py
- [X] T013 [P] [US1] Implement add_task MCP tool with user ownership validation
- [X] T014 [P] [US1] Implement list_tasks MCP tool with user ownership validation
- [X] T015 [P] [US1] Implement complete_task MCP tool with user ownership validation
- [X] T016 [P] [US1] Implement delete_task MCP tool with user ownership validation
- [X] T017 [P] [US1] Implement update_task MCP tool with user ownership validation
- [X] T018 [US1] Create MCP server implementation at mcp-server/src/server.py
- [X] T019 [US1] Configure MCP server to use task tools
- [X] T020 [US1] Update AI agent service to register MCP tools
- [X] T021 [US1] Configure AI agent instructions for task-related intents
- [X] T022 [US1] Create chat API endpoint at backend/src/api/chat.py
- [X] T023 [US1] Implement POST /api/{user_id}/chat endpoint handler
- [X] T024 [US1] Add JWT verification to chat endpoint
- [X] T025 [US1] Add user identity matching to chat endpoint
- [X] T026 [US1] Implement conversation history loading in chat endpoint
- [X] T027 [US1] Implement user message storage in chat endpoint
- [X] T028 [US1] Implement AI agent execution with message history
- [X] T029 [US1] Implement assistant response storage
- [X] T030 [US1] Return response in ChatKit-compatible format
- [X] T031 [US1] Update main.py to include chat router

## Phase 4: [US2] Secure Chat Interaction with Authentication (P1)

**Goal**: Ensure chat interactions are properly authenticated with user isolation

**Independent Test**: Send authenticated requests with valid JWT tokens and verify only user's own tasks are accessible, demonstrating proper authentication and authorization.

- [X] T032 [P] [US2] Enhance JWT authentication middleware for chat routes
- [X] T033 [P] [US2] Add user isolation enforcement to conversations service
- [X] T034 [US2] Implement 401 Unauthorized response for invalid tokens
- [X] T035 [US2] Implement 403 Forbidden response for mismatched user_ids
- [X] T036 [US2] Add comprehensive JWT validation to chat endpoint
- [X] T037 [US2] Implement cross-user data access prevention
- [X] T038 [US2] Add security tests for chat endpoint

## Phase 5: [US3] Persistent Conversation History (P2)

**Goal**: Maintain conversation history across requests for natural conversation flow

**Independent Test**: Send multiple messages in sequence and verify conversation history is preserved and accessible in subsequent requests.

- [X] T039 [P] [US3] Implement conversation creation in conversations service
- [X] T040 [P] [US3] Implement conversation retrieval in conversations service
- [X] T041 [P] [US3] Implement message creation in conversations service
- [X] T042 [P] [US3] Implement message retrieval in conversations service
- [X] T043 [US3] Update chat endpoint to create new conversations when needed
- [X] T044 [US3] Update chat endpoint to maintain conversation context
- [X] T045 [US3] Implement conversation state reconstruction from database
- [X] T046 [US3] Test conversation persistence after server restart

## Phase 6: [US4] Task Operation Confirmation and Feedback (P2)

**Goal**: Provide clear feedback to users about AI task operations

**Independent Test**: Perform task operations via chat and verify AI provides clear, understandable feedback about results.

- [X] T047 [P] [US4] Update AI agent to provide friendly confirmations
- [X] T048 [P] [US4] Implement error handling in AI agent for missing tasks
- [X] T049 [US4] Enhance chat endpoint to return tool call information
- [X] T050 [US4] Add proper response formatting for task confirmations
- [X] T051 [US4] Implement graceful error handling for task operations

## Phase 7: Polish & Cross-Cutting Concerns

**Goal**: Complete implementation with error handling, testing, and documentation

- [X] T052 Add comprehensive error handling for edge cases
- [X] T053 Implement handling for malformed JWT tokens
- [X] T054 Add handling for invalid natural language commands
- [X] T055 Implement retry logic for database availability issues
- [X] T056 Add logging for tool calls and agent responses
- [X] T057 Create tests for chat endpoint functionality
- [X] T058 Create integration tests for AI agent and MCP tools
- [X] T059 Update frontend to support chat interface
- [X] T060 Add performance monitoring for response times
- [X] T061 Update documentation with new API endpoints
- [X] T062 Conduct end-to-end testing of all user stories

## Dependencies

**User Story Dependency Graph**:
- US2 (Security) → US1 (Natural Language) [Security must be implemented first]
- US3 (History) → US1 (Natural Language) [History needed for natural language flow]
- US4 (Feedback) → US1 (Natural Language) [Feedback needed for task operations]

**Story Completion Order**:
1. US2 (Security) - Foundation for all other stories
2. US1 (Natural Language) - Core functionality
3. US3 (History) - Enhancement to core functionality
4. US4 (Feedback) - User experience improvement

## Parallel Execution Examples

**Per Story**:
- **US1**: T012-T017 (MCP tools) can run in parallel
- **US2**: JWT middleware and service-level security can run in parallel
- **US3**: Conversation and message services can run in parallel
- **US4**: AI agent updates and response formatting can run in parallel

## Implementation Strategy

**MVP Scope (Just US1)**: Tasks T001-T031 provide the core functionality for natural language task management with basic security.

**Incremental Delivery**:
- Sprint 1: Phase 1-2 (Setup and Foundation)
- Sprint 2: Phase 3 (Core US1 functionality)
- Sprint 3: Phase 4-5 (Security and History)
- Sprint 4: Phase 6-7 (Feedback and Polish)