# TODO опишите view-функцию ниже
from faker.providers import address
from rest_framework import viewsets

from lookup_queries_2.models import Store

from lookup_queries_2.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.filter(address__endswith="д. 30")
    serializer_class = StoreSerializer
