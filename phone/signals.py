"""
Application model signals
"""

from django.core.mail import mail_admins
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.template.loader import render_to_string

from app.urls import ADMIN_URL
from phone import models


@receiver(post_save, sender=models.Comment)
def notify_admin_about_comment(sender, instance, created, **kwargs):
    """
    Send email notification about new comment
    """
    if created:
        content = render_to_string('phone/email/new_comment.html', {
            'admin_prefix': ADMIN_URL,
            'pk': instance.pk,
            'phone': instance.phone,
            'comment': instance.body
        })
        mail_admins('New comment posted in kasmanzvana.lv', content)
