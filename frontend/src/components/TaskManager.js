import React, { useState, useEffect } from 'react';

const TaskManager = () => {
  const [tasks, setTasks] = useState([]);
  const [projects, setProjects] = useState([]);
  const [users, setUsers] = useState([]);
  const [newTask, setNewTask] = useState({
    title: '',
    description: '',
    projectId: '',
    assigneeId: '',
    priority: 'medium',
    dueDate: ''
  });
  const [newProject, setNewProject] = useState({
    name: '',
    description: '',
    ownerId: ''
  });
  const [newUser, setNewUser] = useState({
    username: '',
    email: '',
    role: 'user'
  });
  const [activeTab, setActiveTab] = useState('tasks');
  const [searchQuery, setSearchQuery] = useState('');

  // Mock data for demonstration (in real app, this would come from API)
  useEffect(() => {
    // Simulate loading data
    setUsers([
      { id: '1', username: 'john_doe', email: 'john@example.com', role: 'admin' },
      { id: '2', username: 'jane_smith', email: 'jane@example.com', role: 'user' }
    ]);
    
    setProjects([
      { id: '1', name: 'Website Redesign', description: 'Redesign company website', ownerId: '1' },
      { id: '2', name: 'Mobile App', description: 'Develop mobile application', ownerId: '2' }
    ]);
    
    setTasks([
      { 
        id: '1', 
        title: 'Design Homepage', 
        description: 'Create new homepage design', 
        projectId: '1', 
        assigneeId: '2',
        status: 'pending',
        priority: 'high',
        dueDate: '2024-02-01'
      },
      { 
        id: '2', 
        title: 'Implement Navigation', 
        description: 'Build navigation menu', 
        projectId: '1', 
        assigneeId: '1',
        status: 'in_progress',
        priority: 'medium',
        dueDate: '2024-01-15'
      }
    ]);
  }, []);

  const handleCreateTask = () => {
    if (newTask.title && newTask.description && newTask.projectId && newTask.assigneeId) {
      const task = {
        id: Date.now().toString(),
        ...newTask,
        status: 'pending',
        createdAt: new Date().toISOString()
      };
      setTasks([...tasks, task]);
      setNewTask({
        title: '',
        description: '',
        projectId: '',
        assigneeId: '',
        priority: 'medium',
        dueDate: ''
      });
    }
  };

  const handleCreateProject = () => {
    if (newProject.name && newProject.description && newProject.ownerId) {
      const project = {
        id: Date.now().toString(),
        ...newProject,
        status: 'active',
        createdAt: new Date().toISOString()
      };
      setProjects([...projects, project]);
      setNewProject({
        name: '',
        description: '',
        ownerId: ''
      });
    }
  };

  const handleCreateUser = () => {
    if (newUser.username && newUser.email) {
      const user = {
        id: Date.now().toString(),
        ...newUser,
        isActive: true,
        createdAt: new Date().toISOString()
      };
      setUsers([...users, user]);
      setNewUser({
        username: '',
        email: '',
        role: 'user'
      });
    }
  };

  const updateTaskStatus = (taskId, newStatus) => {
    setTasks(tasks.map(task => 
      task.id === taskId ? { ...task, status: newStatus } : task
    ));
  };

  const deleteTask = (taskId) => {
    setTasks(tasks.filter(task => task.id !== taskId));
  };

  const filteredTasks = tasks.filter(task => 
    task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    task.description.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const getStatusColor = (status) => {
    switch (status) {
      case 'completed': return 'bg-green-500';
      case 'in_progress': return 'bg-blue-500';
      case 'pending': return 'bg-yellow-500';
      case 'cancelled': return 'bg-red-500';
      default: return 'bg-gray-500';
    }
  };

  const getPriorityColor = (priority) => {
    switch (priority) {
      case 'high': return 'text-red-600';
      case 'medium': return 'text-yellow-600';
      case 'low': return 'text-green-600';
      default: return 'text-gray-600';
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">
          🚀 Task Management System
        </h1>

        {/* Navigation Tabs */}
        <div className="flex space-x-1 bg-white rounded-lg p-1 mb-6">
          {['tasks', 'projects', 'users'].map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`px-4 py-2 rounded-md font-medium capitalize ${
                activeTab === tab
                  ? 'bg-blue-500 text-white'
                  : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              {tab}
            </button>
          ))}
        </div>

        {/* Search Bar */}
        <div className="mb-6">
          <input
            type="text"
            placeholder="Search tasks..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>

        {/* Tasks Tab */}
        {activeTab === 'tasks' && (
          <div className="space-y-6">
            {/* Create Task Form */}
            <div className="bg-white rounded-lg p-6 shadow-sm">
              <h2 className="text-xl font-semibold mb-4">Create New Task</h2>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <input
                  type="text"
                  placeholder="Task Title"
                  value={newTask.title}
                  onChange={(e) => setNewTask({...newTask, title: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                />
                <textarea
                  placeholder="Description"
                  value={newTask.description}
                  onChange={(e) => setNewTask({...newTask, description: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                />
                <select
                  value={newTask.projectId}
                  onChange={(e) => setNewTask({...newTask, projectId: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                >
                  <option value="">Select Project</option>
                  {projects.map(project => (
                    <option key={project.id} value={project.id}>{project.name}</option>
                  ))}
                </select>
                <select
                  value={newTask.assigneeId}
                  onChange={(e) => setNewTask({...newTask, assigneeId: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                >
                  <option value="">Select Assignee</option>
                  {users.map(user => (
                    <option key={user.id} value={user.id}>{user.username}</option>
                  ))}
                </select>
                <select
                  value={newTask.priority}
                  onChange={(e) => setNewTask({...newTask, priority: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                >
                  <option value="low">Low Priority</option>
                  <option value="medium">Medium Priority</option>
                  <option value="high">High Priority</option>
                </select>
                <input
                  type="date"
                  value={newTask.dueDate}
                  onChange={(e) => setNewTask({...newTask, dueDate: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                />
              </div>
              <button
                onClick={handleCreateTask}
                className="mt-4 px-6 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
              >
                Create Task
              </button>
            </div>

            {/* Tasks List */}
            <div className="bg-white rounded-lg shadow-sm">
              <div className="px-6 py-4 border-b border-gray-200">
                <h2 className="text-xl font-semibold">Tasks ({filteredTasks.length})</h2>
              </div>
              <div className="divide-y divide-gray-200">
                {filteredTasks.map(task => (
                  <div key={task.id} className="px-6 py-4 hover:bg-gray-50">
                    <div className="flex items-center justify-between">
                      <div className="flex-1">
                        <div className="flex items-center space-x-3">
                          <h3 className="text-lg font-medium text-gray-900">{task.title}</h3>
                          <span className={`px-2 py-1 text-xs font-medium rounded-full ${getStatusColor(task.status)} text-white`}>
                            {task.status.replace('_', ' ')}
                          </span>
                          <span className={`px-2 py-1 text-xs font-medium rounded-full ${getPriorityColor(task.priority)}`}>
                            {task.priority}
                          </span>
                        </div>
                        <p className="text-gray-600 mt-1">{task.description}</p>
                        <div className="flex items-center space-x-4 mt-2 text-sm text-gray-500">
                          <span>Project: {projects.find(p => p.id === task.projectId)?.name}</span>
                          <span>Assignee: {users.find(u => u.id === task.assigneeId)?.username}</span>
                          {task.dueDate && <span>Due: {task.dueDate}</span>}
                        </div>
                      </div>
                      <div className="flex items-center space-x-2">
                        <select
                          value={task.status}
                          onChange={(e) => updateTaskStatus(task.id, e.target.value)}
                          className="px-3 py-1 border border-gray-300 rounded-md text-sm"
                        >
                          <option value="pending">Pending</option>
                          <option value="in_progress">In Progress</option>
                          <option value="completed">Completed</option>
                          <option value="cancelled">Cancelled</option>
                        </select>
                        <button
                          onClick={() => deleteTask(task.id)}
                          className="px-3 py-1 bg-red-500 text-white rounded-md text-sm hover:bg-red-600"
                        >
                          Delete
                        </button>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Projects Tab */}
        {activeTab === 'projects' && (
          <div className="space-y-6">
            {/* Create Project Form */}
            <div className="bg-white rounded-lg p-6 shadow-sm">
              <h2 className="text-xl font-semibold mb-4">Create New Project</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <input
                  type="text"
                  placeholder="Project Name"
                  value={newProject.name}
                  onChange={(e) => setNewProject({...newProject, name: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                />
                <textarea
                  placeholder="Description"
                  value={newProject.description}
                  onChange={(e) => setNewProject({...newProject, description: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                />
                <select
                  value={newProject.ownerId}
                  onChange={(e) => setNewProject({...newProject, ownerId: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                >
                  <option value="">Select Owner</option>
                  {users.map(user => (
                    <option key={user.id} value={user.id}>{user.username}</option>
                  ))}
                </select>
              </div>
              <button
                onClick={handleCreateProject}
                className="mt-4 px-6 py-2 bg-green-500 text-white rounded-md hover:bg-green-600"
              >
                Create Project
              </button>
            </div>

            {/* Projects List */}
            <div className="bg-white rounded-lg shadow-sm">
              <div className="px-6 py-4 border-b border-gray-200">
                <h2 className="text-xl font-semibold">Projects ({projects.length})</h2>
              </div>
              <div className="divide-y divide-gray-200">
                {projects.map(project => (
                  <div key={project.id} className="px-6 py-4">
                    <h3 className="text-lg font-medium text-gray-900">{project.name}</h3>
                    <p className="text-gray-600 mt-1">{project.description}</p>
                    <div className="flex items-center space-x-4 mt-2 text-sm text-gray-500">
                      <span>Owner: {users.find(u => u.id === project.ownerId)?.username}</span>
                      <span>Tasks: {tasks.filter(t => t.projectId === project.id).length}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Users Tab */}
        {activeTab === 'users' && (
          <div className="space-y-6">
            {/* Create User Form */}
            <div className="bg-white rounded-lg p-6 shadow-sm">
              <h2 className="text-xl font-semibold mb-4">Create New User</h2>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <input
                  type="text"
                  placeholder="Username"
                  value={newUser.username}
                  onChange={(e) => setNewUser({...newUser, username: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                />
                <input
                  type="email"
                  placeholder="Email"
                  value={newUser.email}
                  onChange={(e) => setNewUser({...newUser, email: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                />
                <select
                  value={newUser.role}
                  onChange={(e) => setNewUser({...newUser, role: e.target.value})}
                  className="px-3 py-2 border border-gray-300 rounded-md"
                >
                  <option value="user">User</option>
                  <option value="admin">Admin</option>
                </select>
              </div>
              <button
                onClick={handleCreateUser}
                className="mt-4 px-6 py-2 bg-purple-500 text-white rounded-md hover:bg-purple-600"
              >
                Create User
              </button>
            </div>

            {/* Users List */}
            <div className="bg-white rounded-lg shadow-sm">
              <div className="px-6 py-4 border-b border-gray-200">
                <h2 className="text-xl font-semibold">Users ({users.length})</h2>
              </div>
              <div className="divide-y divide-gray-200">
                {users.map(user => (
                  <div key={user.id} className="px-6 py-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <h3 className="text-lg font-medium text-gray-900">{user.username}</h3>
                        <p className="text-gray-600">{user.email}</p>
                        <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800 mt-1">
                          {user.role}
                        </span>
                      </div>
                      <div className="text-sm text-gray-500">
                        Tasks: {tasks.filter(t => t.assigneeId === user.id).length}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default TaskManager; 