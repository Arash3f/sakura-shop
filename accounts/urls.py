from django.urls import path
from accounts import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('v1/auth/obtain_token/', obtain_jwt_token),
    path('v1/auth/refresh_token/', refresh_jwt_token),   
    path('v1/auth/register/' , views.register_user.as_view() , name="register_user"),
]