from django.test import SimpleTestCase
from django.urls import resolve, reverse
from accounts import views
class test_accounts_urls(SimpleTestCase):

    def test_register(self):
        url = reverse('register_user')
        self.assertEquals(resolve(url).func.view_class , views.register_user)

    def test_check_confirm_email(self):
        url = reverse('email_confirm')
        self.assertEquals(resolve(url).func.view_class , views.Check_Confirm_Email)

    def test_request_reset_email(self):
        url = reverse('request_reset_email')
        self.assertEquals(resolve(url).func.view_class , views.RequestPasswordResetEmail)

    def test_register(self):
        url = reverse('check_reset_token')
        self.assertEquals(resolve(url).func.view_class , views.PasswordTokenCheck)

    def test_register(self):
        url = reverse('change_password')
        self.assertEquals(resolve(url).func.view_class , views.SetNewPassword)

    def test_register(self):
        url = reverse('username')
        self.assertEquals(resolve(url).func , views.catch_username)

    def test_register(self):
        url = reverse('login_pic')
        self.assertEquals(resolve(url).func , views.login_pic)

    def test_register(self):
        url = reverse('register_pic')
        self.assertEquals(resolve(url).func , views.register_pic)

    def test_register(self):
        url = reverse('re_password_pic')
        self.assertEquals(resolve(url).func , views.re_password_pic)

        