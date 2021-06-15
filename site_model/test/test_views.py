from rest_framework.test import APITestCase
from django.urls import reverse
from site_model.models import Contact_Us

class Test_contact_us(APITestCase):

    def setUp(self):
        self.url = reverse('contact_us')
        self.data = {
            "title": "1", 
            "name" : "arash" ,
            "email": "arash@yahoo.com" ,
            "phone": "09176017702",
            "body" : "slm",
        }
        return super().setUp()
    
    def test_create_msg(self):
        response = self.client.post(self.url,self.data,format='json')
        self.assertEqual(response.status_code, 201)





        