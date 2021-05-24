from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

# site detail ...
class product_group(models.Model):
    name = models.CharField("متن" ,max_length = 100 , blank=True , null = True ,help_text = "متن نمایشی")  
    group = models.ForeignKey('self' , verbose_name="سر گروه", on_delete=models.CASCADE , null=True , blank = True ,help_text = "درصورت داشتن سر گروه ، وارد شود ")
  
    class Meta:
        verbose_name = ("دسته بندی")
        verbose_name_plural = ("دسته بندی ها")
    
    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField("نام کالا" ,max_length = 100 , blank=True , null = True)
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=255)
    picture = models.ImageField("عکس" ,upload_to = 'product/', blank=True , null = True)
    inventory = models.PositiveIntegerField(verbose_name='موجودی',)
    available = models.BooleanField(verbose_name="(موجودی)وضعیت" , default=True  )
    sell = models.IntegerField(verbose_name='تعداد فروش' , blank=True , null = True )
    # relations :
    group = models.ForeignKey('product_group' , verbose_name="گروه" , on_delete=models.CASCADE )

    class Meta:
        unique_together = ['slug', 'name']
        verbose_name = ("کالا")
        verbose_name_plural = ("کالا ها")

    def __str__(self):
        return self.name

class packs(models.Model):
    title = models.CharField(verbose_name="عنوان" , max_length = 100 , blank=True , null = True )
    weight = models.IntegerField(verbose_name='اندازه' )

    class Meta:
        verbose_name = ("بسته ها")
        verbose_name_plural = ("بسته")

    def __str__(self):
        return self.title
    
class product_cost(models.Model):
    # relations :
    product = models.ForeignKey('product' ,related_name = "product_cost", verbose_name="کالا" , on_delete=models.CASCADE )
    pack = models.ForeignKey('packs' ,related_name = "product_cost", verbose_name="بسته" , on_delete=models.CASCADE )
    discount = models.PositiveIntegerField(verbose_name='تخفیف' ,default = 0 ,validators=[MaxValueValidator(99)])
    available = models.BooleanField(verbose_name="(بسته)وضعیت" , default=True  )
    cost = models.IntegerField(verbose_name='قیمت' , blank=True , null = True )
    
    class Meta:
        unique_together = [['product', 'pack']]
        verbose_name = ("قیمت")
        verbose_name_plural = ("قیمت ها")

    def p_cost(self):
        return "{:,}".format(int(self.cost))
    p_cost.short_description = "قیمت"

class comment(models.Model):
    product = models.ForeignKey("product", on_delete=models.CASCADE )
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("نظر")
        verbose_name_plural = ("نظرات")

    def __str__(self):
        return self.product.name

