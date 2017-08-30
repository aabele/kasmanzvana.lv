from django.contrib import admin
from blog import models


admin.site.register([
    models.Category,
    models.Post,
    models.Comment
])
