from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
	TokenVerifyView,
)
urlpatterns = [
	# token
	path('v1/auth/obtain_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/auth/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'), 
	# authentications
	path('v1/auth/register/' , views.register_user.as_view() , name="register_user"),
		# email for change password
	path('v1/request_reset_email/', views.RequestPasswordResetEmail.as_view()),
	path('v1/check_reset_token/<uidb64>/<token>/', views.PasswordTokenCheck.as_view(), name = "password-reset-confirm"),
	path('v1/change_password/', views.SetNewPassword.as_view(), name = "SetNewPassword"),
		# confirm account
	path('v1/check_confirm_email/', views.Check_Confirm_Email.as_view(), name = "email-confirm"),
	# img page
	path('v1/login_pic/' , views.login_pic ),
	path('v1/register_pic/' , views.register_pic ),
	path('v1/re_password_pic/' , views.re_password_pic ),
	path("v1/username/" , views.username ),

]