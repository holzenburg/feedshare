"""
Django settings for feedshare project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '---replace-this-with-a-custom-secret-key---'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts
ALLOWED_HOSTS = [
    'feedshare.net', 'www.feedshare.net',
    'localhost', '127.0.0.1'
]

# Application
WSGI_APPLICATION = 'feedshare.wsgi.application'

# Urls
ROOT_URLCONF = 'feedshare.urls'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, '../cache'),
    }
}


# Templates

TEMPLATE_DIRS = [
    os.path.abspath(os.path.join(BASE_DIR, 'feedshare', 'templates'))
]
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

SITE_ID = 1
# Applications

INSTALLED_APPS = (
    # grappelli
    'grappelli',

    # django contrib
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third party
    'south',
    'django_extensions',
    'bootstrap3',
    'bootstrap_pagination',
    'taggit',
    'bootstrapform',

    # project apps
    'feedshare.feedlists',

    # Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Third kinds
    'allauth.socialaccount.providers.github',
)


# Middlware

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Media files (Uploads)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../htdocs/media/'))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../htdocs/static/'))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


# Grappelli
# http://grappelliproject.com

GRAPPELLI_ADMIN_TITLE = 'feedshare.net Admin'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Local settings
# - Set a SECRET_KEY!

LOCAL_APPS = tuple()

try:
    from local_settings import *
    INSTALLED_APPS += LOCAL_APPS
except ImportError, e:
    pass
