[RU](https://github.com/wezbicka/django-orm-watching-storage/blob/master/README.md)
# Bank security console

This is an internal repository for employees of the bank "Sianie". If you got into this repository by accident, then you will not be able to run it, because you do not have access to the database, but you can freely use the layout code or see how database queries are implemented.

The security console is a website that is connected to a remote database, records the time of visits to the vault of all bank employees.

## How to install

Install and activate virtual environment for project isolation.

```
python -m venv venv<br>
source ./venv/Scripts/activate  #для Windows
source ./venv/bin/activate      #для Linux и macOS
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```
 
The program takes settings from non-standard environment variables. Before starting the program, create a file .env, put it there:

```
DB_ENGINE=django.db.backends.<desired_engine>
DB_HOST=<hostname or IP>
DB_PORT=<port number>
DB_NAME=<database name>
DB_USER=<database user name>
DB_PASSWORD=<database user password>
SECRET_KEY=secret_key
DEBUG=<debugging mode True or False>
```


How to launch a project
Run localhost with a command from the terminal.

```
python manage.py runserver
```
In the browser, go to http://127.0.0.1:8000

## Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org).