"""
Application url config
"""
from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^saglabat-epastu/$', views.EmailFillView.as_view(), name='account_fill_email'),
    url(r'^lietotajs/(?P<pk>\w+)/$', views.UserDetailView.as_view(), name='details'),
]
