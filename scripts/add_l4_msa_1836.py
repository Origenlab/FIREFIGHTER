# -*- coding: utf-8 -*-
"""Agrega slug + bloque l4 a la card MSA Cairns 1836 (L3 de cascos).

Fuente primaria: ficha de producto MSA 3600-169-MC del Cairns 1836, consultada el 2026-08-06.
Datos publicados que sostienen la ficha:
  - coquilla de composite de fibra de vidrio "through-colored" con resina termoestable de alta
    temperatura, resistente a flama y a desprendimiento, reforzada con fibra picada de 1" y 2",
    moldeada por compresion en una sola pieza
  - espesor de pared: 0.075" en corona y 0.085" en ala
  - peso 53.6 oz (1.5 kg) a 63.0 oz (1.8 kg) segun configuracion
  - dimensiones 15.3" de largo, 11.8" de ancho y 5.78" de profundidad de corona
  - cofia: forro de polimero resistente al impacto cubierto por espuma de uretano de celda
    abierta semirrigida de alta temperatura que cubre toda la corona interior
  - suspension de seis vias con tres tiras de nylon de 0.75" montadas en seis puntos del forro
  - talla 5-3/8" a 8-3/8" ajustable en incrementos de 1/8"
  - orejeras de triple capa: Nomex de 7.5 oz/yd amarillo o negro con dos capas interiores de
    franela negra retardante
  - barboquejo de tres piezas en cinta de Nomex hilado de 3/4" con hebilla de liberacion rapida
    y corredera postman opcional, 35" a extension total
  - proteccion ocular: visor articulado Defender (claro o ambar), Bourke Eye Shield, careta
    externa Tuffshield ambar y sistemas de goggle ESS
  - careta envolvente de alto pivote, 4.0" x 18.0" x 0.150"
  - colores sin pintar blanco, rojo, negro y amarillo; pintados suman naranja, azul, verde y
    rosa sobre coquilla blanca
  - portafrente de laton colapsable para escudos de 6" o 5.5"
  - cintas reflejantes en ocho piezas tetraedricas, Reflexite o Scotchlite
  - garantia de diez anos desde la fecha de fabricacion
  - declara NFPA 1971-2018

Eje editorial: es la ficha mejor documentada del catalogo, y esta pagina ensena a leer cada
dato —espesor por zona, rango de peso, rango de talla— y a migrar una especificacion que
todavia pide el descontinuado Cairns 1044.
Idempotente. Correr DESPUES de add_l3_cascos.py.
"""
import json, io, collections

RUTA = 'src/data/productos.json'
SLUG = 'msa-cairns-1836'

L4 = collections.OrderedDict([
  ("seoTitle", "Casco MSA Cairns 1836 tradicional composite"),
  ("seoDescription", "Casco MSA Cairns 1836: composite moldeado en una pieza, espesor de 0.075\" y 0.085\", peso de 1.5 a 1.8 kg, talla 5-3/8\" a 8-3/8\" y garantía de 10 años."),
  ("h1", "Casco estructural MSA Cairns 1836"),
  ("subtitulo", "La tradicional vigente de MSA y la ficha con más datos publicados del catálogo: coquilla de composite moldeada en una pieza con espesor declarado por zona, peso de 53.6 a 63.0 oz según configuración, suspensión de seis vías con talla de 5-3/8\" a 8-3/8\" y garantía de diez años desde la fecha de fabricación."),
  ("heroImg", {
    "src": "/images/catalogo/1735107673023-1000x750.webp",
    "alt": "Bombero con casco tradicional de ala completa y capucha bajo el casco",
    "caption": "La tradicional vigente de MSA"
  }),
  ("heroBloques", [
    {
      "label": "Por qué esta ficha se puede defender por escrito",
      "texto": "De las seis series del catálogo, esta es la única que publica <strong>espesor de coquilla por zona, rango de peso, dimensiones y rango de talla en incrementos exactos</strong>. Eso cambia la naturaleza de la compra: un anexo técnico se puede redactar con números verificables —0.075\" en corona, 0.085\" en ala, 1.5 a 1.8 kg, 5-3/8\" a 8-3/8\"— en lugar de adjetivos que cualquier proveedor declara cumplir. Es también la serie que sustituye al <strong>Cairns 1044</strong>, descontinuado y todavía citado por nombre en especificaciones mexicanas."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "Entregamos el casco con <strong>certificado del modelo cotizado, etiqueta legible y fecha de fabricación por unidad</strong> —dato que aquí manda, porque la garantía de diez años corre desde ahí—, más los números de parte de suspensión, orejeras, barboquejo, visor y portafrente. Propuesta con partidas, color y configuración ocular definidas en menos de <strong>24 horas hábiles</strong>, con cobertura en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Norma declarada", "valor": "NFPA 1971 · edición 2018"},
    {"label": "Peso publicado", "valor": "1.5 a 1.8 kg"},
    {"label": "Garantía", "valor": "10 años desde fabricación"}
  ]),
  ("specStrip", [
    {"label": "Coquilla", "valor": "Composite moldeado en una pieza"},
    {"label": "Espesor", "valor": "0.075\" corona · 0.085\" ala"},
    {"label": "Dimensiones", "valor": "15.3\" × 11.8\" × 5.78\""},
    {"label": "Suspensión", "valor": "Seis vías con ratchet pivotante"},
    {"label": "Rango de talla", "valor": "5-3/8\" a 8-3/8\" en 1/8\""},
    {"label": "Protección ocular", "valor": "Defender, Bourke o goggles"}
  ]),
])

L4["secciones"] = [
  {
    "id": "construccion",
    "eyebrow": "Qué estás comprando",
    "titulo": "Una coquilla moldeada en una sola pieza",
    "parrafos": [
      "La ficha de MSA describe la coquilla con un nivel de detalle poco común: <strong>composite de fibra de vidrio con resina termoestable de alta temperatura, tintada en masa, resistente a flama y a desprendimiento, reforzada con fibra picada de una y dos pulgadas y moldeada por compresión en una sola pieza</strong>. Cada parte de esa frase es un criterio de compra, no adorno.",
      "“Tintada en masa” significa que el color atraviesa el material y un rayón no deja fibra desnuda. “Moldeada en una pieza” significa que no hay unión estructural entre corona y ala, que es donde fallaría primero un ensamble en dos partes. Y “fibra picada de una y dos pulgadas” describe el refuerzo que le da rigidez al voladizo del ala sin sumar espesor uniforme."
    ],
    "lista": [
      {"t": "Cofia de impacto en dos capas", "d": "Forro de polímero resistente al impacto cubierto por una espuma de uretano de celda abierta semirrígida y de alta temperatura, que cubre <strong>toda la corona interior</strong>. La celda abierta es lo que permite lavarla y secarla."},
      {"t": "Suspensión de seis vías", "d": "Tres tiras de nylon de 0.75 pulgadas montadas en seis puntos del forro de impacto, con ratchet pivotante. Es la descripción textual que conviene copiar a la partida en lugar de un número de puntos."},
      {"t": "Portafrente de latón colapsable", "d": "Diseñado para escudos de identificación de 6 o 5.5 pulgadas. “Colapsable” es intencional: cede en un golpe en lugar de transmitirlo a la coquilla."},
      {"t": "Cintas reflejantes en ocho piezas", "d": "Ocho piezas tetraédricas, en Reflexite o Scotchlite. La geometría en tetraedros devuelve luz desde más ángulos que una banda continua."}
    ]
  },
  {
    "id": "espesor",
    "eyebrow": "Cómo se lee un espesor",
    "titulo": "0.075\" en la corona y 0.085\" en el ala: por qué son distintos",
    "parrafos": [
      "Este es el dato que ninguna otra serie del catálogo publica, y el que más se malinterpreta. MSA declara <strong>0.075 pulgadas de espesor en la corona y 0.085 pulgadas en el ala</strong>. La lectura ingenua es que la corona está “menos protegida”; la lectura correcta es que cada zona resuelve un problema distinto.",
      "La corona recibe impacto vertical y trabaja en conjunto con la cofia, que es la que absorbe: ahí el espesor de coquilla reparte la carga y el resto lo hace la espuma. El ala, en cambio, trabaja en voladizo, sin cofia detrás, y recibe golpes laterales contra marcos y estructura: necesita más material propio porque no tiene nada que la respalde. Diez milésimas de pulgada de diferencia son una decisión de ingeniería, no una tolerancia."
    ],
    "nota": "En una comparativa técnica, pedir el <strong>espesor nominal por zona</strong> es una pregunta legítima y discriminante: la mayoría de los fabricantes no lo publica, así que quien lo entrega demuestra control de proceso. Es uno de los cuatro datos que recomendamos exigir en un anexo técnico de cascos."
  },
  {
    "id": "peso",
    "eyebrow": "El rango de peso",
    "titulo": "1.5 a 1.8 kg: qué configuración cae en cada extremo",
    "parrafos": [
      "MSA publica el peso como rango —<strong>53.6 oz (1.5 kg) a 63.0 oz (1.8 kg)</strong>— y añade la condición que casi nadie lee: <strong>según configuración</strong>. Esas 9.4 onzas de diferencia, unos 265 gramos, no son variabilidad de fabricación: son los accesorios.",
      "El extremo bajo corresponde a una configuración simple; el alto, a una con visor articulado, careta externa, orejera de triple capa y portafrente con escudo. Sobre la columna cervical de un elemento en un turno de doce horas, esos 265 gramos son la diferencia entre terminar el turno cómodo o con dolor de cuello. Por eso el peso que hay que pedir es el de la clave cotizada, no el del rango."
    ],
    "tabla": {
      "head": ["Concepto", "Dato publicado", "Cómo usarlo en la compra"],
      "rows": [
        ["Peso mínimo", "53.6 oz · 1.5 kg", "Referencia de configuración base. No asumir que la oferta llega en este extremo del rango"],
        ["Peso máximo", "63.0 oz · 1.8 kg", "Configuración completa con accesorios. Es el número realista si se pide visor, careta y escudo"],
        ["Diferencia", "9.4 oz · unos 265 g", "El costo en carga cervical de cada accesorio que se agrega a la partida"],
        ["Condición del dato", "“Según configuración”", "Obliga a pedir el peso de la clave exacta: es la única cifra que se puede evaluar"]
      ]
    },
    "nota": "Comparación útil dentro del catálogo: el único otro peso publicado es el del <strong>UST LowRider</strong> de Bullard, entre 1.4 y 1.5 kg. Es decir, la configuración base del 1836 arranca donde termina el rango del perfil ligero de la competencia directa."
  },
  {
    "id": "talla",
    "eyebrow": "Rango de talla",
    "titulo": "De 5-3/8\" a 8-3/8\" en incrementos de un octavo",
    "parrafos": [
      "MSA es el único fabricante del catálogo que publica el rango de talla en unidades verificables: <strong>de 5-3/8 a 8-3/8 pulgadas, ajustable en incrementos de 1/8 de pulgada</strong>. Traducido a lo que importa en una dotación, son 25 posiciones discretas de perímetro, no un “ajuste universal”.",
      "Ese dato resuelve una pregunta que en México casi nunca se hace antes de comprar: qué porcentaje del personal queda dentro del rango. Con un rango publicado se puede medir la plantilla, comparar contra la tabla y saber de antemano si alguien va a quedar fuera —y a quién hay que cotizarle otra serie— en lugar de descubrirlo el día de la entrega."
    ],
    "nota": "El ajuste se valida con capucha y pieza facial del equipo de respiración puestas. Un perímetro correcto en seco puede quedar apretado con capucha, y ahí es donde la <strong>capucha</strong> deja de ser un accesorio y se vuelve parte de la prueba de ajuste."
  },
  {
    "id": "ocular",
    "eyebrow": "Protección ocular",
    "titulo": "Defender, Bourke, careta externa y goggles: cuatro caminos",
    "parrafos": [
      "El 1836 es la serie con más opciones oculares documentadas del catálogo, y cada una responde a una tradición operativa distinta. La careta publicada es <strong>envolvente de alto pivote, de 4.0\" × 18.0\" × 0.150\"</strong> de espesor —las tres dimensiones están en la ficha, lo cual permite compararla con la de otras marcas.",
      "La regla de fondo es la misma de toda la línea: una careta o un visor montados al casco protegen la cara de proyecciones frontales pero no cierran el contorno del ojo. Cuando el elemento trae la pieza facial del equipo de respiración, esa es la protección primaria; para las maniobras sin máscara, goggles."
    ],
    "lista": [
      {"t": "Visor Defender articulado", "d": "Integrado al casco, en versión clara o ámbar. Se despliega y se guarda con el casco puesto, lo que lo hace la opción práctica cuando la maniobra alterna interior y exterior."},
      {"t": "Bourke Eye Shield", "d": "La solución tradicional montada bajo el ala. Es la que muchos cuerpos con silueta tradicional tienen normada, y MSA la mantiene en catálogo por eso."},
      {"t": "Careta externa Tuffshield", "d": "Versión ámbar, envolvente y de alto pivote. Cubre más superficie facial y es la más simple de reponer cuando se raya."},
      {"t": "Sistemas de goggle ESS", "d": "La única opción que sella el contorno del ojo. Se especifica aparte, con su propio número de parte, y es lo que corresponde para ventilación, remoción y rescate vehicular."}
    ]
  },
  {
    "id": "soft-goods",
    "eyebrow": "Orejeras y barboquejo",
    "titulo": "Triple capa y 35 pulgadas de extensión",
    "parrafos": [
      "Las orejeras se publican con su gramaje y su construcción: <strong>Nomex de 7.5 oz por yarda en amarillo o negro, con dos capas interiores de franela negra retardante</strong>. Tres capas en total. Es la pieza que cierra la brecha entre casco, capucha y cuello del chaquetón del traje estructural, y también la que más se contamina y menos se lava.",
      "El barboquejo es de tres piezas en cinta de Nomex hilado de 3/4 de pulgada, con hebilla de liberación rápida y corredera tipo postman opcional, y <strong>35 pulgadas a extensión total</strong>. Ese número importa más de lo que parece: define si el barboquejo cierra sobre una capucha y una barba, o si obliga a llevarlo al límite."
    ],
    "nota": "Las dos son refacciones con número de parte y las dos definen higiene. En una compra por volumen conviene pedir <strong>un juego de orejeras de repuesto por cada tres cascos</strong>: es la pieza que se retira para lavar y la que se pierde primero."
  },
  {
    "id": "el-1044",
    "eyebrow": "Migrar una especificación",
    "titulo": "Si tu especificación todavía pide un Cairns 1044",
    "parrafos": [
      "El <strong>Cairns 1044</strong> —y también el 1010— aparecen marcados como descontinuados en el sitio de MSA, y siguen siendo los modelos más citados por nombre en especificaciones y procedimientos mexicanos. Una convocatoria que pide un 1044 hoy está pidiendo un producto que el fabricante ya no ofrece, y el efecto práctico es que abre la puerta a “equivalentes” sin criterio escrito para evaluarlos.",
      "La salida no es cambiar un nombre por otro. Es reescribir la partida con los <strong>atributos</strong> que el 1044 representaba —silueta tradicional de ala completa, coquilla de composite, suspensión con ratchet, protección ocular tipo Bourke o visor integrado— y agregar los datos que ahora sí se pueden exigir porque el modelo vigente los publica."
    ],
    "tabla": {
      "head": ["Si la especificación dice…", "Escribe esto en su lugar", "Por qué"],
      "rows": [
        ["“Casco MSA Cairns 1044 o equivalente”", "“Casco estructural tradicional de composite moldeado en una pieza, espesor mínimo declarado por zona, suspensión de seis vías con ratchet”", "Describe atributos verificables en lugar de un modelo descontinuado"],
        ["“Con protección ocular”", "“Visor articulado integrado, más goggles como partida independiente”", "El visor y los goggles no son sustitutos: uno protege la cara, el otro sella el ojo"],
        ["“Certificado NFPA”", "“Certificado del modelo cotizado con edición normativa vigente y organismo certificador”", "“NFPA” sin edición ni alcance no es verificable"],
        ["“Talla ajustable”", "“Rango de ajuste declarado con incremento, de 5-3/8\" a 8-3/8\" en 1/8\"”", "Es el dato que permite saber si toda la plantilla entra en el rango"]
      ]
    },
    "nota": "Si la especificación está en un procedimiento interno o en un manual de operación, conviene actualizar el documento y no solo la requisición: mientras el 1044 siga escrito ahí, va a volver a aparecer en la siguiente compra."
  },
  {
    "id": "garantia",
    "eyebrow": "Garantía y vida útil",
    "titulo": "Diez años desde la fecha de fabricación, no desde la compra",
    "parrafos": [
      "MSA garantiza el 1836 por <strong>diez años desde la fecha de fabricación</strong> contra defectos de material y de mano de obra. La palabra que decide el presupuesto es “fabricación”: un lote que estuvo dos años en inventario del distribuidor llega con ocho años de cobertura, no con diez.",
      "Y hay una coincidencia útil: el criterio de retiro de <strong>NFPA 1850 (1851)</strong> también son diez años desde la fecha de fabricación. Es decir, en este modelo la garantía y la vida útil normativa corren en paralelo, lo que hace del dato de la etiqueta el único número relevante para planear la reposición."
    ],
    "nota": "Pide la <strong>fecha de fabricación por unidad</strong> antes de firmar, no después. Es un dato que el proveedor tiene y que rara vez se entrega si no se solicita; con él se puede escalonar la reposición y evitar que toda la flota venza el mismo año."
  },
  {
    "id": "edicion",
    "eyebrow": "Edición normativa",
    "titulo": "La ficha declara NFPA 1971-2018 y qué significa hoy",
    "parrafos": [
      "La ficha de producto del 1836 declara conformidad con <strong>NFPA 1971-2018</strong>, la norma de conjuntos de protección para combate estructural y de proximidad. Esa edición fue consolidada en <strong>NFPA 1970 edición 2025</strong> junto con las NFPA 1975, 1981 y 1982, y el periodo de transición cerró el 18 de marzo de 2026.",
      "Que la ficha cite 2018 no invalida el producto ni el inventario ya etiquetado: la permanencia en servicio se rige por NFPA 1850 (1851). Lo que sí exige es precisión en la compra nueva, porque un certificado emitido hoy debería referirse a la edición vigente y no a la que quedó sustituida."
    ],
    "nota": "Lo exigible: <strong>certificado del modelo y de la configuración cotizada</strong>, con organismo certificador, alcance y edición. Si el certificado que entrega el proveedor todavía dice 2018, hay que pedir la constancia de la edición vigente por escrito antes de fallar la partida."
  },
  {
    "id": "lo-no-publicado",
    "eyebrow": "Lo que el fabricante no publica",
    "titulo": "Incluso la ficha más completa deja tres huecos",
    "parrafos": [
      "Sería fácil presentar esta serie como si no le faltara nada, y sería falso. Aun siendo la mejor documentada del catálogo, hay tres datos que no están y que conviene pedir por escrito."
    ],
    "tabla": {
      "head": ["Dato ausente", "Qué decide", "Cómo se resuelve"],
      "rows": [
        ["Peso por número de parte", "La cifra real de la configuración cotizada dentro del rango de 1.5 a 1.8 kg", "Se pide el peso de la clave exacta con visor, careta, orejera y escudo montados"],
        ["Edición vigente en el certificado", "Si la partida se puede fallar sin observaciones en 2026", "Se solicita constancia referida a NFPA 1970 edición 2025 para el modelo cotizado"],
        ["Vida útil declarada por el fabricante", "Cuándo sale del inventario si no hubo impacto", "No hay cifra propia más allá de la garantía: rige el retiro de NFPA 1850 (1851) a los diez años de fabricación"]
      ]
    },
    "nota": "Los tres se piden en un solo correo referido al número de parte, y los gestionamos como parte de la propuesta. La diferencia entre una ficha comercial y una propuesta técnica es exactamente esa: <strong>el dato se consigue, no se supone</strong>."
  }
]

L4["galeria"] = [
  {"src": "/images/catalogo/1638401607229-600x400.webp", "alt": "Casco tradicional de bombero con visera y careta de protección facial", "caption": "Configuración ocular documentada"},
  {"src": "/images/catalogo/1756112277157-1000x750.webp", "alt": "Rack con cascos estructurales alineados en la estación", "caption": "Fecha de fabricación por unidad"},
  {"src": "/images/catalogo/1592235905030-600x450.webp", "alt": "Bombero con pieza facial de equipo de respiración bajo el casco estructural", "caption": "El ajuste se valida con el conjunto"},
  {"src": "/images/catalogo/1690210795713-600x450.webp", "alt": "Dos bomberos con casco estructural y visera durante una operación", "caption": "Silueta tradicional en escena"}
]

L4["aplicaciones"] = [
  {"sector": "Cuerpos de bomberos", "desc": "Para corporaciones con silueta tradicional normada que necesitan sustituir un Cairns 1044 o 1010 descontinuado sin abrir la partida a equivalentes indefinidos."},
  {"sector": "Brigadas industriales", "desc": "Cuando la matriz de riesgo contempla intervención estructural y la evaluación pide datos verificables: espesor por zona, rango de peso y rango de talla publicados."},
  {"sector": "Licitación pública", "desc": "Es la serie del catálogo con la que un anexo técnico se puede redactar con números de fabricante en lugar de descripciones que cualquier oferta declara cumplir."}
]

L4["datoClave"] = {
  "titulo": "Garantía y vida útil corren juntas",
  "texto": "Los <strong>diez años de garantía</strong> de MSA corren desde la <strong>fecha de fabricación</strong>, igual que el retiro obligatorio de NFPA 1850 (1851). Pide esa fecha por unidad antes de firmar: un lote con dos años de inventario llega con ocho de vida útil y de cobertura."
}

L4["referencias"] = [
  {"code": "NFPA 1971 · 2018", "desc": "Edición declarada en la ficha de producto del Cairns 1836. Fue consolidada en NFPA 1970 edición 2025; el inventario etiquetado bajo ella sigue siendo válido en servicio."},
  {"code": "NFPA 1970 · 2025", "desc": "Estándar vigente que integró NFPA 1971, 1975, 1981 y 1982. La transición cerró el 18 de marzo de 2026 y es la edición que debe citar un certificado emitido hoy."},
  {"code": "ANSI/ISEA Z87.1", "desc": "Norma de protección ocular y facial aplicable a caretas y goggles. La careta publicada del 1836 mide 4.0\" × 18.0\" × 0.150\" y es envolvente de alto pivote."},
  {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento: inspección anual documentada y retiro a los diez años de la fecha de fabricación, el mismo horizonte que la garantía del fabricante."},
  {"code": "Cairns 1044 y 1010", "desc": "Modelos marcados como descontinuados en el sitio de MSA. Si una especificación todavía los pide por nombre, hay que reescribirla por atributos antes de licitar."}
]

L4["blog"] = [
  "cascos-forestales-msa-cairns-guia",
  "casco-bombero-bullard-usrhb-guia",
  "nfpa-1971-mexico-norma-bomberos",
  "mantenimiento-epp-estructural-nfpa-1851",
  "epp-completo-kit-bombero-profesional",
  "capucha-nomex-pbi-proteccion-cuello-cara"
]

L4["faqs"] = [
  {
    "q": "¿El Cairns 1836 sustituye al Cairns 1044?",
    "a": "En la práctica sí: el 1044 y el 1010 aparecen marcados como descontinuados en el sitio de MSA y el 1836 es su tradicional vigente. Pero conviene no hacer la sustitución solo por nombre. Lo correcto es reescribir la partida por atributos —silueta tradicional, coquilla de composite moldeada en una pieza, espesor declarado por zona, suspensión de seis vías con ratchet, protección ocular definida— y agregar los datos que el modelo vigente sí publica. Si el 1044 está citado en un procedimiento interno, hay que actualizar ese documento también."
  },
  {
    "q": "¿Por qué el ala es más gruesa que la corona?",
    "a": "Porque resuelven problemas distintos. La corona, con 0.075 pulgadas, trabaja junto con la cofia de impacto: la coquilla reparte la carga y la espuma de uretano absorbe. El ala, con 0.085 pulgadas, trabaja en voladizo y sin cofia detrás, y recibe los golpes laterales contra marcos y estructura, así que necesita más material propio. Esas diez milésimas de pulgada son una decisión de diseño, no una tolerancia de fabricación."
  },
  {
    "q": "¿Cuánto pesa exactamente y de qué depende?",
    "a": "MSA publica un rango: 53.6 oz (1.5 kg) a 63.0 oz (1.8 kg) según configuración. Los 265 gramos de diferencia son los accesorios: visor articulado, careta externa, orejera de triple capa y portafrente con escudo. Para una evaluación por peso, el número que sirve es el de la clave exacta que se va a cotizar, con todo montado, y se pide por escrito. Como referencia del catálogo, el único otro peso publicado es el del Bullard UST LowRider, entre 1.4 y 1.5 kg."
  },
  {
    "q": "¿Cómo sé si todo mi personal entra en el rango de talla?",
    "a": "Con este modelo se puede saber antes de comprar, porque el rango está publicado: de 5-3/8 a 8-3/8 pulgadas en incrementos de 1/8, que son 25 posiciones discretas de perímetro. El procedimiento es medir la plantilla, compararla con ese rango y detectar de antemano a quién habría que cotizarle otra serie. Y la prueba de ajuste se hace con capucha y pieza facial puestas: un perímetro correcto en seco puede quedar apretado con capucha."
  },
  {
    "q": "¿Qué diferencia hay entre el visor Defender, el Bourke y la careta externa?",
    "a": "El Defender es un visor articulado integrado al casco, en versión clara o ámbar, que se despliega y se guarda con el casco puesto. El Bourke Eye Shield es la solución tradicional montada bajo el ala, que muchos cuerpos con silueta tradicional tienen normada. La careta externa Tuffshield es envolvente, de alto pivote y cubre más superficie facial. Ninguna de las tres sella el contorno del ojo: para eso están los goggles ESS, que se especifican como partida aparte."
  },
  {
    "q": "¿La garantía de diez años cubre todo el casco?",
    "a": "Cubre defectos de material y de mano de obra, y corre desde la fecha de fabricación por MSA, no desde la compra. No es una autorización de uso por diez años ni cubre desgaste, contaminación o daño por impacto. La coincidencia útil es que el retiro obligatorio de NFPA 1850 (1851) también son diez años desde fabricación, así que en este modelo garantía y vida útil normativa corren en paralelo y basta un dato —la fecha de la etiqueta— para planear la reposición."
  },
  {
    "q": "¿Qué refacciones conviene comprar con la dotación?",
    "a": "Orejeras, suspensión completa, barboquejo, visor o careta según la configuración, y escudos de portafrente. La recomendación práctica para volumen es un juego de orejeras de repuesto por cada tres cascos: es la pieza que se retira para lavar, la que más se contamina y la que se pierde primero. El portafrente es de latón colapsable, diseñado para escudos de 6 o 5.5 pulgadas, así que el escudo se especifica con la medida y el marcaje desde la orden."
  },
  {
    "q": "¿Qué documentación entregan con este modelo?",
    "a": "Certificado del modelo y de la configuración cotizada con organismo certificador y alcance, constancia referida a la edición normativa vigente, etiqueta legible y fecha de fabricación por unidad, ficha técnica con espesor por zona, peso, dimensiones y rango de talla, números de parte de suspensión, orejeras, barboquejo, visor y portafrente, procedimiento de inspección y retiro, carta de distribuidor autorizado y factura desglosada por color y configuración."
  }
]

# ===MARCADOR===

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'cascos-bullard-y-msa')
card = next(c for c in prod['l3']['catalogo']['cards']
            if c['marca'] == 'MSA' and c['modelo'] == 'Cairns 1836')
card['slug'] = SLUG
card['fichaLabel'] = 'el Cairns 1836'
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
