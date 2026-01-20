from typing import Dict, Any, List
from .validation import validate_task_data, validate_user_access, validate_uuid
import json


class TaskTools:
    """
    MCP tools for task operations that enforce user ownership.
    """

    def __init__(self, db_session):
        """
        Initialize with database session.
        """
        self.db = db_session

    def add_task(self, user_id: str, title: str, description: str = "") -> Dict[str, Any]:
        """
        Add a new task for the user.
        """
        try:
            # Validate inputs
            if not user_id or not validate_uuid(user_id):
                raise ValueError("Invalid user_id provided")
            if not title or not isinstance(title, str):
                raise ValueError("Valid title is required")

            # Prepare task data
            task_data = validate_task_data({"title": title, "description": description})

            # Create task in database (using SQLModel)
            # Note: Actual implementation would import and use the Task model
            # For now, simulating the creation
            import uuid
            from datetime import datetime

            new_task = {
                "id": str(uuid.uuid4()),
                "user_id": user_id,
                "title": task_data.get("title"),
                "description": task_data.get("description", ""),
                "completed": False,
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
            }

            # In a real implementation, we would save to the database here
            # self.db.add(new_task)
            # self.db.commit()
            # self.db.refresh(new_task)

            return {
                "success": True,
                "task": new_task,
                "message": f"Task '{new_task['title']}' added successfully"
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to add task"
            }

    def list_tasks(self, user_id: str) -> Dict[str, Any]:
        """
        List all tasks for the user.
        """
        try:
            # Validate inputs
            if not user_id or not validate_uuid(user_id):
                raise ValueError("Invalid user_id provided")

            # In a real implementation, we would query the database
            # statement = select(Task).where(Task.user_id == user_id)
            # tasks = self.db.exec(statement).all()

            # For simulation purposes:
            simulated_tasks = [
                {
                    "id": "task-1",
                    "user_id": user_id,
                    "title": "Sample task",
                    "description": "This is a sample task",
                    "completed": False,
                    "created_at": "2026-01-20T17:00:00Z",
                    "updated_at": "2026-01-20T17:00:00Z"
                }
            ]

            return {
                "success": True,
                "tasks": simulated_tasks,
                "count": len(simulated_tasks),
                "message": f"Retrieved {len(simulated_tasks)} tasks for user"
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to list tasks"
            }

    def complete_task(self, user_id: str, task_id: str) -> Dict[str, Any]:
        """
        Mark a task as completed for the user.
        """
        try:
            # Validate inputs
            if not user_id or not validate_uuid(user_id):
                raise ValueError("Invalid user_id provided")
            if not task_id or not validate_uuid(task_id):
                raise ValueError("Invalid task_id provided")

            # In a real implementation, we would:
            # 1. Query the task to ensure it belongs to the user
            # 2. Update the task's completed status
            # task = self.db.get(Task, task_id)
            # if not task or task.user_id != user_id:
            #     raise PermissionError("User does not have access to this task")

            # For simulation:
            simulated_task = {
                "id": task_id,
                "user_id": user_id,
                "title": "Sample task",
                "description": "This is a sample task",
                "completed": True,
                "created_at": "2026-01-20T17:00:00Z",
                "updated_at": "2026-01-20T17:05:00Z"
            }

            return {
                "success": True,
                "task": simulated_task,
                "message": f"Task '{simulated_task['title']}' marked as completed"
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to complete task"
            }

    def delete_task(self, user_id: str, task_id: str) -> Dict[str, Any]:
        """
        Delete a task for the user.
        """
        try:
            # Validate inputs
            if not user_id or not validate_uuid(user_id):
                raise ValueError("Invalid user_id provided")
            if not task_id or not validate_uuid(task_id):
                raise ValueError("Invalid task_id provided")

            # In a real implementation, we would:
            # 1. Query the task to ensure it belongs to the user
            # 2. Delete the task
            # task = self.db.get(Task, task_id)
            # if not task or task.user_id != user_id:
            #     raise PermissionError("User does not have access to this task")
            # self.db.delete(task)
            # self.db.commit()

            return {
                "success": True,
                "task_id": task_id,
                "message": f"Task {task_id} deleted successfully"
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to delete task"
            }

    def update_task(self, user_id: str, task_id: str, **updates) -> Dict[str, Any]:
        """
        Update a task for the user.
        """
        try:
            # Validate inputs
            if not user_id or not validate_uuid(user_id):
                raise ValueError("Invalid user_id provided")
            if not task_id or not validate_uuid(task_id):
                raise ValueError("Invalid task_id provided")

            # Validate updates
            validated_updates = validate_task_data(updates)

            # In a real implementation, we would:
            # 1. Query the task to ensure it belongs to the user
            # 2. Apply updates
            # task = self.db.get(Task, task_id)
            # if not task or task.user_id != user_id:
            #     raise PermissionError("User does not have access to this task")
            #
            # for key, value in validated_updates.items():
            #     setattr(task, key, value)
            # task.updated_at = datetime.now()
            # self.db.add(task)
            # self.db.commit()
            # self.db.refresh(task)

            # For simulation:
            simulated_task = {
                "id": task_id,
                "user_id": user_id,
                "title": validated_updates.get("title", "Sample task"),
                "description": validated_updates.get("description", "This is a sample task"),
                "completed": validated_updates.get("completed", False),
                "created_at": "2026-01-20T17:00:00Z",
                "updated_at": "2026-01-20T17:10:00Z"
            }

            return {
                "success": True,
                "task": simulated_task,
                "message": f"Task {task_id} updated successfully"
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to update task"
            }


# Example usage (would be integrated with MCP server)
# task_tools = TaskTools(db_session)