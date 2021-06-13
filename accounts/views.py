from django.http import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from accounts.serializer import (
                        User_Register_Serialiaer ,
                        RequestPasswordResetEmailSerializer , 
                        SetNewPasswordSerializer,
                        Check_Confirm_Email_serializer,
                        )
from django.contrib.auth.models import User
from accounts.models import detail
from rest_framework import (
                            generics,
                            mixins ,
                            status,
                            )
from rest_framework.response import Response
from rest_framework.decorators import (
                                        api_view, 
                                        permission_classes,
                                        )
from django.urls import reverse

# email section ===
from django.core.mail import EmailMultiAlternatives
from datetime import datetime
from email.mime.image import MIMEImage
from django.template.loader import get_template
import os
# 
from django.core.mail import send_mail
from django.utils.http import (
                                urlsafe_base64_decode, 
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
from rest_framework.exceptions import ValidationError
from coreapi.compat import force_text

from rest_framework.exceptions import APIException
class CustomValidation(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Bad request'

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else: self.detail = {'detail': force_text(self.default_detail)}


class register_user(generics.GenericAPIView , mixins.CreateModelMixin):
    serializer_class = User_Register_Serialiaer
    
    def post(self, request, *args, **kwargs):
        try:
            username = request.data['username']
            email = request.data['email']
        except KeyError as e :
            raise CustomValidation('Incomplete information','error', status_code=status.HTTP_400_BAD_REQUEST)
        
        users = User.objects.all()
        new_json = {}

        # check available user with this username
        if users.filter(username = username):
            new_json['user'] = False
            # check available user with this email
            if users.filter(email = email):
                new_json['email'] = False
            else:
                new_json['email'] = True
            return Response(new_json , status=status.HTTP_200_OK)
        else:
            new_json['user'] = True
            # check available user with this email
            if users.filter(email = email):
                new_json['email'] = False
                return Response(new_json , status=status.HTTP_200_OK)
            else:
                # create user
                self.create(request, *args, **kwargs)
                user = User.objects.get(email=email)
                token = RefreshToken.for_user(user)
                current_site = get_current_site(request).domain
                relativeLink = reverse('email-confirm')
                absurl = 'http://'+current_site+relativeLink+str(token)

                message = get_template("confirm_email.html").render({
                                        'username': user.username ,
                                        'absurl' : absurl,
                                    })
                mail = EmailMultiAlternatives(
                                    "تایید ایمیل",
                                    message,
                                    from_email="alfshop3@gmail.com",
                                    to=[email],
                                )
                mail.mixed_subtype = 'related'
                # add img to email :
                mail.attach_alternative(message, "text/html")
                image = "reset_email_Sakura.png"
                file_path = os.path.join('static', image)
                with open(file_path, mode='rb') as f:
                    img = MIMEImage(f.read())
                    img.add_header('Content-ID', '<{name}>'.format(name=image))
                    img.add_header('Content-Disposition', 'inline', filename=image)
                mail.attach(img)

                mail.send()
                return Response({"success" : "Email sent "} , status=status.HTTP_200_OK)

# first user request for give email  
class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = RequestPasswordResetEmailSerializer

    def post(self , request):

        serializer = self.serializer_class(request.data)
        try:
            email = request.data['email']
        except KeyError as e :
            raise CustomValidation('Incomplete information','error', status_code=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request).domain
            relativeLink = reverse('check_reset_token' , kwargs={"uidb64" : uidb64 , "token" : token})
            absurl = 'http://'+current_site+relativeLink

            message = get_template("email_reset_password.html").render({
                                    'username': user.username ,
                                    'date' : datetime.now(),
                                    'absurl' : absurl,
                                })
            mail = EmailMultiAlternatives(
                                "درخواست تغییر رمز",
                                message,
                                from_email="alfshop3@gmail.com",
                                to=[email],
                            )
            mail.mixed_subtype = 'related'
            # img for email :
            mail.attach_alternative(message, "text/html")
            image = "reset_email_Sakura.png"
            file_path = os.path.join('static', image)
            with open(file_path, mode='rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', '<{name}>'.format(name=image))
                img.add_header('Content-Disposition', 'inline', filename=image)
            mail.attach(img)

            mail.send()

        return Response({"success" : "Email sent "} , status=status.HTTP_200_OK)

# check token for reset password
class PasswordTokenCheck(generics.GenericAPIView):
    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64 ))
            user = User.objects.get(id =id )
            if not PasswordResetTokenGenerator().check_token(user , token):
                raise CustomValidation('token not vaid','error', status_code=status.HTTP_200_OK)

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
    serializer_class = Check_Confirm_Email_serializer
    def post(self, request):
        serializer =  self.serializer_class(request.data)
        try:
            token = request.data['token']
            pyload = jwt.decode(token,settings.SECRET_KEY)
            user = User.objects.get(id =pyload["user_id"] )

            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({"email":"email activated"} , status = status.HTTP_200_OK)

        except KeyError as e :
            raise CustomValidation('Incomplete information','error', status_code=status.HTTP_400_BAD_REQUEST)
        except jwt.ExpiredSignature as identifier:
            raise CustomValidation('activate expired','error', status_code=status.HTTP_200_OK)
        except jwt.exceptions.DecodeError as identifier:
            raise CustomValidation('token not vaid','error', status_code=status.HTTP_200_OK)


@api_view(('GET',))
def login_pic(request):
    img = detail.objects.all()[0].login_img
    return Response({"url":img.url} , status=status.HTTP_200_OK)

@api_view(('GET',))
def register_pic(request):
    img = detail.objects.all()[0].register_img
    return Response({"url":img.url} , status=status.HTTP_200_OK)

@api_view(('GET',))
def re_password_pic(request):
    img = detail.objects.all()[0].re_password_img
    return Response({"url":img.url} , status=status.HTTP_200_OK)

@api_view(('GET',))
@permission_classes([IsAuthenticated])
def username(request):
    user = request.user
    if user.first_name:
        return Response({"username":request.user.first_name} , status=status.HTTP_200_OK) 
    else:
        return Response({"username":request.user.username} , status=status.HTTP_200_OK) 