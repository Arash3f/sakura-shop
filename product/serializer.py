from .models import product ,packs , product_cost
from .models import product_group 
from rest_framework import serializers

class product_group_serializer(serializers.ModelSerializer):

    class Meta:
        model = product_group
        fields = ('id','name' ,'group')

class product_group_serializer2(serializers.ModelSerializer):
    # sub = product_group_serializer2_helper(many=True, read_only=True)
    sub_group = serializers.StringRelatedField(many=True)
    class Meta:
        model = product_group
        fields = ('name' ,'sub_group')

class product_list_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = product
        fields = ('id','slug','name','show_cost','available','picture')


class pack_list_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = packs
        fields = ('id','title','weight','parent')
    
class product_cost_serializer(serializers.ModelSerializer):
    class Meta:
        model = product_cost
        fields = ('pack' , 'cost' ,'discount' , 'available' )
        depth = 1

class product_serializer(serializers.ModelSerializer):
    product_cost = product_cost_serializer(many=True, read_only=True)

    class Meta:
        model = product
        fields = ('name','inventory','available','product_cost')
        



