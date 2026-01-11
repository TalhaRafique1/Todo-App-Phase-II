'use client';

import { ProtectedRoute } from '../../components/auth/ProtectedRoute';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <ProtectedRoute>
      <div className="py-6">
        {children}
      </div>
    </ProtectedRoute>
  );
}