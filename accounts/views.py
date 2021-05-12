from rest_framework import generics, mixins
from .serializer import user_register 

class register_user(generics.GenericAPIView , mixins.CreateModelMixin):
    serializer_class = user_register
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
