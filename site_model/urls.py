from django.urls import path , include
from site_model import views

urlpatterns = [
    path('api/v1/site_information/', views.site_information.as_view() , name="site_information"),
    path('api/v1/About_Us/', views.About_Us.as_view() , name = "About_Us"),
    path('api/v1/contact_us/', views.contact_us.as_view() , name= "contact_us"),
]