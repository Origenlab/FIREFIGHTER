# -*- coding: utf-8 -*-
"""Agrega el bloque l3 a protector-de-cuello-y-capucha (EPP para Bomberos).

Fuentes primarias consultadas el 2026-08-06:
  - innotexprotection.com  (GRAY Hood 25 y GRAY Hood 25 con PBI: tres capas, exterior
    Nomex/Lenzing 20/80 u Oro PBI/Lenzing 20/80, capa intermedia Stedair PREVENT, forro
    interior de viscosa; bloqueo >99 % de particulas de 0.1 a 1.0 um sostenido "incluso
    despues de 100 lavadas"; THL 427 y TPP 22.6 frente a minimos citados de 325 y 20;
    disenadas para NFPA 1971 edicion 2018)
  - barriaire.com  (PGI BarriAire Gold: exterior de tela FR propia y forro interior de
    DuPont Nomex Nano Flex; 97.4 % de eficiencia en 0.1 a 1.0 um "as received" y 97.3 %
    despues de 10 lavadas; VFE 96.8 %, BFE 97.9 %; acabado DWR libre de PFAS; talla unica;
    23" de largo al frente y atras; certificada EN 13911:2017 y categoria NFPA 70E HRC 4
    con ATPV de 46 cal/cm2)
  - firedex.com  (H41 Interceptor: dos capas de PBI/Lenzing 6.0 oz 20/80 con DuPont Nomex
    Nano Flex laminado en medio; bloquea particulado de 0.2 um o mayor; certificada NFPA 1970,
    sin edicion listada en la pagina)
  - LION Particulate Blocking Hood via distribuidor  (dos capas con Stedair PREVENT,
    efectividad de bloqueo sostenida "incluso despues de 100 lavadas", NFPA 1971 edicion 2018,
    talla universal, bib extendido, tejido permeable al aire)
  - Majestic PAC II Nomex Blend via distribuidor  (la clasica sin capa de particulas,
    listada en 21" y en versiones de 2 y 3 capas, NFPA 1971 edicion 2018)

Eje editorial: la capucha es el punto de fuga del conjunto, y lo que separa una capucha de
otra no es el material del tejido: es si tiene capa de bloqueo de particulas y —sobre todo—
cuanta eficiencia conserva DESPUES DE LAVARLA.
Idempotente.
"""
import json, io, collections

RUTA = 'src/data/productos.json'

L3 = collections.OrderedDict([
  ("seoTitle", "Capuchas de bloqueo de partículas NFPA 1971"),
  ("seoDescription", "Capuchas para bombero con capa de bloqueo de partículas: eficiencias publicadas de 0.1 a 1.0 micras, retención después de lavadas, bib de 21\" a 23\" y TPP y THL."),
  ("h1", "Capuchas para bombero con bloqueo de partículas"),
  ("subtitulo", "Protector de cuello y capucha estructural en tejido aramídico o con capa intermedia de bloqueo de partículas: eficiencias declaradas entre 0.1 y 1.0 micras, retención después de 10 y de 100 lavadas, y bib de 21\" a 23\" para cerrar la interfaz con casco y pieza facial."),
  ("heroImg", {
    "src": "/images/catalogo/1592235905030-1000x750.webp",
    "alt": "Bombero con capucha aramídica y pieza facial de equipo de respiración bajo el casco",
    "caption": "La capucha cierra la interfaz del conjunto"
  }),
  ("heroBloques", [
    {
      "label": "Por qué la capucha es el punto de fuga",
      "texto": "El chaquetón tiene tres capas y barrera de humedad; la capucha, históricamente, es <strong>tejido de punto</strong>. Eso la convierte en la zona más permeable del conjunto, justo sobre cuello y mandíbula. La respuesta del mercado es la <strong>capa intermedia de bloqueo de partículas</strong>, y ahí el dato que decide no es la eficiencia de la capucha nueva: es <strong>cuánta conserva después de lavarla</strong>, porque una capucha se lava después de cada exposición."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "Distribuimos capuchas con <strong>certificado del modelo cotizado, edición normativa y las cifras de eficiencia y de retención por escrito</strong> —no solo la etiqueta “particulate blocking”—. Cotizamos <strong>dos por elemento</strong> como criterio de programa, porque una capucha en la lavadora es un elemento sin protección de cuello. Propuesta técnica en menos de <strong>24 horas hábiles</strong> y cobertura en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Rango de bloqueo", "valor": "0.1 a 1.0 micras"},
    {"label": "Retención publicada", "valor": "Hasta 100 lavadas"}
  ]),
  ("specStrip", [
    {"label": "Capas", "valor": "Dos o tres, según modelo"},
    {"label": "Capa de bloqueo", "valor": "Stedair PREVENT o Nomex Nano Flex"},
    {"label": "Exterior", "valor": "Nomex/Lenzing o PBI/Lenzing"},
    {"label": "Eficiencia declarada", "valor": "97.4 % a más de 99 %"},
    {"label": "Bib", "valor": "De 21\" a 23\""},
    {"label": "Talla", "valor": "Universal en la mayoría"}
  ]),
])

L3["catalogo"] = collections.OrderedDict([
  ("eyebrow", "Catálogo por marca"),
  ("titulo", "Capuchas estructurales<br>por marca y construcción"),
  ("intro", "Todas se ven casi iguales y no protegen igual. Lo que las separa son tres datos: si tienen <strong>capa intermedia de bloqueo de partículas</strong>, la <strong>eficiencia declarada</strong> en el rango de 0.1 a 1.0 micras y —el que casi nadie compara— <strong>cuántas lavadas conserva esa eficiencia</strong>. Cada card reproduce lo que publica el fabricante, incluidas las declaraciones que no son NFPA."),
  ("imgRef", "Imagen de referencia de la línea"),
  ("nota", "Dos advertencias de lectura. Primera: <strong>la etiqueta “particulate blocking” no es una norma</strong>. La página de la PGI BarriAire Gold declara <strong>EN 13911:2017</strong> y categoría NFPA 70E con ATPV de 46 cal/cm², no NFPA 1971; la Fire-Dex H41 declara <strong>NFPA 1970 sin listar edición</strong>; INNOTEX y LION declaran <strong>NFPA 1971 edición 2018</strong>. Segunda: las eficiencias no son comparables sin su condición —“as received”, después de 10 lavadas o después de 100— ni sin el rango de partícula, porque bloquear desde 0.2 micras no es lo mismo que bloquear desde 0.1. Verificación por modelo: certificado, edición, organismo y las cifras de eficiencia y retención por escrito."),
  ("cards", [
    {
      "marca": "INNOTEX",
      "modelo": "GRAY Hood 25",
      "variante": "Tres capas · Nomex",
      "varianteLabel": "Construcción",
      "badge": "NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1735107673023-600x400.webp",
      "alt": "Bombero con capucha aramídica y protector de cuello bajo el casco",
      "desc": "La ficha con más números publicados del catálogo: bloqueo de partículas de 0.1 a 1.0 micras <strong>superior al 99 %</strong> sostenido <strong>incluso después de 100 lavadas</strong>. Tres capas: exterior Nomex/Lenzing 20/80, capa intermedia Stedair PREVENT y forro interior de viscosa.",
      "specs": [
        "Bloqueo declarado >99 % en 0.1 a 1.0 micras",
        "Retención declarada tras 100 lavadas",
        "Tres capas con Stedair PREVENT intermedia",
        "THL 427 y TPP 22.6 publicados"
      ],
      "chip": "El fabricante cita mínimos de 325 THL y 20 TPP"
    },
    {
      "marca": "INNOTEX",
      "modelo": "GRAY Hood 25 con PBI",
      "variante": "Tres capas · PBI",
      "varianteLabel": "Construcción",
      "badge": "NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1592235905030-600x450.webp",
      "alt": "Bombero con capucha bajo el casco y pieza facial de equipo de respiración",
      "desc": "Misma arquitectura de tres capas, con el exterior en <strong>PBI/Lenzing 20/80</strong> en lugar de Nomex/Lenzing. Es la versión premium de la línea y la que se especifica cuando el resto del conjunto ya es PBI, para no mezclar familias de fibra en el ensamble.",
      "specs": [
        "Exterior Oro PBI/Lenzing 20/80",
        "Capa intermedia Stedair PREVENT",
        "Forro interior de viscosa para confort térmico",
        "Diseñada para NFPA 1971 edición 2018"
      ],
      "chip": "Coherencia de fibra con un conjunto PBI"
    },
    {
      "marca": "PGI",
      "modelo": "BarriAire Gold",
      "variante": "Dos capas · bib 23\"",
      "varianteLabel": "Construcción",
      "badge": "EN 13911 · 2017",
      "estado": "documentada",
      "img": "/images/catalogo/1504667452459-600x450.webp",
      "alt": "Bombero con pieza facial y capucha avanzando en escena con humo",
      "desc": "La única del catálogo que publica <strong>eficiencia antes y después de lavar</strong>: 97.4 % en 0.1 a 1.0 micras “as received” y <strong>97.3 % después de 10 lavadas</strong>. Suma VFE de 96.8 % y BFE de 97.9 %, acabado repelente <strong>libre de PFAS</strong> y el bib más largo: 23\" al frente y atrás.",
      "specs": [
        "97.4 % as received · 97.3 % tras 10 lavadas",
        "Forro interior DuPont Nomex Nano Flex",
        "Bib de 23\" al frente y atrás, talla única",
        "Acabado DWR libre de PFAS y antimicrobiano"
      ],
      "chip": "Declara EN 13911:2017 y NFPA 70E, no NFPA 1971"
    },
    {
      "marca": "Fire-Dex",
      "modelo": "H41 Interceptor",
      "variante": "Dos capas · PBI",
      "varianteLabel": "Construcción",
      "badge": "NFPA 1970 · sin edición",
      "estado": "documentada",
      "img": "/images/catalogo/1575867094974-600x450.webp",
      "alt": "Bomberos con equipo de respiración autónoma frente a un frente de fuego",
      "desc": "Dos capas de <strong>PBI/Lenzing de 6.0 oz en 20/80</strong> con <strong>DuPont Nomex Nano Flex laminado en medio</strong>. El fabricante declara bloqueo de particulado de <strong>0.2 micras o mayor</strong> —un umbral distinto al de 0.1 de las otras fichas— y certificación NFPA 1970 sin listar edición.",
      "specs": [
        "Dos capas de PBI/Lenzing 6.0 oz 20/80",
        "Nomex Nano Flex laminado entre capas",
        "Bloqueo declarado desde 0.2 micras",
        "Certificada NFPA 1970 según el fabricante"
      ],
      "chip": "Umbral de 0.2 micras · pedir edición del certificado"
    },
    {
      "marca": "LION",
      "modelo": "Particulate Blocking",
      "variante": "Dos capas · bib extendido",
      "varianteLabel": "Construcción",
      "badge": "NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1608723724615-600x450.webp",
      "alt": "Bomberos con casco y capucha operando en ambiente con humo",
      "desc": "Construcción de dos capas con bloqueador <strong>Stedair PREVENT</strong> —la misma familia de barreras que se usa en trajes— y efectividad de bloqueo declarada <strong>incluso después de 100 lavadas</strong>. Tejido permeable al aire para manejo térmico y bib extendido para hombro y cuello.",
      "specs": [
        "Bloqueador Stedair PREVENT en dos capas",
        "Efectividad declarada tras 100 lavadas",
        "Tejido permeable al aire",
        "Bib extendido, talla universal"
      ],
      "chip": "Certificada NFPA 1971 edición 2018"
    },
    {
      "marca": "Majestic",
      "modelo": "PAC II Nomex Blend",
      "variante": "Clásica sin filtración",
      "varianteLabel": "Construcción",
      "badge": "NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1563062067-bb-600x450.webp",
      "alt": "Bombero de perfil con capucha y equipo de respiración autónoma",
      "desc": "La capucha clásica de tejido, <strong>sin capa de bloqueo de partículas</strong>. Está en el catálogo a propósito: es la referencia contra la que se compara y sigue siendo válida para tareas sin exposición a humo de combustión. Listada en <strong>bib de 21\"</strong> y en versiones de dos y tres capas.",
      "specs": [
        "Tejido aramídico sin capa de filtración",
        "Bib de 21\" según listado de distribuidor",
        "Versiones de dos y tres capas",
        "Certificada NFPA 1971 edición 2018"
      ],
      "chip": "Sin bloqueo de partículas · no equivale a las anteriores"
    }
  ])
])

L3["secciones"] = [
  {
    "id": "punto-de-fuga",
    "eyebrow": "Por qué importa",
    "titulo": "La zona más permeable del conjunto",
    "parrafos": [
      "El chaquetón y el pantalón son sistemas de tres capas con barrera de humedad. La capucha, en su versión clásica, es <strong>tejido de punto</strong>: aramídico, resistente a la flama, pero permeable por construcción. Eso la convierte en la interfaz por la que entra lo que el resto del conjunto detiene, y ocurre justo sobre cuello, mandíbula y nuca.",
      "La respuesta del mercado no fue engrosar el tejido —eso solo suma carga térmica—, sino agregar una <strong>capa intermedia de bloqueo de partículas</strong>. Es el cambio de producto más importante que ha tenido esta pieza en veinte años, y el que separa el catálogo en dos: capuchas con capa de filtración y capuchas sin ella."
    ],
    "lista": [
      {"t": "El tejido no filtra", "d": "Un tejido de punto detiene flama y calor por contacto, no partículas. Una capucha clásica certificada cumple su función térmica y sigue dejando pasar el humo de combustión."},
      {"t": "La capa intermedia sí", "d": "Materiales como <strong>Stedair PREVENT</strong> o <strong>DuPont Nomex Nano Flex</strong> se laminan o cosen entre el exterior y el forro. No cambian la apariencia de la capucha, y son la única diferencia funcional real entre dos capuchas que se ven iguales."},
      {"t": "El bib es parte de la protección", "d": "El faldón que baja al hombro cierra la brecha con el cuello del chaquetón. Entre las referencias del catálogo va de <strong>21\" a 23\"</strong>, y esas dos pulgadas cambian si el traslape se sostiene al levantar los brazos."},
      {"t": "Y sigue siendo una pieza de conjunto", "d": "La capucha se prueba con el <strong>casco estructural</strong> y la pieza facial del equipo de respiración puestos. Una capucha que ajusta sola puede empujar el sello de la máscara."}
    ]
  },
  {
    "id": "particulas",
    "eyebrow": "Cómo se lee una eficiencia",
    "titulo": "Eficiencias declaradas y el rango de partícula",
    "parrafos": [
      "Aquí es donde una comparativa honesta se separa de un folleto. Las eficiencias que publican los fabricantes <strong>no son comparables entre sí</strong> si no se leen con sus dos condiciones: el <strong>rango de partícula</strong> y el <strong>estado del material</strong> —nuevo o después de un número de lavadas—.",
      "El rango importa porque bloquear desde <strong>0.2 micras</strong> no es lo mismo que bloquear desde <strong>0.1</strong>: el humo de combustión estructural tiene fracción ultrafina, y el umbral más bajo cubre más de esa fracción. El estado importa porque una capucha se lava después de cada exposición, así que la cifra de la capucha nueva describe el día uno y nada más."
    ],
    "tabla": {
      "head": ["Referencia", "Eficiencia declarada", "Rango", "Condición del dato"],
      "rows": [
        ["INNOTEX GRAY Hood 25", "Más de 99 %", "0.1 a 1.0 micras", "Declarada sostenida incluso después de 100 lavadas"],
        ["LION Particulate Blocking", "No publica porcentaje", "No especificado", "Efectividad declarada incluso después de 100 lavadas"],
        ["PGI BarriAire Gold", "97.4 % · 97.3 %", "0.1 a 1.0 micras", "97.4 % “as received” y 97.3 % después de 10 lavadas"],
        ["Fire-Dex H41 Interceptor", "No publica porcentaje", "0.2 micras o mayor", "Sin condición de lavado publicada en la página consultada"],
        ["Majestic PAC II", "Sin capa de bloqueo", "—", "Capucha clásica de tejido: cumple función térmica, no filtra"]
      ]
    },
    "nota": "La pregunta que hay que hacerle a cualquier proveedor: <strong>“¿qué porcentaje, en qué rango de micras, y medido en qué condición: nueva o después de cuántas lavadas?”</strong>. Tres datos. Si falta uno, la cifra no se puede comparar contra otra oferta."
  },
  {
    "id": "lavadas",
    "eyebrow": "El dato que decide la compra",
    "titulo": "La eficiencia después de lavar es la que se usa",
    "parrafos": [
      "Una capucha de partículas se lava <strong>después de cada exposición</strong> —es la pieza que más contacto tiene con la piel y la que más contaminante acumula—. Eso significa que en tres años de servicio una capucha acumula decenas de ciclos, y que la cifra relevante no es la del material nuevo.",
      "El catálogo se ordena solo cuando se mira por ahí: INNOTEX y LION declaran retención de la efectividad <strong>después de 100 lavadas</strong>; PGI publica el par completo —97.4 % nueva y <strong>97.3 % después de 10</strong>—, que es la manera más transparente de decirlo aunque el número de ciclos sea menor; Fire-Dex no publica condición de lavado en la página que consultamos."
    ],
    "nota": "Consecuencia práctica para el programa: <strong>dos capuchas por elemento</strong>. Una en servicio y una en rotación de lavado. Una capucha en la lavadora es, literalmente, un elemento sin protección de cuello ese turno."
  },
  {
    "id": "tpp-thl",
    "eyebrow": "Desempeño térmico",
    "titulo": "TPP y THL de capucha: los mínimos no son los del traje",
    "parrafos": [
      "Es un error frecuente comparar el TPP de una capucha contra el del chaquetón. Son piezas distintas con umbrales distintos, y muy pocos fabricantes de capucha publican sus números. INNOTEX sí: declara <strong>THL de 427 y TPP de 22.6</strong> para su GRAY Hood 25, y cita como mínimos aplicables <strong>325 de THL y 20 de TPP</strong>.",
      "Lo valioso de ese dato no es el número aislado: es que el fabricante publica <strong>el suyo y el mínimo contra el que se compara</strong>. Con eso, una evaluación técnica puede pedir el mismo par de cifras a las demás ofertas en lugar de conformarse con “cumple NFPA”."
    ],
    "nota": "Ojo con el balance: subir capas mejora el TPP y <strong>baja el THL</strong> —la capacidad de disipar calor—. Una capucha más protectora térmicamente puede aumentar el estrés por calor del elemento, así que las dos cifras se piden juntas o no dicen nada."
  },
  {
    "id": "declaraciones",
    "eyebrow": "Cómo leer la declaración",
    "titulo": "“Particulate blocking” no es una norma",
    "parrafos": [
      "En esta línea la etiqueta comercial y la declaración normativa se confunden más que en cualquier otra. “Particulate blocking” describe una tecnología, no una certificación, y las referencias del catálogo declaran cosas distintas: dos citan <strong>NFPA 1971 edición 2018</strong>, una cita <strong>NFPA 1970 sin edición</strong> y otra cita <strong>EN 13911:2017</strong> más una categoría de <strong>NFPA 70E</strong> con ATPV de 46 cal/cm².",
      "Ninguna de esas declaraciones es falsa; simplemente no son equivalentes. Y la de NFPA 70E merece una aclaración: es la norma de <strong>seguridad eléctrica en el trabajo</strong>, no la de combate estructural. Un ATPV alto es un dato real de protección contra arco eléctrico, y no sustituye una certificación de conjunto estructural."
    ],
    "tabla": {
      "head": ["Declaración", "Qué es", "Cómo tratarla en una partida"],
      "rows": [
        ["NFPA 1970 · 2025", "Estándar vigente de conjuntos estructurales y de proximidad", "Es la edición que debe citar un certificado emitido hoy"],
        ["NFPA 1971 · 2018", "Edición previa, consolidada en NFPA 1970-2025", "Válida en inventario; en compra nueva se pide constancia de la edición vigente"],
        ["EN 13911:2017", "Norma europea de capuchas para bombero", "Es una referencia distinta a NFPA: no se homologan entre sí"],
        ["NFPA 70E · ATPV", "Seguridad eléctrica en el trabajo, con valor de arco", "Dato adicional real, pero no acredita conjunto estructural"],
        ["“Particulate blocking”", "Descripción de tecnología, no certificación", "Solo sirve acompañada de porcentaje, rango de micras y condición de lavado"]
      ]
    },
    "nota": "Redacción que resuelve las cinco filas de golpe: <strong>“capucha estructural con capa de bloqueo de partículas, certificada bajo la edición vigente de NFPA 1970, con eficiencia declarada de al menos X % en el rango de 0.1 a 1.0 micras y retención documentada después de N lavadas”</strong>."
  },
  {
    "id": "ajuste",
    "eyebrow": "Ajuste e interfaz",
    "titulo": "Bib, drape y el sello de la pieza facial",
    "parrafos": [
      "La mayoría de estas capuchas se surte en <strong>talla universal</strong>, lo que traslada la decisión al bib y al drape: cuánto baja el faldón y cómo se acomoda sobre el hombro. Entre las referencias del catálogo el bib va de 21\" a 23\", y el criterio no es “más largo es mejor” sino que <strong>el traslape se sostenga en movimiento</strong>.",
      "La prueba correcta no es frente al espejo. Se hace con capucha, casco y pieza facial del equipo de respiración puestos, y en las posiciones que producen la falla: levantar los brazos, girar la cabeza, mirar hacia arriba y avanzar en gateo."
    ],
    "lista": [
      {"t": "Traslape con el chaquetón", "d": "Con los brazos arriba, el bib debe seguir cubriendo la zona entre nuca y cuello del chaquetón. Si se levanta y aparece piel, el bib es corto para ese usuario."},
      {"t": "Sello de la pieza facial", "d": "La capucha va <strong>sobre</strong> los bordes de la máscara, no debajo. Un pliegue de capucha atrapado bajo el sello facial es una fuga en ambiente IDLH."},
      {"t": "Apertura facial", "d": "El elástico debe cerrar contra la máscara sin deformarla. Una apertura holgada deja canal de entrada; una demasiado tensa desplaza la careta."},
      {"t": "Audición", "d": "Varias referencias declaran tejido permeable al aire pensado, entre otras cosas, para no comprometer la audición. Es un criterio operativo: el elemento tiene que oír la orden."}
    ]
  },
  {
    "id": "cuidado",
    "eyebrow": "Ciclo de vida",
    "titulo": "Lavado, contaminación y retiro",
    "parrafos": [
      "La capucha es la pieza del conjunto con el ciclo de mantenimiento más corto: se lava después de cada exposición a humo, no cada mes. Y se lava <strong>por separado</strong> del resto del conjunto, siguiendo las instrucciones del fabricante, porque el objetivo es retirar contaminante de la capa que toca la piel.",
      "El límite de una capucha de partículas no es el desgaste visible: es la <strong>pérdida de eficiencia de la capa intermedia</strong>. Por eso la cifra de retención tras lavadas es también un criterio de retiro: cuando el programa supera el número de ciclos que el fabricante documenta, la capucha ya no está haciendo lo que se compró, aunque se vea entera."
    ],
    "lista": [
      {"t": "Lavado por exposición", "d": "Después de cada intervención con humo de combustión, no por calendario. Es la práctica que da sentido a tener dos por elemento."},
      {"t": "Sin calor directo", "d": "Secado a temperatura ambiente. El calor directo degrada laminados y elásticos, que es justo donde vive la función de la capucha."},
      {"t": "Registro de ciclos", "d": "Anotar cuántos lavados acumula cada capucha permite retirarla contra el dato del fabricante y no contra su apariencia."},
      {"t": "Retiro del conjunto", "d": "Como elemento del conjunto estructural, aplica el retiro de <strong>NFPA 1850 (1851)</strong> a los diez años de la fecha de fabricación, más el retiro anticipado por daño o contaminación no removible."}
    ]
  }
]

L3["galeria"] = [
  {"src": "/images/catalogo/1735107673023-1000x750.webp", "alt": "Bombero con capucha aramídica sellando la zona bajo el casco", "caption": "El punto de fuga del conjunto"},
  {"src": "/images/catalogo/1690210795713-600x450.webp", "alt": "Dos bomberos con equipo estructural completo durante una operación", "caption": "Bib sobre el hombro en movimiento"},
  {"src": "/images/catalogo/1606613817012-600x450.webp", "alt": "Bombero equipado junto a la unidad en escena", "caption": "Interfaz con casco y chaquetón"},
  {"src": "/images/catalogo/1756112277157-1000x750.webp", "alt": "Rack con equipo estructural alineado en la estación", "caption": "Dos capuchas por elemento, una en rotación"}
]

L3["aplicaciones"] = [
  {"sector": "Cuerpos de bomberos", "desc": "Dos capuchas por elemento para rotación de lavado, con registro de ciclos y criterio de retiro contra la retención declarada por el fabricante."},
  {"sector": "Brigadas industriales", "desc": "Cuando la brigada entra a ambientes con humo de combustión. La capa de bloqueo de partículas es lo que separa a esta pieza de un pasamontañas retardante."},
  {"sector": "Protección civil", "desc": "Certificado del modelo cotizado con edición vigente, más las cifras de eficiencia, rango de micras y retención por escrito para comprobación de recurso público."}
]

L3["datoClave"] = {
  "titulo": "Pide la eficiencia después de lavar",
  "texto": "Una capucha se lava tras cada exposición: la cifra que importa no es la del material nuevo. <strong>INNOTEX y LION declaran retención después de 100 lavadas; PGI publica 97.4 % nueva y 97.3 % tras 10</strong>. Sin condición de lavado, un porcentaje no se puede comparar."
}

L3["normasRef"] = ["NFPA 1970", "NFPA 1971", "NFPA 1851", "NOM-017-STPS", "EN 469"]

L3["documentacion"] = [
  "Certificado del modelo cotizado con edición normativa vigente",
  "Eficiencia declarada con porcentaje, rango de micras y condición de medición",
  "Retención de eficiencia después del número de lavadas que documente el fabricante",
  "TPP y THL de la capucha cuando el fabricante los publique",
  "Instrucciones de lavado y secado del fabricante, en español donde exista",
  "Factura desglosada por modelo y cantidad, con dos piezas por elemento"
]

L3["blog"] = [
  "capucha-nomex-pbi-proteccion-cuello-cara",
  "mantenimiento-epp-estructural-nfpa-1851",
  "epp-completo-kit-bombero-profesional",
  "nfpa-1971-mexico-norma-bomberos",
  "guia-trajes-estructurales-nfpa-1971",
  "equipar-brigada-industrial-mexico-guia"
]

L3["faqs"] = [
  {
    "q": "¿Qué diferencia real hay entre una capucha clásica y una de bloqueo de partículas?",
    "a": "Una capa. La clásica es tejido de punto aramídico: resiste flama y calor por contacto, pero es permeable por construcción y deja pasar el humo de combustión. La de bloqueo agrega una capa intermedia —Stedair PREVENT o DuPont Nomex Nano Flex, según la marca— entre el exterior y el forro. Por fuera se ven casi iguales y cuestan distinto, así que la única forma de saber qué se está comprando es pedir la construcción por capas y la eficiencia declarada."
  },
  {
    "q": "¿Cómo comparo dos eficiencias de bloqueo?",
    "a": "Con tres datos, no con uno: porcentaje, rango de partícula y condición de medición. INNOTEX declara más de 99 % en el rango de 0.1 a 1.0 micras sostenido incluso después de 100 lavadas; PGI publica 97.4 % en el mismo rango “as received” y 97.3 % después de 10 lavadas; Fire-Dex declara bloqueo desde 0.2 micras sin porcentaje ni condición de lavado en la página consultada. Un porcentaje sin rango y sin condición no se puede poner en una tabla comparativa."
  },
  {
    "q": "¿Por qué insisten en la eficiencia después de lavar?",
    "a": "Porque es la que se usa. Una capucha de partículas se lava después de cada exposición a humo, así que en tres años acumula decenas de ciclos y la cifra del material nuevo describe el primer día. Dos fabricantes del catálogo declaran retención después de 100 lavadas y uno publica el par completo a 10 lavadas. Ese dato es además criterio de retiro: cuando el programa supera los ciclos documentados, la capucha dejó de hacer lo que se compró aunque se vea entera."
  },
  {
    "q": "¿Cuántas capuchas se necesitan por elemento?",
    "a": "Dos, como criterio de programa. Una en servicio y una en rotación de lavado, porque una capucha en la lavadora es un elemento sin protección de cuello ese turno. Es la pieza del conjunto con el ciclo de mantenimiento más corto —se lava por exposición, no por calendario— y también una de las más económicas, así que duplicarla es la decisión de mejor relación costo-protección de todo el ensamble."
  },
  {
    "q": "¿Qué significa que una capucha declare EN 13911 y no NFPA?",
    "a": "Que está certificada contra la norma europea de capuchas para bombero y no contra el esquema NFPA. No es una declaración falsa ni menor, pero no son equivalentes y no deben tratarse como intercambiables en la misma partida. Lo mismo aplica a la categoría NFPA 70E con valor de ATPV que publica una de las referencias: es un dato real de protección contra arco eléctrico, de la norma de seguridad eléctrica en el trabajo, no de combate estructural."
  },
  {
    "q": "¿El TPP de la capucha se compara con el del traje?",
    "a": "No: son piezas distintas con umbrales distintos. Muy pocos fabricantes de capucha publican sus números; INNOTEX declara THL de 427 y TPP de 22.6 para su GRAY Hood 25 y cita como mínimos 325 y 20. Lo útil de ese dato es que permite pedirle el mismo par de cifras a las demás ofertas. Y hay que leerlas juntas: subir capas mejora el TPP y baja el THL, así que una capucha térmicamente más protectora puede aumentar el estrés por calor."
  },
  {
    "q": "¿La capucha va por encima o por debajo de la máscara?",
    "a": "Por encima de los bordes de la pieza facial, nunca debajo. Un pliegue de capucha atrapado bajo el sello facial es una fuga en ambiente IDLH, y es uno de los errores de ajuste más frecuentes en estación. La prueba se hace con capucha, casco y máscara puestos, levantando los brazos, girando la cabeza y avanzando en gateo: lo que se busca es que el bib no se levante y que el elástico cierre contra la máscara sin deformarla."
  },
  {
    "q": "¿Cada cuándo se reemplaza una capucha?",
    "a": "Por dos criterios. El del conjunto: NFPA 1850 (1851) fija el retiro a los diez años de la fecha de fabricación, más el retiro anticipado por daño o contaminación no removible. Y el propio de la capa de partículas: cuando se superan los ciclos de lavado para los que el fabricante documenta retención de eficiencia. Por eso conviene registrar los lavados por pieza: es el único dato que permite retirarla contra evidencia y no contra su apariencia."
  }
]



with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'protector-de-cuello-y-capucha')
# El nombre arranca con el sustantivo que manda. Ademas de leerse mejor, el modulo
# "Productos mencionados" del blog resuelve por la RAIZ del primer sustantivo: con
# "Protector de cuello y capucha" la raiz era "protector" y ningun post de capucha lo
# mencionaba, asi que la ficha no aparecia en ninguno. El slug no se toca.
prod['nombre'] = 'Capuchas y protector de cuello'
prod['l3'] = L3

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('l3 agregado a', prod['slug'])
print('  secciones:', len(L3['secciones']), '| faqs:', len(L3['faqs']),
      '| cards:', len(L3['catalogo']['cards']), '| galeria:', len(L3['galeria']))
print('  seoTitle len:', len(L3['seoTitle']) + len(' | Firefighter.com.mx'),
      '| seoDescription len:', len(L3['seoDescription']))
ids = [s['id'] for s in L3['secciones']]
assert len(ids) == len(set(ids)), 'ids duplicados'
imgs = [c['img'] for c in L3['catalogo']['cards']] + [g['src'] for g in L3['galeria']]
dup = [i for i in set(imgs) if imgs.count(i) > 1]
print('  imagenes repetidas en la pagina:', dup or 'ninguna')
