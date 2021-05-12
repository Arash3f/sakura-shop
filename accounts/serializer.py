from rest_framework import serializers , status
from django.contrib.auth.models import User
from rest_framework.response import Response

class user_register(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            is_active=True,
            is_staff=True,
        )
        return user
    class Meta:
        model = User
        fields = ("username", "password", "email")

