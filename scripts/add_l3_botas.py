# -*- coding: utf-8 -*-
"""Agrega el bloque l3 a botas-dielectricas (EPP para Bomberos).

Fuente primaria consolidada: ~/Documents/Claude/Projects/LGACONTRAINCENDIOS/src/data/
productos/botasBombero.mjs (revisada 2026-07-20), con 9 referencias de fabricante:
HAIX Fire Hero Xtreme / Fire Flash Xtreme / Fire Eagle Xtreme / Fire Eagle Air,
Black Diamond X2 y 16" Rubber, LION-Thorogood QR14, Croydon FILTREX y RESCUE (linea SKOLD).

Eje editorial: "dielectrica" no significa lo que la mayoria cree. Una bota estructural declara
resistencia electrica de ENSAYO (18 kV, 14 kV) y no equivale a calzado dielectrico industrial
de uso permanente. A partir de ahi, los cuatro datos que si diferencian: altura de cana,
puntera, sistema de ANCHO y paquete normativo.

Idempotente. Si se corre despues de agregar fichas L4 a esta L3, hay que volver a correrlas.
"""
import json, io, collections

RUTA = 'src/data/productos.json'

L3 = collections.OrderedDict([
  ("seoTitle", "Botas estructurales para bombero NFPA 1970"),
  ("seoDescription", "Botas estructurales HAIX, Black Diamond y Croydon: caña de 11 a 16 pulgadas, puntera compuesta o de acero, anchos publicados y barrera CROSSTECH."),
  ("h1", "Botas estructurales para bombero, de 11 a 16 pulgadas"),
  ("subtitulo", "Calzado de protección para combate estructural con caña de 11\" a 16\", puntera compuesta o de acero, plantilla antipunción, barrera CROSSTECH y sistemas de ancho publicados por el fabricante: la talla sin ancho declarado no resuelve el calce."),
  ("heroImg", {
    "src": "/images/catalogo/1651368615152-1000x750.webp",
    "alt": "Rack de equipo de bombero con botas estructurales y trajes por turno",
    "caption": "Botas asignadas por elemento, con talla y ancho"
  }),
  ("heroBloques", [
    {
      "label": "Por qué la especificación importa",
      "texto": "En una estructura incendiada el piso concentra los riesgos que nadie ve: clavo, varilla expuesta, vidrio y cable bajo el agua. Una <strong>bota estructural</strong> responde con puntera, plantilla antipunción, barrera de humedad y suela con resistencia eléctrica <strong>medida en ensayo</strong>. Ese último punto es el más malentendido del rubro: <strong>“dieléctrica” no significa calzado para trabajo eléctrico permanente</strong>, y confundir las dos categorías es lo que aparece en verificación."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "Distribuimos <strong>HAIX, Black Diamond y Croydon</strong> con levantamiento de <strong>talla y ancho por usuario</strong>, no solo curva de tallas, y con certificado del modelo cotizado, etiqueta y edición normativa por escrito. Entregamos <strong>propuesta técnica en menos de 24 horas hábiles</strong> y equipamos cuerpos de bomberos, brigadas industriales y unidades de protección civil en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Altura de caña", "valor": "De 11\" a 16\" según modelo"},
    {"label": "Retiro obligatorio", "valor": "10 años desde fabricación"}
  ]),
  ("specStrip", [
    {"label": "Altura de caña", "valor": "11\", 13\", 14\" o 16\""},
    {"label": "Puntera", "valor": "Compuesta o de acero"},
    {"label": "Barrera", "valor": "CROSSTECH según modelo"},
    {"label": "Plantilla", "valor": "Antipunción de acero o composite"},
    {"label": "Anchos", "valor": "Narrow, Medium y Wide o Multi-Fit"},
    {"label": "Cierre", "valor": "Pull-on o agujetas de Nomex"}
  ]),
])

L3["catalogo"] = collections.OrderedDict([
  ("eyebrow", "Catálogo por marca"),
  ("titulo", "Botas estructurales<br>por marca y modelo"),
  ("intro", "Entre estas referencias cambian cuatro cosas que deciden la compra: <strong>altura de caña, tipo de puntera, sistema de ancho y paquete normativo declarado</strong>. Ninguna de las cuatro se deduce de la foto ni del precio. Cada card reproduce lo que publica el fabricante, con la declaración normativa tal cual la escribe —incluidas las que citan ediciones ya sustituidas—."),
  ("imgRef", "Imagen de referencia de la línea"),
  ("nota", "Las declaraciones no están homologadas y aquí se conservan literales: <strong>Black Diamond ya publica la nomenclatura consolidada NFPA 1970 (1971)-2025</strong>, mientras HAIX declara NFPA 1971-2018 con normas adicionales por modelo y Croydon FILTREX declara certificación UL bajo NFPA 1971-18. Un caso que conviene conocer: la <strong>Croydon RESCUE</strong> de la misma línea se declara “fabricada bajo los requerimientos de la Norma NTC 1741”, que es una <strong>norma colombiana y no una certificación NFPA</strong>; no debe tratarse como equivalente en la misma partida. La LION-Thorogood QR14 declara barrera GORE CROSSTECH de triple capa pero <strong>no publica altura de caña</strong> en la fuente consultada. Verificación por modelo: etiqueta, organismo certificador, edición y certificado del modelo cotizado."),
  ("cards", [
    {
      "marca": "HAIX",
      "modelo": "Fire Hero Xtreme",
      "variante": "13\" pull-on",
      "varianteLabel": "Caña y cierre",
      "badge": "NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1651368615152-600x400.webp",
      "alt": "Rack de equipo con botas estructurales y chaquetones listos por turno",
      "desc": "La referencia con el tallaje más completo del catálogo: <strong>tallas 5 a 16 con medias tallas y tres anchos</strong> —Narrow, Medium y Wide—. Caña de 13\", puntera compuesta, barrera CROSSTECH y resistencia eléctrica declarada de 18 kV en ensayo de fabricante.",
      "specs": [
        "Caña de 13\" con sistema pull-on",
        "Puntera compuesta y barrera CROSSTECH",
        "Tallas 5 a 16 con medias tallas",
        "Anchos Narrow, Medium y Wide"
      ],
      "chip": "18 kV declarados en ensayo · claves 507101 H / 507102 M"
    },
    {
      "marca": "HAIX",
      "modelo": "Fire Flash Xtreme",
      "variante": "13\" con agujetas",
      "varianteLabel": "Caña y cierre",
      "badge": "NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1563062067-9d-600x450.webp",
      "alt": "Bombero con equipo estructural completo abriendo un acceso metálico",
      "desc": "La única del catálogo con <strong>agujetas de Nomex y puntera de acero</strong>, en lugar de pull-on y puntera compuesta. Es la opción cuando el procedimiento exige cierre ajustable. Caña de 13\" y resistencia eléctrica declarada de 14 kV en ensayo.",
      "specs": [
        "Agujetas de Nomex, cierre ajustable",
        "Puntera de acero",
        "Caña de 13\"",
        "Paquete normativo con NFPA 1951 y 1977"
      ],
      "chip": "14 kV declarados en ensayo · claves 506005 / 506006"
    },
    {
      "marca": "HAIX",
      "modelo": "Fire Eagle Xtreme",
      "variante": "14\" metatarsal",
      "varianteLabel": "Caña y protección",
      "badge": "NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1633540440007-600x450.webp",
      "alt": "Bombero forzando un acceso con herramienta de mango largo",
      "desc": "Caña de 14\" con <strong>protección metatarsal y de espinilla</strong>, y sistema <strong>Vario Wide Fit con tres plantillas</strong> para ajustar volumen sin cambiar de talla. Declara el paquete normativo más amplio de la tabla: estructural, química, rescate técnico y forestal.",
      "specs": [
        "Caña de 14\" con protección metatarsal",
        "Vario Wide Fit con tres plantillas",
        "Paquete cuádruple declarado por HAIX",
        "Barrera CROSSTECH"
      ],
      "chip": "Un paquete largo no siempre es el correcto · verifica tareas"
    },
    {
      "marca": "Black Diamond",
      "modelo": "X2 Leather",
      "variante": "14\" Multi-Fit",
      "varianteLabel": "Caña y ajuste",
      "badge": "NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1690210795620-600x450.webp",
      "alt": "Bombero con equipo estructural completo sujetando una herramienta de mango largo",
      "desc": "La única referencia del catálogo que <strong>ya declara la nomenclatura consolidada NFPA 1970 (1971)-2025</strong>. Caña de 14\" en piel, sistema pull-on y <strong>Multi-Fit System</strong>: un mismo par cubre medium, wide y extra wide. Tallas 5 a 15.",
      "specs": [
        "Declara NFPA 1970 (1971) edición 2025",
        "Caña de 14\" en piel, sistema pull-on",
        "Multi-Fit System: medium, wide y extra wide",
        "Tallas 5 a 15"
      ],
      "chip": "La única ya migrada a la edición vigente · clave 2772025"
    },
    {
      "marca": "Black Diamond",
      "modelo": "16\" Rubber",
      "variante": "16\" de caucho",
      "varianteLabel": "Caña y material",
      "badge": "NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1759673824678-600x400.webp",
      "alt": "Bombero con equipo autónomo saliendo de una estructura durante una maniobra",
      "desc": "La caña <strong>más alta del catálogo</strong> —16\"— en caucho vulcanizado: se calza en segundos, resiste mejor la inmersión y protege más espinilla. Es la referencia con la <strong>curva de tallas más amplia</strong>: 3 a 16, en tres anchos.",
      "specs": [
        "Caña de 16\" en caucho vulcanizado",
        "Tallas 3 a 16 en tres anchos",
        "Declara NFPA 1970 (1971) edición 2025",
        "Calzado y descalzado rápido"
      ],
      "chip": "La más alta y la de curva de tallas más amplia · clave 6991625"
    },
    {
      "marca": "Croydon",
      "modelo": "FILTREX",
      "variante": "14\" línea SKÖLD",
      "varianteLabel": "Caña y línea",
      "badge": "UL · NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1503714964235-600x450.webp",
      "alt": "Bombero revisando y ajustando su equipo de protección antes de salir",
      "desc": "La única de la línea SKÖLD con <strong>certificación de tercera parte declarada por UL</strong>, y la única del catálogo que <strong>publica peso</strong>: 3,661 g por par. Caña de 14\" (35.5 cm), con paquete UL bajo NFPA 1971-18, NFPA 1990-2022, ASTM F2413-18 y CSA Z195-14.",
      "specs": [
        "Certificación UL declarada por el fabricante",
        "Peso publicado: 3,661 g por par",
        "Caña de 14\" · 35.5 cm",
        "Paquete con ASTM F2413 y CSA Z195"
      ],
      "chip": "La única con peso publicado y certificación de tercera parte"
    }
  ])
])

L3["secciones"] = [
  {
    "id": "dielectrica",
    "eyebrow": "Nomenclatura",
    "titulo": "Qué significa —y qué no— que una bota sea “dieléctrica”",
    "parrafos": [
      "En el mercado mexicano esta línea se pide casi siempre como “bota dieléctrica”, y ahí empieza la confusión. Una bota estructural declara <strong>resistencia eléctrica medida en un ensayo específico</strong> —HAIX publica 18 kV para la Fire Hero Xtreme y 14 kV para la Fire Flash Xtreme—, y eso <strong>no equivale a calzado dieléctrico para trabajo eléctrico permanente</strong>. Son dos categorías de producto con propósitos distintos.",
      "La distinción importa por dos razones. La primera es de seguridad: un valor de ensayo describe el comportamiento del calzado nuevo, seco y limpio en condiciones de laboratorio, no una garantía de aislamiento con la suela mojada, contaminada con hidrocarburos o desgastada. La segunda es de cumplimiento: si el puesto exige calzado dieléctrico bajo <strong>NOM-113-STPS</strong> para tarea eléctrica, una bota estructural no lo sustituye, y viceversa."
    ],
    "lista": [
      {"t": "Bota estructural", "d": "Diseñada para combate de incendio: exposición térmica, punción, aplastamiento, agua e hidrocarburos, con barrera de humedad y caña alta que traslapa con el pantalón. Declara resistencia eléctrica como resultado de ensayo."},
      {"t": "Calzado dieléctrico industrial", "d": "Diseñado para el riesgo eléctrico del puesto según NOM-113-STPS. No está evaluado para calor radiante sostenido ni para las tareas mecánicas del combate estructural."},
      {"t": "Bota forestal", "d": "Otra categoría más: prioriza ligereza, tracción en pendiente y transpirabilidad. No se compra con criterio estructural ni al revés."}
    ],
    "nota": "Cómo se escribe bien en una partida: <strong>“bota estructural con resistencia eléctrica declarada de X kV según ensayo del fabricante”</strong>, en lugar de “bota dieléctrica”. La primera se puede verificar contra un documento; la segunda deja a interpretación qué se está comprando."
  },
  {
    "id": "anatomia",
    "eyebrow": "Anatomía de la bota",
    "titulo": "Las cuatro protecciones que trabajan a la vez",
    "parrafos": [
      "Una bota estructural es un ensamble, no una pieza. Cada capa responde a un riesgo distinto del piso de una estructura incendiada, y las cuatro pueden especificarse por separado en la orden. Cuando una requisición dice solo “bota de bombero”, está dejando tres de las cuatro al criterio del proveedor.",
      "El orden en que fallan también es distinto: la suela y el corte se ven, la plantilla y la barrera se degradan por dentro. Los hidrocarburos y el calor pueden comprometer la suela <strong>sin cambiar su apariencia</strong>, que es la razón por la que la inspección no puede ser solo visual."
    ],
    "lista": [
      {"t": "Corte y caña", "d": "Piel o caucho vulcanizado, de 11\" a 16\" de altura. La caña define protección de espinilla, facilidad de calzado y cómo traslapa con el pantalón del traje estructural para que no quede zona expuesta."},
      {"t": "Barrera de humedad", "d": "Varias referencias declaran CROSSTECH; la LION-Thorogood QR14 declara GORE CROSSTECH de triple capa. Es la capa que impide que el agua de la línea y los contaminantes lleguen al pie sin bloquear la salida del vapor."},
      {"t": "Plantilla antipunción", "d": "Acero o composite. Es la que responde al clavo y la varilla, que son el riesgo más frecuente del piso de un incendio estructural y el que más lesiones evitables produce."},
      {"t": "Puntera y suela", "d": "Puntera compuesta o de acero contra aplastamiento; suela con dibujo para superficie mojada y escombro, y con la resistencia eléctrica declarada en ensayo."}
    ]
  },
  {
    "id": "altura",
    "eyebrow": "Altura de caña",
    "titulo": "De 11 a 16 pulgadas: qué cambia con cada pulgada",
    "parrafos": [
      "La altura es la decisión más visible y la que más se toma por costumbre. Entre las referencias consultadas hay botas de 11\", 13\", 14\" y 16\", y la diferencia no es solo cuánta espinilla queda cubierta: cambia la movilidad del tobillo, el peso, la facilidad de calzado y cómo se comporta la interfaz con el pantalón."
    ],
    "tabla": {
      "head": ["Altura", "Referencias", "Qué gana", "Qué cuesta"],
      "rows": [
        ["11\"", "HAIX Fire Eagle Air", "La más baja y ligera de la línea consultada: menos carga en jornada larga y más movilidad de tobillo", "Menos protección de espinilla y menor traslape con el pantalón"],
        ["13\"", "HAIX Fire Hero Xtreme · Fire Flash Xtreme", "El equilibrio más común en combate estructural, con el tallaje y los anchos mejor documentados", "Nada relevante: es el punto medio que la mayoría de los cuerpos especifica"],
        ["14\"", "HAIX Fire Eagle Xtreme · Black Diamond X2 · Croydon FILTREX", "Más espinilla cubierta y espacio para protección metatarsal", "Más peso y algo menos de flexión de tobillo"],
        ["16\"", "Black Diamond 16\" Rubber", "La más alta: mejor comportamiento en inmersión y calzado en segundos", "La más voluminosa; el caucho es menos transpirable que la piel"]
      ]
    },
    "nota": "La altura se decide contra la maniobra dominante y contra el pantalón que ya tiene la corporación, no en abstracto. Y conviene escribirla en pulgadas en la partida: “caña alta” no es una medida."
  },
  {
    "id": "ancho",
    "eyebrow": "El dato que decide el calce",
    "titulo": "Una talla correcta con ancho incorrecto sigue siendo inservible",
    "parrafos": [
      "Este es el error más caro de una dotación de calzado y el más fácil de evitar: hacer el tallaje sin levantar el ancho. Los fabricantes resuelven el volumen del pie de formas que <strong>no son equivalentes entre sí</strong>, así que “talla 9” significa cosas distintas según la referencia.",
      "El resultado de no definirlo es predecible: botas que le aprietan a la mitad del turno, botas que bailan en el talón al subir escalera, y un porcentaje del pedido que termina sin usarse. Ninguno de esos problemas se arregla después de la entrega."
    ],
    "tabla": {
      "head": ["Sistema publicado", "Referencia", "Cómo resuelve el volumen"],
      "rows": [
        ["Anchos Narrow, Medium y Wide", "HAIX Fire Hero Xtreme", "Tres hormas distintas. Se pide talla y ancho por usuario: son claves diferentes, no una opción de ajuste"],
        ["Vario Wide Fit con tres plantillas", "HAIX Fire Eagle Xtreme", "Una horma con tres plantillas de distinto grosor: el volumen se ajusta en la estación, sin cambiar de clave"],
        ["Multi-Fit System", "Black Diamond X2", "Un mismo par cubre medium, wide y extra wide, lo que simplifica el levantamiento cuando no hay tiempo de medir uno por uno"],
        ["Tres anchos por talla", "Black Diamond 16\" Rubber", "Curva de 3 a 16 con tres anchos: la combinación más amplia del catálogo para plantillas grandes"]
      ]
    },
    "nota": "Protocolo de prueba que sí sirve: con el <strong>calcetín de trabajo real y el pantalón puesto</strong>, verificar calzado y descalzado rápido, flexión de tobillo, holgura en el empeine, sujeción del talón al subir escalera y ausencia de roce en la espinilla. Se registra <strong>talla y ancho por usuario</strong> en su expediente."
  },
  {
    "id": "paquete-normativo",
    "eyebrow": "Cómo leer la declaración",
    "titulo": "Un paquete normativo largo no siempre es el paquete correcto",
    "parrafos": [
      "Varias referencias declaran más de una norma a la vez, y es fácil leer esa lista como “mejor producto”. No siempre lo es: cada norma adicional responde a una tarea distinta —protección química, rescate técnico, forestal— y ampliar el paquete por costumbre encarece la partida sin mejorar la protección del uso real.",
      "Lo que sí hay que verificar es la <strong>edición</strong>. La referencia vigente para calzado estructural es <strong>NFPA 1970 (1971) edición 2025</strong>, que consolidó las normas anteriores y cuya transición cerró el 18 de marzo de 2026. En este catálogo solo Black Diamond declara ya esa nomenclatura; el resto cita ediciones previas."
    ],
    "tabla": {
      "head": ["Referencia normativa", "Qué cubre", "Cuándo pedirla"],
      "rows": [
        ["NFPA 1970 (1971) · 2025", "Conjuntos estructurales y de proximidad, incluido el calzado", "Siempre: es la edición vigente y la que debe citar un certificado emitido hoy"],
        ["NFPA 1990 (1992)", "Protección química", "Solo si el usuario atiende incidentes con materiales peligrosos como tarea real"],
        ["NFPA 1951 · NFPA 1977", "Rescate técnico y protección forestal", "Solo si la unidad hace rescate técnico o combate forestal con el mismo calzado"],
        ["CSA Z195 · ASTM F2413", "Calzado de protección canadiense y estadounidense", "Como refuerzo mecánico declarado; no sustituyen la certificación NFPA cuando la especificación la exige"],
        ["NTC 1741", "Norma colombiana de calzado", "No es una declaración NFPA. Si aparece en una oferta, hay que tratarla como categoría distinta"]
      ]
    },
    "nota": "La pregunta correcta al proveedor no es “¿cumple NFPA?” sino <strong>“¿qué organismo certificó qué modelo, bajo qué norma, en qué edición, y me lo entregas por escrito?”</strong>. Croydon FILTREX declara certificación UL; otras referencias declaran conformidad sin nombrar organismo."
  },
  {
    "id": "peso",
    "eyebrow": "Carga sobre el usuario",
    "titulo": "El peso que casi nadie publica",
    "parrafos": [
      "En una bota, el peso se paga en cada paso: es la parte del ensamble que el elemento levanta miles de veces por turno. Y aun así, de las nueve referencias que revisamos <strong>solo Croydon publica peso por par</strong>: 3,661 g la FILTREX y 3,225 g la RESCUE. HAIX, Black Diamond y LION-Thorogood no lo publican en las fuentes consultadas.",
      "Eso deja al comprador con dos caminos honestos si el peso va a ser criterio de evaluación en una licitación: pedirlo por escrito al fabricante para la clave exacta —con la talla de referencia, porque el peso cambia con la talla— o especificar la referencia que sí lo publica. Lo que no funciona es estimarlo: una diferencia de 300 gramos por par es real en fatiga y no se puede inventar."
    ],
    "nota": "Cuando pidas peso, pídelo <strong>por par y con la talla de referencia indicada</strong>. Un peso “por bota” o sin talla no se puede comparar entre marcas."
  },
  {
    "id": "ciclo-de-vida",
    "eyebrow": "Ciclo de vida",
    "titulo": "Secado, hidrocarburos y retiro de servicio",
    "parrafos": [
      "La bota es el elemento del conjunto que más se moja y el que peor se seca. Dos prácticas comunes la destruyen antes de tiempo: el <strong>secado forzado con calor directo</strong> —radiador, calefactor, sol directo prolongado—, que endurece el corte y degrada adhesivos, y guardarla húmeda, que ataca el forro y la barrera.",
      "El otro riesgo es invisible: la exposición a <strong>hidrocarburos, calor o contaminación puede degradar la suela sin cambiar su apariencia</strong>. Una suela que se ve entera puede haber perdido tracción y resistencia. Por eso la inspección incluye flexionar la suela y revisar el desprendimiento en el enfranque, no solo mirar el dibujo."
    ],
    "lista": [
      {"t": "Qué se revisa antes y después del uso", "d": "Cortes, deformación o endurecimiento del material, estado de suela y tacón, integridad de la puntera, costuras, forro interior, agujetas cuando existan, plantillas y legibilidad de la etiqueta."},
      {"t": "Secado correcto", "d": "A temperatura ambiente, con circulación de aire y con la plantilla retirada. Nunca con calor directo. Un par de repuesto por elemento es lo que permite secar sin dejar a nadie sin bota."},
      {"t": "Plantillas como consumible", "d": "Se reponen por número de parte y son la pieza de higiene del calzado. En una dotación grande conviene presupuestar plantillas de repuesto desde el primer año."},
      {"t": "Retiro de servicio", "d": "Rige <strong>NFPA 1850 (1851)</strong>: diez años desde la fecha de fabricación, más el retiro anticipado por daño, endurecimiento, delaminación de suela o contaminación no removible."}
    ]
  }
]

L3["galeria"] = [
  {"src": "/images/catalogo/1776648120640-1000x750.webp", "alt": "Vestidor de estación con equipo estructural completo colgado y botas en el piso", "caption": "Un par asignado por elemento"},
  {"src": "/images/catalogo/1606613817012-600x450.webp", "alt": "Bombero equipado junto a la unidad en escena", "caption": "Interfaz con el pantalón estructural"},
  {"src": "/images/catalogo/1690210795713-600x450.webp", "alt": "Dos bomberos con equipo estructural completo durante una operación", "caption": "Tracción en superficie mojada"},
  {"src": "/images/catalogo/1608723724615-600x450.webp", "alt": "Bomberos operando en ambiente con humo durante una maniobra", "caption": "El piso es el riesgo que no se ve"}
]

L3["aplicaciones"] = [
  {"sector": "Cuerpos de bomberos", "desc": "Asignación por usuario con talla y ancho registrados, par de repuesto para rotación de secado y plantillas como consumible presupuestado."},
  {"sector": "Brigadas industriales", "desc": "Selección que distingue bota estructural de calzado dieléctrico NOM-113-STPS y de bota forestal. Si el puesto tiene riesgo eléctrico permanente, el calzado de ese riesgo es otro producto."},
  {"sector": "Protección civil", "desc": "Curva de tallas con ancho declarado, certificado del modelo cotizado con edición vigente y factura desglosada por modelo, talla y ancho para comprobación de recurso público."}
]

L3["datoClave"] = {
  "titulo": "Levanta el ancho, no solo la talla",
  "texto": "Los sistemas de ancho <strong>no son equivalentes entre marcas</strong>: hay tres hormas (Narrow, Medium, Wide), una horma con tres plantillas y un Multi-Fit que cubre tres anchos. Una talla correcta con ancho incorrecto sigue produciendo calzado inservible."
}

L3["normasRef"] = ["NFPA 1970", "NFPA 1971", "NOM-113-STPS", "NFPA 1851", "NOM-017-STPS"]

L3["documentacion"] = [
  "Certificado del modelo cotizado con edición normativa vigente",
  "Organismo certificador nombrado, no solo la mención de la norma",
  "Ficha técnica con altura de caña, puntera, barrera y sistema de ancho",
  "Curva de tallas y anchos confirmada contra el levantamiento por usuario",
  "Números de parte de plantillas y agujetas de repuesto",
  "Procedimiento de secado e inspección, y factura desglosada por talla y ancho"
]

L3["blog"] = [
  "botas-bombero-haix-fire-flash-guia",
  "botas-guantes-bomberos-nfpa-1971",
  "epp-completo-kit-bombero-profesional",
  "mantenimiento-epp-estructural-nfpa-1851",
  "nfpa-1971-mexico-norma-bomberos",
  "equipar-brigada-industrial-mexico-guia"
]

L3["faqs"] = [
  {
    "q": "¿Una bota estructural sirve como calzado dieléctrico para trabajo eléctrico?",
    "a": "No, son categorías distintas. Una bota estructural declara resistencia eléctrica obtenida en un ensayo específico —HAIX publica 18 kV en la Fire Hero Xtreme y 14 kV en la Fire Flash Xtreme—, y ese valor describe el comportamiento del calzado nuevo, seco y limpio en laboratorio. No es una garantía de aislamiento con la suela mojada, contaminada o desgastada, ni sustituye al calzado dieléctrico que exige la NOM-113-STPS para un puesto con riesgo eléctrico. Si el riesgo eléctrico es permanente, ese calzado es otro producto."
  },
  {
    "q": "¿Qué altura de caña conviene: 11, 13, 14 o 16 pulgadas?",
    "a": "Depende de la maniobra dominante y del pantalón que ya usa la corporación. Las 13\" son el punto medio más común en combate estructural y la altura con el tallaje mejor documentado. Las 14\" ganan protección de espinilla y permiten protección metatarsal. Las 16\" en caucho se calzan en segundos y aguantan mejor la inmersión, a costa de volumen y transpirabilidad. Las 11\" son las más ligeras y móviles, con menos espinilla cubierta. Conviene escribir la medida en pulgadas en la partida: “caña alta” no es una medida."
  },
  {
    "q": "¿Por qué insisten tanto en el ancho y no solo en la talla?",
    "a": "Porque los sistemas de ancho no son equivalentes entre marcas y una talla correcta con ancho incorrecto sigue siendo calzado inservible. HAIX publica anchos Narrow, Medium y Wide en la Fire Hero Xtreme —tres hormas distintas, tres claves— y un Vario Wide Fit con tres plantillas en la Fire Eagle Xtreme; Black Diamond declara un Multi-Fit System con el que un par cubre medium, wide y extra wide. Nosotros levantamos talla y ancho por usuario y lo registramos, porque después de la entrega ya no se arregla."
  },
  {
    "q": "¿Puntera de acero o compuesta?",
    "a": "Las dos protegen contra aplastamiento; la diferencia está en peso, comportamiento térmico y detección en arcos de seguridad. La mayoría de las referencias del catálogo declara puntera compuesta, más ligera y sin puente térmico. La HAIX Fire Flash Xtreme es la excepción documentada con puntera de acero, y también la única con agujetas de Nomex en lugar de sistema pull-on: ese par de datos suele decidir la compra cuando el procedimiento exige cierre ajustable."
  },
  {
    "q": "¿Cuánto pesa un par de botas estructurales?",
    "a": "De las nueve referencias que revisamos, solo Croydon publica peso: 3,661 g por par la FILTREX y 3,225 g por par la RESCUE. HAIX, Black Diamond y LION-Thorogood no lo publican en las fuentes consultadas, y no lo vamos a estimar. Si el peso va a ser criterio de evaluación, se pide por escrito al fabricante para la clave exacta, por par y con la talla de referencia indicada, porque un peso sin talla no se puede comparar entre marcas."
  },
  {
    "q": "¿Qué significa que un modelo declare cuatro normas a la vez?",
    "a": "Que el fabricante lo evaluó para varias tareas: la HAIX Fire Eagle Xtreme declara estructural, química, rescate técnico y forestal. Un paquete largo no es automáticamente mejor: cada norma adicional responde a un uso distinto y ampliar el paquete por costumbre encarece la partida sin mejorar la protección del uso real. Lo que sí hay que verificar siempre es la edición, y ahí el dato relevante es que solo Black Diamond declara ya la nomenclatura consolidada NFPA 1970 (1971)-2025."
  },
  {
    "q": "¿Cómo se secan y cada cuándo se reemplazan?",
    "a": "A temperatura ambiente, con circulación de aire y con la plantilla retirada: nunca con calor directo, porque endurece el corte y degrada adhesivos. Un par de repuesto por elemento es lo que permite secar sin dejar a nadie sin bota. El retiro se rige por NFPA 1850 (1851): diez años desde la fecha de fabricación, más retiro anticipado por endurecimiento, delaminación de suela o contaminación no removible. Ojo con la suela: los hidrocarburos y el calor la degradan sin cambiar su apariencia."
  },
  {
    "q": "¿Qué documentación entregan para una licitación de botas?",
    "a": "Certificado del modelo cotizado con la edición normativa vigente y el organismo certificador nombrado, etiqueta y ficha técnica con altura de caña, puntera, barrera y sistema de ancho, curva de tallas y anchos confirmada contra el levantamiento por usuario, números de parte de plantillas y agujetas de repuesto, procedimiento de secado e inspección, carta de distribuidor autorizado y factura desglosada por modelo, talla y ancho. Si la convocatoria pide un formato específico, lo armamos con ese formato."
  }
]



with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'botas-dielectricas')
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
