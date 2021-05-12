from django.urls import path , include
from . import views

urlpatterns = [
    path('v1/site_information/', views.site_information.as_view()),
]