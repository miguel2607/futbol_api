from django.contrib import admin

# Register your models here.

from django.contrib import admin


from django.contrib import admin
from django.contrib.admin import AdminSite

from django.contrib import admin

admin.site.site_header = "Adidas Admin"
admin.site.site_title = "Adidas Admin Portal"
admin.site.index_title = "Bienvenido al portal de administración de Adidas"


from django.contrib import admin
from .models import ProductoHombre, ProductoMujer, ProductoNino

admin.site.register(ProductoHombre)
admin.site.register(ProductoMujer)
admin.site.register(ProductoNino)