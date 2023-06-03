#! /bin/bash

/usr/local/bin/python3 manage.py makemigrations
/usr/local/bin/python3 manage.py migrate
/usr/local/bin/python3 manage.py runserver 0.0.0.0:8000
