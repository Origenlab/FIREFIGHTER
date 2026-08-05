# -*- coding: utf-8 -*-
"""L4 — SKOLD HERO · barrera exterior Kombat Flex.

Patron "ficha sin ficha". Angulo propio: EL NOMBRE COMERCIAL NO ACREDITA DESEMPENO.
Aporta el protocolo de campo con el que si se mide la movilidad de un traje, que es
contenido que ningun competidor esta dando. No se le atribuye ninguna cifra al producto.
"""
import json, io, collections, os, re

RUTA = 'src/data/productos.json'
SLUG = 'skold-hero-kombat-flex'
VARIANTE = 'Kombat Flex'

L4 = collections.OrderedDict([
  ("seoTitle", "Traje SKÖLD HERÖ con barrera Kombat Flex"),
  ("seoDescription",
    "Barrera exterior Kombat Flex del SKÖLD HERÖ: qué documenta el fabricante, qué no, y el "
    "protocolo con el que sí se mide la movilidad de un traje estructural."),
  ("badge", "Alcance por confirmar"),
  ("h1", "Traje estructural SKÖLD HERÖ con barrera exterior Kombat Flex"),
  ("subtitulo",
    "Kombat Flex es una de las cinco barreras exteriores seleccionables del conjunto HERÖ. El "
    "nombre sugiere flexibilidad, pero el fabricante no publica composición, gramaje ni ensayo "
    "que lo respalde: aquí está lo que sí se puede exigir y cómo comprobar la movilidad con la "
    "prenda en la mano."),

  ("heroImg", {
    "src": "/images/catalogo/1705503831904-600x450.webp",
    "alt": "Detalle de cintas reflejantes y lámpara de intervención sobre un traje estructural",
  }),
  ("heroBloques", [
    {
      "label": "Un nombre no es un ensayo",
      "texto": (
        "“Flex” es una promesa comercial, y en protección estructural las promesas se verifican o "
        "no valen. SKÖLD lista <strong>Kombat Flex</strong> entre las barreras exteriores del "
        "HERÖ, pero la ficha del modelo <strong>no publica composición, gramaje ni ningún ensayo "
        "de flexibilidad</strong> para esa configuración. No vamos a repetir el nombre como si "
        "fuera un dato: preferimos explicarte cómo se mide la movilidad de verdad."
      ),
    },
    {
      "label": "Lo que sí puedes comprobar tú mismo",
      "texto": (
        "La movilidad de un traje se comprueba con el elemento vestido, no en un catálogo. En esta "
        "ficha está el <strong>protocolo de cinco pruebas</strong> que aplicamos en una demo: "
        "traslape con brazos arriba, gateo, montar escalera, alcance con guante y vestido "
        "cronometrado. Traemos prenda de muestra y <strong>juego de tallas</strong> antes de que "
        "cierres cualquier pedido de brigada, con cobertura en los <strong>32 estados</strong>."
      ),
    },
  ]),
  ("heroDatos", [
    {"label": "Estado del dato", "valor": "Ficha por solicitar"},
    {"label": "Ensayo de flexibilidad", "valor": "No publicado"},
    {"label": "Certificación del modelo", "valor": "UL · expediente MH60435"},
  ]),
  ("specStrip", [
    {"label": "Capa exterior", "valor": "Kombat Flex · sin gramaje publicado"},
    {"label": "Flexibilidad", "valor": "Sin ensayo declarado"},
    {"label": "Barreras interiores", "valor": "Por confirmar en la ficha"},
    {"label": "Conjunto", "valor": "HERÖ · DRD, cuello 360°, Kevlar"},
    {"label": "Movilidad verificable", "valor": "Protocolo de 5 pruebas en demo"},
    {"label": "Certificación", "valor": "UL MH60435 · alcance por confirmar"},
  ]),

  ("secciones", [
    {
      "id": "que-es",
      "eyebrow": "Qué estás evaluando",
      "titulo": "Kombat Flex es una capa exterior del HERÖ, no otro traje",
      "parrafos": [
        "El <strong>SKÖLD HERÖ</strong> admite cinco barreras exteriores: Advance, Kombat Flex, "
        "PBI MAX 7.0, Pioneer y Defender 750. Cambiar de barrera no cambia el conjunto —el DRD "
        "sigue en la espalda, el cuello sigue siendo el de cobertura 360° y el arnés sigue siendo "
        "de Kevlar—, cambia la capa que toca el fuego, que recibe la abrasión y que define cuánto "
        "pesa y cómo cae la prenda.",
        "De las cinco, esta es la que trae el nombre más sugestivo y la que menos respaldo público "
        "tiene. Eso no la descalifica: la obliga a demostrarse. Y como la variable en juego es "
        "movilidad —algo que sí se puede sentir con la prenda puesta—, es una de las pocas "
        "configuraciones donde una demo bien hecha vale más que una ficha.",
      ],
      "nota": "En la partida tiene que aparecer <strong>la configuración de barreras</strong>, no solo el modelo. Dos propuestas pueden decir “SKÖLD HERÖ” y entregar trajes que no pesan ni caen igual.",
    },
    {
      "id": "que-es-flexibilidad",
      "eyebrow": "Autoridad técnica",
      "titulo": "Qué significaría “flex” si estuviera medido",
      "parrafos": [
        "En ropa de protección estructural la movilidad no es una propiedad única ni la aporta la "
        "tela sola. Se construye —y se puede medir— en cuatro frentes distintos, y un nombre "
        "comercial no dice nada de ninguno de los cuatro.",
      ],
      "lista": [
        {"t": "Gramaje y mano de la tela", "d": "El peso por yarda cuadrada y la rigidez del tejido. Una capa exterior más ligera y de mano más suave se dobla con menos esfuerzo del elemento. Es el dato que ordena todo lo demás, y es justo el que no está publicado."},
        {"t": "Peso total del ensamble", "d": "La movilidad percibida depende de las tres capas juntas, no solo del exterior. Un exterior ligero con barrera térmica gruesa puede resultar más pesado que la combinación contraria."},
        {"t": "Corte y patronaje", "d": "Corte tipo diamante en la entrepierna, sisas amplias, largo de manga y traslape entre chaquetón y pantalón. Aquí sí hay datos del modelo, y son los que producen la mayor parte de la ganancia real de movimiento."},
        {"t": "Interfaces", "d": "Puño con ojillo para pulgar, tirantes con conexión rápida, sujeción del cuello. Un traje flexible con interfaces mal resueltas se siente rígido igual."},
      ],
      "nota": "Cuando un proveedor te ofrezca “mayor flexibilidad”, pregúntale <strong>en cuál de esos cuatro frentes</strong> y con qué dato lo sostiene. Si no puede responder, está vendiendo un adjetivo.",
    },
    {
      "id": "lo-documentado",
      "eyebrow": "Lo que sí está documentado",
      "titulo": "El conjunto: aquí está la movilidad que SKÖLD sí publica",
      "parrafos": [
        "Estos elementos son a nivel de modelo, así que aplican también con Kombat Flex, y varios "
        "de ellos son precisamente los que producen ganancia de movimiento. Son los que puedes "
        "exigir por escrito y verificar contra la prenda cuando llegue.",
      ],
      "lista": [
        {"t": "Corte tipo diamante", "d": "En la entrepierna del pantalón. Amplía el rango al subir, gatear y montar escalera; es la mejora de movilidad más tangible del conjunto."},
        {"t": "Puño de Kevlar con ojillo para pulgar", "d": "Mantiene la manga en posición al levantar el brazo, así el traslape con el guante no se pierde en pleno movimiento."},
        {"t": "Tirantes acolchados con conexión rápida", "d": "Y ajuste elástico posterior en el pantalón. Permiten vestirse en la unidad en movimiento y sostienen el pantalón sin apretar la cintura."},
        {"t": "Refuerzos Stedshield y Ultrashield", "d": "En mangas, hombros, codos y rodillas del chaquetón, y Stedshield en los tobillos: exactamente las zonas de flexión y arrastre."},
        {"t": "DRD integrado", "d": "Drag Rescue Device en la espalda del chaquetón, alojado dentro de la prenda y no como accesorio externo que estorbe."},
        {"t": "Cuello tipo escudo 360°", "d": "Cobertura total sin partes expuestas. Su comportamiento real depende del ajuste y de la interfaz con capucha y casco."},
        {"t": "Tallas S a 4X", "d": "En chaquetón, pantalón o traje completo, cada presentación con clave propia. La tabla de medidas UL del exterior se publica para S a 3XL."},
      ],
    },
    {
      "id": "lo-no-publicado",
      "eyebrow": "Lo que falta",
      "titulo": "Los datos ausentes y qué decide cada uno en movilidad",
      "parrafos": [
        "Esta tabla es el mapa de lo que hay que resolver antes de firmar, y sirve igual para "
        "evaluar a cualquier proveedor que te ofrezca esta configuración.",
      ],
      "tabla": {
        "head": ["Dato ausente", "Qué decide", "Consecuencia de no tenerlo"],
        "rows": [
          ["Gramaje en oz/yd²", "Peso del ensamble y esfuerzo de doblado", "No se puede estimar la fatiga del elemento ni comparar contra PBI MAX 7.0"],
          ["Composición de la tela", "Rigidez, abrasión y comportamiento ante llama", "No se anticipa cómo cae la prenda ni cómo responde al desgarre"],
          ["Ensayo de flexibilidad", "Si “Flex” es una propiedad medida o un nombre", "La afirmación no se puede sostener en un anexo técnico ni en una aclaración de bases"],
          ["Barrera de humedad", "Paso de vapor sobrecalentado y transpirabilidad", "Es la capa que produce la mayoría de las quemaduras por escaldadura dentro de un traje certificado"],
          ["Barrera térmica", "Tiempo de tolerancia térmica y volumen del conjunto", "Sin ella no hay TPP del ensamble, y es la que más suma rigidez percibida"],
          ["TPP y THL del ensamble", "Protección térmica y evacuación de calor metabólico", "El THL bajo saca al elemento por fatiga antes de que el fuego lo toque"],
        ],
      },
      "nota": "Un traje puede ser excelente y no tener ficha pública: la ausencia del dato no es un defecto del producto. Lo que no se puede hacer es <strong>rellenarlo con supuestos</strong> y presentarlo como especificación en una requisición.",
    },
    {
      "id": "protocolo",
      "eyebrow": "Cómo se comprueba",
      "titulo": "Protocolo de cinco pruebas para medir movilidad en una demo",
      "parrafos": [
        "Esto es lo que hacemos en una demostración y lo que puedes exigirle a cualquier proveedor "
        "antes de comprometer un presupuesto. Se corre con el elemento vestido con las capas que "
        "usará en operación —capucha, casco, guantes, botas y equipo de respiración— porque un "
        "traje probado sobre camiseta miente.",
      ],
      "lista": [
        {"t": "1 · Traslape con brazos arriba", "d": "El elemento levanta los brazos por encima de la cabeza. El chaquetón no debe subir tanto que se pierda el traslape mínimo con el pantalón. Es la prueba que reprueban los trajes dos tallas grandes."},
        {"t": "2 · Gateo con carga", "d": "Recorrido en cuatro puntos con línea o herramienta. Se observa si el refuerzo de rodilla cae donde apoya y si el pantalón se enrolla en el tobillo."},
        {"t": "3 · Montar escalera", "d": "Tres o cuatro peldaños. Aquí se siente el corte tipo diamante: si la entrepierna limita el paso, el problema es patronaje, no tela."},
        {"t": "4 · Alcance con guante", "d": "Extender el brazo y sujetar una herramienta. Se verifica que el puño mantenga posición y que la manga y el guante sigan traslapados en extensión completa."},
        {"t": "5 · Vestido cronometrado", "d": "De rack a listo. Mide lo que suman en la práctica el cierre de escape, los tirantes con conexión rápida y la sujeción del cuello."},
      ],
      "nota": "Corre el protocolo con <strong>al menos dos tallas y dos complexiones distintas</strong>, incluyendo corte para mujer si tu cuerpo lo requiere. Una prueba con un solo elemento mide el ajuste de ese elemento, no el del traje.",
    },
    {
      "id": "certificacion",
      "eyebrow": "Certificación",
      "titulo": "El expediente es del modelo; el alcance se confirma por configuración",
      "parrafos": [
        "SKÖLD publica para el HERÖ certificación por laboratorio <strong>UL bajo NFPA 1971 "
        "edición 2018</strong>, con expediente <strong>MH60435</strong>. Es certificación de "
        "tercera parte, rastreable en UL Product iQ, y eso ya la distingue de una declaración de "
        "conformidad del propio fabricante.",
        "Lo que hay que precisar es el alcance. La certificación se emite sobre el ensamble, y la "
        "configuración documentada en la ficha que conocemos es la de PBI MAX 7.0. Pide por "
        "escrito que el fabricante declare si el expediente cubre la combinación con Kombat Flex "
        "y bajo qué edición normativa.",
      ],
      "nota": "NFPA 1971 fue consolidada en <strong>NFPA 1970 (1971) edición 2025</strong> y la transición cerró el 18 de marzo de 2026: un certificado emitido hoy debe referirse a la edición vigente. El inventario ya etiquetado no se invalida —se rige por NFPA 1850 (1851)—, pero en la compra hay que precisar qué edición ampara el documento.",
    },
    {
      "id": "anexo",
      "eyebrow": "Licitación",
      "titulo": "Cómo pedir movilidad en una partida sin escribir un adjetivo",
      "parrafos": [
        "“Traje flexible” no es especificable ni evaluable: cualquier proveedor puede jurar que "
        "cumple. Estas son las formas de pedir lo mismo de manera comparable y auditable.",
      ],
      "tabla": {
        "head": ["En la partida escribe", "En lugar de"],
        "rows": [
          ["Pantalón con corte tipo diamante en entrepierna", "“Pantalón de movimiento amplio”"],
          ["Puño con ojillo para pulgar y traslape verificable con guante en extensión completa", "“Puño ergonómico”"],
          ["Tirantes acolchados con conexión rápida y ajuste elástico posterior", "“Sujeción cómoda”"],
          ["Gramaje de la capa exterior declarado en oz/yd² por el fabricante en ficha técnica", "“Barrera exterior Kombat Flex ligera”"],
          ["Demostración con prenda de muestra y protocolo de movilidad como requisito de evaluación", "sin mención"],
          ["TPP y THL del ensamble armado, declarados por el fabricante", "sin mención"],
        ],
      },
      "nota": "Redactada así, la partida se evalúa con <strong>documento y prueba</strong>, no con opiniones sobre telas. Quien no pueda entregar la ficha ni presentar prenda queda fuera por incumplimiento, no por discusión técnica.",
    },
    {
      "id": "cuando-conviene",
      "eyebrow": "Criterio de selección",
      "titulo": "Cuándo tiene sentido evaluar Kombat Flex",
      "parrafos": [
        "No descartamos una barrera por no tener ficha pública, y tampoco la recomendamos a "
        "ciegas. Estos son los escenarios donde vale la pena pedir la ficha y la demo, y el "
        "escenario donde conviene ir a la configuración documentada.",
      ],
      "lista": [
        {"t": "Tiene sentido evaluarla", "d": "Cuando la movilidad es una queja real de tu personal y puedes correr una demo con protocolo antes de decidir. Ahí la prueba de campo pesa más que la ficha."},
        {"t": "Tiene sentido evaluarla", "d": "Cuando ya operas HERÖ y quieres comparar variantes manteniendo modelo, claves y procedimiento de cuidado."},
        {"t": "Tiene sentido evaluarla", "d": "Cuando tu operación tiene alta frecuencia de rescate vehicular o espacios confinados, donde el rango de movimiento se cobra en cada salida."},
        {"t": "Conviene ir a PBI MAX 7.0", "d": "Cuando la compra es por licitación con anexo técnico cerrado y necesitas cifras verificables desde el primer día. La configuración documentada te ahorra la impugnación."},
      ],
    },
    {
      "id": "siguiente-paso",
      "eyebrow": "Qué hacemos nosotros",
      "titulo": "De un nombre comercial a una prueba con testigos",
      "parrafos": [
        "Solicitamos al fabricante la ficha de la configuración con composición, gramaje, barreras "
        "interiores, valores de TPP y THL del ensamble armado y el alcance del certificado. En "
        "paralelo organizamos la demo con prenda de muestra y corremos el protocolo con tu "
        "personal, para que la decisión tenga documento y experiencia y no solo una de las dos.",
        "Si la ficha no llega o llega incompleta, te lo decimos y comparamos contra PBI MAX 7.0 "
        "con lo que sí está publicado. Antes de cerrar un pedido de brigada enviamos "
        "<strong>juego de tallas de muestra</strong>: la tabla UL describe la prenda extendida, no "
        "el cuerpo del elemento.",
      ],
      "nota": "Cada envío sale con certificado del ensamble, número de serie y fecha de fabricación por prenda, etiqueta permanente con la composición de las tres capas, procedimiento de lavado y retiro en español, carta de distribuidor autorizado y factura desglosada por partida y talla.",
    },
  ]),

  ("galeria", [
    {"src": "/images/catalogo/1690210795620-600x450.webp",
     "alt": "Bombero con guantes de intervención sujetando una herramienta de mango largo",
     "caption": "Alcance con guante en extensión"},
    {"src": "/images/catalogo/1563062067-9d-600x450.webp",
     "alt": "Bombero abriendo una puerta metálica con guantes de intervención",
     "caption": "Rango de movimiento en maniobra"},
    {"src": "/images/catalogo/1690210795713-600x450.webp",
     "alt": "Dos bomberos con casco y visera durante una operación",
     "caption": "El conjunto completo en operación"},
    {"src": "/images/catalogo/1666518809220-600x400.webp",
     "alt": "Manos con guantes de intervención sujetando equipo de bombero",
     "caption": "Interfaz manga y guante"},
  ]),

  ("aplicaciones", [
    {"sector": "Cuerpos de bomberos",
     "desc": "Cuando la movilidad es una queja documentada de tu personal y puedes correr una demo con protocolo antes de decidir. La barrera se define con ficha y prueba, no en la orden de compra."},
    {"sector": "Rescate y espacios confinados",
     "desc": "Operaciones con alta frecuencia de gateo, arrastre y trabajo en posiciones forzadas, donde el rango de movimiento se cobra en cada salida y conviene probar antes de comprar volumen."},
    {"sector": "Licitación pública",
     "desc": "Exige la ficha de la configuración y la demostración con prenda de muestra como requisitos de evaluación. Si el proceso no admite esperarlas, la configuración documentada evita la impugnación."},
  ]),

  ("datoClave", {
    "titulo": "“Flex” no es un valor de ensayo",
    "texto": "Ningún organismo certifica “flexibilidad” en un traje estructural. Lo que sí se mide es <strong>gramaje, peso del ensamble y THL</strong>, y lo que sí se comprueba es el rango de movimiento con la prenda puesta. Pide los tres primeros por escrito y el cuarto en demo."
  }),

  ("referencias", [
    {"code": "UL · MH60435", "desc": "Expediente de certificación del HERÖ publicado por SKÖLD. Rastreable en UL Product iQ. Hay que confirmar si su alcance cubre la configuración Kombat Flex."},
    {"code": "NFPA 1971 · 2018", "desc": "Edición bajo la que está declarada la certificación UL del modelo. Fue sustituida."},
    {"code": "NFPA 1970 · 2025", "desc": "Estándar vigente que consolidó NFPA 1971, 1975, 1981 y 1982. Establece los mínimos de TPP y THL del ensamble."},
    {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento del conjunto en servicio. Rige la permanencia del inventario, no la edición de certificación."},
    {"code": "NOM-017-STPS", "desc": "Selección, entrega y capacitación en el uso del equipo de protección personal según el riesgo del puesto."},
  ]),

  ("blog", [
    "guia-trajes-estructurales-nfpa-1971",
    "equipar-brigada-trajes-bomberos-tallaje-licitacion",
    "marcas-trajes-bomberos-comparativa-mexico",
    "rescate-vehicular-tecnicas-equipos",
    "nfpa-1971-mexico-norma-bomberos",
    "mantenimiento-epp-estructural-nfpa-1851",
  ]),

  ("faqs", [
    {"q": "¿“Kombat Flex” significa que el traje es más flexible?",
     "a": "Significa que así se llama la tela. El fabricante no publica composición, gramaje ni ningún ensayo de flexibilidad para esta configuración, y ningún organismo certifica “flexibilidad” en un traje estructural. Lo que sí existe son datos que se relacionan con la movilidad —gramaje de la capa exterior, peso del ensamble armado y THL— y una comprobación práctica con la prenda puesta. Pedimos los datos al fabricante y organizamos la comprobación; lo que no hacemos es repetir el nombre como si fuera un resultado."},
    {"q": "¿Cómo mido la movilidad de un traje antes de comprar?",
     "a": "Con el elemento vestido con todas las capas que usará en operación, incluida capucha, casco, guantes, botas y equipo de respiración. En esta ficha está el protocolo de cinco pruebas que usamos: traslape con brazos arriba, gateo con carga, montar escalera, alcance con guante y vestido cronometrado. Córrelo con al menos dos tallas y dos complexiones distintas; una prueba con un solo elemento mide el ajuste de ese elemento, no el del traje."},
    {"q": "¿Qué aporta más movilidad, la tela o el corte?",
     "a": "En la práctica, el corte y las interfaces. El corte tipo diamante en la entrepierna, las sisas, el largo de manga, el puño con ojillo para pulgar y los tirantes con conexión rápida producen la mayor parte de la ganancia real de movimiento, y esos elementos sí están documentados a nivel de modelo. La tela influye por gramaje y mano, pero un exterior ligero con mal patronaje se siente rígido igual."},
    {"q": "¿Entonces Kombat Flex es peor que PBI MAX 7.0?",
     "a": "No hay base para afirmarlo, ni tampoco lo contrario. La diferencia verificable hoy es de información: de las cinco barreras del HERÖ solo PBI MAX publica composición y gramaje. Una barrera puede ser excelente y no tener ficha pública. Lo que no se puede es compararlas técnicamente mientras falten composición, gramaje, barreras interiores y los valores de TPP y THL del ensamble armado."},
    {"q": "¿Puedo comprar el HERÖ con Kombat Flex de todas formas?",
     "a": "Sí, es una configuración que el fabricante ofrece y la cotizamos. Antes solicitamos la ficha de la configuración y, si la movilidad es tu criterio de decisión, organizamos la demo con prenda de muestra. Si tu proceso no admite esperar la respuesta del fabricante, te lo decimos y evaluamos ir a PBI MAX 7.0, que ya está documentada."},
    {"q": "¿Qué sí puedo exigir por escrito si elijo Kombat Flex?",
     "a": "Todo lo que SKÖLD publica a nivel de modelo: DRD integrado en la espalda, cuello de cobertura 360° sin partes expuestas, arnés de Kevlar integrado, refuerzos Stedshield y Ultrashield en mangas, hombros, codos, rodillas y tobillos, costura de Kevlar doble y triple, puño de Kevlar con ojillo para pulgar, cinta ORALITE Ultra Brilliance serie FTP2575-S de 3″, corte tipo diamante, tirantes con conexión rápida, tallas de S a 4X y las claves por presentación."},
    {"q": "¿El expediente UL MH60435 cubre la configuración Kombat Flex?",
     "a": "Es lo que hay que confirmar por escrito. El expediente es del modelo HERÖ y la configuración documentada en la ficha que conocemos es la de PBI MAX 7.0. La certificación se emite sobre el ensamble completo, así que la existencia del expediente no acredita automáticamente cualquier combinación de las cinco barreras. Pedimos al fabricante que declare alcance y edición normativa aplicables a la configuración cotizada."},
    {"q": "¿Cuánto tardan en organizar una demo y en cotizar?",
     "a": "La cotización sale en menos de 24 horas hábiles con lo que está publicado y con el estado de cada dato pendiente marcado como tal. La demo depende de disponibilidad de prenda de muestra en la talla que necesitas y te damos fecha comprometida al confirmarla. El tiempo de respuesta del fabricante para la ficha no lo controlamos, así que no te prometemos un plazo: te decimos cuándo la solicitamos y te avisamos en cuanto llega."},
  ]),
])


with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')
card = next(c for c in prod['l3']['catalogo']['cards'] if c['variante'] == VARIANTE)

card['slug'] = SLUG
card['l4'] = L4

orden = ['marca', 'modelo', 'variante', 'varianteLabel', 'slug', 'badge', 'estado',
         'img', 'alt', 'desc', 'specs', 'chip', 'l4']
nuevo = collections.OrderedDict((k, card[k]) for k in orden if k in card)
for k, v in card.items():
    if k not in nuevo:
        nuevo[k] = v
card.clear(); card.update(nuevo)

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

srcs = [L4['heroImg']['src']] + [g['src'] for g in L4['galeria']]
faltan = [s for s in srcs if not os.path.exists('public' + s)]
palabras = 0
for s in L4['secciones']:
    for p in s.get('parrafos', []): palabras += len(re.sub(r'<[^>]+>', '', p).split())
    for it in s.get('lista', []): palabras += len(re.sub(r'<[^>]+>', '', it['d']).split())
    for r in s.get('tabla', {}).get('rows', []): palabras += sum(len(c.split()) for c in r)
    if s.get('nota'): palabras += len(re.sub(r'<[^>]+>', '', s['nota']).split())
for f_ in L4['faqs']: palabras += len(f_['a'].split())

print(SLUG, '| secciones:', len(L4['secciones']), '| faqs:', len(L4['faqs']))
print('  seoTitle:', len(L4['seoTitle']) + 21, 'ch | seoDescription:', len(L4['seoDescription']), 'ch')
print('  imagenes distintas:', len(set(srcs)), 'de', len(srcs), '| faltantes:', faltan or 'ninguna')
print('  palabras:', palabras)
