# Data Model: AI Chatbot Backend & Agent Integration

## Overview
Data models for the AI chatbot backend, extending the existing task management system with conversation and message entities.

## Entity: Conversation
Represents a conversation thread between a user and the AI assistant.

**Fields**:
- `id`: UUID - Unique identifier for the conversation
- `user_id`: UUID - Reference to the user who owns this conversation
- `created_at`: DateTime - Timestamp when the conversation started
- `updated_at`: DateTime - Timestamp when the conversation was last updated

**Relationships**:
- One Conversation → Many Messages (via conversation_id foreign key)
- One User → Many Conversations (via user_id foreign key)

**Validation Rules**:
- user_id must reference an existing user
- created_at must be in the past
- updated_at must be >= created_at

## Entity: Message
Represents individual messages within a conversation.

**Fields**:
- `id`: UUID - Unique identifier for the message
- `user_id`: UUID - Reference to the user who sent/owns this message
- `conversation_id`: UUID - Reference to the parent conversation
- `role`: String(Enum: "user", "assistant") - The role of the message sender
- `content`: Text - The content of the message
- `created_at`: DateTime - Timestamp when the message was created

**Relationships**:
- One Conversation → Many Messages (via conversation_id foreign key)
- One User → Many Messages (via user_id foreign key)

**Validation Rules**:
- conversation_id must reference an existing conversation
- user_id must reference an existing user
- role must be either "user" or "assistant"
- content must not be empty
- created_at must be in the past

## Relationship to Existing Models

The new models extend the existing system without modifying existing structures:

- **User** (existing) ← **Conversation** (new) → **Message** (new)
- **User** (existing) ← **Task** (existing)
- **User** (existing) ← **Message** (new)

All models include user_id to enforce user isolation as required by the constitution.

## State Transitions

Messages have no state transitions - they are immutable once created.
Conversations are implicitly "active" as long as new messages are added, and can be considered "inactive" based on the age of the last message for cleanup purposes.