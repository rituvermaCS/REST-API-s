## True-Value-Access-Task

# Main points for creating a REST API in Django.

 find out steps to creating a REST API.

    Set-Up Virtual Environment.
    Set-Up Django
    Create a model for the database that the Django ORM will manage.
    Set-Up Django Rest Framework
    Serialize the model data from step-3
    Create the URI endpoint to view the serialized data.

# 1. Set-Up Virtual Environment

sudo apt update

sudo apt install python3-django

sudo apt install python3-pip

sudo apt install python3-venv

mkdir True-Value-Access

cd True-Value-Access

python3.6 -m venv my_env

source myenv/bin/activate

# 2. Set-Up Django

pip install django

django-admin startproject ToDo

# Check Django Server is working properly or not

python manage.py runserver

# Creating the app

python manage.py startapp api

# Migrate the database

python manage.py makemigrations

python manage.py migrate

# Create Super User

python manage.py createsuperuser

python manage.py runserver

# 3.Set-Up the Django Rest Framework

pip install djangorestframework

python manage.py runserver

# Root Path for localhost

API Overview: http://127.0.0.1:8000/

Display all data: http://127.0.0.1:8000/task-list/

Display single data: http://127.0.0.1:8000/task-detail/id/

Update an existing data: http://127.0.0.1:8000/task-update/id/

Creating a new data: http://127.0.0.1:8000/task-create/

Delete existing data by ID: http://127.0.0.1:8000/task-delete/id/
