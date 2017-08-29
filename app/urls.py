"""
Application URL Configuration
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from app.sitemaps import sitemap_config
from phone.urls import router_v1 as phone_router_v1
from user.views import LoginView

ADMIN_URL = 'admin' if settings.DEBUG else 'admin-26414607'

urlpatterns = [
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^sitemap\.xml$', sitemap, sitemap_config),
    url(r'^{0}/'.format(ADMIN_URL), admin.site.urls),

    url(r'^api/v1/', include([
        url(r'^', include(phone_router_v1.urls)),
    ])),

    url(r'^login/$', LoginView.as_view(), name='account_login'),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^', include('phone.urls', namespace='phones')),
    url(r'^', include('website.urls', namespace='website')),
    url(r'^', include('user.urls', namespace='users')),
]
