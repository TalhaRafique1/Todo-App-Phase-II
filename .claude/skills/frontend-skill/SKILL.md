---
name: frontend-skill
description: Build responsive pages, reusable components, layouts, and style them effectively using modern frontend techniques. Ideal for Next.js, React, or general web projects.
---

# Frontend Skill – Pages, Components, Layouts, Styling

## Instructions

1. **Page Structure**
   - Use semantic HTML tags (header, main, footer, section)
   - Create responsive layouts with CSS Grid or Flexbox
   - Ensure mobile-first design and accessibility

2. **Component Design**
   - Make reusable UI components (buttons, cards, modals, forms)
   - Accept props for dynamic content
   - Isolate styling using CSS Modules, Tailwind, or styled-components

3. **Layout Guidelines**
   - Consistent spacing (padding, margin) across components
   - Define typography hierarchy (headings, body, captions)
   - Use a design system for colors, fonts, and shadows

4. **Styling**
   - Responsive styling using media queries or Tailwind breakpoints
   - Smooth hover/focus effects for interactive elements
   - Use utility-first classes for faster development
   - Ensure sufficient contrast for accessibility

5. **Best Practices**
   - Keep components small and focused (single responsibility)
   - Use semantic class names or utility classes
   - Optimize images and assets for performance
   - Test responsiveness across devices

## Example Page Structure
```html
<main class="container mx-auto p-4">
  <header class="flex justify-between items-center py-4">
    <h1 class="text-2xl font-bold">My Website</h1>
    <nav>
      <ul class="flex gap-4">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
  </header>

  <section class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
    <div class="card p-4 shadow rounded">Card 1</div>
    <div class="card p-4 shadow rounded">Card 2</div>
    <div class="card p-4 shadow rounded">Card 3</div>
  </section>

  <footer class="mt-12 text-center text-gray-500">
    © 2026 My Website. All rights reserved.
  </footer>
</main>
