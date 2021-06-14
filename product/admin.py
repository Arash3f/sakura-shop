from django.contrib import admin
from . import models

@admin.register(models.product_group)
class product_group(admin.ModelAdmin):
    field = "__all__"
    list_display=['name' , 'group']
    
@admin.register(models.product)
class product(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'name' ,"inventory","sell","group","available" ]
    prepopulated_fields = {'slug': ('name',), }

@admin.register(models.product_cost)
class product_cost(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'product' ,"pack","discount",'available' , 'cost']
    
@admin.register(models.packs)
class producpackst_group(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'title' ,"weight","parent"]

@admin.register(models.Properties)
class Properties(admin.ModelAdmin):
    field = "__all__"

@admin.register(models.ProductGallery)
class ProductGallery(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'product' ,"picture"]
    list_filter = ("product",)

# comment :
# @admin.register(models.comment)
# class comment(admin.ModelAdmin):
#     field = "__all__"