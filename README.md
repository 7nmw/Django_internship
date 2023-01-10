# REST API для Федерации Спортивного Туризма России (ФСТР)
Разработка REST API, обслуживающее мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.
***
## Для начала работы необходимо установить все библиотеки
```
pip install requirements.txt
```
***

## Создана структура базы данных
Была использована база данных PostgreSQL.
***
## Логин, пароль и путь к базе данных получено из переменных окружения
* FSTR_DB_HOST: путь к базе данных;
* FSTR_DB_PORT: порт базы данных;
* FSTR_DB_LOGIN: логин, с которым происходит подключение к БД;
* FSTR_DB_PASS: пароль, с которым происходит подключение к БД.
## Реализован Rest API включающий в себя методы POST, GET и PATCH
Реализован метод POST submitData, позволяющий вносить нужную информацию:
* координаты объекта и его высоту;
* название объекта;
* несколько фотографий;
* информацию о пользователе, который передал данные о перевале:
* имя пользователя (ФИО строкой);
* почта;
* телефон.

Реализован метод GET и PATCH submitDataGetPatch позволяющий выводить информацию и вносить извемения в нее
***
## Дополнительно
Была создана документация с помощью Swagger

