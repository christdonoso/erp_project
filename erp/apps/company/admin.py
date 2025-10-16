from django.contrib import admin
from apps.company import models
# Register your models here.

admin.site.register(models.Company)
admin.site.register(models.Collaborator)
