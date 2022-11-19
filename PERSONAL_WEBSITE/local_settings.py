"""
Local settings for PERSONAL_WEBSITE project.

Must be at the same directory as the settings.py file.

All variables are required unless stated otherwise using 'optional' comment
"""
# PYTHON IMPORTS
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATICFILES_DIR = os.path.join(BASE_DIR, "staticfiles")
STATIC_DIR = os.path.join(BASE_DIR, "static")
MEDIA_DIR = os.path.join(BASE_DIR, "media")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+#4o+jz=8x9dzsb7iemb(^sz+zl_4wt*83qcqr+vy1i7e#c(@)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Add domain name, i.e. example.com
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'dkkundu.tech'
    # add project domain here
]

# CORS HEADERS
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    # add project website here
]

# needed for debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

ENABLE_HTTPS = False

DB_CONFIG = {
    'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
    'HOST': os.getenv('DB_HOST', '127.0.0.1'),
    'PORT': os.getenv('DB_PORT', 5432),
    'NAME': os.getenv('DB_NAME', 'dk_db'),
    'USER': os.getenv('DB_USER', 'bksp_user'),
    'PASSWORD': os.getenv('DB_PASS', 'django')
}

# mysql defaults:
# 'ENGINE': 'django.db.backends.mysql'
# 'PORT': 3306


# Email backend (OPTIONAL)
# Console backend is only meant for development purposes
# Please comment it for production or use the django default:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Celery
CELERY_BROKER_URL = 'amqp://127.0.0.1:5672/'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
