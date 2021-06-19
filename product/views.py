from product.serializer import (
    product_group_serializer ,
    product_group_serializer2,
    product_serializer_helper_properties,
    product_similar_list_serializer,
    product_list_serializer,
    pack_list_serializer,
    product_serializer,
    )
from product import models
from rest_framework import status , generics , mixins
# override PageNumberPagination for product list :
from rest_framework.pagination import PageNumberPagination
from product.serializer import product_serializer_helper_properties, product_similar_list_serializer
from django.db.models import Q

class StandardResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
class search(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = models.product.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        query_name = self.kwargs.get('slug')
        print(query_name)
        return self.queryset.filter(slug__contains=query_name)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

# all group data
class group_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_group_serializer
    queryset = models.product_group.objects.all().order_by("-group")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class group_list2(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_group_serializer2
    queryset = models.product_group.objects.filter(group__isnull=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# all product list
class product_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = models.product.objects.all()
    pagination_class = StandardResultsSetPagination
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# top product (sell)
class top_product(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = models.product.objects.all().order_by('-sell')[0:9]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# best group one
class best_product(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    gro = models.product_group.objects.filter(group__isnull=True)
    if gro.count() >= 1 :
        queryset = models.product.objects.filter(group__group=gro[0])[0:9]
    else:
        queryset = models.product.objects.all().order_by('-sell')[0:9]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class similar_product(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_similar_list_serializer
    queryset = models.product.objects.all()

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        pd = models.product.objects.get(slug=slug)
        gp = pd.group.group
        return self.queryset.filter(~Q(slug = slug),group__group=gp).order_by("-sell")[0:9]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class pack_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = pack_list_serializer
    queryset = models.packs.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class product(generics.GenericAPIView , mixins.RetrieveModelMixin):
    serializer_class = product_serializer
    queryset = models.product.objects.all()
    lookup_field = 'slug'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class properties(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_serializer_helper_properties
    queryset = models.Properties.objects.all()

    def get_queryset(self):
        query_name = self.kwargs.get('slug')
        return self.queryset.filter(product__slug=query_name)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
