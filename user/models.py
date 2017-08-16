"""
Application models
"""
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models
from phone import mixins


class User(mixins.HashidMixin, AbstractUser):
    """
    Application user implementation
    """
    is_banned = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('users:details', kwargs={'pk': self.get_hashid_pk()})
