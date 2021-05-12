from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# site detail ...
class Private_Site_Information(models.Model):
    name = models.CharField(verbose_name="نام سایت" ,max_length = 100 , blank=True , null = True )
    title = models.TextField(verbose_name="موضوع سایت" , blank=True , null = True)
    description = models.TextField(verbose_name="توضیحات سایت", blank=True , null = True ,help_text = "توضیح کوتاهی درباره ی سایت (همانند شعار سایت)")
    address = models.TextField(verbose_name="آدرس سایت", blank=True , null = True )
    phone = models.CharField(verbose_name="تلفون سایت" , max_length=11 , blank=True , null = True)
    email = models.EmailField(verbose_name = "ایمیل سایت" ,max_length = 100 , blank=True , null = True)
    telegram_id = models.CharField(verbose_name="آدرس تلگرام سایت" ,max_length = 100 , blank=True , null = True)
    instagram_id = models.CharField(verbose_name="آدرس اینستاگرام سایت" ,max_length = 100 , blank=True , null = True)
    whatsapp_id = models.CharField(verbose_name="آدرس واتس آپ سایت" ,max_length = 100 , blank=True , null = True)

    class Meta:
        verbose_name = ("اطلاعات")
        verbose_name_plural = ("اطلاعات")

    def __str__(self):
        return self.name

    
    