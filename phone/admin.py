
from django.contrib import admin
from phone import models

admin.site.register([
    models.Phone,
])


class CommentAdmin(admin.ModelAdmin):
    exclude = ('author', 'phone')


admin.site.register(models.Comment, CommentAdmin)
