from django.urls import path , include
from . import views


urlpatterns = [
    # product :
    path('v1/product_list/', views.product_list.as_view()),
    path('v1/top_product/' , views.top_product.as_view()),
    path('v1/best_product_one/', views.best_product_one.as_view()),
    path('v1/best_product_two/', views.best_product_two.as_view()),
    # groups :
    path('v1/group_list/', views.group_list.as_view()),
]