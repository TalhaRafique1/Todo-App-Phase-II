import { AuthResponse, LoginFormData, SignupFormData } from '../types';
import { apiClient } from './api';

// Helper function to format error messages from FastAPI
function formatErrorMessage(error: any): string {
  const detail = error.response?.data?.detail;

  // If detail is an array (Pydantic validation errors)
  if (Array.isArray(detail)) {
    return detail.map((err: any) => err.msg || 'Validation error').join(', ');
  }

  // If detail is a string
  if (typeof detail === 'string') {
    return detail;
  }

  // Fallback to generic message
  return error.response?.data?.message || 'An error occurred';
}

class AuthService {
  async login(credentials: LoginFormData): Promise<AuthResponse> {
    try {
      const response = await apiClient.post('/auth/login', credentials);
      const { user, access_token } = response.data;

      if (access_token) {
        localStorage.setItem('authToken', access_token);
        // Set the authorization header for subsequent requests
        apiClient.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
      }

      return { success: true, user, token: access_token };
    } catch (error: any) {
      const message = formatErrorMessage(error) || 'Login failed';
      return { success: false, error: message };
    }
  }

  async signup(userData: SignupFormData): Promise<AuthResponse> {
    try {
      const response = await apiClient.post('/auth/register', userData);
      const { user, access_token } = response.data;

      if (access_token) {
        localStorage.setItem('authToken', access_token);
        // Set the authorization header for subsequent requests
        apiClient.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
      }

      return { success: true, user, token: access_token };
    } catch (error: any) {
      const message = formatErrorMessage(error) || 'Signup failed';
      return { success: false, error: message };
    }
  }

  async logout(): Promise<void> {
    localStorage.removeItem('authToken');
    delete apiClient.defaults.headers.common['Authorization'];
  }

  async getCurrentUser(): Promise<any> {
    try {
      const token = localStorage.getItem('authToken');
      if (!token) {
        return null;
      }

      // Set the authorization header
      apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;

      const response = await apiClient.get('/auth/me');
      return response.data;
    } catch (error) {
      // If there's an error, remove the token as it might be invalid
      this.logout();
      return null;
    }
  }

  isAuthenticated(): boolean {
    return !!localStorage.getItem('authToken');
  }

  getToken(): string | null {
    return localStorage.getItem('authToken');
  }
}

export const authService = new AuthService();