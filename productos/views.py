from django.shortcuts import render
# productos/views.py
from django.http import JsonResponse
from .models import ProductoHombre, ProductoMujer, ProductoNino

def hombres_view(request):
    productos = list(ProductoHombre.objects.values())
    return JsonResponse(productos, safe=False)

def mujeres_view(request):
    productos = list(ProductoMujer.objects.values())
    return JsonResponse(productos, safe=False)

def ninos_view(request):
    productos = list(ProductoNino.objects.values())
    return JsonResponse(productos, safe=False)


def pago_tarjeta(request):
    return render(request,'PagoTarjeta.html')
def chatbot_page(request):
    return render(request, "chatbot.html")

###################################################################################################3
