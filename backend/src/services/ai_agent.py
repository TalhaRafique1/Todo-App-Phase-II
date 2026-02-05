from typing import Dict, Any, List
import openai
import os
import re
from sqlmodel import Session
from ..models.message import MessageCreate
from ..database import engine
from ..services.todo_service import create_todo_service
from ..models.todo import TaskCreate


class AIAgentService:
    """
    Service for managing AI agent interactions and tool usage.
    """

    def __init__(self):
        # Check if OpenAI API key is available
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            # Initialize OpenAI client if API key is available
            self.client = openai.OpenAI(api_key=api_key)
            self.api_available = True
        else:
            # Use mock functionality if no API key
            self.client = None
            self.api_available = False

        # Define available tools for the AI agent
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "add_task",
                    "description": "Add a new task to the user's task list",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string", "description": "The title of the task"},
                            "description": {"type": "string", "description": "The description of the task"}
                        },
                        "required": ["title"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "list_tasks",
                    "description": "Get the list of user's tasks",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "complete_task",
                    "description": "Mark a task as completed",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "task_id": {"type": "string", "description": "The ID of the task to complete"}
                        },
                        "required": ["task_id"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "delete_task",
                    "description": "Delete a task from the user's task list",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "task_id": {"type": "string", "description": "The ID of the task to delete"}
                        },
                        "required": ["task_id"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "update_task",
                    "description": "Update a task in the user's task list",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "task_id": {"type": "string", "description": "The ID of the task to update"},
                            "title": {"type": "string", "description": "The new title of the task"},
                            "description": {"type": "string", "description": "The new description of the task"},
                            "completed": {"type": "boolean", "description": "Whether the task is completed"}
                        },
                        "required": ["task_id"]
                    }
                }
            }
        ]

    def process_message(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]],
        user_id: str
    ) -> Dict[str, Any]:
        """
        Process a user message with the AI agent and return response and tool calls.
        """
        # If API is not available, use mock responses
        if not self.api_available:
            return self._mock_process_message(user_message, conversation_history, user_id)

        # Prepare messages for the AI agent
        messages = []

        # Add system message to guide the AI
        messages.append({
            "role": "system",
            "content": f"You are a helpful assistant that manages tasks for user {user_id}. "
                       "You must use the provided tools to manage tasks. "
                       "Always respond with friendly confirmations when tasks are created, updated, or completed. "
                       "Never access the database directly. "
                       "Only use the tools provided to you."
        })

        # Add conversation history
        for msg in conversation_history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        # Add the current user message
        messages.append({
            "role": "user",
            "content": user_message
        })

        try:
            # Call the OpenAI API with the tools
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # Could be configurable
                messages=messages,
                tools=self.tools,
                tool_choice="auto"
            )

            # Process the response
            ai_response = response.choices[0].message

            # Extract tool calls if any
            tool_calls = []
            if ai_response.tool_calls:
                for tool_call in ai_response.tool_calls:
                    tool_call_result = {
                        "name": tool_call.function.name,
                        "arguments": {},
                        "result": {}
                    }

                    try:
                        import json
                        tool_call_result["arguments"] = json.loads(tool_call.function.arguments)

                        # Note: In a real implementation, we would call the actual MCP tools here
                        # For now, we'll just record the intention
                        tool_call_result["result"] = {
                            "status": "intended_for_mcp_server",
                            "details": f"Tool {tool_call.function.name} called with arguments {tool_call_result['arguments']}"
                        }

                    except Exception as e:
                        tool_call_result["result"] = {
                            "status": "error",
                            "message": f"Error parsing tool call arguments: {str(e)}"
                        }

                    tool_calls.append(tool_call_result)

            # Prepare the response
            result = {
                "response": ai_response.content if ai_response.content else "",
                "tool_calls": tool_calls
            }

            return result

        except Exception as e:
            return {
                "response": f"I'm sorry, I encountered an error processing your request: {str(e)}",
                "tool_calls": []
            }

    def _mock_process_message(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]],
        user_id: str
    ) -> Dict[str, Any]:
        """
        Mock implementation for when OpenAI API is not available.
        """

        # Simple rule-based processing for demo purposes
        user_message_lower = user_message.lower()

        # Determine if this is a task-related command
        if "add" in user_message_lower and ("task" in user_message_lower or "create" in user_message_lower):
            # Extract potential task title
            import re
            # Look for phrases like "add task to..." or "create task to..."
            match = re.search(r'(?:add|create)\s+(?:a\s+)?(?:task|to)\s+to?\s+(.+?)(?:\.|$)', user_message_lower)
            task_title = match.group(1).strip() if match else user_message.split(" ", 2)[-1] if len(user_message.split()) > 2 else "new task"

            # Actually create the task in the database
            try:
                db = Session(engine)

                # Create the task using the todo service
                todo_service = create_todo_service(db, user_id)
                task_create = TaskCreate(title=task_title, description="")
                created_task = todo_service.create(task_create)

                tool_calls = [{
                    "name": "add_task",
                    "arguments": {"title": task_title, "description": ""},
                    "result": {
                        "status": "success",
                        "details": f"Task '{task_title}' created with ID: {created_task.id}",
                        "task_id": created_task.id,
                        "task": {
                            "id": created_task.id,
                            "title": created_task.title,
                            "description": created_task.description,
                            "completed": created_task.completed
                        }
                    }
                }]
                response = f"I've added a task for you: '{task_title}'."

            except Exception as e:
                tool_calls = [{
                    "name": "add_task",
                    "arguments": {"title": task_title, "description": ""},
                    "result": {
                        "status": "error",
                        "details": f"Failed to create task: {str(e)}"
                    }
                }]
                response = f"I tried to add the task '{task_title}', but encountered an error: {str(e)}"
            finally:
                db.close()

        elif "list" in user_message_lower and "task" in user_message_lower:
            try:
                db = Session(engine)

                # Get tasks for the user
                todo_service = create_todo_service(db, user_id)
                user_tasks = todo_service.get_all()

                tool_calls = [{
                    "name": "list_tasks",
                    "arguments": {},
                    "result": {
                        "status": "success",
                        "details": f"Found {len(user_tasks)} tasks for user",
                        "tasks": [{"id": task.id, "title": task.title, "completed": task.completed} for task in user_tasks]
                    }
                }]
                if user_tasks:
                    task_titles = [task.title for task in user_tasks]
                    response = f"Your tasks are: {', '.join(task_titles)}."
                else:
                    response = "You don't have any tasks yet."

            except Exception as e:
                tool_calls = [{
                    "name": "list_tasks",
                    "arguments": {},
                    "result": {
                        "status": "error",
                        "details": f"Failed to list tasks: {str(e)}"
                    }
                }]
                response = f"I tried to retrieve your tasks, but encountered an error: {str(e)}"
            finally:
                db.close()

        elif ("complete" in user_message_lower or "done" in user_message_lower) and "task" in user_message_lower:
            # For simplicity in mock mode, we'll mark the first task as complete
            try:
                db = Session(engine)

                # Get first task for the user to mark as complete
                todo_service = create_todo_service(db, user_id)
                user_tasks = todo_service.get_all()
                if user_tasks:
                    task_to_complete = user_tasks[0]
                    updated_task = todo_service.update(task_to_complete.id, {"completed": True})

                    tool_calls = [{
                        "name": "complete_task",
                        "arguments": {"task_id": task_to_complete.id},
                        "result": {
                            "status": "success",
                            "details": f"Task '{task_to_complete.title}' marked as complete",
                            "task": {"id": updated_task.id, "title": updated_task.title, "completed": updated_task.completed}
                        }
                    }]
                    response = f"I've marked the task '{task_to_complete.title}' as complete."
                else:
                    tool_calls = [{
                        "name": "complete_task",
                        "arguments": {"task_id": "none"},
                        "result": {
                            "status": "error",
                            "details": "No tasks found to complete"
                        }
                    }]
                    response = "You don't have any tasks to complete."

            except Exception as e:
                tool_calls = [{
                    "name": "complete_task",
                    "arguments": {"task_id": "mock_task_id"},
                    "result": {
                        "status": "error",
                        "details": f"Failed to complete task: {str(e)}"
                    }
                }]
                response = f"I tried to mark the task as complete, but encountered an error: {str(e)}"
            finally:
                db.close()

        else:
            # Generic response
            tool_calls = []
            response = f"I received your message: '{user_message}'. I can help you manage tasks using natural language commands."

        return {
            "response": response,
            "tool_calls": tool_calls
        }


# Global instance
ai_agent_service = AIAgentService()