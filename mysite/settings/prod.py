import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from decouple import config

from .base import ALLOWED_HOSTS

ALLOWED_HOSTS += []  # no use here managed directly though setting.ini file


# Database for prod
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}
