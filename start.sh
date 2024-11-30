#!/bin/bash
# chmod +x start.sh
# ./start.sh

# cd spaproject
# python manage.py collectstatic --noinput
# python manage.py makemigrations
# python manage.py migrate
# gunicorn spaproject.wsgi:application --bind 0.0.0.0:$PORT --log-level debug
# echo "Using PORT: $PORT"

sudo systemctl start redis
cd spaproject
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn spaproject.wsgi:application --log-level debug
