'use client';

import React, { useState } from 'react';
import { Task } from '../../types';
import { Button } from '../ui/Button';
import { EditTaskForm } from './EditTaskForm';

interface TaskItemProps {
  task: Task;
  onToggleCompletion: (id: string) => void;
  onDelete: (id: string) => void;
  onUpdate: (id: string, data: Partial<Task>) => void;
}

export const TaskItem: React.FC<TaskItemProps> = ({
  task,
  onToggleCompletion,
  onDelete,
  onUpdate,
}) => {
  const [isEditing, setIsEditing] = useState(false);

  const handleUpdate = (data: Partial<Task>) => {
    onUpdate(task.id, data);
    setIsEditing(false);
  };

  const handleCancelEdit = () => {
    setIsEditing(false);
  };

  return (
    <div className={`group relative rounded-xl border-2 transition-all duration-300 overflow-hidden ${
      task.completed
        ? 'bg-gradient-to-r from-green-50 to-emerald-50 border-green-200 hover:border-green-300'
        : 'bg-white border-purple-100 hover:border-purple-300 hover:shadow-lg'
    }`}>
      {/* Decorative corner element */}
      <div className={`absolute top-0 right-0 w-24 h-24 rounded-bl-full opacity-5 transition-opacity duration-300 ${
        task.completed
          ? 'bg-gradient-to-br from-green-400 to-emerald-400'
          : 'bg-gradient-to-br from-purple-400 to-indigo-400 group-hover:opacity-10'
      }`}></div>

      <div className="relative z-10 p-5">
        {isEditing ? (
          <EditTaskForm
            task={task}
            onSubmit={handleUpdate}
            onCancel={handleCancelEdit}
          />
        ) : (
          <div className="flex items-start justify-between gap-4">
            <div className="flex items-start space-x-4 flex-1 min-w-0">
              {/* Custom Checkbox */}
              <button
                onClick={() => onToggleCompletion(task.id)}
                className={`mt-1 flex-shrink-0 w-6 h-6 rounded-lg border-2 transition-all duration-300 flex items-center justify-center ${
                  task.completed
                    ? 'bg-gradient-to-r from-green-500 to-emerald-500 border-green-500'
                    : 'border-purple-300 hover:border-purple-500 hover:bg-purple-50'
                }`}
              >
                {task.completed && (
                  <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                  </svg>
                )}
              </button>

              <div className="flex-1 min-w-0">
                <h3 className={`font-semibold text-lg mb-1 transition-all duration-300 ${
                  task.completed
                    ? 'line-through text-gray-500'
                    : 'text-gray-900'
                }`}>
                  {task.title}
                </h3>
                {task.description && (
                  <p className={`text-sm mb-2 transition-all duration-300 ${
                    task.completed
                      ? 'text-gray-400'
                      : 'text-gray-600'
                  }`}>
                    {task.description}
                  </p>
                )}
                <div className="flex items-center space-x-3 text-xs text-gray-500">
                  <span className="flex items-center">
                    <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                    {new Date(task.createdAt).toLocaleDateString('en-US', {
                      month: 'short',
                      day: 'numeric',
                      year: 'numeric'
                    })}
                  </span>
                  {task.completed && (
                    <span className="px-2 py-1 bg-green-100 text-green-700 rounded-full text-xs font-semibold">
                      Completed
                    </span>
                  )}
                </div>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="flex space-x-2 flex-shrink-0">
              <button
                onClick={() => setIsEditing(true)}
                className="p-2 rounded-lg text-purple-600 hover:bg-purple-100 transition-all duration-300 hover:scale-110"
                title="Edit task"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
              </button>
              <button
                onClick={() => onDelete(task.id)}
                className="p-2 rounded-lg text-red-600 hover:bg-red-100 transition-all duration-300 hover:scale-110"
                title="Delete task"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};