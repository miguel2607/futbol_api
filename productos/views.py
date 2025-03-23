from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Jugador, Transaccion
from .serializers import JugadorSerializer, TransaccionSerializer
from django.shortcuts import render
class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class MercadoViewSet(viewsets.ViewSet):
    """
    ViewSet para gestionar la compra y venta de productos.
    """

    @action(detail=False, methods=['get'])
    def jugadores(self, request):
        """Listar productos en venta"""
        jugadores_en_venta = Jugador.objects.filter(en_venta=True)
        serializer = JugadorSerializer(jugadores_en_venta, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def comprar(self, request):
        """Comprar un jugador"""
        jugador_id = request.data.get('jugador_id')
        comprador = request.data.get('comprador')

        try:
            jugador = Jugador.objects.get(id=jugador_id, en_venta=True)
            transaccion = Transaccion.objects.create(
                comprador=comprador,
                vendedor=jugador.equipo,
                jugador=jugador,
                precio=jugador.precio
            )
            # Actualizar el equipo del jugador y quitarlo del mercado
            jugador.equipo = comprador
            jugador.en_venta = False
            jugador.precio = None
            jugador.save()

            return Response({'mensaje': 'Jugador comprado con éxito'}, status=status.HTTP_200_OK)
        except Jugador.DoesNotExist:
            return Response({'error': 'Jugador no disponible'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def transacciones(self, request):
        """Obtener historial de transacciones"""
        transacciones = Transaccion.objects.all()
        serializer = TransaccionSerializer(transacciones, many=True)
        return Response(serializer.data)




def hombres_view(request):
    return render(request, 'hombres.html')  # Incluye la app si es necesario

def mujeres_view(request):
    return render(request, 'mujeres.html')

def niños_views(request):
    return render(request,'niños.html')
def pago_tarjeta(request):
    return render(request,'PagoTarjeta.html')

