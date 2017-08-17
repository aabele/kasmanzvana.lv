from django.apps import AppConfig


class PhoneConfig(AppConfig):
    name = 'phone'

    def ready(self):
        from phone import signals  # noqa
