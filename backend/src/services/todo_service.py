"""Todo service for database operations."""

from typing import List, Optional
from sqlmodel import Session, select
from ..models.todo import Task, TaskCreate, TaskUpdate
from ..models.user import User


class TodoService:
    """Service class for todo CRUD operations."""

    def __init__(self, db: Session, user_id: str):
        self.db = db
        self.user_id = user_id

    def create(self, task_data: TaskCreate) -> Task:
        """Create a new task for the user."""
        task = Task(
            user_id=self.user_id,
            title=task_data.title,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_all(self) -> List[Task]:
        """Get all tasks for the user."""
        tasks = self.db.exec(
            select(Task)
            .where(Task.user_id == self.user_id)
            .order_by(Task.created_at.desc())
        ).all()
        return tasks

    def get_by_id(self, task_id: str) -> Optional[Task]:
        """Get a specific task if it belongs to the user."""
        task = self.db.get(Task, task_id)
        if task and task.user_id == self.user_id:
            return task
        return None

    def update(self, task_id: str, task_data: TaskUpdate) -> Optional[Task]:
        """Update a task if it belongs to the user."""
        task = self.get_by_id(task_id)
        if not task:
            return None

        if task_data.title is not None:
            task.title = task_data.title
        if task_data.completed is not None:
            task.completed = task_data.completed

        self.db.commit()
        self.db.refresh(task)
        return task

    def toggle_completion(self, task_id: str) -> Optional[Task]:
        """Toggle task completion status."""
        task = self.get_by_id(task_id)
        if not task:
            return None

        task.completed = not task.completed
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task_id: str) -> bool:
        """Delete a task if it belongs to the user."""
        task = self.get_by_id(task_id)
        if not task:
            return False

        self.db.delete(task)
        self.db.commit()
        return True


def create_todo_service(db: Session, user_id: str) -> TodoService:
    """Factory function to create a TodoService instance."""
    return TodoService(db, user_id)
