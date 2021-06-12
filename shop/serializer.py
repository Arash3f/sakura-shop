from rest_framework import serializers , status
from accounts.models import users
from rest_framework.response import Response
from shop.models import OrderRow , Order
from product.models import product_cost

from rest_framework.exceptions import APIException
class Order_Row_serializer(serializers.ModelSerializer):

    def create(self, validated_data):

        user = users.objects.get(user_id = self.context['request'].user.id)
        product = validated_data['product']
        amount = validated_data['amount']
        pack = validated_data['pack']

        if pack.product == product :
            if Order.objects.filter(user = user , status= 1).count() == 0 :
                order = Order.objects.create(
                    user = user ,
                    status = 1 ,
                    total_price=pack.cost*amount,
                )

                if product.inventory < amount :
                    raise APIException("There was a problem!")

                new_order_row = OrderRow.objects.create(
                    product = product,
                    order = order ,
                    amount = amount,
                    pack = pack,
                    price = pack.cost*amount,
                )
                return new_order_row
            elif Order.objects.filter(user = user, status= 1).count() == 1 :
                order = Order.objects.get(
                    user = user ,
                )

                old_row = OrderRow.objects.filter(
                    product = product,
                    order = order,
                    pack = pack,
                    )

                if old_row.count() == 1:

                    if product.inventory < amount+old_row[0].amount :
                        raise APIException("There was a problem!")

                    order.total_price+=pack.cost*amount
                    order.save()
                    row = old_row[0]
                    row.amount +=amount
                    row.price += pack.cost*amount
                    row.save()
                    return row
                else:
                
                    if product.inventory < amount :
                        raise APIException("There was a problem!")
                    order.total_price+=pack.cost*amount
                    order.save()
                    new_order_row = OrderRow.objects.create(
                        product = product,
                        order = order ,
                        amount = amount,
                        pack = pack,
                        price = pack.cost*amount,
                    )
                    return new_order_row
            else:
                pass 
    class Meta:
        model = OrderRow
        fields = ('product' , 'amount' , 'pack')
        
    
class Order_serializer_helper(serializers.ModelSerializer):
    class Meta:
        model = OrderRow
        fields = "__all__"
        depth = 1
class Order_serializer(serializers.ModelSerializer):
    rows = Order_serializer_helper(many=True)

    class Meta:
        model = Order
        fields = ('id','order_time' , 'status' , 'total_price' , 'rows')
        