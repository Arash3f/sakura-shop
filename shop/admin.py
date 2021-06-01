from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.OrderRow)
class OrderRow(admin.ModelAdmin):
    field = "__all__"

@admin.register(models.Order)
class Order(admin.ModelAdmin):
    field = "__all__"