# TODO опишите view-функцию ниже
from rest_framework import viewsets
from fk_search.models import Store
from fk_search.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.filter(city__name='Самара')
