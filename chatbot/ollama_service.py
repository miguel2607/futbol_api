# chatbot/ollama_service.py
import ollama
import time
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class OllamaService:
    """
    Servicio para manejar las interacciones con Ollama
    """

    def __init__(self, model_name="llama2", temperature=0.7, max_tokens=1000):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate_response(self, prompt, conversation_history=None):
        """
        Genera una respuesta usando Ollama

        Args:
            prompt (str): El mensaje del usuario
            conversation_history (list): Lista de mensajes anteriores

        Returns:
            dict: Respuesta con el texto generado y metadatos
        """
        start_time = time.time()

        messages = []

        # Añadir el contexto del sistema
        messages.append({
            "role": "system",
            "content": """
            Eres un chatbot oficial de Adidas Fútbol que ayuda a los usuarios con información sobre:
            - Productos Adidas (botas, equipaciones, balones)
            - Equipos patrocinados (Real Madrid, Manchester United, Bayern Múnich, etc.)
            - Jugadores embajadores (Messi, Bellingham, Pedri, etc.)
            - Tecnologías de los productos
            - Ofertas y promociones
            - Tiendas y compras
            - Sostenibilidad e innovación

            Debes ser profesional, amable y conocedor de todos los productos Adidas relacionados con fútbol.
            Respuestas Rapidas y cortas.
            """
        })

        # Añadir histórico de conversación si existe
        if conversation_history:
            for msg in conversation_history:
                role = "user" if msg.sender == "user" else "assistant"
                messages.append({
                    "role": role,
                    "content": msg.content
                })

        # Añadir el mensaje actual del usuario
        messages.append({
            "role": "user",
            "content": prompt
        })

        try:
            # Llamada a la API de Ollama
            response = ollama.chat(
                model=self.model_name,
                messages=messages,
                options={
                    "temperature": self.temperature,
                    "num_predict": self.max_tokens,
                }
            )

            processing_time = time.time() - start_time

            result = {
                "content": response['message']['content'] if 'message' in response and 'content' in response[
                    'message'] else "Lo siento, no pude generar una respuesta.",
                "model_used": self.model_name,
                "processing_time": processing_time,
                "success": True
            }

            return result

        except Exception as e:
            logger.error(f"Error en la llamada a Ollama: {str(e)}")

            return {
                "content": "Lo siento, estoy experimentando problemas técnicos. Por favor, inténtalo de nuevo más tarde.",
                "model_used": None,
                "processing_time": time.time() - start_time,
                "success": False,
                "error": str(e)
            }

    @staticmethod
    def get_available_models():
        """
        Obtiene la lista de modelos disponibles en Ollama

        Returns:
            list: Lista de modelos disponibles
        """
        try:
            models = ollama.list()
            return [model['name'] for model in models['models']] if 'models' in models else []
        except Exception as e:
            logger.error(f"Error al obtener modelos disponibles: {str(e)}")
            return []