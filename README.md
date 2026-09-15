# Django Task Management System

A simple multi-user task management web application built with Django. Users can create and manage their own tasks, track their progress, and view their task statistics from the dashboard.

## Features

* User registration and login
* User-specific tasks
* Create, view, update and delete tasks
* Mark tasks as completed
* Search tasks
* Add due date and due time
* Dashboard with task statistics
* Pending, completed and overdue task counts
* Django Admin Panel

## Technologies

* Python
* Django
* SQLite
* HTML
* CSS

## Project Structure

```text
TODO/
│
├── base/
│   ├── migrations/
│   ├── templates/
│   │   └── base/
│   │       ├── dashboard.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── task_detail.html
│   │       ├── task_form.html
│   │       └── task_list.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── TODO/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── db.sqlite3
```

## Dashboard

The dashboard gives the user a quick overview of their tasks.

It displays:

* Total tasks
* Pending tasks
* Completed tasks
* Overdue tasks

## Authentication

Django's built-in authentication system is used for user registration, login and logout.

Tasks are connected to the logged-in user, so each user can manage their own tasks.

## Running the Project

Clone the repository and open the project folder:

```bash
git clone <your-repository-url>
cd TODO
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install Django:

```bash
pip install django
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Screenshots

### Login
![Login Page](screenshots/login.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Task List
![Task List](screenshots/task-list.png)

### Add Task
![Add Task](screenshots/add-task.png)

## About the Project

This is my first Django project. I built it while learning Django and used it to understand how models, views, URLs, templates, forms, authentication and databases work together in a web application.

## Author

**Swati Vishnoi**

