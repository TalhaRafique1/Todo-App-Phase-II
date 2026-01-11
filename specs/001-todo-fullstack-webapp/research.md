# Research: Full-Stack Todo Web Application

## Better Auth Next.js App Router Integration

**Decision**: Use Better Auth with Next.js App Router using client-side providers and server actions pattern.

**Rationale**: Better Auth provides a clean abstraction over authentication flows. For Next.js App Router, the recommended pattern is:
- Client components handle form submission and auth state
- Server actions for secure server-side operations
- Better Auth hooks for session management

**Implementation Pattern**:
```typescript
// lib/auth.ts
import { createAuth } from "better-auth"

export const auth = createAuth({
  plugins: [...],
  advanced: {
    cookiePrefix: "todo-app",
  },
})
```

**Integration Points**:
- `useSession` hook for client-side session access
- `auth.callbacks` for protecting routes
- `signIn`/`signOut` functions for auth operations

## FastAPI JWT Verification Middleware

**Decision**: Use python-jose for JWT encoding/decoding with fastapi Depends for route protection.

**Rationale**: python-jose is the standard JWT library for Python. FastAPI's dependency injection makes it clean to verify tokens per route.

**Implementation Pattern**:
```python
# utils/jwt.py
from jose import jwt, JWTError
from fastapi import HTTPException, status

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

**Middleware Approach**:
- Create auth dependency: `get_current_user(token: str)`
- Apply to protected routes: `@app.get("/tasks", dependencies=[Depends(get_current_user)])`

## SQLModel Neon PostgreSQL Connection

**Decision**: Use SQLModel with psycopg3 driver for Neon Serverless PostgreSQL.

**Rationale**: SQLModel combines Pydantic and SQLAlchemy, providing type-safe ORM. Neon requires sslmode=require for connections.

**Implementation Pattern**:
```python
# database.py
from sqlmodel import SQLModel, create_engine

DATABASE_URL = os.getenv("DATABASE_URL")  # postgresql+psycopg://...
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)
```

**Neon-Specific Considerations**:
- Connection string must include `?sslmode=require`
- Use connection pooling for serverless environments
- Neon automatically manages connection pooling with pooler endpoints

## Security Considerations

### Password Hashing
- Use bcrypt with appropriate work factor (12 rounds)
- Never store plain text passwords

### JWT Token Security
- HS256 algorithm for symmetric signing
- Token expiry: 24 hours (configurable)
- Store in HTTP-only secure cookie or Authorization header

### User Isolation
- Every database query must filter by user_id
- JWT must contain user_id for efficient lookups
- Verify ownership before any modify operation

## Alternatives Considered

| Alternative | Why Rejected |
|-------------|--------------|
| Session-based auth | JWT required by constitution |
| Auth0/Clerk | Must use Better Auth per constitution |
| Raw SQL queries | SQLModel required by constitution |
| Prisma | SQLModel required by constitution |

## References

- [Better Auth Documentation](https://www.better-auth.com/docs)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Neon Serverless PostgreSQL](https://neon.tech/docs/introduction)
- [python-jose Documentation](https://python-jose.readthedocs.io/)
