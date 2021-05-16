from django.http import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializer import user_register 
from django.contrib.auth.models import User
from .models import detail
from rest_framework import (generics,
                            mixins ,
                            status,
                            )
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


class register_user(generics.GenericAPIView , mixins.CreateModelMixin):
    serializer_class = user_register
    
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        email = request.data['email']
        users = User.objects.all()
        new_json = {}
        if users.filter(username = username):
            new_json['user'] = False
            if users.filter(email = email):
                new_json['email'] = False
            else:
                new_json['email'] = True
            return Response(new_json , status=status.HTTP_200_OK)
        else:
            new_json['user'] = True
            if users.filter(email = email):
                new_json['email'] = False
                return Response(new_json , status=status.HTTP_200_OK)
            else:
                return self.create(request, *args, **kwargs)
            
@api_view(('GET',))
def login_pic(request):
    img = detail.objects.get(pk=1).login_img
    return Response({"url":img.url} , status=status.HTTP_200_OK)

@api_view(('GET',))
def register_pic(request):
    img = detail.objects.get(pk=1).register_img
    return Response({"url":img.url} , status=status.HTTP_200_OK)

@api_view(('GET',))
def re_password_pic(request):
    img = detail.objects.get(pk=1).re_password_img
    return Response({"url":img.url} , status=status.HTTP_200_OK)

@api_view(('GET',))
@permission_classes([IsAuthenticated])
def username(request):
    return Response({request.user.username} , status=status.HTTP_200_OK) 
