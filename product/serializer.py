from product.models import (
    product ,
    Packs ,
    Product_Cost , 
    ProductGallery ,
    product_group,
)
from rest_framework import serializers

class product_serializer_helper_picture(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields =('picture',)
        
class product_list_serializer(serializers.ModelSerializer):
    picture = product_serializer_helper_picture(many=True )
    class Meta:
        model = product
        fields = ('slug','name','show_cost','available','picture')

# ************************************************************************

class product_serializer_helper_cost(serializers.ModelSerializer):
    class Meta:
        model = Product_Cost
        fields = ('pack' , 'cost' ,'discount' , 'available' )
        depth = 1

class product_serializer(serializers.ModelSerializer):
    Product_Cost = product_serializer_helper_cost(many=True, read_only=True)
    picture = product_serializer_helper_picture(many=True )

    class Meta:
        model = product
        fields = ('name','inventory','available','Product_Cost','picture' ,'description')

# ************************************************************************

class pack_list_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Packs
        fields = ('id','title','weight','parent')

# ************************************************************************

class product_group_serializer(serializers.ModelSerializer):

    class Meta:
        model = product_group
        fields = ('id','name' ,'group' , 'open' , 'picture')
