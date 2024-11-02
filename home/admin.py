from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.AssessmentComponent)
admin.site.register(models.Assessment)
admin.site.register(models.Mark)
