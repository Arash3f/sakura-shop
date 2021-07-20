from django.contrib import admin
from accounting import models

@admin.register(models.Accounts_Form)
class Accounts_Form(admin.ModelAdmin):
    field = "__all__"

@admin.register(models.Accounting_Score)
class Accounting_Score(admin.ModelAdmin):
    field = "__all__"

@admin.register(models.Accounting_Score_Rows)
class Accounting_Score_Rows(admin.ModelAdmin):
    field = "__all__"