"""
Application signals
"""
from django.contrib.auth.signals import user_logged_in as generic_user_logged_id
from allauth.account.signals import user_logged_in
from django.dispatch.dispatcher import receiver
from phone import models


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