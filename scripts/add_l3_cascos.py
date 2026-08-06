# -*- coding: utf-8 -*-
"""Agrega el bloque l3 a cascos-bullard-y-msa (EPP para Bomberos).

Datos de fabricante verificados el 2026-08-05 en:
  - bullard.com (PX Series, USRX) y hojas BIDSPECS de api.bullard.com (PX, UST)
  - us.msasafety.com (Cairns 1836, 660C Metro, XF1, 1044, 1010)
  - ficha de producto MSA Cairns 1836 (3600-169-MC)
  - ~/Documents/Claude/Projects/LGACONTRAINCENDIOS/src/data/productos/cascoBombero.mjs
    (fuente primaria consolidada, revisada 2026-07-20)
Idempotente: reescribe el bloque l3 completo cada vez que se corre.
"""
import json, io, collections

RUTA = 'src/data/productos.json'

L3 = collections.OrderedDict([
  ("seoTitle", "Cascos de bombero Bullard y MSA NFPA 1970"),
  ("seoDescription", "Cascos estructurales Bullard y MSA Cairns con coquilla de composite o termoplástico, cofia de impacto, ratchet y protección ocular. Cotización en 24 horas."),
  ("h1", "Cascos estructurales Bullard y MSA para bombero"),
  ("subtitulo", "Coquilla de composite termoestable o termoplástico de alta temperatura, cofia de impacto, suspensión con ratchet y protección ocular integrada, en las series que Bullard y MSA Cairns publican con ficha técnica y edición normativa verificable."),
  ("heroImg", {
    "src": "/images/catalogo/1776648120640-1000x750.webp",
    "alt": "Cascos estructurales y trajes de bombero colgados en el vestidor de la estación",
    "caption": "Un casco asignado por elemento, con clave y talla"
  }),
  ("heroBloques", [
    {
      "label": "Por qué la especificación importa",
      "texto": "El <strong>casco de bombero</strong> es el único elemento del ensamble que todavía se compra por silueta. Lo que cambia entre series no es la forma: es el material de la coquilla, la cofia de impacto, el rango de ajuste y el tipo de protección ocular. Un casco industrial clase E puesto en un incendio estructural no es menos protección, es otra categoría de producto, y la verificación llega por dos frentes —<strong>NFPA 1970</strong> sobre el ensamble y <strong>NOM-017-STPS</strong> sobre su entrega y capacitación—."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "Distribuimos <strong>Bullard y MSA Cairns</strong> con refacciones de suspensión, barboquejo, orejeras y protección ocular disponibles por número de parte, etiqueta y certificado del modelo cotizado, y manual del fabricante en español donde la marca lo publica. Entregamos <strong>propuesta técnica en menos de 24 horas hábiles</strong> y equipamos cuerpos de bomberos, brigadas industriales y unidades de protección civil en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Certificación", "valor": "NFPA 1970, edición vigente"},
    {"label": "Retiro obligatorio", "valor": "10 años desde fabricación"}
  ]),
  ("specStrip", [
    {"label": "Coquilla", "valor": "Composite termoestable o termoplástico"},
    {"label": "Cofia de impacto", "valor": "Espuma de uretano de alta temperatura"},
    {"label": "Suspensión", "valor": "Ratchet con ajuste de altura"},
    {"label": "Protección ocular", "valor": "Visor abatible, Bourkes o goggles"},
    {"label": "Barboquejo", "valor": "Nomex con liberación rápida"},
    {"label": "Rango de talla", "valor": "5-3/8 a 8-3/8 pulgadas"}
  ]),
])

L3["catalogo"] = collections.OrderedDict([
  ("eyebrow", "Catálogo por marca"),
  ("titulo", "Cascos estructurales<br>por marca y serie"),
  ("intro", "Cada marca organiza su línea por <strong>serie</strong>, y la serie es la que define coquilla, suspensión, rango de talla y protección ocular. Aquí cada card es una serie cotizable, con la norma que declara el fabricante y el dato que hay que pedirle antes de compararla contra otra. Hoy están publicadas tres series de <strong>Bullard</strong> y tres de <strong>MSA Cairns</strong>; el catálogo crece por marca."),
  ("imgRef", "Imagen de referencia de la serie"),
  ("nota", "Las declaraciones normativas no están homologadas entre marcas y aquí se reproducen tal cual: Bullard publica <strong>NFPA 1970 edición 2025</strong> en las series PX, UST y LT, mientras sus hojas de especificación para licitación todavía citan NFPA 1971; MSA declara <strong>NFPA 1971 edición 2018</strong> en la ficha del Cairns 1836 y no especifica edición en 660C Metro ni en XF1. La transición a NFPA 1970 cerró el <strong>18 de marzo de 2026</strong>, así que un certificado emitido hoy debe referirse a la edición vigente; el inventario ya etiquetado no se invalida —su uso en campo se rige por NFPA 1850 (1851)—. La verificación es por unidad: etiqueta cosida, organismo certificador, edición, serie, configuración ocular y número de parte."),
  ("cards", [
    {
      "marca": "Bullard",
      "modelo": "PX Series",
      "variante": "Termoplástico",
      "varianteLabel": "Coquilla",
      "badge": "NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1575507371202-600x400.webp",
      "alt": "Cascos estructurales amarillos de perfil contemporáneo con visera abatible",
      "desc": "Silueta contemporánea de perfil recortado con ala trasera acampanada. Bullard publica <strong>dimensiones exteriores de 14\" × 10\" × 6-7/8\"</strong> y coquilla termoplástica de alta temperatura. Es la serie con más opciones de iluminación integrada del catálogo.",
      "specs": [
        "Coquilla termoplástica de alta temperatura",
        "Suspensión U-Fit con 36 posiciones de ajuste",
        "Visor ReTrak retráctil operable con una mano",
        "TrakLite: ocho LED frontales y luz trasera"
      ],
      "chip": "Peso no publicado · se solicita por número de parte"
    },
    {
      "marca": "Bullard",
      "modelo": "UST Traditional",
      "variante": "Composite termoestable",
      "varianteLabel": "Coquilla",
      "badge": "NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1638401607229-600x450.webp",
      "alt": "Bombero con casco tradicional de ala completa y protector facial junto a la unidad",
      "desc": "La tradicional de ala completa de Bullard: fibra de vidrio con resina termoestable, beading reforzado con aluminio y <strong>dimensiones de 15-5/8\" × 12\" × 7\"</strong>. Su versión LowRider es la única referencia consultada con peso publicado.",
      "specs": [
        "Composite de fibra de vidrio con resina termoestable",
        "Cofia de uretano sobre coquilla interior de alta temperatura",
        "Tres opciones de protección ocular documentadas",
        "Cinco años de garantía en la coquilla"
      ],
      "chip": "LowRider: 49.3 a 54.4 oz · 1.4 a 1.5 kg publicados"
    },
    {
      "marca": "Bullard",
      "modelo": "LT Series",
      "variante": "Termoplástico ligero",
      "varianteLabel": "Coquilla",
      "badge": "NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1690210795713-600x450.webp",
      "alt": "Dos bomberos con casco estructural y visera durante una operación",
      "desc": "La serie ligera, con <strong>Quick-Attach</strong> para cambiar la protección ocular sin herramienta y ajuste U-Fit de 12 posiciones. Es la única serie donde el fabricante documenta <strong>qué ajusta cada eje</strong>: altura de uso y balance adelante-atrás por separado.",
      "specs": [
        "Coquilla termoplástica de perfil contemporáneo",
        "Quick-Attach para careta y goggles sin herramienta",
        "U-Fit de 12 posiciones en dos ejes documentados",
        "Modelos LTX y LTG4X en la misma serie"
      ],
      "chip": "Ajuste documentado por eje · altura y balance"
    },
    {
      "marca": "MSA",
      "modelo": "Cairns 1836",
      "variante": "Tradicional composite",
      "varianteLabel": "Serie",
      "badge": "NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1735107673023-600x400.webp",
      "alt": "Bombero de perfil con casco tradicional de ala completa y equipo estructural",
      "desc": "La tradicional vigente de MSA y la ficha más detallada del catálogo: coquilla de composite moldeada en una pieza con <strong>espesor de 0.075\" en la corona y 0.085\" en el ala</strong>, y peso publicado de 53.6 a 63.0 oz (1.5 a 1.8 kg) según configuración.",
      "specs": [
        "Composite de fibra de vidrio con espesor publicado por zona",
        "Cofia de impacto de uretano de alta temperatura",
        "Suspensión de seis tiras con ratchet pivotante",
        "Rango de talla de 5-3/8 a 8-3/8 pulgadas"
      ],
      "chip": "Garantía de 10 años desde la fecha de fabricación"
    },
    {
      "marca": "MSA",
      "modelo": "Cairns 660C Metro",
      "variante": "Perfil metro",
      "varianteLabel": "Serie",
      "badge": "NFPA · edición a confirmar",
      "estado": "sin-ficha",
      "img": "/images/catalogo/1575507371089-600x450.webp",
      "alt": "Chaquetones y cascos estructurales colgados en la estación de bomberos",
      "desc": "Perfil recortado para maniobra en espacios reducidos, con coquilla de composite tintado en masa y <strong>banda frontal diseñada para librar el reborde de la pieza facial del ERA</strong>. Admite visor Defender retráctil operable con guante puesto.",
      "specs": [
        "Coquilla de composite tintado en masa",
        "Ratchet trasero con tres posiciones de altura",
        "Banda frontal con interfaz para pieza facial de ERA",
        "Visor Defender retráctil o careta de 4 pulgadas"
      ],
      "chip": "MSA no publica peso ni edición · se piden por parte"
    },
    {
      "marca": "MSA",
      "modelo": "Cairns XF1",
      "variante": "Jet sin ala",
      "varianteLabel": "Serie",
      "badge": "NFPA · edición a confirmar",
      "estado": "sin-ficha",
      "img": "/images/catalogo/1726262693471-600x450.webp",
      "alt": "Casco estructural de perfil jet con visor integrado en escena nocturna",
      "desc": "Silueta jet sin ala, pensada para reducir enganches y alojar módulo de luz e intercomunicación. Se surte en <strong>tallas M y L</strong>, y MSA advierte que las aprobaciones cambian según número de parte, configuración y país.",
      "specs": [
        "Silueta jet sin ala, menor superficie de enganche",
        "Módulo de luz frontal y lateral integrado",
        "Headset de comunicación interno opcional",
        "Interiores lavables y reemplazables"
      ],
      "chip": "Aprobación por número de parte · confirmar antes de licitar"
    }
  ])
])

L3["secciones"] = [
  {
    "id": "anatomia",
    "eyebrow": "Anatomía del casco",
    "titulo": "Las cuatro piezas que trabajan en un impacto",
    "parrafos": [
      "Un <strong>casco estructural</strong> parece una sola pieza y en realidad son cuatro trabajando en secuencia: la coquilla desvía y reparte, la cofia de impacto absorbe, la suspensión sostiene la cabeza separada de la coquilla y el barboquejo mantiene todo en posición. Cuando una especificación se limita a decir “casco de bombero certificado”, está comprando la primera y dejando las otras tres al criterio del proveedor.",
      "El orden en que fallan también es distinto. La coquilla se ve y se revisa; la cofia y la suspensión se degradan por dentro, por calor y por sudor, y son las piezas que casi nadie inspecciona hasta que el casco ya no ajusta. Por eso la inspección anual documentada que pide NFPA 1850 tiene que abrir el casco, no solo mirarlo. Las cuatro piezas se venden por número de parte, así que la reposición no obliga a cambiar el casco completo."
    ],
    "lista": [
      {"t": "Coquilla", "d": "Composite de fibra de vidrio con resina termoestable o termoplástico de alta temperatura. Recibe el impacto, reparte la carga y resiste penetración y calor radiante. Es la pieza que define la silueta y, con ella, casi toda la discusión de compra."},
      {"t": "Cofia de impacto", "d": "Espuma de uretano de alta temperatura sobre una coquilla interior. Es la que absorbe la energía deformándose: Bullard declara una coquilla interior con temperatura de deflexión superior a 220 °F a 264 psi, y MSA describe una cofia de celda abierta removible para limpieza."},
      {"t": "Suspensión", "d": "Sistema de tiras de nylon con banda de ratchet y ajuste de altura. Mantiene la separación entre cráneo y coquilla —el espacio donde ocurre la absorción— y define el rango de talla. MSA publica de 5-3/8 a 8-3/8 pulgadas en incrementos de un octavo."},
      {"t": "Barboquejo", "d": "Cinta de Nomex con hebilla de liberación rápida. Sin él abrochado el casco se desplaza en cuanto el elemento deja de estar vertical: gateo, escalera, ataque bajo. Bullard declara dos tramos de 3/4 de pulgada con extensión máxima de 24 pulgadas."}
    ]
  },
  {
    "id": "coquilla",
    "eyebrow": "Decisión de material",
    "titulo": "Composite, termoplástico o cuero: qué cambia",
    "parrafos": [
      "La discusión suele plantearse como “tradicional o moderno”, que es una decisión de silueta. La decisión técnica es el material de la coquilla, porque de ahí salen el peso, el comportamiento tras exposiciones repetidas a calor y el costo de reposición. Ninguna de las tres familias es mejor en abstracto: cada una tiene un perfil de uso donde gana."
    ],
    "tabla": {
      "head": ["Material de coquilla", "Series consultadas", "Lo que publica el fabricante", "Perfil de uso"],
      "rows": [
        ["Composite de fibra de vidrio con resina termoestable", "Bullard UST · MSA Cairns 1836 y 660C Metro", "Espesor por zona en el 1836: 0.075\" en corona y 0.085\" en ala. Beading reforzado con aluminio en la UST.", "Cuerpos con procedimiento de ala completa y exposición térmica frecuente, donde la rigidez y el color en masa importan más que el peso."],
        ["Termoplástico de alta temperatura", "Bullard PX y LT Series", "Bullard describe materiales de alta temperatura que resisten degradación tras exposiciones repetidas; dimensiones publicadas de 14\" × 10\" × 6-7/8\" en la PX.", "Brigadas industriales y unidades que priorizan menor peso, perfil recortado y reposición económica de la coquilla."],
        ["Cuero curtido", "MSA Cairns N6A Houston y N5A New Yorker", "MSA lo trabaja a mano en piel de res de grano superior y lo documenta como línea histórica de la marca.", "Cuerpos con tradición de cuero y unidades ceremoniales. Es la familia más pesada y la de mantenimiento más específico."],
        ["Termoplástico de silueta jet", "MSA Cairns XF1", "Tallas M y L, módulo de luz integrado y headset interno. Las aprobaciones cambian por número de parte, configuración y país.", "Rescate técnico, espacios reducidos y unidades que necesitan luz y comunicación integradas sin accesorios colgados."]
      ]
    },
    "nota": "El material no se deduce de la foto: hay siluetas tradicionales en composite y en cuero que se ven casi idénticas, y perfiles modernos en termoplástico y en composite que también. En la partida debe escribirse el material, no el estilo."
  },
  {
    "id": "peso",
    "eyebrow": "Carga sobre el cuello",
    "titulo": "El peso publicado y el que no se publica",
    "parrafos": [
      "El casco es el único elemento del ensamble que cuelga de la columna cervical, y en intervenciones largas la diferencia entre 1.4 y 1.8 kg se acumula. El problema práctico es que <strong>la mayoría de los fabricantes no publica el peso</strong> de sus series de casco estructural: lo publican del cilindro del equipo de respiración autónoma, del ensamble y de la bota, pero no del casco.",
      "De las series consultadas para esta ficha, solo dos tienen cifra publicada. Cuando el peso es criterio de evaluación —y en un cuerpo con turnos de doce horas debería serlo— hay que pedirlo por escrito al fabricante para la configuración exacta, con protección ocular y accesorios montados, porque un visor y un módulo de luz cambian el número."
    ],
    "tabla": {
      "head": ["Serie", "Peso publicado", "Dónde lo publica"],
      "rows": [
        ["Bullard UST LowRider", "49.3 a 54.4 oz · 1.4 a 1.5 kg", "Ficha de producto de la versión LowRider"],
        ["MSA Cairns 1836", "53.6 a 63.0 oz · 1.5 a 1.8 kg", "Ficha de producto, rango por configuración"],
        ["Bullard PX Series", "No publicado", "La hoja de licitación detalla materiales y dimensiones, no peso"],
        ["Bullard LT Series", "No publicado", "Se solicita al fabricante por número de parte"],
        ["MSA Cairns 660C Metro", "No publicado", "Se solicita al fabricante por número de parte"],
        ["MSA Cairns XF1", "No publicado", "Se solicita al fabricante por número de parte y configuración"]
      ]
    },
    "nota": "Un rango de peso no es un peso. “1.5 a 1.8 kg” significa que la configuración cotizada puede estar en cualquier punto de ese rango: el número que importa es el de la clave que va a llegar a la estación."
  },
  {
    "id": "ajuste",
    "eyebrow": "Ajuste y talla",
    "titulo": "El rango de ajuste no sustituye la prueba individual",
    "parrafos": [
      "Un rango de ajuste amplio permite compartir cascos entre turnos y facilita la administración del inventario, pero no dice nada sobre cómo queda el casco en una cabeza concreta con capucha y pieza facial puestas. La prueba de ajuste se hace con el conjunto completo y en las posiciones reales de trabajo, no con el casco solo frente al espejo del almacén.",
      "El punto crítico es la interfaz: el borde inferior del casco tiene que solapar con la capucha sin comprimir el reborde de la pieza facial del ERA. Un casco bien ajustado que empuja la máscara compromete el sello facial, que es el elemento que sostiene la vida en ambiente IDLH. MSA documenta explícitamente una banda frontal ajustable para librar ese reborde en el 660C Metro. Es la misma lógica con la que se prueba el traje estructural: el elemento se mide con el conjunto completo puesto, no pieza por pieza."
    ],
    "lista": [
      {"t": "Rango de talla publicado", "d": "MSA declara de 5-3/8 a 8-3/8 pulgadas en incrementos de un octavo para el Cairns 1836. Bullard describe su sistema U-Fit con 36 posiciones en la PX y la UST LowRider, y 12 posiciones en la serie LT."},
      {"t": "Ajuste de altura", "d": "Además del perímetro, el casco se ajusta en altura. Bullard declara al menos una pulgada de recorrido con tres llaves de altura; MSA usa un ratchet trasero de tres posiciones. Ese ajuste es el que cambia la posición del ala frente a los ojos."},
      {"t": "Prueba con el conjunto puesto", "d": "Capucha, protección ocular, pieza facial y comunicaciones. Mirar hacia arriba, agacharse, avanzar en gateo, girar la cabeza en un espacio reducido. Lo que se busca es que el casco no se mueva ni empuje la máscara."},
      {"t": "Operación con guante", "d": "El visor, la hebilla del barboquejo y el ratchet tienen que operarse con guante estructural puesto. MSA declara el visor Defender del 660C Metro como operable con guante; es un dato que conviene exigir por escrito para cualquier serie."}
    ]
  },
  {
    "id": "puntos-de-suspension",
    "eyebrow": "Cómo leer la ficha",
    "titulo": "Cuatro, seis u ocho puntos: qué declara el fabricante",
    "parrafos": [
      "En catálogo comercial es común leer “suspensión de cuatro puntos” o “de ocho puntos” como si fuera una medida normalizada. No lo es: cada fabricante cuenta de forma distinta —tiras, llaves de anclaje o puntos de contacto— y dos cascos anunciados con el mismo número pueden tener geometrías diferentes. Lo que sí es verificable es la descripción textual de la ficha.",
      "Bullard describe para la UST Traditional un sistema de tres tiras de nylon de 3/4 de pulgada ancladas en <strong>seis llaves</strong>, con banda de ratchet y ajuste trasero de altura; para la PX declara la corona U-Fit de seis puntos con <strong>36 combinaciones de ajuste</strong>. MSA describe para el Cairns 1836 una <strong>suspensión de seis vías</strong> con ratchet pivotante. Ninguno de los tres se compara bien contra un “ocho puntos” de catálogo sin ver el dibujo."
    ],
    "nota": "En una partida conviene pedir la descripción literal de la suspensión y el número de parte de la refacción, no un número de puntos. Así la evaluación se hace contra la ficha del fabricante y no contra un adjetivo comercial."
  },
  {
    "id": "proteccion-ocular",
    "eyebrow": "Protección ocular",
    "titulo": "El visor del casco no es protección ocular primaria",
    "parrafos": [
      "Esta es la confusión más cara del rubro. La careta o el visor montados al casco protegen la cara de proyecciones frontales, pero <strong>ANSI Z87.1 y la práctica del sector coinciden en que no se consideran protección ocular primaria</strong>: las partículas entran por abajo y por los lados. NFPA 1500 reconoce la <strong>pieza facial del ERA</strong> como protección ocular y facial primaria durante el combate.",
      "La consecuencia práctica es que un casco con visor no resuelve la protección ocular en las maniobras donde el elemento no trae la máscara puesta: ventilación, remoción de escombro, rescate vehicular, trabajo en exterior. Para esas tareas la respuesta son goggles, y por eso todas las series consultadas ofrecen configuración con goggles además del visor."
    ],
    "lista": [
      {"t": "Visor o careta abatible", "d": "Bullard declara careta de PPC con recubrimiento duro de 4\" × 15\" que cumple ANSI/ISEA Z87.1, y el visor ReTrak de poliarilato operable con una mano. MSA ofrece el visor Defender articulado en versión clara o ámbar."},
      {"t": "Bourkes", "d": "Protección tipo Bourke, la solución tradicional montada bajo el ala. MSA la documenta como opción en la línea Cairns, incluida la versión declarada para NFPA en el 1836."},
      {"t": "Goggles", "d": "La única de las tres que funciona como protección ocular en el sentido estricto. Bullard documenta ESS FirePro e Inner Zone; MSA documenta ESS Innerzone. Se especifican por separado y con su propio número de parte."}
    ],
    "nota": "En la especificación conviene separar dos renglones: protección facial montada al casco y protección ocular. Si se escriben como uno solo, el proveedor entrega la careta y la brigada se queda sin goggles."
  },
  {
    "id": "edicion-normativa",
    "eyebrow": "Tendencia del mercado",
    "titulo": "NFPA 1970, series descontinuadas y qué escribir hoy",
    "parrafos": [
      "El mercado de cascos está en el punto más confuso de su transición normativa. <strong>NFPA 1970 edición 2025</strong> consolidó las NFPA 1971, 1975, 1981 y 1982, y el periodo de transición cerró el <strong>18 de marzo de 2026</strong>. En la práctica eso convive con fichas de fabricante que todavía citan NFPA 1971 en ediciones 2013 o 2018, con hojas de licitación sin actualizar y con material comercial que escribe “cumple con NFPA” sin edición.",
      "Al mismo tiempo, dos de las series más citadas en especificaciones mexicanas —el <strong>Cairns 1044 y el 1010</strong>— aparecen marcadas como descontinuadas en el sitio de MSA, y el 1836 es su tradicional vigente. Una especificación que todavía pide un 1044 por nombre no está pidiendo un producto disponible: está garantizando que el proveedor ofrezca “equivalente” sin criterio escrito para evaluarlo."
    ],
    "nota": "La partida que resuelve las dos cosas al mismo tiempo se escribe así: serie y modelo vigentes, material de coquilla, descripción literal de la suspensión, rango de talla, configuración de protección facial y ocular por separado, accesorios, color y marcaje, <strong>edición normativa vigente</strong>, organismo certificador, certificado del modelo cotizado e idioma del manual. Con esos renglones, dos cotizaciones del mismo precio dejan de ser dos cascos distintos."
  }
]

L3["galeria"] = [
  {"src": "/images/catalogo/1756112277157-1000x750.webp", "alt": "Rack con cascos estructurales alineados en la estación de bomberos", "caption": "Un casco por elemento, con clave y talla"},
  {"src": "/images/catalogo/1592235905030-600x450.webp", "alt": "Bombero con pieza facial de equipo de respiración bajo el casco estructural", "caption": "La interfaz con la pieza facial"},
  {"src": "/images/catalogo/1608723724615-600x450.webp", "alt": "Dos bomberos con casco numerado operando en ambiente con humo", "caption": "Identificación visible en escena"},
  {"src": "/images/catalogo/1563062067-bb-600x450.webp", "alt": "Bombero de perfil con casco rojo y equipo de respiración autónoma", "caption": "Color por función y mando"}
]

L3["aplicaciones"] = [
  {"sector": "Cuerpos de bomberos", "desc": "Casco asignado por elemento con talla registrada, refacciones de suspensión y barboquejo en inventario, y bitácora por fecha de fabricación para escalonar el retiro a diez años."},
  {"sector": "Brigadas industriales", "desc": "Selección que distingue casco estructural de casco industrial NOM-115-STPS según la matriz de riesgo, con protección ocular especificada aparte del visor del casco."},
  {"sector": "Protección civil", "desc": "Cascos con etiqueta legible, certificado del modelo cotizado, manual en español donde el fabricante lo publica y factura desglosada por serie, talla y accesorio."}
]

L3["datoClave"] = {
  "titulo": "El dato que mueve el presupuesto",
  "texto": "MSA garantiza el Cairns 1836 por <strong>10 años desde la fecha de fabricación</strong>, y ese mismo criterio rige el retiro del casco bajo NFPA 1850 (1851). Pide la fecha por número de serie antes de firmar: un lote con dos años de inventario llega con ocho de vida útil."
}

L3["normasRef"] = ["NFPA 1970", "NFPA 1971", "NOM-115-STPS", "NFPA 1851", "NOM-017-STPS"]

# El expediente del casco no es el del traje: aquí no hay tres capas ni procedimiento de
# lavado de prenda. Sobreescribe cat.documentacion en el sidebar de esta ficha.
L3["documentacion"] = [
  "Certificado del modelo cotizado con edición normativa vigente",
  "Etiqueta permanente legible con fecha de fabricación por unidad",
  "Ficha técnica con material de coquilla, suspensión y rango de talla",
  "Números de parte de suspensión, barboquejo, orejeras y visor",
  "Manual de inspección y retiro de servicio en español donde el fabricante lo publica",
  "Carta de distribuidor autorizado y factura desglosada por serie y talla"
]

L3["blog"] = [
  "casco-bombero-bullard-usrhb-guia",
  "cascos-forestales-msa-cairns-guia",
  "epp-completo-kit-bombero-profesional",
  "capucha-nomex-pbi-proteccion-cuello-cara",
  "nfpa-1971-mexico-norma-bomberos",
  "mantenimiento-epp-estructural-nfpa-1851"
]

L3["faqs"] = [
  {
    "q": "¿Qué diferencia real hay entre un casco estructural y un casco industrial?",
    "a": "Son categorías distintas de producto, no dos grados del mismo. El casco industrial que regula la NOM-115-STPS está diseñado para impacto de objetos que caen y, en su clase dieléctrica, para aislamiento eléctrico; su suspensión está optimizada para confort en jornada larga. El casco estructural se evalúa además por resistencia a calor radiante, llama directa y penetración, integra protección facial certificada y está diseñado para trabajar con capucha y pieza facial de ERA. Un casco industrial en combate estructural no es menos protección: es protección para otras amenazas."
  },
  {
    "q": "¿Cuánto pesa un casco estructural y cuál es un peso aceptable?",
    "a": "De las series consultadas, solo dos publican peso: la Bullard UST LowRider entre 49.3 y 54.4 oz (1.4 a 1.5 kg) y el MSA Cairns 1836 entre 53.6 y 63.0 oz (1.5 a 1.8 kg). No hay un límite normativo de peso, así que el criterio es operativo: turnos largos y maniobra en espacios reducidos empujan hacia el extremo bajo del rango. Si el peso va a evaluarse, hay que pedirlo por escrito para la configuración exacta —con visor y accesorios montados—, porque la mayoría de las series no lo publica."
  },
  {
    "q": "¿El visor del casco cuenta como protección ocular?",
    "a": "No como protección ocular primaria. ANSI Z87.1 y la práctica del sector coinciden en que la careta montada al casco no se considera protección ocular primaria, porque las partículas entran por abajo y por los costados; NFPA 1500 reconoce la pieza facial del ERA como protección ocular y facial primaria durante el combate. Para las maniobras donde el elemento no trae máscara —ventilación, remoción, rescate vehicular— la respuesta son goggles, que se especifican por separado y con su propio número de parte."
  },
  {
    "q": "¿Cada cuándo se retira un casco de bombero?",
    "a": "El criterio es la fecha de fabricación de la etiqueta, no la fecha de compra: NFPA 1850 (1851) fija el retiro del elemento a los 10 años de fabricación, y MSA emite su garantía del Cairns 1836 con ese mismo horizonte. Antes de ese plazo el casco se retira si tuvo un impacto, si la coquilla presenta deformación, burbujeo o decoloración por calor, o si la etiqueta dejó de ser legible. Un golpe absorbido puede comprometer la cofia sin dejar marca visible en la coquilla."
  },
  {
    "q": "¿Se venden refacciones o hay que cambiar el casco completo?",
    "a": "Las cuatro piezas se venden por número de parte. Suspensión completa, banda de ratchet, cubierta de la banda, almohadilla frontal, barboquejo, orejeras y protección ocular son reemplazables en las series de Bullard y de MSA que distribuimos. Bullard declara además cinco años de garantía en la coquilla y cobertura del resto de componentes no electrónicos por la vida útil definida en NFPA 1851. Reponer suspensión y orejeras es lo que sostiene el ajuste y la higiene del casco entre inspecciones anuales."
  },
  {
    "q": "¿Conviene el estilo tradicional de ala completa o el perfil moderno?",
    "a": "Depende de la maniobra dominante y del procedimiento local, no de la marca. El ala completa desvía agua y escombro hacia atrás y es la silueta que la mayoría de los cuerpos mexicanos tiene normada; el perfil recortado y el jet sin ala estorban menos en espacios reducidos y en el interior de vehículos, y alojan mejor luz y comunicación integradas. Muchos cuerpos resuelven con dos configuraciones: ala completa para combate estructural y perfil jet para rescate técnico."
  },
  {
    "q": "¿El casco es compatible con cualquier pieza facial de ERA?",
    "a": "No se debe asumir. La compatibilidad depende de la geometría del borde inferior del casco y del reborde de la pieza facial, y se comprueba con el equipo real que va a usar el elemento, con capucha puesta. MSA documenta una banda frontal ajustable pensada para librar ese reborde en el 660C Metro; en el resto de las series es una prueba que hay que hacer antes de cerrar la compra. Un casco que empuja la máscara compromete el sello facial, que es lo que sostiene la vida en ambiente IDLH."
  },
  {
    "q": "¿Qué debe pedir una licitación de cascos para que dos ofertas sean comparables?",
    "a": "Serie y modelo vigentes, material de coquilla, descripción literal de la suspensión con su número de parte, rango de talla, configuración de protección facial y de protección ocular en renglones separados, accesorios, color y marcaje, edición normativa vigente, organismo certificador, certificado del modelo cotizado, idioma del manual y fecha de fabricación por unidad. Sin ese desglose, dos cotizaciones del mismo precio pueden corresponder a cascos de categorías distintas."
  }
]



with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'cascos-bullard-y-msa')
prod['l3'] = L3

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('l3 agregado a', prod['slug'])
print('  secciones:', len(L3['secciones']), '| faqs:', len(L3['faqs']),
      '| cards:', len(L3['catalogo']['cards']), '| galeria:', len(L3['galeria']))
print('  seoTitle len:', len(L3['seoTitle']) + len(' | Firefighter.com.mx'))
print('  seoDescription len:', len(L3['seoDescription']))
ids = [s['id'] for s in L3['secciones']]
assert len(ids) == len(set(ids)), 'ids de seccion duplicados: %s' % ids
imgs = [c['img'] for c in L3['catalogo']['cards']] + [g['src'] for g in L3['galeria']]
dup = [i for i in set(imgs) if imgs.count(i) > 1]
print('  imagenes repetidas en la pagina:', dup or 'ninguna')
