"""
Application models
"""
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from phone import mixins

user_model = get_user_model()


class Phone(mixins.HashidMixin, models.Model):
    """
    Phone model implementation
    """
    phone = models.CharField(max_length=8, unique=True)

    cat_1 = models.CharField(max_length=2, blank=True, null=True, editable=False)
    cat_2 = models.CharField(max_length=4, blank=True, null=True, editable=False)
    cat_3 = models.CharField(max_length=6, blank=True, null=True, editable=False)

    def __str__(self):
        """
        Object representation as string
        :return:
        """
        return self.phone

    def make_categories(self):
        """
        This data will help browsing Subcategories
        """
        if len(self.phone) >= 2:
            self.cat_1 = self.phone[0:2]

        if len(self.phone) >= 4:
            self.cat_2 = self.phone[0:4]

        if len(self.phone) >= 6:
            self.cat_3 = self.phone[0:6]

    def visible_comments(self):
        return self.comment_set.exclude(author__isnull=True).order_by('-id')

    @classmethod
    def get_namespace(cls, prefix=None):

        if not prefix:
            namespace = [str(i).zfill(2) for i in range(0, 100)]
            items = cls.objects.only('cat_1').distinct().values_list('cat_1', flat=True)
            return list(set(namespace) & set(items))

        if len(prefix) == 2:
            namespace = ['{0}{1}'.format(prefix, str(i).zfill(2)) for i in range(0, 100)]
            items = cls.objects.only('cat_2').distinct().values_list('cat_2', flat=True)
            return list(set(namespace) & set(items))

        if len(prefix) == 4:
            namespace = ['{0}{1}'.format(prefix, str(i).zfill(2)) for i in range(0, 100)]
            items = cls.objects.only('cat_3').distinct().values_list('cat_3', flat=True)
            return list(set(namespace) & set(items))

        if len(prefix) == 6:
            namespace = ['{0}{1}'.format(prefix, str(i).zfill(2)) for i in range(0, 100)]
            items = cls.objects.only('phone').distinct().values_list('phone', flat=True)
            return list(set(namespace) & set(items))

    def get_absolute_url(self):
        """
        Get the visible url of phone
        :return: string
        """
        return reverse('phones:details', kwargs={'number': self.phone})

    def save(self, *args, **kwargs):
        self.make_categories()
        super().save(*args, **kwargs)


class Comment(mixins.HashidMixin, models.Model):
    """
    Comment model implementation
    """
    phone = models.ForeignKey('phone.Phone')
    body = models.TextField()

    # Allow to display old comments from file based engine
    legacy = models.BooleanField(default=False, editable=False)

    anonymous_session = models.CharField(max_length=200, blank=True, null=True, editable=False)
    author = models.ForeignKey(user_model, blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        """
        Object representation as string
        :return: string
        """
        return self.body

    def get_absolute_url(self):
        """
        Generate comment url - ID is hidden by hashid
        :return: string
        """
        return reverse('phones:comment_profile', kwargs={'pk': self.get_hashid_pk()})

    def is_admin(self):
        """
        Check if the comment has been left by the admin user
        :return: Boolean
        """
        if not self.author:
            return False

        return self.author.is_staff is True

    def save(self, *args, **kwargs):
        if not (self.pk and self.insert_date):
            self.insert_date = now()
        super().save(*args, **kwargs)
