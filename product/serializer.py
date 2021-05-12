from .models import product_group , product
from rest_framework import serializers

class product_group_serializer(serializers.ModelSerializer):
    sub_group = serializers.StringRelatedField(many=True)

    class Meta:
        model = product_group
        fields = ('name' ,'sub_group')
        depth = 1

class product_list_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = product
        fields = ('name','description_one','cost','picture')
