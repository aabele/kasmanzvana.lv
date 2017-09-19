"""
Application models
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from phone import mixins


class User(mixins.HashidMixin, AbstractUser):
    """
    Application user implementation
    """
    is_banned = models.BooleanField(default=False)
    legacy = models.BooleanField(default=False)

    following_list = models.ManyToManyField('phone.Phone', blank=True)

    def get_absolute_url(self):
        return reverse('users:details', kwargs={'pk': self.get_hashid_pk()})

    def last_15_comments(self):
        return self.comment_set.all().order_by('-id')[:15]
