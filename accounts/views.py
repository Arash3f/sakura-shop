from django.http import request
from .serializer import user_register 
from django.contrib.auth.models import User
from .models import detail
from rest_framework import (generics,
                            mixins ,
                            status,
                            )
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

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
            # return Response(new_json , status=status.HTTP_400_BAD_REQUEST)
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

# check email is reserved
@api_view(['POST'])
def check_email_is_available(request):
    check = User.objects.all().filter(email = request.data["params"]["email"])
    if len(check) == 0:
        return Response({"reserved": False},status=status.HTTP_200_OK)
    else:
        return Response({"reserved": True},status=status.HTTP_400_BAD_REQUEST)
