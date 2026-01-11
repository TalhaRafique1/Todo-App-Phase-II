import { Task, ApiResponse } from '../types';
import { apiClient } from './api';

class TaskService {
  private getUserId(): string {
    // Get user ID from stored token or user data
    const token = localStorage.getItem('authToken');
    if (!token) throw new Error('Not authenticated');

    // Decode JWT to get user ID
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload.sub;
  }

  async getAllTasks(): Promise<ApiResponse<Task[]>> {
    try {
      const userId = this.getUserId();
      const response = await apiClient.get(`/${userId}/tasks`);
      return {
        success: true,
        data: response.data,
      };
    } catch (error: any) {
      const message = error.response?.data?.detail || error.response?.data?.message || 'Failed to fetch tasks';
      return { success: false, error: message };
    }
  }

  async createTask(taskData: Partial<Task>): Promise<ApiResponse<Task>> {
    try {
      const userId = this.getUserId();
      const response = await apiClient.post(`/${userId}/tasks`, taskData);
      return {
        success: true,
        data: response.data,
      };
    } catch (error: any) {
      const message = error.response?.data?.detail || error.response?.data?.message || 'Failed to create task';
      return { success: false, error: message };
    }
  }

  async updateTask(id: string, taskData: Partial<Task>): Promise<ApiResponse<Task>> {
    try {
      const userId = this.getUserId();
      const response = await apiClient.put(`/${userId}/tasks/${id}`, taskData);
      return {
        success: true,
        data: response.data,
      };
    } catch (error: any) {
      const message = error.response?.data?.detail || error.response?.data?.message || 'Failed to update task';
      return { success: false, error: message };
    }
  }

  async deleteTask(id: string): Promise<ApiResponse<null>> {
    try {
      const userId = this.getUserId();
      await apiClient.delete(`/${userId}/tasks/${id}`);
      return {
        success: true,
        message: 'Task deleted successfully',
      };
    } catch (error: any) {
      const message = error.response?.data?.detail || error.response?.data?.message || 'Failed to delete task';
      return { success: false, error: message };
    }
  }

  async toggleTaskCompletion(id: string): Promise<ApiResponse<Task>> {
    try {
      const userId = this.getUserId();
      const response = await apiClient.patch(`/${userId}/tasks/${id}/complete`);
      return {
        success: true,
        data: response.data,
      };
    } catch (error: any) {
      const message = error.response?.data?.detail || error.response?.data?.message || 'Failed to toggle task completion';
      return { success: false, error: message };
    }
  }
}

export const taskService = new TaskService();