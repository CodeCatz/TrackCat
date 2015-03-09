"""
Django settings for TrackCat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from os.path import join
TEMPLATE_DIRS = (
	join(BASE_DIR, 'web/templates'),
)

from os.path import abspath, basename, dirname, join, normpath

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4ww32!z(uf2p+)e7*)ufr%-3^1_+@5m$hz_=w-q3g!ho97o-pc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'social.apps.django_app.default',

	# defined apps
	'web',
	'api',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

########## AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
	'social.backends.github.GithubOAuth2',
	'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.request',
	'social.apps.django_app.context_processors.backends',
	'social.apps.django_app.context_processors.login_redirect',
	'django.contrib.messages.context_processors.messages',
)

AUTH_PROFILE_MODULE = 'api.UserProfile'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'
SOCIAL_AUTH_ENABLED_BACKENDS = ('github')
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''
########## END AUTHENTICATION CONFIGURATION

ROOT_URLCONF = 'TrackCat.urls'

WSGI_APPLICATION = 'TrackCat.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db', 'develop-db.sqlite3'),
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Ljubljana'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, "static"),
)

try:
	from .settings_local import *
except ImportError as e:
	pass

########## MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = normpath(join(BASE_DIR, 'media'))
# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'
MEDIA_UPLOAD_FOLDER = 'profile_picture'
########## END MEDIA CONFIGURATION

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = False

