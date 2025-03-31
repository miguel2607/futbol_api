from django.shortcuts import render

# Create your views here.
# chatbot/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chat_history(request, user_id):
    """
    Obtener el historial de conversaciones para un usuario específico
    """
    if request.user.id != user_id and not request.user.is_staff:
        return Response(
            {"error": "No tienes permiso para ver este historial"},
            status=status.HTTP_403_FORBIDDEN
        )

    conversations = Conversation.objects.filter(user_id=user_id)
    serializer = ConversationSerializer(conversations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def end_conversation(request, conversation_id):
    """
    Finalizar una conversación activa
    """
    try:
        conversation = Conversation.objects.get(id=conversation_id)
        if request.user != conversation.user and not request.user.is_staff:
            return Response(
                {"error": "No tienes permiso para finalizar esta conversación"},
                status=status.HTTP_403_FORBIDDEN
            )

        conversation.is_active = False
        conversation.save()
        return Response({"status": "Conversación finalizada"})
    except Conversation.DoesNotExist:
        return Response(
            {"error": "Conversación no encontrada"},
            status=status.HTTP_404_NOT_FOUND
        )