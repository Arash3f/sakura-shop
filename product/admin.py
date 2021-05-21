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

@admin.register(models.Price_to_weight)
class Price_to_weight(admin.ModelAdmin):
    field = "__all__"
    list_display=[ 'product'  , 'size' , 'weight_type'  , 'p_cost']
    list_filter = ['product',]
    