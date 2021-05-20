from django.http import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializer import (user_register ,
                        RequestPasswordResetEmailSerializer , 
                        SetNewPasswordSerializer,
                        )
from django.contrib.auth.models import User
from .models import detail
from rest_framework import (generics,
                            mixins ,
                            status,
                            )
from rest_framework.response import Response
from rest_framework.decorators import (api_view, 
                                        permission_classes,
                                        )
from django.urls import reverse

from django.core.mail import EmailMultiAlternatives

from django.core.mail import send_mail
from django.utils.http import (urlsafe_base64_decode, 
                                urlsafe_base64_encode,
                                )
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import (DjangoUnicodeDecodeError, 
                                    smart_bytes, smart_str,
                                    )
from rest_framework_simplejwt.tokens import RefreshToken
from onshop import settings
import jwt
from django.contrib.sites.shortcuts import get_current_site

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
                self.create(request, *args, **kwargs)
                user = User.objects.get(email=email)
                token = RefreshToken.for_user(user)
                current_site = get_current_site(request).domain
                relativeLink = reverse('email-confirm')
                absurl = 'http://'+current_site+relativeLink+'?token='+str(token)
                email_body ="""با سلام
                متن پیام .....  """+"\n"+" نام شما :"+user.username+"\n"+"link : "+absurl
                send_mail(subject="Sakura shop support" , message=email_body , from_email="alfshop3@gmail.com" ,recipient_list=[email] , fail_silently=False)
                return Response({"success" : "Email sent "} , status=status.HTTP_200_OK)

# first user request for give email  
class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = RequestPasswordResetEmailSerializer

    def post(self , request):

        serializer = self.serializer_class(request.data)
        email = request.data['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request).domain
            relativeLink = reverse('password-reset-confirm' , kwargs={"uidb64" : uidb64 , "token" : token})
            absurl = 'http://'+current_site+relativeLink
            email_body ="""با سلام
            متن پیام .....  """+"\n"+" نام شما :"+user.username+"\n"+"link : "+absurl

            # html_content = '<p>This is an <strong>important</strong> message.</p>'
            # msg = EmailMultiAlternatives(())
            # msg = EmailMultiAlternatives(subject="Sakura shop support" , body=email_body , from_email="alfshop3@gmail.com" ,to=[email] )
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            
            send_mail(subject="Sakura shop support" , message=email_body , from_email="alfshop3@gmail.com" ,recipient_list=[email] , fail_silently=False)
        
        return Response({"success" : "Email sent "} , status=status.HTTP_200_OK)

# check token for reset password
class PasswordTokenCheck(generics.GenericAPIView):
    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64 ))
            user = User.objects.get(id =id )
            if not PasswordResetTokenGenerator().check_token(user , token):
                return Response({"error":"token not vaid"} , status = status.HTTP_200_OK)
            return Response({  
                "success":True , 
                "message":"valid",
                "uidb64" : uidb64 , 
                "token" : token
            } , status = status.HTTP_200_OK)

        except DjangoUnicodeDecodeError:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({"error":"token not vaid"} , status = status.HTTP_200_OK)

# change password
class SetNewPassword(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data= request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"ok":"Password changed "} , status = status.HTTP_200_OK)

# confirm user email 
class Check_Confirm_Email(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            pyload = jwt.decode(token,settings.SECRET_KEY)
            user = User.objects.get(id =pyload["user_id"] )

            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({"email":"email activated"} , status = status.HTTP_200_OK)
        except jwt.ExpiredSignature as identifier:
            return Response({"error":"activate expired"} , status = status.HTTP_200_OK)
        except jwt.exceptions.DecodeError as identifier:
            return Response({"error":"token not vaid"} , status = status.HTTP_200_OK)

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
    return Response({"username":request.user.username} , status=status.HTTP_200_OK) 