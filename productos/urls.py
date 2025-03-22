from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JugadorViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JugadorViewSet, MercadoViewSet

router = DefaultRouter()
router.register(r'productos', JugadorViewSet)
router.register(r'mercado', MercadoViewSet, basename='mercado')

urlpatterns = [
    path('', include(router.urls)),
]
