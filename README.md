[EN](https://github.com/wezbicka/django-orm-watching-storage/blob/master/README.EN.md)
# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который подключён к удалённой базе данных, фиксирует время визитов в хранилище всех сотрудников банка.

## Как установить
Создайте и активируйте виртуальное окружение

```
python -m venv venv
source ./venv/Scripts/activate  #для Windows
source ./venv/bin/activate      #для Linux и macOS
```

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Программа берет настройки из нестандартных переменных окружения. Перед запуском программы создаём фаил .env, туда положите:
```
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_HOST=host
DB_PORT=port
DB_NAME=name
DB_USER=user
DB_PASSWORD=password
SECRET_KEY=secret_key
DEBUG=False
```
Как запустить проект
Запустите localhost командой из терминала.
```
python manage.py runserver
```
В браузере перейдите по адресу http://127.0.0.1:8000

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).