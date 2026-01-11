'use client';

import React from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { Button } from '../ui/Button';
import { Input } from '../ui/Input';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '../ui/Card';

const signupSchema = z.object({
  name: z.string().min(2, 'Name must be at least 2 characters'),
  email: z.string().email('Invalid email address'),
  password: z.string().min(8, 'Password must be at least 8 characters'),
});

type SignupFormData = z.infer<typeof signupSchema>;

interface SignupFormProps {
  onSubmit: (data: SignupFormData) => void;
  loading?: boolean;
  error?: string;
}

export const SignupForm: React.FC<SignupFormProps> = ({ onSubmit, loading, error }) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SignupFormData>({
    resolver: zodResolver(signupSchema),
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="animate-slideUp">
      <Card className="w-full max-w-md mx-auto overflow-hidden">
        <div className="absolute top-0 right-0 w-40 h-40 bg-gradient-to-br from-pink-400 to-rose-400 rounded-bl-full opacity-10"></div>
        <CardHeader className="space-y-1 relative z-10">
          <CardTitle className="text-3xl text-center gradient-text">Create Account</CardTitle>
          <CardDescription className="text-center text-base">
            Enter your information to get started
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-5 relative z-10">
          {error && (
            <div className="p-4 bg-red-50 border border-red-200 text-red-700 rounded-lg text-sm flex items-start animate-slideDown">
              <svg className="w-5 h-5 mr-2 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
              </svg>
              <span>{error}</span>
            </div>
          )}
          <div className="space-y-2">
            <Input
              label="Full Name"
              type="text"
              placeholder="John Doe"
              {...register('name')}
              error={errors.name?.message}
            />
          </div>
          <div className="space-y-2">
            <Input
              label="Email"
              type="email"
              placeholder="name@example.com"
              {...register('email')}
              error={errors.email?.message}
            />
          </div>
          <div className="space-y-2">
            <Input
              label="Password"
              type="password"
              placeholder="Create a password (min. 6 characters)"
              {...register('password')}
              error={errors.password?.message}
            />
          </div>
        </CardContent>
        <CardFooter className="flex flex-col relative z-10">
          <Button
            type="submit"
            className="w-full"
            loading={loading}
            size="lg"
          >
            {loading ? 'Creating account...' : 'Create Account'}
          </Button>
        </CardFooter>
      </Card>
    </form>
  );
};