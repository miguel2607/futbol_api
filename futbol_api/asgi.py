import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chatbot.consumers import ChatConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'futbol_api.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/chat/<int:user_id>/", ChatConsumer.as_asgi()),
    ])
})
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'futbol_api.settings')
