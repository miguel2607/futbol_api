# chatbot/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Conversation, Message, OllamaConfig
from .ollama_service import OllamaService
import json
import time
import logging

logger = logging.getLogger(__name__)


@login_required
def chat_view(request):
    """
    Vista principal del chat
    """
    # Obtenemos la conversación activa o creamos una nueva
    conversation = Conversation.objects.filter(user=request.user, is_active=True).first()

    if not conversation:
        conversation = Conversation.objects.create(
            user=request.user,
            is_active=True,
            model_name="llama2",  # modelo por defecto
            context_used="Chatbot Adidas Fútbol"
        )

    # Obtenemos los modelos disponibles
    available_models = OllamaService.get_available_models()

    context = {
        'conversation': conversation,
        'messages': conversation.messages.all(),
        'available_models': available_models
    }

    return render(request, 'chatbot/chat.html', context)


@csrf_exempt
@login_required
def send_message(request):
    """
    Endpoint para enviar mensajes al chatbot
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            model_name = data.get('model', 'llama2')

            if not user_message:
                return JsonResponse({'error': 'El mensaje no puede estar vacío'}, status=400)

            # Obtenemos la conversación activa
            conversation = Conversation.objects.filter(user=request.user, is_active=True).first()

            if not conversation:
                conversation = Conversation.objects.create(
                    user=request.user,
                    is_active=True,
                    model_name=model_name
                )

            # Guardamos el mensaje del usuario
            Message.objects.create(
                conversation=conversation,
                content=user_message,
                sender='user'
            )

            # Obtenemos los últimos 5 mensajes para contexto
            recent_messages = conversation.get_last_messages(5)

            # Inicializamos el servicio de Ollama
            ollama_config = OllamaConfig.objects.filter(model_name=model_name, is_active=True).first()

            if ollama_config:
                ollama_service = OllamaService(
                    model_name=ollama_config.model_name,
                    temperature=ollama_config.temperature,
                    max_tokens=ollama_config.max_tokens
                )
            else:
                ollama_service = OllamaService(model_name=model_name)

            # Generamos la respuesta
            start_time = time.time()
            response = ollama_service.generate_response(user_message, recent_messages)
            processing_time = time.time() - start_time

            # Guardamos la respuesta del bot
            bot_message = Message.objects.create(
                conversation=conversation,
                content=response['content'],
                sender='bot',
                processed_by_ollama=response['success'],
                ollama_model_used=response['model_used'],
                processing_time=processing_time
            )

            return JsonResponse({
                'message': bot_message.content,
                'timestamp': bot_message.timestamp.strftime('%H:%M:%S'),
                'model_used': response['model_used'],
                'processing_time': round(processing_time, 2)
            })

        except Exception as e:
            logger.error(f"Error al procesar mensaje: {str(e)}")
            return JsonResponse({'error': f'Error al procesar mensaje: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@login_required
def end_conversation(request):
    """
    Finaliza la conversación actual y crea una nueva
    """
    if request.method == 'POST':
        Conversation.objects.filter(user=request.user, is_active=True).update(is_active=False)

        # Creamos una nueva conversación
        Conversation.objects.create(
            user=request.user,
            is_active=True,
            model_name="llama2"
        )

        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@login_required
def change_model(request):
    """
    Cambia el modelo utilizado en la conversación actual
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            model_name = data.get('model', 'llama2')

            conversation = Conversation.objects.filter(user=request.user, is_active=True).first()

            if conversation:
                conversation.model_name = model_name
                conversation.save()

                return JsonResponse({
                    'status': 'success',
                    'model': model_name
                })
            else:
                return JsonResponse({'error': 'No hay conversación activa'}, status=400)

        except Exception as e:
            logger.error(f"Error al cambiar modelo: {str(e)}")
            return JsonResponse({'error': f'Error al cambiar modelo: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)