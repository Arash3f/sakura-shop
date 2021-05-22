from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.product_group)
class product_group(admin.ModelAdmin):
    field = "__all__"
    list_display=['name']
    # ordering = ['-top_group']
    
@admin.register(models.product_sub_group)
class product_sub_group(admin.ModelAdmin):
    field = "__all__"
    list_display=['name']
    # ordering = ['-top_group']
@admin.register(models.product)
class product(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'name'  , 'group']
    prepopulated_fields = {'slug': ('name',), }

@admin.register(models.product_cost)
class product_cost(admin.ModelAdmin):
    field = "__all__"
    
@admin.register(models.packs)
class producpackst_group(admin.ModelAdmin):
    field = "__all__"
@admin.register(models.comment)
class comment(admin.ModelAdmin):
    field = "__all__"