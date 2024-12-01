#!/bin/bash

cd spaproject
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn spaproject.wsgi:application --log-level debug
