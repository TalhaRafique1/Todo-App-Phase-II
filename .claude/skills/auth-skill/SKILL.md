---
name: auth-skill
description: Implement secure authentication for web applications, including signup, signin, password hashing, JWT token management, and integration with modern auth systems.
---
# Auth Skill

## Instructions

1. **User Signup**
   - Collect essential fields: `username`, `email`, `password`
   - Validate input (email format, password strength)
   - Hash passwords securely (e.g., using bcrypt, argon2)
   - Store user data in the database

2. **User Signin**
   - Validate credentials
   - Compare hashed password
   - Return authentication tokens on success

3. **JWT Tokens**
   - Generate access tokens for session management
   - Optionally create refresh tokens
   - Include user ID and role in the token payload
   - Set proper expiration and secure storage (HTTPOnly cookies or secure local storage)

4. **Password Management**
   - Provide password reset flow
   - Hash new passwords before saving
   - Ensure tokens for password reset are time-limited

5. **Better Auth Integration**
   - Use middlewares to protect routes (e.g., `isAuthenticated`, `hasRole`)
   - Support OAuth/social logins (optional)
   - Log failed attempts and monitor suspicious activity

## Best Practices
- Use strong password hashing (bcrypt/argon2)
- Never store plain-text passwords
- Keep JWT secrets secure and rotate periodically
- Validate all user inputs
- Implement rate-limiting to prevent brute-force attacks
- Mobile-first approach for auth UI

## Example Structure

```javascript
// signup.js
import bcrypt from 'bcryptjs';
import { createUser } from './db';
import { generateToken } from './jwt';

export async function signup(req, res) {
  const { username, email, password } = req.body;

  // Validate input
  if (!email || !password || !username) {
    return res.status(400).json({ message: 'All fields required' });
  }

  // Hash password
  const hashedPassword = await bcrypt.hash(password, 12);

  // Store user
  const user = await createUser({ username, email, password: hashedPassword });

  // Generate JWT
  const token = generateToken({ id: user.id });

  res.status(201).json({ token, user });
}

// middleware/auth.js
import jwt from 'jsonwebtoken';

export function isAuthenticated(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'Unauthorized' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch {
    res.status(401).json({ message: 'Invalid token' });
  }
}
