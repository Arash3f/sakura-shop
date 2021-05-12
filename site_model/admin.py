from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Private_Site_Information)
class Private_Site_Information(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'name' , 'title']
    