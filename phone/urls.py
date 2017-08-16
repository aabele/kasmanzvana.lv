"""
Application url config
"""
from django.conf.urls import url

from phone import views

urlpatterns = [

    url(r'^numurs/(?P<number>[0-9]{1,8})/$', views.PhoneDetailView.as_view(), name='details'),
    url(r'^komentars/(?P<pk>\w+)/$', views.CommentProfileView.as_view(), name='comment_profile'),
    url(r'^komentet/$', views.CommentCreateView.as_view(), name='add_comment'),
    url(r'^kategorija/(?P<category>[0-9-]{1,7})/$', views.CategoryView.as_view(), name='category'),
    url(r'^kategorija/$', views.CategoryView.as_view(), name='category_index'),

]
