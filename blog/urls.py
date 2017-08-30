"""
Application url config
"""
from django.conf.urls import url

from blog import views

urlpatterns = [

    # url(r'^publikacija/(?P<category>\w+)/$', views.PostView.as_view(), name='post'),
    # url(r'^kategorija/(?P<category>\w+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^$', views.FrontPage.as_view(), name='front'),

]
