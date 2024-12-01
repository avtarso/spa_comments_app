# spa_comments
SPA app for comments

Как установить и запустить на локальном компьютере (Linyx)
(На компьютере уже должен быть установлен python, Git, Redis)

Установка и первый запуск
0. Откройте новое окно терминала
1. Создайте новый отдельный каталог (например, projects_from_github)
mkdir projects_from_github
2. Перейдите в новый отдельный каталог
cd projects_from_github 
3. Клонируйте данный репозиторий
git clone https://github.com/avtarso/spa_comments_app
4. Перейдите в каталог spa_comments_app
cd spa_comments_app
5. Создайте виртуальную среду
python3 -m venv spa
6. Активируйте виртуальную среду
source spa/bin/activate
7. установите необходимые для работы библиотеки python
pip install -r requirements.txt
8. Перейдите в папку с Django проектом
cd spaproject
9. Создайте и примените настройки базы данных
python manage.py makemigrations && python manage.py migrate
10. Завершите процессы, которые (вдруг) занимают порт 8000
kill -9 $(lsof -t -i:8000)
11. запустите сервер
python manage.py runserver

Теперь приложение из этого репозитория доступно по адресу http://127.0.0.1:8000/

Последующие запуски
0. Откройте новое окно терминала
1. Перейдите в папку projects_from_github/spa_comments_app
cd projects_from_github/spa_comments_app
1.1. Измените атрибуты файла s.sh для обеспечения возможности его запуска
(этот пункт необходимо сделать только один раз)
chmod +x s.sh
2. Запустите файл s.sh
./s.sh

Теперь приложение из этого репозитория доступно по адресу http://127.0.0.1:8000/, а процедура всех последущих запусков сводится к выполнению одной команды:
cd projects_from_github/spa_comments_app && ./s.sh


