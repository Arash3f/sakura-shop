from site_model.models import (Private_Site_Information ,
                                About_Us ,
                                Contact_Us
                                )
from rest_framework import serializers

class site_model_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Private_Site_Information
        fields = '__all__'

class about_we_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = About_Us
        fields = '__all__'

class contact_us_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact_Us
        fields = '__all__'