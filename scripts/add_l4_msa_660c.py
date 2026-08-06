# -*- coding: utf-8 -*-
"""Agrega slug + bloque l4 a la card MSA Cairns 660C Metro (L3 de cascos).

Fuente primaria: us.msasafety.com, pagina de producto del Cairns 660C Metro, 2026-08-06.
Datos publicados:
  - coquilla de composite de fibra de vidrio tintado en masa, no corrosiva, resistente a
    agrietamiento y desprendimiento
  - cofia de impacto ("impact cap") para proteccion adicional
  - sistema patentado de liberacion de la coquilla para escape ante riesgo de enganche
  - ajuste de altura por ratchet trasero de tres posiciones
  - banda frontal con interfaz para pieza facial de ERA, disenada para acomodar distintos
    disenos de mascara
  - barboquejo de Nomex negro suave con hebilla de liberacion rapida con una mano y corredera
    postman
  - proteccion ocular: careta estandar de 4", TuffShield de 4" o visor Defender retractil
    operable con guante
  - interiores: franela estandar, deluxe de piel con almohadilla de corona, versiones removibles
  - siete colores: negro, amarillo, rojo, blanco, naranja, azul y verde
  - MSA no publica peso ni edicion normativa para este modelo; varias variantes de color con
    goggles ESS y ciertas configuraciones Defender aparecen descontinuadas

Eje editorial: el perfil metro es una decision de interfaz —lo que cambia respecto a una
tradicional es como convive con la pieza facial del ERA y con el riesgo de enganche—, y es la
ficha que ensena a comprar cuando el fabricante NO publica peso ni edicion.
Idempotente. Correr DESPUES de add_l3_cascos.py.
"""
import json, io, collections

RUTA = 'src/data/productos.json'
SLUG = 'msa-cairns-660c-metro'

L4 = collections.OrderedDict([
  ("seoTitle", "Casco MSA Cairns 660C Metro perfil bajo"),
  ("seoDescription", "Casco MSA Cairns 660C Metro: composite tintado en masa, cofia de impacto, ratchet de tres posiciones, banda con interfaz para pieza facial y visor Defender."),
  ("h1", "Casco estructural MSA Cairns 660C Metro"),
  ("subtitulo", "El perfil metro de MSA: coquilla de composite tintado en masa con cofia de impacto, sistema patentado de liberación de coquilla ante enganche, ajuste de altura por ratchet de tres posiciones y banda frontal diseñada para convivir con la pieza facial del equipo de respiración."),
  ("badge", "NFPA · edición a confirmar"),
  ("heroImg", {
    "src": "/images/catalogo/1575507371089-600x450.webp",
    "alt": "Cascos estructurales de perfil recortado colgados en la estación",
    "caption": "Perfil metro para maniobra en espacios reducidos"
  }),
  ("heroBloques", [
    {
      "label": "Por qué el perfil metro es una decisión de interfaz",
      "texto": "Un casco recortado no se elige por estética: se elige por lo que <strong>deja de estorbar</strong>. El 660C reduce superficie de ala y, sobre todo, resuelve dos interfaces que en un casco tradicional se resuelven a la fuerza: la <strong>banda frontal está diseñada para acomodar distintos diseños de pieza facial</strong> del equipo de respiración, y la coquilla incorpora un sistema patentado de liberación para escapar si algo la engancha. Esas dos cosas, no el perfil, son el argumento técnico."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "Entregamos el casco con <strong>certificado del modelo cotizado, etiqueta legible y fecha de fabricación por unidad</strong>, y con los números de parte de suspensión, interior, orejera, barboquejo y visor. En este modelo insistimos en algo más: MSA <strong>no publica peso ni edición normativa</strong>, así que los dos se solicitan por escrito para el número de parte antes de cerrar. Propuesta en menos de <strong>24 horas hábiles</strong>, con cobertura en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Coquilla", "valor": "Composite tintado en masa"},
    {"label": "Ajuste de altura", "valor": "Ratchet de tres posiciones"},
    {"label": "Estado del dato", "valor": "Peso y edición por confirmar"}
  ]),
  ("specStrip", [
    {"label": "Coquilla", "valor": "Composite no corrosivo"},
    {"label": "Cofia", "valor": "Impact cap interior"},
    {"label": "Escape", "valor": "Liberación de coquilla patentada"},
    {"label": "Interfaz con ERA", "valor": "Banda frontal ajustable"},
    {"label": "Protección ocular", "valor": "Careta 4\", TuffShield o Defender"},
    {"label": "Colores", "valor": "Siete opciones de coquilla"}
  ]),
])

L4["secciones"] = [
  {
    "id": "el-perfil",
    "eyebrow": "Qué estás comprando",
    "titulo": "Perfil recortado, coquilla de composite y cofia interior",
    "parrafos": [
      "El 660C Metro es la respuesta de MSA para quien necesita casco estructural con menos silueta. La coquilla es de <strong>composite de fibra de vidrio tintado en masa, no corrosiva y resistente a agrietamiento y desprendimiento</strong>, y por dentro lleva una cofia de impacto que es la que absorbe energía. Esa combinación —composite afuera, cofia adentro— es la misma arquitectura de una tradicional; lo que cambia es cuánta superficie queda expuesta a engancharse.",
      "En operación, el perfil recortado se nota en tres momentos concretos: al entrar por una escotilla o un hueco, al trabajar dentro de un vehículo durante una extricación y al girar la cabeza en un espacio donde el ala de un casco tradicional toca antes que el hombro. Frente a una tradicional como el <strong>Cairns 1836</strong> de la misma marca, lo que se cede es la cuenca del ala completa."
    ],
    "lista": [
      {"t": "Coquilla tintada en masa", "d": "El color atraviesa el material, así que un rayón profundo no deja fibra desnuda. El criterio de retiro se apoya en deformación, burbujeo y agrietamiento, no en la apariencia."},
      {"t": "Cofia de impacto", "d": "La pieza interior que absorbe el golpe deformándose. Es la que hay que inspeccionar después de una exposición térmica o de un impacto, aunque la coquilla se vea intacta."},
      {"t": "Interior configurable", "d": "MSA lo ofrece en franela estándar, en versión deluxe de piel con almohadilla de corona y en configuraciones removibles. La versión removible es la que hace viable el lavado periódico."},
      {"t": "Siete colores de coquilla", "d": "Negro, amarillo, rojo, blanco, naranja, azul y verde. Es el rango más amplio del catálogo y el que permite un código de color por función, por rango y por compañía sin pintar nada."}
    ]
  },
  {
    "id": "liberacion",
    "eyebrow": "El sistema que casi nadie menciona",
    "titulo": "Liberación de coquilla: pensado para soltarse",
    "parrafos": [
      "Todos los cascos se diseñan para quedarse puestos. Este además está diseñado para <strong>soltarse a propósito</strong>: MSA publica un sistema patentado de liberación de la coquilla, previsto para escapar cuando algo la engancha —cable colgante, malla, estructura colapsada, cinta de una carga—. Es una función de rescate propio, no de confort.",
      "Vale la pena entender el compromiso: un casco que puede liberarse es un casco que también puede perderse en el peor momento, y por eso el barboquejo y la práctica de uso importan más, no menos. Lo que aporta el sistema es una salida cuando la alternativa es quedar anclado a una estructura con el aire corriendo."
    ],
    "nota": "En capacitación de entrega esto se demuestra y se practica, no se explica: el personal tiene que saber que existe, cómo se activa y en qué situación conviene usarlo. Si no se enseña, es una función que el casco trae y nadie va a usar."
  },
  {
    "id": "interfaz-era",
    "eyebrow": "La interfaz que decide el ajuste",
    "titulo": "La banda frontal y el reborde de la pieza facial",
    "parrafos": [
      "Aquí está el argumento más sólido de este modelo. MSA describe una <strong>banda frontal con interfaz para pieza facial, diseñada para acomodar distintos diseños de máscara</strong> de equipo de respiración. Traducido: la banda no compite por el espacio que ocupa el reborde superior de la máscara.",
      "El problema que resuelve es real y frecuente. Un casco cuya banda frontal queda justo donde va el reborde de la pieza facial empuja la máscara hacia abajo o hacia adelante, y el sello facial —lo único que separa al elemento de la atmósfera— se compromete. En una estación con dos o tres marcas de equipo de respiración, un casco que acomoda distintos diseños de máscara deja de ser una preferencia y se vuelve una necesidad de inventario."
    ],
    "lista": [
      {"t": "Prueba con la máscara real", "d": "El ajuste se valida con la pieza facial que el elemento va a usar de verdad, no con una prestada. Entre marcas y entre tallas de máscara el reborde cambia de posición."},
      {"t": "Prueba con capucha", "d": "La capucha suma volumen justo donde el casco y la máscara ya compiten. Un ajuste correcto en seco puede empujar la máscara con capucha puesta."},
      {"t": "Posiciones reales de trabajo", "d": "Mirar hacia arriba, agacharse, avanzar en gateo y girar la cabeza. Lo que se busca es que el casco no se mueva y que no presione la máscara en ninguna de las cuatro."},
      {"t": "Ratchet trasero de tres posiciones", "d": "El ajuste de altura del 660C. Es el que fija a qué altura queda la banda frontal y, con ella, si toca o libera el reborde de la máscara."}
    ]
  },
  {
    "id": "ocular",
    "eyebrow": "Protección ocular",
    "titulo": "Tres opciones y el detalle del guante",
    "parrafos": [
      "El 660C se ofrece con careta estándar de 4 pulgadas, con TuffShield de 4 pulgadas o con el <strong>visor Defender retráctil</strong>. La ficha añade un dato que casi ninguna otra menciona y que en campo lo es todo: el Defender está declarado como <strong>operable con guante puesto</strong>.",
      "Ese detalle separa una función usable de una que se queda guardada. Un visor que requiere destreza de dedos desnudos no se despliega en escena; uno operable con guante estructural sí. Como en el resto de la línea, ninguna de las tres cierra el contorno del ojo: para eso están los goggles, y en este modelo conviene revisar disponibilidad porque varias combinaciones con goggles aparecen descontinuadas."
    ],
    "nota": "Si la partida va a incluir goggles, hay que <strong>confirmar el número de parte vigente</strong> antes de cotizar: en este modelo MSA marca como descontinuadas varias variantes de color con goggles ESS y algunas configuraciones de Defender. El casco sigue disponible; la combinación exacta puede no estarlo."
  },
  {
    "id": "sin-peso-ni-edicion",
    "eyebrow": "Lo que el fabricante no publica",
    "titulo": "Ni peso ni edición: cómo se compra igual",
    "parrafos": [
      "Este modelo es el caso contrario al del Cairns 1836 de la misma marca: la construcción está bien descrita, pero <strong>MSA no publica peso ni especifica la edición normativa</strong> en la página del producto. No lo vamos a rellenar con la cifra de otro modelo ni con un “aproximadamente”.",
      "Lo que sí se puede hacer es comprar con método. Los dos datos se piden por escrito referidos al número de parte, y mientras llegan, la partida se redacta con los atributos que sí están publicados. Así la evaluación se sostiene con documento y no con estimaciones."
    ],
    "tabla": {
      "head": ["Dato ausente", "Qué decide", "Cómo se resuelve"],
      "rows": [
        ["Peso del casco", "Fatiga cervical y comparación contra el 1836 y contra la línea Bullard", "Se solicita por escrito para el número de parte, con la configuración ocular montada"],
        ["Edición normativa declarada", "Si el certificado sirve para una compra nueva en 2026", "Se pide el certificado del modelo cotizado indicando edición, organismo certificador y alcance"],
        ["Rango de talla en unidades", "Qué personal queda dentro del rango de ajuste", "Se pide el rango del sistema de ratchet; el 1836 de la misma marca lo publica de 5-3/8\" a 8-3/8\", así que es un dato exigible"],
        ["Disponibilidad de la combinación", "Que la clave cotizada exista de verdad", "Se confirma el número de parte de la combinación color + visor + goggles antes de ofertar"]
      ]
    },
    "nota": "Regla que aplicamos en toda la línea: <strong>un dato que no publica el fabricante no se estima, se solicita</strong>. Si el proveedor lo estima por ti, lo que estás comprando es su suposición con tu presupuesto."
  },
  {
    "id": "cuando-conviene",
    "eyebrow": "Criterio de selección",
    "titulo": "Cuándo el perfil metro es la respuesta correcta",
    "parrafos": [
      "Un perfil recortado no es “mejor” ni “peor” que una tradicional: cambia lo que gana y lo que pierde. Esta tabla es la conversación que tenemos con un comprador antes de cotizar."
    ],
    "tabla": {
      "head": ["Situación operativa", "Recomendación", "Por qué"],
      "rows": [
        ["Extricación vehicular y espacios confinados frecuentes", "660C Metro", "Menos superficie de ala que enganche y perfil que libra el interior de un vehículo"],
        ["Estación con dos o más marcas de pieza facial", "660C Metro", "La banda frontal está diseñada para acomodar distintos diseños de máscara"],
        ["Interior con línea y mucha agua encima", "Cairns 1836 o UST Traditional", "El ala completa forma la cuenca que deriva agua y escombro fuera del cuello del chaquetón"],
        ["El peso es criterio de evaluación escrito", "1836 o UST LowRider", "Son los dos modelos del catálogo con peso publicado por el fabricante"]
      ]
    },
    "nota": "Muchas corporaciones no eligen: <strong>dotan por función</strong>. Ala completa para la línea de ataque, perfil recortado para rescate técnico y extricación. Cuesta más en inventario de refacciones y resuelve mejor las dos maniobras."
  },
  {
    "id": "configuracion",
    "eyebrow": "Cómo se pide",
    "titulo": "Las cinco decisiones de la partida",
    "parrafos": [
      "El 660C se configura por color, protección facial, interior, barboquejo y accesorios. Cada combinación es una clave distinta, y una requisición que no las fija deja la configuración al criterio del proveedor."
    ],
    "tabla": {
      "head": ["Decisión", "Opciones publicadas", "Cómo se escribe en la partida"],
      "rows": [
        ["Color de coquilla", "Negro, amarillo, rojo, blanco, naranja, azul y verde", "Cantidad por color, asignando el color a función o rango"],
        ["Protección facial", "Careta de 4\", TuffShield de 4\" o visor Defender retráctil", "“Visor Defender retráctil operable con guante”, y los goggles como partida independiente"],
        ["Interior", "Franela estándar, deluxe de piel con almohadilla de corona, versiones removibles", "“Interior removible” cuando hay programa de descontaminación, porque es el que se puede lavar"],
        ["Barboquejo", "Nomex negro suave con hebilla de liberación rápida y corredera postman", "Explícito en la partida, con el número de parte de repuesto"],
        ["Datos a confirmar", "Peso y edición normativa no publicados", "Renglón de la propuesta: “el proveedor entrega peso por número de parte y certificado con edición vigente”"]
      ]
    },
    "nota": "Con esos cinco renglones más el certificado y la fecha de fabricación por unidad, dos ofertas del mismo precio dejan de ser dos cascos distintos —que es el problema real de una licitación de cascos, no el precio—."
  },
  {
    "id": "mantenimiento",
    "eyebrow": "Ciclo de vida",
    "titulo": "Inspección del composite y retiro programado",
    "parrafos": [
      "En un composite lo que se busca en la inspección anual documentada es <strong>agrietamiento, desprendimiento del acabado, decoloración por calor y burbujeo</strong>, además del estado de la cofia por dentro, del interior, del barboquejo y del sistema de liberación de coquilla, que también se revisa porque es un mecanismo.",
      "El interior removible es lo que hace realista el lavado, y el lavado es lo que evita que el casco se convierta en el punto sucio del conjunto. La coquilla se limpia con detergente suave y agua: los solventes, adhesivos y pinturas quedan fuera, igual que en el resto de la línea."
    ],
    "nota": "El retiro se rige por <strong>NFPA 1850 (1851)</strong>: diez años desde la fecha de fabricación, más el retiro anticipado por impacto o daño. Al no haber vida útil declarada por el fabricante para este modelo, ese criterio normativo es el único que aplica."
  }
]

L4["galeria"] = [
  {"src": "/images/catalogo/1592235905030-600x450.webp", "alt": "Bombero con pieza facial de equipo de respiración bajo el casco estructural", "caption": "La interfaz con la pieza facial"},
  {"src": "/images/catalogo/1606613817012-600x450.webp", "alt": "Bombero equipado junto a la unidad en escena", "caption": "Perfil recortado en operación"},
  {"src": "/images/catalogo/1776784163597-600x450.webp", "alt": "Equipo de rescate operando sobre un vehículo siniestrado", "caption": "Extricación: menos superficie que enganche"},
  {"src": "/images/catalogo/1726262693471-600x450.webp", "alt": "Casco de protección amarillo listo para asignación de brigada", "caption": "Siete colores para código por función"}
]

L4["aplicaciones"] = [
  {"sector": "Cuerpos de bomberos", "desc": "Para rescate técnico y extricación vehicular, o como segunda configuración de la corporación cuando la línea de ataque usa ala completa."},
  {"sector": "Brigadas industriales", "desc": "Cuando la maniobra dominante es paso lateral en espacios reducidos y la planta tiene más de una marca de equipo de respiración en inventario."},
  {"sector": "Licitación pública", "desc": "Partida cerrada por color, protección facial, interior y barboquejo, con un renglón explícito que obliga al proveedor a entregar peso y certificado con edición vigente."}
]

L4["datoClave"] = {
  "titulo": "Dos datos que el proveedor debe entregar",
  "texto": "MSA <strong>no publica peso ni edición normativa</strong> de este modelo. Ponlo como renglón de la partida: el proveedor entrega peso por número de parte y certificado del modelo con la edición vigente. Lo que no se pide por escrito, no llega."
}

L4["referencias"] = [
  {"code": "NFPA 1970 · 2025", "desc": "Estándar vigente para conjuntos de protección estructural y de proximidad. Es la edición que debe citar el certificado del modelo cotizado en una compra nueva."},
  {"code": "NFPA · sin edición", "desc": "La página de producto del 660C Metro no especifica edición normativa. Es exactamente el dato que hay que exigir por escrito antes de fallar una partida."},
  {"code": "ANSI/ISEA Z87.1", "desc": "Norma de protección ocular y facial. Aplica a la careta de 4\", al TuffShield y a los goggles que se especifiquen como partida independiente."},
  {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento: inspección anual documentada y retiro a los diez años de la fecha de fabricación. Al no haber vida útil declarada, es el criterio aplicable."},
  {"code": "NOM-017-STPS", "desc": "Selección, entrega y capacitación en el uso del EPP. En este modelo la capacitación incluye demostrar el sistema de liberación de coquilla."}
]

L4["blog"] = [
  "cascos-forestales-msa-cairns-guia",
  "rescate-vehicular-tecnicas-equipos",
  "epp-completo-kit-bombero-profesional",
  "casco-bombero-bullard-usrhb-guia",
  "mantenimiento-epp-estructural-nfpa-1851",
  "espacios-confinados-proteccion-respiratoria"
]

L4["faqs"] = [
  {
    "q": "¿Qué gana y qué pierde un perfil metro frente a una tradicional?",
    "a": "Gana en maniobra: menos superficie de ala que enganche, mejor paso por escotillas y huecos, y menos interferencia dentro de un vehículo durante una extricación. Pierde la cuenca del ala completa, que es la que deriva agua de la línea, brasa y escombro fuera del cuello del chaquetón. Por eso muchas corporaciones no eligen entre uno y otro: dotan ala completa a la línea de ataque y perfil recortado al equipo de rescate técnico."
    },
  {
    "q": "¿Para qué sirve el sistema de liberación de coquilla?",
    "a": "Para escapar si algo engancha el casco: un cable colgante, una malla, estructura colapsada o la cinta de una carga. MSA lo publica como sistema patentado y es una función de rescate propio, no de confort. Tiene un compromiso obvio —un casco que puede liberarse también puede perderse— así que el barboquejo y la práctica importan más, no menos. Y sobre todo: hay que demostrarlo en la capacitación de entrega, porque una función que nadie sabe que existe no se usa."
  },
  {
    "q": "¿Por qué se insiste tanto en la banda frontal?",
    "a": "Porque es la interfaz que decide si el sello facial de la máscara se compromete. MSA describe la banda frontal del 660C como diseñada para acomodar distintos diseños de pieza facial de equipo de respiración. Un casco cuya banda queda justo donde va el reborde superior de la máscara la empuja y afecta el sello, que es lo único que separa al elemento de la atmósfera. En una estación con dos o tres marcas de ERA, esa compatibilidad deja de ser preferencia y se vuelve inventario."
  },
  {
    "q": "¿Cuánto pesa el 660C Metro?",
    "a": "MSA no publica el peso de este modelo, y no lo vamos a estimar a partir de otro. Se solicita por escrito al fabricante referido al número de parte y con la configuración ocular montada. Para referencia del catálogo: el Cairns 1836 de la misma marca publica 1.5 a 1.8 kg según configuración y el Bullard UST LowRider publica 1.4 a 1.5 kg. Si el peso va a ser criterio de evaluación, conviene especificar un modelo que sí tenga cifra publicada."
  },
  {
    "q": "¿Qué edición de la norma cumple?",
    "a": "La página de producto no especifica edición, así que la respuesta honesta es que hay que pedirla. Lo exigible en una compra nueva es el certificado del modelo cotizado referido a NFPA 1970 edición 2025 —el estándar vigente que consolidó las NFPA 1971, 1975, 1981 y 1982, con transición cerrada el 18 de marzo de 2026—, con organismo certificador y alcance. Nosotros lo gestionamos como parte de la propuesta y lo entregamos por escrito."
  },
  {
    "q": "¿El visor Defender se puede operar con guante?",
    "a": "Sí, y es un dato que MSA declara explícitamente para este modelo. Importa más de lo que parece: un visor que requiere dedos desnudos no se despliega en escena, así que en la práctica es como no tenerlo. Aun así, el visor no sustituye la protección ocular: no cierra el contorno del ojo. Para ventilación, remoción de escombro y rescate vehicular se especifican goggles, y en este modelo hay que confirmar el número de parte vigente porque varias combinaciones aparecen descontinuadas."
  },
  {
    "q": "¿Qué interior conviene elegir?",
    "a": "El removible, si existe un programa de descontaminación real. MSA ofrece franela estándar, versión deluxe de piel con almohadilla de corona y configuraciones removibles. El interior es la parte del casco que más se contamina y la que menos se lava, así que un interior que se retira completo es la diferencia entre un procedimiento que se cumple y uno que existe en papel. El deluxe gana en confort percibido; el removible gana en higiene."
  },
  {
    "q": "¿Cómo se escribe la partida de este modelo?",
    "a": "Cinco decisiones más dos exigencias documentales. Las decisiones: color de coquilla con cantidad por color, protección facial —careta de 4\", TuffShield o Defender—, goggles como partida independiente, tipo de interior y barboquejo. Las exigencias: que el proveedor entregue peso por número de parte y certificado del modelo con edición normativa vigente, más fecha de fabricación por unidad. Nosotros entregamos la propuesta ya desglosada así, con los números de parte confirmados como vigentes."
  }
]

# ===MARCADOR===

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'cascos-bullard-y-msa')
card = next(c for c in prod['l3']['catalogo']['cards']
            if c['marca'] == 'MSA' and c['modelo'] == 'Cairns 660C Metro')
card['slug'] = SLUG
card['fichaLabel'] = 'el 660C Metro'
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
