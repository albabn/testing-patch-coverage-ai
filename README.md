# 🚀 Task Management System

A comprehensive task management system with Python backend and React frontend, designed to demonstrate code coverage tracking across multiple languages.

## 🏗️ Project Structure

```
project/
├── backend/                 # Python backend
│   ├── src/
│   │   └── core/
│   │       ├── task_manager.py    # Main task management logic
│   │       ├── calculator.py      # Legacy calculator functions
│   │       └── advanced_math.py   # Advanced math operations
│   ├── tests/
│   │   ├── test_task_manager.py   # Task manager tests
│   │   └── test_calculator.py     # Calculator tests
│   └── requirements.txt
├── frontend/               # React frontend
│   ├── src/
│   │   └── components/
│   │       └── TaskManager.js     # Main React component
│   ├── tests/
│   │   └── TaskManager.test.js    # React component tests
│   └── package.json
├── .github/workflows/      # GitHub Actions workflows
└── docs/                   # Documentation
```

## 🎯 Features

### Backend (Python)
- **User Management**: Create, deactivate, and manage user roles
- **Project Management**: Create projects with owners and members
- **Task Management**: Full CRUD operations for tasks
- **Advanced Features**: Due dates, priorities, tags, search
- **Validation**: Comprehensive error handling and validation

### Frontend (React)
- **Modern UI**: Clean, responsive interface with Tailwind CSS
- **Tab Navigation**: Separate views for tasks, projects, and users
- **Real-time Updates**: Dynamic task status changes and filtering
- **Form Handling**: Create new tasks, projects, and users
- **Search Functionality**: Filter tasks by title or description

## 🚀 Getting Started

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests with coverage:**
   ```bash
   pytest --cov=. --cov-report=term --cov-report=xml
   ```

4. **Run the task manager demo:**
   ```bash
   python src/core/task_manager.py
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Run tests with coverage:**
   ```bash
   npm test
   ```

4. **Start development server:**
   ```bash
   npm start
   ```

## 📊 Code Coverage

### Current Coverage Status
- **Backend (Python)**: Comprehensive tests for all core functionality
- **Frontend (React)**: Full component testing with user interactions
- **Overall Coverage**: Mixed language coverage tracking

### Coverage Reports
- **Python**: pytest-cov with XML and HTML reports
- **JavaScript**: Jest with coverage reporting
- **Datadog Integration**: Automatic coverage upload on CI/CD

## 🔧 Testing

### Python Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=term --cov-report=xml

# Run specific test file
pytest tests/test_task_manager.py
```

### React Tests
```bash
# Run all tests
npm test

# Run with coverage
npm test -- --coverage --watchAll=false

# Run tests in watch mode
npm run test:watch
```

## 🚀 GitHub Actions

The project includes automated workflows that:
1. **Run tests** for both Python and JavaScript
2. **Generate coverage reports** in multiple formats
3. **Upload coverage** to Datadog automatically
4. **Track coverage changes** across commits and PRs

## 📈 Datadog Integration

- **Automatic Coverage Upload**: Every PR and push triggers coverage upload
- **Multi-language Support**: Python and JavaScript coverage in one dashboard
- **Historical Tracking**: Monitor coverage trends over time
- **PR Comments**: Automatic coverage percentage display on PRs

## 🎨 UI Components

### Task Management
- Create, edit, and delete tasks
- Assign priorities and due dates
- Track task status (pending, in progress, completed, cancelled)
- Search and filter tasks

### Project Management
- Create projects with descriptions
- Assign project owners
- Track project members
- View project statistics

### User Management
- User registration and role management
- Admin and user roles
- User activity tracking
- Task assignment tracking

## 🔍 Code Quality

- **Type Hints**: Full Python type annotations
- **Error Handling**: Comprehensive validation and error messages
- **Testing**: High test coverage for both languages
- **Documentation**: Clear docstrings and comments
- **Modern Practices**: React hooks, functional components, modern Python

## 🚀 Future Enhancements

- **Database Integration**: Replace in-memory storage with persistent database
- **Authentication**: JWT-based user authentication
- **Real-time Updates**: WebSocket integration for live updates
- **Mobile App**: React Native mobile application
- **API Documentation**: OpenAPI/Swagger documentation
- **Performance Monitoring**: Application performance metrics

## 📝 License

This project is designed for educational purposes and demonstrating code coverage tracking across multiple programming languages.

---

**Built with ❤️ for learning code coverage and multi-language development**