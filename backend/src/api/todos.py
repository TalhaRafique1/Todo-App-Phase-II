"""Todo API endpoints with CRUD operations."""

from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials
from sqlmodel import Session
from ..middleware.auth import security
from ..database import get_db
from ..models.todo import Task, TaskCreate, TaskUpdate, TaskResponse
from ..services.todo_service import create_todo_service
from ..middleware.auth import get_current_user, verify_user_access
from ..models.user import UserResponse


router = APIRouter(prefix="/api/{user_id}/tasks", tags=["todos"])


@router.get("", response_model=List[TaskResponse])
async def get_tasks(
    user_id: str,
    current_user: UserResponse = Depends(get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """Get all tasks for the authenticated user."""
    # Verify user owns the requested data
    await verify_user_access(user_id, credentials)

    service = create_todo_service(db, user_id)
    tasks = service.get_all()
    return tasks


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    user_id: str,
    task_data: TaskCreate,
    current_user: UserResponse = Depends(get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """Create a new task for the authenticated user."""
    await verify_user_access(user_id, credentials)

    service = create_todo_service(db, user_id)
    task = service.create(task_data)
    return task


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    user_id: str,
    task_id: str,
    current_user: UserResponse = Depends(get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """Get a specific task by ID."""
    await verify_user_access(user_id, credentials)

    service = create_todo_service(db, user_id)
    task = service.get_by_id(task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    user_id: str,
    task_id: str,
    task_data: TaskUpdate,
    current_user: UserResponse = Depends(get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """Update a task."""
    await verify_user_access(user_id, credentials)

    service = create_todo_service(db, user_id)
    task = service.update(task_id, task_data)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


@router.patch("/{task_id}/complete", response_model=TaskResponse)
async def toggle_complete(
    user_id: str,
    task_id: str,
    current_user: UserResponse = Depends(get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """Toggle task completion status."""
    await verify_user_access(user_id, credentials)

    service = create_todo_service(db, user_id)
    task = service.toggle_completion(task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    user_id: str,
    task_id: str,
    current_user: UserResponse = Depends(get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """Delete a task."""
    await verify_user_access(user_id, credentials)

    service = create_todo_service(db, user_id)
    success = service.delete(task_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return None
