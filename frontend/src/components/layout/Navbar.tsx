'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useAuth } from '../../hooks/useAuth';
import { Button } from '../ui/Button';

export const Navbar = () => {
  const { user, isAuthenticated, logout } = useAuth();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <nav className="glass sticky top-0 z-50 border-b border-purple-100 animate-slideDown">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="flex-shrink-0 flex items-center group">
              <span className="text-2xl font-bold gradient-text transition-all duration-300 group-hover:scale-110">
                TodoApp
              </span>
            </Link>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center space-x-2">
            {!isAuthenticated ? (
              <>
                <Link href="/login" className="text-gray-700 hover:text-purple-600 px-4 py-2 rounded-lg text-sm font-semibold transition-all duration-300 hover:bg-purple-50">
                  Login
                </Link>
                <Link href="/signup">
                  <Button variant="primary" size="sm">
                    Sign Up
                  </Button>
                </Link>
              </>
            ) : (
              <>
                <Link href="/dashboard" className="text-gray-700 hover:text-purple-600 px-4 py-2 rounded-lg text-sm font-semibold transition-all duration-300 hover:bg-purple-50">
                  Dashboard
                </Link>
                <span className="text-gray-600 px-3 py-2 rounded-lg text-sm font-medium bg-purple-50">
                  {user?.name || user?.email}
                </span>
                <Button variant="outline" size="sm" onClick={logout}>
                  Logout
                </Button>
              </>
            )}
          </div>

          {/* Mobile menu button */}
          <div className="flex items-center md:hidden">
            <button
              type="button"
              className="inline-flex items-center justify-center p-2 rounded-lg text-gray-700 hover:text-purple-600 hover:bg-purple-50 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-purple-500 transition-all duration-300"
              onClick={toggleMobileMenu}
              aria-expanded={mobileMenuOpen}
            >
              <span className="sr-only">Open main menu</span>
              {mobileMenuOpen ? (
                <svg className="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              ) : (
                <svg className="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              )}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {mobileMenuOpen && (
        <div className="md:hidden animate-slideDown border-t border-purple-100">
          <div className="px-4 pt-2 pb-3 space-y-2">
            {!isAuthenticated ? (
              <>
                <Link href="/login" className="text-gray-700 hover:text-purple-600 hover:bg-purple-50 block px-4 py-3 rounded-lg text-base font-semibold transition-all duration-300">
                  Login
                </Link>
                <Link href="/signup" className="block">
                  <Button variant="primary" size="md" className="w-full">
                    Sign Up
                  </Button>
                </Link>
              </>
            ) : (
              <>
                <Link href="/dashboard" className="text-gray-700 hover:text-purple-600 hover:bg-purple-50 block px-4 py-3 rounded-lg text-base font-semibold transition-all duration-300">
                  Dashboard
                </Link>
                <div className="text-gray-600 block px-4 py-3 rounded-lg text-base font-medium bg-purple-50">
                  Welcome, {user?.name || user?.email}
                </div>
                <Button variant="outline" onClick={logout} className="w-full">
                  Logout
                </Button>
              </>
            )}
          </div>
        </div>
      )}
    </nav>
  );
};