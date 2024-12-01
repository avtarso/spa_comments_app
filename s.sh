#!/bin/bash

kill -9 $(lsof -t -i:8000)
source spa/bin/activate
cd spaproject
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
