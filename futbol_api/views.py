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


def ninos_view(request):
    # lógica de la vista
    return render(request, 'ninos.html')


# En tu archivo views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import json
from chatbot.models import Usuario  # Asumiendo que tienes un modelo Usuario


@ensure_csrf_cookie
def login_view(request):
    """Vista para mostrar la página de login"""
    return render(request, 'login.html')


@ensure_csrf_cookie
def registro_view(request):
    """Vista para mostrar la página de registro"""
    return render(request, 'registro.html')


@require_http_methods(["POST"])
def api_login(request):
    """API para procesar el login"""
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Validar que los campos no estén vacíos
        if not email or not password:
            return JsonResponse({'success': False, 'message': 'Por favor completa todos los campos'})

        # Buscar usuario en la base de datos
        try:
            usuario = Usuario.objects.get(email=email)

            # Verificar contraseña
            if check_password(password, usuario.password):
                # Actualizar la sesión
                request.session['usuario_id'] = usuario.id
                request.session['email'] = usuario.email

                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Contraseña incorrecta'})

        except Usuario.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El usuario no existe'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


@require_http_methods(["POST"])
def api_registro(request):
    """API para procesar el registro"""
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Validar que los campos no estén vacíos
        if not email or not password:
            return JsonResponse({'success': False, 'message': 'Por favor completa todos los campos'})

        # Verificar si el usuario ya existe
        if Usuario.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Este correo ya está registrado'})

        # Crear nuevo usuario
        nuevo_usuario = Usuario(
            email=email,
            password=make_password(password)  # Encriptar la contraseña
        )
        nuevo_usuario.save()

        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})