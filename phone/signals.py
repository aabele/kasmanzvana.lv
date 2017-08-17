"""
Application model signals
"""

from django.core.mail import mail_admins
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from app.urls import ADMIN_URL

from phone import models


@receiver(post_save, sender=models.Comment)
def notify_admin_about_comment(sender, instance, created, **kwargs):
    """
    Send email notification about new comment
    """
    if created:
        mail_admins(
            'New comment posted in kasmanzvana.lv',
            'https://kasmanzvana.lv/{0}/auth/user/{1}/change/\n\n{2}\n\n{3}'.format(
                ADMIN_URL, instance.pk, instance.phone, instance.body)
        )
