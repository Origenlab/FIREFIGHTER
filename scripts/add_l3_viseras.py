#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sexta y ultima L3 de EPP: viseras, caretas y goggles para casco estructural.

Eje editorial: es la unica linea del catalogo que NO es un producto certificado. La visera,
la careta, los Bourkes y los goggles son COMPONENTES del casco (NFPA 1971 3.3.41, 3.3.42 y
3.3.55: "the component of the helmet that..."), y el elemento certificado es el casco. De ahi
salen las tres correcciones de la ficha:

  1. La visera montada externamente, usada sola, NO es proteccion ocular primaria
     (NFPA 1500-2018, 7.18.1.3). Lo primario es la pieza facial del SCBA, y los goggles
     calificados Z87+ tambien cuentan. Son dos renglones distintos de una partida.
  2. La norma exige visera O goggles. Si el casco trae los dos, solo uno tiene que ser parte
     del producto certificado; el otro puede quedar fuera del alcance.
  3. "Antirrayadura" no es una especificacion: ningun producto del mercado NFPA publica
     marcado EN 166 "K" ni datos de abrasion. La norma NFPA si mide el rayado (delta haze).

Fuentes primarias consultadas 2026-08-06: NFPA (TIA_1970_25_5, Proposed TIA 1790,
1971_A2017_SD_prelimSR), preview NFPA 1971-2018 y 1970-2025, NJ Dept. of Labor Alert 32
(cita textual de NFPA 1500-2018 7.18.1.3), fichas y manuales de MSA (3600-169-MC del Cairns
1836, bulletin del Defender, pagina de Bourkes NFPA), bid specs de Bullard (UST y PX ReTrak),
paginas de ESS Innerzone, Pacific F15, whitepaper de visores de MSA (EN 166 K/N), y los textos
oficiales de NOM-115-STPS-2009 y NOM-017-STPS-2008 en stps.gob.mx.

Uso: python3 scripts/add_l3_viseras.py
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

L3 = collections.OrderedDict()

L3['seoTitle'] = 'Viseras y caretas para casco de bombero NFPA'
L3['seoDescription'] = (
    'Viseras, caretas y goggles para casco estructural: son componente del casco, no '
    'protección ocular primaria. Qué exigir en el certificado y qué nadie publica.'
)

L3['h1'] = 'Viseras, caretas y goggles para casco estructural'
L3['subtitulo'] = (
    # OJO: el subtitulo se imprime como texto, no con set:html. Sin etiquetas.
    'Visor retráctil integrado, careta externa de 4 y 6 pulgadas, Bourkes y goggles: cuatro '
    'formas de cubrir la cara que la norma trata como componentes del casco, no como productos '
    'certificados por separado, y ninguna de ellas sustituye a la pieza facial del equipo de '
    'respiración.'
)

L3['heroImg'] = collections.OrderedDict([
    ('src', '/images/catalogo/1776784163560-1000x750.webp'),
    ('alt', 'Bombero con casco estructural y careta abajo trabajando sobre el cristal de un vehículo'),
    ('caption', 'La careta protege la cara; los ojos los protege otra pieza'),
])

L3['heroBloques'] = [
    collections.OrderedDict([
        ('label', 'Por qué esta pieza se compra mal'),
        ('texto',
         'Es la única línea del catálogo que <strong>no es un producto certificado</strong>: la '
         'visera, la careta, los Bourkes y los goggles son <strong>componentes del casco</strong>, '
         'y el certificado se emite para el casco completo. De ahí los dos errores que se repiten '
         'en una partida: creer que la visera protege los ojos —NFPA 1500 dice que usada sola '
         '<strong>no es protección ocular primaria</strong>— y suponer que si el casco trae visera '
         'y goggles, los dos están certificados.'),
    ]),
    collections.OrderedDict([
        ('label', 'Distribución autorizada, no reventa'),
        ('texto',
         'Cotizamos el componente óptico <strong>por serie y número de parte del casco</strong>, con '
         'el certificado donde consta qué componente quedó dentro del alcance, y decimos con '
         'claridad <strong>qué dato no publica el fabricante</strong> en lugar de rellenarlo. '
         'Propuesta técnica en menos de <strong>24 horas hábiles</strong> y cobertura en los '
         '<strong>32 estados de la República</strong>.'),
    ]),
]

L3['heroDatos'] = [
    collections.OrderedDict([('label', 'Protección primaria'), ('valor', 'Pieza facial del SCBA')]),
    collections.OrderedDict([('label', 'Transmitancia mínima'), ('valor', '85 % claro · 43 % teñido')]),
]

L3['specStrip'] = [
    collections.OrderedDict([('label', 'Configuraciones'), ('valor', 'Visor, careta, Bourkes o goggles')]),
    collections.OrderedDict([('label', 'Cómo certifica'), ('valor', 'Componente del casco')]),
    collections.OrderedDict([('label', 'Lente claro'), ('valor', 'Transmitancia mínima de 85 %')]),
    collections.OrderedDict([('label', 'Lente teñido'), ('valor', 'Transmitancia mínima de 43 %')]),
    collections.OrderedDict([('label', 'Visera de proximidad'), ('valor', 'Mínimo 30 % de transmitancia')]),
    collections.OrderedDict([('label', 'Sin herramienta'), ('valor', 'Solo en visores retráctiles')]),
]

CARDS = json.loads(r'''
[
  {
    "marca": "Bullard",
    "modelo": "ReTrak",
    "variante": "Visor retráctil",
    "varianteLabel": "Configuración",
    "badge": "NFPA 1971 · Z87.1+",
    "estado": "Sin edición declarada",
    "img": "/images/catalogo/1642752468603-600x400.webp",
    "alt": "Casco con visor transparente y pantalla facial, vista de producto",
    "desc": "Visor integrado que se desliza hacia arriba y se guarda dentro del casco. Bullard publica <strong>poliarilato de alta temperatura</strong> con recubrimiento resistente a rayaduras <strong>en la cara interna y externa</strong>, operación con una sola mano y cambio de lente sin herramienta. Disponible en las series UST, UST-LW, FX y PX. Su declaración textual es “meet NFPA 1971 / ANSI/ISEA Z87.1+ requirements”: <strong>no nombra edición</strong>.",
    "specs": [
      "Poliarilato de alta temperatura",
      "Recubrimiento en ambas caras del lente",
      "Cambio de lente sin herramienta",
      "Series UST, UST-LW, FX y PX"
    ],
    "chip": "Se cotiza por serie de casco"
  },
  {
    "marca": "Bullard",
    "modelo": "Caretas de 4\" y 6\"",
    "variante": "Careta externa",
    "varianteLabel": "Configuración",
    "badge": "Z87.1 óptico + NFPA 1971",
    "estado": "Herraje aparte",
    "img": "/images/catalogo/1729843997809-600x450.webp",
    "alt": "Casco de bombero de perfil con careta de protección facial montada al ala",
    "desc": "La careta que va montada al ala. Bullard la describe como material <strong>PPC endurecido de 4\" × 15\" moldeado en posición</strong> y la monta con perilla de nylon reforzado con fibra de vidrio sobre stud de acero inoxidable: <strong>se ajusta con perillas, no es la pieza “sin herramienta”</strong>. La declaración es doble y vale leerla completa: <strong>certificada a los requisitos ópticos de ANSI/ISEA Z87.1 además de los de NFPA 1971 para calor e impacto</strong>.",
    "specs": [
      "PPC endurecido de 4\" × 15\"",
      "Montaje con perilla y stud de acero inoxidable",
      "Z87.1 óptico más NFPA 1971 calor e impacto",
      "R325, R330, R333 y R334 según medida"
    ],
    "chip": "El herraje se cotiza por separado"
  },
  {
    "marca": "Bullard",
    "modelo": "R340",
    "variante": "Careta chapada en oro",
    "varianteLabel": "Configuración",
    "badge": "Proximidad y ARFF",
    "estado": "Reflectividad no publicada",
    "img": "/images/catalogo/1584033376505-600x400.webp",
    "alt": "Rostro de bombero con casco estructural y lámpara integrada bajo luz cálida",
    "desc": "Careta de <strong>6 pulgadas chapada en oro</strong> para la configuración de proximidad y rescate en aeronaves de la serie FX, que se acompaña de <strong>cubierta aluminizada de tres capas</strong>. Bullard escribe “enhanced radiant heat protection” <strong>sin publicar una sola cifra</strong>. Lo que sí exige la norma para esta pieza es medible: transmitancia mínima de <strong>30 %</strong> y adhesión del recubrimiento no peor que la clasificación 2B.",
    "specs": [
      "Número de parte R340, medida de 6\"",
      "Va con cubierta aluminizada de tres capas",
      "Transmitancia mínima de 30 % por norma",
      "Sustrato, espesor del oro y reflectividad: no publicados"
    ],
    "chip": "Pedir plazo: se surte de fábrica"
  },
  {
    "marca": "MSA",
    "modelo": "Defender",
    "variante": "Visor retráctil articulado",
    "varianteLabel": "Configuración",
    "badge": "NFPA · Z87.1 impacto",
    "estado": "Polímero sin nombrar",
    "img": "/images/catalogo/1777059017572-600x400.webp",
    "alt": "Bombera de perfil con casco estructural y equipo de respiración autónoma",
    "desc": "El visor que MSA sí documenta con verbos operativos: <strong>se sube y se baja con la mano enguantada</strong> y el lente <strong>se cambia en menos de 15 segundos y sin herramienta</strong> —es el único tiempo de servicio publicado en toda la línea—. Lente claro o Tuffshield ámbar, recubrimiento resistente a rayaduras en ambas caras, y en el Cairns 1836 <strong>articula hasta 14° hacia adelante y atrás</strong>. MSA nunca nombra el polímero: escribe “high-performance, impact-resistant plastic”.",
    "specs": [
      "Se opera con la mano enguantada",
      "Cambio de lente en menos de 15 segundos",
      "Lente claro 10077117 o ámbar 10077118",
      "Material declarado sin nombrar el polímero"
    ],
    "chip": "Compatible por serie, confirmar modelo"
  },
  {
    "marca": "MSA",
    "modelo": "Bourkes NFPA",
    "variante": "Kit 10186311",
    "varianteLabel": "Configuración",
    "badge": "NFPA-1971:2018 · Z87+",
    "estado": "El tradicional no protege",
    "img": "/images/catalogo/1628026552212-600x450.webp",
    "alt": "Bombero sosteniendo el casco estructural en una escena con humo",
    "desc": "Aquí hay dos piezas con el mismo nombre y solo una protege. De los Bourkes tradicionales MSA publica algo que conviene leer dos veces: <strong>“are for cosmetic purposes only and do not provide eye or face protection”</strong>. El kit NFPA es otro producto: declara <strong>NFPA-1971:2018</strong> y <strong>ANSI/ISEA Z87.1:2015 como protector de impacto (Z87+)</strong>, da cerca de <strong>20 % más área</strong> que el Bourkes original y <strong>lleva el marcado de certificación en el lente derecho</strong>.",
    "specs": [
      "Kit 10186311 y presentación a granel 10189839",
      "Declara NFPA-1971:2018 y Z87.1:2015 Z87+",
      "Cerca de 20 % más área que el original",
      "El marcado va en el lente derecho"
    ],
    "chip": "Verificar el marcado al recibir"
  },
  {
    "marca": "ESS",
    "modelo": "Innerzone 2 y 3",
    "variante": "Goggles",
    "varianteLabel": "Configuración",
    "badge": "NFPA 1970-2025 · Z87.1-2020",
    "estado": "Edición vigente declarada",
    "img": "/images/catalogo/1705503828024-600x450.webp",
    "alt": "Piezas faciales y protección ocular colgadas en el rack de la estación",
    "desc": "La única pieza de la línea que puede ser <strong>protección ocular primaria</strong> cuando está calificada Z87+, y la que publica el recubrimiento con más detalle: <strong>2.6 mm de policarbonato</strong> con tratamiento ClearZone FlowCoat, <strong>antirrayaduras por fuera y antivaho por dentro</strong>. ESS declara “compliant with the NFPA 1970-2025 structural fire equipment performance requirements” y “exceed the requirements of ANSI Z87.1-2020”. MSA advierte que <strong>no se usan sobre lentes graduados</strong>.",
    "specs": [
      "Policarbonato de 2.6 mm",
      "Antirrayaduras por fuera, antivaho por dentro",
      "Declara NFPA 1970-2025 y Z87.1-2020",
      "No se usan encima de lentes graduados"
    ],
    "chip": "Se surte por clave de casco: IZ2, IZ3 o S549P"
  }
]
''')

L3['catalogo'] = collections.OrderedDict([
    ('eyebrow', 'Catálogo por configuración'),
    ('titulo', 'Viseras, caretas y goggles\npor tipo y por marca'),
    ('intro',
     'Cuatro datos deciden si la pieza que te cotizan protege o solo se ve bien: '
     '<strong>si quedó dentro del alcance del certificado del casco, qué edición declara el '
     'fabricante, qué recubrimiento publica y si el lente se cambia sin herramienta</strong>. '
     'Ninguno se ve en la foto, y el primero es el que más se omite en una orden.'),
    ('imgRef', 'Imagen de referencia de la línea'),
    ('nota',
     'Estas piezas <strong>se cotizan contra la serie y el número de parte del casco</strong>, no '
     'por descripción genérica: la misma careta de 6" aparece atribuida a series distintas según '
     'el distribuidor, y el herraje de montaje se vende aparte.'),
    ('cards', CARDS),
])

L3['secciones'] = json.loads(r'''
[
  {
    "id": "primaria",
    "eyebrow": "El error de partida",
    "titulo": "La visera, usada sola, no es protección ocular",
    "parrafos": [
      "Es la confusión más costosa de esta línea y no es una opinión de proveedor: <strong>NFPA 1500 establece que la protección ocular provista únicamente por la visera montada externamente al casco no se considera protección ocular primaria</strong>. El anexo de la misma norma señala como protección primaria los anteojos o goggles calificados <strong>Z87+</strong> cuando hay riesgo de proyección de fragmentos, y reconoce que <strong>la pieza facial completa del equipo de respiración constituye protección facial y ocular</strong> mientras se usa.",
      "La consecuencia operativa es la que importa: el rostro queda descubierto justo en las maniobras donde no se trae la pieza facial puesta —ventilación, corte, remoción de escombro, trabajo con herramienta— y ahí una careta abatida cubre la cara, pero <strong>no cierra el contorno del ojo</strong>. Por eso la dotación necesita dos piezas y la partida necesita dos renglones."
    ],
    "lista": [
      { "t": "Protección primaria mientras se usa", "d": "La <strong>pieza facial del equipo de respiración</strong>. Es la única que cierra contra el rostro y por eso la norma la reconoce como protección facial y ocular." },
      { "t": "Protección primaria sin SCBA", "d": "Goggles calificados <strong>Z87+</strong>, es decir, marcados como protectores de alto impacto. Es la pieza que cubre el hueco entre maniobras." },
      { "t": "Protección secundaria", "d": "La <strong>visera o careta del casco</strong>. Protege la cara de calor y proyecciones, y la norma la exige como parte instalada del conjunto, pero no sustituye a las dos anteriores." },
      { "t": "Cómo se escribe en la partida", "d": "Dos renglones: <strong>protección facial</strong> (visera o careta, con la serie del casco) y <strong>protección ocular</strong> (goggles Z87+). Un solo renglón deja fuera una de las dos." }
    ],
    "nota": "El propio fabricante lo pone por escrito en sus guías de usuario: “su careta no está diseñada para servir como protección ocular primaria”. Si una especificación pide “visera con protección ocular”, está pidiendo dos cosas con un solo nombre."
  },
  {
    "id": "componente",
    "eyebrow": "Cómo certifica la norma",
    "titulo": "Es componente del casco, no un producto certificado",
    "parrafos": [
      "La norma define estas piezas con la misma fórmula: <strong>“the component of the helmet that…”</strong>. La careta, los goggles y la combinación de ambos son <strong>componentes</strong>; el <strong>elemento</strong> certificado es el casco. Nadie emite un certificado para una careta suelta, y por eso ningún fabricante publica número de expediente ni organismo certificador para el componente óptico por separado: <strong>la certificación se declara siempre a nivel de casco</strong>.",
      "Ahí aparece el hallazgo que cambia una compra. La norma exige que el casco estructural se suministre con <strong>careta o goggles</strong> —uno u otro, no los dos—. Cuando el casco trae los dos, <strong>solo uno de ellos tiene que formar parte del producto certificado</strong>: el otro puede quedar fuera del alcance. Y las piezas que se agregan después tienen su propia advertencia normativa: <strong>un accesorio no es parte del producto certificado</strong> aunque se monte encima de él."
    ],
    "tabla": {
      "head": ["Cómo lo llama la norma", "Qué es en la práctica", "Qué pedir en el expediente"],
      "rows": [
        ["Elemento", "El casco completo. Es lo que se certifica y lo que lleva etiqueta", "Certificado del modelo con organismo y edición"],
        ["Componente", "La careta, el visor, los Bourkes o los goggles montados de fábrica", "Que el certificado del casco indique <strong>qué componente óptico quedó dentro del alcance</strong>"],
        ["Accesorio", "Lo que se agrega después y no fue evaluado con el casco", "Declaración por escrito de que no altera la certificación, o no comprarlo"]
      ]
    },
    "nota": "Redacción que cierra la ambigüedad: <strong>“casco estructural certificado, indicando en el certificado cuál de los componentes de protección facial u ocular está incluido en el alcance”</strong>. Sin esa frase, una cotización puede entregar goggles no certificados montados en un casco certificado y no estar mintiendo."
  },
  {
    "id": "cuatro",
    "eyebrow": "Visor, careta, Bourkes o goggles",
    "titulo": "Cuatro maneras de cubrir la cara, y no son intercambiables",
    "parrafos": [
      "Las cuatro conviven en el mismo catálogo y se piden como si fueran la misma cosa. Lo que cambia entre ellas no es cuánto protegen en abstracto, sino <strong>qué cubren, cómo se guardan y qué tan rápido se ponen en servicio</strong> —y en el caso de los Bourkes, si protegen del todo—."
    ],
    "tabla": {
      "head": ["Configuración", "Cómo se lleva", "Qué considerar"],
      "rows": [
        ["Visor retráctil integrado", "Se guarda dentro del casco y baja con una mano", "El más rápido de poner en servicio y el que no se golpea al guardarse. Es la única configuración que los fabricantes publican como <strong>de cambio sin herramienta</strong>"],
        ["Careta externa de 4\" o 6\"", "Montada al ala con perillas, abatible", "Más área cubierta y más exposición mecánica. Se ajusta con perillas y el <strong>herraje se cotiza aparte</strong>"],
        ["Bourkes", "Dos lentes independientes que se abaten sobre los ojos", "Solo la versión NFPA protege: la tradicional está publicada como <strong>pieza cosmética</strong>. El marcado va en el lente derecho"],
        ["Goggles", "Con banda al casco o al cuerpo; se pueden llevar sueltos", "La única que puede ser <strong>protección ocular primaria</strong> si está calificada Z87+. No se usan sobre lentes graduados"]
      ]
    },
    "nota": "Un detalle de servicio que casi nunca entra en la comparación: en un casco tipo jet del mercado, el cambio del componente óptico <strong>requiere herramienta Torx</strong>. “Sin herramienta” aplica a los visores retráctiles y a los sistemas de blade de acople rápido, no a toda la línea."
  },
  {
    "id": "declaraciones",
    "eyebrow": "El dato que falta",
    "titulo": "En la ficha del componente no aparece la edición",
    "parrafos": [
      "En guantes el problema era el peso de las palabras; aquí es más simple y más incómodo: <strong>la edición normativa no está en la ficha del componente</strong>. Las páginas de producto de visores, caretas, Bourkes y goggles muestran el campo “NFPA” sin año, o escriben “meet NFPA 1971 requirements”. El año aparece en otra parte: en la ficha técnica del casco completo, en el manual de usuario, o en la página del distribuidor —que es justo donde menos control hay—.",
      "Hay un caso que demuestra que el dato sí puede publicarse: la ficha técnica de un casco tradicional de composite cita <strong>NFPA 1970-2025</strong> y describe ahí mismo el visor, la careta y los Bourkes. Y en el mismo modelo, dos revisiones consecutivas del manual de usuario citan primero NFPA 1971 y después NFPA 1970: <strong>la migración se puede rastrear entre revisiones de documento</strong>, no en la página del componente."
    ],
    "tabla": {
      "head": ["Dónde se busca la edición", "Qué se encuentra"],
      "rows": [
        ["Página del componente óptico", "Campo “NFPA” sin año, o “meet … requirements”. <strong>Ninguna edición</strong>"],
        ["Ficha técnica del casco completo", "Es donde aparece: hay fichas que ya citan <strong>NFPA 1970-2025</strong>"],
        ["Manual de usuario", "Aparece, y cambia entre revisiones del mismo documento"],
        ["Página de distribuidor", "A veces la trae —1971-2018, 1971 Ed. 2013— y a veces se contradice con el título de su propia categoría"]
      ]
    },
    "nota": "Regla de compra que se sostiene sola: <strong>la edición se exige en el certificado del casco, no en la ficha del componente</strong>. Y las cifras técnicas escritas por un revendedor no se reutilizan en una especificación: hay números de absorción de energía circulando en el mercado mexicano que no son rastreables a la literatura del fabricante."
  },
  {
    "id": "antirrayadura",
    "eyebrow": "Recubrimientos",
    "titulo": "“Antirrayadura” no es una especificación",
    "parrafos": [
      "Es la palabra más repetida de la línea y <strong>ningún fabricante la publica como dato verificable</strong>. Lo que sí publican son adjetivos: “hard-coated”, “scratch resistant coating on the inner and outer surfaces”, “recubrimiento resistente a rayaduras en ambas caras”. No hay ciclos de abrasión, no hay valor de dispersión de luz, no hay espesor de recubrimiento y no hay vida útil declarada.",
      "El único método cuantificado que existe en el mercado es europeo y lo cita un fabricante en su propio documento técnico: solo los visores marcados <strong>EN 166 “K”</strong> acreditan resistencia a la abrasión y solo los marcados <strong>“N”</strong> acreditan antiempañante —con criterio medible: permanecer sin empañarse un mínimo de 8 segundos en el ensayo—. <strong>Ningún producto del mercado NFPA revisado publica esas letras</strong>: NFPA y Z87.1 no tienen una clase de abrasión equivalente.",
      "Lo que sí mide la norma NFPA es el rayado del lente, con un ensayo propio de <strong>resistencia al rayado del componente careta/goggle</strong> cuyo resultado se expresa como <strong>delta haze</strong>, es decir, cuánta turbidez gana el lente después del ensayo. Ese es el dato que un lente certificado ya pasó; “antirrayadura” en un folleto no lo acredita."
    ],
    "lista": [
      { "t": "Lo que sí es exigible", "d": "Transmitancia luminosa: mínimo <strong>85 % en lente claro</strong> y <strong>43 % en lente coloreado</strong>. Es un número, viene de la norma y se puede escribir en una partida." },
      { "t": "Lo que solo declaran los goggles", "d": "El <strong>antiempañante</strong>. Las caretas externas y los visores retráctiles no lo declaran: atribuírselo en una especificación es pedir algo que el fabricante no ofrece." },
      { "t": "Lo que advierte el propio fabricante", "d": "Que <strong>cualquier recubrimiento desaparece con los lavados</strong> en semanas o meses de uso. Un lente “antirrayadura” de dos años no se comporta como uno nuevo." },
      { "t": "Cómo se compra entonces", "d": "Por <strong>número de parte del lente de repuesto</strong> y por transmitancia, no por adjetivo. El repuesto es el que mantiene la visibilidad, no el recubrimiento original." }
    ],
    "nota": "Redacción sugerida: <strong>“lente con transmitancia luminosa no menor a 85 % en versión clara, con número de parte de repuesto publicado”</strong>. Es verificable con documento; “antirrayadura” no."
  },
  {
    "id": "oro",
    "eyebrow": "Proximidad y ARFF",
    "titulo": "La careta dorada: lo que la norma pide y lo que nadie publica",
    "parrafos": [
      "La proximidad dejó de tener norma propia hace tiempo: el estándar de ensamble de proximidad se fusionó en el de estructural, y desde 2025 ambos viven dentro de <strong>NFPA 1970</strong>, que tiene capítulos de diseño y desempeño <strong>específicos para cascos de proximidad</strong>, distintos de los de estructural. Ahí es donde se buscan los requisitos de la careta dorada, no en la ficha comercial.",
      "Y ahí está la asimetría que conviene conocer antes de escribir una especificación: <strong>la norma no publica un porcentaje de calor radiante reflejado</strong>. Lo que sí exige es transmitancia visible <strong>no menor a 30 %</strong> en el lente de la visera de proximidad —para que el usuario siga viendo— y <strong>adhesión del recubrimiento reflectivo</strong> evaluada por método de cinta, sin exceder la clasificación 2B. El fabricante, por su parte, escribe “mayor protección contra calor radiante” y no da una cifra."
    ],
    "tabla": {
      "head": ["Dato", "Qué se publica"],
      "rows": [
        ["Transmitancia del lente de proximidad", "<strong>No menor a 30 %</strong> de la radiación visible incidente"],
        ["Adhesión del recubrimiento reflectivo", "Método de cinta, <strong>sin exceder clasificación 2B</strong> (remoción de 15 a 35 %)"],
        ["Composición del recubrimiento", "Un fabricante especializado publica <strong>oro al 99.99 %</strong> con recubrimiento duro exterior"],
        ["Reflectividad radiante", "<strong>No publicada</strong> por ningún fabricante ni exigida como cifra por la norma"],
        ["Sustrato y espesor del oro", "<strong>No publicados</strong>"]
      ]
    },
    "nota": "Si una especificación pide “careta que refleje un X % del calor radiante”, <strong>nadie puede acreditarlo con documento</strong> y la partida se decide por quien afirme más, no por quien pruebe más. Se pide por configuración —careta chapada en oro con cubierta aluminizada, certificada como parte del casco de proximidad— y se verifica la transmitancia."
  },
  {
    "id": "mexico",
    "eyebrow": "Marco mexicano",
    "titulo": "En México “visera” significa otra cosa",
    "parrafos": [
      "La norma mexicana de cascos de protección define <strong>visera</strong> como <em>“parte del casco que se extiende desde la concha y se proyecta hacia el frente”</em>: es <strong>el ala</strong>, no una pantalla transparente. Es una diferencia terminológica con consecuencias reales, porque una especificación que pide “visera conforme a la NOM” está pidiendo el ala del casco y no la protección facial.",
      "Y hay algo más de fondo: esa norma <strong>no contiene ningún requisito de protección ocular ni facial</strong>. Clasifica cascos en clases G, E y C, y sus métodos de prueba son <strong>impacto, penetración, tensión eléctrica y combustión</strong>. Los accesorios que reconoce son barboquejo y forro de invierno. Ninguna norma oficial mexicana establece requisitos de desempeño térmico para la careta o los goggles de un casco estructural de bombero.",
      "Lo que sí aplica en México es la obligación de proceso: identificar y analizar el riesgo, determinar el equipo en función de ese riesgo, entregarlo, capacitar y supervisar su uso. En su guía de referencia, la lista de protección de ojos y cara incluye anteojos, goggles y <strong>pantalla facial</strong> —y la entrada de brigadistas contra incendio es genérica, con la nota de equipo adicional según las actividades de rescate—."
    ],
    "lista": [
      { "t": "Lo que la NOM de cascos sí cubre", "d": "Clases G, E y C, con pruebas de impacto, penetración, tensión eléctrica y combustión. Nada óptico." },
      { "t": "Lo que la NOM de cascos llama visera", "d": "<strong>El ala del casco.</strong> Si el documento de compra usa esa palabra sin aclarar, pide otra pieza." },
      { "t": "Lo que aporta la NOM de EPP", "d": "El sustento del proceso: <strong>análisis de riesgos, determinación del equipo, entrega y capacitación</strong>. Es la vía formal para justificar por qué se compra NFPA." },
      { "t": "Cómo se resuelve en una licitación", "d": "Se cita <strong>NFPA para el desempeño</strong> —certificado del casco, con el componente óptico dentro del alcance— y la NOM de EPP para el proceso. Las dos, no una." }
    ],
    "nota": "Este es también el motivo por el que conviene escribir <strong>“careta”, “pantalla facial” o “goggles”</strong> en un documento mexicano de compra, y reservar “visera” para cuando de verdad se hable del ala. La ambigüedad se paga en la entrega."
  },
  {
    "id": "cuidado",
    "eyebrow": "Ciclo de vida",
    "titulo": "El componente óptico no se retira por antigüedad: se retira por falla",
    "parrafos": [
      "El programa de cuidado y mantenimiento —hoy en el estándar consolidado, vigente desde septiembre de 2025— trata la protección facial y ocular como parte del casco: <strong>inspección de rutina a cargo del usuario, inspección avanzada anual</strong> por el fabricante o un proveedor de servicio verificado, y almacenamiento que evite daño térmico, daño mecánico y contaminación.",
      "El retiro obligatorio a los <strong>diez años desde la fecha de fabricación</strong> aplica al casco. <strong>No existe un criterio de retiro calendárico propio para el lente</strong>: el componente óptico se reemplaza cuando falla la inspección, y eso pasa mucho antes de los diez años. Por eso el número de parte del lente de repuesto es un dato de compra, no un detalle."
    ],
    "lista": [
      { "t": "Qué se busca en la inspección", "d": "Componentes faltantes o dañados, <strong>crazing</strong>, rayado que limite la visibilidad, decoloración, deformación por calor y funcionamiento del mecanismo." },
      { "t": "Cómo se limpia", "d": "Paño o esponja suaves y agua limpia. <strong>Nada de solventes abrasivos ni limpiadores con alcohol</strong>: son los que dejan el lente turbio de forma permanente." },
      { "t": "Cómo se guarda", "d": "Accesible y protegido de calor, golpe y contaminación. Un lente guardado suelto en el casco se raya con el propio casco." },
      { "t": "Qué se pide junto con la pieza", "d": "<strong>Número de parte del lente de repuesto</strong> y las instrucciones de limpieza del fabricante. Dos lentes por casco es lo que evita operar con visibilidad comprometida." }
    ],
    "nota": "El criterio práctico es de visibilidad, no de estética: si el lente limita la visión, se reemplaza. Una guía de fabricante lo dice sin rodeos —si la visión se ve afectada por la careta, debe reemplazarse de inmediato—."
  }
]
''')

L3['galeria'] = json.loads(r'''
[
  {
    "src": "/images/catalogo/1606613816768-1000x750.webp",
    "alt": "Dos bomberos con casco estructural y equipo de respiración autónoma en la calle",
    "caption": "La pieza facial del equipo de respiración es la protección primaria"
  },
  {
    "src": "/images/catalogo/1606613640173-600x450.webp",
    "alt": "Bombero de espaldas con cilindro de equipo de respiración y casco estructural",
    "caption": "Entre maniobras, el rostro queda descubierto"
  },
  {
    "src": "/images/catalogo/1776104501594-600x400.webp",
    "alt": "Piezas faciales montadas en cabezas de maniquí en un taller de mantenimiento",
    "caption": "Inspección avanzada: anual y documentada"
  },
  {
    "src": "/images/catalogo/1705503729371-600x400.webp",
    "alt": "Chaquetones y equipo de protección colgados en el rack de la estación",
    "caption": "Almacenamiento sin daño térmico ni mecánico"
  }
]
''')

L3['aplicaciones'] = json.loads(r'''
[
  {
    "sector": "Cuerpos de bomberos",
    "desc": "Dos renglones por elemento: protección facial montada al casco y protección ocular con goggles calificados Z87+. El lente de repuesto entra en la misma orden, con número de parte."
  },
  {
    "sector": "Brigadas industriales",
    "desc": "Donde el análisis de riesgos contemple exposición térmica y proyección de fragmentos. La pantalla facial de la guía de la NOM de EPP y la careta certificada del casco no son la misma pieza ni cubren el mismo riesgo."
  },
  {
    "sector": "Licitación pública",
    "desc": "Es la línea donde una partida mal redactada se decide por afirmación y no por documento. Se pide certificado del casco indicando el componente óptico incluido, transmitancia del lente y número de parte de repuesto."
  }
]
''')

L3['datoClave'] = collections.OrderedDict([
    ('titulo', 'Si el casco trae careta y goggles, pregunta cuál está certificado'),
    ('texto',
     'La norma exige que el casco se suministre con <strong>careta o goggles</strong>. Cuando trae '
     'los dos, <strong>solo uno tiene que formar parte del producto certificado</strong>: el otro '
     'puede quedar fuera del alcance. Es la pregunta que ninguna ficha responde sola, y la que '
     'conviene dejar por escrito en la partida.'),
])

L3['normasRef'] = ['NFPA 1970', 'NFPA 1971', 'ANSI/ISEA Z87.1', 'NFPA 1500', 'NFPA 1851',
                   'NOM-115-STPS', 'NOM-017-STPS']

L3['documentacion'] = [
    'Certificado del casco indicando qué componente óptico está dentro del alcance',
    'Ficha técnica del componente con material, medida y recubrimiento declarados',
    'Número de parte del lente de repuesto y del herraje de montaje',
    'Marcado del lente cuando la configuración lo lleva, como en los Bourkes NFPA',
    'Instrucciones de limpieza y reemplazo del fabricante',
    'Factura desglosada por serie de casco, configuración y número de parte',
]

L3['blog'] = [
    'casco-bombero-bullard-usrhb-guia',
    'guia-scba-equipos-respiracion-autonoma',
    'nfpa-1971-mexico-norma-bomberos',
    'mantenimiento-epp-estructural-nfpa-1851',
    'epp-completo-kit-bombero-profesional',
    'licitaciones-equipos-contra-incendios-mexico',
]

L3['faqs'] = json.loads(r'''
[
  {
    "q": "¿La visera del casco sirve como protección ocular?",
    "a": "No como protección primaria. NFPA 1500 establece que la protección ocular provista únicamente por la visera montada externamente al casco no se considera protección ocular primaria, y las propias guías de usuario de los fabricantes lo escriben igual: “su careta no está diseñada para servir como protección ocular primaria”. Lo primario es la pieza facial del equipo de respiración mientras se usa, y goggles calificados Z87+ cuando no se trae puesta. La careta protege la cara de calor y proyecciones, y la norma la exige como parte instalada del conjunto, pero no cierra el contorno del ojo."
  },
  {
    "q": "¿Necesito careta y goggles, o basta con uno?",
    "a": "La norma exige que el casco se suministre con careta o goggles: uno u otro. La dotación real necesita los dos, porque cubren momentos distintos —la careta durante la maniobra con la pieza facial fuera, los goggles cuando hay riesgo de fragmentos—. Y hay un detalle de compra que conviene saber: cuando el casco trae los dos, solo uno de ellos tiene que formar parte del producto certificado. Si no se pide por escrito cuál, la entrega puede traer un componente fuera del alcance de la certificación sin faltar a la verdad."
  },
  {
    "q": "¿Cómo verifico que la careta que me cotizan está certificada?",
    "a": "No busques el certificado de la careta: no existe. Estas piezas son componentes del casco y la certificación se emite para el casco completo. Lo que se pide es el certificado del casco con el número de expediente, el organismo certificador, la edición y una indicación de qué componente de protección facial u ocular quedó dentro del alcance. En configuraciones como los Bourkes NFPA hay además un marcado físico en el lente derecho que se puede verificar al recibir."
  },
  {
    "q": "¿Qué significa Z87+ y por qué no es lo mismo que certificación NFPA?",
    "a": "Z87 es la marca de cumplimiento básico de impacto de la norma estadounidense de protección ocular y facial; el signo “+” indica protección de alto impacto. Es relevante porque NFPA 1500 reconoce como protección primaria los goggles calificados Z87+. Pero esa norma no aborda calor ni calor radiante: se centra en impacto, radiación no ionizante y salpicadura. Por eso los fabricantes serios declaran las dos cosas por separado, y la redacción más honesta que se encuentra en el mercado dice que la certificación óptica es “además del cumplimiento con los requisitos de NFPA 1971 para calor e impacto”."
  },
  {
    "q": "¿“Antirrayadura” es una especificación que pueda exigir?",
    "a": "No. Ningún fabricante del mercado NFPA publica un dato verificable de abrasión: publican adjetivos —“hard-coated”, “recubrimiento resistente a rayaduras en ambas caras”— sin ciclos, sin valor de dispersión de luz y sin espesor. El único método cuantificado es europeo: solo los visores marcados EN 166 “K” acreditan resistencia a la abrasión y los marcados “N” acreditan antiempañante, y ningún producto NFPA revisado publica esas letras. Lo que sí es exigible es la transmitancia luminosa: mínimo 85 % en lente claro y 43 % en lente coloreado."
  },
  {
    "q": "¿Para qué sirve la careta dorada y cuánto calor refleja?",
    "a": "Es la configuración de proximidad y rescate en aeronaves: recubrimiento metálico reflectivo sobre el lente, acompañado de cubierta aluminizada. Cuánto refleja es exactamente el dato que nadie publica: el fabricante escribe “mayor protección contra calor radiante” sin cifra, y la norma no fija un porcentaje de reflexión. Lo que la norma sí exige para esa pieza es transmitancia visible no menor a 30 % y adhesión del recubrimiento reflectivo evaluada por método de cinta, sin exceder la clasificación 2B. Si una especificación pide un porcentaje de calor reflejado, nadie puede acreditarlo con documento."
  },
  {
    "q": "¿Cada cuándo se reemplaza una visera o una careta?",
    "a": "Cuando falla la inspección, no por calendario. El retiro obligatorio a los diez años desde la fecha de fabricación aplica al casco; no hay criterio de retiro propio del componente óptico. Se reemplaza por componentes faltantes, crazing, rayado que limite la visibilidad, decoloración o deformación por calor, y eso ocurre bastante antes de los diez años. Dos criterios prácticos: si la visión se ve afectada, se reemplaza de inmediato; y el número de parte del lente de repuesto es un dato de compra, no un detalle."
  },
  {
    "q": "¿Hay una norma mexicana que cubra viseras y caretas de bombero?",
    "a": "No con requisitos de desempeño. La NOM de cascos de protección clasifica en clases G, E y C y prueba impacto, penetración, tensión eléctrica y combustión; no tiene un solo requisito óptico, y define “visera” como la parte del casco que se proyecta hacia el frente, es decir, el ala. La NOM de equipo de protección personal es de proceso: análisis de riesgos, determinación, entrega, capacitación y supervisión, y en su guía de referencia lista anteojos, goggles y pantalla facial. La forma correcta de armar el documento es citar NFPA para el desempeño y la NOM de EPP para el proceso."
  }
]
''')

# ── Escritura ──────────────────────────────────────────────────────────────────
with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'viseras-y-caretas')

# El nombre se conserva: "Viseras y caretas" ya arranca por el sustantivo que la gente busca
# y el modulo de "Productos mencionados" del blog resuelve por la raiz "visera".
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
for c in L3['catalogo']['cards']:
    assert len(c['specs']) == 4, 'la card %s no tiene 4 specs' % c['modelo']
imgs = [c['img'] for c in L3['catalogo']['cards']] + [g['src'] for g in L3['galeria']] \
       + [L3['heroImg']['src']]
dup = [i for i in set(imgs) if imgs.count(i) > 1]
print('  imagenes repetidas en la pagina:', dup or 'ninguna')
codes = {n['code'] for n in cat.get('normas', [])}
faltan = [c for c in L3['normasRef'] if c not in codes]
print('  normasRef sin entrada en cat.normas:', faltan or 'ninguna')
