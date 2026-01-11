# API Contracts: Frontend UI & User Experience

## Phase 1: API Contract Definitions

### Authentication Endpoints

#### POST /api/auth/register
**Description**: Register a new user account
**Request Headers**:
- Content-Type: application/json

**Request Body**:
```json
{
  "email": "string",
  "password": "string"
}
```

**Response**:
- 201 Created: User registered successfully
```json
{
  "success": true,
  "user": {
    "id": "string",
    "email": "string"
  },
  "token": "string"
}
```
- 400 Bad Request: Invalid input data
- 409 Conflict: Email already exists

#### POST /api/auth/login
**Description**: Authenticate user and return JWT token
**Request Headers**:
- Content-Type: application/json

**Request Body**:
```json
{
  "email": "string",
  "password": "string"
}
```

**Response**:
- 200 OK: Authentication successful
```json
{
  "success": true,
  "user": {
    "id": "string",
    "email": "string"
  },
  "token": "string"
}
```
- 401 Unauthorized: Invalid credentials

#### POST /api/auth/logout
**Description**: Logout user and invalidate session
**Request Headers**:
- Authorization: Bearer {token}

**Response**:
- 200 OK: Logout successful
```json
{
  "success": true,
  "message": "Logged out successfully"
}
```

### Task Management Endpoints

#### GET /api/v1/users/{user_id}/tasks
**Description**: Get all tasks for the authenticated user
**Request Headers**:
- Authorization: Bearer {token}

**Path Parameters**:
- user_id: String (authenticated user's ID)

**Response**:
- 200 OK: Tasks retrieved successfully
```json
{
  "tasks": [
    {
      "id": "string",
      "title": "string",
      "completed": boolean,
      "user_id": "string",
      "created_at": "timestamp",
      "updated_at": "timestamp"
    }
  ]
}
```
- 401 Unauthorized: Invalid or missing token
- 403 Forbidden: User ID in token doesn't match path parameter

#### POST /api/v1/users/{user_id}/tasks
**Description**: Create a new task for the authenticated user
**Request Headers**:
- Authorization: Bearer {token}
- Content-Type: application/json

**Path Parameters**:
- user_id: String (authenticated user's ID)

**Request Body**:
```json
{
  "title": "string"
}
```

**Response**:
- 201 Created: Task created successfully
```json
{
  "task": {
    "id": "string",
    "title": "string",
    "completed": false,
    "user_id": "string",
    "created_at": "timestamp",
    "updated_at": "timestamp"
  }
}
```
- 401 Unauthorized: Invalid or missing token
- 403 Forbidden: User ID in token doesn't match path parameter

#### PUT /api/v1/users/{user_id}/tasks/{task_id}
**Description**: Update a task for the authenticated user
**Request Headers**:
- Authorization: Bearer {token}
- Content-Type: application/json

**Path Parameters**:
- user_id: String (authenticated user's ID)
- task_id: String (task ID to update)

**Request Body**:
```json
{
  "title": "string",
  "completed": boolean
}
```

**Response**:
- 200 OK: Task updated successfully
```json
{
  "task": {
    "id": "string",
    "title": "string",
    "completed": boolean,
    "user_id": "string",
    "created_at": "timestamp",
    "updated_at": "timestamp"
  }
}
```
- 401 Unauthorized: Invalid or missing token
- 403 Forbidden: User ID in token doesn't match path parameter or task doesn't belong to user
- 404 Not Found: Task not found

#### DELETE /api/v1/users/{user_id}/tasks/{task_id}
**Description**: Delete a task for the authenticated user
**Request Headers**:
- Authorization: Bearer {token}

**Path Parameters**:
- user_id: String (authenticated user's ID)
- task_id: String (task ID to delete)

**Response**:
- 200 OK: Task deleted successfully
```json
{
  "success": true,
  "message": "Task deleted successfully"
}
```
- 401 Unauthorized: Invalid or missing token
- 403 Forbidden: User ID in token doesn't match path parameter or task doesn't belong to user
- 404 Not Found: Task not found

#### PATCH /api/v1/users/{user_id}/tasks/{task_id}/toggle-complete
**Description**: Toggle the completion status of a task for the authenticated user
**Request Headers**:
- Authorization: Bearer {token}
- Content-Type: application/json

**Path Parameters**:
- user_id: String (authenticated user's ID)
- task_id: String (task ID to toggle)

**Response**:
- 200 OK: Task completion toggled successfully
```json
{
  "task": {
    "id": "string",
    "title": "string",
    "completed": boolean,
    "user_id": "string",
    "created_at": "timestamp",
    "updated_at": "timestamp"
  }
}
```
- 401 Unauthorized: Invalid or missing token
- 403 Forbidden: User ID in token doesn't match path parameter or task doesn't belong to user
- 404 Not Found: Task not found

### Error Response Format
All error responses follow this format:
```json
{
  "success": false,
  "error": "error message",
  "details": "optional error details"
}
```

### Authentication Requirements
- All task endpoints require a valid JWT token in the Authorization header
- Tokens must be in the format "Bearer {token}"
- User ID in token must match the user_id in the URL path
- Invalid tokens return 401 Unauthorized
- Mismatched user IDs return 403 Forbidden