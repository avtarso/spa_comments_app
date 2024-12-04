#!/bin/bash
# script for running on hosting

cd spaproject
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
daphne -b 0.0.0.0 -p $PORT spaproject.asgi:application
