# chatbot/bot_logic.py
import ollama
import json

# Definimos información sobre el contexto del chatbot para Ollama
CONTEXT = """
Eres un chatbot oficial de Adidas Fútbol que ayuda a los usuarios con información sobre:
- Productos Adidas (botas, equipaciones, balones)
- Equipos patrocinados (Real Madrid, Manchester United, Bayern Múnich, etc.)
- Jugadores embajadores (Messi, Bellingham, Pedri, etc.)
- Tecnologías de los productos
- Ofertas y promociones
- Tiendas y compras
- Sostenibilidad e innovación

Debes ser profesional, amable y conocedor de todos los productos Adidas relacionados con fútbol.
"""


# Función para generar respuestas utilizando Ollama
def get_bot_response(message):
    """
    Genera respuestas utilizando el modelo de Ollama.
    Si hay algún problema con Ollama, utiliza respuestas de respaldo.
    """
    try:
        # Realizamos la llamada a Ollama
        response = ollama.chat(
            model="llama2",
            messages=[
                {
                    "role": "system",
                    "content": CONTEXT
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        # Extraemos la respuesta generada
        if response and 'message' in response and 'content' in response['message']:
            return response['message']['content']
        else:
            return get_fallback_response(message)
    except Exception as e:
        print(f"Error al conectar con Ollama: {e}")
        return get_fallback_response(message)


# Función de respaldo que utiliza algunas respuestas predefinidas
def get_fallback_response(message):
    """
    Proporciona respuestas de respaldo cuando Ollama no está disponible.
    """
    message = message.lower()

    # Algunas respuestas básicas de respaldo
    if any(word in message for word in ['hola', 'buenos días', 'buenas tardes', 'saludos']):
        return '¡Hola! Soy el asistente oficial de Adidas Fútbol. ¿En qué puedo ayudarte hoy?'

    if any(word in message for word in ['ayuda', 'asistencia']):
        return 'Puedo asistirte con información sobre productos Adidas, equipos patrocinados, jugadores embajadores, tecnologías de nuestros productos, ofertas especiales, y mucho más. ¿Qué te interesa?'

    if any(word in message for word in ['botas', 'calzado']):
        return 'Adidas ofrece cuatro líneas principales de botas de fútbol: Predator (control), X (velocidad), Copa (toque) y Nemeziz (agilidad). ¿Sobre cuál te gustaría más información?'

    if any(word in message for word in ['precio', 'costo', 'valor', 'cuánto cuesta']):
        return 'Los precios de nuestros productos varían según el modelo, tecnología y colección. Puedes consultar precios actualizados en nuestra web oficial o app de Adidas. ¿Te interesa algún producto específico?'

    if any(word in message for word in ['descuento', 'oferta', 'promoción']):
        return 'Actualmente tenemos ofertas especiales en equipaciones de temporadas anteriores y botas seleccionadas. Además, los miembros de adiClub reciben descuentos exclusivos. ¿Te gustaría más información?'

    # Respuesta por defecto
    return 'Entiendo que quieres información sobre productos Adidas relacionados con fútbol. Para ayudarte mejor, ¿podrías especificar si buscas información sobre equipaciones, botas, tecnologías, equipos patrocinados u otras categorías?'


# Función para guardar el historial de conversación para entrenamiento futuro
def log_conversation(user_message, bot_response):
    """
    Guarda las conversaciones para posible entrenamiento futuro del modelo.
    """
    try:
        with open('conversation_logs.jsonl', 'a', encoding='utf-8') as f:
            log_entry = {
                'user_message': user_message,
                'bot_response': bot_response,
                'timestamp': import_datetime_module().now().isoformat()
            }
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"Error al guardar conversación: {e}")


# Función auxiliar para importar datetime solo cuando se necesita
def import_datetime_module():
    import datetime
    return datetime