# Full-Stack Todo Web Application

A modern multi-user todo application built with Spec-Driven Development workflow.

## Tech Stack

- **Frontend**: Next.js 16+ (App Router), TypeScript, TailwindCSS
- **Backend**: FastAPI (Python), SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT

## Features

- User registration and login
- Create, read, update, delete todos
- Toggle task completion
- Responsive design (desktop, tablet, mobile)
- JWT-based authentication with user isolation

## Project Structure

```
Phase -II/
├── backend/
│   ├── src/
│   │   ├── api/          # FastAPI routes
│   │   ├── middleware/   # Auth & error handling
│   │   ├── models/       # SQLModel entities
│   │   ├── services/     # Business logic
│   │   └── utils/        # Helpers (JWT, password)
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── app/          # Next.js pages
│   │   ├── components/   # React components
│   │   ├── lib/          # Auth configuration
│   │   ├── services/     # API client
│   │   └── types/        # TypeScript types
│   ├── package.json
│   └── .env.local
└── specs/                # Specification documents
```

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Neon PostgreSQL database

### Database Setup

1. **Get your Neon PostgreSQL connection string**:
   - Log into [console.neon.tech](https://console.neon.tech)
   - Go to your project
   - Click "Connection Details" or "Connect"
   - Select "Python" and copy the connection string

2. **Update your .env file** with the actual connection string

3. **Initialize database tables** (run after setting up environment variables):
```bash
# From the backend directory
cd backend
python init_db.py
```
Alternatively, the tables will be created automatically when you start the application for the first time.

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Neon PostgreSQL credentials and JWT secrets

# Run the server
uvicorn src.main:app --reload
```

Backend runs at: http://localhost:8000
API Docs: http://localhost:8000/docs

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.example .env.local
# Edit .env.local with your API URL

# Run development server
npm run dev
```

Frontend runs at: http://localhost:3000

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/register | Register new user |
| POST | /api/auth/login | Login user |
| GET | /api/auth/me | Get current user |

### Todos

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/{user_id}/tasks | List all tasks |
| POST | /api/{user_id}/tasks | Create task |
| GET | /api/{user_id}/tasks/{id} | Get single task |
| PUT | /api/{user_id}/tasks/{id} | Update task |
| PATCH | /api/{user_id}/tasks/{id}/complete | Toggle completion |
| DELETE | /api/{user_id}/tasks/{id} | Delete task |

All endpoints require JWT token in Authorization header.

## Troubleshooting

### Database Issues:
- Make sure your Neon PostgreSQL connection string is correct
- Verify that your database is not paused in the Neon dashboard
- Ensure SSL is enabled in your connection string
- Run `python init_db.py` to manually create tables

### Authentication Issues:
- Ensure JWT_SECRET and BETTER_AUTH_SECRET match between frontend and backend
- Check that CORS is properly configured

### Frontend/Backend Communication:
- Verify NEXT_PUBLIC_API_URL points to the correct backend URL
- Ensure backend is running when accessing frontend

## Development Workflow

This project follows Spec-Driven Development:

1. **Write Spec** (`/sp.specify`) - Define requirements
2. **Generate Plan** (`/sp.plan`) - Design architecture
3. **Break into Tasks** (`/sp.tasks`) - Create implementation tasks
4. **Implement** (`/sp.implement`) - Execute tasks with Claude Code

## Environment Variables

### Backend (.env)

```env
DATABASE_URL=postgresql://user:pass@host/db
JWT_SECRET=your-secret-key
BETTER_AUTH_SECRET=your-better-auth-secret
```

### Frontend (.env.local)

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
BETTER_AUTH_SECRET=your-better-auth-secret
```
