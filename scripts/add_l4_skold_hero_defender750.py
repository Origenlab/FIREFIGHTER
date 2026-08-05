# -*- coding: utf-8 -*-
"""L4 — SKOLD HERO · barrera exterior Defender 750.

Patron "ficha sin ficha". Angulo propio: NOMBRES QUE SE PARECEN Y NO SON LO MISMO.
Defender 750 es capa EXTERIOR; Defender M es la barrera TERMICA de la configuracion PBI MAX.
Aporta un mapa de nomenclatura de EPP estructural, que es el error de requisicion mas comun.
"""
import json, io, collections, os, re

RUTA = 'src/data/productos.json'
SLUG = 'skold-hero-defender-750'
VARIANTE = 'Defender 750'

L4 = collections.OrderedDict([
  ("seoTitle", "Traje SKÖLD HERÖ con barrera Defender 750"),
  ("seoDescription",
    "Barrera exterior Defender 750 del SKÖLD HERÖ: por qué no es Defender M, qué documenta el "
    "fabricante y cómo evitar el error de nombre en una requisición."),
  ("badge", "Alcance por confirmar"),
  ("h1", "Traje estructural SKÖLD HERÖ con barrera exterior Defender 750"),
  ("subtitulo",
    "Defender 750 es una de las cinco barreras exteriores seleccionables del conjunto HERÖ. Se "
    "confunde con Defender M, que es la barrera térmica de la configuración PBI MAX: son capas "
    "distintas del ensamble y pedir una creyendo pedir la otra cambia el traje que llega."),

  ("heroImg", {
    "src": "/images/catalogo/1563062067-bb-600x450.webp",
    "alt": "Bombero de perfil con ensamble estructural completo y equipo de respiración",
  }),
  ("heroBloques", [
    {
      "label": "Dos nombres parecidos, dos capas distintas",
      "texto": (
        "<strong>Defender 750</strong> es una capa <strong>exterior</strong>. "
        "<strong>Defender M</strong> es la barrera <strong>térmica</strong> de la configuración "
        "PBI MAX 7.0. No son alternativas entre sí: viven en posiciones diferentes del mismo "
        "ensamble. Pedir “Defender” sin más es la clase de ambigüedad que se resuelve en la "
        "entrega y no en la requisición, cuando ya no se puede corregir sin costo."
      ),
    },
    {
      "label": "Escribimos la partida contigo antes de cotizar",
      "texto": (
        "Antes de mandarte un precio revisamos que la partida nombre <strong>capa por capa</strong> "
        "y no por familia comercial, y solicitamos al fabricante la ficha de la configuración con "
        "composición, gramaje y el alcance del certificado. Cuesta media hora y evita una "
        "aclaración de bases. Cobertura en los <strong>32 estados de la República</strong> con "
        "propuesta en menos de <strong>24 horas hábiles</strong>."
      ),
    },
  ]),
  ("heroDatos", [
    {"label": "Posición en el ensamble", "valor": "Capa exterior"},
    {"label": "No confundir con", "valor": "Defender M · barrera térmica"},
    {"label": "Estado del dato", "valor": "Ficha por solicitar"},
  ]),
  ("specStrip", [
    {"label": "Capa exterior", "valor": "Defender 750 · sin gramaje publicado"},
    {"label": "No es", "valor": "Defender M (barrera térmica)"},
    {"label": "Barrera de humedad", "valor": "Por confirmar en la ficha"},
    {"label": "Barrera térmica", "valor": "Por confirmar en la ficha"},
    {"label": "Conjunto", "valor": "HERÖ · DRD, cuello 360°, Kevlar"},
    {"label": "Certificación", "valor": "UL MH60435 · alcance por confirmar"},
  ]),

  ("secciones", [
    {
      "id": "que-es",
      "eyebrow": "Qué estás evaluando",
      "titulo": "Defender 750 es una capa exterior del HERÖ",
      "parrafos": [
        "El <strong>SKÖLD HERÖ</strong> admite cinco barreras exteriores: Advance, Kombat Flex, "
        "PBI MAX 7.0, Pioneer y Defender 750. El conjunto no cambia —DRD en la espalda, cuello de "
        "cobertura 360°, arnés de Kevlar, refuerzos y claves de producto son los del modelo—; lo "
        "que cambia es la capa que recibe la llama y la abrasión.",
        "Esta configuración tiene un problema adicional que no es técnico sino de nombre, y que en "
        "la práctica genera más errores de compra que cualquier discusión sobre telas. Lo "
        "abordamos primero porque es lo que más dinero cuesta cuando se pasa por alto.",
      ],
      "nota": "En la partida tiene que aparecer <strong>la configuración de barreras completa</strong>, no solo el modelo ni la familia comercial. “SKÖLD HERÖ Defender” no describe un ensamble.",
    },
    {
      "id": "no-es-defender-m",
      "eyebrow": "El error que cuesta",
      "titulo": "Defender 750 no es Defender M",
      "parrafos": [
        "Comparten familia de nombre y nada más. <strong>Defender 750</strong> es una de las "
        "barreras <strong>exteriores</strong> seleccionables del HERÖ. <strong>Defender M</strong> "
        "es la <strong>barrera térmica</strong> que el fabricante documenta en la configuración "
        "PBI MAX 7.0, es decir la capa interior que define el tiempo de tolerancia térmica.",
        "El error típico se ve así: una requisición pide “barrera Defender” pensando en la "
        "térmica documentada, el proveedor entrega la configuración con capa exterior Defender 750, "
        "y ninguno de los dos está mintiendo. La ambigüedad estaba en el papel. Y como la "
        "certificación se emite sobre el ensamble armado, el traje que llegó es un ensamble "
        "distinto del que se creyó comprar.",
      ],
      "tabla": {
        "head": ["Capa del ensamble", "Función", "En la configuración PBI MAX 7.0", "En esta configuración"],
        "rows": [
          ["Exterior", "Resiste llama directa, abrasión y desgarre; lleva las cintas reflejantes", "PBI MAX 7 oz · 70 % PBI, 30 % Kevlar", "Defender 750 · sin composición ni gramaje publicados"],
          ["Barrera de humedad", "Impide el paso de agua y vapor sobrecalentado sin bloquear la salida del sudor", "Stedair 3000", "Por confirmar en la ficha"],
          ["Barrera térmica", "Define el tiempo real de tolerancia térmica", "Defender M", "Por confirmar en la ficha"],
        ],
      },
      "nota": "Si en tu expediente aparece “Defender” a secas, corrígelo antes de la entrega: escribe <strong>“capa exterior: …” y “barrera térmica: …”</strong> en renglones separados. Es la corrección más barata de todo el proceso de compra.",
    },
    {
      "id": "mapa-nombres",
      "eyebrow": "Autoridad técnica",
      "titulo": "Mapa de nombres que se confunden en EPP estructural",
      "parrafos": [
        "Defender 750 y Defender M no son el único par problemático. Estas confusiones aparecen en "
        "requisiciones, en bases de licitación y en propuestas todo el tiempo, y cada una cambia "
        "lo que se compra o lo que se puede exigir.",
      ],
      "lista": [
        {"t": "NFPA 1971 vs NFPA 1970", "d": "1971 era el estándar de conjuntos estructurales. 1970 es el vigente y consolidó 1971, 1975, 1981 y 1982. Citar 1971 en unas bases nuevas obliga a aclarar edición; citar 1970 sin año deja abierto qué se exige."},
        {"t": "NFPA 1851 vs NFPA 1850", "d": "1851 regía selección, cuidado y mantenimiento del conjunto. Quedó consolidada en 1850, que además cubre equipo de respiración. Es la norma del inventario en servicio, no la de certificación."},
        {"t": "Nomex vs Nomex IIIA", "d": "Nomex es la familia de meta-aramida. Nomex IIIA es una mezcla específica con fibra antiestática. Pedir “Nomex” no especifica cuál ni en qué gramaje."},
        {"t": "PBI vs PBI Matrix vs PBI MAX", "d": "PBI es la fibra. PBI Matrix y PBI MAX son construcciones de tela distintas, con mezclas y gramajes propios. “Traje de PBI” no dice cuál de las tres."},
        {"t": "Stedair vs Stedshield", "d": "Stedair es una familia de barreras de humedad —Stedair 3000 en la configuración documentada—. Stedshield es material de refuerzo en zonas de desgaste. Nombres parecidos, funciones opuestas."},
        {"t": "TPP vs THL", "d": "TPP mide protección térmica; THL mide cuánto calor metabólico evacua el traje. Van en direcciones contrarias: subir uno baja el otro. Pedir solo TPP produce trajes que cansan al elemento."},
      ],
      "nota": "Regla práctica: en un anexo técnico, <strong>ningún nombre comercial debe aparecer sin su función y su posición en el ensamble</strong>. “Barrera térmica: Defender M” es especificable. “Defender” no lo es.",
    },
    {
      "id": "lo-documentado",
      "eyebrow": "Lo que sí está documentado",
      "titulo": "El conjunto: esto no depende de la barrera exterior",
      "parrafos": [
        "Estos elementos los publica SKÖLD a nivel de modelo, así que aplican también con "
        "Defender 750. Son los que puedes especificar por escrito y verificar contra la prenda "
        "física cuando llegue.",
      ],
      "lista": [
        {"t": "DRD integrado", "d": "Drag Rescue Device alojado en la espalda del chaquetón, para extraer a un elemento inconsciente desde un punto diseñado para eso."},
        {"t": "Cuello tipo escudo 360°", "d": "Cobertura total alrededor del cuello sin partes expuestas. Su desempeño real depende del ajuste y de la interfaz con capucha y casco."},
        {"t": "Arnés de Kevlar integrado", "d": "Incorporado a la prenda, no accesorio externo."},
        {"t": "Refuerzos Stedshield y Ultrashield", "d": "En mangas, hombros, codos y rodillas del chaquetón, y Stedshield en los tobillos del pantalón. Refuerzo, no barrera: otro nombre que conviene no mezclar."},
        {"t": "Costura de Kevlar doble y triple", "d": "Hilo aramídico en todo el conjunto, con puño de Kevlar y ojillo para pulgar."},
        {"t": "Cinta ORALITE® FTP2575-S de 3″", "d": "Ultra Brilliance™ en amarillo verdoso fluorescente, más bies reflejante plata. Especificada por serie, que es justo lo contrario de un nombre ambiguo."},
        {"t": "Claves y tallas", "d": "Chaquetón CHB910, pantalón PB910 y traje completo TB910, en tallas de S a 4X. Las claves incluyen “2018” porque identifican la edición normativa certificada."},
      ],
      "nota": "Fíjate en el detalle de las claves: el propio fabricante mete la <strong>edición normativa dentro del código de producto</strong>. Ese es el nivel de precisión al que conviene llegar en la requisición.",
    },
    {
      "id": "lo-no-publicado",
      "eyebrow": "Lo que falta",
      "titulo": "Los datos ausentes de esta configuración",
      "parrafos": [
        "Resuelta la ambigüedad de nombre, queda el vacío de información. Esta tabla es el mapa de "
        "lo que hay que pedir antes de firmar.",
      ],
      "tabla": {
        "head": ["Dato ausente", "Qué decide", "Consecuencia de no tenerlo"],
        "rows": [
          ["Composición de Defender 750", "Comportamiento ante llama y resistencia mecánica", "No se anticipa si carboniza conservando estructura ni cómo responde al desgarre"],
          ["Gramaje en oz/yd²", "Peso del ensamble y carga térmica", "No hay forma de comparar fatiga del elemento contra PBI MAX 7.0"],
          ["Barrera de humedad de la configuración", "Paso de vapor sobrecalentado", "No se sabe si es Stedair 3000 u otra: es una de las tres capas del ensamble"],
          ["Barrera térmica de la configuración", "Tiempo real de tolerancia térmica", "Aquí es donde la confusión de nombres se vuelve un vacío real de dato"],
          ["TPP y THL del ensamble", "Los dos valores que exige la norma", "Sin ellos no hay base técnica para aceptar ni rechazar la propuesta"],
          ["Alcance del certificado", "Si el expediente ampara esta combinación", "El expediente puede existir y no cubrir la configuración entregada"],
        ],
      },
      "nota": "Un traje puede ser excelente y no tener ficha pública: la ausencia del dato no es un defecto del producto, es un vacío de información. Lo que no se puede hacer es <strong>rellenarlo con supuestos</strong> y presentarlo como especificación.",
    },
    {
      "id": "certificacion",
      "eyebrow": "Certificación",
      "titulo": "El expediente es del modelo; el alcance se confirma por configuración",
      "parrafos": [
        "SKÖLD publica para el HERÖ certificación por laboratorio <strong>UL bajo NFPA 1971 "
        "edición 2018</strong>, con expediente <strong>MH60435</strong>. Es certificación de "
        "tercera parte y se puede rastrear en UL Product iQ, lo que ya la distingue de una "
        "declaración de conformidad del propio fabricante.",
        "Como la certificación se emite sobre el ensamble de tres capas, y aquí dos de las tres "
        "están sin declarar, el alcance para esta configuración es precisamente lo que hay que "
        "pedir por escrito. No es un trámite: es la diferencia entre un expediente que resiste una "
        "auditoría y uno que no.",
      ],
      "nota": "NFPA 1971 fue consolidada en <strong>NFPA 1970 (1971) edición 2025</strong> y la transición cerró el 18 de marzo de 2026: un certificado emitido hoy debe referirse a la edición vigente. El inventario ya etiquetado no se invalida —se rige por NFPA 1850 (1851)—, pero en la compra hay que precisar qué edición ampara el documento.",
    },
    {
      "id": "anexo",
      "eyebrow": "Licitación",
      "titulo": "Cómo redactar la partida sin ambigüedad de nombres",
      "parrafos": [
        "Estas redacciones eliminan el margen de interpretación. Son las mismas que usamos cuando "
        "un cliente nos pide revisar sus bases antes de publicarlas.",
      ],
      "tabla": {
        "head": ["En la partida escribe", "En lugar de"],
        "rows": [
          ["Capa exterior: nombre comercial, composición con porcentajes y gramaje en oz/yd²", "“Barrera Defender”"],
          ["Barrera de humedad: nombre comercial y tipo de membrana", "sin mención"],
          ["Barrera térmica: nombre comercial", "“Barrera térmica de alto desempeño”"],
          ["TPP y THL del ensamble armado, declarados por el fabricante", "sin mención"],
          ["Certificado de tercera parte con expediente, organismo emisor y edición normativa vigente", "“Cumple NFPA”"],
          ["Clave de producto por presentación y talla, tal como la publica el fabricante", "“Talla L”"],
        ],
      },
      "nota": "Tres renglones —una línea por capa— convierten una partida discutible en una partida <strong>evaluable</strong>. Quien no pueda llenarlos queda fuera por incumplimiento documental, no por criterio.",
    },
    {
      "id": "cuando-conviene",
      "eyebrow": "Criterio de selección",
      "titulo": "Cuándo tiene sentido evaluar Defender 750",
      "parrafos": [
        "No descartamos una barrera por no tener ficha pública, y tampoco la recomendamos a "
        "ciegas. Estos son los escenarios donde vale la pena pedir la ficha, y el escenario donde "
        "conviene ir directo a la configuración documentada.",
      ],
      "lista": [
        {"t": "Tiene sentido evaluarla", "d": "Cuando el fabricante puede entregar la ficha de la configuración —las tres capas, no solo la exterior— dentro del plazo de tu proceso."},
        {"t": "Tiene sentido evaluarla", "d": "Cuando ya operas HERÖ y buscas alternativas de costo o disponibilidad manteniendo modelo, claves y programa de cuidado."},
        {"t": "Tiene sentido evaluarla", "d": "Cuando tus bases especifican por conjunto y dejan la configuración de barreras abierta a propuesta con ficha respaldatoria."},
        {"t": "Conviene ir a PBI MAX 7.0", "d": "Cuando la compra va a auditoría o a licitación con anexo cerrado. Con dos de las tres capas sin declarar, el expediente queda expuesto."},
      ],
    },
    {
      "id": "siguiente-paso",
      "eyebrow": "Qué hacemos nosotros",
      "titulo": "Primero la partida, después el precio",
      "parrafos": [
        "Revisamos tu requisición o tus bases para que cada capa aparezca nombrada con su función y "
        "su posición en el ensamble, y solicitamos al fabricante la ficha de la configuración con "
        "composición, gramaje, barreras interiores, valores de TPP y THL del ensamble armado y la "
        "declaración de alcance del certificado.",
        "Si la ficha no llega o llega incompleta, te lo decimos y comparamos contra PBI MAX 7.0 con "
        "lo que sí está publicado. Antes de cerrar un pedido de brigada enviamos <strong>juego de "
        "tallas de muestra</strong>: la tabla de medidas UL describe la prenda extendida, no el "
        "cuerpo del elemento.",
      ],
      "nota": "Cada envío sale con certificado del ensamble, número de serie y fecha de fabricación por prenda, etiqueta permanente con la composición de las tres capas, procedimiento de lavado y retiro en español, carta de distribuidor autorizado y factura desglosada por partida y talla.",
    },
  ]),

  ("galeria", [
    {"src": "/images/catalogo/1638401607229-600x450.webp",
     "alt": "Bombero con casco y protector facial junto a la unidad",
     "caption": "El ensamble completo en escena"},
    {"src": "/images/catalogo/1756112277157-1000x750.webp",
     "alt": "Rack con equipo estructural alineado en la estación de bomberos",
     "caption": "Control por clave y talla"},
    {"src": "/images/catalogo/1666518809220-1000x750.webp",
     "alt": "Manos con guantes de intervención sujetando equipo de bombero",
     "caption": "Interfaz entre elementos"},
    {"src": "/images/catalogo/1584033376442-600x450.webp",
     "alt": "Bombero equipado con herramienta de intervención durante una maniobra",
     "caption": "Desempeño en maniobra"},
  ]),

  ("aplicaciones", [
    {"sector": "Licitación pública",
     "desc": "Aquí la ambigüedad de nombres se cobra en aclaraciones e impugnaciones. Especifica una línea por capa —exterior, humedad y térmica— con nombre comercial, composición y gramaje declarados en ficha."},
    {"sector": "Cuerpos de bomberos",
     "desc": "Para ampliar una flota que ya opera HERÖ manteniendo modelo y claves. Conviene reponer con la misma configuración que está en servicio para no administrar ensambles mezclados."},
    {"sector": "Brigadas industriales",
     "desc": "Dotación conforme a NOM-002-STPS con expediente documental completo. La configuración de barreras se declara capa por capa, no por familia comercial."},
  ]),

  ("datoClave", {
    "titulo": "Nunca escribas “Defender” a secas",
    "texto": "<strong>Defender 750</strong> es capa exterior. <strong>Defender M</strong> es barrera térmica. Una requisición que dice solo “Defender” se resuelve en la entrega, no en el papel — y ahí ya no se corrige sin costo."
  }),

  ("referencias", [
    {"code": "UL · MH60435", "desc": "Expediente de certificación del HERÖ publicado por SKÖLD. Rastreable en UL Product iQ. Hay que confirmar si su alcance cubre la configuración con Defender 750."},
    {"code": "NFPA 1971 · 2018", "desc": "Edición bajo la que está declarada la certificación UL del modelo. Fue sustituida; su número sigue apareciendo en las claves de producto."},
    {"code": "NFPA 1970 · 2025", "desc": "Estándar vigente que consolidó NFPA 1971, 1975, 1981 y 1982. La transición cerró el 18 de marzo de 2026."},
    {"code": "NFPA 1850 · 2026", "desc": "Consolidó la antigua NFPA 1851. Rige selección, cuidado y mantenimiento del conjunto en servicio, no la certificación."},
    {"code": "NOM-017-STPS", "desc": "Selección, entrega y capacitación en el uso del equipo de protección personal según el riesgo del puesto."},
  ]),

  ("blog", [
    "guia-trajes-estructurales-nfpa-1971",
    "nfpa-1971-mexico-norma-bomberos",
    "equipar-brigada-trajes-bomberos-tallaje-licitacion",
    "licitaciones-equipos-contra-incendios-mexico",
    "marcas-trajes-bomberos-comparativa-mexico",
    "mantenimiento-epp-estructural-nfpa-1851",
  ]),

  ("faqs", [
    {"q": "¿Defender 750 y Defender M son lo mismo?",
     "a": "No, y esta es la confusión que más errores de requisición produce en esta línea. Defender 750 es una de las cinco barreras exteriores seleccionables del HERÖ: la capa que recibe la llama, la abrasión y las cintas reflejantes. Defender M es la barrera térmica que el fabricante documenta en la configuración PBI MAX 7.0: la capa interior que define el tiempo de tolerancia térmica. Comparten familia de nombre y ocupan posiciones distintas del mismo ensamble; no son alternativas entre sí."},
    {"q": "Mi requisición dice “barrera Defender”. ¿Qué me van a entregar?",
     "a": "Depende de cómo lo interprete quien la surta, y eso ya es el problema. Escrito así, el proveedor puede entregar la configuración con capa exterior Defender 750 mientras tú esperabas la barrera térmica Defender M de la configuración PBI MAX, y ninguno de los dos estaría mintiendo. Corrígelo antes de la entrega: escribe una línea por capa —“capa exterior: …”, “barrera de humedad: …”, “barrera térmica: …”—. Es la corrección más barata de todo el proceso."},
    {"q": "¿Por qué importa tanto nombrar cada capa por separado?",
     "a": "Porque la certificación se emite sobre el ensamble armado, no sobre la tela. Los dos valores que exige la norma —TPP y THL— se ensayan sobre la muestra de las tres capas en el orden y con los materiales de la configuración real. Si cambia una capa, el ensamble certificado es otro. Una partida que solo nombra una familia comercial no describe un ensamble y por lo tanto no describe nada certificable."},
    {"q": "¿Qué otros nombres se confunden en equipo estructural?",
     "a": "Varios, y todos cambian lo que se compra: NFPA 1971 frente a NFPA 1970, la vigente que la consolidó; NFPA 1851 frente a NFPA 1850, que rige el inventario en servicio; Nomex como familia frente a Nomex IIIA como mezcla específica; PBI como fibra frente a PBI Matrix y PBI MAX como construcciones de tela distintas; y Stedair, que es familia de barreras de humedad, frente a Stedshield, que es material de refuerzo. La regla es simple: ningún nombre comercial sin su función y su posición en el ensamble."},
    {"q": "¿Qué sí puedo exigir por escrito si elijo Defender 750?",
     "a": "Todo lo que SKÖLD publica a nivel de modelo: DRD integrado en la espalda, cuello de cobertura 360° sin partes expuestas, arnés de Kevlar integrado, refuerzos Stedshield y Ultrashield en mangas, hombros, codos, rodillas y tobillos, costura de Kevlar doble y triple, puño de Kevlar con ojillo para pulgar, cinta ORALITE Ultra Brilliance serie FTP2575-S de 3″, corte tipo diamante en el pantalón, tallas de S a 4X y las claves CHB910, PB910 y TB910 por presentación."},
    {"q": "¿El expediente UL MH60435 cubre la configuración Defender 750?",
     "a": "Es lo que hay que confirmar por escrito, y aquí pesa más que en otras configuraciones porque dos de las tres capas están sin declarar. El expediente es del modelo HERÖ y la configuración documentada en la ficha que conocemos es la de PBI MAX 7.0. Como la certificación se emite sobre el ensamble completo, su existencia no acredita automáticamente esta combinación. Pedimos al fabricante que declare alcance y edición normativa aplicables."},
    {"q": "¿Entonces Defender 750 es peor que PBI MAX 7.0?",
     "a": "No hay base para afirmarlo, ni tampoco lo contrario. La diferencia verificable hoy es de información: de las cinco barreras del HERÖ solo PBI MAX publica composición, gramaje y la combinación de barreras interiores de su configuración. Una barrera puede ser excelente y no tener ficha pública. Lo que no se puede es compararlas técnicamente ni sostener su alcance certificado mientras falten esos datos."},
    {"q": "¿Pueden revisar mis bases antes de que las publique?",
     "a": "Sí, y es lo que recomendamos hacer primero. Revisamos que cada capa aparezca nombrada con su función y su posición en el ensamble, que el certificado se pida con expediente, organismo emisor y edición, y que las claves de producto y tallas queden especificadas como el fabricante las publica. Después cotizamos. Cuesta media hora y evita una aclaración de bases o una impugnación."},
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
