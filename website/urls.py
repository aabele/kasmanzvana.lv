"""
Application url configuration
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView


urlpatterns = [

    url(r'^informacijas-dzesana/$', TemplateView.as_view(template_name='website/agreement/takedown.html'), name='takedown'),
    url(r'^atruna/$', TemplateView.as_view(template_name='website/agreement/agreement.html'), name='agreement'),
    url(r'^$', TemplateView.as_view(template_name='website/front.html'), name='front'),


]
