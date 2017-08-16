"""
Application url config
"""
from django.conf.urls import url

from user import views

urlpatterns = [

    url(r'^lietotajs/(?P<pk>\w+)/$', views.UserDetailView.as_view(), name='details'),
]
