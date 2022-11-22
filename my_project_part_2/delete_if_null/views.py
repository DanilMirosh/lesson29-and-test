# TODO опишите view-функцию ниже
from rest_framework import generics

from delete_if_null.models import Store
from delete_if_null.serializers import StoreSerializer


class StoreListView(generics.ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def get_queryset(self):
        Store.objects.filter(visits=0).delete()

        return super().get_queryset()
