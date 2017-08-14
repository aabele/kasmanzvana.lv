"""
Settings file for CI server
"""
from app.settings import *  # noqa

INSTALLED_APPS += [
    'django_nose',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

COVERAGE_APPS = [
    'phone',
]

NOSE_ARGS = (
    '--with-xunit',
    '--with-coverage',
    '--cover-erase',
    '--cover-html',
    '--cover-package={0}'.format(','.join(COVERAGE_APPS)),
    '--nologcapture',
    '--exclude=testing.py'
)

NOSE_WHERE = COVERAGE_APPS

RAVEN_CONFIG = {}

THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.dbm_kvstore.KVStore'
