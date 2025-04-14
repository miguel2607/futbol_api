from django.shortcuts import render
from .models import ProductoHombre, ProductoMujer, ProductoNino

def hombres_view(request):
    productos = ProductoHombre.objects.all()
    return render(request, 'hombres.html', {'productos': productos})

def mujeres_view(request):
    productos = ProductoMujer.objects.all()
    return render(request, 'mujeres.html', {'productos': productos})

def ninos_view(request):
    productos = ProductoNino.objects.all()
    return render(request, 'niños.html', {'productos': productos})



def pago_tarjeta(request):
    return render(request,'PagoTarjeta.html')
def chatbot_page(request):
    return render(request, "chatbot.html")

def pago_tarjeta(request):
    return render(request,'PagoTarjeta.html')
def chatbot_page(request):
    return render(request, "chatbot.html")

###################################################################################################3
