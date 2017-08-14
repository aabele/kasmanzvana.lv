"""
Application url config
"""
from django.conf.urls import url
from phone import views

FRONT_PAGE_NAME = 'phone.page.front'
AGREEMENT_PAGE_NAME = 'phone.page.agreement'
TAKEDOWN_PAGE_NAME = 'phone.page.takedown'
CONTACTS_PAGE_NAME = 'phone.page.contacts'
NOT_FOUND_PAGE_NAME = 'phone.page.404'
CATEGORY_INDEX_PAGE_NAME = 'phone.category.all'
CATEGORY_PAGE_NAME = 'phone.category'
NUMBER_PAGE_NAME = 'phone.number'

urlpatterns = [

    url(r'^numurs/(?P<number>[0-9]{1,8})/$', views.PhoneDetailView.as_view(), name='details'),
    url(r'^komentet/$', views.CommentCreateView.as_view(), name='add_comment'),
    # url(r'^kategorija/(?P<category>[0-9-]{1,7})/$', views.CategoryView.as_view(), name='category'),
    # url(r'^kategorija/$', views.CategoryView.as_view(), name=CATEGORY_INDEX_PAGE_NAME),

]
