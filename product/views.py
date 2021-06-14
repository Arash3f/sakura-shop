from .serializer import product_list_serializer , pack_list_serializer , product_serializer
from .serializer import (
    product_group_serializer ,
    product_group_serializer2,
    )
from .models import product , packs
from .models import product_group
from product import models
from rest_framework import status , generics , mixins

# override PageNumberPagination for product list :
from rest_framework.pagination import PageNumberPagination
from product.serializer import product_similar_list_serializer
class StandardResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

# all group data
class group_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_group_serializer
    queryset = product_group.objects.all().order_by("-group")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class group_list2(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_group_serializer2
    queryset = product_group.objects.filter(group__isnull=True)

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
    queryset = product.objects.all().order_by('-sell')[0:9]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# best group one
class best_product(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    gro = product_group.objects.filter(group__isnull=True)
    if gro.count() >= 1 :
        queryset = product.objects.filter(group__group=gro[0])[0:9]
    else:
        queryset = product.objects.all().order_by('-sell')[0:9]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class similar_product(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_similar_list_serializer
    queryset = product.objects.all()

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        pd = models.product.objects.get(slug=slug)
        gp = pd.group.group
        return self.queryset.filter(group__group=gp).order_by("-sell")[0:9]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class pack_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = pack_list_serializer
    queryset = packs.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class product(generics.GenericAPIView , mixins.RetrieveModelMixin):
    serializer_class = product_serializer
    queryset = product.objects.all()
    lookup_field = 'slug'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


