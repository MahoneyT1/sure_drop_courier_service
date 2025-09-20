from .base import *
import dj_database_url
import os


DEBUG = False

ALLOWED_HOSTS = ["fastlink-backend.onrender.com", "www.yourdomain.com"]

# Secure DB (Postgres, MySQL, etc.)
DATABASES = {
    "default": dj_database_url.config(
        default= os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
        )
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CSRF_TRUSTED_ORIGINS = [
    "https://your-backend-service.onrender.com",
    "https://www.yourdomain.com",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Production email backend
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = os.getenv("SENDGRID_API_KEY")

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', 
]