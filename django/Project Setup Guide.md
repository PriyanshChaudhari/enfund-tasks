# Project Setup Guide

## Prerequisites

1. **Python**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. **Django**: Install Django using pip:

    ```sh
    pip install django
    ```

3. **Django Channels**: Install Django Channels for WebSocket support:

    ```sh
    pip install channels
    ```

4. **Daphne**: Install Daphne for ASGI server support:

    ```sh
    pip install daphne
    ```

## Setup

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/PriyanshChaudhari/enfund-tasks.git
    cd django/enfund_chat_project
    ```

2. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Apply Migrations**:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Create a Superuser**:

    ```sh
    python manage.py createsuperuser
    ```

## Running the Project

1. **Start the Django Development Server**:

    ```sh
    python manage.py runserver
    ```

2. **Access the Application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Additional Information

- **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
- **Login**: Use the homepage at `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/accounts/login` to log in to the application.

- **WebSocket Configuration**:
  - **ASGI Configuration**: Ensure that your `asgi.py` file is properly configured for Django Channels.
