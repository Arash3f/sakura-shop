from .models import Private_Site_Information
from rest_framework import serializers

class site_model_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Private_Site_Information
        fields = '__all__'