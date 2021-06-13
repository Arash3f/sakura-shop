from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# uniquee email
User._meta.get_field('email')._unique = True

# Create your models here.
class users(models.Model):
    user = models.OneToOneField(User , related_name='user',  on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'((\+|00)98|0)9\d{9}', message="Phone number must be entered in the format: '09176666666'. Up to 11 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=11, blank=True) # validators should be a list
    money = models.IntegerField("money" , default=0 )
    registration_date = models.DateField("registration date" , auto_now_add=True)
    picture = models.ImageField("picture" , upload_to = "users_picture/" , null=True , blank=True)

    class Meta:
        verbose_name = ("کاربر")
        verbose_name_plural = ("کاربران")

    def __str__(self):
        return self.user.username
        
    def email(self):
        return self.user.email

class detail(models.Model):
    login_img = models.ImageField("login" , upload_to = "login_img/" , null=True , blank=True)
    register_img = models.ImageField("register" , upload_to = "register_img/" , null=True , blank=True)
    re_password_img = models.ImageField("re password" , upload_to = "re_password_img/" , null=True , blank=True)
    
    def __str__(self):
        return "part"

    class Meta:
        verbose_name = ("تصویر")
        verbose_name_plural = ("تصاویر")
