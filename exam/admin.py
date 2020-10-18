from django.contrib import admin
from . import models


admin.site.register(models.Question)
admin.site.register(models.FinalResult)
admin.site.register(models.Exam)
admin.site.register(models.Category)
