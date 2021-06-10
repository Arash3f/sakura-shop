from django.urls import path
from shop import views

urlpatterns = [
    path("v1/new_Order/" , views.Add_Order_Row.as_view() , name='Add_Order_Row'),
    path("v1/Show_Order/" , views.Show_Order.as_view() , name='Show_Order'),
    path("v1/Show_all_Order/" , views.Show_all_Order.as_view() , name='Show_all_Order'),
    path("v1/modify_Order/" , views.modify_Order , name='modify_Order'),
    path("v1/Cancel_Order/" , views.Cancel_Order , name='Cancel_Order'),
    path("v1/Cancel_Order_Row/" , views.Cancel_Order_Row , name='Cancel_Order_Row'),
]