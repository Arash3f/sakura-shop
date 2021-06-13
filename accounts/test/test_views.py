from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.hashers import make_password
from accounts.models import users
from shop.models import Order

class TestViews_Register(APITestCase):

    def setUp(self):
        self.url = reverse('register_user')
        self.data = {
            "username": "string",
            "password": "string",
            "email": "user@example.com"
        }
        self.user = User.objects.create_user(
            username="string",
            password="string",
            email="user@example.com",
            is_active=False,
            is_staff=True,
        )
        self.user.save()
        return super().setUp()

    def test_register_create_new_user_ok(self):
        response = self.client.post(self.url,self.data,format='json')
        self.assertEqual(response.status_code, 200)

    def test_register_create_new_user_Incomplete_information(self):
        data = {
            "password": "string",
            "email": "user@example.com"
        }
        response = self.client.post(self.url,data,format='json')
        self.assertEqual(response.status_code, 400)

    def test_register_create_new_user_Duplicate_account(self):
        response = self.client.post(self.url,self.data,format='json')
        self.assertEqual(response.data, {'user': False, 'email': False})
        
class TestViews_Confirm_Email(APITestCase):

    def setUp(self):
        self.url = reverse('email_confirm')
        self.user = User.objects.create_user(
            username="string",
            password="string",
            email="user@example.com",
            is_active=False,
            is_staff=True,
        )
        self.user.save()
        self.token = RefreshToken.for_user(self.user)
        self.data = {
            "token": str(self.token),
        }
        return super().setUp()

    def test_check_email_ok(self):
        response = self.client.post(self.url,self.data,format='json')
        user = User.objects.get(username = self.user.username)
        user2 = users.objects.get(user=user)
        order = Order.objects.get(user=user2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user.is_active  , True)

    def test_check_email_Incomplete_information(self):
        response = self.client.post(self.url,{},format='json')
        self.assertEqual(response.data, {'error': 'Incomplete information'})
        self.assertEqual(response.status_code, 400)

    def test_check_email_Incorect_token(self):
        data = {
            "token": "strdasdasdasdasding",
        }
        response = self.client.post(self.url,data,format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data , {'error':'token not vaid'})
        
class TestViews_PasswordReset(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="string",
            password="string",
            email="user@example.com",
            is_active=True,
            is_staff=True,
        )
        self.user.save()
        self.uidb64 = urlsafe_base64_encode(smart_bytes(self.user.id))
        self.token = PasswordResetTokenGenerator().make_token(self.user)

        self.data = {"email": "user@example.com"}
        self.data_2={
            "password" : 'new_password',
            "token" : self.token,
            "uidb64" : self.uidb64,
        }

        self.url_1 = reverse('request_reset_email')
        self.url_2 = reverse('check_reset_token',kwargs={"uidb64" : self.uidb64 , "token" : self.token})
        self.url_3 = reverse('change_password')

        return super().setUp()

    def test_request_reset_email_ok(self):
        response = self.client.post(self.url_1,self.data,format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'success': 'Email sent '})

    def test_request_reset_email_invalid_email(self):
        response = self.client.post(self.url_1,{},format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {'error': 'Incomplete information'})

    def test_PasswordTokenCheck(self):
        response = self.client.get(self.url_2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'success': True,
            'message': 'valid',
            'uidb64': self.uidb64,
            'token': self.token,
            })
    def test_SetNewPassword(self):
        response = self.client.patch(self.url_3,self.data_2,format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'ok': 'Password changed '})
        user = User.objects.get(username = self.user.username)
        self.assertEquals(user.check_password("new_password"), True)

class TestViews_catch_username(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="string",
            password="string",
            email="user@example.com",
            is_active=True,
            is_staff=True,
        )
        self.user.save()

        self.url_1 = reverse('catch_username')

        return super().setUp()

    def test_catch_username(self):
        self.client.login(username="string",password="string")
        response = self.client.get(self.url_1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'username': 'string'})

    def test_catch_username_by_first_name(self):
        self.client.login(username="string",password="string")
        user = User.objects.get(username=self.user.username)
        user.first_name = "arash"
        user.save()
        response = self.client.get(self.url_1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'username': 'arash'})

        