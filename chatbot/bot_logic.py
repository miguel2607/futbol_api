# chatbot/bot_logic.py

# Diccionario simple de respuestas
RESPUESTAS = {
    'hola': '¡Hola! ¿En qué puedo ayudarte con respecto al fútbol?',
    'equipos': 'Tenemos información sobre varios equipos de fútbol. ¿De qué equipo quieres saber más?',
    'productos': 'Contamos con una variedad de productos relacionados con el fútbol. ¿Estás buscando algo específico?',
    'ayuda': 'Puedo ayudarte con información sobre equipos, jugadores, productos, o estadísticas. ¿Qué te interesa?',
}


def get_bot_response(message):
    """
    Función simple para generar respuestas del bot basadas en palabras clave.
    En un entorno de producción, podrías usar NLP o conectar con servicios como Dialogflow o GPT.
    """
    message = message.lower()

    # Verificar palabras clave
    for key, response in RESPUESTAS.items():
        if key in message:
            return response

    # Respuestas personalizadas para consultas específicas
    if 'precio' in message or 'costo' in message or 'valor' in message:
        return 'Los precios varían según el producto. ¿Te gustaría ver nuestro catálogo?'

    if 'liga' in message or 'torneo' in message or 'campeonato' in message:
        return 'Tenemos información actualizada sobre las principales ligas de fútbol. ¿Cuál te interesa?'

    # Respuesta por defecto
    return 'Lo siento, no entendí tu consulta. ¿Podrías reformularla o preguntar sobre equipos, jugadores o productos?'