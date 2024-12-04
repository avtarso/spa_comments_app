# SPA app for comments

## Как установить и запустить на локальном компьютере (Linyx)
(На компьютере уже должен быть установлен python, Git, Redis)

### Установка и первый запуск

Откройте новое окно терминала

Создайте новый отдельный каталог (например, projects_from_github)

    mkdir projects_from_github
  
Перейдите в новый отдельный каталог

    cd projects_from_github
    
Клонируйте данный репозиторий

    git clone https://github.com/avtarso/spa_comments_app
    
Перейдите в каталог spa_comments_app

    cd spa_comments_app
    
Создайте виртуальную среду

    python3 -m venv spa

Активируйте виртуальную среду

    source spa/bin/activate

установите необходимые для работы библиотеки python

    pip install -r requirements.txt

Перейдите в папку с Django проектом

    cd spaproject

Создайте и примените настройки базы данных

    python manage.py makemigrations && python manage.py migrate
    
Завершите процессы, которые (вдруг) занимают порт 8000

    kill -9 $(lsof -t -i:8000)

Запустите приложение

    daphne spaproject.asgi:application

#### Теперь приложение из этого репозитория доступно по адресу http://127.0.0.1:8000/

Все вышеперечисленные операции можно выполнить одной серией команд:

    mkdir projects_from_github && cd projects_from_github
    git clone https://github.com/avtarso/spa_comments_app
    cd spa_comments_app
    python3 -m venv spa && source spa/bin/activate
    pip install -r requirements.txt
    cd spaproject
    python manage.py makemigrations && python manage.py migrate
    kill -9 $(lsof -t -i:8000)
    daphne spaproject.asgi:application

### Последующие запуски

**(Этот пункт необходимо сделать только один раз)** Откройте новое окно терминала и измените атрибуты файла **s.sh** для обеспечения возможности его запуска **(этот пункт необходимо сделать только один раз)**

    cd projects_from_github/spa_comments_app && chmod +x s.sh && ./s.sh

#### Теперь приложение из этого репозитория доступно по адресу http://127.0.0.1:8000/, а процедура всех последущих запусков сводится к выполнению одной команды в новом окне терминала:

    cd projects_from_github/spa_comments_app && ./s.sh