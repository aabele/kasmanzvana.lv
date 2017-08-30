"""
Application url config
"""
from django.conf.urls import url

from blog import views

urlpatterns = [

    url(r'^publikacija/(?P<slug>[a-z0-9\-]+)/$', views.PostView.as_view(), name='post'),
    # url(r'^kategorija/(?P<category>\w\_+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^$', views.FrontPage.as_view(), name='front'),

]
