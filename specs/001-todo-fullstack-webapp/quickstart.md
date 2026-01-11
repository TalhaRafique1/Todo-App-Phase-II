# Quickstart Guide: Full-Stack Todo Web Application

## Prerequisites

- Python 3.12 or higher
- Node.js 18 or higher
- Neon PostgreSQL database URL

## Environment Setup

### 1. Database (Neon PostgreSQL)

1. Create account at [neon.tech](https://neon.tech)
2. Create new project with PostgreSQL 15
3. Copy connection string (includes sslmode=require)

### 2. Backend Configuration

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with:
#   DATABASE_URL=postgresql+psycopg://...
#   JWT_SECRET=your-secret-key
#   BETTER_AUTH_SECRET=your-auth-secret
```

### 3. Frontend Configuration

```bash
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.example .env.local
# Edit .env.local with:
#   NEXT_PUBLIC_API_URL=http://localhost:8000
#   JWT_SECRET=your-secret-key (same as backend)
```

## Running the Application

### Start Backend

```bash
cd backend
source venv/bin/activate
uvicorn src.main:app --reload --port 8000
```

- API available at: http://localhost:8000
- API docs at: http://localhost:8000/docs

### Start Frontend

```bash
cd frontend
npm run dev
```

- App available at: http://localhost:3000

## Verification Steps

### 1. Backend Health

```bash
curl http://localhost:8000/health
# Expected: {"status":"healthy"}
```

### 2. API Documentation

Open http://localhost:8000/docs to explore the API using Swagger UI.

### 3. Frontend Access

Open http://localhost:3000 in browser.

### 4. Complete User Flow

1. Click "Sign Up" and create account
2. Verify login succeeds
3. Create a task
4. View task in list
5. Toggle completion
6. Edit task title
7. Delete task
8. Logout

## Troubleshooting

### Database Connection Failed

- Verify DATABASE_URL is correct
- Ensure sslmode=require is in connection string
- Check Neon project is active

### JWT Token Errors

- Verify JWT_SECRET is same in backend and frontend
- Ensure token is not expired
- Check Authorization header format: "Bearer <token>"

### CORS Errors

- Verify frontend URL is in backend CORS origins
- Check browser console for specific CORS messages

## Development Commands

### Backend Tests

```bash
cd backend
source venv/bin/activate
pytest tests/ -v
```

### Frontend Tests

```bash
cd frontend
npm test
```

### Linting

```bash
# Backend
cd backend
source venv/bin/activate
ruff check src/

# Frontend
cd frontend
npm run lint
```
