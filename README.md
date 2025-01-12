# Enfund Tasks

This repository contains tasks related to frontend development, Django, and AWS. Below are the details of the available files and code structure.

## File Structure
<!-- enfund/  -->

    ├── frontend/ 
    │ ├── Q1.html 
    │ ├── Q1.css 
    │ └── Q1.js
    ├── django/ 
    │ └── enfund_chat_project/ 
    │   ├── manage.py
    │   ├── enfund_chat_project/
    │   │ ├── settings.py
    │   │ ├── urls.py
    │   │ ├── asgi.py
    │   │ ├── wsgi.py
    │   │ ├── consumers.py
    │   │ └── routing.py
    │   ├── chatapp/
    │   │ ├── admin.py
    │   │ ├── apps.py
    │   │ ├── models.py
    │   │ ├── urls.py
    │   │ └── views.py
    │   └── templates/
    │     ├── registration/
    │     │ └── login.html
    │     ├── base.html
    │     ├── chat.html
    │     ├── home.html
    │     └── user_list.html
    ├── aws/ 
    │ ├── Q1.py 
    │ ├── Q2.py
    │ └── Q3.md

## Frontend Development

- `Q1.html`: HTML file for the webpage structure.
- `Q1.css`: CSS file for styling the webpage.
- `Q1.js`: JavaScript file for page scaling function.

## Django

- `manage.py`: Django project management script.
- `enfund_chat_project/`: Django project directory.
  - `enfund_chat_project/`: Main Django project settings and configuration.
    - `settings.py`: Django settings configuration.
    - `urls.py`: URL routing for the Django project.
    - `asgi.py`: ASGI configuration for asynchronous support.
    - `wsgi.py`: WSGI configuration for deployment.
    - `consumers.py`: WebSocket consumers for handling real-time communication.
    - `routing.py`: WebSocket URL routing.
  - `chatapp/`: Django app for the chat application using channels.
    - `admin.py`: Admin configuration for the chat app.
    - `apps.py`: App configuration for the chat app.
    - `models.py`: Models for the chat app, including the `Message` model.
    - `urls.py`: URL routing for the chat app.
    - `views.py`: Views for handling chat and home page rendering.
    - `migrations/`: Database migrations for the chat app.
    - `templates/`: HTML templates for the chat app.
      - `base.html`: Base template for the project.
      - `chat.html`: Template for the chat page.
      - `home.html`: Template for the home page.
      - `registration/login.html`: Template for the login page.

## AWS

- `Q1.py`: AWS Lambda function to add two numbers.
- `Q2.py`: AWS Lambda function to store a document in an S3 bucket.
- `Q3.md`: AWS theory answers.
