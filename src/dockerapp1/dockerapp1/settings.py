import os, sys


############################################################
# Directory Definitions
############################################################

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(SETTINGS_DIR)
PROJECT_DIR = os.path.dirname(SRC_DIR)
CLIENTS_DIR = os.path.join(SRC_DIR, 'clients/')
LOGS_DIR = os.environ.get('LOGS_DIR', os.path.join(PROJECT_DIR, 'logs'))
PUBLIC_DIR = os.environ.get('PUBLIC_DIR', os.path.join(PROJECT_DIR, 'public'))
STATIC_DIR = os.environ.get('STATIC_DIR', os.path.join(PUBLIC_DIR, 'static'))
COMPRESS_DIR = os.environ.get('COMPRESS_DIR', os.path.join(PUBLIC_DIR, 'compress'))
MEDIA_DIR = os.environ.get('MEDIA_DIR', os.path.join(PUBLIC_DIR, 'media'))

FOLDER_CREATION_CHECK = [LOGS_DIR, PUBLIC_DIR, STATIC_DIR, MEDIA_DIR]


############################################################
# Application Definition
############################################################

VERSION = "0.0.1a"
SECRET_KEY = '3ic91ry%*^0h2kzar0n16xl4tm^q6k6p7-51*g(-a+=v8!#*-c'
DEBUG = bool(os.environ.get('DEBUG', 1))
TEST_MODE = sys.argv[1:2] == ['test']
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dockerapp1.urls'

WSGI_APPLICATION = 'dockerapp1.wsgi.application'


############################################################
# Database Definition
############################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'django_db'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE_HOST', 'db'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
        'ATOMIC_REQUESTS': bool(os.environ.get('DATABASE_ATOMIC_REQUESTS', 1))
    }
}


############################################################
# Authentication Definition
############################################################

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


############################################################
# Internationalization
############################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kuala_Lumpur'
USE_I18N = True
USE_L10N = True
USE_TZ = True


############################################################
# Templates and Static Files
############################################################

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
        },
    },
]

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/public/static/'
