# -*- coding: utf-8 -*-
"""Agrega el bloque l3 a guantes-de-intervencion (EPP para Bomberos).

Fuente primaria consolidada: ~/Documents/Claude/Projects/LGACONTRAINCENDIOS/src/data/
productos/guantesBombero.mjs (revisada 2026-07-20), con 8 referencias de fabricante:
Shelby 5228 y 5227, Pro-Tech 8 Titan K Pro / Titan Pro / Vision, Majestic M7G y M7W,
Veridian Fire Knight y el guante SKOLD.

Eje editorial: es la unica linea del catalogo donde el mercado YA migro a NFPA 1970-2025,
asi que aqui la pregunta no es que edicion cita el fabricante sino QUE PESO TIENE SU
DECLARACION: "certificado por UL" no es lo mismo que "cumple con los requisitos de" ni que
"fabricado bajo los requerimientos de". Y el segundo hilo: la destreza es criterio de
seguridad, no de confort.

Idempotente.
"""
import json, io, collections

RUTA = 'src/data/productos.json'

L3 = collections.OrderedDict([
  ("seoTitle", "Guantes estructurales para bombero NFPA 1970"),
  ("seoDescription", "Guantes estructurales certificados NFPA 1970: puño gauntlet o wristlet, concha de canguro, koala o Kevlar, barrera declarada y tallas de XXS a Jumbo."),
  ("h1", "Guantes estructurales para bombero, gauntlet y wristlet"),
  ("subtitulo", "Guante de intervención con concha de piel de canguro, koala, búfalo de agua o compuesto de Kevlar, barrera de humedad declarada por modelo y curvas de tallas que van de XXS a Jumbo: la pieza del conjunto donde la destreza también es un criterio de seguridad."),
  ("heroImg", {
    "src": "/images/catalogo/1666518809220-1000x750.webp",
    "alt": "Manos con guantes de intervención sujetando equipo de bombero",
    "caption": "Destreza e interfaz con la manga del chaquetón"
  }),
  ("heroBloques", [
    {
      "label": "Por qué la destreza es criterio de seguridad",
      "texto": "Un guante que protege pero <strong>impide operar una válvula, un mosquetón o una radio</strong> no reduce el riesgo: lo desplaza. Por eso esta pieza no se compra por costumbre ni por precio del par. Y es la única línea del catálogo donde el mercado <strong>ya migró a NFPA 1970-2025</strong>: hay fabricantes con certificación vigente bajo la edición nueva, así que aquí sí se puede exigir sin aceptar una edición sustituida."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "Entregamos el guante con <strong>certificado del modelo cotizado, organismo certificador nombrado y edición normativa</strong> —porque en esta línea “cumple con los requisitos de” y “certificado por UL” no pesan igual—, y levantamos la <strong>talla por usuario</strong>, no por promedio de brigada. Propuesta técnica en menos de <strong>24 horas hábiles</strong> y cobertura en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Edición exigible", "valor": "NFPA 1970 · 2025"},
    {"label": "Tallas publicadas", "valor": "De XXS a Jumbo según marca"}
  ]),
  ("specStrip", [
    {"label": "Puño", "valor": "Gauntlet o wristlet"},
    {"label": "Concha", "valor": "Canguro, koala, búfalo o Kevlar"},
    {"label": "Barrera", "valor": "PU sin PFAS, Porelle o CROSSTECH"},
    {"label": "Forro", "valor": "Kovenex y equivalentes"},
    {"label": "Tallaje", "valor": "8 u 11 tallas según fabricante"},
    {"label": "TPP publicado", "valor": "Superior a 60 en un modelo"}
  ]),
])

L3["catalogo"] = collections.OrderedDict([
  ("eyebrow", "Catálogo por marca"),
  ("titulo", "Guantes estructurales<br>por marca y construcción"),
  ("intro", "Cuatro datos separan un guante de otro: <strong>tipo de puño, material de la concha, barrera de humedad y curva de tallas</strong>. Ninguno se deduce de la foto. Cada card reproduce la declaración normativa tal como la escribe el fabricante, porque en esta línea <strong>las palabras del expediente pesan distinto</strong>."),
  ("imgRef", "Imagen de referencia de la línea"),
  ("nota", "Dos referencias quedan fuera del grid y vale conocerlas. El <strong>Pro-Tech 8 Vision</strong> suma concha de piel de búfalo de agua y <strong>banda RIT fotoluminiscente</strong> para localización, con declaración de NFPA 1970-2025 y EN 659. El <strong>guante SKÖLD</strong> es <strong>unitalla</strong> y la fuente consultada <strong>no declara ninguna certificación NFPA</strong>: no debe presentarse ni comprarse como equivalente a las referencias certificadas de este grid, y si la especificación exige certificación de tercera parte, esa referencia no la acredita. La única mención normativa de su fuente aclara que el puño interior de Kevlar no es requerimiento NFPA."),
  ("cards", [
    {
      "marca": "Shelby",
      "modelo": "5228",
      "variante": "Gauntlet",
      "varianteLabel": "Tipo de puño",
      "badge": "NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1666518809220-600x400.webp",
      "alt": "Manos con guantes de intervención sujetando equipo de bombero",
      "desc": "Concha de <strong>piel Koala</strong>, barrera de poliuretano <strong>libre de PFAS</strong> y forro Kovenex, con la curva de tallas más amplia del catálogo: <strong>de XXS a Jumbo</strong>. Puño largo tipo gauntlet, que va por fuera de la manga del chaquetón.",
      "specs": [
        "Concha de piel Koala",
        "Barrera de poliuretano libre de PFAS",
        "Forro Kovenex",
        "Tallas de XXS a Jumbo"
      ],
      "chip": "Declara cumplir los requisitos de NFPA 1970-2025"
    },
    {
      "marca": "Shelby",
      "modelo": "5227",
      "variante": "Wristlet",
      "varianteLabel": "Tipo de puño",
      "badge": "NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1666518809220-600x450.webp",
      "alt": "Manos operando conexiones de equipo de respiración con guante puesto",
      "desc": "<strong>El mismo guante que el 5228</strong> con puño wristlet de Nomex, que ajusta al antebrazo y se lleva por dentro de la manga. El par 5228/5227 es la prueba de que gauntlet y wristlet son <strong>decisión de procedimiento, no de nivel de protección</strong>.",
      "specs": [
        "Misma construcción que el 5228",
        "Puño wristlet de Nomex",
        "Se lleva por dentro de la manga",
        "Tallas de XXS a Jumbo"
      ],
      "chip": "Elige por procedimiento e interfaz, no por protección"
    },
    {
      "marca": "Pro-Tech 8",
      "modelo": "Titan K Pro",
      "variante": "Canguro 100 %",
      "varianteLabel": "Concha",
      "badge": "SEI · NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1690210795620-600x450.webp",
      "alt": "Bombero con guantes de intervención sujetando una herramienta de mango largo",
      "desc": "El fabricante lo presenta como el <strong>único guante estructural con concha 100 % de piel de canguro</strong>, la piel con mejor relación entre delgadez y resistencia a la abrasión. Barrera <strong>Porelle DXT PRO</strong> y certificación SEI con efecto declarado el 18 de marzo de 2026.",
      "specs": [
        "Concha 100 % de piel de canguro",
        "Barrera Porelle DXT PRO",
        "Certificación SEI declarada",
        "Clave PT-8 TNK SC"
      ],
      "chip": "Certificación de tercera parte con fecha de efecto declarada"
    },
    {
      "marca": "Pro-Tech 8",
      "modelo": "Titan Pro",
      "variante": "Kevlar sin piel",
      "varianteLabel": "Concha",
      "badge": "SEI · NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1563062067-9d-600x450.webp",
      "alt": "Bombero abriendo una puerta metálica con guantes de intervención",
      "desc": "Construcción <strong>sin piel</strong>: compuesto de Kevlar y Litex fusionado con silicón. Es la referencia para quien quiere evitar el comportamiento de la piel al mojarse y secarse, y la única del catálogo con <strong>TPP declarado superior a 60</strong>.",
      "specs": [
        "Kevlar con Litex fusionado con silicón",
        "TPP declarado superior a 60",
        "Sin piel: otro comportamiento al mojado",
        "Clave PT-8 TN SC"
      ],
      "chip": "El único con TPP publicado en el catálogo"
    },
    {
      "marca": "Majestic",
      "modelo": "M7G y M7W",
      "variante": "Canguro premium",
      "varianteLabel": "Concha",
      "badge": "UL · NFPA 1970 · 2025",
      "estado": "documentada",
      "img": "/images/catalogo/1633540440007-600x450.webp",
      "alt": "Bombero forzando un acceso con herramienta de mango largo",
      "desc": "Piel de canguro premium en las dos versiones de puño: <strong>M7G gauntlet y M7W con wristlet de Kevlar</strong>. Es la declaración más fuerte del grid: el fabricante escribe <strong>“NFPA 1970-2025 UL CERTIFIED”</strong>, es decir nombra organismo certificador y edición vigente.",
      "specs": [
        "Piel de canguro premium",
        "M7G gauntlet · M7W wristlet de Kevlar",
        "Ocho tallas publicadas",
        "Declara UL como organismo certificador"
      ],
      "chip": "Organismo y edición nombrados en la misma línea"
    },
    {
      "marca": "Veridian",
      "modelo": "Fire Knight",
      "variante": "PBI y Kevlar",
      "varianteLabel": "Concha",
      "badge": "UL · NFPA 1971 · 2018",
      "estado": "documentada",
      "img": "/images/catalogo/1776784163597-600x450.webp",
      "alt": "Equipo de rescate operando sobre un vehículo siniestrado con guante puesto",
      "desc": "Dorso <strong>tejido de PBI y Kevlar</strong> con inserto <strong>GORE CROSSTECH</strong> y la curva de tallas más fina del catálogo: <strong>11 tallas</strong>. Certificado por UL bajo <strong>NFPA 1971 edición 2018</strong>, edición que fue sustituida: en compra nueva hay que pedir constancia de la vigente.",
      "specs": [
        "Dorso tejido de PBI y Kevlar",
        "Inserto GORE CROSSTECH",
        "Once tallas publicadas",
        "Certificado por UL según el fabricante"
      ],
      "chip": "Edición 2018 declarada · pedir constancia de la vigente"
    }
  ])
])

L3["secciones"] = [
  {
    "id": "destreza",
    "eyebrow": "Por qué importa",
    "titulo": "La destreza también es un criterio de seguridad",
    "parrafos": [
      "El guante es la pieza del conjunto que más compromete la capacidad de trabajar, y la que más se compra por costumbre. El razonamiento habitual —“más gruesa protege más”— falla aquí: un guante que protege pero <strong>impide operar una válvula, un mosquetón, una radio o una conexión de manguera</strong> no reduce el riesgo, lo mueve de lugar. El elemento se lo quita, o pierde tiempo en la maniobra crítica.",
      "Por eso la selección tiene que enfrentar dos criterios al mismo tiempo: exposición térmica esperada y <strong>tarea real</strong>. Y tiene que probarse con la tarea, no apretando el puño en la bodega."
    ],
    "lista": [
      {"t": "Prueba con herramienta", "d": "Operar una válvula de 1½\", abrir y cerrar un mosquetón, conectar y desconectar una manguera, manipular la radio y sacar una linterna del bolsillo. Si algo de eso obliga a quitarse el guante, el guante no es para esa función."},
      {"t": "Prueba de interfaz", "d": "Con el chaquetón puesto: el <strong>gauntlet</strong> va por fuera de la manga y el <strong>wristlet</strong> por dentro. Lo que se verifica es que no quede piel expuesta al levantar y estirar los brazos."},
      {"t": "Prueba en mojado", "d": "La destreza cambia con el guante húmedo, y no todos los materiales se comportan igual. Vale la pena mojar un par de muestra antes de decidir por volumen."},
      {"t": "Talla por usuario", "d": "La talla se asigna <strong>por persona</strong>, no por promedio de brigada. En manos pequeñas un guante grande es pérdida de destreza; en manos grandes un guante corto es pérdida de protección en la muñeca."}
    ]
  },
  {
    "id": "puno",
    "eyebrow": "Gauntlet o wristlet",
    "titulo": "El tipo de puño es decisión de procedimiento, no de protección",
    "parrafos": [
      "Es la confusión más común de la línea. El puño largo tipo <strong>gauntlet</strong> cubre por fuera la manga del chaquetón; el <strong>wristlet</strong> ajusta al antebrazo y se lleva por dentro. Se discute como si uno protegiera más, y la prueba de que no es así está en el propio catálogo: varios fabricantes publican <strong>el mismo guante en las dos versiones</strong> —Shelby 5228 y 5227, Majestic M7G y M7W—.",
      "Lo que cambia es la interfaz y el procedimiento de la corporación. Cambia por dónde puede entrar agua y escombro, cambia la velocidad para calzarse y descalzarse, y cambia cómo se comporta la muñeca al estirar el brazo por encima de la cabeza."
    ],
    "tabla": {
      "head": ["Tipo de puño", "Cómo se lleva", "Cuándo conviene"],
      "rows": [
        ["Gauntlet (puño largo)", "Por fuera de la manga del chaquetón", "Cuando el procedimiento prioriza cubrir el traslape desde afuera y el calzado rápido; es el más común en combate estructural"],
        ["Wristlet (puño corto)", "Por dentro de la manga, ajustado al antebrazo", "Cuando se prioriza que no entre escombro por la boca del puño y un perfil más limpio para trabajar con cuerda o herramienta fina"],
        ["El mismo modelo en las dos", "Shelby 5228/5227 · Majestic M7G/M7W", "Es la prueba de que la elección es de interfaz: misma concha, misma barrera, mismo forro"],
        ["Puño de Kevlar o de piel", "Variante de material del puño", "En una de las referencias el puño interior de Kevlar se aclara como <strong>no requerido</strong> por NFPA: es preferencia, no norma"]
      ]
    },
    "nota": "En la partida se escribe el tipo de puño, no se deja abierto. Si la corporación usa las dos configuraciones —gauntlet en línea de ataque y wristlet en rescate— se cotizan como <strong>dos renglones</strong> con cantidad por talla en cada uno."
  },
  {
    "id": "concha",
    "eyebrow": "Material de la concha",
    "titulo": "Canguro, koala, búfalo o Kevlar: qué cambia de verdad",
    "parrafos": [
      "El material exterior decide destreza, comportamiento al mojarse y resistencia a la abrasión, y es el dato que con más frecuencia queda sin escribir en una orden. Entre las referencias del catálogo hay cuatro construcciones distintas, y ninguna es mejor en abstracto."
    ],
    "tabla": {
      "head": ["Material declarado", "Referencia", "Qué gana", "Qué considerar"],
      "rows": [
        ["Piel de canguro 100 %", "Pro-Tech 8 Titan K Pro", "La mejor relación entre delgadez y resistencia a la abrasión: destreza sin sacrificar durabilidad", "Es la construcción de mayor costo de la tabla"],
        ["Piel Koala", "Shelby 5228 y 5227", "Buen equilibrio de destreza y precio, con la curva de tallas más amplia del catálogo", "Como toda piel, requiere secado correcto para no endurecerse"],
        ["Piel de búfalo de agua", "Pro-Tech 8 Vision", "Robustez y resistencia mecánica en tareas de fuerza", "Menos destreza fina que el canguro"],
        ["Kevlar con Litex y silicón", "Pro-Tech 8 Titan Pro", "Sin piel: otro comportamiento al mojarse y secarse, y TPP declarado superior a 60", "Tacto distinto al de la piel; conviene probarlo con la herramienta real"],
        ["Tejido de PBI y Kevlar en dorso", "Veridian Fire Knight", "Flexibilidad en el dorso con inserto GORE CROSSTECH y 11 tallas", "Su declaración es de la edición 2018 de NFPA 1971"]
      ]
    },
    "nota": "El material va escrito en la orden. “Guante de piel” no es una especificación: entre canguro y búfalo hay una diferencia de destreza que el usuario nota en la primera maniobra."
  },
  {
    "id": "barrera",
    "eyebrow": "Barrera de humedad",
    "titulo": "No se supone: se declara por modelo",
    "parrafos": [
      "La barrera de humedad del guante es la capa que decide si entra líquido y cómo se comporta térmicamente el conjunto cuando la mano está mojada. Las referencias del catálogo declaran <strong>tres barreras distintas</strong> —poliuretano libre de PFAS, Porelle DXT PRO e inserto GORE CROSSTECH— y esa diferencia no se ve por fuera.",
      "La regla es simple y ahorra discusiones: <strong>si el fabricante no la declara para el modelo cotizado, no se asume que está</strong>. Un guante sin barrera declarada puede ser perfectamente válido para la tarea, pero no se compra creyendo que la tiene."
    ],
    "nota": "El dato de la barrera <strong>libre de PFAS</strong> ya aparece en esta línea, igual que en trajes. Es una tendencia que va a llegar a las especificaciones mexicanas: conviene preguntarla ahora, cuando todavía es un diferenciador y no un requisito."
  },
  {
    "id": "tallaje",
    "eyebrow": "Curva de tallas",
    "titulo": "De XXS a Jumbo, once tallas, ocho o unitalla",
    "parrafos": [
      "El tallaje del guante varía más entre fabricantes que en cualquier otra pieza del conjunto, y es lo que decide si el guante se usa o se queda en el casillero. En el catálogo hay curvas de <strong>XXS a Jumbo</strong>, de <strong>once tallas</strong>, de <strong>ocho</strong> y una referencia <strong>unitalla</strong>.",
      "Una curva corta obliga a compromisos que siempre se pagan: la mano pequeña pierde destreza y la grande pierde protección en la muñeca. En una dotación mixta —y toda dotación es mixta— la amplitud de la curva vale más que una diferencia de precio del par."
    ],
    "tabla": {
      "head": ["Curva publicada", "Referencia", "Qué implica en una dotación"],
      "rows": [
        ["De XXS a Jumbo", "Shelby 5228 y 5227", "La más amplia del catálogo: cubre extremos que otras curvas dejan fuera"],
        ["Once tallas", "Veridian Fire Knight", "La más fina: mejor ajuste intermedio, más renglones que administrar"],
        ["Ocho tallas", "Majestic M7G y M7W", "Curva estándar del mercado, suficiente para la mayoría de una plantilla"],
        ["Unitalla", "Referencia SKÖLD, fuera del grid", "Obliga a compromiso de ajuste en toda la plantilla; y esa referencia tampoco declara certificación NFPA"]
      ]
    },
    "nota": "Se levanta <strong>talla por usuario</strong> y se pide cantidad por talla en la partida. Un pedido “20 pares talla L” es la forma más rápida de terminar con seis pares sin usar."
  },
  {
    "id": "declaraciones",
    "eyebrow": "El peso de las palabras",
    "titulo": "La única línea donde el mercado ya migró a NFPA 1970-2025",
    "parrafos": [
      "En cascos y en botas casi todos los fabricantes siguen citando ediciones previas. En guantes pasó lo contrario: <strong>varias referencias ya declaran NFPA 1970-2025</strong>. Eso cambia el estándar de exigencia de una compra: aquí sí se puede pedir la edición vigente sin quedarse sin ofertas.",
      "Y aparece el segundo hilo, más fino: <strong>no todas las declaraciones pesan igual</strong>. “Certificado por UL” nombra un organismo de tercera parte. “Cumple con los requisitos de” es una afirmación del propio fabricante. “Fabricado bajo los requerimientos de” es todavía más débil. Y no declarar nada es la cuarta categoría. Las cuatro conviven en este catálogo."
    ],
    "tabla": {
      "head": ["Cómo lo escribe el fabricante", "Qué significa", "Qué pedir"],
      "rows": [
        ["“NFPA 1970-2025 UL CERTIFIED”", "Nombra organismo certificador y edición vigente. Es la declaración más fuerte del grid", "El certificado con número de expediente y modelo"],
        ["Certificación SEI con fecha de efecto", "Organismo de tercera parte y fecha a partir de la cual aplica la edición nueva", "La constancia con esa fecha y el modelo cotizado"],
        ["“Meets the glove requirements of NFPA 1970-2025”", "Declaración de conformidad del fabricante, sin nombrar organismo", "Preguntar quién certificó y pedir el documento"],
        ["“Certificado por UL conforme a NFPA 1971-2018”", "Tercera parte, pero bajo una edición sustituida", "Constancia referida a la edición vigente"],
        ["Sin declaración normativa", "No acredita nada, aunque el producto pueda ser útil", "No usarla donde la especificación exija certificación de tercera parte"]
      ]
    },
    "nota": "Redacción que cierra la partida: <strong>“guante estructural certificado por organismo de tercera parte conforme a NFPA 1970 edición 2025, indicando organismo, número de certificado y modelo”</strong>. En esta línea es exigible, y quien no pueda entregarlo queda fuera por documento, no por opinión."
  },
  {
    "id": "cuidado",
    "eyebrow": "Ciclo de vida",
    "titulo": "Secado, contaminación y los guantes que no son este guante",
    "parrafos": [
      "El guante se lava y se seca más veces que cualquier otra pieza, y la piel es el material que peor tolera el error: <strong>secado con calor directo</strong> —radiador, sol prolongado, dentro del vehículo— la endurece y la agrieta, y una concha endurecida ya perdió la destreza por la que se pagó. Secado a temperatura ambiente, con circulación de aire y sin prensar.",
      "El otro punto es de alcance: un guante estructural <strong>no equivale</strong> a un guante de extricación, ni a uno de manejo de químicos, ni a uno de contacto con superficie caliente. Cada tarea tiene su guante y su norma, y usar el estructural para todo lo desgasta antes de tiempo sin proteger mejor."
    ],
    "lista": [
      {"t": "Inspección", "d": "Costuras, desgaste en palma y punta de dedos, endurecimiento de la piel, estado del forro y del puño, y legibilidad de la etiqueta. Un forro desprendido hace imposible calzarse el guante con la mano húmeda."},
      {"t": "Secado", "d": "Temperatura ambiente y aire, nunca calor directo. Dos pares por elemento es lo que permite secar sin dejar a nadie sin guante."},
      {"t": "Contaminación", "d": "Es la pieza que toca todo. Se lava según las instrucciones del fabricante y se retira cuando la contaminación no es removible."},
      {"t": "Retiro", "d": "Como elemento del conjunto estructural aplica <strong>NFPA 1850 (1851)</strong>: diez años desde la fecha de fabricación, más el retiro anticipado por daño, endurecimiento o pérdida de destreza."}
    ]
  }
]

L3["galeria"] = [
  {"src": "/images/catalogo/1666518809220-1000x750.webp", "alt": "Manos con guantes de intervención sujetando equipo de bombero", "caption": "Destreza con el guante puesto"},
  {"src": "/images/catalogo/1690210795713-600x450.webp", "alt": "Dos bomberos con equipo estructural completo durante una operación", "caption": "Interfaz con la manga del chaquetón"},
  {"src": "/images/catalogo/1584033376442-600x450.webp", "alt": "Bombero equipado con herramienta de intervención durante una maniobra", "caption": "La tarea real es la prueba"},
  {"src": "/images/catalogo/1651368615152-600x450.webp", "alt": "Rack de equipo de protección personal listo en una estación de bomberos", "caption": "Dos pares por elemento"}
]

L3["aplicaciones"] = [
  {"sector": "Cuerpos de bomberos", "desc": "Talla asignada por usuario y tipo de puño definido por función: gauntlet en línea de ataque y wristlet donde se prioriza trabajo fino, cotizados como renglones separados."},
  {"sector": "Brigadas industriales", "desc": "Para brigadas cuya matriz de riesgo y entrenamiento contemplen intervención con exposición térmica. Un guante estructural no sustituye al de extricación, químicos o superficie caliente."},
  {"sector": "Licitación pública", "desc": "Es la línea donde sí se puede exigir certificación de tercera parte bajo NFPA 1970 edición 2025, con organismo y número de certificado nombrados."}
]

L3["datoClave"] = {
  "titulo": "Aquí sí puedes exigir la edición vigente",
  "texto": "Guantes es la única línea del catálogo donde <strong>varios fabricantes ya declaran NFPA 1970-2025</strong>, incluso con organismo nombrado —“UL CERTIFIED”— o certificación SEI con fecha de efecto. Pedir la edición vigente aquí no deja la partida sin ofertas: la filtra."
}

L3["normasRef"] = ["NFPA 1970", "NFPA 1971", "NFPA 1851", "NOM-017-STPS", "EN 469"]

L3["documentacion"] = [
  "Certificado del modelo cotizado con organismo de tercera parte y edición vigente",
  "Ficha técnica con material de concha, barrera declarada y forro",
  "Tipo de puño por renglón: gauntlet o wristlet",
  "Curva de tallas con cantidad por talla, levantada por usuario",
  "Instrucciones de lavado y secado del fabricante",
  "Factura desglosada por modelo, tipo de puño y talla"
]

L3["blog"] = [
  "guantes-estructurales-msa-orca-proteccion",
  "botas-guantes-bomberos-nfpa-1971",
  "epp-completo-kit-bombero-profesional",
  "nfpa-1971-mexico-norma-bomberos",
  "mantenimiento-epp-estructural-nfpa-1851",
  "rescate-vehicular-tecnicas-equipos"
]

L3["faqs"] = [
  {
    "q": "¿Gauntlet o wristlet: cuál protege más?",
    "a": "Ninguno de los dos: es una decisión de procedimiento e interfaz. El gauntlet cubre por fuera la manga del chaquetón y el wristlet ajusta al antebrazo por dentro. La prueba de que no es un asunto de nivel de protección está en el catálogo: varios fabricantes publican el mismo guante en las dos versiones —Shelby 5228 y 5227, Majestic M7G y M7W—, con la misma concha, la misma barrera y el mismo forro. Lo que cambia es por dónde puede entrar escombro y cómo se comporta al estirar el brazo."
  },
  {
    "q": "¿Por qué se habla tanto de la piel de canguro?",
    "a": "Porque tiene la mejor relación entre delgadez y resistencia a la abrasión: permite una concha fina —y por lo tanto destreza— sin perder durabilidad. Un fabricante del catálogo presenta su modelo como el único guante estructural con concha 100 % de canguro. También es la construcción más cara de la tabla, así que la pregunta correcta no es si el canguro es mejor material, sino si la tarea justifica pagar por esa destreza."
  },
  {
    "q": "¿Cómo asigno tallas para una brigada?",
    "a": "Por usuario, nunca por promedio. Las curvas publicadas varían mucho: de XXS a Jumbo en una línea, once tallas en otra, ocho en una tercera y unitalla en un caso. Una curva corta obliga a compromisos que se pagan en las dos direcciones: la mano pequeña pierde destreza y la grande pierde protección en la muñeca. Nosotros levantamos la talla por persona y cotizamos cantidad por talla; un pedido de “20 pares talla L” es la forma más rápida de terminar con pares sin usar."
  },
  {
    "q": "¿Qué barrera de humedad debo pedir?",
    "a": "La que el fabricante declare para el modelo exacto, y por escrito. Las referencias del catálogo declaran tres barreras distintas: poliuretano libre de PFAS, Porelle DXT PRO e inserto GORE CROSSTECH. No se ven por fuera y no se deben suponer: si el fabricante no la declara para el modelo cotizado, se asume que no está. El dato de barrera libre de PFAS ya aparece en esta línea y conviene preguntarlo ahora, cuando todavía es un diferenciador."
  },
  {
    "q": "¿Todos los guantes ya están certificados bajo NFPA 1970-2025?",
    "a": "No todos, pero varios sí, y eso hace de esta la línea donde más se puede exigir. En el catálogo hay declaraciones de NFPA 1970-2025 con organismo nombrado —“UL CERTIFIED”—, certificación SEI con fecha de efecto declarada el 18 de marzo de 2026, declaraciones de conformidad del propio fabricante bajo la edición nueva, y una referencia certificada por UL pero bajo la edición 2018, ya sustituida. Pedir la edición vigente aquí no deja la partida sin ofertas: la filtra."
  },
  {
    "q": "¿Qué diferencia hay entre “certificado por UL” y “cumple con los requisitos de”?",
    "a": "El peso del documento. “Certificado por UL” nombra a un organismo de tercera parte que evaluó el producto. “Cumple con los requisitos de” es una declaración del propio fabricante. “Fabricado bajo los requerimientos de” es aún más débil. Y no declarar nada es la cuarta categoría, que también existe en el mercado mexicano. En una licitación conviene pedir organismo, número de certificado y modelo: así la evaluación se resuelve con documento y no con interpretación."
  },
  {
    "q": "¿Un guante estructural sirve para extricación o para químicos?",
    "a": "No. Cada tarea tiene su guante y su norma: el de extricación prioriza resistencia al corte y agarre en superficie mojada, el de químicos se evalúa contra permeación de sustancias específicas y el de superficie caliente contra calor por contacto. Usar el estructural para todo lo desgasta antes de tiempo sin proteger mejor en esas tareas. En la dotación conviene separar el guante de combate del guante de trabajo, aunque implique dos renglones."
  },
  {
    "q": "¿Cómo se secan y cada cuándo se reemplazan?",
    "a": "A temperatura ambiente, con circulación de aire y sin prensar: el calor directo endurece y agrieta la piel, y una concha endurecida ya perdió la destreza por la que se pagó. Dos pares por elemento es lo que permite secar sin dejar a nadie sin guante. El retiro sigue NFPA 1850 (1851) —diez años desde la fecha de fabricación— más el retiro anticipado por daño, endurecimiento, contaminación no removible o pérdida evidente de destreza."
  }
]



with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'guantes-de-intervencion')
# El nombre arranca por el sustantivo que la gente usa y que el modulo del blog resuelve
# por raiz ("guante"). "Guantes de intervencion" ya cumplia; se precisa a estructurales.
prod['nombre'] = 'Guantes estructurales'
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
