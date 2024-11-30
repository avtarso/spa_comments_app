# chmod +x first_tune.sh
# ./first_tune.sh

python3 -m venv spa
source spa/bin/activate

# pip install django djangorestframework
# pip install django-redis pillow

pip install -r requirements.txt


#django-admin startproject spaproject

cd spaproject
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

