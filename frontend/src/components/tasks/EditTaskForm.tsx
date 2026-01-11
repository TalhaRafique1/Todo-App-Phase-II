import React from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { Button } from '../ui/Button';
import { Input } from '../ui/Input';
import { Task } from '../../types';

const taskSchema = z.object({
  title: z.string().min(1, 'Title is required').max(100, 'Title must be less than 100 characters'),
  description: z.string().optional(),
});

type TaskFormData = z.infer<typeof taskSchema>;

interface EditTaskFormProps {
  task: Task;
  onSubmit: (data: TaskFormData) => void;
  onCancel: () => void;
}

export const EditTaskForm: React.FC<EditTaskFormProps> = ({ task, onSubmit, onCancel }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<TaskFormData>({
    resolver: zodResolver(taskSchema),
    defaultValues: {
      title: task.title,
      description: task.description,
    },
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="w-full">
      <div className="grid grid-cols-1 gap-4">
        <div>
          <Input
            label="Task Title"
            placeholder="What needs to be done?"
            {...register('title')}
            error={errors.title?.message}
          />
        </div>
        <div>
          <Input
            label="Description (Optional)"
            placeholder="Add details..."
            {...register('description')}
          />
        </div>
        <div className="flex space-x-3 pt-2">
          <Button
            type="button"
            variant="outline"
            className="flex-1"
            onClick={onCancel}
          >
            Cancel
          </Button>
          <Button
            type="submit"
            className="flex-1"
          >
            Save Changes
          </Button>
        </div>
      </div>
    </form>
  );
};