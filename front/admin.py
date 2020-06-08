from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Solution)
admin.site.register(models.Student)
admin.site.register(models.Task)
admin.site.register(models.ClassName)
admin.site.register(models.Teacher)
