from app.settings_remote import *  # noqa

SECRET_KEY = get_env_setting('PRODUCTION_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kasmanzvana_production',
        'USER': 'kasmanzvana_production_user',
        'PASSWORD': get_env_setting('PRODUCTION_PASSWORD'),
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

INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
RAVEN_CONFIG = {
    'dsn': 'https://efe407373a044897a69eff5e66523b04:22a7c13b77fa433ea549541ebe388550@sentry.io/183774',
}

EMAIL_USE_SSL = True
EMAIL_HOST = 'mail.sigmanet.lv'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'rekins@skolutiesibas.lv'
EMAIL_HOST_PASSWORD = 'rekins2016!'

EMAIL_SUBJECT_PREFIX = '[kasmanzvana.lv] '
SERVER_EMAIL = 'rekins@skolutiesibas.lv'

ADMINS = (
    ('Aivis Abele', 'aabele@gmail.com'),
)

ACCOUNT_EMAIL_VERIFICATION = 'none'
