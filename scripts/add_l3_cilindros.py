#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Segunda L3 de equipos de respiracion: cilindros de aire respirable.

EJE EDITORIAL — el cilindro es la unica pieza del conjunto que **no la certifica NFPA ni NIOSH**:
es un recipiente a presion bajo jurisdiccion del **Departamento de Transporte**. Y es la pieza
que el mercado compra por minutos, que es justamente la unidad que menos dice de ella.

  La asimetria documental que sostiene la ficha, verificada fuente por fuente:
    · **Luxfer**, que es quien FABRICA los cilindros, publica volumen de agua y capacidad de aire
      en todas sus lineas —y en LCX-30Y deja la columna de duracion en minutos **vacia**, y en la
      linea LCX base la omite—.
    · **3M Scott y MSA**, que son marcas de ERA, publican duracion en minutos y pies cubicos,
      pero **no publican volumen de agua** en sus documentos de EE. UU.
    · **Drager** publica volumen, aire libre y **dos** duraciones distintas —"working duration" y
      "nominal duration"— y no publica diametro ni longitud.
  Quien fabrica publica volumen; quien vende publica minutos.

  Y las cifras no cuadran entre fuentes: 45 minutos son **67 SCF** para 3M Scott y **65 ft³** para
  MSA y Luxfer; 60 minutos son **88** contra **87**. Se reportan tal cual, sin reconciliar.

SEGUNDO EJE — la vida de servicio no es del material, es del permiso. Es el punto donde las
fuentes se contradicen y donde conviene tener el documento:
    · DOT-CFFC: "Cylinder service life is 15 years from the date of manufacture."
    · PHMSA, interpretacion 12-0091 (2012): "no service life extension is authorized for
      cylinders manufactured in accordance with DOT-SP 10915", y al terminar su vida "must be
      condemned"; razon publicada: "there is no effective non-destructive method of detecting the
      degree of strength loss for a composite cylinder".
    · Luxfer: "DOT declined to approve life extension for these cylinders", asi que diseno un
      cilindro NUEVO bajo DOT-SP 14232 en lugar de extender los existentes. Y advierte en la
      propia pagina de ese producto: "no cylinder manufactured under DOT-SP 14232 has thus far
      been approved for a service life longer than 15 years".
    · MSA: "DOT regulations require that composite cylinders be retired from service after the
      fifteenth year."
    · 3M Scott vende una linea "30-Year Life Cylinder" con "up to a 30-year life expectancy",
      **sin aprobacion TC** y **sin publicar el numero de DOT-SP** en el flyer.
    · Drager, bajo regimen EN: 20 y 30 anos de design life en Type 3, y vida no limitada en acero
      y en Type 4.

FUENTES PRIMARIAS consultadas 2026-08-06: PHMSA (DOT-CFFC, interpretacion 12-0091, DOT-SP 21575,
white paper de extension de vida), eCFR 49 CFR 180.209 y 178.35, NIOSH Pub. 2021-111 (hot
filling), paginas de producto y manual de inspeccion de compuestos de Luxfer (2024), folleto de
cilindros y flyer de 30 anos de 3M Scott, ficha ANZ de 3M, manual de operacion y catalogo de MSA,
ficha PI-100211 de Drager, CGA C-6.1 y C-6.2 (via ANSI y eCFR), y NOM-020-STPS-2011.

Uso: python3 scripts/add_l3_cilindros.py
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

L3 = collections.OrderedDict()

L3['seoTitle'] = 'Cilindros de aire respirable para ERA'
L3['seoDescription'] = (
    'Cilindros SCBA de carbono, aluminio y acero en 2216, 4500 y 5500 psig: capacidad publicada, '
    'recalificación a cinco años y la vida que fija el permiso DOT.'
)

L3['h1'] = 'Cilindros de aire respirable para equipos autónomos'
L3['subtitulo'] = (
    'La única pieza del conjunto que no la certifica NFPA ni NIOSH: es un recipiente a presión '
    'bajo jurisdicción del Departamento de Transporte. Se compra por minutos y se debería '
    'comparar por pies cúbicos, por peso y por el permiso marcado en el hombro.'
)

L3['heroImg'] = collections.OrderedDict([
    ('src', '/images/catalogo/1606613640173-600x450.webp'),
    ('alt', 'Bombero de espaldas con cilindro de aire respirable en el arnés'),
    ('caption', 'El dato que decide está grabado, no en la ficha'),
])

L3['heroBloques'] = [
    collections.OrderedDict([
        ('label', 'Por qué los minutos no alcanzan'),
        ('texto',
         'La duración en minutos es una <strong>medida de laboratorio</strong>, no una propiedad '
         'del cilindro: se determina con máquina de respiración a ritmo fijo. Se nota en quién '
         'publica qué: <strong>el fabricante del cilindro publica volumen de agua y capacidad de '
         'aire</strong> —y en algunas líneas deja la columna de minutos vacía—, mientras las '
         'marcas de ERA publican minutos y no publican volumen. Y las cifras de una misma '
         'duración <strong>no coinciden entre fuentes</strong>.'),
    ]),
    collections.OrderedDict([
        ('label', 'Distribución autorizada, no reventa'),
        ('texto',
         'Cotizamos el cilindro por <strong>número de parte y permiso DOT</strong>, verificando que '
         'la presión marcada corresponda al ERA de destino —porque la aprobación de NIOSH es del '
         'sistema completo, cilindro y válvula incluidos—, y revisamos <strong>fecha de '
         'fabricación y de última recalificación al recibir</strong>. Propuesta técnica en menos de '
         '<strong>24 horas hábiles</strong> y cobertura en los <strong>32 estados</strong>.'),
    ]),
]

L3['heroDatos'] = [
    collections.OrderedDict([('label', 'Recalificación'), ('valor', 'Cada cinco años')]),
    collections.OrderedDict([('label', 'Vida de servicio'), ('valor', 'La fija el permiso, no el material')]),
]

L3['specStrip'] = [
    collections.OrderedDict([('label', 'Construcciones'), ('valor', 'Carbono, aluminio y acero')]),
    collections.OrderedDict([('label', 'Presiones'), ('valor', '2216, 4500 y 5500 psig')]),
    collections.OrderedDict([('label', 'Capacidades'), ('valor', 'De 43 a 110 pies cúbicos')]),
    collections.OrderedDict([('label', 'Peso a 2216 psig'), ('valor', '8.3 lb en carbono, 18.1 en aluminio')]),
    collections.OrderedDict([('label', 'Quién certifica'), ('valor', 'DOT y Transport Canada')]),
    collections.OrderedDict([('label', 'Quién recalifica'), ('valor', 'Instalación autorizada con RIN')]),
]

CARDS = json.loads(r'''
[
  {
    "marca": "Luxfer",
    "modelo": "LCX-HP",
    "variante": "5500 psi",
    "varianteLabel": "Presión",
    "fichaLabel": "el Luxfer LCX-HP",
    "badge": "DOT-SP 15136 · TC SU 10350",
    "estado": "La tabla más completa",
    "img": "/images/catalogo/1606613640173-600x400.webp",
    "alt": "Cilindro de aire respirable montado en el arnés de un equipo autónomo",
    "desc": "Es la referencia documental de la línea: Luxfer publica <strong>número de parte, diámetro, longitud, peso, volumen de agua, capacidad de aire, duración, vida y rosca</strong> en una sola tabla —algo que ninguna marca de ERA hace—. Cuatro claves: <strong>L46A</strong> 45 ft³ y 5.8 lb, <strong>L66D</strong> 65 ft³ y 8.0 lb, <strong>L88B</strong> 87 ft³ y 10.1 lb, <strong>L110C</strong> 110 ft³ y 12.8 lb. Los 5500 psi solo existen bajo permiso especial: la norma DOT-CFFC limita la presión marcada a 5000 psi.",
    "specs": [
      "L46A, L66D, L88B y L110C · 45 a 110 ft³",
      "Vida publicada de 15 años · rosca M18 × 1.5",
      "5500 psi requiere permiso especial, no especificación",
      "Publica volumen de agua en pulgadas cúbicas"
    ],
    "chip": "Verificar que el ERA sea de 5500 psi"
  },
  {
    "marca": "Luxfer",
    "modelo": "LCX-SL",
    "variante": "4500 psi",
    "varianteLabel": "Presión",
    "fichaLabel": "el Luxfer LCX-SL",
    "badge": "DOT · métrico e imperial",
    "estado": "La presión más común",
    "img": "/images/catalogo/1592235905030-600x450.webp",
    "alt": "Bombero con pieza facial y equipo de respiración con cilindro",
    "desc": "La línea Super Light a la presión que domina el mercado. Publica cada fila en <strong>las dos unidades</strong>, que es lo que hace posible comparar contra una ficha europea sin convertir a mano: <strong>L45R</strong> 285 in³ / 4.6 l y 45 ft³ / 1274 l; <strong>L65R</strong> 418 in³ / 6.8 l y 65 ft³ / 1840 l; <strong>L87E</strong> 550 in³ / 9 l y 87 ft³ / 2462 l. Rosca 0.875-14UNF y vida publicada de 15 años.",
    "specs": [
      "L45R, L65R, L66B, L87E y L87R",
      "Volumen y capacidad en métrico e imperial",
      "5.9 a 10.7 lb según capacidad",
      "Rosca 0.875-14UNF · vida de 15 años"
    ],
    "chip": "La opción estándar de una flota nueva"
  },
  {
    "marca": "Luxfer",
    "modelo": "LCX-XD",
    "variante": "Abrasión",
    "varianteLabel": "Construcción",
    "fichaLabel": "el Luxfer LCX-XD",
    "badge": "DOT · KHK en un modelo",
    "estado": "Para escombro y arrastre",
    "img": "/images/catalogo/1608723724615-600x450.webp",
    "alt": "Dos bomberos con equipo de respiración avanzando en ambiente con humo",
    "desc": "La misma presión de 4500 psi con una construcción distinta y un reclamo que el fabricante publica textual: <strong>“three times the abrasion resistance of standard Luxfer LCX cylinders”</strong>, con domos reforzados por un proceso propio. El precio de esa resistencia también está publicado y conviene verlo: el <strong>L87G-XD pesa 11.6 lb contra las 10.7 del L87E</strong> equivalente. Es la decisión clásica de esta pieza: durabilidad contra peso.",
    "specs": [
      "L45M-XD, L65G-XD y L87G-XD",
      "Tres veces la resistencia a la abrasión, declarada",
      "Pesa más que la línea Super Light equivalente",
      "Fabricado en Estados Unidos, según el fabricante"
    ],
    "chip": "Cuando el cilindro se arrastra"
  },
  {
    "marca": "Luxfer",
    "modelo": "LCX-EL",
    "variante": "Vida extendida",
    "varianteLabel": "Construcción",
    "fichaLabel": "el Luxfer LCX-EL",
    "badge": "DOT-SP 14232",
    "estado": "Leer la advertencia",
    "img": "/images/catalogo/1756112277157-1000x750.webp",
    "alt": "Equipo de protección respiratoria almacenado en el rack de la estación",
    "desc": "Aquí hay que leer el documento completo, y el propio fabricante lo pone por escrito. El cilindro se diseñó bajo un permiso nuevo porque —textual— <strong>“DOT declined to approve life extension for these cylinders”</strong>, y su tabla publica 30 años de vida. Pero la misma página advierte que el permiso fija requisitos de ensayo previos y que <strong>“no cylinder manufactured under DOT-SP 14232 has thus far been approved for a service life longer than 15 years”</strong>. Los 30 años son un potencial, no una autorización vigente.",
    "specs": [
      "L23B, L45Z, L65Z y L87Z · DOT-SP 14232",
      "Tabla publicada con 30 años de vida",
      "Ningún cilindro aprobado aún por más de 15",
      "Pesa más que la Super Light equivalente"
    ],
    "chip": "Pedir el estado del permiso por escrito"
  },
  {
    "marca": "3M Scott",
    "modelo": "30-Year Life Cylinder",
    "variante": "Vida extendida",
    "varianteLabel": "Construcción",
    "fichaLabel": "el cilindro 3M de 30 años",
    "badge": "Sin aprobación TC",
    "estado": "Dos datos ausentes",
    "img": "/images/catalogo/1705503828024-600x450.webp",
    "alt": "Piezas de equipo de respiración colgadas en el rack de la estación",
    "desc": "Línea separada del catálogo de carbono estándar, que anuncia <strong>“up to a 30-year life expectancy”</strong> con recalificación a cinco años, en 4500 psi y en las dos conexiones: <strong>200128-35, 200129-35 y 200130-35</strong> en Snap-Change y <strong>804721-35, 804722-35 y 804723-35</strong> en CGA roscado. Dos cosas que conviene saber antes de compararlo con el estándar: el flyer <strong>no publica el número de permiso DOT</strong>, y dice explícitamente que <strong>no tiene aprobación TC y no puede usarse ni transportarse a Canadá</strong>.",
    "specs": [
      "4500 psi en 30, 45 y 60 minutos",
      "Snap-Change y CGA roscado, claves publicadas",
      "Número de permiso DOT: no publicado",
      "Sin aprobación TC, no entra a Canadá"
    ],
    "chip": "Pedir el número de DOT-SP"
  },
  {
    "marca": "Dräger",
    "modelo": "NANO Type 4",
    "variante": "300 bar",
    "varianteLabel": "Presión",
    "fichaLabel": "el Dräger NANO",
    "badge": "EN 12245 · régimen europeo",
    "estado": "Otro marco normativo",
    "img": "/images/catalogo/1776104501594-600x400.webp",
    "alt": "Piezas faciales y equipo respiratorio en un taller de mantenimiento",
    "desc": "El contraste útil, porque juega con otras reglas: camisa plástica en lugar de aluminio, certificado a <strong>EN 12245</strong> y no a un permiso DOT, y con <strong>vida no limitada</strong> —“can be used indefinitely when proper maintenance and periodic inspections are fulfilled”—. Es el más ligero de su tabla: <strong>2.8 kg de camisa contra 3.74 del Type 3 y 7.10 del acero</strong>, al mismo volumen y presión. Y el fabricante publica una condición: <strong>la válvula de exceso de flujo es obligatoria en Type 4</strong>.",
    "specs": [
      "6.0, 6.8 y 9.0 litros a 300 bar",
      "Vida no limitada bajo régimen EN, no DOT",
      "2.8 kg de camisa contra 7.10 del acero",
      "Válvula de exceso de flujo obligatoria"
    ],
    "chip": "Confirmar compatibilidad con el ERA"
  }
]
''')

L3['catalogo'] = collections.OrderedDict([
    ('eyebrow', 'Catálogo por construcción y presión'),
    ('titulo', 'Cilindros de aire respirable\npor construcción, presión y permiso'),
    ('intro',
     'Cuatro datos deciden qué cilindro sirve: <strong>la presión marcada, la capacidad en pies '
     'cúbicos o litros, el peso y el número de permiso DOT</strong>. Los minutos son consecuencia '
     'de los tres primeros, no una característica. Y el permiso es lo que fija la vida de '
     'servicio: no la fija el material ni la marca del ERA.'),
    ('imgRef', 'Imagen de referencia de la línea'),
    ('nota',
     'El cilindro se cotiza contra el <strong>ERA de destino</strong>, no por marca ni por '
     'minutos: la aprobación de NIOSH es del sistema completo —incluye cilindro y válvula—, así '
     'que un cilindro que no está en la configuración aprobada deja un conjunto que nadie evaluó. '
     'Y las presiones <strong>no son intercambiables</strong>: un equipo de 4500 psi lleva '
     'cilindro de 4500 psi.'),
    ('cards', CARDS),
])

L3['secciones'] = json.loads(r'''
[
  {
    "id": "quien-certifica",
    "eyebrow": "Jurisdicción",
    "titulo": "Ni NFPA ni NIOSH: el cilindro lo certifica el DOT",
    "parrafos": [
      "Todo el resto del equipo de respiración se documenta con dos papeles —certificado NFPA y aprobación NIOSH— y el cilindro con ninguno de los dos. Es un <strong>recipiente a presión</strong>, y quien lo autoriza es el Departamento de Transporte estadounidense; en Canadá, Transport Canada. De ahí sale una consecuencia que sorprende a más de un comprador: <strong>los cilindros compuestos no son cilindros “de especificación”</strong>. Existen bajo <strong>permiso especial</strong>, con un número que empieza por DOT-SP o DOT-E y que va seguido de la presión de servicio.",
      "Eso no los hace menos confiables: los hace <strong>rastreables a un titular y a un texto concreto</strong>, que es mejor. El permiso dice quién puede fabricarlos, cuántos años viven, cada cuándo se recalifican, quién puede hacerlo y qué condiciones anulan su uso. Es el documento que conviene pedir cuando alguien afirma que un cilindro dura más de lo que dura."
    ],
    "tabla": {
      "head": ["Marcado que verás", "Qué significa", "En qué construcción aparece"],
      "rows": [
        ["<strong>DOT-3AL</strong>", "Cilindro de especificación publicada en el reglamento", "Aluminio"],
        ["<strong>DOT-3AA</strong>", "Cilindro de especificación publicada en el reglamento", "Acero"],
        ["<strong>DOT-SP</strong> o <strong>DOT-E</strong> + presión", "No es de especificación: existe bajo permiso especial nominado a un titular", "Todo compuesto y todo 5500 psi"],
        ["<strong>TC SU</strong> + presión en bar", "Permiso equivalente de Transport Canada", "Compuesto que además entra a Canadá"],
        ["<strong>EN 12245</strong> / <strong>ISO 9809</strong>", "Régimen europeo, con reglas de vida distintas a las del DOT", "Líneas europeas de carbono, Type 4 y acero"]
      ]
    },
    "nota": "Un detalle que explica por qué el 5500 psi siempre va por permiso: la norma de cilindros compuestos establece que <strong>la presión marcada no puede exceder 5000 psi</strong> a temperatura de referencia. Todo lo que esté por encima existe porque un permiso lo autoriza expresamente."
  },
  {
    "id": "minutos",
    "eyebrow": "La unidad equivocada",
    "titulo": "Quien fabrica publica litros; quien vende publica minutos",
    "parrafos": [
      "Esta línea se pide por minutos y ese es el dato que menos dice. La duración nominal <strong>se determina con máquina de respiración a ritmo fijo</strong>: es una medida de laboratorio, no una propiedad del cilindro. Y la forma más clara de verlo es mirar quién publica qué.",
      "El fabricante de los cilindros publica <strong>volumen de agua y capacidad de aire</strong> en todas sus líneas —en litros y en pulgadas cúbicas—, y en dos de ellas <strong>deja la columna de minutos vacía o la omite</strong>. Las marcas de ERA hacen lo contrario: publican minutos y pies cúbicos, y no publican volumen de agua. Un tercer fabricante, bajo régimen europeo, publica <strong>dos duraciones distintas para el mismo cilindro</strong> —una “de trabajo” y una “nominal”—, lo que dice bastante sobre cuánto confiar en un solo número."
    ],
    "tabla": {
      "head": ["Quién publica", "Volumen de agua", "Capacidad de aire", "Duración en minutos"],
      "rows": [
        ["Fabricante del cilindro", "Sí, en litros y pulgadas cúbicas", "Sí, en litros y pies cúbicos", "Solo en algunas líneas; en otras, columna vacía"],
        ["Marcas de ERA de EE. UU.", "No", "Sí, en pies cúbicos", "Sí, es su unidad principal"],
        ["Marca europea", "Sí", "Sí, aire libre en litros", "Dos: “de trabajo” y “nominal”"]
      ]
    },
    "nota": "Y las cifras de una misma duración no coinciden entre fuentes: <strong>45 minutos son 67 pies cúbicos para una marca y 65 para otras dos</strong>; 60 minutos son 88 contra 87. Es una diferencia pequeña que se vuelve grande en una tabla comparativa de licitación, y la única forma de evitarla es <strong>evaluar por capacidad, no por minutos</strong>."
  },
  {
    "id": "peso",
    "eyebrow": "Lo que se siente en turno",
    "titulo": "El peso está publicado, y la diferencia es de más del doble",
    "parrafos": [
      "Este es el dato que en otras líneas del catálogo nadie publica y que aquí sí está, con número de parte y todo. A <strong>la misma presión de 2216 psig y la misma capacidad de 45 pies cúbicos</strong>, un mismo fabricante publica en la misma tabla: <strong>18.1 libras vacío en aluminio y 8.3 en carbono</strong>. Lleno, 21.4 contra 11.6. Es más del doble, y es peso que se carga en la espalda toda la jornada.",
      "La otra comparación publicada es entre construcciones bajo régimen europeo, al mismo volumen y presión: <strong>7.10 kg de camisa en acero, 3.74 en carbono sobre camisa de aluminio y 2.8 en carbono sobre camisa plástica</strong>. Y a mayor presión, menor perfil para la misma capacidad: un fabricante publica que su cilindro de 30 minutos mide 6.71 pulgadas de diámetro a 2216 psi y 5.00 a 5500 psi."
    ],
    "lista": [
      { "t": "Por qué el aluminio sigue existiendo", "d": "Porque su vida de servicio se publica como <strong>no limitada</strong> mientras pase las pruebas periódicas, y porque es la construcción de menor costo. En una flota de reserva o de entrenamiento, esa combinación tiene sentido." },
      { "t": "Qué se gana con más presión", "d": "Menor diámetro y menor longitud para la misma capacidad. En equipos de perfil bajo eso se nota al pasar por un vano o al recostarse contra una pared." },
      { "t": "Qué se paga con más resistencia", "d": "Peso. La línea de alta abrasión publica <strong>11.6 libras contra 10.7</strong> de la línea ligera en la misma capacidad de 87 pies cúbicos." },
      { "t": "Cómo se compara de verdad", "d": "Con la tabla del fabricante del cilindro, que publica peso, volumen y dimensiones en la misma fila. Una hoja que solo trae minutos no permite comparar nada." }
    ],
    "nota": "Cuidado con una asimetría más: un fabricante publica el peso de la <strong>camisa</strong>, otro el del cilindro <strong>con válvula vacío</strong> y otro el <strong>lleno</strong>. Tres números distintos de la misma pieza. Al pedir peso conviene decir cuál de los tres."
  },
  {
    "id": "vida",
    "eyebrow": "Donde las fuentes se contradicen",
    "titulo": "La vida de servicio la fija el permiso, no el material",
    "parrafos": [
      "Aquí hay que ser preciso porque hay dinero en juego y porque las fuentes no dicen lo mismo. El punto de partida no está en discusión: la norma de cilindros compuestos establece que <strong>la vida de servicio es de 15 años desde la fecha de fabricación</strong>. Lo que sigue es donde conviene tener el documento en la mano.",
      "La autoridad publicó en una interpretación que <strong>para los cilindros de cierto permiso no está autorizada ninguna extensión de vida</strong> y que al terminarla deben condenarse, con una razón técnica que vale citar: <strong>no existe un método no destructivo eficaz para detectar la pérdida de resistencia de un cilindro compuesto</strong>. El fabricante lo confirma desde su lado y con más crudeza: participó una década en las deliberaciones y <strong>“DOT declined to approve life extension”</strong>, así que diseñó un cilindro nuevo bajo otro permiso en lugar de extender los existentes.",
      "Y en ese cilindro nuevo, cuya tabla publica 30 años, la misma página advierte que <strong>ningún cilindro fabricado bajo ese permiso ha sido aprobado todavía para una vida mayor a 15 años</strong>. Mientras tanto, una marca de ERA afirma tajante que el reglamento obliga a retirar el compuesto <strong>después del año quince</strong>, otra vende una línea que anuncia <strong>hasta 30 años</strong> sin publicar su número de permiso, y una tercera, bajo régimen europeo, publica 20 y 30 años de vida de diseño y vida no limitada en acero y en camisa plástica."
    ],
    "tabla": {
      "head": ["Qué dice la fuente", "Quién lo publica", "Cómo usarlo al comprar"],
      "rows": [
        ["15 años desde la fecha de fabricación", "La norma de cilindros compuestos", "Es el punto de partida de cualquier cálculo de reposición"],
        ["No hay extensión autorizada; al terminar, se condena", "Interpretación de la autoridad", "Es la postura más dura y la que conviene asumir al presupuestar"],
        ["“DOT declined to approve life extension”", "El fabricante de los cilindros", "Explica por qué existe una línea nueva en lugar de una extensión"],
        ["Tabla con 30 años, sin cilindro aprobado aún", "El mismo fabricante, en el producto", "Los 30 años son potencial: se pide el estado del permiso"],
        ["Retiro después del año quince", "Una marca de ERA, en su manual", "Es la instrucción que seguirá su servicio técnico"],
        ["“Up to a 30-year life expectancy”", "Otra marca de ERA, en un flyer", "Sin número de permiso publicado y sin aprobación para Canadá"],
        ["Vida no limitada en acero, aluminio y Type 4", "Fabricantes, bajo régimen EN y para aluminio", "Aplica mientras pase las pruebas periódicas"]
      ]
    },
    "nota": "Regla que resuelve la contradicción sin tomar partido: <strong>la vida de un cilindro es la que dice el permiso marcado en ese cilindro</strong>, no la que dice el folleto de la línea. Y la fecha que la arranca es la de fabricación grabada en el hombro, no la de la factura."
  },
  {
    "id": "marcado",
    "eyebrow": "Control de recepción",
    "titulo": "Cómo se lee un cilindro con el cilindro en la mano",
    "parrafos": [
      "Es la verificación más valiosa de toda la categoría porque no depende de que el proveedor mande papeles: el cilindro trae su expediente encima. En compuesto el marcado <strong>no se troquela</strong> —iría contra la fibra—, sino que se integra en la sobreenvoltura de fibra de vidrio, y el fabricante publica exactamente qué debe aparecer.",
      "El orden importa porque cada elemento responde una pregunta distinta: el <strong>número de permiso seguido de la presión</strong> dice bajo qué régimen existe el cilindro y a qué equipo puede ir; el <strong>número de serie y el identificador del fabricante</strong> lo hacen rastreable; la <strong>marca del organismo de inspección con mes y año</strong> fija el inicio de la vida; y el <strong>REE en centímetros cúbicos</strong> es el umbral contra el que se compara la expansión medida en la recalificación. No es una fecha ni una capacidad: es un criterio de aprobación."
    ],
    "lista": [
      { "t": "Número de serie legible", "d": "Criterio de condena publicado por el fabricante: <strong>si el número de serie ya no es legible, el cilindro debe condenarse</strong>. Se revisa antes de firmar la recepción." },
      { "t": "Fecha de fabricación", "d": "Es la que arranca los 15, 20 o 30 años del permiso. Un cilindro con dos años de inventario entra a la estación con dos años menos de vida." },
      { "t": "Fecha de recalificación y RIN", "d": "Va cerca de los marcados originales. Un fabricante indica dónde buscarla: <strong>en la etiqueta de aprobación del cuello del cilindro</strong>." },
      { "t": "Estado de la válvula", "d": "Manómetro con carátula y aguja visibles, vástago sin doblar y <strong>bota de hule presente</strong>: el manual dice que si falta la bota, el cilindro sale de servicio. En conexión rápida, revisar que la cola de milano no esté dañada." }
    ],
    "nota": "Y el marcado sirve para una verificación que nadie más puede hacer por ti: que <strong>el número de permiso y la presión marcada correspondan al ERA de destino</strong>. Es el filtro que evita recibir un cilindro correcto para un equipo que no es el tuyo."
  },
  {
    "id": "compatibilidad",
    "eyebrow": "Lo que no se puede mezclar",
    "titulo": "Las presiones no son intercambiables, y la razón es de certificación",
    "parrafos": [
      "La pregunta llega siempre y la respuesta publicada es clara: no. Y el motivo no es mecánico, es documental. <strong>La aprobación de NIOSH se emite al sistema completo, e incluye el cilindro y su válvula</strong>: usar un cilindro distinto del que se sometió a evaluación con ese modelo de equipo deja el conjunto fuera de lo aprobado. Por eso las válvulas no se cruzan entre marcas, aunque la rosca coincida.",
      "Tampoco se cruzan las presiones. La regla publicada es que la intercambiabilidad existe <strong>solo dentro de un mismo rango de presión</strong>: un equipo de 4500 psi lleva cilindro de 4500 psi. Y hay una restricción de duración que conviene conocer antes de dimensionar una flota: un equipo de <strong>2216 psi solo admite cilindros de 30 minutos</strong>, mientras los de presión más alta admiten 30, 45 y 60."
    ],
    "lista": [
      { "t": "Por qué importa en una flota mixta", "d": "Porque el umbral del aviso de fin de servicio <strong>se expresa como porcentaje de la presión</strong> y cambia con ella: se publican 34 % para 2216 psi, 31 % para 4500 y 29 % para 5500. Dos equipos avisan en momentos distintos." },
      { "t": "Qué pasa con el llenado", "d": "La estación tiene que poder llenar a la presión del cilindro. Un cilindro de 5500 psi no se aprovecha con un sistema que llena a 4500." },
      { "t": "Conexiones publicadas", "d": "Una marca publica sus conexiones normalizadas: <strong>una para 2216 y 3000 psig y otra para 4500</strong>. La de 5500 no está publicada en las fuentes consultadas." },
      { "t": "La regla de compra", "d": "Un cilindro se cotiza <strong>contra el modelo de ERA y su configuración aprobada</strong>, nunca por marca ni por minutos. Es la misma regla que en refacciones." }
    ],
    "nota": "Consecuencia práctica para una corporación que va a comprar en varias etapas: <strong>elegir una presión de flota y sostenerla</strong>. Mezclar presiones multiplica cilindros de repuesto, cambia el punto de alarma entre equipos y complica el llenado."
  },
  {
    "id": "llenado",
    "eyebrow": "Lo que se hace mal a diario",
    "titulo": "El llenado rápido deja el cilindro corto",
    "parrafos": [
      "Se llama <em>hot filling</em> y es probablemente el error más común de una estación. La autoridad de seguridad ocupacional lo publica sin ambigüedad: llenar rápido <strong>genera calor excesivo y produce una pérdida de presión al enfriarse el cilindro</strong>, así que el usuario se queda con menos aire del que cree. Y agrega la consecuencia: <strong>un cilindro llenado en caliente debe completarse después de que enfríe</strong>.",
      "Lo notable es lo que <strong>no</strong> publica: ni una cifra. No hay psi por grado, ni temperatura de referencia de llenado, ni tasa recomendada, ni porcentaje típico de faltante. Lo único que sí publica el reglamento es la temperatura de referencia de la presión marcada, que no es lo mismo. Así que el control real es de procedimiento: <strong>quien llena tiene que estar capacitado</strong>, y eso también lo dice la publicación."
    ],
    "lista": [
      { "t": "Qué necesita una estación de llenado", "d": "Compresor de varias etapas con capacidad para la presión de la flota, banco de almacenamiento en cascada, mangueras con los conectores de cada presión y <strong>contención capaz de retener el cilindro y sus fragmentos</strong> si reventara durante el llenado." },
      { "t": "El aire es parte del equipo", "d": "El aire que entra al cilindro tiene su propia norma de calidad y su propio análisis periódico. Un cilindro impecable llenado con aire fuera de especificación es un problema invisible." },
      { "t": "Protección térmica", "d": "Un interruptor de temperatura en la descarga de la última etapa que detenga el sistema al pasar el punto fijado. Es lo que evita meter aire caliente al cilindro." },
      { "t": "Qué se documenta", "d": "Presión final verificada después del enfriamiento, no durante el llenado. Es la diferencia entre un cilindro al 100 % y uno que solo lo pareció." }
    ],
    "nota": "Detalle de operación con consecuencia directa: si los cilindros se llenan al terminar la intervención y se guardan de inmediato, buena parte de la flota amanece <strong>por debajo de su presión nominal</strong> sin que nadie lo haya hecho mal a propósito."
  },
  {
    "id": "dano",
    "eyebrow": "Cuándo se condena",
    "titulo": "Fibra de carbono expuesta: se rechaza",
    "parrafos": [
      "El fabricante publica un manual de inspección con criterios numéricos y una jerarquía de tres niveles —aceptable, reparable y rechazo— que es exactamente lo que una corporación necesita para no discutir en la recepción ni en la baja. La regla que conviene memorizar es la más simple de verificar a simple vista: <strong>si la fibra de carbono quedó expuesta, el cilindro se rechaza</strong>. El daño limitado a la capa de fibra de vidrio, en cambio, puede ser reparable.",
      "Y hay una condición que aparece por escrito tanto en el permiso como en el manual del fabricante, y que en un cuerpo de bomberos se vuelve muy concreta: <strong>un cilindro que estuvo sometido a fuego no vuelve a servicio</strong>. La evidencia que lo determina también está publicada: carbonización o quemado del compuesto, de la pintura, de las etiquetas o de los materiales de la válvula, resina fundida o ausente. Solo el daño por humo, sin más, se considera aceptable tras limpieza."
    ],
    "tabla": {
      "head": ["Tipo de daño", "Criterio publicado", "Resultado"],
      "rows": [
        ["Abrasión", "Fibra de carbono expuesta", "<strong>Rechazo</strong>"],
        ["Corte", "Corte que atraviesa la capa de vidrio y entra al carbono", "<strong>Rechazo</strong>"],
        ["Impacto", "Indentación visible en la superficie interna de la camisa metálica", "<strong>Rechazo</strong>"],
        ["Delaminación", "Restringida a la capa de vidrio y menor a 2 pulgadas de ancho", "Reparable"],
        ["Corrosión interna aislada", "Picadura estimada de más de 0.03 pulgadas de profundidad", "<strong>Rechazo</strong>"],
        ["Ataque químico", "Burbujeo, picado o deterioro extremo de la resina", "<strong>Rechazo</strong>"],
        ["Fuego", "Carbonización, resina fundida o ausente, etiquetas quemadas", "<strong>No vuelve a servicio</strong>"],
        ["Número de serie", "Ilegible", "<strong>Se condena</strong>"]
      ]
    },
    "nota": "Quién puede dictaminar también está publicado: <strong>solo instalaciones de recalificación autorizadas</strong> por la autoridad pueden examinar el cilindro por dentro y por fuera y hacer la prueba hidrostática. La inspección visual sigue una norma específica para cilindros reforzados con fibra, distinta de la de aluminio."
  },
  {
    "id": "mexico",
    "eyebrow": "Marco mexicano",
    "titulo": "En México un cilindro portátil queda fuera de la NOM de recipientes",
    "parrafos": [
      "Es un hallazgo que cambia cómo se arma un expediente y que casi nadie menciona: la norma oficial mexicana de <strong>recipientes sujetos a presión</strong> aplica a los centros de trabajo donde funcionen esos recipientes, pero <strong>excluye expresamente los recipientes portátiles que contengan gases comprimidos</strong>. Un cilindro de aire respirable de ERA es precisamente eso.",
      "La consecuencia es directa: <strong>no hay registro ni dictamen mexicano que respalde a un cilindro SCBA</strong>. Su trazabilidad se sostiene sobre el marcado extranjero —permiso DOT, permiso de Transport Canada o norma europea— y sobre la aprobación NIOSH del sistema completo. Por eso la lectura del marcado deja de ser un detalle técnico y se convierte en <strong>el control de recepción real</strong>."
    ],
    "lista": [
      { "t": "Qué NO se puede pedir", "d": "Un dictamen de recipiente a presión bajo la NOM para un cilindro de ERA: la propia norma lo excluye. Pedirlo deja la partida sin ofertas válidas." },
      { "t": "Qué sí sostiene la compra", "d": "El <strong>marcado del cilindro</strong> —permiso y presión, número de serie, fecha de fabricación, fecha de recalificación y REE— más la configuración aprobada del equipo al que va." },
      { "t": "Qué entregable pedir", "d": "Constancia de la última recalificación con la identificación del recalificador, y la fecha de la próxima. Es lo que un auditor puede verificar contra el cilindro físico." },
      { "t": "Cómo se redacta la partida", "d": "Por <strong>capacidad y presión</strong>, con número de parte y permiso, y con la referencia al modelo de ERA de destino. Nunca solo por minutos." }
    ],
    "nota": "Consecuencia para quien administra una flota en México: el expediente del cilindro <strong>lo construye la corporación</strong>, cilindro por cilindro, con el marcado y las constancias de recalificación. No existe una autoridad nacional que lo tenga por ella."
  }
]
''')

L3['galeriaIntro'] = (
    'Referencias del cilindro en uso. Lo que ninguna foto alcanza a mostrar es lo único que '
    'permite recibirlo bien: el número de permiso con su presión, la fecha de fabricación y la de '
    'la última recalificación, todo marcado sobre la sobreenvoltura y en la etiqueta del cuello.'
)

L3['galeria'] = json.loads(r'''
[
  {
    "src": "/images/catalogo/1606613816768-1000x750.webp",
    "alt": "Dos bomberos con cilindros de aire respirable en la espalda",
    "caption": "El peso se carga toda la jornada"
  },
  {
    "src": "/images/catalogo/1584033376505-600x400.webp",
    "alt": "Rostro de bombero con casco estructural y lámpara integrada",
    "caption": "La presión de flota se decide una vez"
  },
  {
    "src": "/images/catalogo/1705503729371-600x400.webp",
    "alt": "Equipo de protección colgado en el rack de la estación",
    "caption": "Almacenado, el cilindro sigue envejeciendo"
  },
  {
    "src": "/images/catalogo/1777059017572-600x450.webp",
    "alt": "Bombera de perfil con equipo de respiración junto a la unidad",
    "caption": "Recalificación cada cinco años, por instalación autorizada"
  }
]
''')

L3['aplicaciones'] = json.loads(r'''
[
  {
    "sector": "Cuerpos de bomberos",
    "desc": "Cilindros de repuesto dimensionados por el consumo real de la corporación, con una sola presión de flota para no multiplicar inventario ni cambiar el punto de alarma entre equipos. El expediente lo construye la corporación, cilindro por cilindro."
  },
  {
    "sector": "Espacios confinados",
    "desc": "Donde el trabajo es prolongado y la logística de relevo importa más que el peso: aquí conviene mirar capacidad en pies cúbicos y no minutos, y la construcción de aluminio con vida no limitada tiene sentido económico si pasa las pruebas periódicas."
  },
  {
    "sector": "Industria química",
    "desc": "Programa de protección respiratoria auditado, con constancias de recalificación por cilindro y análisis periódico del aire del compresor que los llena. Un cilindro impecable llenado con aire fuera de especificación es un problema invisible."
  }
]
''')

L3['datoClave'] = collections.OrderedDict([
    ('titulo', 'La vida no es del material: es del permiso'),
    ('texto',
     'La norma de cilindros compuestos fija <strong>15 años desde la fecha de fabricación</strong>, '
     'y la autoridad publicó que para cierto permiso <strong>no hay extensión autorizada</strong> '
     '—porque no existe método no destructivo eficaz para detectar la pérdida de resistencia—. '
     'Hay líneas que anuncian 20 y 30 años bajo otros permisos o bajo régimen europeo. '
     '<strong>Lo que vale es el número marcado en ese cilindro</strong>, no lo que dice el folleto.'),
])

L3['normasRef'] = ['NFPA 1970', 'NIOSH 42 CFR 84', 'NFPA 1850', 'NFPA 1989',
                   'NOM-033-STPS', 'NOM-017-STPS']

L3['documentacion'] = [
    'Número de permiso DOT o TC con la presión de servicio, y número de parte del fabricante',
    'Fecha de fabricación del cilindro y vida de servicio que fija ese permiso',
    'Constancia de la última recalificación con identificación del recalificador y fecha de la próxima',
    'Referencia al modelo de ERA de destino y a su configuración aprobada por NIOSH',
    'Capacidad de aire publicada en pies cúbicos o litros, además de la duración nominal',
    'Peso declarado, indicando si es de camisa, con válvula vacío o lleno',
    'Manual de inspección visual del fabricante y criterios de condena',
]

L3['blog'] = [
    'cilindros-fibra-carbono-scba-guia',
    'guia-scba-equipos-respiracion-autonoma',
    'mantenimiento-scba-programa-anual',
    'nfpa-1981-mexico-equipos-respiracion',
    'espacios-confinados-proteccion-respiratoria',
    'scba-msa-g1-guia-tecnica',
]

L3['faqs'] = json.loads(r'''
[
  {
    "q": "¿Por qué un cilindro no trae certificado NFPA?",
    "a": "Porque no le corresponde. El cilindro es un recipiente a presión y quien lo autoriza es el Departamento de Transporte estadounidense, o Transport Canada del lado canadiense, o el régimen europeo con sus normas EN e ISO. NFPA certifica el equipo de respiración como ensamble y NIOSH aprueba el aparato respiratorio completo —cilindro y válvula incluidos—, pero el documento propio del cilindro es su permiso o su especificación, marcado sobre la pieza. Pedirle un certificado NFPA a un cilindro es pedirle un papel que no existe."
  },
  {
    "q": "¿Cómo comparo dos cilindros si las duraciones no coinciden entre marcas?",
    "a": "Por capacidad y peso, no por minutos. La misma duración de 45 minutos se publica como 67 pies cúbicos en una marca y 65 en otras dos; los 60 minutos, como 88 contra 87. La duración nominal se determina con máquina de respiración a ritmo fijo, así que es una etiqueta derivada. Lo comparable es la capacidad de aire, el volumen de agua, el peso y las dimensiones, y ahí el fabricante del cilindro publica tablas completas que las marcas de ERA no publican."
  },
  {
    "q": "¿Un cilindro compuesto se puede usar más de 15 años?",
    "a": "Depende del permiso marcado en ese cilindro, y las fuentes no dicen lo mismo. La norma de compuestos fija 15 años desde la fecha de fabricación; la autoridad publicó que para cierto permiso no hay extensión autorizada y que al terminar deben condenarse, con una razón técnica: no hay método no destructivo eficaz para detectar la pérdida de resistencia. El fabricante confirma que la extensión no fue aprobada y por eso diseñó una línea nueva bajo otro permiso, cuya tabla publica 30 años pero cuya propia página aclara que ningún cilindro fabricado bajo él ha sido aprobado aún para más de 15. Y hay líneas europeas con 20 y 30 años de vida de diseño. La respuesta honesta es: se lee el permiso del cilindro, no el folleto."
  },
  {
    "q": "¿Puedo poner un cilindro de 5500 psi en un equipo de 4500?",
    "a": "No. La intercambiabilidad existe solo dentro del mismo rango de presión, y hay una razón adicional que pesa más: la aprobación de NIOSH se emite al sistema completo e incluye el cilindro y su válvula, así que montar un cilindro que no está en la configuración aprobada deja un conjunto que nadie evaluó así. Hay además una restricción de duración publicada: un equipo de 2216 psi solo admite cilindros de 30 minutos, mientras los de presión más alta admiten 30, 45 y 60."
  },
  {
    "q": "¿Qué es el REE que viene grabado?",
    "a": "Rejection Elastic Expansion, expresado en centímetros cúbicos. No es una fecha ni una capacidad: es el umbral de expansión elástica contra el cual el recalificador compara el resultado de la prueba hidrostática. Si el cilindro se expande más de ese valor, se rechaza. Va marcado de fábrica junto al número de permiso, el número de serie y la marca del organismo de inspección con mes y año, y en un cilindro compuesto todo eso se integra en la sobreenvoltura de fibra de vidrio en lugar de troquelarse."
  },
  {
    "q": "¿Por qué mi cilindro llega con menos presión de la que marcó al llenarlo?",
    "a": "Casi siempre por llenado rápido. La autoridad de seguridad ocupacional publica que llenar rápido genera calor excesivo y produce pérdida de presión al enfriarse el cilindro, y que un cilindro llenado en caliente debe completarse después de que enfríe. Lo que no publica es ninguna cifra: ni psi por grado ni tasa recomendada. Así que el control es de procedimiento —quien llena debe estar capacitado— y la verificación se hace después del enfriamiento, no durante el llenado. Si la estación llena al terminar la intervención y guarda de inmediato, buena parte de la flota amanece por debajo de su presión nominal."
  },
  {
    "q": "¿Un cilindro que estuvo en un incendio se puede seguir usando?",
    "a": "No. Es una condición que aparece por escrito tanto en el permiso como en el manual de inspección del fabricante: un cilindro sometido a fuego no vuelve a servicio. La evidencia que lo determina también está publicada —carbonización o quemado del compuesto, de la pintura, de las etiquetas o de los materiales de la válvula, resina fundida o ausente— y solo el daño por humo, sin más, se considera aceptable después de limpiarlo. En la misma línea: si la fibra de carbono quedó expuesta por abrasión o por un corte, se rechaza."
  },
  {
    "q": "¿Existe una NOM que respalde a un cilindro de ERA en México?",
    "a": "No, y conviene saberlo antes de redactar una partida. La norma oficial mexicana de recipientes sujetos a presión excluye expresamente los recipientes portátiles que contengan gases comprimidos, que es exactamente lo que es un cilindro de aire respirable. No hay registro ni dictamen nacional que lo respalde: su trazabilidad se sostiene sobre el marcado extranjero —permiso DOT, permiso de Transport Canada o norma europea— y sobre la aprobación NIOSH del sistema completo. Por eso el control de recepción real es leer el marcado del cilindro, y el expediente lo construye la corporación, cilindro por cilindro."
  }
]
''')

# ── Escritura ──────────────────────────────────────────────────────────────────
with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'equipos-de-respiracion')
prod = next(p for p in cat['productos'] if p['slug'] == 'cilindros-30-45-60-min')
prod['l3'] = L3

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('l3 agregado a', prod['slug'], '·', prod['nombre'])
print('  secciones:', len(L3['secciones']), '| faqs:', len(L3['faqs']),
      '| cards:', len(L3['catalogo']['cards']), '| galeria:', len(L3['galeria']))
print('  seoTitle:', len(L3['seoTitle']) + 21, '(máx 62) | seoDescription:',
      len(L3['seoDescription']), '(140-160)')
ids = [s['id'] for s in L3['secciones']]
assert len(ids) == len(set(ids)), 'ids duplicados'
RESERVADOS = {'ficha', 'galeria', 'sectores', 'preguntas', 'configuraciones', 'catalogo'}
assert not (set(ids) & RESERVADOS), 'id reservado'
for c in L3['catalogo']['cards']:
    assert len(c['specs']) == 4, 'la card %s no tiene 4 specs' % c['modelo']
imgs = [c['img'] for c in L3['catalogo']['cards']] + [g['src'] for g in L3['galeria']]
print('  imágenes repetidas en la página:',
      [i for i in set(imgs) if imgs.count(i) > 1] or 'ninguna')
codes = {n['code'] for n in cat.get('normas', [])}
print('  normasRef sin entrada en la categoría:',
      [c for c in L3['normasRef'] if c not in codes] or 'ninguna')
faqs_l2 = {f['q'] for f in cat.get('faqs', [])}
print('  FAQs repetidas de la L2:',
      [q for q in (f['q'] for f in L3['faqs']) if q in faqs_l2] or 'ninguna')
hermana = next(p for p in cat['productos'] if p['slug'] == 'scba-scott-air-pak')
qs_era = {f['q'] for f in hermana['l3']['faqs']}
print('  FAQs repetidas de la ficha del ERA:',
      [q for q in (f['q'] for f in L3['faqs']) if q in qs_era] or 'ninguna')
