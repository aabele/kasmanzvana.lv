"""
Celery app
"""
import raven
from celery import Celery
from django.conf import settings
from raven.contrib.celery import register_signal, register_logger_signal


class MyCelery(Celery):

    def on_configure(self):
        client = raven.Client(settings.RAVEN_CONFIG.get('dsn', ''))
        register_logger_signal(client)
        register_signal(client)
        super().on_configure()


app = MyCelery('app', broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
