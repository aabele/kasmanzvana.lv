"""
Settings file for Hosting server
"""
from app.settings import *  # noqa

DEBUG = False
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'

CELERY_ENABLED = True
