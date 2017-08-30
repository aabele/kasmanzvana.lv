"""
Application models
"""
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.text import slugify


user_model = get_user_model()


class Category(models.Model):
    """
    Category details
    """
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        """
        Object representation as string
        :return: title field contents
        """
        return self.title


class Post(models.Model):
    """
    Blog post details
    """
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, blank=True, null=True, unique=True)
    body = models.TextField(blank=True, null=True)

    categories = models.ManyToManyField('blog.Category', blank=True)

    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        """
        Object representation as string
        :return: title field contents
        """
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug': self.slug})


class Comment(models.Model):
    """
    Comment model implementation
    """
    post = models.ForeignKey('blog.Post')
    body = models.TextField()

    # Allow to display old comments from file based engine
    legacy = models.BooleanField(default=False, editable=False)

    anonymous_session = models.CharField(max_length=200, blank=True, null=True, editable=False)
    author = models.ForeignKey(user_model, blank=True, null=True, related_name='blog_comments')
    insert_date = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        """
        Object representation as string
        :return: string
        """
        return self.body

    def save(self, *args, **kwargs):
        if not (self.pk and self.insert_date):
            self.insert_date = now()
        super().save(*args, **kwargs)
