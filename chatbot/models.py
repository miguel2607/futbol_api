from django.db import models

# Create your models here.
# chatbot/models.py
from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    started_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Conversación con {self.user.username} iniciada el {self.started_at.strftime('%d/%m/%Y')}"


class Message(models.Model):
    SENDER_CHOICES = (
        ('user', 'Usuario'),
        ('bot', 'Bot'),
    )

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_sender_display()} ({self.timestamp.strftime('%H:%M:%S')}): {self.content[:50]}"

    class Meta:
        ordering = ['timestamp']