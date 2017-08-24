"""
Application model admin configuration.
"""
from django.contrib import admin
from phone import models

admin.site.register([
    models.RemovedPhone
])


class PhoneAdmin(admin.ModelAdmin):
    search_fields = ('phone', )

admin.site.register(models.Phone, PhoneAdmin)


class CommentAdmin(admin.ModelAdmin):
    exclude = ('author', 'phone')


admin.site.register(models.Comment, CommentAdmin)
