from django.urls import path
from accounts import views
from rest_framework_jwt.views import (obtain_jwt_token,
									refresh_jwt_token,
									)

urlpatterns = [
	path('v1/auth/obtain_token/', obtain_jwt_token),
	path('v1/auth/refresh_token/', refresh_jwt_token),   
	path('v1/auth/register/' , views.register_user.as_view() , name="register_user"),
	# for page img
	path('v1/login_pic/' , views.login_pic ),
	path('v1/register_pic/' , views.register_pic ),
	path('v1/re_password_pic/' , views.re_password_pic ),
]