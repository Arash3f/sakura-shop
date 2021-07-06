from django.db import models
from accounts.models import users
from product.models import product , product_cost
# Create your models here.

class OrderRow(models.Model):
	product = models.ForeignKey(product , on_delete=models.CASCADE)
	order =models.ForeignKey("Order",  on_delete=models.CASCADE,related_name='rows')
	amount = models.IntegerField()
	pack = models.ForeignKey(product_cost , on_delete=models.PROTECT)
	price = models.IntegerField(default=0)

	class Meta:
		verbose_name = ('ردیف')
		verbose_name_plural=('ردیف ها')

	def Order_row_user(self):
		return self.order.user.user.username

	def Increase_amount(self , amount ):
		self.amount += amount
		self.save()
	
	def Increase_price(self , amount ,cost):
		self.price += cost*amount
		self.save()

	def Decrease_amount(self , amount ):
		self.amount -= amount
		self.save()
	
	def Decrease_price(self , amount ,cost):
		self.price -= cost*amount
		self.save()

class Order(models.Model):
	# Status values. DO NOT EDIT
	STATUS_SHOPPING = 1
	STATUS_SUBMITTED = 2
	STATUS_CANCELED = 3
	STATUS_SENT = 4
	choi = ( (  STATUS_SHOPPING  , "در حال خرید" ),
			(  STATUS_SUBMITTED   , "ثبت‌شده"  ),
			( STATUS_CANCELED   , "لغوشده"  ),
			(  STATUS_SENT   , "ارسال‌شده"  )
			)
	user = models.ForeignKey(users , on_delete=models.CASCADE)
	order_time = models.DateTimeField(null=True)
	status = models.IntegerField(choices=choi)
	total_price = models.IntegerField(default=0)

	class Meta:
		verbose_name = ('سبد')
		verbose_name_plural=('سبد ها')

	def Order_user(self):
		return self.user.user.username

	def __str__(self):
		return self.user.user.get_username()
	
	def Increase_total_price(self , cost ,  amount ):
		self.total_price += cost*amount
		self.save()

	def Decrease_total_price(self , cost ,  amount ):
		self.total_price -= cost*amount
		self.save()
