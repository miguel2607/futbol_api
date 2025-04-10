from django.urls import path
from productos.views import hombres_view, mujeres_view, ninos_view

urlpatterns = [

path('productos/hombres/', hombres_view),
    path('productos/mujeres/', mujeres_view),
    path('productos/ninos/', ninos_view),
]