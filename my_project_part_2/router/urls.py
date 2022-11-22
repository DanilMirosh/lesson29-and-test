# TODO опишите здесь маршрутизацию с помощью класса SimpleRouter
from django.urls import path, include
from rest_framework import routers

from router import views

router = routers.SimpleRouter()
router.register('router_stores', views.StoreViewSet)

urlpatterns = [
    path('', include(router.urls))
]
