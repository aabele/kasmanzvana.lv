from app.settings_remote import *  # noqa

SECRET_KEY = get_env_setting('DEVELOPMENT_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'huntercamera_web_development',
        'USER': 'huntercamera_web_development_user',
        'PASSWORD': get_env_setting('DEVELOPMENT_PASSWORD'),
        'HOST': 'localhost',
        'CONN_MAX_AGE': 600  # DB connection max age - 10 mins
    }
}

ALLOWED_HOSTS = [
    'kasmanzvana.lv',
    'kmz.deals.lv',
]


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

PRODUCTION = True
