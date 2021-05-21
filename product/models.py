from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
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
    picture = models.ImageField("عکس" ,upload_to = 'product/', blank=True , null = True)
    inventory = models.PositiveIntegerField(verbose_name='موجودی',)
    discount = models.PositiveIntegerField(verbose_name='تخفیف' , blank=True , null = True ,validators=[MaxValueValidator(99)])
    available = models.BooleanField(verbose_name="وضعیت" , default=True  )
    # relations :
    group = models.ForeignKey('product_group' , verbose_name="گروه" , on_delete=models.CASCADE )

    class Meta:
        verbose_name = ("کالا")
        verbose_name_plural = ("کالا ها")

    def __str__(self):
        return self.name

class Price_to_weight(models.Model):

    MY_CHOICES = [("1",'گرم'),]
    cost = models.IntegerField(verbose_name='قیمت' , blank=True , null = True )
    weight_type = models.CharField(verbose_name="نوع وزن" ,choices=MY_CHOICES , max_length = 100, blank=True , null = True )
    size = models.IntegerField(verbose_name='اندازه' )
    # relations :
    product = models.ForeignKey('product' , verbose_name="کالا" , on_delete=models.CASCADE , null=True , blank = True)

    class Meta:
        verbose_name = ("معیار")
        verbose_name_plural = ("معیار ها")

    def p_cost(self):
        return "{:,}".format(int(self.cost))
    p_cost.short_description = "قیمت"

class comment(models.Model):
    MY_CHOICES = [("1",'پیشنهاد'),
                    ("2",'انتقاد یا شکایت'),
                    ("3","مدیریت"),
                    ("4",'حسابداری'),
                    ("5",'سایر موضوعات')]

    title = models.CharField(verbose_name="عنوان" ,choices=MY_CHOICES , max_length = 100 , blank=True , null = True )
    name = models.CharField(verbose_name="نام" ,max_length = 100 , blank=True , null = True )
    email = models.EmailField(verbose_name="ایمیل" ,max_length = 100 , blank=True , null = True)
    phone = models.CharField(verbose_name="شماره تماس" , max_length=11 , blank=True , null = True)
    body = models.TextField(verbose_name="متن" , blank=True , null = True)

    class Meta:
        verbose_name = ("ارتباط با ما")
        verbose_name_plural = ("ارتباط با ما")

    def __str__(self):
        return self.title

    