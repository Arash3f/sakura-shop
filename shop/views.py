from product.views import product_list
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import (generics,
                            mixins,
                            status,
                            )
from shop.serializer import Order_Row_serializer , Order_serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (api_view, 
                                        permission_classes,
                                        )
from shop.models import OrderRow , Order
from product.models import product_cost , product
from rest_framework.response import Response
# from product
def index(request):
    return HttpResponse("slm")

class Add_Order_Row(generics.GenericAPIView , mixins.CreateModelMixin ):
    serializer_class = Order_Row_serializer
    permission_classes = [IsAuthenticated,]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs )
    
class Show_Order(generics.GenericAPIView  , mixins.ListModelMixin):
    serializer_class = Order_serializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated,]
    
    def get_queryset(self):
        user = self.request.user
        order = Order.objects.filter(user_id = user.id , status = 1)
        return order
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class Show_all_Order(generics.GenericAPIView  , mixins.ListModelMixin):
    serializer_class = Order_serializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated,]
    
    def get_queryset(self):
        user = self.request.user
        order = Order.objects.filter(user_id = user.id )
        return order
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
@api_view(('POST',))
@permission_classes([IsAuthenticated])
def modify_Order(request):
    user = request.user
    order = Order.objects.get(user_id = user.id , status=1)
    pproduct_id = request.data["product"]
    pproduct = product.objects.get(id = pproduct_id )
    pack = request.data["pack"]
    cost = product_cost.objects.get(product_id = pproduct.id , pack_id = pack).cost
    amount =  request.data["amount"]
    order_row =OrderRow.objects.filter(order = order , product_id = pproduct.id)[0]
    
    
    if amount[0] == "-":
        if order_row.amount <= int(amount[1:]):
            order.total_price-=int(order_row.amount)*cost
            order_row.delete()
        else : 
            order_row.amount-=int(amount[1:])
            order_row.price -=int(amount[1:])*cost
            order.total_price-=int(amount[1:])*cost
            order_row.save()
            order.save()
    elif amount[0] == "+":
        total_amount = order_row.amount + int(amount[1:])
        if pproduct.inventory < total_amount:
            return Response({"error"} , status=status.HTTP_200_OK)
        else : 
            order_row.amount+=int(amount[1:])
            order_row.price +=int(amount[1:])*cost
            order.total_price+=int(amount[1:])*cost
            order_row.save()
            order.save()
    
    
    return Response({"ok"} , status=status.HTTP_200_OK)


@api_view(('GET',))
@permission_classes([IsAuthenticated]) 
def Cancel_Order(request):
    user = request.user
    order = Order.objects.get(user_id = user.id , status=1)
    order.delete()
    return Response({"order deleted"} , status=status.HTTP_200_OK)

@api_view(('POST',))
@permission_classes([IsAuthenticated]) 
def Cancel_Order_Row(request):
    user = request.user
    order = Order.objects.get(user_id = user.id , status=1)
    pproduct_id = request.data["product"]
    pproduct = product.objects.get(id = pproduct_id )
    pack = request.data["pack"]
    cost = product_cost.objects.get(product_id = pproduct.id , pack_id = pack).cost
    order_row =OrderRow.objects.filter(order = order , product_id = pproduct.id)[0]
    order.total_price-=int(order_row.amount)*cost
    if order.total_price == 0 :
        order.delete()
    else:
        order.save()
    order_row.delete()
    return Response({"order deleted"} , status=status.HTTP_200_OK)
    
    
    # {
    #     "product":"1",
    #     "pack":"3",
    #     "amount":"-20"
    # }