"""Task API endpoints with user-specific routes and JWT authentication."""

from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session
from ...database import get_db
from ...models.todo import Task, TaskCreate, TaskUpdate, TaskResponse
from ...services.todo_service import create_todo_service
from ...middleware.auth import get_current_user
from ...models.user import UserResponse
from ...utils.jwt import verify_access_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(prefix="/users", tags=["tasks"])

# Security scheme for JWT token
security = HTTPBearer()


@router.get("/{user_id}/tasks", response_model=List[TaskResponse])
async def get_user_tasks(
    user_id: str,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all tasks for the authenticated user."""
    # Verify that the requested user_id matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access another user's tasks"
        )

    service = create_todo_service(db, user_id)
    tasks = service.get_all()
    return tasks


@router.post("/{user_id}/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_user_task(
    user_id: str,
    task_data: TaskCreate,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new task for the authenticated user."""
    # Verify that the requested user_id matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot create tasks for another user"
        )

    service = create_todo_service(db, user_id)
    task = service.create(task_data)
    return task


@router.put("/{user_id}/tasks/{task_id}", response_model=TaskResponse)
async def update_user_task(
    user_id: str,
    task_id: str,
    task_data: TaskUpdate,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a task for the authenticated user."""
    # Verify that the requested user_id matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot update another user's tasks"
        )

    service = create_todo_service(db, user_id)
    task = service.update(task_id, task_data)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


@router.delete("/{user_id}/tasks/{task_id}", response_model=dict)
async def delete_user_task(
    user_id: str,
    task_id: str,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a task for the authenticated user."""
    # Verify that the requested user_id matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot delete another user's tasks"
        )

    service = create_todo_service(db, user_id)
    success = service.delete(task_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return {"success": True, "message": "Task deleted successfully"}


@router.patch("/{user_id}/tasks/{task_id}/toggle-complete", response_model=TaskResponse)
async def toggle_user_task_completion(
    user_id: str,
    task_id: str,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Toggle the completion status of a task for the authenticated user."""
    # Verify that the requested user_id matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot modify another user's tasks"
        )

    service = create_todo_service(db, user_id)
    task = service.toggle_completion(task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task