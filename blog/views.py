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
