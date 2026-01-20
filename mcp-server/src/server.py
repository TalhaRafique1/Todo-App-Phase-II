"""
MCP (Model Context Protocol) Server for AI Agent Tools
Implements a server that exposes task management tools to AI agents.
"""

from typing import Dict, Any, List
import asyncio
import json
from .tools.task_tools import TaskTools
from .tools.validation import validate_user_access


class MCPServer:
    """
    MCP Server that handles requests from AI agents to execute tools.
    """

    def __init__(self, db_session=None):
        """
        Initialize the MCP server with database session and tools.
        """
        self.db_session = db_session
        self.task_tools = TaskTools(db_session)

        # Map tool names to their functions
        self.tools_map = {
            "add_task": self._execute_add_task,
            "list_tasks": self._execute_list_tasks,
            "complete_task": self._execute_complete_task,
            "delete_task": self._execute_delete_task,
            "update_task": self._execute_update_task
        }

    async def handle_request(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle incoming MCP request from AI agent.
        """
        try:
            # Parse the request
            tool_name = request_data.get("tool_name")
            user_id = request_data.get("user_id")
            arguments = request_data.get("arguments", {})

            if not tool_name:
                return {
                    "success": False,
                    "error": "Missing tool_name in request",
                    "result": None
                }

            if not user_id:
                return {
                    "success": False,
                    "error": "Missing user_id in request",
                    "result": None
                }

            # Check if the tool exists
            if tool_name not in self.tools_map:
                return {
                    "success": False,
                    "error": f"Unknown tool: {tool_name}",
                    "result": None
                }

            # Execute the tool
            result = await self.tools_map[tool_name](user_id, arguments)

            return {
                "success": True,
                "result": result,
                "error": None
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"Error processing request: {str(e)}",
                "result": None
            }

    async def _execute_add_task(self, user_id: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the add_task tool.
        """
        try:
            title = arguments.get("title")
            description = arguments.get("description", "")

            if not title:
                raise ValueError("Title is required for add_task")

            result = self.task_tools.add_task(
                user_id=user_id,
                title=title,
                description=description
            )

            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to add task"
            }

    async def _execute_list_tasks(self, user_id: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the list_tasks tool.
        """
        try:
            result = self.task_tools.list_tasks(user_id=user_id)
            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to list tasks"
            }

    async def _execute_complete_task(self, user_id: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the complete_task tool.
        """
        try:
            task_id = arguments.get("task_id")

            if not task_id:
                raise ValueError("task_id is required for complete_task")

            result = self.task_tools.complete_task(
                user_id=user_id,
                task_id=task_id
            )

            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to complete task"
            }

    async def _execute_delete_task(self, user_id: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the delete_task tool.
        """
        try:
            task_id = arguments.get("task_id")

            if not task_id:
                raise ValueError("task_id is required for delete_task")

            result = self.task_tools.delete_task(
                user_id=user_id,
                task_id=task_id
            )

            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to delete task"
            }

    async def _execute_update_task(self, user_id: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the update_task tool.
        """
        try:
            task_id = arguments.get("task_id")

            if not task_id:
                raise ValueError("task_id is required for update_task")

            # Extract other possible arguments
            updates = {k: v for k, v in arguments.items() if k != "task_id"}

            result = self.task_tools.update_task(
                user_id=user_id,
                task_id=task_id,
                **updates
            )

            return result
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Failed to update task"
            }


# Global instance
mcp_server = MCPServer()


async def run_server():
    """
    Run the MCP server (placeholder implementation).
    In a real implementation, this would set up an actual server.
    """
    print("MCP Server starting...")
    print("Available tools: add_task, list_tasks, complete_task, delete_task, update_task")
    print("Server ready to handle AI agent requests")


if __name__ == "__main__":
    asyncio.run(run_server())