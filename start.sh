#!/bin/bash
# chmod +x start.sh
# ./start.sh

cd spaproject
python manage.py makemigrations
python manage.py migrate
python manage.py runserver