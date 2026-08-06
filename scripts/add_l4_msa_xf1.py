# -*- coding: utf-8 -*-
"""Agrega slug + bloque l4 a la card MSA Cairns XF1 (L3 de cascos).

Fuente primaria: us.msasafety.com, pagina de producto del Cairns XF1, 2026-08-06.
Datos publicados:
  - silueta jet sin ala
  - tallas Medium y Large
  - iluminacion integrada con luz frontal y lateral
  - comunicaciones integradas con headset interno
  - visor interno declarado ANSI Z87 en ciertos numeros de parte; configuraciones con careta clara
  - soft goods desmontables, lavables y reinstalables
  - colores negro, rojo, blanco, amarillo y azul, en acabado brillante y mate
  - aviso literal del fabricante: "Approvals subject to change without notice and may differ
    based on configuration, part number and/or country."
  - MSA no publica peso ni material de coquilla en la pagina consultada

Eje editorial: es un casco de plataforma integrada (luz + comunicacion) y por eso su compra se
decide por NUMERO DE PARTE: las aprobaciones cambian por configuracion y por pais, asi que la
ficha ensena a verificar alcance antes de asumir que un jet europeo sirve para estructural en
Mexico.
Idempotente. Correr DESPUES de add_l3_cascos.py.
"""
import json, io, collections

RUTA = 'src/data/productos.json'
SLUG = 'msa-cairns-xf1'

L4 = collections.OrderedDict([
  ("seoTitle", "Casco MSA Cairns XF1 jet con luz y comms"),
  ("seoDescription", "Casco MSA Cairns XF1 de silueta jet: iluminación frontal y lateral integrada, headset interno, tallas M y L y aprobaciones que cambian por número de parte."),
  ("h1", "Casco estructural MSA Cairns XF1"),
  ("subtitulo", "La silueta jet de MSA: sin ala, con iluminación frontal y lateral integrada, comunicaciones con headset interno, interiores desmontables y lavables, en tallas M y L. Es un casco de plataforma, y su alcance de aprobación depende del número de parte."),
  ("badge", "Alcance por número de parte"),
  ("heroImg", {
    "src": "/images/catalogo/1726262693471-600x450.webp",
    "alt": "Casco estructural de perfil jet con visor integrado en escena nocturna",
    "caption": "Silueta jet con luz integrada"
  }),
  ("heroBloques", [
    {
      "label": "Por qué este casco se compra por número de parte",
      "texto": "El XF1 no es una coquilla con accesorios: es una <strong>plataforma integrada</strong> —luz frontal y lateral, headset de comunicación interno, visor interno— y cada combinación es un número de parte distinto. MSA lo dice con todas sus letras en su propia página: <em>“Approvals subject to change without notice and may differ based on configuration, part number and/or country.”</em> Traducido a una compra mexicana: <strong>el alcance de certificación se verifica por parte y por país</strong>, no se hereda del nombre del modelo."
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": "En este modelo nuestro trabajo empieza antes de cotizar: <strong>confirmamos por escrito qué aprobación ampara el número de parte</strong> y para qué uso, y entregamos certificado del modelo cotizado, etiqueta legible y fecha de fabricación por unidad. Si la configuración que pide la convocatoria no está amparada para combate estructural en el alcance que aplica, lo decimos antes de la propuesta. Respuesta en menos de <strong>24 horas hábiles</strong>, con cobertura en los <strong>32 estados de la República</strong>."
    }
  ]),
  ("heroDatos", [
    {"label": "Silueta", "valor": "Jet sin ala"},
    {"label": "Tallas", "valor": "Medium y Large"},
    {"label": "Aprobación", "valor": "Varía por parte y país"}
  ]),
  ("specStrip", [
    {"label": "Perfil", "valor": "Jet, sin ala"},
    {"label": "Iluminación", "valor": "Frontal y lateral integrada"},
    {"label": "Comunicación", "valor": "Headset interno opcional"},
    {"label": "Visor interno", "valor": "Declarado ANSI Z87 por parte"},
    {"label": "Interiores", "valor": "Desmontables y lavables"},
    {"label": "Acabados", "valor": "Cinco colores, brillante o mate"}
  ]),
])

L4["secciones"] = [
  {
    "id": "la-plataforma",
    "eyebrow": "Qué estás comprando",
    "titulo": "Un casco jet pensado como plataforma",
    "parrafos": [
      "La silueta jet sin ala existe por dos razones operativas: <strong>reduce la superficie que puede engancharse</strong> y libera espacio alrededor de la cabeza para montar cosas. El XF1 aprovecha las dos: sobre esa coquilla MSA integra iluminación frontal y lateral y un headset de comunicación interno, con interiores que se desmontan, se lavan y se reinstalan.",
      "Eso lo pone en una categoría distinta al resto del catálogo. Una tradicional y una metro se compran por construcción; esta se compra por <strong>qué trae integrado y con qué alcance está aprobada esa integración</strong>. Es la diferencia entre comparar cascos y comparar sistemas. Sigue siendo un casco estructural y se compra con el mismo expediente que el resto de la línea: certificado del modelo, etiqueta y fecha de fabricación."
    ],
    "lista": [
      {"t": "Silueta jet sin ala", "d": "Menos superficie expuesta a engancharse con cable, malla o estructura, y menor interferencia en el interior de un vehículo o en un hueco estrecho."},
      {"t": "Iluminación integrada", "d": "Luz frontal y lateral montada en la coquilla, orientada a conciencia situacional: iluminar donde se mira y ser visible de costado, no sustituir la lámpara de intervención."},
      {"t": "Comunicación integrada", "d": "Headset interno para hablar sin sostener nada. En maniobras con las dos manos ocupadas —herramienta hidráulica, línea, camilla— eso es tiempo de operación, no comodidad."},
      {"t": "Interiores desmontables", "d": "Soft goods que se retiran completos para lavar y se reinstalan. En un casco con electrónica integrada, poder separar la parte lavable de la que no lo es deja de ser un detalle."}
    ]
  },
  {
    "id": "aprobaciones",
    "eyebrow": "Lo que hay que verificar antes de cotizar",
    "titulo": "Las aprobaciones cambian por configuración, parte y país",
    "parrafos": [
      "MSA publica en la propia página del producto un aviso que conviene leer dos veces: <em>“Approvals subject to change without notice and may differ based on configuration, part number and/or country.”</em> Es decir, <strong>el alcance de aprobación no es una propiedad del modelo, es una propiedad del número de parte</strong> —y puede cambiar según el país donde se venda.",
      "Para un comprador mexicano eso tiene una consecuencia práctica: no se puede asumir que un casco de silueta jet, aunque lo venda una marca con presencia global, está amparado para combate estructural bajo el mismo alcance en todos sus números de parte. La verificación es documental, por parte, y se hace antes de la propuesta, no después de la entrega."
    ],
    "tabla": {
      "head": ["Qué verificar", "Cómo se pide", "Por qué importa"],
      "rows": [
        ["Número de parte exacto", "La clave completa de la configuración cotizada, no el nombre del modelo", "Es la unidad a la que se refiere la aprobación según el propio aviso del fabricante"],
        ["Norma y edición amparadas", "Constancia que indique norma, edición y alcance para ese número de parte", "Un casco puede estar aprobado bajo un esquema y no bajo el que exige la convocatoria"],
        ["País del alcance", "Confirmación de que la aprobación aplica al mercado donde se va a usar", "El propio aviso menciona el país como variable de la aprobación"],
        ["Alcance de los módulos", "Si la luz y el headset están cubiertos por la aprobación o van como accesorio", "Un componente electrónico integrado puede tener alcance distinto al de la coquilla"]
      ]
    },
    "nota": "Esta es la ficha del catálogo donde más insistimos en lo mismo: <strong>si el alcance no está por escrito para el número de parte, no está</strong>. No es desconfianza hacia la marca, es cómo funciona una certificación de tercera parte."
  },
  {
    "id": "cuando-tiene-sentido",
    "eyebrow": "Criterio de selección",
    "titulo": "Cuándo un jet sin ala es la respuesta y cuándo no",
    "parrafos": [
      "Un jet no es una tradicional recortada: cambia lo que protege y lo que estorba. Frente a una tradicional como el Cairns 1836 se cede la cuenca del ala y se gana perfil; frente a un perfil metro se gana integración y se cede la banda frontal pensada para la pieza facial. En México, además, hay un factor cultural y normativo real —muchas corporaciones tienen la silueta tradicional escrita en su procedimiento—, así que esta decisión rara vez es solo técnica."
    ],
    "tabla": {
      "head": ["Situación", "Recomendación", "Por qué"],
      "rows": [
        ["Rescate técnico, alturas, espacios confinados", "Cairns XF1", "Sin ala que engancharse, con luz y comunicación integradas y sin accesorios colgando"],
        ["Maniobras con las dos manos ocupadas y necesidad de comunicación constante", "Cairns XF1", "El headset interno evita sostener o manipular un equipo de radio con guante"],
        ["Interior estructural con línea y agua encima", "Cairns 1836 o UST Traditional", "La cuenca del ala completa deriva agua y escombro fuera del cuello del chaquetón"],
        ["Procedimiento interno que exige silueta tradicional", "1836 o UST Traditional", "La silueta está normada por la corporación; discutirlo con el jefe de estación va antes que cotizar"]
      ]
    },
    "nota": "Un patrón que funciona: <strong>dotar por función</strong>. La línea de ataque con ala completa y el equipo de rescate técnico con jet. Cuesta más en refacciones y resuelve mejor las dos maniobras, en lugar de comprometer las dos con un solo modelo."
  },
  {
    "id": "integracion",
    "eyebrow": "Luz y comunicación",
    "titulo": "Lo que cambia cuando la electrónica va adentro",
    "parrafos": [
      "Integrar luz y comunicación resuelve problemas —nada que colgar, nada que se enganche, manos libres— y crea otros que hay que presupuestar desde el principio. Un casco con electrónica tiene consumibles, tiene un componente que puede fallar sin que la coquilla tenga nada, y tiene una ruta de servicio distinta a la de un casco puramente mecánico.",
      "Ninguno de esos puntos es un argumento en contra: son renglones del presupuesto de operación que casi nunca aparecen en la comparativa de compra, y que a tres años explican por qué dos flotas del mismo tamaño cuestan distinto."
    ],
    "lista": [
      {"t": "Consumibles y carga", "d": "Antes de comprar hay que confirmar cómo se alimentan los módulos —pilas o batería recargable—, la autonomía declarada y el ciclo de reemplazo. Es un costo recurrente, no una compra única."},
      {"t": "Servicio del módulo", "d": "Qué pasa si falla la luz o el headset: si se repone el módulo, si va a servicio o si obliga a retirar el casco. Conviene pedirlo por escrito junto con el número de parte del repuesto."},
      {"t": "Atmósferas clasificadas", "d": "Cualquier equipo electrónico que entre a un área con atmósfera clasificada necesita su propia declaración. Si la instalación exige aptitud para División 1, hay que verificar el módulo específico, no el casco."},
      {"t": "Higiene con electrónica", "d": "Los interiores desmontables permiten lavar la parte textil sin mojar la parte electrónica. Es la razón práctica por la que en este modelo el soft good removible no es opcional en un programa de descontaminación."}
    ]
  },
  {
    "id": "configuracion",
    "eyebrow": "Cómo se pide",
    "titulo": "Talla, color, acabado y módulos: cuatro decisiones y una verificación",
    "parrafos": [
      "El XF1 se surte en <strong>tallas Medium y Large</strong> —dos, no un rango continuo de ajuste—, en cinco colores y en acabado brillante o mate. La talla es la primera decisión y conviene tomarla midiendo, con capucha puesta y no a ojo: con solo dos tallas, el margen de error es menor que en un casco con 25 posiciones de perímetro."
    ],
    "tabla": {
      "head": ["Decisión", "Opciones publicadas", "Cómo se escribe en la partida"],
      "rows": [
        ["Talla", "Medium y Large", "Cantidad por talla, resultado de medir la plantilla y no de estimarla"],
        ["Color y acabado", "Negro, rojo, blanco, amarillo y azul; brillante o mate", "Color por función o compañía, con el acabado explícito"],
        ["Módulos integrados", "Iluminación frontal y lateral; headset de comunicación interno", "Cada módulo como renglón, con número de parte, consumible y repuesto"],
        ["Protección ocular", "Visor interno declarado ANSI Z87 en ciertas partes; configuraciones con careta clara", "Renglón propio, indicando la declaración que ampara el visor de esa parte"],
        ["Verificación documental", "Aprobación por número de parte y país", "Renglón que obliga al proveedor a entregar la constancia de alcance antes de la entrega"]
      ]
    },
    "nota": "Con dos tallas, la <strong>medición de la plantilla</strong> deja de ser un trámite: si una parte del personal queda fuera del rango de las dos tallas, este modelo no es la opción para esa parte de la dotación y hay que cotizarle otra serie."
  },
  {
    "id": "lo-no-publicado",
    "eyebrow": "Lo que el fabricante no publica",
    "titulo": "Cuatro datos ausentes en la página consultada",
    "parrafos": [
      "En la página de producto que consultamos no aparecen datos que en el resto del catálogo sí están. Los nombramos para poder pedirlos, no para descalificar el modelo: un casco de plataforma se documenta por número de parte, y buena parte de esa documentación se entrega bajo solicitud."
    ],
    "tabla": {
      "head": ["Dato ausente", "Qué decide", "Cómo se resuelve"],
      "rows": [
        ["Material de la coquilla", "Comportamiento tras exposiciones repetidas y criterio de inspección", "Se pide la especificación de material para el número de parte cotizado"],
        ["Peso del casco", "Fatiga cervical, más relevante aquí porque hay módulos montados", "Se pide el peso con luz y headset instalados, no el de la coquilla desnuda"],
        ["Norma y edición por parte", "Si la configuración sirve para la convocatoria", "Se solicita constancia de alcance con norma, edición, número de parte y país"],
        ["Autonomía de los módulos", "Costo de operación y disponibilidad en turno", "Se pide autonomía declarada, tipo de alimentación y número de parte del consumible"]
      ]
    },
    "nota": "Los cuatro caben en un correo referido al número de parte, y los gestionamos como parte de la propuesta. En este modelo la regla de la casa se vuelve especialmente literal: <strong>el dato se consigue, no se supone</strong>."
  },
  {
    "id": "mantenimiento",
    "eyebrow": "Ciclo de vida",
    "titulo": "Inspección de un casco con módulos y retiro",
    "parrafos": [
      "La inspección de este casco tiene un componente que los demás no: además de revisar coquilla, interior, barboquejo, visor y la interfaz con la pieza facial del equipo de respiración, hay que <strong>verificar que los módulos enciendan y comuniquen</strong>, y revisar sus puntos de anclaje. Un módulo flojo es un enganche y un punto de entrada de contaminación.",
      "La limpieza sigue el criterio de toda la línea —detergente suave y agua, sin solventes, adhesivos ni pinturas— con la ventaja de que los interiores se desmontan completos. Lo que no se moja es la electrónica, y por eso el procedimiento de lavado debe estar escrito para este modelo en particular."
    ],
    "nota": "El retiro se rige por <strong>NFPA 1850 (1851)</strong>: diez años desde la fecha de fabricación, más el retiro anticipado por impacto o daño. Los módulos tienen su propio ciclo: pueden reponerse sin retirar el casco, siempre que el repuesto sea el que corresponde al número de parte."
  }
]

L4["galeria"] = [
  {"src": "/images/catalogo/1608723724615-600x450.webp", "alt": "Dos bomberos con casco identificado operando en ambiente con humo", "caption": "Visibilidad y comunicación en humo"},
  {"src": "/images/catalogo/1759673824678-1000x750.webp", "alt": "Bombero equipado saliendo de una estructura durante una maniobra de rescate", "caption": "Maniobra en espacio reducido"},
  {"src": "/images/catalogo/1776784163597-600x450.webp", "alt": "Equipo de rescate operando sobre un vehículo siniestrado", "caption": "Rescate técnico con manos ocupadas"},
  {"src": "/images/catalogo/1690210795713-600x450.webp", "alt": "Dos bomberos con casco estructural y visera durante una operación", "caption": "Dotación por función"}
]

L4["aplicaciones"] = [
  {"sector": "Rescate técnico", "desc": "Alturas, espacios confinados y extricación: sin ala que se engancha, con luz y comunicación integradas y sin accesorios colgando de la coquilla."},
  {"sector": "Brigadas industriales", "desc": "Cuando la maniobra exige manos libres y comunicación constante. Si el área tiene atmósfera clasificada, los módulos electrónicos necesitan su propia declaración de aptitud."},
  {"sector": "Licitación pública", "desc": "Partida por número de parte, con renglón explícito de constancia de alcance —norma, edición, parte y país— antes de la entrega."}
]

L4["datoClave"] = {
  "titulo": "La aprobación es del número de parte",
  "texto": "MSA advierte que las aprobaciones <strong>pueden diferir según configuración, número de parte y país</strong>. En este modelo, pedir la constancia de alcance por parte no es exceso de celo: es la única forma de saber qué ampara el certificado que te van a entregar."
}

L4["referencias"] = [
  {"code": "Aviso de aprobaciones", "desc": "MSA publica en la página del producto que las aprobaciones pueden cambiar sin aviso y diferir según configuración, número de parte y país. Es el punto de partida de cualquier verificación."},
  {"code": "NFPA 1970 · 2025", "desc": "Estándar vigente para conjuntos de protección estructural y de proximidad. Es la referencia contra la que hay que pedir el alcance del número de parte cotizado."},
  {"code": "ANSI Z87", "desc": "Declaración que MSA indica para el visor interno en ciertos números de parte. Conviene confirmar cuál aplica a la configuración exacta que se va a comprar."},
  {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento: inspección anual documentada y retiro a los diez años de la fecha de fabricación."},
  {"code": "NOM-017-STPS", "desc": "Selección, entrega y capacitación en el uso del EPP. En este modelo la capacitación incluye operación de los módulos de luz y comunicación."}
]

L4["blog"] = [
  "rescate-vehicular-tecnicas-equipos",
  "espacios-confinados-proteccion-respiratoria",
  "cascos-forestales-msa-cairns-guia",
  "epp-completo-kit-bombero-profesional",
  "equipamiento-unidad-rescate-completa",
  "mantenimiento-epp-estructural-nfpa-1851"
]

L4["faqs"] = [
  {
    "q": "¿Un casco jet sirve para combate estructural?",
    "a": "Depende del alcance de aprobación del número de parte, no de la silueta. MSA advierte en la propia página del XF1 que las aprobaciones pueden cambiar sin aviso y diferir según configuración, número de parte y país. Así que la respuesta correcta no es sí ni no: es pedir la constancia de alcance —norma, edición, número de parte y país— para la configuración exacta que se va a comprar. Nosotros hacemos esa verificación antes de cotizar y la entregamos por escrito."
  },
  {
    "q": "¿Qué gana un jet frente a una tradicional o un perfil metro?",
    "a": "Gana en enganche y en integración: sin ala hay menos superficie que se atore con cable, malla o estructura, y la coquilla libera espacio para montar luz y comunicación sin accesorios colgando. Pierde la cuenca del ala completa, que es la que deriva agua de la línea y escombro fuera del cuello del chaquetón. Por eso el jet se ve más en rescate técnico y espacios confinados que en interior estructural con línea."
  },
  {
    "q": "¿Cómo funcionan las tallas M y L?",
    "a": "Son dos tallas discretas, no un rango continuo de ajuste como los cascos con banda de ratchet de 25 posiciones. Eso obliga a medir la plantilla antes de comprar y no estimarla: si parte del personal queda fuera del rango que cubren las dos tallas, para esa parte de la dotación hay que cotizar otra serie. Es un dato que conviene resolver en la etapa de especificación, no el día de la entrega."
  },
  {
    "q": "¿La iluminación integrada sustituye la lámpara de intervención?",
    "a": "No. La luz integrada está orientada a conciencia situacional —iluminar donde se mira y ser visible de costado— y resuelve la tarea inmediata con manos libres. Una lámpara de intervención tiene otro alcance, otra potencia y otra autonomía. Lo que sí conviene pedir antes de comprar es la autonomía declarada del módulo, el tipo de alimentación y el número de parte del consumible, porque es un costo recurrente del programa."
  },
  {
    "q": "¿Se puede usar en un área con atmósfera clasificada?",
    "a": "Cualquier equipo electrónico que entre a un área clasificada necesita su propia declaración de aptitud, y eso aplica a los módulos de luz y de comunicación, no al casco. La verificación es por módulo y por número de parte. Como referencia de lo estricto que es este punto: el sistema de iluminación integrada de otra marca del catálogo está declarado únicamente para Clase I División 2, y no cubre atmósferas clasificadas como División 1."
  },
  {
    "q": "¿Qué mantenimiento tiene un casco con electrónica integrada?",
    "a": "Tres capas. La mecánica de siempre: coquilla, interior, barboquejo y visor. La eléctrica: verificar que los módulos enciendan y comuniquen, y revisar sus anclajes, porque un módulo flojo es un enganche y una entrada de contaminación. Y la de limpieza: los interiores se desmontan completos para lavarse con detergente suave y agua, sin mojar la parte electrónica. El procedimiento de lavado debe estar escrito para este modelo en particular."
  },
  {
    "q": "¿Qué pasa si falla la luz o el headset?",
    "a": "Hay que definirlo antes de comprar, y es una pregunta que casi nadie hace: si el módulo se repone en sitio, si va a servicio o si obliga a retirar el casco. Nosotros lo pedimos por escrito junto con el número de parte del repuesto y el tiempo de reposición. Un casco con un módulo muerto sigue siendo un casco, pero una flota donde el 30 % trae la luz apagada dejó de tener la capacidad por la que se pagó."
  },
  {
    "q": "¿Cómo se especifica este modelo en una licitación?",
    "a": "Por número de parte, con cinco renglones: talla y cantidad, color y acabado, módulos integrados con su consumible y repuesto, protección ocular indicando la declaración que la ampara, y un renglón de verificación documental que obliga al proveedor a entregar la constancia de alcance —norma, edición, número de parte y país— antes de la entrega. Sin ese último renglón, la partida queda abierta a que el alcance no sea el que la convocatoria supone."
  }
]

# ===MARCADOR===

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'cascos-bullard-y-msa')
card = next(c for c in prod['l3']['catalogo']['cards']
            if c['marca'] == 'MSA' and c['modelo'] == 'Cairns XF1')
card['slug'] = SLUG
card['fichaLabel'] = 'el Cairns XF1'
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
