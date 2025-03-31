import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from chatbot.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'futbol_api.settings')
django.setup()  # 🔹 Importante para evitar errores de "Apps aren't loaded yet"

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        re_path(r"ws/chat/(?P<user_id>\d+)/$", ChatConsumer.as_asgi()),  # 🔹 Expresión regular correcta
    ]),
})
