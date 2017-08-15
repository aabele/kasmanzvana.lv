"""
Application models
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from phone import mixins


class User(mixins.HashidMixin, AbstractUser):
    """
    Application user implementation
    """
    is_banned = models.BooleanField(default=False)
