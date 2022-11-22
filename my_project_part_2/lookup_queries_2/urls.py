# TODO здесь необходимо настроить urls приложения
from django.urls import include, path
from rest_framework import routers

from lookup_queries_2 import views

simple_router = routers.SimpleRouter()
simple_router.register('lookup_queries_2', views.StoreViewSet)

urlpatterns = [
    path('', include(simple_router.urls))
]
