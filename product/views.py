from .serializer import product_group_serializer , product_list_serializer
from .models import product_group , product
from rest_framework import status , generics , mixins


# override PageNumberPagination for product list :
from rest_framework.pagination import PageNumberPagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

# all group data
class group_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_group_serializer
    queryset = product_group.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# all product list
class product_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = product.objects.all()
    pagination_class = StandardResultsSetPagination
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# top product (sell)
class top_product(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# best group one
class best_product_one(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# best group two
class best_product_two(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


