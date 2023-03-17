# Team Project 32

## Table of contents

- [About This Project](#about-this-project)
- [Getting started](#getting-started)
- [Using your own PostgresSQL server](#using-your-own-postgressql-server)

## About this project

![Screen grab of Oaxaca site](/Oaxaca/restaurant/static/images/dish/Mom's%20Spaghetti.png "Screen grab of Oaxaca site")

Welcome to Oaxaca, a restaurant serving fine, savory meme dishes.

This project is built using Python with the Django framework and uses PostgreSQL as the database.

## Getting started

Prerequisites: Python 3 installed, and an PostgresSQL server if you plan to use your own

1. Start a virtual environment in an empty folder with `python -m venv env`
    - On Linux, you may need to use `python3` if `python` is not specified.
2. Enter the virtual environment with 
    - Windows Command Prompt: `env\Scripts\activate.bat`
    - Windows Powershell: `.\env\Scripts\Activate.ps1`
        - You may need to allow unsigned script execution with `Set-ExecutionPolicy -ExecutionPolicy Unrestricted`
    - Linux: `source env/bin/activate`
3. After entering the venv, install the required python packages:
    - django
        - `pip install django`
    - django-environ
        - `pip install django-environ`
    - django-crispy-forms
        - `pip install django-crispy-forms`
    - crispy_bootstrap4
        - `pip install crispy_bootstrap4`
    - psycopg2
        - Windows: `pip install psycopg2`
        - Linux: `pip install psycopg2-binary`
4. Change to the `Oaxaca` directory with `cd Oaxaca`
5. Create a `.env` file in `Oaxaca/Oaxaca` with the following PostgresSQL server config:
    ```
    DJANGO_SETTINGS_MODULE='restaurant'
    DB_NAME=default_db
    DB_USER=root
    DB_PASSWORD=asdjkl
    DB_HOST=ps32.swinghin.com
    DB_PORT=5432
    ```
    - You may specify your own PostgresSQL server, see [Using your own PostgresSQL server](#using-your-own-postgressql-server).
6. To start the web server, run `python manage.py runserver`
    - The server will run at port `8000` by default.

## Using your own PostgresSQL server

1. Create an empty PostgresSQL server in your environment.
2. Edit `Oaxaca/Oaxaca/.env` with your PostgresSQL server config.
    - Fields to be changed: 
        - `DB_NAME`
        - `DB_USER`
        - `DB_PASSWORD`
        - `DB_HOST`
        - `DB_PORT`
3. Change to the `Oaxaca` directory with `cd Oaxaca`
4. Migrate the database models to your own DB with `python manage.py migrate`
5. After a successful DB migration, start a Python shell using `python manage.py shell`
6. Import from `batch.py` using `from restaurant.batch import *`
7. Drop all tables (if necessary) using `drop_all()`
8. Add all required data using `add_all()`
9. Exit the Python shell using `exit()`