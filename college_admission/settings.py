"""
Django settings for college_admission project.

This file contains all the configuration settings for the College Admission System.
It includes database settings, installed apps, middleware, templates, and other Django configurations.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8#v$#g$#g$#g$#g$#g$#g$#g$#g$#g$#g$#g$#g$#g$#g$#g$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# List of allowed host domains
ALLOWED_HOSTS = []

# Application definition
# List of all Django applications used in this project
INSTALLED_APPS = [
    'django.contrib.admin',  # Django's built-in admin interface
    'django.contrib.auth',   # Authentication system
    'django.contrib.contenttypes',  # Content type system
    'django.contrib.sessions',  # Session framework
    'django.contrib.messages',  # Message framework
    'django.contrib.staticfiles',  # Static file handling
    
    # Custom applications
    'accounts',      # User authentication and profiles
    'colleges',      # College information management
    'admissions',    # Admission process management
    'cutoffs',       # Cutoff scores management
    'notifications', # Notification system
]

# Middleware configuration
# These are the hooks for modifying request/response globally
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security features
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session handling
    'django.middleware.common.CommonMiddleware',  # Common operations
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Message handling
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
]

# Root URL configuration
ROOT_URLCONF = 'college_admission.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Custom templates directory
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

# WSGI application configuration
WSGI_APPLICATION = 'college_admission.wsgi.application'

# Database configuration
# Using SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Media files (User uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login URL configuration
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home' 