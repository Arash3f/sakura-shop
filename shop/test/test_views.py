from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import users
from shop.models import Order, OrderRow
from product.models import packs, product, product_cost

class Test_Shop(APITestCase):

    def setUp(self):
        self.url_1 = reverse('Add_Order_Row')
        # self.url_2 = reverse('Show_Order')
        self.url_3 = reverse('modify_Order')
        self.url_4 = reverse('Cancel_Order_Row')

        # create Order
        self.user = User.objects.create_user(
            username="string",
            password="string",
            email="user@example.com",
            is_active=True,
            is_staff=True,
        )
        self.user.save()
        self.user_1 = users.objects.create(
            user = self.user
        )
        self.user_1.save()
        self.order = Order.objects.create(
            user = self.user_1,
            status=1,
        )
        self.order.save()
        # create product 
        self.product_1 = product.objects.create(
            name="productone",
            slug="productone",
            inventory=1000
        )
        self.product_1.save()
        # create pack :
        self.pack = packs.objects.create(
            title = "pack_one",
            weight =  100 ,
        )
        self.pack.save()
        # create coste :
        self.product_one_cost = product_cost.objects.create(
            product = self.product_1 ,
            pack = self.pack ,
            cost = 1 ,
        )
        self.product_one_cost.save()

        self.client.login(username="string",password="string")

        return super().setUp()
    
    def test_add_new_order_ok(self):
        self.data = {
            "product": self.product_1.id ,
            "amount": 10 , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_1,self.data ,format='json')
        order = Order.objects.filter(user=self.user_1 )
        order_row = OrderRow.objects.filter(product=self.product_1)

        self.assertEqual(response.data, self.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(order.count(), 1)
        self.assertEqual(order[0].total_price, 10*1)
        self.assertEqual(order_row.count(), 1)
        self.assertEqual(order_row[0].amount, 10)
        self.assertEqual(order_row[0].pack.pack, self.pack)

    def test_add_new_order_incorect_amount(self):
        self.data = {
            "product": self.product_1.id ,
            "amount": 10000 , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_1,self.data ,format='json')
        self.assertEqual(response.data, {'inventory': 'Product inventory is not enough '} )
        self.assertEqual(response.status_code, 400)
    def test_add_new_order_2ok(self):
        self.data = {
            "product": self.product_1.id ,
            "amount": 500 , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_1,self.data ,format='json')
        response = self.client.post(self.url_1,self.data ,format='json')
        self.data['amount'] = 1000
        self.assertEqual(response.data, self.data)
        self.assertEqual(response.status_code, 201)

        order = Order.objects.filter(user=self.user_1 )
        order_row = OrderRow.objects.filter(product=self.product_1)
        self.assertEqual(order.count(), 1)
        self.assertEqual(order[0].total_price, 1000*1)
        self.assertEqual(order_row.count(), 1)
        self.assertEqual(order_row[0].amount, 1000)
        self.assertEqual(order_row[0].pack.pack, self.pack)
    
    # modify order :

    def test_modify_order_ok_increase(self):

        self.data = {
            "product": self.product_1.id ,
            "amount": 100 , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_1,self.data ,format='json')
        self.data = {
            "product": self.product_1.id ,
            "amount": "+100" , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_3,self.data ,format='json')
        self.assertEqual(response.data, {"ok"})
        order_row = OrderRow.objects.filter(product=self.product_1)
        self.assertEqual(order_row[0].amount, 200)
        order = Order.objects.filter(user=self.user_1 )
        self.assertEqual(order[0].total_price, 200)

    def test_modify_order_ok_decrease(self):

        self.data = {
            "product": self.product_1.id ,
            "amount": 100 , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_1,self.data ,format='json')
        self.data = {
            "product": self.product_1.id ,
            "amount": "-100" , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_3,self.data ,format='json')
        self.assertEqual(response.data, {"ok"})
        order_row = OrderRow.objects.filter(product=self.product_1)
        self.assertEqual(order_row.count(), 0)
        order = Order.objects.filter(user=self.user_1 )
        self.assertEqual(order[0].total_price, 0)
    
    def test_modify_order_failed_inventory(self):

        self.data = {
            "product": self.product_1.id ,
            "amount": 100 , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_1,self.data ,format='json')
        self.data = {
            "product": self.product_1.id ,
            "amount": "+100000" , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_3,self.data ,format='json')
        self.assertEqual(response.data, {'inventory': 'Product inventory is not enough'})

    def test_modify_order_failed_amount(self):

        self.data = {
            "product": self.product_1.id ,
            "amount": 100 , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_1,self.data ,format='json')
        self.data = {
            "product": self.product_1.id ,
            "amount": "-101" , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_3,self.data ,format='json')
        self.assertEqual(response.data, {'ok'})

        order_row = OrderRow.objects.filter(product=self.product_1)
        self.assertEqual(order_row.count(), 0)
        order = Order.objects.filter(user=self.user_1 )
        self.assertEqual(order[0].total_price, 0)

    
    # order row cancel :

    def test_cancel_order_row(self):

        self.data = {
            "product": self.product_1.id ,
            "amount": 100 , 
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_1,self.data ,format='json')
        self.data = {
            "product": self.product_1.id ,
            "pack": self.pack.id ,
        }
        response = self.client.post(self.url_4,self.data ,format='json')
        self.assertEqual(response.data, {'order_row deleted'})
        self.assertEqual(response.status_code, 200)

        order_row = OrderRow.objects.filter(product=self.product_1)
        self.assertEqual(order_row.count(), 0)
        order = Order.objects.filter(user=self.user_1 )
        self.assertEqual(order[0].total_price, 0)

