'use client';

import React, { useState } from 'react';
import { useTasks } from '../../hooks/useTasks';
import { useAuth } from '../../hooks/useAuth';
import { TaskList } from '../../components/tasks/TaskList';
import { CreateTaskForm } from '../../components/tasks/CreateTaskForm';
import { LoadingSpinner } from '../../components/ui/LoadingSpinner';
import { Button } from '../../components/ui/Button';
import { Task } from '../../types';

const DashboardPage = () => {
  const { user, logout } = useAuth();
  const {
    tasks,
    loading,
    error,
    createTask,
    updateTask,
    deleteTask,
    toggleTaskCompletion
  } = useTasks();

  const [formLoading, setFormLoading] = useState(false);

  const handleCreateTask = async (data: Partial<Task>) => {
    setFormLoading(true);
    try {
      await createTask(data);
    } finally {
      setFormLoading(false);
    }
  };

  const handleToggleCompletion = async (id: string) => {
    await toggleTaskCompletion(id);
  };

  const handleDeleteTask = async (id: string) => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      await deleteTask(id);
    }
  };

  const handleUpdateTask = async (id: string, data: Partial<Task>) => {
    await updateTask(id, data);
  };

  if (loading && tasks.length === 0) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-white to-indigo-50 relative overflow-hidden">
      {/* Decorative Background Elements */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
        <div className="absolute top-40 left-20 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl opacity-10 animate-float"></div>
        <div className="absolute bottom-40 right-20 w-96 h-96 bg-indigo-300 rounded-full mix-blend-multiply filter blur-xl opacity-10 animate-float" style={{ animationDelay: '2s' }}></div>
      </div>

      <header className="glass border-b border-purple-100 relative z-10 animate-slideDown">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
            <div>
              <h1 className="text-3xl font-bold gradient-text mb-1">My Tasks</h1>
              <p className="text-gray-600">Manage your tasks and stay productive</p>
            </div>
            <div className="flex items-center space-x-4">
              <div className="hidden sm:flex items-center space-x-3 px-4 py-2 bg-gradient-to-r from-purple-50 to-indigo-50 rounded-lg border border-purple-200">
                <div className="w-10 h-10 rounded-full bg-gradient-to-r from-purple-600 to-indigo-600 flex items-center justify-center text-white font-bold">
                  {user?.name?.charAt(0).toUpperCase() || user?.email?.charAt(0).toUpperCase()}
                </div>
                <div>
                  <p className="text-sm font-semibold text-gray-900">{user?.name || 'User'}</p>
                  <p className="text-xs text-gray-600">{user?.email}</p>
                </div>
              </div>
              <Button variant="outline" onClick={logout} size="sm">
                Logout
              </Button>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto py-8 sm:px-6 lg:px-8 relative z-10">
        <div className="px-4 sm:px-0">
          {/* Create Task Section */}
          <div className="mb-8 animate-slideUp">
            <div className="bg-white rounded-2xl shadow-xl border border-purple-100 p-6 sm:p-8">
              <div className="flex items-center mb-6">
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-indigo-600 flex items-center justify-center mr-4 shadow-lg">
                  <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                  </svg>
                </div>
                <div>
                  <h2 className="text-xl font-bold text-gray-900">Create New Task</h2>
                  <p className="text-sm text-gray-600">Add a new task to your list</p>
                </div>
              </div>
              <CreateTaskForm
                onSubmit={handleCreateTask}
                loading={formLoading}
                error={error || undefined}
              />
            </div>
          </div>

          {/* Tasks List Section */}
          <div className="bg-white rounded-2xl shadow-xl border border-purple-100 overflow-hidden animate-slideUp animate-delay-100">
            <div className="px-6 py-5 sm:px-8 border-b border-purple-100 bg-gradient-to-r from-purple-50 to-indigo-50">
              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center mr-3 shadow-lg">
                    <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                    </svg>
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-gray-900">Your Tasks</h3>
                    <p className="text-sm text-gray-600">{tasks.length} {tasks.length === 1 ? 'task' : 'tasks'} total</p>
                  </div>
                </div>
                <div className="flex items-center space-x-2">
                  <span className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm font-semibold">
                    {tasks.filter(t => t.completed).length} completed
                  </span>
                  <span className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm font-semibold">
                    {tasks.filter(t => !t.completed).length} pending
                  </span>
                </div>
              </div>
            </div>
            <div className="px-6 py-6 sm:p-8">
              <TaskList
                tasks={tasks}
                loading={loading}
                error={error}
                onToggleCompletion={handleToggleCompletion}
                onDelete={handleDeleteTask}
                onUpdate={handleUpdateTask}
              />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DashboardPage;