from django.db import models

# Create your models here.

from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    edad = models.IntegerField()
    equipo = models.CharField(max_length=100)
    en_venta = models.BooleanField(default=False)  # Nuevo campo
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Precio

    def __str__(self):
        return f"{self.nombre} - {self.equipo}"

class Transaccion(models.Model):
    comprador = models.CharField(max_length=100)
    vendedor = models.CharField(max_length=100)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jugador.nombre} comprado por {self.comprador}"


from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.URLField()

    def __str__(self):
        return self.nombre
