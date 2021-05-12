from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# site detail ...
class product_group(models.Model):
    name = models.CharField("متن" ,max_length = 100 , blank=True , null = True ,help_text = "متن نمایشی")    
    class Meta:
        verbose_name = ("دسته بندی")
        verbose_name_plural = ("دسته بندی ها")
    
    def __str__(self):
        return self.name

class product_sub_group(models.Model):
    name = models.CharField("متن" ,max_length = 100 , blank=True , null = True ,help_text = "متن نمایشی")
    group = models.ForeignKey('product_group' ,related_name='sub_group', verbose_name="سر گروه", on_delete=models.CASCADE , null=True , blank = True ,help_text = "درصورت داشتن سر گروه ، وارد شود ")
    
    class Meta:
        verbose_name = ("زیر گروه")
        verbose_name_plural = ("زیر گروه ها")
    
    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField("نام کالا" ,max_length = 100 , blank=True , null = True)
    description_one = models.CharField("توضیحات" ,max_length = 100 , blank=True , null = True ,help_text = "کمتر از ۱۰۰ کلمه")
    description_two = models.TextField("توضیحات کامل", blank=True , null = True )
    cost = models.IntegerField("قیمت" , blank=False, null=False )
    picture = models.ImageField("عکس" ,upload_to = 'product/', blank=True , null = True)
    group = models.ForeignKey('product_group' , verbose_name="گروه" , on_delete=models.CASCADE , null=True , blank = True)

    class Meta:
        verbose_name = ("کالا")
        verbose_name_plural = ("کالا ها")

    def p_cost(self):
        return "{:,}".format(int(self.cost))
    p_cost.short_description = "قیمت"

    def __str__(self):
        return self.name


    