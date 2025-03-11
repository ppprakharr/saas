"""
Django settings for cfeadmin project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=config('EMAIL_HOST',default='smtp.gmail.com',cast=str)
EMAIL_PORT=config('EMAIL_PORT',default='587',cast=str)
EMAIL_USE_TLS=config('EMAIL_USE_TLS',default=True,cast=bool)
EMAIL_USE_SSL=config('EMAIL_USE_SSL',default=False,cast=bool)
EMAIL_HOST_USER=config('EMAIL_HOST_USER',default=None,cast=str)
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD',default=None,cast=str)
ADMIN_NAME=config('ADMIN_NAME',default='admin user')
ADMIN_EMAIL=config('ADMIN_EMAIL',default=None)

MANAGERS=[]
ADMINS=[]

if all([ADMIN_NAME,ADMIN_EMAIL]):
    ADMINS+=[
        (ADMIN_NAME,ADMIN_EMAIL)
    ]
MANAGERS=ADMINS


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'commando',
    'userauth',
    'profiles',

    #oauth installation ->allauth
    "allauth_ui",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    "widget_tweaks",
    "slippers",

]
SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
     "allauth.account.middleware.AccountMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cfeadmin.urls'

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        # 'APP': {
        #     'client_id': config("GITHUB_CLIENT_ID"),
        #     'secret': config("GITHUB_CLIENT_SECRET"),
        # },
        'VERIFIED_EMAIL': True,
        'SCOPE': ['user:email'],
        'AUTH_PARAMS': {
            'redirect_uri': 'http://localhost:8000/accounts/github/login/callback/'
        }
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'cfeadmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASE_URL = config("DATABASE_URL",cast=str)
CONN_MAX_AGE=config("CONN_MAX_AGE",default=30,cast=int)
if DATABASE_URL is not None:
    import dj_database_url
    DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=CONN_MAX_AGE,
        conn_health_checks=True
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
ACCOUNT_LOGIN_METHODS={"email"}
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION="mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX="[TEST]"
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_AUTO_SIGNUP = True 
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = "optional"


AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
   
]



# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_BASE_DIR  = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_VENDOR_DIR= os.path.join(STATICFILES_BASE_DIR,'vendor')


#source for python manage.py collectstatic
STATICFILES_DIRS=[
    STATICFILES_BASE_DIR
]

#output for python manage.py collectstatic
#local cdn
STATIC_ROOT=BASE_DIR/'local-cdn'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
