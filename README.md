# Tutorial - Wing Hin Shih

## How to Run

1. Start a virtual environment with `python -m venv env`.
2. Enter the venv with `source env/bin/activate`.
3. Install the required python packages:
    - django
        - `pip install django`
    - environ
        - `pip install environ`
    - psycopg2
        - `pip install psycopg2` (windows)
        - `pip install psycopg2-binary` (linux)
4. Change to the inner directory with `cd oaxaca_test/`.
5. Create a `.env` file in `oaxaca_test/oaxaca_test` with the following text:
    ```
    DB_NAME=default_db
    DB_USER=root
    DB_PASSWORD=asdjkl
    DB_HOST=ps32.swinghin.com
    DB_PORT=5432
    ```
6. To start the web server, run `python3 manage.py runserver`.