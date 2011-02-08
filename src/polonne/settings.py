# -*- coding: utf-8 -*-
import os.path
import sys

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
sys.path.append(os.path.join(PROJECT_PATH, 'apps'),)
sys.path.append(os.path.join(PROJECT_PATH, 'plugins'),)
sys.path.append(os.path.join(PROJECT_PATH, 'contrib'),)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Vasyl Dizhak', 'dijakroot@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',                     
        'USER': '',                      
        'PASSWORD': '',                 
        'HOST': '',                      
        'PORT': '',                     
    }
}

TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'ua'

LANGUAGES = (
    ('ua', ('Ukrainian')),
    ('ru', ('Russian')),
    ('en', ('English')),
)


SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '=g+@l)yw3)23#(o+u=e@$c+_t!_^sk2z=@a$cpbaiav)iy#-u-'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'polonne.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'localeurl',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'grappelli',
    'django.contrib.admin',
    'south',
    'transmeta',
    'sorl.thumbnail',
    'django_extensions',
    
    # apps
    'people',
    'articles',
    'news',
    'gallery'
)

# Grappelli configuration
GRAPPELLI_ADMIN_TITLE = 'Polonne.info'

try:
    from local_settings import *
except ImportError:
    print "No local settings found"