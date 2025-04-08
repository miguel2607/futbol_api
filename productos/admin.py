from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Producto

admin.site.register(Producto)

from django.contrib import admin
from django.contrib.admin import AdminSite

from django.contrib import admin

admin.site.site_header = "Adidas Admin"
admin.site.site_title = "Adidas Admin Portal"
admin.site.index_title = "Bienvenido al portal de administración de Adidas"