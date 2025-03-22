from tempfile import template

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context



import os
from django.conf import settings
from django.http import HttpResponse

def miPrimera_pnatilla(request):
    # Construir la ruta absoluta correctamente
    ruta_plantilla = os.path.join(settings.BASE_DIR, "plantillas", "PrimeraPlantilla.html")

    try:
        with open(ruta_plantilla, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        return HttpResponse(contenido)
    except FileNotFoundError:
        return HttpResponse("Archivo no encontrado", status=404)




def home_view(request):
    return render(request, "PrimeraPlantilla.html")  # Asegúrate de que el archivo existe