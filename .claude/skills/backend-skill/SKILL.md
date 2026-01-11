---
name: backend-skill
description: Generate backend routes, handle HTTP requests/responses, and connect to databases. Use for building APIs and server-side logic.
---

# Backend Skill

## Instructions

1. **Route Creation**
   - Define RESTful endpoints (GET, POST, PUT, DELETE)
   - Use clear and descriptive route names
   - Group related routes logically (e.g., /users, /products)

2. **Request Handling**
   - Parse request data (query params, body, headers)
   - Validate incoming data
   - Handle errors gracefully with proper status codes

3. **Response Handling**
   - Return JSON or appropriate content type
   - Include success/error messages
   - Use consistent response structure
   - Set proper HTTP status codes

4. **Database Integration**
   - Connect to SQL or NoSQL databases
   - Perform CRUD operations efficiently
   - Use prepared statements or ORM for security
   - Close connections properly

5. **Security & Best Practices**
   - Sanitize user inputs
   - Use environment variables for sensitive info
   - Implement authentication/authorization if required
   - Follow consistent naming conventions
   - Log errors for debugging

## Example Structure (Node.js + Express + MongoDB)
```javascript
import express from 'express';
import mongoose from 'mongoose';

const app = express();
app.use(express.json());

// Database connection
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('DB connected'))
  .catch(err => console.error('DB connection error', err));

// Routes
app.get('/users', async (req, res) => {
  try {
    const users = await User.find();
    res.status(200).json({ success: true, data: users });
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
});

app.post('/users', async (req, res) => {
  try {
    const user = await User.create(req.body);
    res.status(201).json({ success: true, data: user });
  } catch (err) {
    res.status(400).json({ success: false, message: err.message });
  }
});

// Server
app.listen(3000, () => console.log('Server running on port 3000'));
