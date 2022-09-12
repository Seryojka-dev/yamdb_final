# yamdb_final
![yamdb workflow](https://github.com/Seryojka-dev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Адрес сайта

```
http://62.84.113.243/redoc/
```

Проект содержит три приложения: reviews, api, users. Приложение reviews содержит модели сервиса, приложение api предоставляет доступ к моделям через API, а в приложениии users реализована вся логика для управления ролями и выдачи доступов: пермишены, эндпоинты для регистрации и получения токена. Подробное описание запросов доступно по адресу /redoc/

## Шаблон наполнения env-файла

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

## Запуск контейнера и приложения в нем
Перейти в репозиторий для запуска докера
```
cd infra/
```
Запуск docker-compose
```
docker-compose up -d --build
```
Создайте суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
Войдите в админку и создайте одну-две записи объектов
### Следующим шагом создайте дамп (резервную копию) базы:
```
docker-compose exec web python manage.py dumpdata > fixtures.json
```
### Примеры запросов и ответов на эндпоинты:
##### 1.post Добавление новой категории эндпоинт api/v1/categories/:
Права доступа: Администратор.
```
{
    "name": "Игры",
    "slug": "Witcher"
}
```

Пример успешного ответа:
Status: 201 OK
```
{
    "name": "Игры",
    "slug": "Witcher"
}
```
##### 2.get Получение списка всех жанров эндпоинт api/v1/genre/:
Права доступа: Доступно без токена.
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```
Пример успешного ответа:
Status: 200 OK
```
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}
```
##### 3. post Добавление произведения эндпоинт api/v1/titles/:
Права доступа: Администратор.
```
{
    "name": "Хроники Нарнии",
    "year": 1955,
    "description": "Fantasy",
    "genre": [
        "string"
    ],
    "category": "Книги"
}
```
Пример успешного ответа:
```
{
    "id": 1,
    "name": "Хроники Нарнии",
    "year": 1955,
    "rating": 0,
    "description": "Fantasy",
    "genre": [
        {}
    ],
    "category": {
        "name": "Книги",
        "slug": "Fantasy"
    }
}
```
##### 4. post Добавление нового отзыва эндпоинт api/v1/titles/{title_id}/reviews/:
Права доступа: Аутентифицированные пользователи.
```
{
    "text": "круто",
    "score": 1
}
```
Пример успешного ответа:
Status: 201 OK
```
{
    "id": 1,
    "text": "круто",
    "author": "admin",
    "score": 1,
    "pub_date": "2022-09-03T08:29:22Z"
}
```
##### 5. get Получение списка всех пользователей эндпоинт api/v1/users/:
Права доступа: Администратор.
Пример успешного ответа:
Status: 200 OK
```
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "username": "sector",
            "email": "sector@mail.ru",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "user"
        },
        {
            "username": "sonya",
            "email": "sonya@ya.ru",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "user"
        },
        {
            "username": "jax",
            "email": "jax@ya.ru",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "user"
        },
        {
            "username": "admin",
            "email": "admin@ya.ru",
            "first_name": "",
            "last_name": "",
            "bio": "",
            "role": "user"
        }
    ]
}
```
##### 6. post Регистрация нового пользователя эндпоинт api/v1/auth/signup/:
Права доступа: Доступно без токена.
```
{
    "email": "cyrax@ya.ru",
    "username": "cyrax"
}
```
Пример успешного ответа:
Status: 200 OK
```
{
    "username": "cyrax",
    "email": "cyrax@ya.ru"
}
```
