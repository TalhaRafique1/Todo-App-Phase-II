import React from 'react';
import clsx from 'clsx';

interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

export const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({
  size = 'md',
  className,
}) => {
  const sizeClasses = clsx({
    'h-4 w-4 border-2': size === 'sm',
    'h-8 w-8 border-4': size === 'md',
    'h-12 w-12 border-4': size === 'lg',
  });

  return (
    <div className="flex items-center justify-center">
      <div
        className={clsx(
          'animate-spin rounded-full border-solid border-current border-t-transparent',
          sizeClasses,
          className
        )}
        role="status"
        aria-label="loading"
      >
        <span className="sr-only">Loading...</span>
      </div>
    </div>
  );
};