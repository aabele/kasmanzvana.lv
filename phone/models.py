"""
Application models
"""
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from phone import mixins

user_model = get_user_model()


class RemovedPhone(models.Model):
    """
    Phones with owners that do not want their numbers to be published.
    """
    phone = models.CharField(max_length=8, unique=True)

    def __str__(self):
        """
        Object representation as string
        :return: string
        """
        return self.phone


class RatingBase(models.Model):
    """
    Rating base implementation
    """

    PLUS = 1
    MINUS = -1
    PLUS_TITLE = 'Celt'
    MINUS_TITLE = 'Necelt'
    CHOICES = (
        (PLUS, PLUS_TITLE),
        (MINUS, MINUS_TITLE),
    )
    value = models.SmallIntegerField(choices=CHOICES, blank=True, null=True)
    user = models.ForeignKey(user_model)

    class Meta(object):
        """
        Model meta options
        """
        abstract = True


class PhoneRating(RatingBase):
    """
    User voting for the number
    """
    PLUS_TITLE = 'Celt'
    MINUS_TITLE = 'Necelt'
    phone = models.ForeignKey('phone.Phone')

    class Meta(object):
        """
        Model meta options
        """
        unique_together = ('phone', 'user')

    def save(self, *args, **kwargs):
        """
        Regenerate related phone stats after each save
        """
        super().save(*args, **kwargs)
        self.phone.generate_phone_rating()
        self.phone.save()


class Phone(mixins.HashidMixin, models.Model):
    """
    Phone model implementation
    """
    rating_model = PhoneRating

    phone = models.CharField(max_length=8, unique=True)

    cat_1 = models.CharField(max_length=2, blank=True, null=True, editable=False)
    cat_2 = models.CharField(max_length=4, blank=True, null=True, editable=False)
    cat_3 = models.CharField(max_length=6, blank=True, null=True, editable=False)

    rating_value = models.IntegerField(default=0, editable=False)
    positive_votes = models.IntegerField(default=0, editable=False)
    negative_votes = models.IntegerField(default=0, editable=False)

    def generate_phone_rating(self):
        """
        Calculate the phone rating values
        """
        positive_votes = self.phonerating_set.filter(value=self.rating_model.PLUS).count()
        negative_votes = self.phonerating_set.filter(value=self.rating_model.MINUS).count()
        self.rating_value = positive_votes - negative_votes
        self.positive_votes = positive_votes
        self.negative_votes = negative_votes

    def get_positive_votes(self):
        return self.rating_model.objects.filter(phone=self, value=self.rating_model.PLUS).count()

    def get_negative_votes(self):
        return self.rating_model.objects.filter(phone=self, value=self.rating_model.MINUS).count()

    def vote_plus(self, user):
        """
        Vote plus or minus
        :param user: user instance
        """
        obj, _ = self.rating_model.objects.get_or_create(phone=self, user=user)
        obj.value = self.rating_model.PLUS
        obj.save()

    def vote_minus(self, user):
        """
        Vote plus or minus
        :param user: user instance
        """
        obj, _ = self.rating_model.objects.get_or_create(phone=self, user=user)
        obj.value = self.rating_model.MINUS
        obj.save()

    def total_votes(self):
        return self.rating_model.objects.filter(phone=self).count()

    def vote_rating(self):
        return sum(list(self.rating_model.objects.filter(phone=self).values_list('value', flat=True)))

    def __str__(self):
        """
        Object representation as string
        :return: string
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
        return self.comment_set.order_by('-id')

    def get_last_authenticated_comment(self):
        obj = (Comment.objects
               .filter(phone=self, legacy=False)
               .exclude(author_id__isnull=True)
               .order_by('-id')
               .first())

        return obj

    @classmethod
    def get_namespace(cls, prefix=None):

        def get_items(key):
            """
            Return list of namespace items mixed with existing db records
            :param key: object field name
            :return: list containing unique items
            """
            if not prefix:
                namespace = [str(i).zfill(2) for i in range(0, 100)]
            else:
                namespace = ['{0}{1}'.format(prefix, str(i).zfill(2)) for i in range(0, 100)]
            items = cls.objects.only(key).distinct().values_list(key, flat=True)
            return list(set(namespace) & set(items))

        if not prefix:
            return get_items('cat_1')

        mapping = {
            2: 'cat_2',
            4: 'cat_3',
            6: 'phone'
        }

        if len(prefix) in mapping.keys():
            return get_items(mapping.get(len(prefix)))

    def get_absolute_url(self):
        """
        Get the visible url of phone
        :return: string
        """
        return reverse('phones:details', kwargs={'number': self.phone})

    def save(self, *args, **kwargs):
        self.make_categories()
        super().save(*args, **kwargs)


class CommentRating(RatingBase):
    """
    User voting for the number
    """
    PLUS_TITLE = 'Labs'
    MINUS_TITLE = 'Nelabs'
    comment = models.ForeignKey('phone.Comment')

    class Meta(object):
        """
        Model meta options
        """
        unique_together = ('comment', 'user')


class Comment(mixins.HashidMixin, models.Model):
    """
    Comment model implementation
    """
    rating_model = CommentRating

    phone = models.ForeignKey('phone.Phone')
    body = models.TextField()

    # Allow to display old comments from file based engine
    legacy = models.BooleanField(default=False, editable=False)

    anonymous_session = models.CharField(max_length=200, blank=True, null=True, editable=False)

    author_raw_pk = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(user_model, blank=True, null=True)
    insert_date = models.DateTimeField(blank=True, null=True, editable=False)

    def handle_author_raw_id(self):
        if self.author_raw_pk:
            try:
                self.author = user_model.objects.get(pk=self.author_raw_pk)
            except user_model.DoesNotExist:
                pass
            self.author_raw_pk = None

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

    def get_positive_votes(self):
        return self.rating_model.objects.filter(comment=self, value=self.rating_model.PLUS).count()

    def get_negative_votes(self):
        return self.rating_model.objects.filter(comment=self, value=self.rating_model.MINUS).count()

    def vote_plus(self, user):
        """
        Vote plus or minus
        :param user: user instance
        """
        obj, _ = self.rating_model.objects.get_or_create(comment=self, user=user)
        obj.value = self.rating_model.PLUS
        obj.save()

    def vote_minus(self, user):
        """
        Vote plus or minus
        :param user: user instance
        """
        obj, _ = self.rating_model.objects.get_or_create(comment=self, user=user)
        obj.value = self.rating_model.MINUS
        obj.save()

    def save(self, *args, **kwargs):
        if not (self.pk and self.insert_date):
            self.insert_date = now()
        self.handle_author_raw_id()
        super().save(*args, **kwargs)
