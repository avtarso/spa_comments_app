#!/bin/bash
# chmod +x s.sh
# ./s.sh

kill -9 $(lsof -t -i:8000)
cd spaproject
python manage.py makemigrations
python manage.py migrate
python manage.py runserver