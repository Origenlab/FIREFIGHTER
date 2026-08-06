# -*- coding: utf-8 -*-
"""Agrega slug + bloque l4 a la card Bullard LT Series (L3 de cascos).

Fuentes primarias consultadas el 2026-08-06:
  - api.bullard.com FH_LT_USERMANUAL_AM_EN_0520_6027006129J.pdf  (modelos LTX y LTG4X,
    termoplastico contemporaneo, U-Fit con 12 ajustes: pestanas A/B/C para altura de uso y
    postes 1/2 para balance adelante-atras; careta R330 de 4" PPC con recubrimiento duro;
    ensambles de goggle IZ4 y FP4 con herraje Quick-Attach; limpieza con detergente suave;
    retiro tras impacto aunque no haya dano visible; declara NFPA 1971)
  - bullard.com: la pagina de producto de la serie declara NFPA 1970 edicion 2025
  - manual del TrakLite: compatibilidad con UST6, FX, PX y LT

OJO: la ficha consolidada del proyecto LGA afirmaba que el manual del LT esta en espanol.
Al verificar el PDF, lo unico en espanol es la advertencia de la Propuesta 65 de California.
El manual de fabricante que SI existe traducido es el de la serie UST. La card L3 del LT se
corrigio en add_l3_cascos.py.

Eje editorial: el ajuste se documenta por eje —altura y balance por separado—, que es lo que
convierte una dotacion por volumen en una dotacion que de verdad ajusta.
Idempotente. Correr DESPUES de add_l3_cascos.py.
"""
import json, io, collections

RUTA = 'src/data/productos.json'
SLUG = 'bullard-lt-series'

L4 = collections.OrderedDict([
  ("seoTitle", "Casco Bullard LT Series LTX y LTG4X"),
  ("seoDescription", "Casco estructural Bullard LT Series: termoplástico contemporáneo, U-Fit de 12 posiciones en dos ejes, Quick-Attach para careta y goggles. Cotiza en 24 h."),
  ("h1", "Casco estructural Bullard LT Series"),
  ("subtitulo", "La serie ligera de Bullard en sus modelos LTX y LTG4X: coquilla termoplástica de perfil contemporáneo, suspensión U-Fit con 12 posiciones repartidas en dos ejes —altura de uso y balance adelante-atrás— y herraje Quick-Attach para cambiar careta o goggles sin herramienta."),
  ("heroImg", {
    "src": "/images/catalogo/1690210795713-600x450.webp",
    "alt": "Bomberos con casco estructural de perfil contemporáneo durante una operación",
    "caption": "La serie ligera en operación"
  }),
  ("heroBloques", [
    {
      "label": "Por qué esta serie sirve para dotar por volumen",
      "texto": "Cuando hay que equipar veinte, cincuenta o cien elementos, el casco que gana no es el más completo: es el que <strong>ajusta a más cabezas, se limpia rápido y se repone barato</strong>. La LT resuelve las tres cosas con una coquilla termoplástica de perfil contemporáneo, un sistema Quick-Attach que cambia la protección ocular sin herramienta y —esto es lo distintivo— un ajuste que el fabricante documenta <strong>eje por eje</strong> en lugar de venderlo como un número de posiciones."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "Entregamos la serie con <strong>certificado del modelo cotizado, etiqueta legible y fecha de fabricación por unidad</strong>, y con los números de parte de banda de ratchet, careta, orejera e interior, que en una dotación grande son la diferencia entre reponer una pieza y reponer el casco. Propuesta con partidas y modelo definido —LTX o LTG4X— en menos de <strong>24 horas hábiles</strong>, con cobertura en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Norma declarada", "valor": "NFPA 1970 · edición 2025"},
    {"label": "Ajuste", "valor": "12 posiciones en dos ejes"},
    {"label": "Modelos", "valor": "LTX y LTG4X"}
  ]),
  ("specStrip", [
    {"label": "Coquilla", "valor": "Termoplástico contemporáneo"},
    {"label": "Ajuste de altura", "valor": "Pestañas A, B y C"},
    {"label": "Balance", "valor": "Postes 1 y 2"},
    {"label": "Protección ocular", "valor": "Careta R330 o goggles IZ4/FP4"},
    {"label": "Montaje", "valor": "Quick-Attach sin herramienta"},
    {"label": "Iluminación", "valor": "TrakLite compatible"}
  ]),
])

L4["secciones"] = [
  {
    "id": "la-serie",
    "eyebrow": "Qué estás comprando",
    "titulo": "Dos modelos, una plataforma ligera",
    "parrafos": [
      "El manual de fabricante cubre la serie con <strong>dos modelos: LTX y LTG4X</strong>, los dos descritos como casco estructural termoplástico de estilo contemporáneo. Es la línea que Bullard posiciona como ligera y de perfil recortado, y en la práctica es la que más se ve en dotaciones grandes: brigadas industriales, cuerpos municipales que equipan por licitación y programas de reposición escalonada.",
      "La decisión entre modelos no se toma por catálogo sino por el herraje y los accesorios que ya tiene la corporación. Cuando hay inventario de caretas o de goggles, el criterio es cuál de los dos monta lo que ya está en la estación sin comprar herraje nuevo."
    ],
    "lista": [
      {"t": "Coquilla termoplástica", "d": "Perfil contemporáneo, más recortado que una tradicional de ala completa. Menos superficie que enganche en espacios reducidos y reposición más económica que un composite."},
      {"t": "Quick-Attach", "d": "El herraje que permite montar o cambiar careta y goggles <strong>sin herramienta</strong>. En una flota grande esto define si el cambio de protección ocular lo hace la estación o el proveedor."},
      {"t": "Careta R330", "d": "Careta de 4 pulgadas de PPC con recubrimiento duro. El manual la lista para FX y PX además de la LT, así que es refacción compartida entre series: una sola clave de repuesto para varias familias."},
      {"t": "Goggles IZ4 y FP4", "d": "Ensambles de goggle disponibles también con herraje Quick-Attach. Son la protección ocular real para maniobras sin pieza facial, y se piden por separado."}
    ]
  },
  {
    "id": "ajuste-por-eje",
    "eyebrow": "Lo que distingue a esta serie",
    "titulo": "12 posiciones, pero repartidas en dos ejes",
    "parrafos": [
      "Casi todos los fabricantes venden el ajuste como un número: 12 posiciones, 36 posiciones, ocho puntos. El manual de la LT hace algo distinto y más útil: <strong>dice qué controla cada ajuste</strong>. Las pestañas se identifican como A, B y C y mueven la <strong>altura de uso</strong>; los postes se identifican como 1 y 2 y controlan el <strong>balance adelante-atrás</strong>, es decir si el casco tiende a irse hacia la frente o hacia la nuca.",
      "Eso cambia la práctica de dotación por completo. Un elemento al que el casco “se le va para atrás” no necesita otra talla: necesita mover el poste. Un elemento que siente el ala demasiado baja no necesita otro casco: necesita cambiar de pestaña. Con esa información, el ajuste inicial de una flota deja de ser prueba y error y se convierte en un procedimiento de dos preguntas."
    ],
    "tabla": {
      "head": ["Ajuste", "Qué controla", "Síntoma que resuelve"],
      "rows": [
        ["Pestañas A, B y C", "Altura de uso del casco sobre la cabeza", "El ala queda demasiado baja sobre los ojos o demasiado alta y deja frente expuesta"],
        ["Postes 1 y 2", "Balance adelante-atrás y nivelación", "El casco se va hacia la nuca al mirar arriba o se cae hacia la frente al agacharse"],
        ["Banda de ratchet", "Perímetro, operable con guante", "Ajuste fino por turno y por elemento, sin herramienta"],
        ["Combinación", "12 configuraciones de asiento documentadas", "Compartir cascos entre turnos con un procedimiento escrito en lugar de criterio individual"]
      ]
    },
    "nota": "Este es el dato que hay que llevarse a la capacitación de entrega: <strong>NOM-017-STPS</strong> obliga a capacitar en el uso del equipo, y un ajuste documentado por eje es lo que hace que esa capacitación sea reproducible en lugar de una demostración que se olvida."
  },
  {
    "id": "dotacion",
    "eyebrow": "Dotación por volumen",
    "titulo": "Por qué esta serie gana en pedidos grandes",
    "parrafos": [
      "En una compra de veinte cascos el precio unitario decide; en una de cien, lo que decide es el costo de operar la flota durante diez años. Ahí la LT tiene tres ventajas concretas: la coquilla termoplástica se repone más barato que un composite, la careta R330 es refacción compartida con otras series de la misma marca, y el herraje Quick-Attach permite que el cambio de protección ocular lo haga el propio personal.",
      "El punto a considerar es el opuesto: si el procedimiento de la corporación exige silueta tradicional de ala completa, esta serie no es la respuesta y conviene evaluar la <strong>UST Traditional</strong> de la misma marca. La comparación no es de calidad, es de geometría y de norma interna."
    ],
    "lista": [
      {"t": "Reposición por pieza", "d": "Banda de ratchet, cubierta de la banda, almohadilla, interior, orejera, barboquejo y careta tienen número de parte. En flota grande la partida de refacciones se presupuesta desde el primer año."},
      {"t": "Refacción compartida", "d": "La careta R330 aparece en el manual para FX y PX además de la LT. Una sola clave cubre varias series, lo que simplifica el almacén de una corporación con parque mixto."},
      {"t": "Cambio sin herramienta", "d": "Quick-Attach permite pasar de careta a goggles según la maniobra sin mandar el casco a taller. Es tiempo de disponibilidad, no comodidad."},
      {"t": "Iluminación opcional", "d": "El manual del TrakLite lista compatibilidad con UST6, FX, PX y LT. Si se agrega, entran pilas AAA como consumible y la restricción de atmósfera Clase I División 2."}
    ]
  },
  {
    "id": "limpieza",
    "eyebrow": "Lo que dice el fabricante, textual",
    "titulo": "Limpieza: detergente suave y agua, nada más",
    "parrafos": [
      "El manual es explícito y conviene citarlo en el procedimiento de la estación en lugar de parafrasearlo: la instrucción es <strong>limpiar coquilla interior y exterior con jabón o detergente suave</strong>, y no usar el casco si no está completamente limpio y seco. La versión en español del manual de la marca —publicada para la serie UST— lo pone en mayúsculas: limpiar sólo con detergente suave y agua, y <strong>no exponer el casco a pinturas, solventes, productos químicos, adhesivos o gasolina</strong>.",
      "Esto tiene una consecuencia que casi nadie aplica: los adhesivos entran en la lista. Las calcomanías de patrocinio, los stickers de identificación pegados encima y la pintura de retoque no son personalización inocua, son sustancias que el fabricante pide no aplicar sobre la coquilla. La identificación va donde el fabricante la previó: portafrente, marcaje de fábrica y cintas."
    ],
    "nota": "El mismo manual pide <strong>retirar el casco de servicio después de un impacto fuerte, aunque no haya daño visible</strong>, y nunca alterar ni modificar el diseño o la construcción sin instrucciones escritas explícitas del fabricante. Las dos frases valen más en una bitácora de estación que cualquier folleto."
  },
  {
    "id": "edicion",
    "eyebrow": "Edición normativa",
    "titulo": "El manual dice NFPA 1971 y la página dice NFPA 1970 · 2025",
    "parrafos": [
      "El manual de usuario de la serie declara que el modelo <strong>cumple o excede las especificaciones de NFPA 1971</strong>, sin edición. La página de producto de la marca, en cambio, declara hoy <strong>NFPA 1970 edición 2025</strong>, el estándar que consolidó las NFPA 1971, 1975, 1981 y 1982 y cuya transición cerró el 18 de marzo de 2026.",
      "Las dos cosas pueden ser ciertas a la vez porque son documentos con distinta fecha de revisión: un manual impreso no se reimprime cada vez que cambia un estándar. Lo que no se puede hacer es tomar la cita del manual y copiarla al anexo técnico de una convocatoria de 2026, porque estaría pidiendo una edición sustituida."
    ],
    "nota": "Lo exigible en la compra: <strong>certificado del modelo cotizado referido a la edición vigente</strong>, con organismo certificador y alcance. El manual sirve para operar y capacitar; el certificado es el que sostiene la partida."
  },
  {
    "id": "capacitacion",
    "eyebrow": "Entrega y capacitación",
    "titulo": "El expediente de entrega que pide la NOM-017-STPS",
    "parrafos": [
      "En México la compra no termina con la factura. <strong>NOM-017-STPS</strong> obliga al patrón a seleccionar el equipo según el riesgo del puesto, entregarlo y <strong>capacitar en su uso, limpieza, mantenimiento y límites</strong>. En un casco eso significa cuatro cosas concretas que se pueden documentar el día de la entrega.",
      "Cuando la dotación es grande, esa capacitación es la que determina si a los seis meses la flota sigue ajustada o si la mitad del personal trae el casco flojo. El ajuste documentado por eje de esta serie hace la diferencia: se enseña una vez, se escribe y se repite igual en cada turno."
    ],
    "lista": [
      {"t": "Ajuste individual registrado", "d": "Pestaña —A, B o C— y poste —1 o 2— con los que quedó cada elemento, anotados en su expediente. Es un dato de dos caracteres que evita reajustar a ciegas."},
      {"t": "Prueba con el conjunto", "d": "Ajuste validado con capucha, protección ocular y pieza facial del equipo de respiración puestas, en posiciones reales de trabajo."},
      {"t": "Procedimiento de limpieza", "d": "Detergente suave y agua, sin solventes ni adhesivos, con el criterio de no usar el casco hasta que esté seco. Copiado textual del manual, no resumido."},
      {"t": "Criterios de retiro", "d": "Retiro tras impacto aunque no haya daño visible, y retiro programado a los diez años de la fecha de fabricación conforme a NFPA 1850 (1851)."}
    ]
  },
  {
    "id": "lo-no-publicado",
    "eyebrow": "Lo que el fabricante no publica",
    "titulo": "Tres datos ausentes y una corrección que hicimos",
    "parrafos": [
      "El manual de la serie es fuerte en operación y débil en cifras de comparación. Lo decimos con nombre y apellido porque es lo que permite pedir el dato en lugar de suponerlo."
    ],
    "tabla": {
      "head": ["Dato ausente", "Qué decide", "Cómo se resuelve"],
      "rows": [
        ["Peso de la serie", "Fatiga cervical y comparación entre familias de la misma marca", "Se solicita por escrito para la clave cotizada; en la línea Bullard el único peso publicado es el del perfil UST LowRider"],
        ["Rango de talla en pulgadas o centímetros", "Qué personal queda fuera del rango en una dotación grande", "El manual no lo indica: se pide el rango del sistema U-Fit para el modelo cotizado y se valida con prueba de ajuste"],
        ["Dimensiones exteriores", "Paso por escotilla y maniobra en cabina", "No están en el manual; se piden por escrito o se comparan contra las series que sí las publican en su hoja de licitación"]
      ]
    },
    "nota": "La corrección: una ficha consolidada de nuestro propio archivo daba por hecho que <strong>el manual de esta serie estaba disponible en español</strong>. Al revisar el PDF, lo único en español es la advertencia de la Propuesta 65 de California. El manual de fabricante que sí existe traducido es el de la <strong>serie UST</strong>. Preferimos corregirlo aquí que sostener un dato cómodo."
  },
  {
    "id": "cuando-conviene",
    "eyebrow": "Criterio de selección",
    "titulo": "Cuándo conviene la LT y cuándo no",
    "parrafos": [
      "Ninguna serie es la mejor en abstracto, y una ficha que dice que sí no está informando, está vendiendo. Estos son los casos en los que esta serie es la respuesta correcta y los casos en los que hay que mandar al comprador a otra."
    ],
    "tabla": {
      "head": ["Situación", "Recomendación", "Por qué"],
      "rows": [
        ["Dotación grande con presupuesto por unidad ajustado", "LT Series", "Coquilla termoplástica de reposición económica, refacción compartida y cambio de protección ocular sin herramienta"],
        ["Procedimiento interno que exige ala completa", "UST Traditional", "La silueta es un requisito normado por la corporación; el composite sostiene el voladizo del ala"],
        ["El peso es criterio de evaluación escrito", "Perfil UST LowRider", "Es el único de la línea con peso publicado por el fabricante: 1.4 a 1.5 kg"],
        ["Se busca máxima iluminación y visor integrado", "PX Series", "Es la serie con más opciones de iluminación integrada y visor ReTrak del catálogo"]
      ]
    },
    "nota": "El criterio que no aparece en ninguna tabla y decide más compras de las que debería: si la corporación ya tiene inventario de caretas y goggles con herraje de una serie, cambiar de familia cuesta más que la diferencia de precio unitario."
  },
  {
    "id": "mantenimiento",
    "eyebrow": "Ciclo de vida",
    "titulo": "Inspección, refacciones y retiro",
    "parrafos": [
      "La inspección de esta serie sigue el mismo criterio de todo casco estructural, con una particularidad del termoplástico: <strong>lo que hay que buscar es deformación y burbujeo, no fisuras</strong>. Un termoplástico expuesto a calor sostenido cede y se abomba antes de romperse; una coquilla con burbujeo se retira aunque la superficie esté completa.",
      "Del lado de las refacciones, la serie tiene listado de partes reemplazables: banda de ratchet, careta, orejera con protector de cuello e interior. Reponer esas cuatro piezas es lo que mantiene el ajuste y la higiene entre inspecciones anuales, y es una fracción del costo de la unidad completa."
    ],
    "nota": "El retiro se rige por <strong>NFPA 1850 (1851)</strong>: diez años desde la fecha de fabricación, más el retiro inmediato tras un impacto fuerte —aunque no haya daño visible— y el retiro cuando el daño ya no es económicamente reparable, que es la formulación literal del manual."
  }
]

L4["galeria"] = [
  {"src": "/images/catalogo/1575507371202-600x450.webp", "alt": "Cascos estructurales con visera de policarbonato en la estación", "caption": "Dotación por volumen, misma clave"},
  {"src": "/images/catalogo/1503714964235-600x450.webp", "alt": "Bombero revisando y ajustando su equipo de protección antes de salir", "caption": "El ajuste se registra por elemento"},
  {"src": "/images/catalogo/1651368615152-600x450.webp", "alt": "Rack de equipo de protección personal listo en una estación de bomberos", "caption": "Refacciones por número de parte"},
  {"src": "/images/catalogo/1608723724615-600x450.webp", "alt": "Dos bomberos con casco identificado operando en ambiente con humo", "caption": "Identificación en escena"}
]

L4["aplicaciones"] = [
  {"sector": "Brigadas industriales", "desc": "Dotación por volumen con ajuste documentado por eje, capacitación de entrega conforme a NOM-017-STPS y refacciones presupuestadas desde el primer año."},
  {"sector": "Cuerpos de bomberos", "desc": "Para corporaciones sin silueta tradicional normada, o para dotar personal de apoyo y rescate con perfil recortado mientras la línea de ataque usa ala completa."},
  {"sector": "Licitación pública", "desc": "Partida cerrada por modelo —LTX o LTG4X—, protección facial y ocular en renglones separados, edición normativa vigente y números de parte de refacciones."}
]

L4["datoClave"] = {
  "titulo": "Registra dos caracteres por elemento",
  "texto": "La pestaña —<strong>A, B o C</strong>— y el poste —<strong>1 o 2</strong>— con los que quedó ajustado cada casco caben en dos caracteres del expediente. Es el dato que evita reajustar a ciegas cada vez que rota el turno."
}

L4["referencias"] = [
  {"code": "NFPA 1970 · 2025", "desc": "Edición que la marca declara hoy para la serie en su página de producto. Consolidó NFPA 1971, 1975, 1981 y 1982; la transición cerró el 18 de marzo de 2026."},
  {"code": "NFPA 1971 · sin edición", "desc": "Cita que aparece en el manual de usuario de la serie, anterior a la consolidación. Sirve para operar y capacitar, no para redactar el anexo técnico de una compra nueva."},
  {"code": "ANSI/ISEA Z87.1", "desc": "Norma de protección ocular y facial. La careta R330 de 4 pulgadas de PPC con recubrimiento duro es el componente declarado contra ella en la línea."},
  {"code": "NOM-017-STPS", "desc": "Selección, entrega y capacitación en el uso del equipo de protección personal según el riesgo del puesto. Es la norma mexicana que exige documentar la entrega."},
  {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento: inspección anual documentada y retiro a los diez años de la fecha de fabricación."}
]

L4["blog"] = [
  "casco-bombero-bullard-usrhb-guia",
  "equipar-brigada-industrial-mexico-guia",
  "nom-002-stps-guia-brigadas-industriales",
  "epp-completo-kit-bombero-profesional",
  "mantenimiento-epp-estructural-nfpa-1851",
  "nfpa-1971-mexico-norma-bomberos"
]

L4["faqs"] = [
  {
    "q": "¿Cuál es la diferencia entre los modelos LTX y LTG4X?",
    "a": "El manual de fabricante cubre los dos como casco estructural termoplástico de estilo contemporáneo dentro de la misma serie, y la diferencia práctica está en el herraje y los accesorios que monta cada uno. Por eso el criterio de selección no es de catálogo: si la corporación ya tiene inventario de caretas o de goggles, conviene definir el modelo que usa ese herraje. En la propuesta indicamos el modelo, el herraje y los números de parte compatibles para que la reposición no obligue a comprar todo de nuevo."
  },
  {
    "q": "¿Qué significa que el ajuste tenga 12 posiciones en dos ejes?",
    "a": "Que el fabricante documenta qué controla cada ajuste en lugar de sumar posiciones. Las pestañas A, B y C mueven la altura de uso —qué tan abajo monta el casco— y los postes 1 y 2 controlan el balance adelante-atrás. Eso convierte un problema difuso en dos preguntas: si el casco se va hacia la nuca, se mueve el poste; si el ala queda muy baja sobre los ojos, se cambia la pestaña. En una dotación grande es la diferencia entre un procedimiento reproducible y prueba y error."
  },
  {
    "q": "¿Cuánto pesa un casco LT Series?",
    "a": "Bullard no publica el peso de esta serie y no lo vamos a estimar. En toda la línea de casco estructural de la marca el único peso publicado es el del perfil UST LowRider: 49.3 a 54.4 oz, es decir 1.4 a 1.5 kg. Si el peso va a ser criterio de evaluación en una convocatoria, hay dos caminos honestos: pedirlo por escrito al fabricante para la clave exacta que se va a cotizar, o especificar la serie que sí tiene cifra publicada."
  },
  {
    "q": "¿Se le pueden poner calcomanías o pintura de identificación?",
    "a": "El fabricante pide no hacerlo. La versión en español de su manual lo escribe en mayúsculas: limpiar sólo con detergente suave y agua, y no usar ni exponer el casco a pinturas, solventes, productos químicos, adhesivos o gasolina. Los adhesivos están en esa lista, así que las calcomanías pegadas sobre la coquilla no son personalización inocua. La identificación va donde el fabricante la previó: portafrente, marcaje de fábrica y cintas reflejantes especificadas en la orden."
  },
  {
    "q": "¿La LT acepta el sistema TrakLite?",
    "a": "Sí: el manual del TrakLite lista compatibilidad con las series UST6, FX, PX y LT. Dos consecuencias que conviene presupuestar antes de decidirlo. La primera, que introduce componentes electrónicos y por lo tanto pilas AAA alcalinas como consumible del programa. La segunda, y más importante para planta, que el sistema está declarado únicamente para Clase I División 2, Grupos A a D, o áreas no peligrosas: no cubre atmósferas clasificadas como División 1."
  },
  {
    "q": "¿El manual de esta serie está en español?",
    "a": "No, y vale la pena decirlo porque nuestra propia ficha interna lo daba por hecho: al revisar el PDF del manual de la serie LT, lo único en español es la advertencia de la Propuesta 65 de California. El manual de fabricante que sí existe traducido al español es el de la serie UST. Si el idioma de la documentación es un requisito de la convocatoria, hay que verificarlo por serie y por modelo antes de comprometerlo en la propuesta, y así lo entregamos nosotros."
  },
  {
    "q": "¿Qué se inspecciona en una coquilla termoplástica?",
    "a": "Deformación y burbujeo antes que fisuras. Un termoplástico expuesto a calor sostenido cede y se abomba, así que una coquilla abombada se retira aunque la superficie esté completa. Además se revisan decoloración por calor, estado del interior y de la banda de ratchet, integridad del barboquejo y de la orejera, y legibilidad de la etiqueta. El manual es tajante en un punto: después de un impacto fuerte el casco se reemplaza aunque no haya daño visible."
  },
  {
    "q": "¿Qué documentación entregan con una dotación grande?",
    "a": "Certificado del modelo cotizado referido a la edición normativa vigente, etiqueta legible y fecha de fabricación por unidad, ficha técnica con material de coquilla y sistema de ajuste, números de parte de banda de ratchet, careta, orejera e interior, procedimiento de limpieza y criterios de retiro, carta de distribuidor autorizado y factura desglosada por modelo y color. Para dotaciones grandes agregamos la hoja de registro de ajuste por elemento, con pestaña y poste."
  }
]

# ===MARCADOR===

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'cascos-bullard-y-msa')
card = next(c for c in prod['l3']['catalogo']['cards']
            if c['marca'] == 'Bullard' and c['modelo'] == 'LT Series')
card['slug'] = SLUG
card['fichaLabel'] = 'la LT Series'
card['l4'] = L4

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('l4 agregado a', card['marca'], card['modelo'], '→', SLUG)
print('  secciones:', len(L4['secciones']), '| faqs:', len(L4['faqs']))
print('  seoTitle len:', len(L4['seoTitle']) + len(' | Firefighter.com.mx'),
      '| seoDescription len:', len(L4['seoDescription']))
ids = [s['id'] for s in L4['secciones']]
assert len(ids) == len(set(ids)) and not ({'ficha','galeria','sectores','preguntas','configuraciones','catalogo'} & set(ids))
assert len({g['src'] for g in L4['galeria']}) == len(L4['galeria'])
print('  palabras (aprox):', sum(len(p.split()) for s in L4['secciones']
      for p in list(s.get('parrafos', [])) + [i['d'] for i in s.get('lista', [])] + [s.get('nota', '')]))
