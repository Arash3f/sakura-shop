from .models import product ,packs , product_cost , ProductGallery
from .models import product_group 
from rest_framework import serializers
from product.models import Properties

class product_group_serializer(serializers.ModelSerializer):

    class Meta:
        model = product_group
        fields = ('id','name' ,'group' , 'open' , 'picture')

class product_group_serializer2(serializers.ModelSerializer):
    # sub = product_group_serializer2_helper(many=True, read_only=True)
    sub_group = serializers.StringRelatedField(many=True)
    class Meta:
        model = product_group
        fields = ('id','name' ,'sub_group' ,'open')

class product_serializer_helper_picture(serializers.ModelSerializer):

    class Meta:
        model = ProductGallery
        fields =('picture',)
        
class product_list_serializer(serializers.ModelSerializer):
    picture = product_serializer_helper_picture(many=True )
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
        fields = ('id','pack' , 'cost' ,'discount' , 'available' )
        depth = 1

class product_serializer_helper_properties(serializers.ModelSerializer):

    class Meta:
        model = Properties
        fields = ("one"   ,"two"   ,"three" ,"four"  ,"five"  ,"six"   ,"seven" ,"eight" ,"nine"  ,"ten" )

class product_serializer(serializers.ModelSerializer):
    product_cost = product_cost_serializer(many=True, read_only=True)
    product_properties = product_serializer_helper_properties( read_only=True)
    picture = product_serializer_helper_picture(many=True )

    class Meta:
        model = product
        fields = ('id','name','inventory','available','product_properties','product_cost','picture' )

class product_similar_list_serializer(serializers.ModelSerializer):
    picture = product_serializer_helper_picture(many=True )

    class Meta:
        model = product
        fields = ('slug','name','show_cost','available','picture')
    
        

    

