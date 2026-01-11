---
id: "001"
title: "Project Constitution for Full-Stack Todo Web Application"
stage: "constitution"
date: "2026-01-08"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "main"
user: "User"
command: "/sp.constitution"
labels: [constitution,project-principles,sdd]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - ".specify/memory/constitution.md"
tests:
  - "none"
---

## Prompt

/sp.constitution

Project: Full-Stack Spec-Driven Todo Web Application (Hackathon Phase II)

Core principles:
- Strict Spec-Driven Development (No manual coding — only Agentic workflow)
- Reliability (application must run end-to-end without breaks)
- Security (proper authentication + user isolation)
- Scalability readiness (production capable architecture)
- Clarity (well-structured specs, plans, and implementation steps)

Key standards:
- Development must strictly follow workflow:
  Write Spec → Generate Plan → Break into Tasks → Implement with Claude Code
- Every feature must originate from a written specification
- API must follow proper REST standards
- Authentication must enforce secure JWT verification
- UI must be responsive and user-friendly
- Backend, Frontend, DB, and Auth must fully integrate
- No hardcoding users — multi-user real system

Technology Constraints:
- Frontend: Next.js 16+ (App Router)
- Backend: FastAPI (Python)
- ORM: SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT token issuance + verification
- Architecture: Separate Frontend & Backend services with secure communication

Functional Requirements:
- Implement full Todo Web App (multi-user)
- Build complete REST API with CRUD + completion toggle
- Connect with PostgreSQL persistent storage
- Implement Signup + Login using Better Auth
- Secure backend using JWT validation middleware
- Ensure each user only accesses their own tasks
- Build responsive modern UI consuming backend API

Security Requirements:
- All endpoints require valid JWT token
- Requests without valid token → 401 Unauthorized
- User ownership enforcement on every API operation
- Shared JWT secret between frontend & backend via env variable
- Tokens must have expiry strategy

Constraints:
- Must follow Agentic Dev Stack flow
- No manual coding — only AI-assisted implementation
- Architecture must be production capable
- Proper error handling and validation required
- Clear documentation of process, prompts, and outputs

Success Criteria:
- Application fully works end-to-end
- All REST endpoints operational
- JWT auth works and enforces isolation
- Data stored persistently in Neon PostgreSQL
- UI is responsive and functional
- System passes review of correctness, security, and workflow discipline
- Fully demonstrable working project

## Response snapshot

PHR created for constitution input. Project constitution recorded with core principles for Spec-Driven Development workflow. Document establishes technology stack (Next.js 16+, FastAPI, SQLModel, Neon PostgreSQL, Better Auth), development standards, security requirements, and success criteria for the Hackathon Phase II Todo Web Application project.

## Outcome

- ✅ Impact: Constitution established as authoritative source for project principles, technology constraints, and development workflow
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: Next step is to write feature specification for Todo Web App basic features
- 🧠 Reflection: Constitution phase complete - project now has documented principles to guide all subsequent spec, plan, and implementation work

## Evaluation notes (flywheel)

- Failure modes observed: "none"
- Graders run and results (PASS/FAIL): "none"
- Prompt variant (if applicable): "none"
- Next experiment (smallest change to try): "none"
