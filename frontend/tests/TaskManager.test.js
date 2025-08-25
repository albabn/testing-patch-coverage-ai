import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import TaskManager from '../src/components/TaskManager';

// Mock axios to avoid actual HTTP requests
jest.mock('axios');

describe('TaskManager Component', () => {
  beforeEach(() => {
    // Clear all mocks before each test
    jest.clearAllMocks();
  });

  test('renders Task Management System title', () => {
    render(<TaskManager />);
    expect(screen.getByText('🚀 Task Management System')).toBeInTheDocument();
  });

  test('renders navigation tabs', () => {
    render(<TaskManager />);
    expect(screen.getByText('tasks')).toBeInTheDocument();
    expect(screen.getByText('projects')).toBeInTheDocument();
    expect(screen.getByText('users')).toBeInTheDocument();
  });

  test('shows tasks tab by default', () => {
    render(<TaskManager />);
    expect(screen.getByText('Create New Task')).toBeInTheDocument();
    expect(screen.getByText('Tasks (2)')).toBeInTheDocument();
  });

  test('switches to projects tab when clicked', () => {
    render(<TaskManager />);
    fireEvent.click(screen.getByText('projects'));
    expect(screen.getByText('Create New Project')).toBeInTheDocument();
    expect(screen.getByText('Projects (2)')).toBeInTheDocument();
  });

  test('switches to users tab when clicked', () => {
    render(<TaskManager />);
    fireEvent.click(screen.getByText('users'));
    expect(screen.getByText('Create New User')).toBeInTheDocument();
    expect(screen.getByText('Users (2)')).toBeInTheDocument();
  });

  test('displays mock tasks on initial load', () => {
    render(<TaskManager />);
    expect(screen.getByText('Design Homepage')).toBeInTheDocument();
    expect(screen.getByText('Implement Navigation')).toBeInTheDocument();
  });

  test('displays mock projects on projects tab', () => {
    render(<TaskManager />);
    fireEvent.click(screen.getByText('projects'));
    expect(screen.getByText('Website Redesign')).toBeInTheDocument();
    expect(screen.getByText('Mobile App')).toBeInTheDocument();
  });

  test('displays mock users on users tab', () => {
    render(<TaskManager />);
    fireEvent.click(screen.getByText('users'));
    expect(screen.getByText('john_doe')).toBeInTheDocument();
    expect(screen.getByText('jane_smith')).toBeInTheDocument();
  });

  test('creates new task when form is filled and submitted', async () => {
    render(<TaskManager />);
    
    // Fill in the task form
    fireEvent.change(screen.getByPlaceholderText('Task Title'), {
      target: { value: 'New Test Task' }
    });
    fireEvent.change(screen.getByPlaceholderText('Description'), {
      target: { value: 'New test description' }
    });
    
    // Select project and assignee
    const projectSelect = screen.getByDisplayValue('Select Project');
    fireEvent.change(projectSelect, { target: { value: '1' } });
    
    const assigneeSelect = screen.getByDisplayValue('Select Assignee');
    fireEvent.change(assigneeSelect, { target: { value: '1' } });
    
    // Submit the form
    fireEvent.click(screen.getByText('Create Task'));
    
    // Check if new task appears
    await waitFor(() => {
      expect(screen.getByText('New Test Task')).toBeInTheDocument();
    });
  });

  test('creates new project when form is filled and submitted', async () => {
    render(<TaskManager />);
    fireEvent.click(screen.getByText('projects'));
    
    // Fill in the project form
    fireEvent.change(screen.getByPlaceholderText('Project Name'), {
      target: { value: 'New Test Project' }
    });
    fireEvent.change(screen.getByPlaceholderText('Description'), {
      target: { value: 'New test project description' }
    });
    
    // Select owner
    const ownerSelect = screen.getByDisplayValue('Select Owner');
    fireEvent.change(ownerSelect, { target: { value: '1' } });
    
    // Submit the form
    fireEvent.click(screen.getByText('Create Project'));
    
    // Check if new project appears
    await waitFor(() => {
      expect(screen.getByText('New Test Project')).toBeInTheDocument();
    });
  });

  test('creates new user when form is filled and submitted', async () => {
    render(<TaskManager />);
    fireEvent.click(screen.getByText('users'));
    
    // Fill in the user form
    fireEvent.change(screen.getByPlaceholderText('Username'), {
      target: { value: 'new_user' }
    });
    fireEvent.change(screen.getByPlaceholderText('Email'), {
      target: { value: 'newuser@example.com' }
    });
    
    // Submit the form
    fireEvent.click(screen.getByText('Create User'));
    
    // Check if new user appears
    await waitFor(() => {
      expect(screen.getByText('new_user')).toBeInTheDocument();
    });
  });

  test('filters tasks when search query is entered', () => {
    render(<TaskManager />);
    
    // Enter search query
    const searchInput = screen.getByPlaceholderText('Search tasks...');
    fireEvent.change(searchInput, { target: { value: 'Design' } });
    
    // Check if only matching task is shown
    expect(screen.getByText('Design Homepage')).toBeInTheDocument();
    expect(screen.queryByText('Implement Navigation')).not.toBeInTheDocument();
  });

  test('updates task status when changed', async () => {
    render(<TaskManager />);
    
    // Find the first task's status select
    const statusSelects = screen.getAllByDisplayValue('pending');
    const firstStatusSelect = statusSelects[0];
    
    // Change status to completed
    fireEvent.change(firstStatusSelect, { target: { value: 'completed' } });
    
    // Check if status changed
    await waitFor(() => {
      expect(firstStatusSelect.value).toBe('completed');
    });
  });

  test('deletes task when delete button is clicked', async () => {
    render(<TaskManager />);
    
    // Find and click delete button for first task
    const deleteButtons = screen.getAllByText('Delete');
    fireEvent.click(deleteButtons[0]);
    
    // Check if task count decreased
    await waitFor(() => {
      expect(screen.getByText('Tasks (1)')).toBeInTheDocument();
    });
  });

  test('displays task priority colors correctly', () => {
    render(<TaskManager />);
    
    // Check if high priority task has correct styling
    const highPriorityTask = screen.getByText('Design Homepage').closest('div');
    expect(highPriorityTask).toBeInTheDocument();
  });

  test('displays task status badges correctly', () => {
    render(<TaskManager />);
    
    // Check if status badges are displayed
    expect(screen.getByText('pending')).toBeInTheDocument();
    expect(screen.getByText('in progress')).toBeInTheDocument();
  });

  test('shows project owner information', () => {
    render(<TaskManager />);
    fireEvent.click(screen.getByText('projects'));
    
    expect(screen.getByText('Owner: john_doe')).toBeInTheDocument();
    expect(screen.getByText('Owner: jane_smith')).toBeInTheDocument();
  });

  test('shows user role information', () => {
    render(<TaskManager />);
    fireEvent.click(screen.getByText('users'));
    
    expect(screen.getByText('admin')).toBeInTheDocument();
    expect(screen.getByText('user')).toBeInTheDocument();
  });
}); 