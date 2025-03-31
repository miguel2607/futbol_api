# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/chat/history/<int:user_id>/', views.chat_history, name='chat_history'),
    path('api/chat/end/<int:conversation_id>/', views.end_conversation, name='end_conversation'),
]