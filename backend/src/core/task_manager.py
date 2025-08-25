#!/usr/bin/env python3
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import uuid


class User:
    """User class for authentication and authorization."""
    
    def __init__(self, username: str, email: str, role: str = "user"):
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.role = role
        self.created_at = datetime.now()
        self.is_active = True
    
    def deactivate(self):
        """Deactivate user account."""
        self.is_active = False
    
    def change_role(self, new_role: str):
        """Change user role."""
        self.role = new_role


class Project:
    """Project class for organizing tasks."""
    
    def __init__(self, name: str, description: str, owner_id: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.created_at = datetime.now()
        self.status = "active"
        self.members: List[str] = [owner_id]
    
    def add_member(self, user_id: str):
        """Add member to project."""
        if user_id not in self.members:
            self.members.append(user_id)
    
    def remove_member(self, user_id: str):
        """Remove member from project."""
        if user_id in self.members and user_id != self.owner_id:
            self.members.remove(user_id)


class Task:
    """Task class for individual work items."""
    
    def __init__(self, title: str, description: str, project_id: str, assignee_id: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.project_id = project_id
        self.assignee_id = assignee_id
        self.created_at = datetime.now()
        self.due_date: Optional[datetime] = None
        self.status = "pending"
        self.priority = "medium"
        self.tags: List[str] = []
    
    def set_due_date(self, due_date: datetime):
        """Set task due date."""
        self.due_date = due_date
    
    def change_status(self, new_status: str):
        """Change task status."""
        valid_statuses = ["pending", "in_progress", "completed", "cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
    
    def add_tag(self, tag: str):
        """Add tag to task."""
        if tag not in self.tags:
            self.tags.append(tag)
    
    def is_overdue(self) -> bool:
        """Check if task is overdue."""
        if self.due_date and self.status != "completed":
            return datetime.now() > self.due_date
        return False


class TaskManager:
    """Main task management system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.projects: Dict[str, Project] = {}
        self.tasks: Dict[str, Task] = {}
    
    def create_user(self, username: str, email: str, role: str = "user") -> str:
        """Create a new user."""
        user = User(username, email, role)
        self.users[user.id] = user
        return user.id
    
    def create_project(self, name: str, description: str, owner_id: str) -> str:
        """Create a new project."""
        if owner_id not in self.users:
            raise ValueError("Owner user does not exist")
        project = Project(name, description, owner_id)
        self.projects[project.id] = project
        return project.id
    
    def create_task(self, title: str, description: str, project_id: str, assignee_id: str) -> str:
        """Create a new task."""
        if project_id not in self.projects:
            raise ValueError("Project does not exist")
        if assignee_id not in self.users:
            raise ValueError("Assignee user does not exist")
        task = Task(title, description, project_id, assignee_id)
        self.tasks[task.id] = task
        return task.id
    
    def get_user_tasks(self, user_id: str) -> List[Task]:
        """Get all tasks assigned to a user."""
        return [task for task in self.tasks.values() if task.assignee_id == user_id]
    
    def get_project_tasks(self, project_id: str) -> List[Task]:
        """Get all tasks in a project."""
        return [task for task in self.tasks.values() if task.project_id == project_id]
    
    def get_overdue_tasks(self) -> List[Task]:
        """Get all overdue tasks."""
        return [task for task in self.tasks.values() if task.is_overdue()]
    
    def search_tasks(self, query: str) -> List[Task]:
        """Search tasks by title or description."""
        query_lower = query.lower()
        return [
            task for task in self.tasks.values()
            if query_lower in task.title.lower() or query_lower in task.description.lower()
        ]


if __name__ == "__main__":
    # Example usage when run as script
    print("🚀 Task Management System Demo")
    print("=" * 40)
    
    # Initialize system
    tm = TaskManager()
    
    # Create users
    user1_id = tm.create_user("john_doe", "john@example.com", "admin")
    user2_id = tm.create_user("jane_smith", "jane@example.com", "user")
    
    # Create project
    project_id = tm.create_project("Website Redesign", "Redesign company website", user1_id)
    
    # Create tasks
    task1_id = tm.create_task("Design Homepage", "Create new homepage design", project_id, user2_id)
    task2_id = tm.create_task("Implement Navigation", "Build navigation menu", project_id, user1_id)
    
    # Get some data
    user_tasks = tm.get_user_tasks(user2_id)
    project_tasks = tm.get_project_tasks(project_id)
    
    print(f"Created {len(tm.users)} users")
    print(f"Created {len(tm.projects)} projects")
    print(f"Created {len(tm.tasks)} tasks")
    print(f"User {user2_id} has {len(user_tasks)} tasks")
    print(f"Project {project_id} has {len(project_tasks)} tasks")
    
    print("\n✨ Task Management System is ready to use!") 