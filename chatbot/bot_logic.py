# chatbot/bot_logic.py

# Diccionario ampliado de respuestas para chatbot de API de Adidas
RESPUESTAS = {
    # Saludos y presentación
    'hola': '¡Hola! Soy el asistente oficial de Adidas Fútbol. ¿En qué puedo ayudarte hoy?',
    'buenos días': '¡Buenos días! Bienvenido al asistente virtual de Adidas Fútbol. ¿Cómo puedo asistirte?',
    'buenas tardes': '¡Buenas tardes! Estoy aquí para ayudarte con todo lo relacionado con Adidas y fútbol. ¿Qué necesitas?',
    'buenas noches': '¡Buenas noches! Gracias por contactar con el asistente de Adidas Fútbol. ¿En qué puedo ayudarte?',
    'ayuda': 'Puedo asistirte con información sobre productos Adidas, equipos patrocinados, jugadores embajadores, tecnologías de nuestros productos, ofertas especiales, y mucho más. ¿Qué te interesa?',

    # Productos Adidas
    'productos': 'Adidas ofrece una amplia gama de productos para fútbol, desde equipaciones oficiales hasta calzado especializado y accesorios. ¿Qué categoría te interesa explorar?',
    'novedades': 'Nuestras últimas novedades incluyen la colección Predator Edge, los nuevos X Speedportal y las equipaciones oficiales para la temporada 2025. ¿Te gustaría conocer alguna en detalle?',
    'exclusivos': 'Los productos exclusivos de Adidas incluyen ediciones limitadas de botas firmadas por estrellas como Messi, colecciones conmemorativas y productos personalizables mediante Adidas Creators Club.',

    # Calzado de fútbol
    'botas': 'Adidas ofrece cuatro líneas principales de botas de fútbol: Predator (control), X (velocidad), Copa (toque) y Nemeziz (agilidad). ¿Sobre cuál te gustaría más información?',
    'predator': 'Las Predator son nuestras botas diseñadas para el control del balón. El último modelo Predator Edge incorpora la tecnología Zone Skin para un control preciso y potencia en los disparos.',
    'x speedportal': 'Las X Speedportal están diseñadas para los jugadores más veloces. Incorporan la tecnología SPEEDFRAME para estabilidad y la suela SPEEDSKIN para máxima ligereza.',
    'copa': 'Las Copa son nuestras botas clásicas de piel, diseñadas para un toque exquisito. El modelo Copa Sense utiliza tecnología Sensepods para una conexión perfecta con el balón.',
    'nemeziz': 'Las Nemeziz están diseñadas para jugadores ágiles que necesitan flexibilidad. Utilizan un sistema de vendaje adaptativo inspirado en técnicas deportivas de vendaje.',
    'terreno': 'Ofrecemos botas para diferentes superficies: FG (terreno firme), AG (césped artificial), SG (terreno blando), IC (indoor/futsal) y TF (turf/multitáctil). ¿Qué superficie te interesa?',

    # Equipaciones y ropa
    'camisetas': 'Disponemos de camisetas oficiales de todos los equipos y selecciones patrocinados por Adidas, incluyendo ediciones home, away y third kit. ¿De qué equipo te interesa?',
    'equipaciones': 'Las equipaciones oficiales Adidas incluyen camiseta, pantalón y medias, fabricadas con tecnología AEROREADY para máxima comodidad y rendimiento durante el juego.',
    'entrenamiento': 'Nuestra ropa de entrenamiento incluye sudaderas, chaquetas, pantalones y equipaciones de entrenamiento con tecnología AEROREADY para mantenerte seco durante los entrenamientos.',
    'tallas': 'Disponemos de tallas desde XS hasta 3XL en adultos, y desde 4 años hasta 16 en niños. Cada producto incluye una guía de tallas específica que puedes consultar antes de comprar.',
    'personalizados': 'Puedes personalizar tus equipaciones con nombre y número en nuestra web oficial o en tiendas Adidas seleccionadas. El servicio tiene un coste adicional de 15€.',

    # Equipos patrocinados
    'equipos': 'Adidas patrocina a equipos de élite mundial como Real Madrid, Manchester United, Bayern Múnich, Juventus, Arsenal y muchas selecciones nacionales. ¿Sobre cuál quieres información?',
    'real madrid': 'El Real Madrid viste Adidas desde 1998. Su última equipación incorpora tecnología HEAT.RDY y un diseño que conmemora los éxitos del club en competiciones europeas.',
    'manchester united': 'El Manchester United y Adidas mantienen una colaboración histórica. Su equipación actual rinde homenaje al espíritu de los "Red Devils" con un diseño innovador.',
    'bayern': 'El Bayern Múnich luce equipación Adidas que incorpora los tradicionales colores bávaros con un diseño moderno que representa la filosofía del club.',
    'juventus': 'La Juventus viste Adidas con un diseño que reinterpreta las clásicas rayas blancas y negras, utilizando tecnología AEROREADY para máximo rendimiento.',
    'arsenal': 'El Arsenal presenta una equipación Adidas que combina tradición e innovación, con detalles que homenajean la historia del club londinense.',
    'alemania': 'La selección alemana viste Adidas desde hace décadas. Su equipación actual incorpora elementos de diseño que reflejan la identidad del fútbol alemán.',
    'españa': 'La selección española luce equipación Adidas con tecnología HEAT.RDY. El diseño se inspira en elementos gráficos históricos del fútbol español.',
    'argentina': 'La selección argentina, actual campeona del mundo, viste Adidas con un diseño que rinde tributo a su rica historia futbolística.',

    # Jugadores Adidas
    'jugadores': 'Adidas cuenta con embajadores de élite mundial como Lionel Messi, Jude Bellingham, Pedri, Toni Kroos, Vinícius Jr., y muchas estrellas más. ¿Sobre quién te gustaría saber?',
    'messi': 'Lionel Messi es nuestro embajador histórico. Utiliza un modelo especial de X Speedportal diseñado específicamente para su estilo de juego.',
    'bellingham': 'Jude Bellingham es una de nuestras jóvenes estrellas. Juega con las Predator Edge que potencian su capacidad de control y pase.',
    'pedri': 'Pedri representa la nueva generación de talentos Adidas. Utiliza las X Speedportal que complementan su agilidad y visión de juego.',
    'vinicius': 'Vinícius Jr. es uno de nuestros embajadores más dinámicos. Juega con las X Speedportal diseñadas para maximizar su velocidad.',
    'cristiano': 'Cristiano Ronaldo es un futbolista portugués considerado uno de los mejores jugadores de la historia. Nació el 5 de febrero de 1985 en Funchal, Madeira, Portugal. Se ha destacado por su capacidad goleadora, su velocidad, su habilidad técnica y su gran físico.',
    


    # Tecnologías Adidas
    'tecnologías': 'Adidas ha desarrollado tecnologías como HEAT.RDY, AEROREADY, PRIMEKNIT, BOOST y SPEEDFRAME para maximizar el rendimiento de los jugadores. ¿Sobre cuál quieres saber más?',
    'heat.rdy': 'HEAT.RDY es nuestra tecnología avanzada de gestión del calor que mantiene a los jugadores frescos en condiciones de alta temperatura y humedad.',
    'aeroready': 'AEROREADY absorbe la humedad y mantiene tu cuerpo seco durante el ejercicio, proporcionando una sensación de confort durante todo el partido.',
    'primeknit': 'PRIMEKNIT ofrece un ajuste sin costuras, proporcionando flexibilidad y soporte exactamente donde se necesita, reduciendo el peso total de la bota.',
    'boost': 'La tecnología BOOST proporciona un retorno de energía inigualable, ofreciendo mayor comodidad y capacidad de respuesta en cada paso.',
    'speedframe': 'SPEEDFRAME es nuestra tecnología para estabilizar el pie a altas velocidades, evitando lesiones y mejorando la aceleración del jugador.',

    # Colecciones especiales
    'colecciones': 'Adidas lanza colecciones especiales como "Numbering", "Teamgeist Revival", "Predator Legacy" y ediciones conmemorativas de Copas del Mundo. ¿Cuál te interesa?',
    'mundial': 'Para cada Copa del Mundo, Adidas lanza colecciones especiales que incluyen el balón oficial, equipaciones conmemorativas y botas en edición limitada.',
    'retro': 'Nuestra colección retro recupera diseños icónicos de equipaciones y botas históricas, adaptándolos a las tecnologías actuales.',
    'colaboraciones': 'Adidas colabora con diseñadores, artistas y marcas como Stella McCartney, Pharrell Williams y Parley for the Oceans en colecciones exclusivas.',

    # Balones
    'balones': 'Adidas es el proveedor oficial de balones para competiciones como la UEFA Champions League, la Copa del Mundo FIFA y múltiples ligas nacionales.',
    'al rihla': 'Al Rihla fue el balón oficial del Mundial 2022, diseñado con tecnología CRT-CORE para precisión y SPEEDSHELL para estabilidad aérea.',
    'champions': 'El balón oficial de la UEFA Champions League presenta un diseño estrellado icónico y tecnología térmica para detectar cuándo cruza la línea de gol.',
    'finale': 'La serie Finale representa a nuestros balones oficiales para competiciones de élite, fabricados con materiales sostenibles y máxima precisión.',

    # Compra y distribución
    'comprar': 'Puedes adquirir productos oficiales Adidas en nuestra web oficial, aplicación Adidas, tiendas físicas Adidas y distribuidores autorizados.',
    'tiendas': 'Encuentra tu tienda Adidas más cercana en nuestra web oficial. Las Adidas Flagship Stores ofrecen la gama más completa de productos de fútbol.',
    'envío': 'Ofrecemos envío gratuito para pedidos superiores a 50€. El tiempo de entrega estándar es de 3-5 días laborables, con opciones de envío express disponibles.',
    'devoluciones': 'Tienes 30 días para devolver tu compra sin coste adicional. Las devoluciones se pueden realizar online o en cualquier tienda física Adidas.',
    'descuentos': 'Únete a adiClub para acceder a descuentos exclusivos, ofertas anticipadas y promociones especiales para miembros. La inscripción es gratuita.',

    # Sostenibilidad
    'sostenibilidad': 'Adidas está comprometida con la sostenibilidad a través de nuestra iniciativa "End Plastic Waste". Muchos productos de fútbol utilizan materiales reciclados.',
    'reciclado': 'Nuestras camisetas Primeblue están fabricadas con plástico reciclado recuperado de océanos en colaboración con Parley for the Oceans.',
    'ecológico': 'Para 2025, el 90% de los productos Adidas utilizarán materiales sostenibles como parte de nuestro compromiso con el medio ambiente.',

    # Innovación
    'innovación': 'El centro de innovación Adidas desarrolla constantemente nuevas tecnologías para mejorar el rendimiento, la sostenibilidad y la experiencia del usuario.',
    'futuro': 'Estamos trabajando en botas inteligentes con sensores que proporcionan datos en tiempo real y materiales ultraligeros que optimizan el rendimiento.',
    'adidas lab': 'Adidas Lab es nuestro centro de investigación donde desarrollamos y probamos nuevas tecnologías con la ayuda de deportistas profesionales.',

    # Experiencias y comunidad
    'eventos': 'Adidas organiza eventos como Tango League, sesiones de entrenamiento con profesionales y pruebas de producto exclusivas para miembros de adiClub.',
    'comunidad': 'Únete a la comunidad Adidas Football a través de nuestras redes sociales y la app Adidas para conectar con otros aficionados y acceder a contenido exclusivo.',
    'app': 'La aplicación Adidas te permite comprar con facilidad, acceder a ofertas exclusivas, seguir tus entrenamientos y participar en desafíos de la comunidad.',

    # Tallas y ajuste
    'talla': 'Para encontrar tu talla ideal, consulta nuestra guía de tallas en la web. Recomendamos medir tu pie al final del día para mayor precisión.',
    'ajuste': 'Las botas Adidas tienen diferentes tipos de ajuste: regular, ajustado y muy ajustado. Consulta las especificaciones de cada modelo para elegir el adecuado.',
    'anchura': 'Ofrecemos modelos específicos para pies anchos, como la serie Copa que proporciona mayor comodidad y adaptabilidad.',

    # Mantenimiento
    'cuidado': 'Para prolongar la vida de tus productos Adidas, sigue las instrucciones de cuidado en la etiqueta. Las botas de fútbol deben limpiarse después de cada uso.',
    'limpieza': 'Limpia tus botas con agua tibia y un cepillo suave. Nunca las laves en lavadora ni las seques directamente al sol o cerca de fuentes de calor.',
    'durabilidad': 'La durabilidad de tus botas dependerá de la superficie de juego y la frecuencia de uso. Para uso intensivo, recomendamos alternar entre dos pares.',

    # Garantía y problemas
    'garantía': 'Todos los productos Adidas tienen una garantía de 2 años que cubre defectos de fabricación. Conserva el ticket de compra para posibles reclamaciones.',
    'defectos': 'Si detectas algún defecto en tu producto, contacta con nuestro servicio de atención al cliente a través de la web o visita una tienda Adidas.',
    'problemas': 'Para resolver cualquier problema con tu compra, visita la sección de Ayuda en nuestra web o contacta directamente con nuestro servicio de atención al cliente.',

    # Miscelánea
    'historia': 'Adidas fue fundada por Adolf "Adi" Dassler en 1949. Desde entonces, ha sido pionera en innovación para el fútbol, creando las primeras botas con tacos intercambiables.',
    'curiosidades': '¿Sabías que las icónicas tres bandas de Adidas se introdujeron inicialmente para dar estabilidad a las botas, y luego se convirtieron en el logo reconocible de la marca?',
    'contacto': 'Puedes contactar con nuestro servicio de atención al cliente a través de chat en vivo, email, teléfono o redes sociales. Estamos disponibles de lunes a domingo.',
    'adiclub': 'adiClub es nuestro programa de fidelización gratuito que te permite acumular puntos con cada compra y acceder a beneficios exclusivos según tu nivel.',
}


def get_bot_response(message):
    """
    Función mejorada para generar respuestas del bot basadas en palabras clave.
    Incluye procesamiento más sofisticado para detectar consultas complejas.
    """
    message = message.lower()

    # Verificar palabras clave exactas primero
    for key, response in RESPUESTAS.items():
        if key == message:
            return response

    # Verificar palabras clave dentro del mensaje
    matches = []
    for key, response in RESPUESTAS.items():
        if key in message:
            matches.append((key, response))

    # Si hay múltiples coincidencias, priorizar la más larga (más específica)
    if matches:
        matches.sort(key=lambda x: len(x[0]), reverse=True)
        return matches[0][1]

    # Categorías de consultas comunes para respuestas personalizadas
    if any(word in message for word in ['precio', 'costo', 'valor', 'cuánto cuesta', 'cuánto vale']):
        return 'Los precios de nuestros productos varían según el modelo, tecnología y colección. Puedes consultar precios actualizados en nuestra web oficial o app de Adidas. ¿Te interesa algún producto específico?'

    if any(word in message for word in ['descuento', 'oferta', 'promoción', 'rebaja']):
        return 'Actualmente tenemos ofertas especiales en equipaciones de temporadas anteriores y botas seleccionadas. Además, los miembros de adiClub reciben descuentos exclusivos. ¿Te gustaría más información?'

    if any(word in message for word in ['envío', 'entrega', 'recibir', 'enviar']):
        return 'Ofrecemos envío gratuito para pedidos superiores a 50€. El tiempo estimado de entrega es de 3-5 días laborables, con opción de entrega express por un coste adicional. ¿Necesitas información sobre envíos internacionales?'

    if any(word in message for word in ['comparar', 'diferencia', 'mejor', 'recomendar']):
        return 'Para ayudarte a elegir el mejor producto, necesitaría saber más sobre tus preferencias. ¿Qué posición juegas? ¿En qué tipo de superficie? ¿Tienes alguna preferencia de ajuste o tecnología?'

    if any(word in message for word in ['disponible', 'stock', 'agotado', 'reservar']):
        return 'La disponibilidad de productos varía según talla, modelo y ubicación. Te recomiendo consultar nuestra web oficial o app para verificar el stock en tiempo real. ¿Buscas algún producto específico?'

    # Respuestas sobre tecnologías específicas
    if 'tecnología' in message:
        if 'bota' in message or 'calzado' in message:
            return 'Nuestras botas incorporan tecnologías como PRIMEKNIT para ajuste, CONTROLFRAME para estabilidad, y AGILITYKNIT para flexibilidad. ¿Sobre cuál te gustaría saber más?'
        if 'camiseta' in message or 'equipación' in message:
            return 'Nuestras equipaciones utilizan tecnología HEAT.RDY para regular la temperatura y AEROREADY para gestionar la humedad durante el juego. ¿Quieres conocer más detalles?'
        if 'balón' in message:
            return 'Los balones Adidas incorporan tecnologías como CTR-CORE para precisión, SPEEDSHELL para estabilidad aerodinámica, y sensores térmicos en competiciones oficiales.'

    # Respuestas sobre eventos deportivos
    if any(word in message for word in ['mundial', 'champions', 'euro', 'competición', 'torneo']):
        return 'Adidas es patrocinador oficial de eventos como la Copa del Mundo FIFA, la UEFA Champions League y la Eurocopa. Lanzamos colecciones especiales para cada torneo. ¿Te interesa alguna competición en particular?'

    # Respuesta por defecto más elaborada
    return 'Entiendo que quieres información sobre productos Adidas relacionados con fútbol. Para ayudarte mejor, ¿podrías especificar si buscas información sobre equipaciones, botas, tecnologías, equipos patrocinados u otras categorías?'


# Función adicional para análisis más sofisticado del mensaje
def analyze_query_intent(message):
    """
    Analiza la intención de la consulta del usuario para ofrecer respuestas más precisas.
    Implementa un sistema básico de categorización de intenciones.
    """
    message = message.lower()

    # Categorías de intención
    intent = {
        'producto_info': 0,
        'compra': 0,
        'comparación': 0,
        'problema': 0,
        'opinión': 0,
        'equipo_info': 0,
        'tecnología_info': 0,
        'disponibilidad': 0
    }

    # Palabras clave por categoría
    producto_keywords = ['qué es', 'características', 'descripción', 'detalles', 'especificaciones']
    compra_keywords = ['comprar', 'adquirir', 'precio', 'pagar', 'envío', 'enviar', 'entrega']
    comparación_keywords = ['comparar', 'diferencia', 'mejor', 'peor', 'vs', 'versus', 'o']
    problema_keywords = ['problema', 'error', 'defecto', 'roto', 'dañado', 'devolver', 'garantía']
    opinión_keywords = ['recomendación', 'opinión', 'recomiendas', 'piensas', 'crees']
    equipo_keywords = ['equipo', 'club', 'selección', 'madrid', 'barça', 'bayern', 'united']
    tecnología_keywords = ['tecnología', 'innovación', 'material', 'tejido', 'suela', 'diseño']
    disponibilidad_keywords = ['disponible', 'stock', 'talla', 'color', 'cuándo', 'dónde']

    # Análisis básico de intención
    for word in producto_keywords:
        if word in message:
            intent['producto_info'] += 1

    for word in compra_keywords:
        if word in message:
            intent['compra'] += 1

    for word in comparación_keywords:
        if word in message:
            intent['comparación'] += 1

    for word in problema_keywords:
        if word in message:
            intent['problema'] += 1

    for word in opinión_keywords:
        if word in message:
            intent['opinión'] += 1

    for word in equipo_keywords:
        if word in message:
            intent['equipo_info'] += 1

    for word in tecnología_keywords:
        if word in message:
            intent['tecnología_info'] += 1

    for word in disponibilidad_keywords:
        if word in message:
            intent['disponibilidad'] += 1

    # Determinar la intención principal
    max_intent = max(intent.items(), key=lambda x: x[1])

    return max_intent[0] if max_intent[1] > 0 else 'general'


# Función para procesar consultas específicas sobre productos
def get_product_info(message):
    """
    Proporciona información detallada sobre productos específicos de Adidas.
    """
    message = message.lower()

    # Botas de fútbol
    if 'predator' in message:
        return {
            'nombre': 'Adidas Predator Edge',
            'descripción': 'Diseñadas para máximo control y precisión en los pases y disparos.',
            'tecnologías': ['Zone Skin', 'CONTROLFRAME', 'PRIMEKNIT'],
            'jugadores': ['Jude Bellingham', 'Paul Pogba', 'David Alaba'],
            'precio_aproximado': '250-280€',
            'superficies': ['FG', 'AG', 'SG', 'IC', 'TF']
        }

    if 'x speedportal' in message or 'speedportal' in message:
        return {
            'nombre': 'Adidas X Speedportal',
            'descripción': 'Diseñadas para velocidad extrema y aceleración explosiva.',
            'tecnologías': ['SPEEDFRAME', 'AGILITYKNIT', 'SPEEDSKIN'],
            'jugadores': ['Lionel Messi', 'Vinícius Jr.', 'Karim Benzema'],
            'precio_aproximado': '240-270€',
            'superficies': ['FG', 'AG', 'SG', 'IC', 'TF']
        }

    if 'copa' in message and ('bota' in message or 'calzado' in message):
        return {
            'nombre': 'Adidas Copa Sense',
            'descripción': 'Botas clásicas de piel para un toque exquisito y control del balón.',
            'tecnologías': ['Sensepods', 'Touchpods', 'Softstuds'],
            'jugadores': ['Paulo Dybala', 'João Félix', 'Manuel Neuer'],
            'precio_aproximado': '220-250€',
            'superficies': ['FG', 'AG', 'SG', 'IC', 'TF']
        }

    # Equipaciones
    equipos = {
        'real madrid': {
            'nombre': 'Equipación Real Madrid',
            'descripción': 'Equipación oficial del Real Madrid para la temporada actual.',
            'tecnologías': ['HEAT.RDY', 'AEROREADY'],
            'precio_aproximado': 'Camiseta 90-110€, Equipación completa 160-200€',
            'jugadores': ['Bellingham', 'Vinícius Jr.', 'Rodrygo']
        },
        'manchester united': {
            'nombre': 'Equipación Manchester United',
            'descripción': 'Equipación oficial del Manchester United para la temporada actual.',
            'tecnologías': ['HEAT.RDY', 'AEROREADY'],
            'precio_aproximado': 'Camiseta 90-110€, Equipación completa 160-200€',
            'jugadores': ['Bruno Fernandes', 'Marcus Rashford', 'Casemiro']
        },
        'bayern': {
            'nombre': 'Equipación Bayern Múnich',
            'descripción': 'Equipación oficial del Bayern Múnich para la temporada actual.',
            'tecnologías': ['HEAT.RDY', 'AEROREADY'],
            'precio_aproximado': 'Camiseta 90-110€, Equipación completa 160-200€',
            'jugadores': ['Harry Kane', 'Jamal Musiala', 'Alphonso Davies']
        },
        'alemania': {
            'nombre': 'Equipación Selección Alemana',
            'descripción': 'Equipación oficial de la selección de Alemania.',
            'tecnologías': ['HEAT.RDY', 'AEROREADY'],
            'precio_aproximado': 'Camiseta 90-110€, Equipación completa 160-200€',
            'jugadores': ['Toni Kroos', 'İlkay Gündoğan', 'Joshua Kimmich']
        }
    }

    for equipo, info in equipos.items():
        if equipo in message and ('camiseta' in message or 'equipación' in message):
            return info

    # Balones
    if 'balón' in message:
        if 'champions' in message:
            return {
                'nombre': 'Adidas Champions League Pro Ball',
                'descripción': 'Balón oficial de la UEFA Champions League, con el icónico diseño de estrellas.',
                'tecnologías': ['CTR-CORE', 'Thermosealing', 'Texturizado 3D'],
                'precio_aproximado': '140-160€',
                'competición': 'UEFA Champions League'
            }
        if 'mundial' in message:
            return {
                'nombre': 'Adidas Al Rihla / Al Hilm',
                'descripción': 'Balón oficial de la Copa del Mundo FIFA 2022 en Qatar.',
                'tecnologías': ['CTR-CORE', 'SPEEDSHELL', 'Texturizado 3D'],
                'precio_aproximado': '140-160€',
                'competición': 'FIFA World Cup 2022'
            }

    return None