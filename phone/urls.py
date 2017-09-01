"""
Application url config
"""
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from phone import views
from phone import viewsets

router_v1 = DefaultRouter()
router_v1.register(r'phone', viewsets.PhoneViewSet, 'phone')
router_v1.register(r'comment', viewsets.CommentViewSet, 'comment')

urlpatterns = [

    url(r'^numurs/(?P<number>[0-9]{1,8})/$', views.PhoneDetailView.as_view(), name='details'),
    url(r'^komentars/(?P<pk>\w+)/$', views.CommentProfileView.as_view(), name='comment_profile'),
    url(r'^komentet/$', views.CommentCreateView.as_view(), name='add_comment'),
    url(r'^kategorija/(?P<category>[0-9-]{1,7})/$', views.CategoryView.as_view(), name='category'),
    url(r'^kategorija/$', views.CategoryView.as_view(), name='category_index'),

]
