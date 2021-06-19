from django.urls import path , include , re_path
from product import views


urlpatterns = [
    # product :
    path('api/v1/product_list/', views.product_list.as_view() , name="product_list"),
    path('api/v1/top_product/' , views.top_product.as_view(), name="top_product"),
    path('api/v1/best_product/', views.best_product.as_view(), name="best_product"),
    re_path(r'api/v1/similar_product/(?P<slug>[\w-]+)/', views.similar_product.as_view(), name="similar_product"),
    path('api/v1/pack_list/', views.pack_list.as_view()),
    re_path(r'api/v1/product/(?P<slug>[\w-]+)/', views.product.as_view()),
	re_path(r'api/v1/search/(?P<slug>[\w-]+)/' , views.search.as_view() , name = "search_product"),

    re_path(r'api/v1/properties/(?P<slug>[\w-]+)/' , views.properties.as_view() , name="properties"),
    
    # groups :
    path('api/v1/group_list/', views.group_list.as_view()),
    path('api/v1/group_list2/', views.group_list2.as_view()),
]