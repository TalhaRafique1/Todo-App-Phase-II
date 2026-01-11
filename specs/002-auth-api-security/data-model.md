# Data Model: Authentication & Secure API Communication

## Phase 1: Entity Definitions and Relationships

### User Entity
- **Fields**:
  - `id` (UUID/string): Unique identifier for the user
  - `email` (string): User's email address (unique, required)
  - `name` (string): User's display name (optional)
  - `created_at` (timestamp): Account creation time
  - `updated_at` (timestamp): Last update time

- **Validations**:
  - Email must be valid email format
  - Email must be unique across all users
  - Email is required for account creation

- **Relationships**:
  - One-to-many with Task entity (user owns multiple tasks)

### Task Entity
- **Fields**:
  - `id` (UUID/string): Unique identifier for the task
  - `title` (string): Task title/description (required)
  - `completed` (boolean): Whether the task is completed (default: false)
  - `user_id` (UUID/string): Foreign key to User entity (required)
  - `created_at` (timestamp): Task creation time
  - `updated_at` (timestamp): Last update time

- **Validations**:
  - Title must be provided and non-empty
  - User ID must reference an existing user
  - Completed status defaults to false

- **Relationships**:
  - Many-to-one with User entity (task belongs to one user)

### Authentication Token Entity (Conceptual - handled by Better Auth)
- **Fields**:
  - `token` (string): JWT token string
  - `user_id` (UUID/string): Associated user ID
  - `expires_at` (timestamp): Token expiration time
  - `created_at` (timestamp): Token creation time

- **Validations**:
  - Token must be properly formatted JWT
  - Expiration time must be in the future
  - User ID must reference an existing user

## State Transitions

### Task State Transitions
- **Created**: Task is created with `completed: false`
- **Updated**: Task details (title, completion status) can be modified
- **Completed**: Task completion status toggled to `completed: true`
- **Deleted**: Task is removed from user's list

### Security State Transitions
- **Authenticated**: User provides valid credentials, receives JWT token
- **Authorized**: JWT token is validated, user identity confirmed
- **Access Granted**: User accesses resources they own
- **Access Denied**: Unauthorized access attempts are blocked

## Data Access Patterns

### User-Specific Queries
- All queries must filter by `user_id` to ensure data isolation
- No cross-user data access is allowed
- Authentication middleware validates user identity before query execution

### Indexing Strategy
- User table: Primary key on `id`, unique index on `email`
- Task table: Primary key on `id`, index on `user_id` for efficient filtering