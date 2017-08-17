"""
Application URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from user.views import LoginView
from phone.urls import router_v1 as phone_router_v1


ADMIN_URL = 'admin' if settings.DEBUG else 'admin-26414607'

urlpatterns = [
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
