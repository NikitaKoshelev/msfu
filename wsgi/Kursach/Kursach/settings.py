"""
Django settings for Kursach project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

FILES_DIRS = os.path.normpath(os.path.join(BASE_DIR, '..', 'static'))

print FILES_DIRS

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'article', 'templates'),
    os.path.join(BASE_DIR, 'author', 'templates'),
    os.path.join(BASE_DIR, 'category', 'templates'),
    os.path.join(BASE_DIR, 'customuser', 'templates'),
    os.path.join(BASE_DIR, 'comment', 'templates'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e%li%r(!uz^85%s0x20h#clncnz$ncq7s1rc^nwacnc*wx^kb1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
    'ckeditor',
    'PIL',
    'pytz',
)

LOCAL_APPS = (
    'article',
    'author',
    'blog',
    'category',
    'comment',
    'customuser',
    'tag',
    'likes',
)


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Kursach.urls'

WSGI_APPLICATION = 'Kursach.wsgi.application'


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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/files/static/'

#STATIC_ROOT = os.path.join(FILES_DIRS, 'static')

#STATICFILES_DIRS = (
#    os.path.join(FILES_DIRS, 'statics'),
#    os.path.join(BASE_DIR, 'article', 'files', 'static'),
#    os.path.join(BASE_DIR, 'author', 'files', 'static'),
#    os.path.join(BASE_DIR, 'blog', 'files', 'static'),
#    os.path.join(BASE_DIR, 'category', 'files', 'static'),
#    os.path.join(BASE_DIR, 'comment', 'files', 'static'),
#    os.path.join(BASE_DIR, 'customuser', 'files', 'static'),
#    os.path.join(BASE_DIR, 'tag', 'files', 'static'),
#)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = os.path.join(FILES_DIRS, 'upload')
MEDIA_URL = '/files/media/'

CKEDITOR_UPLOAD_PATH = '/article_content/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    }
}

AUTHENTICATION_BACKENDS = (
    'customuser.auth_backend.CustomUserModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)

CUSTOM_USER_MODEL = 'customuser.CustomUser'
