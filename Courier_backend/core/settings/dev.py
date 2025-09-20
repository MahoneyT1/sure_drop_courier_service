from .base import *


ALLOWED_HOSTS = [
    "localhost",
]

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

DEBUG=True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

