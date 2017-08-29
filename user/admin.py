from django.contrib import admin

from user import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    """
    User model admin configuration
    """
    list_display = ('pk', 'username', 'first_name', 'last_name', 'email', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email')
