from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Private_Site_Information)
class Private_Site_Information(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'name' ]

@admin.register(models.About_Us)
class About_Us(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'title' , 'sub_title']

@admin.register(models.Contact_Us)
class Contact_Us(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'get_title_display' , 'name' , 'email' , 'phone']
    