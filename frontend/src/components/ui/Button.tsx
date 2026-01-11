import React from 'react';
import clsx from 'clsx';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  icon?: React.ReactNode;
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  loading = false,
  icon,
  children,
  className,
  disabled,
  ...props
}) => {
  const baseClasses = 'inline-flex items-center justify-center rounded-lg font-semibold transition-all duration-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-purple-500 focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-background transform hover:scale-105 active:scale-95';

  const variantClasses = clsx({
    'bg-gradient-to-r from-purple-600 to-indigo-600 text-white hover:from-purple-700 hover:to-indigo-700 shadow-lg hover:shadow-xl': variant === 'primary',
    'bg-gradient-to-r from-pink-500 to-rose-500 text-white hover:from-pink-600 hover:to-rose-600 shadow-lg hover:shadow-xl': variant === 'secondary',
    'border-2 border-purple-600 bg-transparent text-purple-600 hover:bg-purple-50 hover:border-purple-700': variant === 'outline',
    'hover:bg-purple-50 text-gray-700 hover:text-purple-700': variant === 'ghost',
  });

  const sizeClasses = clsx({
    'h-9 px-4 py-2 text-sm': size === 'sm',
    'h-11 px-6 py-2.5 text-base': size === 'md',
    'h-13 px-8 py-3 text-lg': size === 'lg',
  });

  const disabledClass = disabled || loading ? 'opacity-50 cursor-not-allowed hover:scale-100' : '';

  const classes = clsx(baseClasses, variantClasses, sizeClasses, disabledClass, className);

  return (
    <button
      className={classes}
      disabled={disabled || loading}
      {...props}
    >
      {loading && (
        <span className="mr-2 h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent"></span>
      )}
      {icon && !loading && <span className="mr-2">{icon}</span>}
      {children}
    </button>
  );
};