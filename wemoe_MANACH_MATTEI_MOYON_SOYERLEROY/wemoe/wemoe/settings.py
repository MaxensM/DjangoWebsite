"""
Django settings for wemoe project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from django.db.models import manager 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NEOMODEL_NEO4J_BOLT_URL = os.environ.get('NEO4J_BOLT_URL', 'bolt://neo4j:wemoe@riwan-mattei.ovh:7687')
INTERNAL_IPS = ('127.0.0.1',)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xofn+cwwtvu608gch*_1#4xd_c%nrek9z5zes@$k(z955hj-ov'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_neomodel',
    'main.apps.MainConfig',
    #'django_extensions',
    'debug_toolbar',

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wemoe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.contrib.staticfiles.templatetags.staticfiles',
            ],
        },
    },
]

WSGI_APPLICATION = 'wemoe.wsgi.application'
STATIC_URL = '/static/'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASE_ROUTERS = ['routers.DatabaseAppsRouter']
#DATABASE_APPS_MAPPING = {'contenusPage': 'MONGO'}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "test",
        'USER': 'wemoe',
        'PASSWORD': 'wemoe',
        'HOST': 'riwan-mattei.ovh',
        'PORT': '3306',
        'OPTIONS':{
            'sql_mode': "STRICT_ALL_TABLES",
        }
    },

    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': "wemoe",
        'USERNAME': 'wemoe',
        'PASSWORD': 'wemoe',
        'HOST': 'riwan-mattei.ovh',
        'PORT': 37017,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'