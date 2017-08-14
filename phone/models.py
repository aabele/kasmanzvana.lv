"""
Application models
"""
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


user_model = get_user_model()


class Phone(models.Model):
    """
    Phone model implementation
    """
    phone = models.CharField(max_length=8, unique=True)

    def __str__(self):
        """
        Object representation as string
        :return:
        """
        return self.phone

    def get_absolute_url(self):
        return reverse('phones:details', kwargs={'number': self.phone})


class Comment(models.Model):
    """
    Comment model implementation
    """
    phone = models.ForeignKey('phone.Phone')
    body = models.TextField()

    anonymous_session = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(user_model, blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Object representation as string
        :return:
        """
        return self.body
