"""
Application model signals
"""

from django.core.mail import mail_admins
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from app.urls import ADMIN_URL

from website import models


@receiver(post_save, sender=models.Message)
def notify_admin_about_comment(sender, instance, created, **kwargs):
    """
    Send email notification about new message
    """
    if created:
        mail_admins(
            'New message from kasmanzvana.lv visitor',
            ('https://kasmanzvana.lv/{0}/phone/comment/{1}/change/\n\n'
             'Comment: {2}').format(ADMIN_URL, instance.pk, instance.body)
        )
