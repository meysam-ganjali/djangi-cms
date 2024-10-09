from os import path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-q9l*wak@u+vai$$l-hi+ote+2==#byxyu-24qlxxgd1663x2rq'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'colorfield',
    'django_jalali',
    'easy_select2',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.settings.apps.SettingsConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.banner.apps.BannerConfig',
    'apps.slider.apps.SliderConfig',
    'apps.blog.apps.BlogConfig',
    'apps.product.apps.ProductConfig',
    'apps.horizonta_lists.apps.HorizontaListsConfig',
    'apps.ticket.apps.TicketConfig'
]
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cmsProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'cmsProject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cms_db',
        'USER': 'root',
        'PASSWORD': '8730310248m',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

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

LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'

USE_I18N = True
USE_L10N = True
USE_TZ = True

CKEDITOR_UPLOAD_PATH = 'ckeditor/upload_files/'
CKEDITOR_STORAGE_BACKEND = 'django.core.files.storage.FileSystemStorage'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Link', 'Unlink', 'Image'],
        ]
    },
    'special': {
        'toolbar': 'Special',
        'height': 200,
        'toolbar': 'full',
        'toolbar_Special': [
            ['Bold', 'Italic', 'Underline', 'Link', 'Unlink', 'Image'],
            ['CodeSnippet'],

        ], 'extraPlugins': ','.join(['codesnippet', 'clipboard'])
    },
    'special_an': {
        'toolbar': 'Special',
        'height': 200,
        'toolbar_Special': [
            ['Bold'],
            ['CodeSnippet'],
        ], 'extraPlugins': ','.join(['codesnippet', 'clipboard'])
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS = (path.join(BASE_DIR, 'static/'),)

MEDIA_URL = 'media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'
LOGOUT_REDIRECT_URL = '/'

