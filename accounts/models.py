from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

# uniquee email
User._meta.get_field('email')._unique = True

# Create your models here.
class users(models.Model):
    user = models.OneToOneField(User , related_name='user',  on_delete=models.CASCADE)
    phone = models.IntegerField("phone number"  , blank=True , null = True)
    money = models.IntegerField("money" , default=0 )
    registration_date = models.DateField("registration date" , auto_now_add=True)
    picture = models.ImageField("picture" , upload_to = "users_picture/" , null=True , blank=True)


class detail(models.Model):
    login_img = models.ImageField("login" , upload_to = "login_img/" , null=True , blank=True)
    register_img = models.ImageField("register" , upload_to = "register_img/" , null=True , blank=True)
    re_password_img = models.ImageField("re password" , upload_to = "re_password_img/" , null=True , blank=True)
    
