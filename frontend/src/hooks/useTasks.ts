import { useState, useEffect } from 'react';
import { Task } from '../types';
import { taskService } from '../services/tasks';

export const useTasks = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  const fetchTasks = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await taskService.getAllTasks();
      if (result.success && result.data) {
        setTasks(result.data);
      } else {
        setError(result.error || 'Failed to fetch tasks');
      }
    } catch (err) {
      setError('An unexpected error occurred');
    } finally {
      setLoading(false);
    }
  };

  const createTask = async (taskData: Partial<Task>) => {
    setLoading(true);
    try {
      const result = await taskService.createTask(taskData);
      if (result.success && result.data) {
        setTasks(prev => [...prev, result.data as Task]);
        return { success: true };
      } else {
        return { success: false, error: result.error };
      }
    } catch (err) {
      return { success: false, error: 'Failed to create task' };
    } finally {
      setLoading(false);
    }
  };

  const updateTask = async (id: string, taskData: Partial<Task>) => {
    setLoading(true);
    try {
      const result = await taskService.updateTask(id, taskData);
      if (result.success && result.data) {
        setTasks(prev => prev.map(task => task.id === id ? result.data! : task));
        return { success: true };
      } else {
        return { success: false, error: result.error };
      }
    } catch (err) {
      return { success: false, error: 'Failed to update task' };
    } finally {
      setLoading(false);
    }
  };

  const deleteTask = async (id: string) => {
    setLoading(true);
    try {
      const result = await taskService.deleteTask(id);
      if (result.success) {
        setTasks(prev => prev.filter(task => task.id !== id));
        return { success: true };
      } else {
        return { success: false, error: result.error };
      }
    } catch (err) {
      return { success: false, error: 'Failed to delete task' };
    } finally {
      setLoading(false);
    }
  };

  const toggleTaskCompletion = async (id: string) => {
    setLoading(true);
    try {
      const result = await taskService.toggleTaskCompletion(id);
      if (result.success && result.data) {
        setTasks(prev => prev.map(task =>
          task.id === id ? result.data! : task
        ));
        return { success: true };
      } else {
        return { success: false, error: result.error };
      }
    } catch (err) {
      return { success: false, error: 'Failed to toggle task completion' };
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return {
    tasks,
    loading,
    error,
    fetchTasks,
    createTask,
    updateTask,
    deleteTask,
    toggleTaskCompletion,
  };
};