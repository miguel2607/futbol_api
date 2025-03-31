import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'futbol_api.settings')

# Asegura que Django se inicializa antes de importar módulos que dependen de él
django.setup()

import chatbot.routing  # 🔄 Ahora lo importamos después de django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatbot.routing.websocket_urlpatterns
        )
    ),
})

