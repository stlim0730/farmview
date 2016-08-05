"""
Django settings for farmview project.
Generated by 'django-admin startproject' using Django 1.8.2.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^rbx%hfej#irat_i__!7n6(%e624nqpp0-4))yu+#5q3it$d^m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

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

SITE_ID = 1
ZINNIA_MARKUP_LANGUAGE = 'textile'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

SITE_ID = 1
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

ROOT_URLCONF = 'farmview.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'farmview.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'd4tj4urol6fqf1',
    'USER': 'hjgblmqzztzppf',
    'PASSWORD': 'tTtTEE2HPi7BNZXPhyji6Nxlkv',
    'HOST': 'ec2-54-225-134-223.compute-1.amazonaws.com',
    'PORT': '5432'
  }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

##
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LANGUAGES = [
  ('en', _('English')),
  ('es', _('Spanish')),
]

TIME_ZONE = 'US/Pacific'

USE_I18N = True #specifies whether Django's translation system should be enabled

USE_L10N = True

USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPOSITORY_ROOT = os.path.dirname(BASE_DIR)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(REPOSITORY_ROOT, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(REPOSITORY_ROOT, 'media/')

# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)