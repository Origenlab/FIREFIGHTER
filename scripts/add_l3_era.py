#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Primera L3 de la segunda categoria: equipos de respiracion autonoma (ERA / SCBA).

EJE EDITORIAL — es distinto al de las seis fichas de EPP y por eso esta ficha no se parece a
ninguna de ellas: es la unica linea del catalogo donde **la certificacion NFPA no basta**.

  Un ERA para combate estructural necesita DOS cosas a la vez:
    · certificacion NFPA 1970 (capitulos 15 a 19, antes NFPA 1981), que evalua el desempeno
      en incendio: lente frente a calor radiante, EOSTI, HUD, RIC UAC, comunicacion de voz;
    · **aprobacion NIOSH bajo 42 CFR Parte 84**, que evalua el aparato respiratorio.

  Y la aprobacion NIOSH tiene una propiedad que cambia como se compra: se emite al conjunto
  COMPLETAMENTE ENSAMBLADO. Texto del reglamento, 42 CFR 84.30:
    (a) "...only for individual, completely assembled respirators..."
    (b) "The Institute will not issue certificates of approval for any respirator component
         or for any respirator subassembly."
  Y la postura de NIOSH sobre refacciones no originales (publicacion 2016-107):
    "The use of components which are not part of the approved assembly results in a respirator
     that has not been evaluated and certified by NIOSH."

  Consecuencia comercial, que es la que le sirve al comprador mexicano: una pieza facial, un
  cilindro o un regulador comprados por separado pueden dejar al equipo fuera de la
  configuracion aprobada. El numero que lo amarra es el **numero TC** de la etiqueta, y en
  Mexico practicamente ningun distribuidor lo publica.

SEGUNDO HILO: el tiempo nominal no es el tiempo real. La duracion se mide con maquina de
respiracion a 40 L/min y 24 respiraciones por minuto (42 CFR 84.88(b)); un elemento trabajando
consume mas. El piso regulatorio del aviso de fin de servicio es 25 % del tiempo nominal
(42 CFR 84.83(f)).

FUENTES PRIMARIAS consultadas 2026-08-06: eCFR 42 CFR Parte 84 (subpartes D, F, H), NIOSH
2011-179 y 2016-107, NFPA TIA 1970-25-1 y tabla de contenido de NFPA 1970-2025, borrador
balotado de NFPA 1850, 49 CFR 178.35 y 180.209, PHMSA DOT-CFFC, OSHA 29 CFR 1910.134 y su
apendice A, NFPA 1989 (2019) via guia oficial de la Texas Commission on Fire Protection,
fichas y bid specs de MSA (G1 / G1 XR), 3M Scott (Air-Pak X3 Pro, XD, 75i), Drager (PSS 7000
IFU, PSS AirBoss), Luxfer, y los textos oficiales de NOM-017-STPS, NOM-033-STPS y NOM-116-STPS.

Uso: python3 scripts/add_l3_era.py
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

L3 = collections.OrderedDict()

L3['seoTitle'] = 'Equipos de respiración autónoma NFPA'
L3['seoDescription'] = (
    'ERA de circuito abierto certificados NFPA 1970 y aprobados por NIOSH: qué exige cada uno, '
    'por qué la aprobación es del conjunto armado y qué pedir.'
)

L3['h1'] = 'Equipos de respiración autónoma de circuito abierto'
L3['subtitulo'] = (
    'La única línea del catálogo que necesita dos certificaciones a la vez: la de NFPA, que '
    'evalúa cómo se comporta el equipo en un incendio, y la aprobación de NIOSH, que se emite '
    'al conjunto completamente ensamblado y no a las piezas por separado.'
)

L3['heroImg'] = collections.OrderedDict([
    ('src', '/images/catalogo/1606613816768-1200x800.webp'),
    ('alt', 'Dos bomberos con equipo de respiración autónoma y cilindro en la espalda'),
    ('caption', 'La pieza que no se compra por partes'),
])

L3['heroBloques'] = [
    collections.OrderedDict([
        ('label', 'Por qué aquí la certificación NFPA no basta'),
        ('texto',
         'Un ERA para combate estructural necesita <strong>certificación NFPA 1970 y aprobación '
         'NIOSH</strong>, y son cosas distintas: la primera mide el desempeño en incendio —lente '
         'frente a calor radiante, aviso de fin de servicio, conexión de rescate—; la segunda '
         'evalúa el aparato respiratorio y <strong>se emite al conjunto completamente '
         'ensamblado</strong>. Cambiar una pieza por una que no está en esa configuración deja '
         'un equipo que nadie evaluó así.'),
    ]),
    collections.OrderedDict([
        ('label', 'Distribución autorizada, no reventa'),
        ('texto',
         'Cotizamos por <strong>número de parte del fabricante</strong> y entregamos el '
         'certificado con edición y organismo nombrado más la <strong>etiqueta de aprobación '
         'NIOSH con su número TC</strong> —el dato que casi ningún distribuidor mexicano '
         'publica—. Propuesta técnica en menos de <strong>24 horas hábiles</strong> y cobertura '
         'en los <strong>32 estados de la República</strong>.'),
    ]),
]

L3['heroDatos'] = [
    collections.OrderedDict([('label', 'Doble requisito'), ('valor', 'NFPA 1970 + NIOSH TC')]),
    collections.OrderedDict([('label', 'Aviso de fin de servicio'), ('valor', 'Mínimo 25 % por NIOSH')]),
]

L3['specStrip'] = [
    collections.OrderedDict([('label', 'Certificación'), ('valor', 'NFPA 1970 capítulos 15 a 19')]),
    collections.OrderedDict([('label', 'Aprobación'), ('valor', 'NIOSH 42 CFR 84, prefijo TC')]),
    collections.OrderedDict([('label', 'Presiones'), ('valor', '2216, 4500 y 5500 psig')]),
    collections.OrderedDict([('label', 'Duraciones'), ('valor', '30, 45, 60 y 75 minutos')]),
    collections.OrderedDict([('label', 'Conexión de rescate'), ('valor', 'RIC UAC obligatoria')]),
    collections.OrderedDict([('label', 'Retiro del equipo'), ('valor', '15 años, 20 si se actualizó')]),
]

CARDS = json.loads(r'''
[
  {
    "marca": "MSA",
    "modelo": "G1 XR",
    "variante": "Edición 2025",
    "varianteLabel": "Plataforma",
    "badge": "NFPA 1970-2025 · SEI · NIOSH",
    "estado": "La declaración más fuerte",
    "img": "/images/catalogo/1606613640173-600x400.webp",
    "alt": "Bombero de espaldas con cilindro de equipo de respiración autónoma",
    "desc": "Es la referencia con la que conviene comparar todo lo demás, porque MSA es el único fabricante que <strong>separa por escrito las dos cosas</strong>: aprobación de NIOSH y <strong>certificación del Safety Equipment Institute (SEI) como conforme a la edición 2025 de NFPA 1970</strong>. Presiones de 2216, 4500 y 5500 psig; duraciones de 30, 45, 60 y 75 minutos; HUD de cuatro LED por incrementos de presión; comunicación electrónica integrada en todas las unidades. Las mejoras de la XR son <strong>retrocompatibles con los G1 ya en servicio</strong>.",
    "specs": [
      "NIOSH aprueba, SEI certifica: dos actos distintos",
      "2216, 4500 y 5500 psig · 30 a 75 minutos",
      "HUD de cuatro LED y telemetría integrada",
      "Retrocompatible con los G1 en servicio"
    ],
    "chip": "Cotizar por número de parte de configuración"
  },
  {
    "marca": "3M Scott",
    "modelo": "Air-Pak X3 Pro",
    "variante": "Estructural",
    "varianteLabel": "Plataforma",
    "badge": "NFPA 1970-2025 · NIOSH",
    "estado": "Documentación abierta",
    "img": "/images/catalogo/1592235905030-600x450.webp",
    "alt": "Bombero con pieza facial de equipo de respiración bajo el casco estructural",
    "desc": "La plataforma mejor documentada del mercado en acceso abierto: 3M publica <strong>especificación de licitación y manual completo</strong>, y ahí están los datos que otros no dan. Lente de la pieza facial descrito como <strong>policarbonato resistente a alta temperatura y calor radiante, tipo no astillable</strong>; HUD que muestra la presión en <strong>incrementos de 100, 75, 50 y 35 % (±2 %)</strong>; RIC UAC integrada al reductor de presión y protegida por la espaldera. Piezas faciales AV-3000 HT o Vision C5 en tallas S, M y L.",
    "specs": [
      "HUD en incrementos de 100, 75, 50 y 35 %",
      "Lente de policarbonato no astillable",
      "RIC UAC integrada al reductor",
      "Piezas faciales AV-3000 HT o Vision C5"
    ],
    "chip": "Certificado a NFPA 1970-2025 desde 2026"
  },
  {
    "marca": "3M Scott",
    "modelo": "Air-Pak XD",
    "variante": "Estructural",
    "varianteLabel": "Plataforma",
    "badge": "NFPA 1970-2025",
    "estado": "Edición vigente",
    "img": "/images/catalogo/1608723724615-600x450.webp",
    "alt": "Dos bomberos con equipo de respiración operando en ambiente con humo",
    "desc": "La segunda plataforma que 3M Scott declaró conforme a la edición 2025 en febrero de 2026, junto con el X3 Pro. Vale leer el verbo con cuidado: el comunicado dice <strong>“compliant with”</strong> y <strong>no nombra organismo certificador</strong>, a diferencia de MSA, que sí nombra a SEI. No es un defecto del equipo —es una diferencia de redacción que conviene resolver pidiendo el certificado con expediente y organismo.",
    "specs": [
      "Declarada conforme a NFPA 1970-2025",
      "El comunicado dice «compliant», no «certified by»",
      "Organismo certificador: pedirlo por escrito",
      "Comparte piezas faciales con el X3 Pro"
    ],
    "chip": "Pedir certificado con organismo nombrado"
  },
  {
    "marca": "Dräger",
    "modelo": "PSS 7000",
    "variante": "Línea NFPA",
    "varianteLabel": "Plataforma",
    "badge": "NFPA · NIOSH",
    "estado": "Sin edición en la ficha",
    "img": "/images/catalogo/1563062067-bb-600x450.webp",
    "alt": "Bombero de perfil con casco rojo y equipo de respiración autónoma",
    "desc": "Dräger mantiene <strong>líneas separadas</strong>: la NFPA/NIOSH para Norteamérica y la EN 137 para Europa, y confundirlas es el error de compra más común con esta marca. Su instructivo oficial dice textual <strong>“The Dräger PSS 7000 S Series is certified by NIOSH”</strong>, pero la página de producto <strong>no publica la edición NFPA</strong>: aparece en el instructivo y en la clave del distribuidor autorizado. Cilindros de 30 a 60 minutos en 2216 o 4500 psi, aluminio o compuesto; pieza facial FPS 7000 con HUD.",
    "specs": [
      "Aprobación NIOSH declarada en el instructivo",
      "La edición NFPA no está en la página de producto",
      "30 a 60 minutos · 2216 o 4500 psi",
      "No confundir con la línea EN 137 europea"
    ],
    "chip": "Verificar edición en la clave del equipo"
  },
  {
    "marca": "Dräger",
    "modelo": "PSS AirBoss",
    "variante": "Línea NFPA",
    "varianteLabel": "Plataforma",
    "badge": "NFPA 1970-2025",
    "estado": "Nuevo en Norteamérica",
    "img": "/images/catalogo/1777059017572-600x450.webp",
    "alt": "Bombera de perfil con equipo de respiración autónoma junto a la unidad",
    "desc": "Disponible para compra en Norteamérica desde <strong>febrero de 2026</strong>, certificado a la edición 2025. Cambia dos cosas que se sienten en turno largo: <strong>cinturón flotante</strong> que carga el peso en la cadera y desarmado sin herramienta para limpieza. Dos advertencias honestas: el comunicado de lanzamiento <strong>no menciona aprobación NIOSH</strong> —el PSS 7000 sí la declara—, y el fabricante <strong>todavía no publica pesos, cilindros ni números de parte</strong> de esta plataforma.",
    "specs": [
      "Certificado a NFPA 1970 edición 2025",
      "Cinturón flotante, carga en la cadera",
      "Desarmado sin herramienta para limpieza",
      "NIOSH, pesos y números de parte: no publicados"
    ],
    "chip": "Pedir aprobación NIOSH por escrito"
  },
  {
    "marca": "3M Scott",
    "modelo": "Air-Pak 75i",
    "variante": "Industrial, no NFPA",
    "varianteLabel": "Plataforma",
    "badge": "NIOSH · sin NFPA",
    "estado": "El contraejemplo útil",
    "img": "/images/catalogo/1776104501594-600x400.webp",
    "alt": "Piezas faciales de equipo de respiración en un taller de mantenimiento",
    "desc": "Esta card está aquí a propósito, porque es la trampa más cara de la línea. El 75i es un equipo <strong>vigente y aprobado por NIOSH</strong> para atmósferas IDLH, y el propio fabricante lo describe para <strong>“industrial, firefighting (non-NFPA) and similar IDLH applications”</strong>: usa un diseño similar al del Air-Pak 75 certificado NFPA, <strong>pero él no lo está</strong>. Sirve para espacio confinado e industria; no para combate estructural. Y una versión industrial cotizada en una partida de bomberos se ve idéntica en una foto.",
    "specs": [
      "Aprobado por NIOSH, no certificado NFPA",
      "2216, 4500 o 5500 psi · 30 a 75 minutos",
      "Para IDLH industrial y espacio confinado",
      "No es equipo de combate estructural"
    ],
    "chip": "Pedirlo solo para uso industrial"
  }
]
''')

# El boton de una card sin ficha L4 dice "Cotizar {fichaLabel ?? variante}". Aqui la variante
# es el tipo de linea —"Linea NFPA", "Industrial, no NFPA"— y dos cards la comparten, asi que sin
# fichaLabel el boton diria lo mismo en las dos. Se etiqueta con el modelo, que es lo que una
# persona escribe en un WhatsApp.
ETIQUETAS = {
    'G1 XR': 'el MSA G1 XR',
    'Air-Pak X3 Pro': 'el Air-Pak X3 Pro',
    'Air-Pak XD': 'el Air-Pak XD',
    'PSS 7000': 'el Dräger PSS 7000',
    'PSS AirBoss': 'el Dräger PSS AirBoss',
    'Air-Pak 75i': 'el Air-Pak 75i industrial',
}
for _c in CARDS:
    _c['fichaLabel'] = ETIQUETAS[_c['modelo']]

L3['catalogo'] = collections.OrderedDict([
    ('eyebrow', 'Catálogo por plataforma'),
    ('titulo', 'Equipos de respiración autónoma\npor plataforma y por marca'),
    ('intro',
     'Cuatro datos deciden si el equipo que te cotizan sirve para combate estructural: '
     '<strong>si tiene aprobación NIOSH, si tiene certificación NFPA, qué edición declara y qué '
     'organismo la emitió</strong>. Los cuatro se ven en dos documentos y ninguno en una foto —y '
     'hay equipos aprobados por NIOSH que el propio fabricante declara <em>no</em> NFPA—.'),
    ('imgRef', 'Imagen de referencia de la línea'),
    ('nota',
     'Estas plataformas se cotizan por <strong>número de parte de configuración</strong>, no por '
     'nombre de familia: la misma marca vende versiones estructurales e industriales que se '
     'parecen y que no son intercambiables. Ninguna ficha de fabricante publica el número TC de '
     'NIOSH: está en la etiqueta física del equipo y es lo primero que verificamos al recibir.'),
    ('cards', CARDS),
])

L3['secciones'] = json.loads(r'''
[
  {
    "id": "doble-marco",
    "eyebrow": "Las dos certificaciones",
    "titulo": "NFPA certifica el desempeño; NIOSH aprueba el aparato",
    "parrafos": [
      "En el resto del catálogo alcanza con leer bien un certificado. Aquí hay que leer dos documentos distintos, y ninguno sustituye al otro. <strong>NIOSH</strong> —el instituto federal estadounidense de seguridad y salud ocupacional— aprueba el equipo como aparato respiratorio bajo el reglamento <strong>42 CFR Parte 84</strong>, y su número de aprobación empieza con el prefijo <strong>TC</strong>. <strong>NFPA 1970</strong>, en sus capítulos 15 a 19, evalúa lo que el reglamento federal no mira: cómo se comporta el equipo dentro de un incendio.",
      "La consecuencia práctica es incómoda y conviene saberla antes de comparar precios: <strong>un equipo puede estar aprobado por NIOSH y no estar certificado por NFPA</strong>. Existen y se venden así, legítimamente, para uso industrial. Lo que no se puede es meterlos en una partida de combate estructural, porque nadie evaluó su lente frente a calor radiante ni su conexión de rescate."
    ],
    "tabla": {
      "head": ["Qué mira", "NIOSH · 42 CFR Parte 84", "NFPA 1970 · capítulos 15 a 19"],
      "rows": [
        ["Objeto", "El aparato respiratorio como conjunto armado", "El desempeño del equipo en incendio"],
        ["Qué evalúa", "Presión positiva, tiempo de servicio, aviso de fin de servicio, hermeticidad", "Lente frente a calor radiante, HUD, RIC UAC, PASS, comunicación de voz"],
        ["Cómo se identifica", "Etiqueta de aprobación con <strong>número TC</strong> y la configuración aprobada", "Certificado con <strong>edición y organismo certificador</strong>"],
        ["Qué NO cubre", "Nada del comportamiento térmico ni del PASS", "No sustituye la aprobación del aparato respiratorio"]
      ]
    },
    "nota": "Redacción que cierra la partida: <strong>“equipo de respiración autónomo de circuito abierto y presión positiva, aprobado por NIOSH bajo 42 CFR Parte 84 y certificado como conforme a NFPA 1970 edición 2025, indicando número TC, organismo certificador y número de parte de la configuración”</strong>. Son cuatro datos y caben en un renglón."
  },
  {
    "id": "conjunto-armado",
    "eyebrow": "Lo que casi nadie sabe",
    "titulo": "La aprobación es del conjunto armado, no de las piezas",
    "parrafos": [
      "Este es el punto que cambia cómo se compra un ERA, y está en el texto del reglamento, no en la interpretación de nadie. <strong>42 CFR 84.30</strong> dice que el instituto emite certificados de aprobación <em>“solo para respiradores individuales, completamente ensamblados”</em> y, en su inciso siguiente, que <strong>no emite certificados de aprobación para ningún componente ni subensamble</strong>. La etiqueta de aprobación no lista un modelo: lista <strong>la configuración de componentes aprobados, con su número de parte</strong>.",
      "De ahí se sigue lo que NIOSH publicó sobre refacciones no originales: usar componentes que no forman parte del ensamble aprobado da como resultado <strong>un respirador que no ha sido evaluado ni certificado</strong> por el instituto. Ojo con la redacción: el reglamento no dice “se anula la aprobación”. Dice algo más preciso y más útil de citar en una aclaración de licitación: <strong>ese conjunto, así armado, nadie lo evaluó</strong>.",
      "En el mercado mexicano esto aterriza en un lugar muy concreto: la pieza facial, el cilindro y el regulador se venden por separado, con claves inventadas por el distribuidor, y se mezclan entre marcas y entre generaciones del mismo fabricante. La foto se ve bien. La configuración aprobada, no."
    ],
    "lista": [
      { "t": "Qué pedir al recibir", "d": "La <strong>etiqueta de aprobación</strong> del equipo, no una copia del certificado del modelo. Ahí está el número TC y la matriz de componentes con su número de parte." },
      { "t": "Qué revisar en la matriz", "d": "Que el <strong>número de parte de la pieza facial, del cilindro y del regulador</strong> que te entregaron aparezca marcado como parte de la configuración aprobada." },
      { "t": "Cuándo se rompe", "d": "Al reponer una pieza con una equivalente “compatible”, al mezclar generaciones del mismo fabricante o al comprar cilindro de una marca para un equipo de otra." },
      { "t": "Lo que sí se puede", "d": "Reponer <strong>con el número de parte que está en la matriz</strong>. Es la única forma de mantener el conjunto dentro de lo aprobado, y por eso la refacción se cotiza por clave, nunca por descripción." }
    ],
    "nota": "Ningún fabricante publica el número TC en su ficha, su especificación de licitación o su manual: <strong>vive en la etiqueta física del equipo</strong> y en la lista de equipo certificado de NIOSH. Es la razón por la que la verificación de un ERA no se puede hacer solo con papeles del proveedor."
  },
  {
    "id": "duracion",
    "eyebrow": "El dato que se malinterpreta",
    "titulo": "Un cilindro de 30 minutos no dura 30 minutos",
    "parrafos": [
      "No es publicidad engañosa: es una unidad de medida que se lee mal. La duración nominal de un ERA <strong>se determina con máquina de respiración</strong>, y el reglamento fija el ritmo: <strong>24 respiraciones por minuto y un volumen minuto de 40 litros</strong> (42 CFR 84.88). Un elemento avanzando una línea, forzando una puerta o subiendo escalera con 20 kilos encima respira bastante más que eso, así que el tiempo de trabajo real siempre es menor —y varía tanto entre personas que <strong>no existe una cifra publicada que aplique a todos</strong>.",
      "Lo que sí es exigible y comparable son las duraciones nominales que reconoce el reglamento —entre ellas <strong>30, 45 y 60 minutos</strong>— y el momento en que el equipo avisa. Ahí el piso regulatorio es duro: el aviso de fin de servicio debe activarse <strong>cuando queda al menos el 25 % del tiempo nominal</strong> (42 CFR 84.83). Ese 25 % no es margen de cortesía: es la reserva para salir."
    ],
    "lista": [
      { "t": "Cómo se compara entre marcas", "d": "Por <strong>volumen de aire y presión de servicio</strong>, no por minutos: el mismo “45 minutos” sale de un cilindro de 4500 psig y de otro de 5500 psig con pesos distintos." },
      { "t": "Qué significa la alarma", "d": "Que el elemento <strong>ya está consumiendo la reserva de emergencia</strong>. La salida del ambiente peligroso se planea para ocurrir antes, no cuando suena." },
      { "t": "Por qué importa en la dotación", "d": "El número de cilindros de repuesto por unidad se dimensiona con el consumo real de la corporación, no con la duración nominal. Es la diferencia entre un relevo y una espera." },
      { "t": "Cómo se mide el consumo propio", "d": "Con un ejercicio de consumo documentado por elemento y por tarea. Es el único dato que sirve para presupuestar aire, y lo genera cada corporación con su gente." }
    ],
    "nota": "Cuidado con un dato que circula mal: <strong>“el aviso se activa al 33 % del tiempo nominal”</strong> es lenguaje de NFPA 1981 edición 2013. En NFPA 1970-2025 el umbral se expresa como porcentaje de la <strong>presión</strong> nominal y varía según la presión del cilindro. El único piso citable con fuente regulatoria es el <strong>25 % del tiempo nominal</strong> de NIOSH."
  },
  {
    "id": "cilindro",
    "eyebrow": "Recipiente a presión",
    "titulo": "El cilindro no lo certifica NFPA ni NIOSH: lo certifica el DOT",
    "parrafos": [
      "El cilindro juega en otra liga normativa y por eso se documenta aparte. Es un <strong>recipiente a presión bajo jurisdicción del Departamento de Transporte</strong> estadounidense, y los cilindros compuestos de ERA operan bajo la norma <strong>DOT-CFFC</strong> y bajo permisos especiales <strong>DOT-SP</strong>. La marca grabada en el hombro del cilindro lo dice todo: primero la especificación DOT, inmediatamente después la presión de servicio, y cerca del número de serie <strong>la marca del inspector con mes y año de prueba</strong>.",
      "Dos cifras que conviene tener claras porque mueven presupuesto: la norma DOT-CFFC establece que <strong>la vida de servicio del cilindro compuesto es de 15 años desde la fecha de fabricación</strong>, y el fabricante de cilindros publica que se permite un <strong>intervalo de recalificación de cinco años</strong>. Existen rutas autorizadas para extender la vida hasta 20 y 30 años mediante permisos especiales y ensayo de emisión acústica, con posturas distintas entre fabricantes."
    ],
    "tabla": {
      "head": ["Dato del cilindro", "Qué dice la fuente", "Para qué sirve al comprar"],
      "rows": [
        ["Quién lo certifica", "DOT y, para Canadá, Transport Canada. <strong>No</strong> NFPA ni NIOSH", "Se pide la designación DOT, no un certificado NFPA"],
        ["Vida de servicio", "<strong>15 años desde la fecha de fabricación</strong> en compuesto, por DOT-CFFC", "Un cilindro con dos años de inventario entra con 13 de vida"],
        ["Recalificación", "Intervalo de <strong>cinco años</strong> publicado por el fabricante de cilindros", "Se verifica la fecha de la última prueba antes de recibir"],
        ["Marcado", "Especificación DOT + presión de servicio, número de serie y fecha de prueba", "Es la verificación que sí se puede hacer con el cilindro en la mano"],
        ["Quién los fabrica", "Marcas de ERA los venden con su clave; <strong>no publican quién los fabrica</strong>", "El dato de vida y recalificación se rastrea al fabricante real"]
      ]
    },
    "nota": "Un cilindro no se compra por marca de ERA: se compra por <strong>número de parte que aparezca en la configuración aprobada del equipo</strong>. Y la fecha que importa en la recepción no es la de la factura: es la de fabricación grabada en el hombro."
  },
  {
    "id": "aire",
    "eyebrow": "Lo que casi nadie audita",
    "titulo": "El aire del compresor es parte del equipo de protección",
    "parrafos": [
      "Se puede tener el mejor ERA del mercado y llenarlo con aire que no cumple. Es el punto ciego más común de un programa de protección respiratoria, y el más fácil de auditar: <strong>NFPA 1989</strong> fija los criterios de calidad del aire respirable para servicios de emergencia, y su exigencia de análisis es <strong>trimestral como mínimo</strong>, más cuando se sospeche contaminación.",
      "El referente que casi todos citan es el <strong>aire Grado D</strong>, cuyos límites sí están en reglamento federal estadounidense: <strong>oxígeno entre 19.5 y 23.5 %</strong>, <strong>monóxido de carbono no más de 10 ppm</strong>, <strong>bióxido de carbono no más de 1000 ppm</strong>, hidrocarburo condensado no más de 5 mg/m³ y ausencia de olor perceptible; y para el aire dentro del cilindro, un <strong>punto de rocío que no exceda −50 °F</strong>. Los laboratorios acreditados que hacen el análisis publican que NFPA 1989 es más estricto que Grado D en monóxido, en aceite y en agua.",
      "Y aquí está el hueco que conviene nombrar: <strong>no localizamos ninguna norma oficial mexicana que fije límites de calidad de aire comprimido respirable</strong>. No hay equivalente nacional de NFPA 1989 ni del Grado D. Quien llena cilindros en México lo hace contra una referencia extranjera o contra ninguna."
    ],
    "lista": [
      { "t": "Qué pedir a quien llena", "d": "El <strong>análisis de laboratorio acreditado</strong> con fecha, no una carta del proveedor del compresor. Y la frecuencia por escrito en el contrato de servicio." },
      { "t": "Qué revisar del compresor", "d": "Ubicación de la toma de aire, estado y bitácora de cambio de filtros y purga de condensados. El monóxido casi siempre entra por la toma, no por el compresor." },
      { "t": "Por qué el agua importa", "d": "El agua condensada corroe por dentro y congela en la válvula al despresurizar. Es la razón del punto de rocío bajísimo que exige el reglamento." },
      { "t": "Cómo entra en una licitación", "d": "Como partida de servicio con entregable: <strong>análisis trimestral por laboratorio acreditado</strong>. Sin eso, el aire es el único componente del sistema que nadie verifica." }
    ],
    "nota": "Si la corporación llena en una estación ajena o con un proveedor externo, el análisis del aire <strong>es de quien llena, no de quien compró el equipo</strong>: hay que pedirlo igual. El cilindro no distingue de quién es la culpa."
  },
  {
    "id": "ajuste",
    "eyebrow": "La pieza que se ajusta a una cara",
    "titulo": "Sin prueba de ajuste, la talla es una suposición",
    "parrafos": [
      "Una pieza facial de ERA es un sello hermético contra una cara, y las caras no vienen en tres tallas. El reglamento estadounidense —<strong>29 CFR 1910.134</strong>— exige prueba de ajuste <strong>antes del primer uso, cada vez que se cambia de marca, modelo, estilo o talla, y al menos una vez al año</strong>. Y distingue métodos: la prueba cualitativa solo vale para respiradores purificadores de presión negativa, así que <strong>para una pieza facial completa de ERA el método aplicable es la prueba cuantitativa</strong>, que mide y arroja un número.",
      "Del lado mexicano hay que decirlo con precisión, sin exagerar en ninguna dirección: <strong>no localizamos requisito de prueba de ajuste en la NOM verificada</strong>. La NOM-017-STPS obliga al patrón a analizar el riesgo, determinar el equipo, entregarlo y capacitar en su uso —y en su edición 2024, en vigor desde septiembre de 2025, sustituyó a la de 2008—, pero la palabra ajuste no aparece en el texto de la edición anterior. Y la <strong>NOM-116-STPS no aplica</strong> a esta pieza: cubre respiradores purificadores de aire de presión negativa contra partículas, no piezas faciales de presión positiva.",
      "Que no esté exigido explícitamente no lo hace opcional en la práctica: un sello que no cierra convierte un equipo aprobado en un equipo que respira el ambiente. Es la verificación más barata de todo el sistema y la que más se omite."
    ],
    "lista": [
      { "t": "Cuándo se hace", "d": "Antes del primer uso, al cambiar de modelo o talla de pieza facial, y <strong>al menos una vez al año</strong>." },
      { "t": "Con qué método", "d": "<strong>Cuantitativo</strong> para pieza facial completa. El cualitativo —sacarina, humo irritante— no aplica a este tipo de equipo." },
      { "t": "Qué invalida el sello", "d": "Barba en la zona del sello, patillas de anteojos cruzando la línea de sellado y cicatrices o rasgos que impiden contacto continuo. Para anteojos existen kits de montaje interno." },
      { "t": "Qué queda documentado", "d": "El registro por usuario con fecha, marca, modelo y talla probada. Es el papel que convierte “se le entregó equipo” en “se le entregó el equipo que le sella”." }
    ],
    "nota": "Comprar tres tallas “para que le queden a todos” es lo contrario de un programa de ajuste. <strong>La talla se determina por usuario y se registra</strong>, y esa lista es la que define cuántas piezas faciales de cada talla se cotizan."
  },
  {
    "id": "mantenimiento",
    "eyebrow": "Ciclo de vida",
    "titulo": "Prueba de flujo anual, técnico certificado y retiro por edición",
    "parrafos": [
      "El programa de cuidado y mantenimiento vive hoy en <strong>NFPA 1850</strong>, que desde su edición 2026 consolidó la norma del ensamble y la de ERA de circuito abierto, con fecha efectiva de septiembre de 2025. En la práctica el calendario que publican fabricantes y autoridades laborales coincide: <strong>inspección después de cada uso, inspección operacional documentada al menos mensual y prueba de flujo del regulador al menos anual</strong>.",
      "Aquí aparece una condición comercial que conviene conocer antes de firmar, porque cambia el costo de propiedad: <strong>los fabricantes no permiten que cualquiera abra el equipo</strong>. Uno lo dice sin rodeos —solo personal capacitado y certificado por su programa puede mantener y reparar el equipo, y nombra incluso el banco de prueba aprobado— y otro exige centro de servicio autorizado para cualquier desarmado que no esté en el manual. Un tercero pide personal capacitado y competente, sin exigir centro de fábrica.",
      "Y el retiro del equipo no depende del cilindro: el ERA se retira por <strong>edición y año de fabricación</strong>. La norma establece retiro a los <strong>15 años del año de fabricación</strong>, y a los <strong>20 años</strong> si el equipo fue actualizado al menos dos ediciones con los kits del fabricante. Es un dato de presupuesto, no de bitácora."
    ],
    "tabla": {
      "head": ["Actividad", "Frecuencia publicada", "Quién la hace"],
      "rows": [
        ["Inspección y limpieza", "Después de cada uso", "El propio usuario"],
        ["Inspección operacional documentada", "Al menos <strong>mensual</strong> y antes de cada uso", "La corporación, con bitácora"],
        ["Prueba de flujo del regulador", "Al menos <strong>anual</strong>, y antes de poner un equipo nuevo en servicio", "Técnico certificado con banco de prueba"],
        ["Recalificación del cilindro", "Según el permiso del cilindro, típicamente <strong>cinco años</strong>", "Centro de prueba hidrostática"],
        ["Retiro del equipo", "<strong>15 años</strong> del año de fabricación, o 20 si se actualizó dos ediciones", "Programación presupuestal"]
      ]
    },
    "nota": "Detalle con ironía útil: los tres fabricantes principales dependen del <strong>banco de prueba de un cuarto fabricante</strong>, que además ya salió del negocio de los ERA. Antes de comprar una plataforma conviene preguntar quién hace la prueba de flujo anual en tu región y con qué software, porque es específico por marca."
  },
  {
    "id": "mexico",
    "eyebrow": "Marco mexicano",
    "titulo": "En México el respaldo es extranjero, y hay que escribirlo bien",
    "parrafos": [
      "Ni NIOSH ni NFPA son autoridad en México, y <strong>no localizamos ninguna norma oficial mexicana que reconozca, exija o equipare esas certificaciones para un ERA</strong>. Tampoco encontramos NOM que fije desempeño del aparato ni calidad del aire respirable. Lo que sí hay es obligación de proceso, y ahí se sostiene la compra: identificar y analizar el riesgo, determinar el equipo en función de ese riesgo, entregarlo, capacitar y supervisar su uso.",
      "Para espacios confinados el marco sí es explícito y conviene citarlo con numeral: la <strong>NOM-033-STPS</strong> define atmósfera respirable como <strong>oxígeno entre 19.5 y 23.5 % en volumen</strong>, obliga a <strong>monitoreo continuo</strong> en los espacios de mayor riesgo y exige <strong>equipo de respiración autónomo o con línea de suministro de aire</strong> cuando no se puede confirmar una atmósfera segura. También prohíbe algo que todavía se ve: <strong>ventilar con oxígeno puro</strong>.",
      "Y hay un dato de vigencia que conviene revisar en cualquier documento heredado: la <strong>NOM-017-STPS-2008 fue cancelada</strong> por la edición 2024, publicada en el Diario Oficial el 28 de marzo de 2025 y en vigor desde el 28 de septiembre de 2025. Una requisición que cite la de 2008 está citando una norma cancelada."
    ],
    "lista": [
      { "t": "Cómo se arma el documento", "d": "<strong>NFPA y NIOSH para el desempeño</strong> del equipo, NOM-017 para el proceso de selección y entrega, y NOM-033 cuando hay espacio confinado. Las tres, no una." },
      { "t": "Qué no se puede pedir", "d": "Una NOM que certifique el ERA: <strong>no existe</strong>. Pedirla deja la partida sin ofertas válidas y sin ganar nada." },
      { "t": "Lo que sí cambia una licitación", "d": "Exigir <strong>número TC, edición NFPA y organismo certificador</strong>. Es documental, es verificable y filtra a quien solo puede escribir “cumple NFPA”." },
      { "t": "El patrón del mercado local", "d": "Fichas que dicen “NFPA” sin edición, claves de producto inventadas por el distribuidor y ninguna mención a NIOSH. Se resuelve pidiendo número de parte del fabricante." }
    ],
    "nota": "Un ejemplo real de por qué la edición importa: circula en el mercado mexicano la designación <strong>“NFPA 1970 2018”</strong>, que no existe —NFPA 1970 es la norma consolidada de 2025; lo de 2018 son las ediciones de NFPA 1981 y 1982—. Quien la escribe está mezclando dos normas distintas."
  }
]
''')

L3['galeriaIntro'] = (
    'Referencias del equipo en operación. Lo que ninguna foto puede mostrar es lo único que '
    'decide si sirve para combate estructural: el número TC de la etiqueta de aprobación y la '
    'edición del certificado. Un equipo industrial y uno estructural se ven idénticos con el '
    'cilindro puesto.'
)

L3['galeria'] = json.loads(r'''
[
  {
    "src": "/images/catalogo/1756112277157-1000x750.webp",
    "alt": "Equipo de protección alineado en el rack de la estación de bomberos",
    "caption": "Inspección operacional documentada, al menos mensual"
  },
  {
    "src": "/images/catalogo/1705503828024-600x450.webp",
    "alt": "Piezas faciales de equipo de respiración colgadas en la estación",
    "caption": "La talla se determina por usuario y se registra"
  },
  {
    "src": "/images/catalogo/1584033376505-600x400.webp",
    "alt": "Rostro de bombero con casco estructural y lámpara integrada",
    "caption": "Entre maniobras, sin pieza facial puesta"
  },
  {
    "src": "/images/catalogo/1606613816768-600x450.webp",
    "alt": "Dos bomberos con equipo de respiración autónoma en la calle",
    "caption": "El aire de repuesto se dimensiona con el consumo real"
  }
]
''')

L3['aplicaciones'] = json.loads(r'''
[
  {
    "sector": "Cuerpos de bomberos",
    "desc": "Equipo certificado NFPA 1970 y aprobado por NIOSH, cotizado por número de parte de configuración, con cilindros de repuesto dimensionados por el consumo real de la corporación y no por la duración nominal."
  },
  {
    "sector": "Espacios confinados",
    "desc": "Donde la NOM-033-STPS obliga a equipo autónomo o con línea de aire porque no se puede confirmar atmósfera respirable. Aquí un equipo industrial aprobado por NIOSH sí es la herramienta correcta, y conviene decirlo: no todo tiene que ser NFPA."
  },
  {
    "sector": "Industria química",
    "desc": "Brigadas con intervención en atmósferas IDLH y programa de protección respiratoria auditado. El entregable que más se olvida no es el equipo: es el análisis trimestral del aire del compresor que llena los cilindros."
  }
]
''')

L3['datoClave'] = collections.OrderedDict([
    ('titulo', 'La aprobación NIOSH es del conjunto, no de las piezas'),
    ('texto',
     'El reglamento federal es explícito: se aprueban <strong>respiradores completamente '
     'ensamblados</strong> y <strong>no se aprueban componentes ni subensambles</strong>. Reponer '
     'una pieza facial, un cilindro o un regulador con una clave que no está en la matriz de la '
     'etiqueta deja un conjunto que <strong>nadie evaluó así</strong>. Por eso la refacción se '
     'pide por número de parte, nunca por descripción.'),
])

L3['normasRef'] = ['NFPA 1970', 'NIOSH 42 CFR 84', 'NFPA 1850', 'NFPA 1989',
                   'NOM-033-STPS', 'NOM-017-STPS', 'NOM-116-STPS']

L3['documentacion'] = [
    'Certificado de cumplimiento NFPA 1970 con edición y organismo certificador nombrado',
    'Etiqueta de aprobación NIOSH con número TC y matriz de la configuración aprobada',
    'Número de parte del fabricante para equipo, pieza facial, regulador y cilindro',
    'Designación DOT del cilindro con fecha de fabricación y de última recalificación',
    'Registro de prueba de ajuste cuantitativa por usuario, con talla y modelo',
    'Programa de servicio: quién hace la prueba de flujo anual y con qué banco de prueba',
    'Análisis de laboratorio acreditado del aire del compresor que llena los cilindros',
]

L3['blog'] = [
    'guia-scba-equipos-respiracion-autonoma',
    'scba-msa-g1-guia-tecnica',
    'scott-airpak-50-vs-msa-g1-comparativa',
    'nfpa-1981-mexico-equipos-respiracion',
    'mantenimiento-scba-programa-anual',
    'espacios-confinados-proteccion-respiratoria',
]

L3['faqs'] = json.loads(r'''
[
  {
    "q": "¿Por qué un ERA necesita dos certificaciones y no una?",
    "a": "Porque miden cosas distintas y ninguna cubre a la otra. La aprobación de NIOSH, bajo el reglamento federal estadounidense 42 CFR Parte 84, evalúa el aparato respiratorio: presión positiva, tiempo de servicio, aviso de fin de servicio. La certificación NFPA 1970, en sus capítulos 15 a 19, evalúa el desempeño en incendio: el lente frente a calor radiante, el HUD, la conexión de rescate RIC UAC, el PASS y la comunicación de voz. Existen equipos aprobados por NIOSH que el propio fabricante declara no-NFPA, vigentes y legítimos para uso industrial. Para combate estructural se necesitan las dos."
  },
  {
    "q": "¿Qué es el número TC y por qué lo piden?",
    "a": "Es el número de aprobación que NIOSH asigna, y empieza con el prefijo TC. No identifica un modelo: identifica una configuración de componentes aprobados, con su número de parte, en una matriz impresa en la etiqueta del equipo. Es el único documento que permite verificar que la pieza facial, el cilindro y el regulador que te entregaron son los que se evaluaron juntos. Y es el dato que ningún fabricante publica en su ficha ni ningún distribuidor mexicano incluye en su cotización: vive en la etiqueta física del equipo."
  },
  {
    "q": "Si repongo una pieza con una equivalente, ¿pierdo la aprobación?",
    "a": "La redacción precisa importa. El reglamento no dice que la aprobación se anule; dice que NIOSH aprueba respiradores completamente ensamblados y que no aprueba componentes ni subensambles. Y NIOSH publicó que usar componentes que no forman parte del ensamble aprobado da como resultado un respirador que no ha sido evaluado ni certificado por el instituto. En una aclaración de licitación conviene citarlo así, porque es más exacto y más difícil de rebatir: ese conjunto, armado de esa forma, nadie lo evaluó."
  },
  {
    "q": "¿Cómo comparo un equipo de 4500 psi contra uno de 5500 psi?",
    "a": "No por minutos, porque los minutos son una etiqueta: se comparan por volumen de aire y peso. Un mismo tiempo nominal se consigue con presiones distintas, y la de mayor presión da un cilindro más compacto y en general más ligero para el mismo volumen. Lo que hay que verificar es que el cilindro esté en la configuración aprobada del equipo y que la estación pueda llenar a esa presión: un cilindro de 5500 psi no se aprovecha con un compresor que llena a 4500."
  },
  {
    "q": "¿Qué debe decir un certificado para que sirva en una licitación?",
    "a": "Cuatro datos: número TC de la aprobación NIOSH, edición de NFPA 1970 declarada, organismo certificador nombrado y número de parte de la configuración cotizada. La diferencia entre proveedores se ve justo ahí: hay fabricantes que separan por escrito la aprobación de NIOSH de la certificación de un organismo tercero, otros que solo escriben que el equipo cumple, y otros que dicen estar certificados sin nombrar la edición. Los tres pueden ser equipos correctos; solo uno te deja un expediente que resiste una auditoría."
  },
  {
    "q": "¿Cada cuándo se retira un ERA, y es lo mismo que el cilindro?",
    "a": "No es lo mismo y se presupuestan por separado. El equipo se retira por edición y año de fabricación: la norma de cuidado y mantenimiento establece retiro a los 15 años del año de fabricación, y a los 20 si el equipo se actualizó al menos dos ediciones con los kits del fabricante. El cilindro sigue su propia regla, que es del Departamento de Transporte y no de NFPA: en compuesto, 15 años de vida de servicio desde la fecha de fabricación, con recalificación típicamente cada cinco años según el permiso del cilindro."
  },
  {
    "q": "¿Hay una NOM mexicana que certifique equipos de respiración autónoma?",
    "a": "No localizamos ninguna. No hay NOM que fije el desempeño de un ERA ni que reconozca o equipare las certificaciones NFPA o NIOSH, y tampoco encontramos NOM que establezca límites de calidad de aire comprimido respirable. Lo que sí aplica es obligación de proceso —la NOM-017-STPS, en su edición 2024 vigente desde septiembre de 2025, obliga a analizar el riesgo, determinar el equipo, entregarlo y capacitar— y la NOM-033-STPS para espacios confinados, que sí exige equipo autónomo o con línea de aire cuando no se puede confirmar atmósfera respirable. Y ojo: la NOM-116-STPS no aplica, porque cubre respiradores purificadores de presión negativa."
  },
  {
    "q": "¿Quién puede darle mantenimiento al equipo?",
    "a": "Depende del fabricante, y conviene resolverlo antes de comprar porque cambia el costo de propiedad. Uno solo permite personal capacitado y certificado por su propio programa, y llega a nombrar el banco de prueba aprobado con el que debe hacerse la prueba de flujo. Otro exige centro de servicio autorizado para cualquier desarmado que no esté en el manual. Un tercero pide personal capacitado y competente sin exigir centro de fábrica. La pregunta útil no es si el equipo es bueno, sino quién hace la prueba de flujo anual en tu región y con qué software, porque el banco de prueba es específico por marca."
  }
]
''')

# ── Escritura ──────────────────────────────────────────────────────────────────
with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'equipos-de-respiracion')
prod = next(p for p in cat['productos'] if p['slug'] == 'scba-scott-air-pak')
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
assert not (set(ids) & RESERVADOS), 'id reservado: %s' % (set(ids) & RESERVADOS)
for c in L3['catalogo']['cards']:
    assert len(c['specs']) == 4, 'la card %s no tiene 4 specs' % c['modelo']
imgs = [c['img'] for c in L3['catalogo']['cards']] + [g['src'] for g in L3['galeria']]
dup = [i for i in set(imgs) if imgs.count(i) > 1]
print('  imágenes repetidas en la página:', dup or 'ninguna')
codes = {n['code'] for n in cat.get('normas', [])}
print('  normasRef sin entrada en la categoría:',
      [c for c in L3['normasRef'] if c not in codes] or 'ninguna')
faqs_l2 = {f['q'] for f in cat.get('faqs', [])}
print('  FAQs repetidas literalmente de la L2:',
      [q for q in (f['q'] for f in L3['faqs']) if q in faqs_l2] or 'ninguna')
