# NewsSite

NewsSite is a web application built with Django that allows users to read, comment on, and share news articles. The application includes a user authentication system, an admin interface for managing articles, and a responsive design for a seamless experience across devices.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Features

- **User authentication** (login, registration, password reset)
- **Create, read, update, and delete (CRUD) operations for news articles**
- **Comment on articles**
- **Admin interface for managing users and articles**
- **Responsive design for mobile and desktop**

## Installation

### Prerequisites

- **Python 3.x**
- **Django 3.x**
- **pip (Python package installer)**

### Clone the Repository

```bash
git clone https://github.com/Mag1ck/NewsSite.git
cd NewsSite

```

### Set Up a Virtual Environment

```bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

### Install Dependencies

```bash

pip install -r requirements.txt

```
### Apply Migrations

```bash

python manage.py migrate

```

### Create a Superuser

```bash

python manage.py createsuperuser

```

### Run the Development Server

```bash

python manage.py runserver

```

Visit http://127.0.0.1:8000 in your browser to view the application.

## Usage

### User Authentication

- **Register for a new account or log in with an existing account.**
- **Reset your password if you've forgotten it.**

 ### Managing Articles

- **Create new articles from the admin interface or your user profile if you have the required permissions.**
- **Edit or delete articles you have created.**

 ### Commenting

- **Comment on articles to share your thoughts.**
- **Manage your comments through your user profile.**

## Configuration

### Environment Variables

The application uses environment variables for configuration. Create a .env file in the project root and add the following variables:

```bash

DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
ALLOWED_HOSTS=127.0.0.1, .yourdomain.com

```
### Settings
Edit the settings.py file to configure the application according to your needs. Refer to the Django documentation for detailed information on each setting.

