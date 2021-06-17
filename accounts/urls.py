from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

	# Token :
	path('api/v1/obtain_token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('api/v1/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'), 
	
	path('api/v1/register/' , views.register_user.as_view() , name="register_user"),
	path('api/v1/check_confirm_email/', views.Check_Confirm_Email.as_view(), name = "email_confirm"),
	# request for give a reset email :
	path('api/v1/request_reset_email/', views.RequestPasswordResetEmail.as_view(), name = "request_reset_email"),
	# check uidb64  and token :
	path('api/v1/check_reset_token/<uidb64>/<token>/', views.PasswordTokenCheck, name = "check_reset_token"),
	# change password :
	path('api/v1/change_password/', views.SetNewPassword.as_view(), name = "change_password"),
	# return username and user order_row count :
	path("api/v1/username/" , views.username , name = "catch_username"),
	# img :
	path('api/v1/login_pic/' , views.login_pic , name = "login_pic"),
	path('api/v1/register_pic/' , views.register_pic , name = "register_pic"),
	path('api/v1/re_password_pic/' , views.re_password_pic , name = "re_password_pic"),

]