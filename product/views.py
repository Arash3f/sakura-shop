from product.serializer import (
    product_group_serializer ,
    product_list_serializer,
    pack_list_serializer,
    product_serializer,
    )
from product import models
from rest_framework import generics , mixins
from django.db.models import Q

# Pagination :
# override PageNumberPagination for product list :
from rest_framework.pagination import PageNumberPagination
class Standard_Results_Set_Pagination(PageNumberPagination):
    page_size_query_param = 'page_size'

# all product list :
class product_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = models.product.objects.all()
    pagination_class = Standard_Results_Set_Pagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# top product (sort by sell field)
class top_product(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = models.product.objects.all().order_by('-sell')[0:9]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# best product (sort by group [0])
class best_product(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    group = models.product_group.objects.filter(group__isnull=True)
    if group.count() >= 1 :
        queryset = models.product.objects.filter(group__group=group[0])[0:9]
    # not have any group yet .
    else:
        queryset = models.product.objects.all().order_by('-sell')[0:9]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# product page :
class product_page(generics.GenericAPIView , mixins.RetrieveModelMixin):
    serializer_class = product_serializer
    queryset = models.product.objects.all()
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# similar product :
class similar_product(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = models.product.objects.all()

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        pd = models.product.objects.get(slug=slug)
        gp = pd.group.group
        return self.queryset.filter(~Q(slug = slug),group__group=gp).order_by("-sell")[0:9]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# search product :
class product_search(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_list_serializer
    queryset = models.product.objects.all()
    pagination_class = Standard_Results_Set_Pagination

    def get_queryset(self):
        query_name = self.kwargs.get('slug')
        return self.queryset.filter(slug__contains=query_name)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# pack : 
class pack_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = pack_list_serializer
    queryset = models.Packs.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# group :
class group_list(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = product_group_serializer
    queryset = models.product_group.objects.all().order_by("-group")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)