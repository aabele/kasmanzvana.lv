"""
Application views
"""

from django.contrib import messages
from django.http import Http404
from django.views.generic import DetailView, CreateView, TemplateView, ListView

from phone import forms
from blog import models


class FrontPage(ListView):
    """
    Blog front page
    """
    model = models.Post


class PostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs.get(self.pk_url_kwarg))
