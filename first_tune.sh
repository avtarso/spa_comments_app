# !/bin/bash

# script for run in VSCode
# chmod +x first_tune.sh && ./first_tune.sh

python3 -m venv spa && source spa/bin/activate
pip install -r requirements.txt
cd spaproject
python manage.py makemigrations && python manage.py migrate
kill -9 $(lsof -t -i:8000)
python manage.py runserver
