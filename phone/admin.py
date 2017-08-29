"""
Application model admin configuration.
"""
from django.contrib import admin
from phone import models

admin.site.register([
    models.RemovedPhone
])


@admin.register(models.Phone)
class PhoneAdmin(admin.ModelAdmin):
    search_fields = ('phone', )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for comment model
    """
    list_display = ('pk', 'phone', 'body', 'author', 'legacy')
    search_fields = ('phone__phone',)
    exclude = ('author', 'phone')
