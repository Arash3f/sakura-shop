from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.detail)
class detail(admin.ModelAdmin):
    field = "__all__"