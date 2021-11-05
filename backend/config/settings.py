"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Секретный ключ из настроек переменных окружения, иначе иначе из default
SECRET_KEY = os.environ.get('SECRET_KEY', default='yp@cq+i8hq^nta7i_)a-')

# SECURITY WARNING: don't run with debug turned on in production!
# Режим дебага из настроек переменных окружения, иначе из default
DEBUG = int(os.environ.get('DEBUG', default=1))

# Разрешённые хосты из настроек переменных окружения, иначе из default
ALLOWED_HOSTS = os.environ.get(
    'DJANGO_ALLOWED_HOSTS', default='localhost 127.0.0.1 [::1] web').split(' ')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    # Настройка политики CORS. Работа с заголовками для доступа React к Django
    'corsheaders',

    'users.apps.UsersConfig',
    'todo.apps.TodoConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Настройка политики CORS. Работа с заголовками для доступа React к Django
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# Настройка политики CORS - доступ с другого домена/порта
# Работа с заголовками для доступа React к Django, разрешенные адреса
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    # 'http://0.0.0.0:3000',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Добавление шаблонов из корневой директории templates
            os.path.join(BASE_DIR, 'templates')
        ],
        # Поиск шаблонов будет вестись по установленным приложениям (APP_DIRS):
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Подключение бд из настроек переменных окружения (PostgreSQL),
# иначе из default (sqlite3)
DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'SQL_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': os.environ.get(
            'SQL_DATABASE', default=os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', default='user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', default='password'),
        'HOST': os.environ.get('SQL_HOST', default='localhost'),
        'PORT': os.environ.get('SQL_PORT', default='5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Пользовательская модель авторизации:
AUTH_USER_MODEL = 'users.User'

# Глобальные настрой рендеринга
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        # Верблюжий стиль для отображения JSON и браузерного API
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
        # 'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': (
        # If you use MultiPartFormParser or FormParser,
        # we also have a camel case version
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        # Any other parsers
    ),
}

if DEBUG:
    # API в браузере
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
    # Стиль удобного администрирования в браузере
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(
        'rest_framework.renderers.AdminRenderer'
    )
    # Логирование
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        # Вывод запросов к бд в консоль
        'loggers': {
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['console'],
            },
        },
    }

# Затирание переменных локальными настройками (если есть):
try:
    from .local_settings import *
except ImportError or ModuleNotFoundError:
    pass
