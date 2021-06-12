from django.urls import reverse,resolve



class TestUrls:


    def test_token_obtain_url(self):
        path = reverse('token_obtain')
        assert resolve(path).view_name == "token_obtain"