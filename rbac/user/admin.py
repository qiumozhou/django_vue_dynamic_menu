from django.contrib import admin

# Register your models here.
from user import models

admin.site.register(models.User)
admin.site.register(models.Menu)
admin.site.register(models.Roles)