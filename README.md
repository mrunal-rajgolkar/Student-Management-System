# Student Management System

The Student Management System is a Django-based web application that allows users to manage student details such as name, age, city, email, and phone number. The application features user authentication, enabling users to sign up, log in, and manage student information in a MySQL database.

## Features

- **User Authentication**: Secure sign-up and login system.
- **Student Management**: Add, edit, or delete student details.
- **MySQL Database**: All data is stored in a MySQL database.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine.
- Django installed (`pip install django`).
- MySQL installed and running.
- Git installed on your local machine.

## Cloning the Repository

To clone the repository, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

    ```bash
    git clone https://github.com/mrunal-rajgolkar/Student-Management-System.git
    ```

4. Navigate into the cloned directory:

    ```bash
    cd Student-Management-System
    ```

## Setting Up the Project

1. **Install the required packages:**

    Make sure you have a virtual environment set up. If not, you can create one using:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

    Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. **Configure the Database:**

    Open the `settings.py` file located in the `StudentManagementSystem` directory. Replace the existing `DATABASES` configuration with your local MySQL database credentials:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_db_name',      # Replace with your database name
            'USER': 'your_db_user',      # Replace with your database user
            'PASSWORD': 'your_password', # Replace with your database password
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

3. **Migrate the Database:**

    After setting up the database configuration, run the following command to apply the migrations:

    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser:**

    To access the Django admin panel, create a superuser with the following command:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up your superuser credentials.

5. **Run the Development Server:**

    Start the Django development server with the following command:

    ```bash
    python manage.py runserver
    ```

    Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application.

## Usage

- **Sign Up**: Register a new user account.
- **Log In**: Access your account to manage student information.
- **Add Student**: Add new student details to the database.
- **Edit Student**: Modify existing student details.
- **Delete Student**: Remove a student from the database.

