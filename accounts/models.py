from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

# uniquee email
User._meta.get_field('email')._unique = True

# Create your models here.
class users(models.Model):
    user = models.OneToOneField(User , related_name='user',  on_delete=models.CASCADE)
    national_code = models.IntegerField('national_code' , blank=True , null=True)
    phone = models.IntegerField("phone number"  , blank=True , null = True)
    money = models.IntegerField("money" , default=0 )
    date_of_birth = models.DateField("date of birth", blank=True , null = True)
    registration_date = models.DateField("registration date" , auto_now_add=True)
    picture = models.ImageField("picture" , upload_to = "users_picture/" , null=True , blank=True)


        