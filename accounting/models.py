from django.db import models

class Accounts_Form(models.Model):
    PERSONS = 1
    MATERIALS = 2
    PRODUCT = 3
    choice = ( 
            (  PERSONS  , "اشخاص" ),
			(  MATERIALS   , "مواد اولیه"  ),
			( PRODUCT   , "محصول"  )
			)
    name = models.CharField('نام حساب',max_length=50)
    type = models.IntegerField('نوع حساب',choices=choice)

class Accounting_Score(models.Model):
    date = models.DateTimeField(null=True)

class Accounting_Score_Rows(models.Model):
    accounting_score = models.ForeignKey('Accounting_Score' , related_name="accounting_score_rows" , on_delete=models.CASCADE)
    accounts_form =models.ForeignKey('Accounts_Form', related_name="accounting_score_rows", on_delete=models.CASCADE)
    description = models.TextField('شرح')
    debit = models.IntegerField('بدهکار')
    credit =models.IntegerField('بستانکار')