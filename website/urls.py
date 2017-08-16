"""
Application url configuration
"""
from django.conf.urls import url
from django.views.generic import TemplateView

from website import views


urlpatterns = [

    url(r'^parakstities/$', views.SubscribeToNewsView.as_view(), name='email_subscribe'),
    url(r'^informacijas-dzesana/$', TemplateView.as_view(template_name='website/agreement/takedown.html'), name='takedown'),  # noqa
    url(r'^atruna/$', TemplateView.as_view(template_name='website/agreement/agreement.html'), name='agreement'),
    url(r'^kontakti/$', views.ContactView.as_view(), name='contacts'),
    url(r'^$', views.FrontPageView.as_view(), name='front'),

]
