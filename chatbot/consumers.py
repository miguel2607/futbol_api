# chatbot/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Conversation, Message
from .bot_logic import get_bot_response


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_name = f"chat_{self.user_id}"
        self.room_group_name = f"chat_{self.user_id}"

        # Unir a la sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Iniciar o recuperar conversación existente
        conversation = await self.get_or_create_conversation()

        # Enviar mensaje de bienvenida
        await self.send(text_data=json.dumps({
            'message': '¡Hola! Soy el chatbot de Adidas. ¿En qué puedo ayudarte?',
            'sender': 'bot',
            'timestamp': self.get_timestamp()
        }))

    async def disconnect(self, close_code):
        # Salir de la sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Guardar mensaje del usuario
        await self.save_message(message, 'user')

        # Obtener respuesta del bot
        bot_response = await self.get_bot_response(message)

        # Guardar respuesta del bot
        await self.save_message(bot_response, 'bot')

        # Enviar respuesta al usuario
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': bot_response,
                'sender': 'bot',
                'timestamp': self.get_timestamp()
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        timestamp = event['timestamp']

        # Enviar mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'timestamp': timestamp
        }))

    @database_sync_to_async
    def get_or_create_conversation(self):
        user, _ = User.objects.get_or_create(id=self.user_id)
        conversation, created = Conversation.objects.get_or_create(
            user=user,
            is_active=True
        )
        return conversation

    @database_sync_to_async
    def save_message(self, content, sender):
        conversation = Conversation.objects.get(user__id=self.user_id, is_active=True)
        Message.objects.create(
            conversation=conversation,
            content=content,
            sender=sender
        )

    @database_sync_to_async
    def get_bot_response(self, user_message):
        # Puedes conectar aquí con un servicio externo o implementar tu propia lógica
        return get_bot_response(user_message)

    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")