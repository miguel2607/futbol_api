from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    started_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    model_name = models.CharField(max_length=50, default="llama3")
    context_used = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Conversación con {self.user.username} iniciada el {self.started_at.strftime('%d/%m/%Y')}"

    def get_last_messages(self, count=5):
        """
        Obtiene los últimos mensajes para proporcionar contexto a Ollama
        """
        return self.messages.order_by('-timestamp')[:count]


class Message(models.Model):
    SENDER_CHOICES = (
        ('user', 'Usuario'),
        ('bot', 'Bot'),
    )

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    # Campos adicionales para tracking de la integración con Ollama
    processed_by_ollama = models.BooleanField(default=False)
    ollama_model_used = models.CharField(max_length=50, blank=True, null=True)
    processing_time = models.FloatField(blank=True, null=True)  # tiempo en segundos

    def __str__(self):
        return f"{self.get_sender_display()} ({self.timestamp.strftime('%H:%M:%S')}): {self.content[:50]}"

    class Meta:
        ordering = ['timestamp']


class Usuario(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Para almacenar contraseña encriptada
    fecha_registro = models.DateTimeField(auto_now_add=True)

    # Preferencias para el chatbot
    preferred_model = models.CharField(max_length=50, default="llama3")
    conversation_history_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class OllamaConfig(models.Model):
    """
    Configuración para la integración con Ollama
    """
    model_name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    temperature = models.FloatField(default=0.7)
    max_tokens = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model_name} ({'Activo' if self.is_active else 'Inactivo'})"