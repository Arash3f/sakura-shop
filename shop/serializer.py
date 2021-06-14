from rest_framework import serializers , status
from accounts.models import users
from rest_framework.response import Response
from shop.models import OrderRow , Order
from product.models import product_cost , product
from accounts.views import CustomValidation

class Order_Row_serializer(serializers.ModelSerializer):

    def create(self, validated_data):

        user = users.objects.get(user_id = self.context['request'].user.id)
        product = validated_data['product']
        amount = validated_data['amount']
        pack = validated_data['pack']

        if pack.product == product :
            if Order.objects.filter(user = user, status= 1).count() == 1 :
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
                        raise CustomValidation('Product inventory is not enough ','inventory', status_code=status.HTTP_400_BAD_REQUEST)
                    order.Increase_total_price(pack.cost,amount)
                    row = old_row[0]
                    row.Increase_amount(amount)
                    row.Increase_price(pack.cost , amount)
                    return row

                else:
                
                    if product.inventory < amount :
                        raise CustomValidation('Product inventory is not enough ','inventory', status_code=status.HTTP_400_BAD_REQUEST)
                    order.Increase_total_price(pack.cost,amount)
                    new_order_row = OrderRow.objects.create(
                        product = product,
                        order = order ,
                        amount = amount,
                        pack = pack,
                        price = pack.cost*amount,
                    )
                    return new_order_row

            else:
                raise CustomValidation('User shoud have one Order','Order', status_code=status.HTTP_400_BAD_REQUEST)
        else : 
            raise CustomValidation('pack not match to product','Invalid data', status_code=status.HTTP_400_BAD_REQUEST)
    
    class Meta:
        model = OrderRow
        fields = ('product' , 'amount' , 'pack')
        

class Order_serializer_helper_product(serializers.ModelSerializer):
    class Meta:
        model = product
        fields =('id' , "name" ,"slug" ,  "picture" , "available")
class Order_serializer_helper_pack(serializers.ModelSerializer):
    class Meta:
        model = product_cost
        fields =('id' , "discount" ,"available" ,  "cost" )
class Order_serializer_helper(serializers.ModelSerializer):
    product = Order_serializer_helper_product()
    pack = Order_serializer_helper_pack()
    
    class Meta:
        model = OrderRow
        fields =("amount" ,"price" ,  "product" , "pack")
class Order_serializer(serializers.ModelSerializer):
    rows = Order_serializer_helper(many=True)

    class Meta:
        model = Order
        fields = ('total_price' , 'rows')
        