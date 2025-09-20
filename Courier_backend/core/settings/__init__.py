import os


env = os.getenv('DJANGO_eNV', 'dev')

if env == 'production':
    from .production import *
else:
    from .dev import *
