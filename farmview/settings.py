"""
Django settings for farmview project.
Generated by 'django-admin startproject' using Django 1.8.2.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""


import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


#
# Debug settings
# SECURITY WARNING: don't run with debug turned on in production!
#
DEBUG = False


#
# Site meta
#
PROJECT_NAME = 'Project Farmview'
PROJECT_EMAIL = 'project.farmview@gmail.com'
ADMINS = [
    (PROJECT_NAME, PROJECT_EMAIL),
    # ('You may add your name', 'you may add your email'),
]
DEFAULT_FROM_EMAIL = '"{}" {}'.format(PROJECT_NAME, PROJECT_EMAIL)
EMAIL_HOST = os.environ.get('HOST', '127.0.0.1')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '25')
SITE_ID = 1


#
# Credentials
# SECURITY WARNING: keep the secret key used in production secret!
#
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')


#
# Connections
#
ALLOWED_HOSTS = ['*']
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


#
# Application dependencies
#
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'map',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',
)


#
# URL routing
#
ROOT_URLCONF = 'farmview.urls'

#
# File structure
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Use this tool to verify your file is accessible:
#   python manage.py findstatic --verbosity 2 your-static-file
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static')
)
# STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

#
# Templates
#
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'build')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'zinnia.context_processors.version',
            ],
        },
    },
]

#
# WSGI instance
#
WSGI_APPLICATION = 'farmview.wsgi.application'


#
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}


#
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
# Language codes: http://www.i18nguy.com/unicode/language-identifiers.html
#
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]
TIME_ZONE = 'US/Pacific'
USE_I18N = True  # specifies whether Django's translation system should be enabled
USE_L10N = True
USE_TZ = True


#
# Zinnia settings
#
ZINNIA_MARKUP_LANGUAGE = 'textile'
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# To override local settings from default settings,
#   local_settings.py must not exist on the production server or in shared repository.
#   This should be at the end of settings.py to override default settings.
try:
    from .local_settings import *
except ImportError:
    pass
