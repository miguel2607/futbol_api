from django.db import models

# Create your models here.

from django.db import models

from django.db import models


class ProductoHombre(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.CharField(max_length=255, default="imagenes/default.jpg")  # Ejemplo: campo específico para hombres

class ProductoMujer(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.CharField(max_length=255, default="imagenes/default.jpg")  # Ejemplo: campo específico para mujeres

class ProductoNino(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.CharField(max_length=255, default="imagenes/default.jpg")  # Elimina el 'e' antes de imagen_url
