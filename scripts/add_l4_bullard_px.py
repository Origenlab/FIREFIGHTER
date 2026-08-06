# -*- coding: utf-8 -*-
"""Agrega slug + bloque l4 a la card de la serie Bullard PX (L3 de cascos).

Fuentes primarias consultadas el 2026-08-05:
  - bullard.com/all-products/fire-and-rescue/px-series-fire-helmet/  (coquilla Ultem,
    U-Fit de 36 posiciones, TrakLite, colores, NFPA 1970 ed. 2025)
  - api.bullard.com FH_PX_ReTrak_BIDSPECS_AM_EN_0823_8229.pdf  (dimensiones, cofia con
    deflexion >220 F @ 264 psi, careta PPC 4"x15" ANSI/ISEA Z87.1, orejera, barboquejo,
    garantia; esta hoja todavia cita NFPA 1971)
  - bullard.com/fire-helmets/retrak-series/  (ReTrak: NFPA 1971 / ANSI Z87.1+, series
    compatibles UST, UST-LW, FX y PX)
  - manual de uso del TrakLite  (8 LED blancos de 5 mm + 1 LED azul trasero, 4 pilas AAA
    alcalinas, interruptor rotatorio operable con guante, Clase I Division 2 Grupos A-D)
  - listados de distribuidor con claves reales: PXTLR350, PXWH726B y la base PXS-XX

Eje editorial de la ficha: la PX no se compra por modelo, se compra por configuracion.
Idempotente: reescribe el bloque l4 completo cada vez que se corre.
"""
import json, io, collections

RUTA = 'src/data/productos.json'
SLUG = 'bullard-px-series'

L4 = collections.OrderedDict([
  ("seoTitle", "Casco Bullard PX Series NFPA 1970 · 2025"),
  ("seoDescription", "Casco estructural Bullard PX: coquilla termoplástica, U-Fit de 36 posiciones, visor ReTrak y TrakLite integrado. Configuración y clave por partida en 24 h."),
  ("h1", "Casco estructural Bullard PX Series"),
  ("subtitulo", "La serie contemporánea de Bullard: coquilla termoplástica de alta temperatura de 14\" × 10\" × 6-7/8\", cofia de uretano sobre coquilla interior de alta temperatura, suspensión U-Fit con 36 posiciones de ajuste y protección ocular e iluminación que se eligen por configuración."),
  ("heroImg", {
    "src": "/images/catalogo/1575507371202-600x400.webp",
    "alt": "Cascos estructurales de perfil contemporáneo con visera abatible en la estación",
    "caption": "Serie PX en configuración con careta abatible"
  }),
  ("heroBloques", [
    {
      "label": "Por qué esta serie se especifica por configuración",
      "texto": "La PX no es un casco, es una <strong>plataforma</strong>: sobre la misma coquilla se eligen protección ocular, iluminación integrada, tipo de barboquejo, color de coquilla, color de cinta reflejante y color de orejera. Cada combinación es una clave de producto distinta —<strong>PXWH726B</strong> y <strong>PXTLR350</strong> son la misma serie con configuraciones distintas—, así que una requisición que dice “casco Bullard PX” todavía no describe lo que va a llegar."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "Entregamos la serie con <strong>certificado del modelo cotizado, etiqueta legible y fecha de fabricación por unidad</strong>, más los números de parte de suspensión, orejeras, barboquejo y protección ocular para que la reposición no dependa de nosotros. Propuesta con partidas y clave por configuración en menos de <strong>24 horas hábiles</strong>, con cobertura en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Norma declarada", "valor": "NFPA 1970 · edición 2025"},
    {"label": "Dimensiones", "valor": "14\" × 10\" × 6-7/8\""},
    {"label": "Garantía", "valor": "5 años en coquilla y electrónica"}
  ]),
  ("specStrip", [
    {"label": "Coquilla", "valor": "Termoplástico de alta temperatura"},
    {"label": "Cofia de impacto", "valor": "Uretano sobre coquilla interior"},
    {"label": "Suspensión", "valor": "U-Fit · 36 posiciones"},
    {"label": "Protección ocular", "valor": "Careta 4\", ReTrak o goggles"},
    {"label": "Iluminación", "valor": "TrakLite opcional · 8 LED"},
    {"label": "Perfil", "valor": "Ala trasera acampanada"}
  ]),
])

L4["secciones"] = [
  {
    "id": "la-serie",
    "eyebrow": "Qué estás comprando",
    "titulo": "La PX es una plataforma, no un modelo cerrado",
    "parrafos": [
      "La serie PX es la línea contemporánea de Bullard: perfil recortado, ala trasera acampanada y coquilla termoplástica de alta temperatura. Lo que casi nunca queda claro en una requisición es que <strong>sobre esa misma coquilla se montan seis decisiones independientes</strong>, y que cada combinación de esas seis tiene su propia clave de producto. Dos cascos PX pueden diferir en protección ocular, iluminación, barboquejo y cintas y seguir llamándose igual.",
      "Eso no es un defecto: es lo que permite que un mismo cuerpo de bomberos equipe al personal de máquina y al de rescate con la misma silueta y distinta configuración. Pero convierte la frase “casco Bullard PX” en una descripción incompleta, y una partida incompleta es la que después llega distinta a lo que se aprobó. Es la misma lógica con la que se compran los trajes estructurales por barrera exterior y no por modelo: lo que se cotiza es la configuración."
    ],
    "lista": [
      {"t": "Protección ocular y facial", "d": "Careta abatible de 4\", visor ReTrak retráctil integrado o goggles. No son intercambiables ni cuestan lo mismo, y cambian el ancho exterior del casco porque el herraje va montado a los costados."},
      {"t": "Iluminación integrada", "d": "Con TrakLite o sin TrakLite. Es la decisión que más cambia la clave y la única que introduce componentes electrónicos —y por lo tanto pilas, mantenimiento y una garantía distinta—."},
      {"t": "Barboquejo", "d": "Estándar o con correa de garganta. Los distribuidores lo listan como opción de configuración, no como accesorio: viene definido de fábrica en la clave."},
      {"t": "Color, cinta y orejera", "d": "Coquilla en ocho colores, cinta reflejante en amarillo lima o rojo-naranja, orejera de Nomex en negro o amarillo. Es lo que sostiene el código de color por función y por rango."}
    ],
    "nota": "Las claves reales lo demuestran: <strong>PXWH726B</strong> es una PX blanca con careta de 4\", sin TrakLite y con correa de garganta; <strong>PXTLR350</strong> es la misma serie con TrakLite y visor ReTrak. En la partida va la clave de la configuración, no el nombre de la serie."
  },
  {
    "id": "coquilla",
    "eyebrow": "Coquilla y cofia",
    "titulo": "Termoplástico de alta temperatura y el dato de los 220 °F",
    "parrafos": [
      "Bullard construye la coquilla de la PX en <strong>termoplástico de alta temperatura con el pigmento integrado durante la fabricación</strong>, no pintado encima. Un rayón profundo en una coquilla tintada en masa no deja el material desnudo, que es la diferencia práctica frente a una coquilla pintada: el desgaste se ve menos y el criterio de retiro se apoya en deformación y burbujeo, no en la estética.",
      "Por dentro va lo que realmente absorbe el golpe: una <strong>cofia de espuma de uretano adherida a una coquilla interior negra resistente al calor</strong>, con temperatura de deflexión térmica declarada por encima de <strong>220 °F a 264 psi</strong> y fabricación libre de CFC. Ese número no es resistencia al fuego —es la temperatura a la que el material empieza a ceder bajo carga— y es el que explica por qué la cofia se inspecciona por dentro después de una exposición y no solo se mira la coquilla."
    ],
    "nota": "La cofia y la suspensión son piezas de reposición con número de parte. Un casco cuya coquilla está intacta puede necesitar cofia nueva; retirar la unidad completa cuando lo que falló es un componente reemplazable es presupuesto tirado."
  },
  {
    "id": "dimensiones",
    "eyebrow": "Geometría",
    "titulo": "14\" × 10\" × 6-7/8\" y el ancho que depende de la configuración",
    "parrafos": [
      "Bullard publica las dimensiones exteriores de la PX en su hoja de especificación para licitación, y hay un detalle que casi nadie lee: el ancho de 10 pulgadas está medido <strong>en el herraje de la careta</strong>. Es decir, la dimensión que decide si el casco pasa por una escotilla o estorba dentro de la cabina depende de la protección ocular que se eligió. La comparación natural es contra la UST Traditional de la misma marca, que declara 15-5/8\" de largo y 12\" de ancho."
    ],
    "tabla": {
      "head": ["Dimensión", "Valor publicado", "Por qué importa en operación"],
      "rows": [
        ["Largo", "14\"", "Perfil recortado frente a las 15-5/8\" de la UST Traditional de la misma marca: casi pulgada y media menos de ala, que se nota al girar la cabeza en un espacio confinado."],
        ["Ancho", "10\" en el herraje de la careta", "El ancho lo define el herraje, no la coquilla. Cambiar de careta a visor integrado cambia el perfil lateral del casco."],
        ["Alto", "6-7/8\"", "Determina el espacio libre bajo un dintel o dentro de la cabina con el elemento sentado y equipado."],
        ["Ala trasera", "Acampanada", "Desvía agua y escombro hacia atrás sin la superficie de un ala completa. Es el compromiso central de la silueta contemporánea."]
      ]
    },
    "nota": "Bullard <strong>no publica el peso</strong> de la serie PX en la ficha ni en la hoja de licitación. Si el peso va a ser criterio de evaluación, se pide por escrito para la clave exacta, con protección ocular y TrakLite montados."
  },
  {
    "id": "suspension",
    "eyebrow": "Ajuste",
    "titulo": "U-Fit: 36 posiciones y para qué sirve cada eje",
    "parrafos": [
      "El sistema U-Fit de la PX combina dos ajustes que se suelen confundir en una sola frase de catálogo. La hoja de licitación los describe por separado y conviene copiarlos así en una partida, porque son los que determinan si el casco se puede compartir entre turnos."
    ],
    "lista": [
      {"t": "Corona de seis puntos", "d": "Tres tiras de nylon de 3/4 de pulgada ancladas en seis llaves, más almohadilla de corona. La combinación de posiciones de esas tiras es la que Bullard cuenta como <strong>36 ajustes distintos</strong>: no son 36 tallas, son 36 geometrías de asiento."},
      {"t": "Banda de ratchet", "d": "Ajuste de perímetro operable con guante. Trae cubierta de algodón removible y almohadilla frontal, ambas lavables y con número de parte propio, que es la pieza de higiene del casco."},
      {"t": "Ajuste de altura", "d": "Al menos una pulgada de recorrido mediante tres llaves de altura. Es el eje que mueve el ala frente a los ojos y el que decide si la careta abatida queda a la altura correcta."},
      {"t": "Prueba con el conjunto puesto", "d": "El ajuste se valida con capucha, pieza facial del equipo de respiración y comunicaciones montadas, no con el casco solo. Un asiento correcto en el almacén puede empujar la máscara en cuanto se agrega la capucha."}
    ]
  },
  {
    "id": "ocular",
    "eyebrow": "Protección ocular",
    "titulo": "Careta, ReTrak y goggles: qué certifica realmente cada opción",
    "parrafos": [
      "Las tres opciones de la PX no resuelven el mismo problema, y la diferencia está en la norma que declara cada una. La careta de 4\" × 15\" está declarada contra <strong>ANSI/ISEA Z87.1</strong>; los cascos con visor ReTrak los declara Bullard contra <strong>NFPA 1971 y ANSI/ISEA Z87.1+</strong> —el signo “+” es el requisito de impacto—; los goggles se especifican como componente aparte, con su propio número de parte.",
      "Cumplir Z87.1+ es un requisito de impacto y no convierte a la careta en protección ocular primaria: por la geometría, las partículas entran por abajo y por los costados, y NFPA 1500 reconoce la <strong>pieza facial del equipo de respiración</strong> como protección ocular y facial primaria durante el combate. Para las maniobras sin máscara puesta la respuesta siguen siendo goggles."
    ],
    "tabla": {
      "head": ["Opción", "Lo que declara Bullard", "Para qué sirve en la práctica"],
      "rows": [
        ["Careta abatible de 4\"", "PPC con recubrimiento duro, 4\" × 15\", conforme a ANSI/ISEA Z87.1", "Protección facial frontal contra proyecciones y calor radiante. Es la configuración más común y la más económica de reponer."],
        ["Visor ReTrak integrado", "Cascos con ReTrak conformes a NFPA 1971 y ANSI/ISEA Z87.1+; poliarilato de alta temperatura, operación con una mano, doble eje, desmontable sin herramienta", "Se guarda dentro del casco cuando no se usa, así que no se raya ni se cuelga. Pivota al bajar para no chocar con lentes graduados. Disponible en las series UST, UST-LW, FX y PX."],
        ["Goggles", "ESS FirePro o Inner Zone; opción de policarbonato ventilado de 2.8 mm con tratamiento antiempañante", "La única de las tres que cierra el contorno del ojo. Es la que hay que especificar para ventilación, remoción de escombro y rescate vehicular."]
      ]
    },
    "nota": "En el anexo técnico van <strong>dos renglones separados</strong>: protección facial montada al casco y protección ocular. Escritos como uno solo, el proveedor entrega la careta y la brigada se queda sin goggles."
  },
  {
    "id": "traklite",
    "eyebrow": "Iluminación integrada",
    "titulo": "TrakLite: ocho LED, cuatro pilas AAA y un límite de atmósfera",
    "parrafos": [
      "TrakLite es el sistema de iluminación integrado a la coquilla, compatible con las series UST6, FX, PX y LT. Su manual publica lo que las fichas comerciales resumen en una línea: <strong>ocho LED blancos de 5 mm en el frente y un LED azul de montaje superficial atrás</strong> —el trasero es para seguimiento del binomio, no para iluminar—, con interruptor rotatorio sobredimensionado para operarse con guante estructural puesto.",
      "La parte que cambia decisiones de compra es la alimentación y su restricción: funciona con <strong>cuatro pilas AAA alcalinas de 1.5 V</strong> —el manual nombra las marcas aceptadas— y está declarado apto únicamente para <strong>Clase I, División 2, Grupos A, B, C y D o áreas no peligrosas</strong>. El propio manual advierte que no debe abrirse en un área potencialmente explosiva y que las pilas se cambian en zona conocida como no peligrosa."
    ],
    "lista": [
      {"t": "Ocho LED frontales", "d": "LED blancos de 5 mm de tipo domo montados al frente de la coquilla. Iluminación manos libres: no sustituye la lámpara de intervención, resuelve la tarea inmediata a un brazo de distancia."},
      {"t": "Luz azul trasera", "d": "Un LED azul de montaje superficial en la parte posterior, pensado para que el binomio se ubique en humo. Es función de identificación, no de iluminación."},
      {"t": "Cuatro pilas AAA alcalinas", "d": "El manual pide reemplazar las cuatro al mismo tiempo y no mezclar tipos ni pilas nuevas con usadas. Conviene presupuestar las pilas como consumible del programa, no como accesorio."},
      {"t": "Interruptor rotatorio", "d": "Se gira en sentido de las manecillas para encender. El tamaño está pensado para guante estructural, que es la única prueba de usabilidad que importa en este componente."}
    ],
    "nota": "Para brigadas de planta el dato decisivo es la clasificación: <strong>Clase I División 2</strong> no cubre una atmósfera clasificada como División 1. Si el procedimiento de la instalación exige equipo apto para División 1, este accesorio no es la opción, aunque el casco sí lo sea."
  },
  {
    "id": "claves",
    "eyebrow": "Cómo se pide",
    "titulo": "Las seis decisiones que forman la clave de producto",
    "parrafos": [
      "Los distribuidores publican la PX como una base configurable, y la clave final se genera al elegir opciones. Por eso una partida que no fija las seis decisiones deja la configuración abierta: técnicamente el proveedor puede entregar “casco Bullard PX” cumpliendo la letra de la especificación y no lo que se esperaba."
    ],
    "tabla": {
      "head": ["Decisión", "Opciones publicadas", "Cómo se escribe en la partida"],
      "rows": [
        ["Protección facial y ocular", "Careta de 4\", visor ReTrak integrado o goggles", "“Visor ReTrak integrado, más goggles ESS como partida independiente”, nunca “con protección ocular”"],
        ["Iluminación", "Con TrakLite o sin TrakLite", "“Con sistema de iluminación integrado TrakLite, ocho LED frontales y luz trasera de seguimiento”"],
        ["Barboquejo", "Estándar o con correa de garganta", "“Barboquejo de Nomex con correa de garganta y hebilla de liberación rápida”"],
        ["Color de coquilla", "Blanco, amarillo, rojo, negro, naranja, amarillo lima, verde y azul", "Un color por función o rango, indicando la cantidad por color en la misma partida"],
        ["Cinta reflejante", "Amarillo lima o rojo-naranja", "“Cinta reflejante amarillo lima”, porque es lo que hace comparable la visibilidad entre ofertas"],
        ["Orejera y confort", "Orejera de Nomex negra o amarilla; sistema de confort estándar o FireFit", "“Orejera de Nomex rip-stop de 6 oz, color negro” y el sistema de confort explícito"]
      ]
    },
    "nota": "Además de las seis, en la partida va la <strong>edición normativa vigente</strong>, el certificado del modelo cotizado y los números de parte de las refacciones. Con eso, dos ofertas del mismo precio dejan de ser dos cascos distintos."
  },
  {
    "id": "garantia",
    "eyebrow": "Garantía y refacciones",
    "titulo": "Cinco años de coquilla, diez de componentes y por qué no es lo mismo",
    "parrafos": [
      "Bullard publica para la PX una garantía de <strong>cinco años en la coquilla y en la electrónica</strong>, y una garantía “de vida útil” en los componentes no electrónicos que la propia hoja define como <strong>los diez años de NFPA 1851</strong>. Es una distinción que conviene leer despacio: el componente con menos cobertura temporal es justamente el que se agrega como opción, el TrakLite.",
      "En términos de costo de propiedad eso significa dos cosas. La primera, que un casco con iluminación integrada tiene un componente con horizonte de garantía más corto que el casco. La segunda, que el resto —suspensión, orejeras, barboquejo, cubierta de la banda, almohadilla, careta— se repone por número de parte y esa reposición es la que sostiene el ajuste y la higiene entre inspecciones anuales."
    ],
    "nota": "La garantía no es la vida útil. El retiro de un casco estructural se rige por <strong>NFPA 1850 (1851)</strong>: diez años desde la <strong>fecha de fabricación</strong> de la etiqueta, más el retiro anticipado por impacto o daño. La garantía cubre defectos; el retiro es obligatorio."
  },
  {
    "id": "lo-no-publicado",
    "eyebrow": "Lo que el fabricante no publica",
    "titulo": "Cuatro datos que la PX no trae en la ficha y hay que pedir",
    "parrafos": [
      "Esta serie está mejor documentada que el promedio del mercado —dimensiones, materiales, normas de la careta, descripción de la suspensión—, y aun así hay huecos que importan cuando la compra se evalúa por criterios y no por preferencia. Nombrarlos vale más que rellenarlos: un número inventado es lo que después no se puede sostener en una aclaración de bases."
    ],
    "tabla": {
      "head": ["Dato ausente", "Qué decide", "Cómo se resuelve"],
      "rows": [
        ["Peso de la serie", "Fatiga cervical en turnos largos y comparación contra otras marcas", "Se solicita por escrito para la clave exacta, con protección ocular y TrakLite montados"],
        ["Rango de talla en pulgadas o centímetros", "Si el casco se puede compartir entre turnos y qué personal queda fuera del rango", "Se pide el rango del sistema U-Fit para la configuración cotizada y se valida con prueba de ajuste"],
        ["Lúmenes y autonomía del TrakLite", "Si la luz integrada resuelve la tarea o solo acompaña, y cuántas pilas consume el programa al año", "Se pide salida luminosa y horas de operación continua; entre tanto se presupuestan pilas como consumible"],
        ["Vida útil declarada del casco", "Cuándo sale del inventario si no hubo impacto", "No hay cifra publicada: rige el retiro de NFPA 1850 (1851) a los diez años de la fecha de fabricación"]
      ]
    },
    "nota": "Las cuatro se piden en un solo correo al fabricante, referidas al número de parte cotizado. Nosotros lo gestionamos como parte de la propuesta: <strong>el dato se consigue, no se supone</strong>."
  },
  {
    "id": "edicion",
    "eyebrow": "Edición normativa",
    "titulo": "NFPA 1970 · 2025 en la ficha, NFPA 1971 en la hoja de licitación",
    "parrafos": [
      "En la página de producto Bullard declara la serie PX conforme a <strong>NFPA 1970, edición 2025</strong>, el estándar que consolidó las NFPA 1971, 1975, 1981 y 1982. Su propia hoja de especificación para licitación —la que muchos compradores copian tal cual en el anexo técnico— todavía cita <strong>NFPA 1971</strong> sin edición, porque su última revisión es anterior a la consolidación.",
      "No es una contradicción del producto: es documentación con distinta fecha. Pero sí es un problema si el anexo se redacta copiando la hoja vieja, porque entonces la convocatoria pide una edición sustituida y cualquier oferta puede argumentar que cumple. La transición cerró el <strong>18 de marzo de 2026</strong>."
    ],
    "nota": "Lo exigible hoy: certificado del modelo cotizado <strong>referido a la edición vigente</strong>, con organismo certificador, alcance y número de parte. El inventario ya etiquetado bajo ediciones previas no se invalida —su permanencia en servicio se rige por NFPA 1850 (1851)—, pero una compra nueva no debería nacer citando una edición sustituida."
  }
]

L4["galeria"] = [
  {"src": "/images/catalogo/1690210795713-600x450.webp", "alt": "Dos bomberos con casco estructural de perfil contemporáneo y visera", "caption": "Misma silueta, distinta configuración"},
  {"src": "/images/catalogo/1592235905030-600x450.webp", "alt": "Bombero con pieza facial de equipo de respiración bajo el casco estructural", "caption": "La interfaz que decide el ajuste"},
  {"src": "/images/catalogo/1608723724615-600x450.webp", "alt": "Dos bomberos con casco identificado operando en ambiente con humo", "caption": "Identificación y seguimiento en humo"},
  {"src": "/images/catalogo/1756112277157-1000x750.webp", "alt": "Rack con cascos estructurales alineados en la estación", "caption": "Una clave y una talla por elemento"}
]

L4["aplicaciones"] = [
  {"sector": "Cuerpos de bomberos", "desc": "Silueta contemporánea con código de color por función y refacciones por número de parte. Permite equipar máquina y rescate con la misma serie en configuraciones distintas."},
  {"sector": "Brigadas industriales", "desc": "Para brigadas cuya matriz de riesgo incluya intervención estructural. Si la instalación exige equipo apto para atmósfera División 1, el TrakLite queda fuera del alcance: está declarado para Clase I División 2."},
  {"sector": "Licitación pública", "desc": "Partida cerrada con las seis decisiones de configuración, edición normativa vigente y certificado del modelo cotizado, en lugar de “casco tipo Bullard PX o equivalente”."}
]

L4["datoClave"] = {
  "titulo": "La clave manda, no el nombre de la serie",
  "texto": "<strong>PXWH726B</strong> y <strong>PXTLR350</strong> son las dos la serie PX y no son el mismo casco: cambian protección ocular, iluminación y barboquejo. Pide la clave completa en la propuesta y escríbela en la requisición."
}

L4["referencias"] = [
  {"code": "NFPA 1970 · 2025", "desc": "Edición que Bullard declara hoy para la serie PX en su página de producto. Consolidó NFPA 1971, 1975, 1981 y 1982; la transición cerró el 18 de marzo de 2026."},
  {"code": "NFPA 1971 · sin edición", "desc": "Cita que todavía aparece en la hoja de especificación para licitación de la PX, anterior a la consolidación. No copiarla al anexo técnico sin actualizarla."},
  {"code": "ANSI/ISEA Z87.1", "desc": "Norma de protección ocular y facial declarada para la careta de 4\" × 15\". Los cascos con visor ReTrak se declaran contra Z87.1+, que añade el requisito de impacto."},
  {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento: inspección anual documentada y retiro a los diez años de la fecha de fabricación. Es lo que fija la vida útil, no la garantía."},
  {"code": "Clase I · División 2 · Grupos A-D", "desc": "Clasificación de atmósfera declarada en el manual del TrakLite. No cubre División 1, y las pilas se cambian en área conocida como no peligrosa."}
]

L4["blog"] = [
  "casco-bombero-bullard-usrhb-guia",
  "epp-completo-kit-bombero-profesional",
  "nfpa-1971-mexico-norma-bomberos",
  "mantenimiento-epp-estructural-nfpa-1851",
  "equipar-brigada-industrial-mexico-guia",
  "capucha-nomex-pbi-proteccion-cuello-cara"
]

L4["faqs"] = [
  {
    "q": "¿Qué diferencia hay entre la serie PX y la UST Traditional de Bullard?",
    "a": "Material de coquilla y silueta. La PX es termoplástico de alta temperatura con perfil recortado y ala trasera acampanada, de 14\" × 10\" × 6-7/8\". La UST Traditional es composite de fibra de vidrio con resina termoestable, ala completa y 15-5/8\" × 12\" × 7\": casi pulgada y media más de largo. La UST tiene además una versión LowRider con peso publicado, dato que la PX no trae. En operación, la PX estorba menos en espacios reducidos y la UST desvía mejor agua y escombro."
  },
  {
    "q": "¿Cuánto pesa un casco PX?",
    "a": "Bullard no publica el peso de la serie PX ni en la página de producto ni en la hoja de especificación para licitación, y no lo vamos a inventar. Si el peso es criterio de evaluación se solicita por escrito al fabricante para el número de parte exacto, con protección ocular y TrakLite montados, porque el visor y el módulo de luz cambian la cifra. Como referencia de rango de la categoría, las series de casco estructural con peso publicado están entre 1.4 y 1.8 kg."
  },
  {
    "q": "¿El visor ReTrak sustituye los goggles?",
    "a": "No. Bullard declara los cascos con ReTrak conformes a NFPA 1971 y ANSI/ISEA Z87.1+, lo cual acredita resistencia al impacto, pero un visor montado al casco no cierra el contorno del ojo: las partículas entran por abajo y por los costados. NFPA 1500 reconoce la pieza facial del equipo de respiración como protección ocular y facial primaria durante el combate. Para ventilación, remoción de escombro o rescate vehicular —maniobras sin máscara— se especifican goggles como partida aparte."
  },
  {
    "q": "¿El TrakLite se puede usar en una planta con atmósfera clasificada?",
    "a": "Solo si la clasificación del área es Clase I División 2, Grupos A, B, C o D, o área no peligrosa: eso es lo que declara su manual. No está declarado para División 1. El manual también advierte que el alojamiento no debe abrirse en un área potencialmente explosiva y que el cambio de pilas se hace en zona conocida como no peligrosa. Si el procedimiento de la instalación exige equipo apto para División 1, se cotiza el casco sin TrakLite y la iluminación se resuelve con un equipo con esa clasificación."
  },
  {
    "q": "¿Qué mantenimiento tiene el TrakLite?",
    "a": "Cuatro pilas AAA alcalinas de 1.5 V, que el manual pide reemplazar todas al mismo tiempo, sin mezclar tipos ni pilas nuevas con usadas, y nombrando marcas aceptadas. El procedimiento es limpiar el casco y el alojamiento antes de abrirlo, retirar los dos tornillos de la tapa, colocar las pilas según la polaridad marcada y volver a asegurar la tapa. Conviene presupuestar las pilas como consumible anual del programa y no como accesorio de compra única."
  },
  {
    "q": "¿Qué cubre la garantía y por cuánto tiempo?",
    "a": "Bullard publica cinco años en la coquilla y en la electrónica, y garantía de vida útil en los componentes no electrónicos, definida en la propia hoja como los diez años de NFPA 1851. Vale leerlo con cuidado: el componente con horizonte más corto es el que se agrega como opción, el TrakLite. Y la garantía no es la vida útil: el retiro del casco se rige por NFPA 1850 (1851), a los diez años de la fecha de fabricación de la etiqueta, más el retiro anticipado por impacto."
  },
  {
    "q": "¿Qué refacciones se cambian sin reemplazar el casco?",
    "a": "Suspensión completa, banda de ratchet, cubierta de algodón de la banda, almohadilla frontal, almohadilla de corona, barboquejo, orejera de Nomex rip-stop de 6 oz con su forro de franela y la protección ocular. Todas tienen número de parte y se piden por separado. Reponer suspensión y orejeras es lo que sostiene el ajuste y la higiene entre inspecciones anuales; cambiar el casco completo por un componente desgastado es presupuesto tirado."
  },
  {
    "q": "¿Cómo se escribe la partida para que llegue exactamente esta configuración?",
    "a": "Se fijan las seis decisiones —protección facial, protección ocular en renglón aparte, iluminación, barboquejo, color de coquilla y de cinta reflejante, orejera y sistema de confort— más la edición normativa vigente, el organismo certificador, el certificado del modelo cotizado, los números de parte de refacciones y la fecha de fabricación por unidad. Nosotros entregamos la propuesta ya desglosada así, con la clave por configuración y la cantidad por color."
  }
]



with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'cascos-bullard-y-msa')
card = next(c for c in prod['l3']['catalogo']['cards']
            if c['marca'] == 'Bullard' and c['modelo'] == 'PX Series')
card['slug'] = SLUG
# El botón de la card dice "Ver ficha de {fichaLabel}". Sin este campo diría
# "Ver ficha de Termoplástico", que es el material, no la serie.
card['fichaLabel'] = 'la serie PX'
card['l4'] = L4

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('l4 agregado a', card['marca'], card['modelo'], '→', SLUG)
print('  secciones:', len(L4['secciones']), '| faqs:', len(L4['faqs']),
      '| galeria:', len(L4['galeria']), '| referencias:', len(L4['referencias']))
print('  seoTitle len:', len(L4['seoTitle']) + len(' | Firefighter.com.mx'))
print('  seoDescription len:', len(L4['seoDescription']))
ids = [s['id'] for s in L4['secciones']]
assert len(ids) == len(set(ids)), 'ids duplicados: %s' % ids
RESERVADOS = {'ficha', 'galeria', 'sectores', 'preguntas', 'configuraciones', 'catalogo'}
choque = RESERVADOS & set(ids)
assert not choque, 'id reservado por la plantilla: %s' % choque
imgs = [g['src'] for g in L4['galeria']]
assert len(imgs) == len(set(imgs)), 'foto repetida en la galeria'
palabras = sum(len(p.split()) for s in L4['secciones']
               for p in list(s.get('parrafos', [])) + [i['d'] for i in s.get('lista', [])] + [s.get('nota', '')])
print('  palabras del cuerpo (aprox):', palabras)
