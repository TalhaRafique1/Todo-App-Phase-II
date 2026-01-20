from typing import Dict, Any, Optional
import uuid


def validate_user_access(user_id: str, target_user_id: str) -> bool:
    """
    Validate that the user has access to resources owned by target_user_id.
    """
    return user_id == target_user_id


def validate_uuid(value: str) -> bool:
    """
    Validate that the provided string is a valid UUID.
    """
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False


def validate_task_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate task-related data and return cleaned data or raise exception.
    """
    errors = []

    # Validate title if provided
    if "title" in data:
        if not isinstance(data["title"], str) or len(data["title"].strip()) == 0:
            errors.append("Title must be a non-empty string")

    # Validate description if provided
    if "description" in data:
        if not isinstance(data["description"], str):
            errors.append("Description must be a string")

    # Validate completed if provided
    if "completed" in data:
        if not isinstance(data["completed"], bool):
            errors.append("Completed must be a boolean")

    # Validate task_id if provided
    if "task_id" in data:
        if not validate_uuid(data["task_id"]):
            errors.append("task_id must be a valid UUID")

    if errors:
        raise ValueError(f"Validation errors: {'; '.join(errors)}")

    # Return cleaned data
    cleaned_data = {}
    for key, value in data.items():
        if key in ["title", "description"]:
            cleaned_data[key] = value.strip() if isinstance(value, str) else value
        elif key in ["completed", "task_id", "id"]:
            cleaned_data[key] = value

    return cleaned_data


def validate_conversation_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate conversation-related data and return cleaned data or raise exception.
    """
    errors = []

    # Validate user_id
    if "user_id" in data:
        if not validate_uuid(data["user_id"]):
            errors.append("user_id must be a valid UUID")

    if errors:
        raise ValueError(f"Validation errors: {'; '.join(errors)}")

    return data