"""
Application url configuration
"""
from django.conf.urls import url
from django.views.generic import TemplateView

from website import views


urlpatterns = [

    url(r'^informacijas-dzesana/$', TemplateView.as_view(template_name='website/agreement/takedown.html'), name='takedown'),
    url(r'^atruna/$', TemplateView.as_view(template_name='website/agreement/agreement.html'), name='agreement'),
    url(r'^$', views.FrontPageView.as_view(), name='front'),


]
