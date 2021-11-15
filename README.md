# Django REST framework. Проект «Web-сервис для работы с TODO-заметками».

## Стек технологий

### Python 3.10
> `django` (v. 3.2.9) - Django framework
> 
> `djangorestframework` (v. 3.12.4) - Django REST framework
> 
> `markdown` (v. 3.3.4) - Язык разметки
> 
> `django-filter` (v. 21.1) - Библиотека для фильтрации запросов + визуализация в браузерном API
> 
> `django-cors-headers` (v. 3.10.0) - Настройка политики CORS. Работа с заголовками для доступа React к Django
> 
> `djangorestframework-camel-case` (v. 1.2.0) - Визуализация в верблюжий стиль для отображения JSON и браузерного API. И наоборот в змеиный стиль для питона

### JavaScript, Node.js
> `npx` - Режим одноразового запуска, пакет для запуска пакетов без установки в систему.
> 
> `create-react-app` Создание/установка проекта на `React` (v. 17.0.2) + `Babel`, `Webpack` и другие полезные зависимости для комфортной работы
> 
> `axios` (v. 0.24.0)  - Библиотека для браузеров и Node.js, HTTP-клиент
> 
> `react-router-dom` (v. 6.0.2) - Маршрутизация `<BrowserRouter>` и `<HashRouter>`.
> 
> `dateformat` (v. 5.0.2) - Преобразование даты

## Frontend. SPA. Точка входа http://localhost:3000/.

> `/` - Single Page Application - вход в приложение, подгрузка данных из backend-а, дальше перемещение по всем компонентам с помощью меню, без перезагрузки страницы
>
> `/users` - подгрузка компонента Пользователи, данные всех пользователей в табличном виде с возможностью перехода на конкретного пользователя, отображение дней рождения переформатировано
>
> `/users/:id` - все данные пользователя по `:id` из БД на backend-е
> 
> `/projects `- подгрузка компонента Проекты, данные всех проектов в табличном виде, возможность перехода к конкретному проекту или к пользователям работающими с конкретным проектом
> 
> `/projects/:id` данные Проекта по `:id` из БД на backend-е. + Отображаются имена/ссылки всех пользователей, кто работают с проектом. + Отображаются все заметки оставленные к проекту с данными чья это заметка и переформатированными датами создания/обновления. Данные собираются и фильтруются из разных источников, собранных в SPA, но без повторных запросов к БД!
> 
> `/todos` - подгрузка компонента Заметки, данные всех заметок в табличном виде, возможность перехода к проекту, к которому оставлены конкретные заметки

## Backend. Точка входа http://localhost:3333/. Web-ресурсы

> `/administration/` - админка

## Backend. Точка входа http://localhost:3333/. Методы API проекта, Endpoint-ы 

> `/api/auth/login/` - Авторизация пользователя

> `/api/auth/logout/` - Деавторизация пользователя

> `/api/token/` - Получение Токена через POST запрос для авторизации

### Пользователи
> `/api/users/` - GET, HEAD, OPTIONS - вывод данных всех пользователей. Создание запрещено!

> `/api/users/superusers/` - GET, HEAD, OPTIONS - вывод данных всех суперпользователей

> `/api/users/<int:pk>/` - GET, PUT, PATCH, HEAD, OPTIONS - в зависимости от метода запроса - вывод данных, редактирование и т.д. пользователя по `id` в БД, вместо `<int:pk>` подставить id Пользователя. Удаление запрещено!

> `api/users/?login=<логин>` - GET, HEAD, OPTIONS - вывод данных пользователей отфильтрованных по части логина (фильтрация в БД username__contains), вместо `<логин>` подставляем часть (можно даже 1-2 буквы) уникального логина пользователя. Настроено вручную стандартными методами

> `api/users/?first_name=<имя>&middle_name=<фамилия>&last_name=<отчество>` - GET, HEAD, OPTIONS - вывод данных пользователей, отфильтрованных по части имени, части фамилии, части отчества вместо `<имя>` подставляем часть имени, вместо `<фамилия>` часть фамилии, вместо `<отчество>` часть отчества пользователей. Некоторые данные можно опускать или комбинировать, в том числе с другими методами фильтрации, как например по части логина выше. Настроено с помощью кастомного `django-filter`

> `/api/users/<int:pk>/login/` - GET, HEAD, OPTIONS - вывод уникального логина пользователя по id в БД, вместо `<int:pk>` подставить id Пользователя

> `/api/users/<int:pk>/fio/` - GET, HEAD, OPTIONS - вывод фамилии, имени, отчества пользователя по id в БД, вместо `<int:pk>` подставить id Пользователя

> `/api/users/?limit=<лимит>&offset=<смещение>` - GET, HEAD, OPTIONS - в поле `<лимит>` указываем количество пользователей, чьи данные придут в ответе на запрос, в поле `<смещение>` - смещение относительно первого пользователя. В ответ кроме пользователей приходят ссылки на смещение относительно страницы и другие данные

### Проекты
> `/api/projects/` - GET, POST, HEAD, OPTIONS - список проектов, создание проекта

> `/api/projects/?name=<имя>` - GET, POST, HEAD, OPTIONS - вывод данных проектов, отфильтрованных по части имени, вместо `<имя>` подставляем часть имени проектов. Настроено с помощью кастомного `django-filter`

> `/api/projects/?limit=<лимит>&offset=<смещение>` - GET, POST, HEAD, OPTIONS - в поле `<лимит>` указываем количество проектов, данные которых придут в ответе на запрос, в поле `<смещение>` - смещение относительно первого проекта. В ответ кроме проектов приходят ссылки на смещение относительно страницы и другие данные

> `/api/projects/<int:pk>/` - GET, PUT, PATCH, DELETE, HEAD, OPTIONS - вывод, редактирование, удаление проекта, вместо `<int:pk>` подставить id Проекта

### Заметки
> `/api/todos/` - GET, POST, HEAD, OPTIONS - список заметок, создание заметки

> `/api/todos/?created_after=<начало>&created_before=<конец>&project=<id>&project__name=<имя>` - GET, POST, HEAD, OPTIONS - вывод данных заметок. Фильтрация заметок по дате, в поле `<начало>` - указываем от какой даты считаем, в поле `<конец>` - до какой даты. Фильтрация заметок по id, поле `<id>`, в браузере можно сразу выбрать проект. Фильтрация заметок по имени проекта, поле `<имя>`. Достаточно использовать 1 из фильтров или использовать комбинации. Настроено с помощью кастомного `django-filter`, некоторые поля дефолтные

> `/api/todos/?limit=<лимит>&offset=<смещение>` - GET, POST, HEAD, OPTIONS - в поле `<лимит>` указываем количество заметок, данные которых придут в ответе на запрос, в поле `<смещение>` - смещение относительно первой заметки. В ответ кроме заметок приходят ссылки на смещение относительно страницы и другие данные

> `/api/todos/<int:pk>/` - GET, PUT, PATCH, DELETE, HEAD, OPTIONS - вывод, редактирование, удаление заметки (Метод переопределён! Вместо фактического удаления активность меняется на 0 (False)), вместо `<int:pk>` подставить id Заметки

## Консольные команды в рамках проекта для запуска моих скриптов:

> `python manage.py add_all_data` - скрипт единой точки создания дефолтных данных в БД

> `python manage.py add_roles` - скрипт заполнения таблиц БД дефолтными группами прав, ролями

> `python manage.py add_users` - скрипт заполнения таблиц БД дефолтным админом и пользователями. Так же админ добавляется в группу разрешений Администратор, остальные дефолтные пользователи в группу Разработчик. В группу Владелец проекта будут попадать те, кто будут создавать свои проекты

> `python manage.py add_projects` - скрипт заполнения таблиц БД дефолтным проектами, те в свою очередь связываются с дефолтными пользователями, работающими с каждым проектом

> `python manage.py add_todos` - скрипт заполнения таблиц БД дефолтным заметками, привязанными к конкретным проектам 

# Полезные команды:

> `curl <address>` - FTP-клиент / HTTP-клиент - В поле `<address>` указываем необходимый ресурс и получаем данные как например JSON по API, так и целого сайта и т.д.

### Консольные команды Backend-а (Python, Django, DRF)

> `python venv env` - создание виртуального окружения

> `pip install django djangorestframework markdown django-filter` - установка зависимостей, полезных библиотек

> `pip freeze > requirements.txt` - помещаем все зависимости проекта в файл `requirements.txt`

> `pip install -r requirements.txt` - устанавливаем все зависимости проекта из файла `requirements.txt`

> `pip list` - удобное отображение всех установленных приложений, библиотек

> `django-admin startproject config` - создание проекта 'config'

> `python manage.py startapp users` - создание приложения 'Пользователи'

> `python manage.py makemigrations` - создание миграций, необходимо после создания/обновления моделей

> `python manage.py migrate` - выполнение миграций

> `python manage.py sqlmigrate <app_name>` - выполняется после создания миграций. Позволяет вывести на экран SQL-запросы, которые будут генерироваться для Django командой применения миграций к базе данных (то есть к таблицам, соответствующим указанному приложению)

> `python manage.py collectstatic` - сборка стандартных и подготовленных статических файлов

> `python manage.py createsuperuser` - создание супер-пользователя

> `python manage.py runserver 0.0.0.0:3333` - запуск проекта на порту 3333 (доступ http://localhost:3333)

#### Работа с дампами БД. В проекте не использую, так как не поддерживается кириллица. Использую export БД в json файл от IDE Pycharm, дампы в каталоге `dumps_pycharm_export`

> `python manage.py dumpdata --indent 2 --exclude auth.permission --exclude contenttypes > ./json/dumps_django_dumpdata/all_data.json` - Дамп всей БД, за исключением некоторых таблиц `--exclude auth.permission` и `--exclude contenttypes`, мешающих восстановлению БД из дампа. `--indent 2` - количество отступов в json файле
> 
> `python manage.py dumpdata users > ./json/dumps_django_dumpdata/users_data.json` - Дамп БД приложения `users`
> 
> `python manage.py dumpdata todo.project > ./json/dumps_django_dumpdata/todo_project_data.json` - Дамп БД конкретной таблицы модели `project` приложения `todo`
> 
> `python manage.py dumpdata todo.todo > ./json/dumps_django_dumpdata/todo_todo_data.json` - Дамп БД конкретной таблицы модели `todo` приложения `todo`
> 
> `python manage.py loaddata ./json/dumps_django_dumpdata/all_data.json` - импорт данных из дампа

### Консольные команды Frontend-а (JavaScript, NodeJS, npx, React)

> `npx create-react-app frontend` - создание/установка проекта на React + Babel, webpack и другие полезные зависимости для комфортной работы, `npx` - режим одноразового запуска, пакет для запуска пакетов без установки в систему.

> `npm run start` - запуск фронтенд проекта, выполнять в корне фронта (в данном случае в каталоге frontend)

> `npx react-codemod rename-unsafe-lifecycles` - переименовать все устаревшие жизненные циклы на их новые имена


### Консольные команды для Docker-compose: 

> `docker-compose build` - Создать образ

> `docker-compose -f docker-compose.prod.yml build` - Создать образ (запуск из файла `docker-compose.prod.yml`). Префикс `-f` `имя_файла`, после `docker-compose` позволяет запускаться из файла с нестандартным именем для выполнения любых возможных команд

> `docker-compose up` - Запустить контейнер

> `docker-compose up -d --build` - Создать образ и запустить контейнер в фоне

> `docker image ls -a && docker container ls -a && docker volume ls` - Посмотреть все образы/контейнеры/тома

> `docker container prune && docker image prune && docker volume prune` - Удалить неиспользуемые контейнеры/образы/тома

> `docker-compose down -v` - Удалить тома вместе с контейнерами 

> `docker-compose -f docker-compose.prod.yml down -v` - Удалить тома вместе с контейнерами (запуск из файла docker-compose.prod.yml)

> `docker-compose logs -f` - Проверка наличия ошибок в журналах, просмотр логов

> `docker exec -it <CONTAINER ID> bash` - Зайти в работающий контейнер 

> `docker volume inspect django-on-docker_postgres_data` - Проверить, что том (volume) был создан

> `docker rmi <CONTAINER ID>`, `docker rmi -f <CONTAINER ID>` - Удалить образ 

> `docker image rm <name_or_id>`, `docker container rm <name_or_id>`, `docker volume rm <name_or_id>` - Удалить образы, контейнеры, тома по названию или id

> `docker stop <CONTAINER ID>` - Приостановить контейнер 

> `docker start <CONTAINER ID>` - Запустить ранее остановленный контейнер 

> `docker restart <CONTAINER ID>` - Перегрузить контейнер 

> `docker ps`, `docker ps -a` - Посмотреть работающие и все контейнеры 

> `docker images` - Посмотреть список всех образов


#### Работа с django, manage.py (сервис web):

> `docker-compose exec web python manage.py flush --no-input ` - Очистка таблиц

> `docker-compose exec web python manage.py makemigrations --no-input` - Создание миграций

> `docker-compose exec web python manage.py migrate` - Запуск миграций

> `docker-compose exec web python manage.py collectstatic --no-input --clear` - Сборка стандартных и подготовленных статических файлов 


#### Вход в postgres (сервис db): 
> `docker-compose exec db psql --username=admin --dbname=db_name` - вход в сервис `db`, а внутри него вход в postgres, имя `admin`, бд `db_name`
##### Внутри postgres: 
> ` # \l ` - Показать базы данных

> ` # \c db_name ` - Подключение к базе данных `db_name`

> ` # \dt ` - Список зависимостей

> ` # \q ` - Выход из postgres
