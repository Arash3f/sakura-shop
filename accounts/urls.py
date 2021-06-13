from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

	# Token :
	path('v1/obtain_token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('v1/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'), 
	
	path('v1/register/' , views.register_user.as_view() , name="register_user"),
	path('v1/check_confirm_email/', views.Check_Confirm_Email.as_view(), name = "email_confirm"),

	path('v1/request_reset_email/', views.RequestPasswordResetEmail.as_view(), name = "request_reset_email"),
	path('v1/check_reset_token/<uidb64>/<token>/', views.PasswordTokenCheck.as_view(), name = "check_reset_token"),
	path('v1/change_password/', views.SetNewPassword.as_view(), name = "change_password"),

	path("v1/username/" , views.username , name = "catch_username"),

	path('v1/login_pic/' , views.login_pic ),
	path('v1/register_pic/' , views.register_pic ),
	path('v1/re_password_pic/' , views.re_password_pic ),

]