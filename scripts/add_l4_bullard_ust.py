# -*- coding: utf-8 -*-
"""Agrega slug + bloque l4 a la card Bullard UST Traditional (L3 de cascos).

Fuentes primarias consultadas el 2026-08-05:
  - api.bullard.com FH_UST_BIDSPECS_AM_EN_LOW_8226.pdf  (composite de fibra de vidrio con
    resina termoestable, acabado hard coat de poliester, beading elastomerico reforzado con
    aluminio con clip de laton y D-ring, cofia de uretano sobre coquilla interior con
    deflexion >220 F @ 264 psi, corona de tres tiras sobre seis llaves, ratchet con ajuste
    trasero de altura, 15-5/8" x 12" x 7", careta PPC 4"x15", goggles de policarbonato
    ventilado de 2.8 mm, orejera de Nomex rip-stop 6 oz, barboquejo de dos tramos,
    garantia de 5 anos en coquilla y de vida util —10 anos NFPA 1851— en el resto)
  - notas de lanzamiento del UST LowRider (Firehouse y Fire Apparatus): 49.3 a 54.4 oz
    (1.4 a 1.5 kg), perfil mas bajo que la UST estandar, "cups the back of the head",
    U-Fit de 36 posiciones, FireFit, TrakLite, ReTrak, NFPA 1970 edicion 2025
  - listado de distribuidor del LowRider: acabado super matte, configuracion estandar con
    trim amarillo lima, orejera de Nomex negra y portafrente de 6" Maple Leaf
  - ~/Documents/Claude/Projects/LGACONTRAINCENDIOS/src/data/productos/cascoBombero.mjs

Eje editorial: el ala completa es una decision de ingenieria, no de nostalgia, y la propia
serie UST resuelve el peso y el centro de gravedad con tres perfiles distintos.
Idempotente: reescribe el bloque l4 completo cada vez que se corre.
"""
import json, io, collections

RUTA = 'src/data/productos.json'
SLUG = 'bullard-ust-traditional'

L4 = collections.OrderedDict([
  ("seoTitle", "Casco Bullard UST Traditional NFPA 1970"),
  ("seoDescription", "Casco tradicional Bullard UST: composite de fibra de vidrio con resina termoestable, ala completa de 15-5/8\", beading de aluminio y tres perfiles de serie."),
  ("h1", "Casco estructural Bullard UST Traditional"),
  ("subtitulo", "La tradicional de ala completa de Bullard: coquilla de composite de fibra de vidrio con resina termoestable de 15-5/8\" × 12\" × 7\", borde elastomérico reforzado con aluminio, cofia de uretano sobre coquilla interior de alta temperatura y tres perfiles dentro de la misma serie."),
  ("heroImg", {
    "src": "/images/catalogo/1638401607229-1000x750.webp",
    "alt": "Casco estructural tradicional de ala completa con protección facial en escena",
    "caption": "Silueta tradicional de ala completa"
  }),
  ("heroBloques", [
    {
      "label": "Por qué el ala completa sigue siendo una decisión técnica",
      "texto": "La silueta tradicional se discute como si fuera nostalgia y en realidad es <strong>geometría</strong>: el ala completa forma una cuenca que manda agua, brasa y escombro hacia atrás y afuera del cuello del chaquetón, y el composite termoestable aporta la rigidez para sostener ese voladizo. Lo que se paga por eso son <strong>1-5/8 de pulgada más de largo y 2 pulgadas más de ancho</strong> que un perfil recortado de la misma marca. La pregunta correcta no es cuál se ve mejor: es qué maniobra domina el turno."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "Entregamos la serie con <strong>certificado del modelo cotizado, etiqueta legible y fecha de fabricación por unidad</strong>, y con los números de parte de suspensión, orejeras, barboquejo, borde y protección ocular, porque en un casco tradicional la reposición del borde y del portafrente es parte del mantenimiento. Propuesta con partidas y acabado definido en menos de <strong>24 horas hábiles</strong>, con cobertura en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Norma declarada", "valor": "NFPA 1970 · edición 2025"},
    {"label": "Dimensiones", "valor": "15-5/8\" × 12\" × 7\""},
    {"label": "Peso del LowRider", "valor": "1.4 a 1.5 kg publicados"}
  ]),
  ("specStrip", [
    {"label": "Coquilla", "valor": "Composite con resina termoestable"},
    {"label": "Acabado", "valor": "Hard coat de poliéster"},
    {"label": "Borde", "valor": "Elastomérico con refuerzo de aluminio"},
    {"label": "Suspensión", "valor": "Corona de seis llaves + ratchet"},
    {"label": "Protección ocular", "valor": "Tres opciones documentadas"},
    {"label": "Perfiles de la serie", "valor": "Traditional · LW · LowRider"}
  ]),
])

L4["secciones"] = [
  {
    "id": "la-tradicional",
    "eyebrow": "Qué estás comprando",
    "titulo": "El ala completa es una cuenca, no un adorno",
    "parrafos": [
      "En un casco tradicional el ala no termina en la nuca: la rodea. Esa continuidad forma una <strong>cuenca de escurrimiento</strong> que dirige el agua de la propia línea de ataque, la brasa y el escombro fino hacia atrás y hacia los costados, en vez de dejarlos caer entre el casco y el cuello del chaquetón. Es la razón por la que la mayoría de los cuerpos que trabajan interior con línea siguen especificando ala completa, y la razón por la que la silueta sobrevivió a cuatro generaciones de materiales.",
      "El costo de esa geometría es volumen y voladizo. Un ala que sobresale necesita una coquilla rígida que la sostenga sin flexionar, y ahí entra el composite de fibra de vidrio con resina termoestable: más rígido que un termoplástico, y por eso mismo la familia que Bullard usa para su línea tradicional."
    ],
    "lista": [
      {"t": "Ala continua con cuenca trasera", "d": "Deriva agua y escombro fuera del cuello del chaquetón. Es lo que gana el ala completa y lo que se pierde al recortar el perfil."},
      {"t": "Composite de fibra de vidrio", "d": "Resina termoestable con el color integrado y acabado hard coat de poliéster resistente a la flama. Rigidez para el voladizo del ala y comportamiento estable tras exposiciones repetidas."},
      {"t": "Borde reforzado con aluminio", "d": "El perímetro del ala lleva un beading elastomérico con refuerzo de aluminio, sujeto con clip de latón y D-ring. Es pieza estructural y de mantenimiento, no terminación estética."},
      {"t": "Portafrente y marcaje", "d": "La configuración estándar del perfil LowRider incluye portafrente de 6\" tipo Maple Leaf; hay portafrentes de cuero como opción. Es donde vive la identificación de compañía y de mando."}
    ],
    "nota": "La serie UST no es un solo casco: Bullard la ofrece en <strong>tres perfiles</strong> —Traditional, UST-LW y LowRider— que resuelven el mismo problema de peso y equilibrio de forma distinta. La comparación está más abajo, y es la decisión que más conviene tomar antes de pedir precio."
  },
  {
    "id": "composite",
    "eyebrow": "Material de coquilla",
    "titulo": "Composite termoestable: qué gana y qué cuesta frente al termoplástico",
    "parrafos": [
      "La coquilla es <strong>fibra de vidrio con una resina termoestable retardante de flama</strong>, con el pigmento integrado en el moldeo y una capa exterior de polvo de poliéster con acabado hard coat. “Termoestable” es la palabra clave: a diferencia de un termoplástico, la resina cura de forma irreversible y no vuelve a ablandarse con temperatura, lo que sostiene la rigidez del ala en exposiciones repetidas.",
      "Lo que cuesta es volumen y precio de reposición. Un composite de este tipo se repone más caro que una coquilla termoplástica y suma dimensiones. Por eso Bullard mantiene las dos familias en catálogo: quien prioriza rigidez y silueta tradicional se queda en composite; quien prioriza perfil recortado y reposición económica se va al termoplástico."
    ],
    "nota": "Si el criterio de compra es peso y maniobra en espacio reducido, la comparación honesta no es contra otra marca: es contra el <strong>casco Bullard PX Series</strong>, la misma marca en termoplástico y perfil recortado. Los dos están certificados; resuelven turnos distintos."
  },
  {
    "id": "borde",
    "eyebrow": "El detalle que nadie especifica",
    "titulo": "El borde del ala: la pieza que se golpea primero",
    "parrafos": [
      "La hoja de especificación describe el perímetro del ala como un <strong>beading elastomérico reforzado con aluminio</strong>, fijado con un clip de latón y un D-ring. Suena a detalle de acabado y es lo contrario: el borde es lo primero que golpea un marco de puerta, lo que raspa contra el piso cuando el casco se apoya y lo que absorbe el impacto lateral que no llega a la coquilla.",
      "En una compra por volumen conviene pedir su número de parte junto con el de la suspensión y las orejeras. Un borde levantado o con el refuerzo expuesto es criterio de reposición inmediata: deja de proteger el canto del composite y empieza a acumular contaminantes en el hueco. Ninguna especificación de licitación que hayamos revisado en México lo menciona, y es una refacción de bajo costo que alarga la vida útil real del casco."
    ]
  },
  {
    "id": "perfiles",
    "eyebrow": "Los tres perfiles",
    "titulo": "Traditional, UST-LW y LowRider: la misma serie, tres respuestas",
    "parrafos": [
      "Bullard resolvió por iteración el problema clásico del casco tradicional —peso y centro de gravedad alto— sin abandonar la silueta. El resultado son tres perfiles de la misma serie. Elegir entre ellos es una decisión previa a pedir precio, porque cambian el peso publicado, la altura de uso y el interior."
    ],
    "tabla": {
      "head": ["Perfil", "Lo que publica Bullard", "Para quién"],
      "rows": [
        ["UST Traditional", "Composite de fibra de vidrio con resina termoestable, 15-5/8\" × 12\" × 7\", tres opciones de protección ocular. No publica peso.", "Cuerpos con silueta tradicional normada que priorizan rigidez y cuenca completa, y para los que el peso no es criterio de evaluación escrito."],
        ["UST-LW", "Plataforma ligera de la misma serie tradicional. Es la base sobre la que Bullard construyó el LowRider.", "Quien quiere ala completa con menos carga que la Traditional y no necesita el perfil bajo."],
        ["UST LowRider", "49.3 a 54.4 oz —1.4 a 1.5 kg—, altura de uso más baja, diseño que “abraza” la parte posterior de la cabeza, U-Fit de 36 posiciones, sistema FireFit, acabado super matte y NFPA 1970 edición 2025.", "Turnos largos y maniobra interior donde el equilibrio y la carga cervical sí se evalúan. Es el único perfil de la serie con peso publicado."]
      ]
    },
    "nota": "El peso de <strong>1.4 a 1.5 kg</strong> del LowRider es, hasta donde hemos verificado, el único peso que Bullard publica en toda su línea de casco estructural. Si el anexo técnico va a evaluar peso, ese perfil es el que se puede sostener con un número de fabricante."
  },
  {
    "id": "geometria",
    "eyebrow": "Cuánto ocupa",
    "titulo": "Lo que cuesta el ala completa, en pulgadas",
    "parrafos": [
      "Comparar siluetas con adjetivos no lleva a ninguna decisión. Bullard publica las dimensiones exteriores de sus dos familias, así que la diferencia se puede poner en números y contra la maniobra real: escotilla, interior de vehículo, gateo en espacio reducido y giro de cabeza con pieza facial puesta."
    ],
    "tabla": {
      "head": ["Dimensión", "UST Traditional", "PX Series (termoplástico)", "Diferencia"],
      "rows": [
        ["Largo", "15-5/8\"", "14\"", "1-5/8\" más de ala en la tradicional: es la cuenca trasera"],
        ["Ancho", "12\"", "10\" en el herraje de la careta", "2\" más de silueta: se nota al girar la cabeza entre obstáculos"],
        ["Alto", "7\"", "6-7/8\"", "Prácticamente igual: la diferencia de la tradicional no es altura, es superficie"],
        ["Peso publicado", "No publicado en la Traditional · 1.4 a 1.5 kg en el LowRider", "No publicado", "Solo un perfil de una de las dos familias tiene cifra de fabricante"]
      ]
    },
    "nota": "La lectura correcta de la tabla: la tradicional no es “más grande” en todas las direcciones, es <strong>más ancha y con más ala</strong>. Si la restricción operativa es altura libre, las dos siluetas son equivalentes; si es paso lateral, no."
  },
  {
    "id": "suspension-y-confort",
    "eyebrow": "Ajuste e higiene",
    "titulo": "Corona de seis llaves, ratchet y el interior de una pieza",
    "parrafos": [
      "La suspensión de la serie está descrita con precisión en la hoja de licitación, y conviene copiarla así en una partida en lugar de reducirla a un número de puntos. El interior, además, es la parte del casco que más contamina y la que decide si la descontaminación se hace de verdad o se pospone."
    ],
    "lista": [
      {"t": "Corona sobre seis llaves", "d": "Tres tiras de nylon de 3/4 de pulgada ancladas en seis llaves de nylon. En el perfil LowRider, Bullard cuenta 36 posiciones de ajuste del sistema U-Fit sobre esa misma arquitectura."},
      {"t": "Banda de ratchet con ajuste de altura", "d": "Ajuste de perímetro operable con guante, más un ajustador trasero de altura con al menos una pulgada de recorrido en tres llaves. El eje de altura es el que fija dónde queda el ala frente a los ojos."},
      {"t": "Sistema FireFit", "d": "Interior de una sola pieza con liberación rápida, estándar en el LowRider. Se retira completo para lavarlo, que es la diferencia entre un programa de descontaminación que se cumple y uno que existe en papel. La prueba de ajuste, en cambio, se hace con capucha puesta: el interior limpio cambia el volumen."},
      {"t": "Orejera y barboquejo", "d": "Orejera de Nomex rip-stop de 6 oz con tres capas de franela retardante; barboquejo de dos tramos de 3/4 de pulgada en Nomex con hebilla de liberación rápida y corredera tipo postman, con extensión de al menos 24 pulgadas."}
    ]
  },
  {
    "id": "ocular",
    "eyebrow": "Protección ocular",
    "titulo": "Tres opciones, y cómo el ala cambia su uso",
    "parrafos": [
      "La UST Traditional se documenta con tres opciones de protección ocular, y el ala completa modifica cómo se usan: da sombra sobre la careta —lo que ayuda con el reflejo y estorba con poca luz— y obliga a que el visor retráctil se guarde en un espacio que ya está ocupado por la geometría del ala.",
      "La regla de fondo no cambia respecto al resto de la línea: una careta montada al casco protege la cara de proyecciones frontales pero no cierra el contorno del ojo. Cuando el elemento trae la pieza facial del equipo de respiración, esa es su protección ocular primaria; para las maniobras sin máscara se especifican goggles, con su propio número de parte y en renglón aparte."
    ],
    "lista": [
      {"t": "Careta de 4\" × 15\"", "d": "Policarbonato PPC con recubrimiento duro, ópticamente correcta, declarada contra ANSI/ISEA Z87.1. Es la opción más común y la más económica de reponer cuando se raya."},
      {"t": "Visor ReTrak", "d": "Poliarilato de alta temperatura, operación con una mano y desmontable sin herramienta. Bullard lo ofrece en UST, UST-LW, FX y PX, y declara los cascos con ReTrak contra NFPA 1971 y ANSI/ISEA Z87.1+."},
      {"t": "Goggles ventilados", "d": "Policarbonato de 2.8 mm con tratamiento antiempañante y ventilación. La única de las tres que sella el contorno del ojo para ventilación, remoción y rescate vehicular."}
    ]
  },
  {
    "id": "configuracion",
    "eyebrow": "Cómo se pide",
    "titulo": "Acabado, frente y trim: lo que define una tradicional",
    "parrafos": [
      "En un casco tradicional la configuración no es solo funcional: el acabado, el portafrente y el color del trim son lo que hace reconocible a una corporación en escena. Y todo eso se define en la orden, no después."
    ],
    "tabla": {
      "head": ["Decisión", "Opciones publicadas", "Cómo se escribe en la partida"],
      "rows": [
        ["Perfil de la serie", "Traditional, UST-LW o LowRider", "“Perfil LowRider” cuando el peso se evalúa; “Traditional” cuando la silueta está normada por procedimiento"],
        ["Acabado", "Gloss o super matte —estándar en el LowRider—", "“Acabado super matte”, porque cambia la apariencia y el criterio de inspección visual"],
        ["Color de coquilla y trim", "Coquilla en blanco, rojo, amarillo o negro; trim reflejante amarillo lima de serie", "Cantidad por color, indicando el color por función o rango"],
        ["Portafrente", "6\" tipo Maple Leaf de serie; portafrentes de cuero opcionales", "“Portafrente de 6\" con número de unidad y nombre de la corporación”, especificando si lleva cuero"],
        ["Protección ocular", "Careta de 4\", visor ReTrak o goggles", "Dos renglones: protección facial montada al casco y protección ocular, nunca uno solo"],
        ["Iluminación y barboquejo", "TrakLite opcional; barboquejo estándar o con correa de garganta", "“Con TrakLite” y “barboquejo con correa de garganta” explícitos: van definidos en la clave"]
      ]
    },
    "nota": "Súmale la <strong>edición normativa vigente</strong>, el certificado del modelo cotizado, el número de parte del borde y de la orejera, y la fecha de fabricación por unidad. Con eso la partida deja de admitir “equivalentes” que no lo son."
  },
  {
    "id": "lo-no-publicado",
    "eyebrow": "Lo que el fabricante no publica",
    "titulo": "Cuatro huecos de la Traditional y cómo cerrarlos",
    "parrafos": [
      "La hoja de licitación de la serie es de las más completas del mercado en materiales y construcción, y aun así hay datos que no están. Decirlo es parte del trabajo: un número inventado es exactamente lo que no se sostiene en una aclaración de bases ni en una inconformidad."
    ],
    "tabla": {
      "head": ["Dato ausente", "Qué decide", "Cómo se resuelve"],
      "rows": [
        ["Peso de la UST Traditional", "Carga cervical en turnos largos y comparación entre perfiles", "Se pide por escrito para la clave cotizada; si el peso va a evaluarse, el perfil LowRider sí tiene cifra publicada"],
        ["Rango de talla en pulgadas o centímetros", "Si el casco se comparte entre turnos y quién queda fuera del rango", "Se solicita el rango del sistema de ajuste para la configuración cotizada y se valida con prueba de ajuste"],
        ["Espesor de la coquilla por zona", "Comparación técnica frente a fabricantes que sí lo publican por corona y ala", "Se pide el espesor nominal por zona; MSA lo publica para su tradicional, así que es un dato exigible en una comparativa"],
        ["Vida útil declarada del casco", "Cuándo sale del inventario si no hubo impacto", "No hay cifra de fabricante: rige el retiro de NFPA 1850 (1851) a los diez años de la fecha de fabricación"]
      ]
    },
    "nota": "Los cuatro se piden en un solo correo referido al número de parte cotizado, y los gestionamos como parte de la propuesta. Lo que no hacemos es rellenar el hueco con el dato de otro perfil de la misma serie: <strong>el peso del LowRider es del LowRider</strong>."
  },
  {
    "id": "mantenimiento",
    "eyebrow": "Ciclo de vida",
    "titulo": "Qué se inspecciona en un composite y qué cubre la garantía",
    "parrafos": [
      "Un composite termoestable no se deforma como un termoplástico: avisa distinto. Lo que hay que buscar en la inspección anual documentada es <strong>decoloración por calor, burbujeo o levantamiento del acabado, fibras expuestas en el canto del ala y borde con el refuerzo visible</strong>, además del estado del interior, del barboquejo y del portafrente. Un golpe absorbido puede comprometer la cofia sin dejar marca en la coquilla.",
      "Del lado comercial, Bullard publica <strong>cinco años de garantía en la coquilla</strong> y garantía de vida útil en los componentes no electrónicos, que su propia hoja define como los diez años de NFPA 1851. Es cobertura por defecto de fabricación, no una autorización para usar el casco más tiempo."
    ],
    "nota": "El retiro se rige por <strong>NFPA 1850 (1851)</strong>: diez años desde la fecha de fabricación de la etiqueta, más el retiro anticipado por impacto o daño. Antes de reemplazar la unidad completa conviene revisar si lo que falló es borde, interior, orejera o suspensión: las cuatro son refacciones con número de parte."
  }
]

L4["galeria"] = [
  {"src": "/images/catalogo/1735107673023-600x400.webp", "alt": "Bombero de perfil con casco tradicional de ala completa", "caption": "El perfil que define la serie"},
  {"src": "/images/catalogo/1606613817012-600x450.webp", "alt": "Casco de ala completa visto desde atrás junto a la unidad", "caption": "La cuenca trasera en uso"},
  {"src": "/images/catalogo/1563062067-bb-600x450.webp", "alt": "Bombero con casco rojo y equipo de respiración autónoma de perfil", "caption": "Color por función y mando"},
  {"src": "/images/catalogo/1575507371089-600x450.webp", "alt": "Chaquetones y cascos estructurales colgados en la estación", "caption": "Una clave y un acabado por corporación"}
]

L4["aplicaciones"] = [
  {"sector": "Cuerpos de bomberos", "desc": "Para corporaciones con la silueta tradicional normada por procedimiento. El portafrente de 6\" sostiene número de unidad e identificación de mando, y el borde es refacción de bajo costo."},
  {"sector": "Brigadas industriales", "desc": "Cuando la matriz de riesgo contempla intervención estructural con línea. Si la maniobra dominante es paso lateral en espacios reducidos, conviene evaluar antes el perfil recortado de la misma marca."},
  {"sector": "Licitación pública", "desc": "Partida cerrada por perfil de la serie, acabado, color, trim, portafrente, protección facial y ocular en renglones separados, y certificado del modelo cotizado con edición vigente."}
]

L4["datoClave"] = {
  "titulo": "El peso es de un perfil, no de la serie",
  "texto": "Los <strong>1.4 a 1.5 kg</strong> publicados corresponden al perfil <strong>LowRider</strong>, no a la Traditional. Si el anexo técnico evalúa peso, especifica ese perfil: es el único de la línea con cifra de fabricante que se puede sostener por escrito."
}

L4["referencias"] = [
  {"code": "NFPA 1970 · 2025", "desc": "Edición declarada por Bullard para la serie, incluida la aprobación del perfil LowRider. Consolidó NFPA 1971, 1975, 1981 y 1982; la transición cerró el 18 de marzo de 2026."},
  {"code": "NFPA 1971 · sin edición", "desc": "Cita que todavía aparece en la hoja de especificación para licitación de la serie UST, anterior a la consolidación. No copiarla al anexo técnico sin actualizarla."},
  {"code": "ANSI/ISEA Z87.1", "desc": "Norma declarada para la careta de 4\" × 15\". Los cascos con visor ReTrak se declaran contra Z87.1+, que añade el requisito de impacto."},
  {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento: inspección anual documentada y retiro a los diez años de la fecha de fabricación. Es lo que fija la vida útil, no la garantía."},
  {"code": "NOM-115-STPS", "desc": "Cascos de protección industrial: especificaciones, métodos de prueba y criterios de retiro. Es otra categoría de producto y no se homologa con un casco estructural."}
]

L4["blog"] = [
  "casco-bombero-bullard-usrhb-guia",
  "mantenimiento-epp-estructural-nfpa-1851",
  "epp-completo-kit-bombero-profesional",
  "nfpa-1971-mexico-norma-bomberos",
  "brigadas-voluntarias-equipamiento-esencial",
  "capucha-nomex-pbi-proteccion-cuello-cara"
]

L4["faqs"] = [
  {
    "q": "¿Cuál es la diferencia entre UST Traditional, UST-LW y UST LowRider?",
    "a": "Son tres perfiles de la misma serie tradicional. La Traditional es la referencia de la familia: composite de fibra de vidrio con resina termoestable, 15-5/8\" × 12\" × 7\" y tres opciones de protección ocular, sin peso publicado. La UST-LW es la plataforma ligera de esa misma silueta y la base sobre la que Bullard construyó el tercer perfil. El LowRider monta más bajo, abraza la parte posterior de la cabeza, trae U-Fit de 36 posiciones, sistema FireFit y acabado super matte, y es el único con peso publicado: 49.3 a 54.4 oz, es decir 1.4 a 1.5 kg."
  },
  {
    "q": "¿El ala completa sirve de algo o es tradición?",
    "a": "Sirve, y es medible en operación aunque no en una tabla: el ala continua forma una cuenca que manda agua de la línea, brasa y escombro fino hacia atrás y afuera del cuello del chaquetón. Eso es lo que se pierde al recortar el perfil. Lo que cuesta es volumen: 1-5/8 de pulgada más de largo y 2 pulgadas más de ancho que el perfil termoplástico de la misma marca. Si la maniobra dominante es interior con línea, el ala gana; si es paso lateral en espacios muy reducidos, el perfil recortado gana."
  },
  {
    "q": "¿Cuánto pesa la UST Traditional?",
    "a": "Bullard no publica el peso de la Traditional, y no lo vamos a estimar a partir del peso de otro perfil. El único dato de fabricante en la serie es el del LowRider: 49.3 a 54.4 oz (1.4 a 1.5 kg). Si el peso va a formar parte de la evaluación, hay dos caminos honestos: especificar el perfil LowRider, que tiene cifra publicada, o pedir el peso por escrito al fabricante para la clave exacta de la Traditional con protección ocular y accesorios montados."
  },
  {
    "q": "¿Qué es el beading del ala y por qué hay que pedir su número de parte?",
    "a": "Es el perímetro del ala: un beading elastomérico reforzado con aluminio, sujeto con clip de latón y D-ring. No es terminación estética, es la pieza que golpea primero contra marcos de puerta y la que se raspa cuando el casco se apoya. Un borde levantado o con el refuerzo expuesto deja de proteger el canto del composite y acumula contaminantes en el hueco, así que es criterio de reposición. Es una refacción de bajo costo que alarga la vida útil real del casco, y prácticamente ninguna especificación mexicana la contempla."
  },
  {
    "q": "¿Se le puede poner portafrente de cuero y águila?",
    "a": "El fabricante ofrece portafrente de 6\" como parte de la configuración —tipo Maple Leaf en el estándar del LowRider— y portafrentes de cuero como opción, así que la vía correcta es pedirlo configurado de fábrica y con número de parte. Sobre accesorios que no vengan del fabricante, el criterio es simple: el certificado se emite sobre el casco tal como se ensambla, así que cualquier pieza añadida debe estar autorizada por escrito antes de montarla en un casco en servicio."
  },
  {
    "q": "¿Conviene acabado gloss o super matte?",
    "a": "Es decisión de imagen y de inspección, no de protección. El super matte —estándar en el perfil LowRider— disimula mejor el rayón superficial y da un aspecto de uso más uniforme en la flota; el gloss mantiene la apariencia tradicional y hace más evidente cualquier marca. Para el programa de inspección conviene lo que permita ver la superficie: sobre acabado brillante se detectan antes el burbujeo y el levantamiento del recubrimiento, que son criterios de retiro."
  },
  {
    "q": "¿La UST acepta TrakLite y visor ReTrak?",
    "a": "Sí. El manual del TrakLite lista compatibilidad con las series UST6, FX, PX y LT, y el visor ReTrak está disponible en UST, UST-LW, FX y PX. Dos advertencias que sí importan: el TrakLite trae componentes electrónicos, así que introduce pilas AAA como consumible y una garantía distinta a la de la coquilla, y está declarado únicamente para Clase I División 2 o áreas no peligrosas, lo que lo descarta en instalaciones que exijan equipo apto para División 1."
  },
  {
    "q": "¿Cómo se escribe la partida de una UST Traditional?",
    "a": "Perfil de la serie, material de coquilla, dimensiones, acabado, color de coquilla y de trim reflejante, portafrente con el marcaje solicitado, protección facial y protección ocular en renglones separados, barboquejo, iluminación si aplica, edición normativa vigente, organismo certificador, certificado del modelo cotizado, números de parte de suspensión, orejera y borde, y fecha de fabricación por unidad. Nosotros entregamos la propuesta ya desglosada así, con cantidad por color y acabado."
  }
]



with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'cascos-bullard-y-msa')
card = next(c for c in prod['l3']['catalogo']['cards']
            if c['marca'] == 'Bullard' and c['modelo'] == 'UST Traditional')
card['slug'] = SLUG
card['fichaLabel'] = 'la UST Traditional'
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
assert not (RESERVADOS & set(ids)), 'id reservado: %s' % (RESERVADOS & set(ids))
imgs = [g['src'] for g in L4['galeria']]
assert len(imgs) == len(set(imgs)), 'foto repetida en la galeria'
palabras = sum(len(p.split()) for s in L4['secciones']
               for p in list(s.get('parrafos', [])) + [i['d'] for i in s.get('lista', [])] + [s.get('nota', '')])
print('  palabras del cuerpo (aprox):', palabras)
