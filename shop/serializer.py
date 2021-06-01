from rest_framework import serializers , status
from accounts.models import users
from rest_framework.response import Response
from shop.models import OrderRow , Order
from product.models import product_cost
class Order_Row_serializer(serializers.ModelSerializer):

    def create(self, validated_data):

        product = validated_data['product']
        amount = validated_data['amount']
        user = users.objects.get(user_id = self.context['request'].user.id)
        pack = validated_data['pack']

        if pack.product == product :
            if Order.objects.filter(user = user , status= 1).count() == 0 :
                order = Order.objects.create(
                    user = user ,
                    status = 1 ,
                    total_price=pack.cost,
                )
                new_order_row = OrderRow.objects.create(
                    product = product,
                    order = order ,
                    amount = amount,
                    pack = pack,
                )
                return new_order_row
            elif Order.objects.filter(user = user, status= 1).count() == 1 :
                order = Order.objects.get(
                    user = user ,
                )
                order.total_price+=pack.cost
                order.save()
                new_order_row = OrderRow.objects.create(
                    product = product,
                    order = order ,
                    amount = amount,
                    pack = pack,
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
        