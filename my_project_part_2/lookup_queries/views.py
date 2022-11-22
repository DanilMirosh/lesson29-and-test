# TODO опишите view-функцию ниже
from rest_framework import viewsets

from lookup_queries.models import Store

from lookup_queries.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.filter(name__icontains="пят")
    serializer_class = StoreSerializer


