#!/usr/bin/env python3
import pytest
from datetime import datetime, timedelta
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from core.task_manager import TaskManager, User, Project, Task


class TestUser:
    """Test User class functionality."""
    
    def test_user_creation(self):
        """Test user creation with basic attributes."""
        user = User("test_user", "test@example.com", "admin")
        assert user.username == "test_user"
        assert user.email == "test@example.com"
        assert user.role == "admin"
        assert user.is_active is True
        assert user.id is not None
    
    def test_user_deactivation(self):
        """Test user deactivation."""
        user = User("test_user", "test@example.com")
        user.deactivate()
        assert user.is_active is False
    
    def test_user_role_change(self):
        """Test user role change."""
        user = User("test_user", "test@example.com", "user")
        user.change_role("admin")
        assert user.role == "admin"


class TestProject:
    """Test Project class functionality."""
    
    def test_project_creation(self):
        """Test project creation."""
        owner_id = "owner123"
        project = Project("Test Project", "Test Description", owner_id)
        assert project.name == "Test Project"
        assert project.description == "Test Description"
        assert project.owner_id == owner_id
        assert project.status == "active"
        assert owner_id in project.members
    
    def test_add_member(self):
        """Test adding member to project."""
        project = Project("Test Project", "Test Description", "owner123")
        project.add_member("member123")
        assert "member123" in project.members
    
    def test_remove_member(self):
        """Test removing member from project."""
        project = Project("Test Project", "Test Description", "owner123")
        project.add_member("member123")
        project.remove_member("member123")
        assert "member123" not in project.members
    
    def test_cannot_remove_owner(self):
        """Test that owner cannot be removed."""
        owner_id = "owner123"
        project = Project("Test Project", "Test Description", owner_id)
        project.remove_member(owner_id)
        assert owner_id in project.members  # Owner should still be there


class TestTask:
    """Test Task class functionality."""
    
    def test_task_creation(self):
        """Test task creation."""
        task = Task("Test Task", "Test Description", "project123", "user123")
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.project_id == "project123"
        assert task.assignee_id == "user123"
        assert task.status == "pending"
        assert task.priority == "medium"
    
    def test_set_due_date(self):
        """Test setting due date."""
        task = Task("Test Task", "Test Description", "project123", "user123")
        due_date = datetime.now() + timedelta(days=7)
        task.set_due_date(due_date)
        assert task.due_date == due_date
    
    def test_change_status(self):
        """Test changing task status."""
        task = Task("Test Task", "Test Description", "project123", "user123")
        task.change_status("in_progress")
        assert task.status == "in_progress"
    
    def test_invalid_status_change(self):
        """Test invalid status change."""
        task = Task("Test Task", "Test Description", "project123", "user123")
        task.change_status("invalid_status")
        assert task.status == "pending"  # Should remain unchanged
    
    def test_add_tag(self):
        """Test adding tag to task."""
        task = Task("Test Task", "Test Description", "project123", "user123")
        task.add_tag("urgent")
        assert "urgent" in task.tags
    
    def test_duplicate_tag(self):
        """Test adding duplicate tag."""
        task = Task("Test Task", "Test Description", "project123", "user123")
        task.add_tag("urgent")
        task.add_tag("urgent")
        assert task.tags.count("urgent") == 1
    
    def test_is_overdue(self):
        """Test overdue task detection."""
        task = Task("Test Task", "Test Description", "project123", "user123")
        # Set due date in the past
        task.set_due_date(datetime.now() - timedelta(days=1))
        assert task.is_overdue() is True
    
    def test_not_overdue(self):
        """Test non-overdue task."""
        task = Task("Test Task", "Test Description", "project123", "user123")
        # Set due date in the future
        task.set_due_date(datetime.now() + timedelta(days=1))
        assert task.is_overdue() is False
    
    def test_completed_task_not_overdue(self):
        """Test completed task is not overdue."""
        task = Task("Test Task", "Test Description", "project123", "user123")
        task.set_due_date(datetime.now() - timedelta(days=1))
        task.change_status("completed")
        assert task.is_overdue() is False


class TestTaskManager:
    """Test TaskManager class functionality."""
    
    def setup_method(self):
        """Set up test environment before each test."""
        self.tm = TaskManager()
        self.user1_id = self.tm.create_user("user1", "user1@example.com")
        self.user2_id = self.tm.create_user("user2", "user2@example.com")
        self.project_id = self.tm.create_project("Test Project", "Test Description", self.user1_id)
    
    def test_create_user(self):
        """Test user creation in task manager."""
        user_id = self.tm.create_user("new_user", "new@example.com", "admin")
        assert user_id in self.tm.users
        assert self.tm.users[user_id].username == "new_user"
        assert self.tm.users[user_id].role == "admin"
    
    def test_create_project(self):
        """Test project creation in task manager."""
        project_id = self.tm.create_project("New Project", "New Description", self.user1_id)
        assert project_id in self.tm.projects
        assert self.tm.projects[project_id].name == "New Project"
    
    def test_create_project_invalid_owner(self):
        """Test project creation with invalid owner."""
        with pytest.raises(ValueError, match="Owner user does not exist"):
            self.tm.create_project("New Project", "New Description", "invalid_user_id")
    
    def test_create_task(self):
        """Test task creation in task manager."""
        task_id = self.tm.create_task("New Task", "New Description", self.project_id, self.user2_id)
        assert task_id in self.tm.tasks
        assert self.tm.tasks[task_id].title == "New Task"
    
    def test_create_task_invalid_project(self):
        """Test task creation with invalid project."""
        with pytest.raises(ValueError, match="Project does not exist"):
            self.tm.create_task("New Task", "New Description", "invalid_project_id", self.user2_id)
    
    def test_create_task_invalid_assignee(self):
        """Test task creation with invalid assignee."""
        with pytest.raises(ValueError, match="Assignee user does not exist"):
            self.tm.create_task("New Task", "New Description", self.project_id, "invalid_user_id")
    
    def test_get_user_tasks(self):
        """Test getting tasks for a specific user."""
        task_id = self.tm.create_task("User Task", "Description", self.project_id, self.user2_id)
        user_tasks = self.tm.get_user_tasks(self.user2_id)
        assert len(user_tasks) == 1
        assert user_tasks[0].id == task_id
    
    def test_get_project_tasks(self):
        """Test getting tasks for a specific project."""
        task_id = self.tm.create_task("Project Task", "Description", self.project_id, self.user1_id)
        project_tasks = self.tm.get_project_tasks(self.project_id)
        assert len(project_tasks) == 1
        assert project_tasks[0].id == task_id
    
    def test_get_overdue_tasks(self):
        """Test getting overdue tasks."""
        task = self.tm.create_task("Overdue Task", "Description", self.project_id, self.user1_id)
        # Set due date in the past
        self.tm.tasks[task].set_due_date(datetime.now() - timedelta(days=1))
        overdue_tasks = self.tm.get_overdue_tasks()
        assert len(overdue_tasks) == 1
        assert overdue_tasks[0].id == task
    
    def test_search_tasks(self):
        """Test task search functionality."""
        self.tm.create_task("Searchable Task", "This is searchable", self.project_id, self.user1_id)
        self.tm.create_task("Another Task", "Not searchable", self.project_id, self.user2_id)
        
        search_results = self.tm.search_tasks("searchable")
        assert len(search_results) == 1
        assert search_results[0].title == "Searchable Task" 