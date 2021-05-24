from .models import product_group , product ,packs , product_cost
from rest_framework import serializers

class product_group_serializer(serializers.ModelSerializer):

    class Meta:
        model = product_group
        fields = ('id','name' ,'group')

class product_list_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = product
        fields = ('slug','name','product_cost','picture')
        depth = 1

class pack_list_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = packs
        fields = ('title','weight')
    
class product_cost_serializer(serializers.ModelSerializer):
    class Meta:
        model = product_cost
        fields = ('pack' , 'cost' ,'discount' , 'available' )

class product_serializer(serializers.ModelSerializer):
    product_cost = product_cost_serializer(many=True, read_only=True)

    class Meta:
        model = product
        fields = ('name','inventory','available','product_cost')
        



