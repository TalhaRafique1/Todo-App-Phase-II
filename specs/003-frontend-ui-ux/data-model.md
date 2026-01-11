# Data Model: Frontend UI & User Experience

## Phase 1: Frontend Entity Definitions and State Management

### User Interface State
- **Fields**:
  - `isLoading` (boolean): Whether the UI is in a loading state
  - `error` (string | null): Error message if an error occurred
  - `success` (string | null): Success message for user feedback
  - `currentUser` (User | null): Current authenticated user information

- **State Transitions**:
  - `idle` → `loading`: When initiating an API call
  - `loading` → `success`: When API call completes successfully
  - `loading` → `error`: When API call fails
  - `error` → `idle`: When user dismisses error or retries

### Task UI Component State
- **Fields**:
  - `tasks` (Task[]): List of tasks to display
  - `editingTaskId` (string | null): ID of task currently being edited
  - `creatingTask` (boolean): Whether in task creation mode
  - `filter` (string): Current filter applied to task list (all, active, completed)

- **State Transitions**:
  - `view` → `editing`: When user clicks edit on a task
  - `editing` → `view`: When user saves or cancels edit
  - `idle` → `creating`: When user clicks create new task
  - `creating` → `idle`: When user saves or cancels creation

### Authentication State
- **Fields**:
  - `isLoggedIn` (boolean): Whether user is currently authenticated
  - `user` (User | null): User information when authenticated
  - `token` (string | null): JWT token for API authentication
  - `authStatus` ('idle' | 'loading' | 'authenticated' | 'unauthenticated'): Current auth status

- **State Transitions**:
  - `unauthenticated` → `loading`: When initiating login/register
  - `loading` → `authenticated`: When login/register succeeds
  - `loading` → `unauthenticated`: When login/register fails
  - `authenticated` → `unauthenticated`: When user logs out or token expires

### Form State
- **Fields**:
  - `values` (Record<string, any>): Current form field values
  - `errors` (Record<string, string[]>): Validation errors for each field
  - `isSubmitting` (boolean): Whether form is currently submitting
  - `touched` (Record<string, boolean>): Which fields have been touched

- **State Transitions**:
  - `idle` → `validating`: When field is changed or form submitted
  - `validating` → `valid`: When all validations pass
  - `validating` → `invalid`: When validations fail
  - `submitting` → `submitted`: When submission completes successfully

## Component Architecture

### Layout Components
- **RootLayout**: Main application layout with global styles
- **AuthLayout**: Layout wrapper for authentication pages
- **DashboardLayout**: Layout for authenticated user pages with navigation

### UI Components
- **Button**: Reusable button component with variants
- **Input**: Reusable input component with validation support
- **Card**: Container component for grouping related content
- **Modal**: Overlay component for dialogs
- **LoadingSpinner**: Visual indicator for loading states

### Authentication Components
- **LoginForm**: Form for user login with validation
- **SignupForm**: Form for user registration with validation
- **ProtectedRoute**: Wrapper to restrict access to authenticated users

### Task Components
- **TaskList**: Container for displaying multiple tasks
- **TaskItem**: Individual task display with controls
- **CreateTaskForm**: Form for creating new tasks
- **EditTaskForm**: Form for editing existing tasks

## Responsive Design Patterns

### Breakpoints
- **Mobile**: 320px - 767px
- **Tablet**: 768px - 1023px
- **Desktop**: 1024px+

### Component Adaptations
- Navigation: Collapsed hamburger menu on mobile, expanded on desktop
- Forms: Stacked layout on mobile, side-by-side on desktop
- Task items: Full-width on mobile, compact on desktop
- Buttons: Larger touch targets on mobile

## User Interaction Flows

### Authentication Flow
1. User visits login page
2. User enters credentials and submits
3. System validates credentials
4. On success: redirect to dashboard
5. On failure: show error message

### Task Management Flow
1. User views task list
2. User performs action (create, edit, delete, toggle)
3. System validates action
4. System updates UI state optimistically
5. System sends API request
6. On success: persist change
7. On failure: revert optimistic update and show error