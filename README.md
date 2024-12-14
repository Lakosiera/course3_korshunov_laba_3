# Лаба3 Первое приложение на Django. Cookies

## Задание

- [x] Создать новый проект на Django.
- [ ] Создать html-форму в соответствии со своим вариантом. 
- [ ] Определить стили страницы через внешнюю страницу стилей. 
- [ ] Добавить текстовый и графический контент на страницу под тематику вашего варианта. 
- [ ] Реализовать функционал для сохранения пользовательских настроек с использованием cookies, таких как темы, язык интерфейса или последние посещенные страницы.

### Варианты:

7. Приложение для изучения языков с сохранением прогресса.

## Настрока Django без Docker

### Настрока Питона

Сохраняем список всех установлинных в питон пакетов

```sh
pip freeze > requirements.txt
```

Устанавливаем в питон список пакетов

```sh
pip install -r requirements.txt
```

### Как создать новый серер

```sh
django-admin startproject server 
```

### Как создать модуль

```sh
python manage.py startapp module_name
```

### Кака запустить джанго

```sh
cd server

python manage.py runserver
```

### Запуск Докера композа

```sh
docker compose up
```

### Зайти в оболочку контейнера

```sh
docker exec -it container_name sh
# docker exec -it django-db sh
```

или

```sh
docker compose exec service_name sh
# docker compose exec db sh
```

### Джанго проверка

[http://127.0.0.1:8080/](http://127.0.0.1:8080/)

## Postgrs

```sh
su - postgres -c psql
```

Создание пользователя и таблицы

```sql
CREATE USER django WITH PASSWORD 'django';  
CREATE DATABASE laba3;
GRANT ALL ON DATABASE laba3 TO django;
ALTER DATABASE laba3 OWNER TO django;
```

### Django

Миграция для админки

```sh
python manage.py migrate
```

Создаение суперпользователя

```sh
python manage.py createsuperuser
```
