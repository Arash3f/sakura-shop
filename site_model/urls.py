from django.urls import path , include
from . import views

urlpatterns = [
    path('v1/site_information/', views.site_information.as_view()),
    path('v1/about_we/', views.about_we.as_view()),
    path('v1/contact_us/', views.contact_us.as_view()),
]