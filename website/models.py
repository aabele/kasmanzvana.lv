"""
Application models
"""

from django.db import models
from django.template.defaultfilters import slugify


class Message(models.Model):
    """
    Message details
    """

    email = models.EmailField(max_length=200)
    body = models.TextField()

    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Object representation as string
        :return: string
        """
        return '{0}'.format(self.email)


class Visitor(models.Model):
    """
    Anonymous visitor profile
    """
    email = models.EmailField()

    def __str__(self):
        """
        Object representation as string
        :return: string
        """
        return self.email


class Service(models.Model):
    """
    Service description page
    """
    slug_length = 50
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=slug_length, unique=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Object representation as string
        :return: string
        """
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)[:self.slug_length]
        super().save(*args, **kwargs)
