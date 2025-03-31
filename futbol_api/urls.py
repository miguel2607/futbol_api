"""
URL configuration for futbol_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from futbol_api.views import miPrimera_pnatilla, home_view
from productos.views import hombres_view  # ✔ Importa desde la app correcta
from productos.views import mujeres_view
from productos.views import niños_views
from productos.views import pago_tarjeta

urlpatterns = [
    path('admin/', admin.site.urls),


    path("hombres/", hombres_view, name="hombres"),
    path("inicio", home_view, name="home"),
    path("mujeres",mujeres_view, name="mujeres"),
    path("niños",niños_views,name="niños"),
    path("tarjeta_credito", pago_tarjeta, name="tarjeta"),

]
