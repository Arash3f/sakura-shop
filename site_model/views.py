from .serializer import site_model_serializer
from .models import Private_Site_Information
from rest_framework import generics, mixins, status
from rest_framework.response import Response

#  api for site detail { just get method}
class site_information(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = site_model_serializer
    queryset = Private_Site_Information.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # create site_ditaio (have jast 1 object)
    def post(self, request, *args, **kwargs):
        if Private_Site_Information.objects.all().count() >= 1 :
            text = "Cannot create a new object. Please modify or delete object 1"
            return Response({text},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return self.create(request, *args, **kwargs)
