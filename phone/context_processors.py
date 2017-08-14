from django.conf import settings


def country_prefix(request):
    key = 'COUNTRY_PREFIX'
    return {
        key: getattr(settings, key, '')
    }


def public_url(request):
    key = 'PUBLIC_URL'
    return {
        key: getattr(settings, key, '')
    }
