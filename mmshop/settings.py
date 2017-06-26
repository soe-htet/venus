"""
Django settings for mmshop project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-#^s_g7g@$5$+&=yk*=wgx=r^!5do$&0%l2is$bp^0m&iv#&4s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

DEFAULT_FROM_EMAIL = "venusleague@gmail.com"

# try:
#     from .email_settings import host, user, password
#     EMAIL_HOST = 'smtp.gmail.comm' #"smtp.gmail.com" #"smtp.sendgrid.net"
#     EMAIL_HOST_USER = 'sendgrid-pointy-93123' #"codingforentrepreneurs@gmail.com"
#     EMAIL_HOST_PASSWORD = 'leagueofVenus' #"password"
#     EMAIL_PORT = 587
#     EMAIL_USE_TLS = True
# except:
#     pass
SEND_GRID_API = "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"



try:
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST= 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
except:
    pass


#SITE_URL = "http://127.0.0.1:8000"
SITE_URL = "https://immense-brushlands-15195.herokuapp.com"



ALLOWED_HOSTS = ['*']


#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'Carts',
    'orders',
    'stripe',
    'accounts',
    'marketing'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'marketing.middleware.DisplayMarketing',
)

ROOT_URLCONF = 'mmshop.urls'

WSGI_APPLICATION = 'mmshop.wsgi.application'


# DATABASES = settings.DATABASES


# import dj_database_url
# DATABASES['default'] = dj_database_url.config()

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.request',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
    )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'static/static_root')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,  'static/static_files'),
)


MEDIA_ROOT = os.path.join(BASE_DIR,'static/media')
MEDIA_URL = '/media/'



TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

STRIPE_SECRET_KEY = 'sk_test_Yw3jbV8iZj9siOweortzcSl2'
STRIPE_PUBLISHABLE_KEY = 'pk_test_np2PXyxXxWPq8n5QmXVm0ZwU'
