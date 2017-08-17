"""
Application signals
"""
from allauth.account.signals import user_logged_in
from django.contrib.auth.signals import user_logged_in as generic_user_logged_id
from django.core.mail import mail_admins
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from app.urls import ADMIN_URL

from phone import models
from user.models import User


def _assign(session_id, user):
    """
    Assign objects to the user
    :param session_id: anonymous session ID
    :param user: authenticated user
    """
    for item in models.Comment.objects.filter(anonymous_session=session_id):
        item.author = user
        item.save()


@receiver(user_logged_in)
def assign_anonymous_comments(sender, user, request, **kwargs):
    """
    Associate all anonymously posted comments with specific session hash with the logged in user
    :param sender:
    :param user:
    :param request:
    :param kwargs:
    :return:
    """
    _assign(request.session.get('_ask'), user)


@receiver(generic_user_logged_id)
def assign_anonymous_comments_generic(sender, user, request, **kwargs):
    """
    Associate all anonymously posted comments with specific session hash with the logged in user
    :param sender:
    :param user:
    :param request:
    :param kwargs:
    :return:
    """
    _assign(request.session.get('_ask'), user)


@receiver(post_save, sender=User)
def notify_admin_about_new_user(sender, instance, created, **kwargs):
    """
    Send email notification about new user
    """
    if created:
        mail_admins(
            'New user registered in kasmanzvana.lv',
            'https://kasmanzvana.lv/{0}/auth/user/{1}/change/'.format(ADMIN_URL, instance.pk)
        )
