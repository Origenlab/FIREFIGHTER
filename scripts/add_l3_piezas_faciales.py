#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tercera L3 de equipos de respiracion: piezas faciales y mascaras completas.

EJE EDITORIAL — es la unica pieza del catalogo que se ajusta a UNA cara, y la unica donde **una
norma oficial mexicana si exige una prueba concreta**: la NOM-033-STPS-2015, en su apartado 6.4,
obliga al trabajador a "realizar pruebas de ajuste, cuando utilicen como equipo de proteccion
personal respiradores con linea de suministro de aire o equipo de respiracion autonomo". Es una
excepcion notable en un catalogo donde casi todo el respaldo normativo es extranjero.

  Y el metodo no es cualquiera. El reglamento estadounidense fija el umbral: apendice A de
  29 CFR 1910.134, seccion I.C.2(b)(9) — "a full facepiece respirator unless a minimum fit factor
  of 500 is obtained". Y su inciso (f)(6) prohibe el metodo cualitativo para eso: solo sirve para
  purificadores de presion negativa con factor de 100 o menos. Ademas, (f)(8): un equipo de
  presion positiva se prueba **en modo de presion negativa**, con adaptador.

SEGUNDO HILO: **los anteojos comunes no se pueden usar debajo**. Dos fabricantes lo publican
textual —"Ordinary eyeglasses cannot be worn under the facepiece"— y los tres venden kit de
montaje interno con numero de parte. Es el dato de compra que nadie mete en una partida y que
deja gente sin poder usar el equipo que se le entrego.

TERCER HILO: **ningun fabricante publica una tabla antropometrica** para elegir talla antes de la
prueba. Hay tres tallas —y una marca usa dos ejes, cuerpo S/M/L por mascara interior 1/2/3—, pero
la talla no se calcula: se determina probando y se registra por usuario.

FUENTES PRIMARIAS consultadas 2026-08-06: OSHA 29 CFR 1910.134 y su apendice A, interpretacion
oficial de OSHA del 20-jun-1997, NIOSH CA 2019-1012 y publicacion 2025-116, NIST sobre la prueba
de calor radiante del visor, hoja de especificacion / bid spec / manual y FAQ del MSA G1, folleto
y datasheet del 3M Scott AV-3000 HT, pagina del AV-3000 SureSeal, bid spec del Vision C5, folleto
e IFU del Drager FPS 7000 y su lista de refacciones, tabla de adaptadores de TSI, y los textos de
NOM-033-STPS-2015, NOM-116-STPS-2009 y la ficha oficial de NOM-017-STPS-2024.

Uso: python3 scripts/add_l3_piezas_faciales.py
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

L3 = collections.OrderedDict()

L3['seoTitle'] = 'Piezas faciales y máscaras completas ERA'
L3['seoDescription'] = (
    'Piezas faciales de ERA en tres tallas, con prueba de ajuste cuantitativa, kit de anteojos y '
    'visor certificado. Qué exige la NOM-033 y qué pedir por escrito.'
)

L3['h1'] = 'Piezas faciales y máscaras completas de presión positiva'
L3['subtitulo'] = (
    'La única pieza del conjunto que se ajusta a una cara en particular, y la única del catálogo '
    'donde una norma oficial mexicana sí exige una prueba concreta: la prueba de ajuste. Se '
    'compra por talla y se entrega por usuario, no por promedio de brigada.'
)

L3['heroImg'] = collections.OrderedDict([
    ('src', '/images/catalogo/1705503828024-600x450.webp'),
    ('alt', 'Piezas faciales de equipo de respiración colgadas en el rack de la estación'),
    ('caption', 'Una talla que no sella es una talla que no protege'),
])

L3['heroBloques'] = [
    collections.OrderedDict([
        ('label', 'Por qué esta pieza se entrega distinto'),
        ('texto',
         'Un sello hermético contra una cara no se resuelve con tres tallas y buena voluntad. La '
         '<strong>NOM-033-STPS obliga a realizar prueba de ajuste</strong> a quien use equipo '
         'autónomo o línea de aire, y el método aplicable a una pieza facial completa es el '
         '<strong>cuantitativo</strong>, con un factor mínimo de <strong>500</strong>. El '
         'cualitativo —sacarina, humo irritante— no vale para esta pieza. Y el equipo, aunque sea '
         'de presión positiva, <strong>se prueba en modo negativo</strong>, con adaptador.'),
    ]),
    collections.OrderedDict([
        ('label', 'Distribución autorizada, no reventa'),
        ('texto',
         'Cotizamos <strong>talla por usuario</strong> a partir de la lista real de la corporación, '
         'con el <strong>kit de anteojos por número de parte</strong> para quien lo necesite '
         '—porque los lentes comunes no se pueden usar debajo— y verificando que la pieza facial '
         'esté dentro de la <strong>configuración aprobada</strong> del equipo. Propuesta técnica '
         'en menos de <strong>24 horas hábiles</strong> y cobertura en los <strong>32 estados</strong>.'),
    ]),
]

L3['heroDatos'] = [
    collections.OrderedDict([('label', 'Factor de ajuste'), ('valor', 'Mínimo 500, cuantitativo')]),
    collections.OrderedDict([('label', 'Tallas publicadas'), ('valor', 'Tres, sin tabla de medidas')]),
]

L3['specStrip'] = [
    collections.OrderedDict([('label', 'Tallas'), ('valor', 'Small, medium y large')]),
    collections.OrderedDict([('label', 'Prueba de ajuste'), ('valor', 'Cuantitativa, factor 500')]),
    collections.OrderedDict([('label', 'Frecuencia'), ('valor', 'Inicial, por cambio y anual')]),
    collections.OrderedDict([('label', 'Anteojos'), ('valor', 'Solo con kit interno')]),
    collections.OrderedDict([('label', 'Visor'), ('valor', 'Policarbonato con recubrimiento')]),
    collections.OrderedDict([('label', 'Doble uso'), ('valor', 'Con adaptador de la misma marca')]),
]

CARDS = json.loads(r'''
[
  {
    "marca": "MSA",
    "modelo": "G1",
    "variante": "Tres tallas",
    "varianteLabel": "Plataforma",
    "fichaLabel": "la pieza facial MSA G1",
    "badge": "NFPA · NIOSH",
    "estado": "La mejor documentada",
    "img": "/images/catalogo/1592235905030-600x450.webp",
    "alt": "Bombero con pieza facial de equipo de respiración bajo el casco estructural",
    "desc": "Es la que más publica, y con un detalle que ahorra errores en el rack: los <strong>puntos de anclaje del arnés van codificados por color</strong> —verde para small, negro para medium, gris para large—, además de la letra impresa. Sello de <strong>hule Hycar</strong> en tres tallas con opción hipoalergénica, máscara interior de silicón removible en tres tallas, y visor de <strong>policarbonato endurecido por fuera y con antivaho por dentro</strong>, reemplazable en campo y común a las tres tallas.",
    "specs": [
      "Anclajes codificados por color: verde, negro y gris",
      "Kevlar de 4 y 5 puntos, o hule de 5 puntos",
      "Sello Hycar, con alternativa hipoalergénica",
      "Kit de anteojos 10144230 para montaje interno"
    ],
    "chip": "Pedir talla por usuario, no por lote"
  },
  {
    "marca": "3M Scott",
    "modelo": "AV-3000 HT",
    "variante": "Cuatro o cinco tiras",
    "varianteLabel": "Arnés",
    "fichaLabel": "la 3M Scott AV-3000 HT",
    "badge": "NFPA 1970-2025",
    "estado": "Se pide con lado",
    "img": "/images/catalogo/1606613640173-600x400.webp",
    "alt": "Bombero de espaldas con equipo de respiración y pieza facial puesta",
    "desc": "La familia <strong>201215-xx</strong> con una particularidad que hay que resolver en la orden y no en la entrega: se surte <strong>sin bracket, con bracket derecho o con bracket izquierdo</strong>, según de qué lado vaya el amplificador de voz. Arnés de punto de Kevlar en versiones de cuatro y cinco tiras, con opción de neopreno, y <strong>dos voicemitters mecánicos</strong>. El sello se publica como polisopreno y la máscara interior como silicón en la ficha internacional.",
    "specs": [
      "Familia 201215-xx en tres tallas",
      "Sin bracket, bracket derecho o izquierdo",
      "Kevlar de 4 o 5 tiras, opción de neopreno",
      "Dos voicemitters mecánicos"
    ],
    "chip": "Definir el lado del bracket en la orden"
  },
  {
    "marca": "3M Scott",
    "modelo": "AV-3000 SureSeal",
    "variante": "Convertible",
    "varianteLabel": "Plataforma",
    "fichaLabel": "la AV-3000 SureSeal",
    "badge": "APR · SAR · PAPR · SCBA",
    "estado": "Una pieza, cuatro usos",
    "img": "/images/catalogo/1776104501594-600x400.webp",
    "alt": "Piezas faciales de equipo respiratorio en un taller de mantenimiento",
    "desc": "La propuesta que más sentido tiene para una brigada industrial: el fabricante la publica como <strong>“top down convertibility”</strong>, una sola pieza facial aprobada <strong>desde el purificador hasta el equipo autónomo</strong>, pasando por línea de aire y motorizado. Se convierte con <strong>adaptadores de 40 mm</strong> de la misma marca. La ventaja real no es de precio: es que <strong>el usuario se ajusta a una sola cara de sello</strong> y esa prueba de ajuste sirve para los cuatro modos.",
    "specs": [
      "Aprobada en APR, SAR, PAPR y SCBA",
      "Adaptadores de 40 mm: 200423-01, 200423-02 y otros",
      "Una sola prueba de ajuste para los cuatro modos",
      "Material del sello: no publicado por el fabricante"
    ],
    "chip": "Solo con adaptadores de la misma marca"
  },
  {
    "marca": "3M Scott",
    "modelo": "Vision C5",
    "variante": "Comunicación",
    "varianteLabel": "Plataforma",
    "fichaLabel": "la Vision C5",
    "badge": "NFPA",
    "estado": "Radio sin cable",
    "img": "/images/catalogo/1608723724615-600x450.webp",
    "alt": "Dos bomberos con equipo de respiración operando entre humo",
    "desc": "Visor descrito como <strong>policarbonato resistente a alta temperatura y a calor radiante, tipo no astillable</strong>, con recubrimiento antiabrasión por fuera y tratamiento interior contra el empañamiento. Suspensión de <strong>cinco puntos, cuatro ajustables</strong>, más dos tiras elastoméricas fijadas al sello. Y la diferencia que se nota en operación: interfaz <strong>directa por radio sin cable</strong>, con equipos habilitados para conexión inalámbrica, en lugar de un amplificador colgado.",
    "specs": [
      "Tres tallas marcadas S, M y L",
      "Suspensión de 5 puntos, 4 ajustables",
      "Dos voicemitters embutidos, uno por lado",
      "Interfaz de radio sin cable, opcional"
    ],
    "chip": "Confirmar compatibilidad con la radio"
  },
  {
    "marca": "Dräger",
    "modelo": "FPS 7000",
    "variante": "Talla en dos ejes",
    "varianteLabel": "Plataforma",
    "fichaLabel": "la Dräger FPS 7000",
    "badge": "NIOSH · EN según versión",
    "estado": "El sistema de tallas más fino",
    "img": "/images/catalogo/1777059017572-600x450.webp",
    "alt": "Bombera de perfil con equipo de respiración junto a la unidad",
    "desc": "Resuelve el tallaje distinto a todos: <strong>cuerpo en S, M y L combinado con máscara interior en tallas 1, 2 y 3</strong>, dos ejes en lugar de uno. Sello en <strong>EPDM o silicón</strong>, con doble sello facial y triple línea de sellado, y siete variantes de visor publicadas —policarbonato liso, antirrayaduras, antivaho, APEC, triplex— más versiones específicas para bomberos, para impacto balístico y para temperatura extrema. Sujeción de cinco puntos de hule o red textil, y conexión de dos puntos al casco de la misma marca.",
    "specs": [
      "Cuerpo S, M, L × máscara interior 1, 2, 3",
      "Sello de EPDM o de silicón",
      "Siete variantes de visor publicadas",
      "Módulos de comunicación FPS-COM 5000 y 7000"
    ],
    "chip": "Pedir la combinación exacta de tallas"
  },
  {
    "marca": "Multimarca",
    "modelo": "Kit de anteojos",
    "variante": "Montaje interno",
    "varianteLabel": "Accesorio",
    "fichaLabel": "el kit de anteojos",
    "badge": "Por número de parte",
    "estado": "El renglón que falta",
    "img": "/images/catalogo/1584033376505-600x400.webp",
    "alt": "Rostro de bombero con casco estructural y lámpara integrada",
    "desc": "Está en el catálogo porque es el renglón que casi nunca aparece en una partida y que deja gente sin poder usar el equipo. Dos fabricantes lo publican textual: <strong>los anteojos comunes no se pueden usar debajo de la pieza facial</strong>, porque las patillas cruzan la línea de sellado. La solución es un <strong>armazón que se monta dentro</strong> y al que el óptico le pone las micas graduadas del usuario: <strong>10144230</strong> en una marca, <strong>R56230</strong> y su armazón en otra, <strong>805773-01</strong> con armazones de 52 y 60 mm en la tercera.",
    "specs": [
      "10144230 · R56230 · 805773-01 según marca",
      "Las micas graduadas las pone el óptico del usuario",
      "Los anteojos comunes rompen el sello",
      "Se cotiza por usuario que use lentes"
    ],
    "chip": "Levantar quién usa lentes antes de cotizar"
  }
]
''')

L3['catalogo'] = collections.OrderedDict([
    ('eyebrow', 'Catálogo por plataforma'),
    ('titulo', 'Piezas faciales\npor plataforma, talla y sello'),
    ('intro',
     'Cuatro datos deciden esta pieza y ninguno se ve en una foto: <strong>qué tallas publica el '
     'fabricante, de qué material es el sello, si el visor lleva recubrimiento por dentro o por '
     'fuera y si acepta un kit de anteojos</strong>. Los cuatro se leen en la hoja de '
     'especificación —cuando el fabricante la publica, porque no todos publican el material del '
     'sello—.'),
    ('imgRef', 'Imagen de referencia de la línea'),
    ('nota',
     'La pieza facial forma parte de la <strong>configuración aprobada</strong> del equipo: no se '
     'cruza entre marcas, ni siquiera cuando la conexión coincide. Y dentro de una misma marca hay '
     'variantes que no son equivalentes —un fabricante marca su arnés de poliéster de cuatro '
     'puntos como <strong>“non-NFPA, industrial use only”</strong>, con la misma pieza facial—.'),
    ('cards', CARDS),
])

L3['secciones'] = json.loads(r'''
[
  {
    "id": "prueba-de-ajuste",
    "eyebrow": "La excepción mexicana",
    "titulo": "Aquí sí hay una NOM que exige una prueba",
    "parrafos": [
      "En casi todo el catálogo el respaldo normativo es extranjero y la NOM aporta el proceso. Esta pieza es la excepción, y conviene saberlo con numeral: la <strong>NOM-033-STPS-2015</strong>, en su apartado <strong>6.4</strong>, establece como obligación de los trabajadores <em>“realizar pruebas de ajuste, cuando utilicen como equipo de protección personal respiradores con línea de suministro de aire o equipo de respiración autónomo”</em>. Y su apartado 9.4 pide que el procedimiento de seguridad contenga el de <strong>revisión de ajuste y prueba de hermeticidad</strong>.",
      "El alcance de esa norma es el <strong>trabajo en espacios confinados</strong>, así que no es una obligación general de todo centro de trabajo. Pero es el único requisito mexicano de prueba de ajuste que localizamos, y en la práctica marca el estándar: si una brigada ya la hace para espacio confinado, no tiene sentido que no la haga para combate estructural con el mismo equipo y la misma gente.",
      "El método sí viene de fuera y es específico. El reglamento estadounidense fija que una <strong>pieza facial completa necesita un factor de ajuste mínimo de 500</strong> bajo protocolo cuantitativo, y <strong>prohíbe el método cualitativo</strong> para eso: la sacarina y el humo irritante solo sirven para purificadores de presión negativa con factor de 100 o menos. Un detalle contraintuitivo: aunque el equipo trabaje con presión positiva, <strong>la prueba se hace en modo de presión negativa</strong>, con adaptador."
    ],
    "tabla": {
      "head": ["Cuándo", "Qué exige la regla", "Qué queda documentado"],
      "rows": [
        ["Antes del primer uso", "Prueba de ajuste con la talla y el modelo que se va a usar", "Registro por usuario con marca, modelo y talla"],
        ["Al cambiar de pieza facial", "Nueva prueba si cambia <strong>talla, estilo, modelo o marca</strong>", "Registro nuevo: el anterior ya no aplica"],
        ["Cada año", "Repetición al menos anual", "Historial por usuario"],
        ["Método", "<strong>Cuantitativo</strong>, factor mínimo de 500", "Número medido, no una apreciación"],
        ["Modo", "Presión negativa, con adaptador de la marca", "Número de parte del adaptador usado"]
      ]
    },
    "nota": "Hay adaptadores publicados por marca y modelo para el equipo de medición más usado, y los fabricantes también publican los suyos. Es un consumible del programa, no una compra única: <strong>si la corporación no tiene con qué probar, la prueba no ocurre</strong>."
  },
  {
    "id": "tallas",
    "eyebrow": "Cómo se elige la talla",
    "titulo": "Tres tallas, y ningún fabricante publica cómo medir",
    "parrafos": [
      "Revisamos las hojas de especificación, los bid specs y los manuales de las tres marcas principales y el resultado es consistente: <strong>ninguna publica una tabla antropométrica</strong> —largo de cara, ancho entre pómulos— para elegir talla antes de probar. Una de ellas dice explícitamente que <strong>la responsabilidad de asistir al usuario en la selección de talla es del administrador del programa</strong>, y no le da criterios dimensionales.",
      "Lo que sí hay son sistemas de tallaje distintos entre marcas, y uno de ellos es notablemente más fino: dos fabricantes ofrecen <strong>tres tallas de cuerpo</strong>, y un tercero combina <strong>tres tallas de cuerpo con tres de máscara interior</strong>, que da un abanico mayor de combinaciones para caras que no caen en el promedio. También hay ayudas físicas: una marca <strong>codifica por color los anclajes del arnés</strong> para que la talla se reconozca de un vistazo en el rack."
    ],
    "lista": [
      { "t": "Cómo se determina en la práctica", "d": "<strong>Probando</strong>, con el equipo de medición puesto, y se registra. No hay forma de calcularla en un escritorio a partir de una lista de personal." },
      { "t": "Qué implica en la orden", "d": "Un pedido de <strong>cantidad por talla levantada por usuario</strong>. Comprar “un tercio de cada talla” garantiza que a alguien no le selle." },
      { "t": "Por qué importa el reconocimiento visual", "d": "Porque en una estación las piezas faciales se comparten de turno a turno. Los anclajes de color o la letra impresa evitan que alguien salga con la talla equivocada." },
      { "t": "La máscara interior también talla", "d": "En la marca que la publica por separado, la máscara interior tiene su propia talla. Pedir solo la del cuerpo deja la mitad de la decisión sin tomar." }
    ],
    "nota": "Consecuencia de compra que conviene anticipar: el <strong>surtido de tallas no se puede definir sin la lista de usuarios</strong>. Cuando una convocatoria pide “20 piezas faciales” sin desglose, lo que está pidiendo es que el proveedor adivine."
  },
  {
    "id": "anteojos",
    "eyebrow": "Lo que rompe el sello",
    "titulo": "Barba, patillas de anteojos y cicatrices",
    "parrafos": [
      "El sello es una línea continua de contacto entre la pieza facial y la piel, y cualquier cosa que la cruce la rompe. Los fabricantes lo publican en sus manuales con nombre propio: <strong>barba, patillas grandes y cicatrices profundas en la zona de sellado</strong>, y una marca añade el pelo largo recogido. El reglamento estadounidense lo convierte en prohibición: no se permite vello facial que quede entre la superficie de sellado y la cara, y la prueba de ajuste <strong>ni siquiera se realiza</strong> si hay crecimiento de barba que cruce el sello.",
      "Y está el punto que casi nunca entra en una partida: <strong>los anteojos comunes no se pueden usar debajo de la pieza facial</strong>. Dos de los tres fabricantes lo publican textual —uno de ellos escribe que “los anteojos ordinarios no pueden usarse bajo la pieza facial” y que quien usa lentes <strong>debe</strong> usar el kit—. La solución existe, tiene número de parte y cuesta poco comparado con el equipo: un <strong>armazón que se monta dentro</strong>, al que el óptico del usuario le pone las micas graduadas."
    ],
    "lista": [
      { "t": "Barba", "d": "No hay excepción, ni siquiera de un día. La prueba de ajuste no se realiza con vello cruzando el sello, así que tampoco hay forma de documentar que el equipo protege." },
      { "t": "Anteojos", "d": "Kit interno con número de parte por marca. <strong>Se levanta quién usa lentes antes de cotizar</strong>: es un renglón aparte y con plazo propio, porque las micas las gradúa el óptico." },
      { "t": "Cicatrices", "d": "Una cicatriz profunda en la línea de sellado puede impedir el contacto continuo. Se detecta en la prueba de ajuste, no en la entrega." },
      { "t": "Otros EPP", "d": "El reglamento pide que cualquier otro equipo de protección se use de forma que no interfiera con el sello. En una estación eso incluye la capucha y el casco, que van por encima." }
    ],
    "nota": "Dato para el programa, no para el catálogo: una corporación que entrega piezas faciales sin levantar quién usa lentes está entregando equipo que una parte del personal <strong>no va a poder usar</strong>, y la factura no lo va a decir."
  },
  {
    "id": "visor",
    "eyebrow": "El único componente con prueba de fuego publicada",
    "titulo": "Qué se le hace al visor para certificarlo",
    "parrafos": [
      "Esta es la parte donde la certificación NFPA se vuelve tangible, y hay cifras publicadas. La prueba de <strong>calor radiante del visor</strong> se introdujo en la edición 2013 del estándar de equipos de respiración y es obligatoria desde septiembre de ese año: el equipo se expone a <strong>15 kW/m² durante 5 minutos</strong> mientras respira a <strong>40 litros por minuto</strong>, y después debe <strong>mantener presión positiva por un total de 24 minutos</strong>. Existe además una prueba de calor y flama: <strong>horno a 260 °C durante 5 minutos</strong>, seguido de exposición directa a flama por <strong>10 segundos</strong> y una prueba de caída.",
      "Esa prueba no nació de un comité: nació de fallas de visor reportadas en incendios, y el instituto federal estadounidense mantiene una alerta activa sobre <strong>degradación térmica y falla del visor</strong>, recomendando reemplazar o actualizar equipos que no cumplan la edición 2013 o posterior. Es el argumento más fuerte que existe para no comprar equipo de generaciones anteriores por precio."
    ],
    "tabla": {
      "head": ["Qué publica el fabricante", "Marca A", "Marca B", "Marca C"],
      "rows": [
        ["Material del visor", "Policarbonato endurecido", "“Materiales de alto desempeño” en el folleto local; policarbonato en la ficha internacional", "Hasta siete variantes: policarbonato, antirrayaduras, antivaho, APEC, triplex"],
        ["Recubrimiento", "Endurecido por fuera, antivaho por dentro", "Antiabrasión y tratamiento antivaho interior", "Según variante"],
        ["Clase óptica", "No publicada", "No publicada", "Referencia europea en la versión para bomberos"],
        ["Ciclos de abrasión", "No publicados", "No publicados", "No publicados"]
      ]
    },
    "nota": "Ningún fabricante publica <strong>cifras de resistencia a la abrasión</strong> ni vida útil del recubrimiento antivaho: las declaraciones son cualitativas. Y una marca advierte algo que sí es operativo: <strong>los visores con antivaho no admiten el procedimiento de lavado en máquina</strong>, y el procedimiento equivocado daña el visor."
  },
  {
    "id": "configuracion",
    "eyebrow": "Lo que no se cruza",
    "titulo": "La pieza facial es parte de la configuración aprobada",
    "parrafos": [
      "Vale repetirlo aquí porque es donde más se rompe en el mercado mexicano: la aprobación del aparato respiratorio <strong>se emite al conjunto ensamblado</strong> y la pieza facial forma parte de esa lista. El instituto que la emite lo publica sin rodeos: la aprobación aplica solo al respirador específico compuesto por los componentes incluidos en la etiqueta, y las adiciones o modificaciones que puedan afectar el desempeño <strong>anulan la aprobación</strong>.",
      "La autoridad laboral estadounidense lo llevó a una interpretación oficial que conviene tener a la mano en una junta de aclaraciones: <strong>los empleadores que usan componentes de otros fabricantes en su equipo están anulando la aprobación</strong>. La única concesión que reconoce es el intercambio de <strong>cilindros</strong> en emergencia para salvar vidas, y con la obligación de devolver el equipo a su condición aprobada después.",
      "Los fabricantes no publican la prohibición con esas palabras, pero publican la equivalente: usar solo partes exactas de repuesto en la configuración especificada, y solo combinaciones aprobadas con componentes auténticos. Y hay una trampa dentro de una misma marca: un fabricante marca su <strong>arnés de poliéster de cuatro puntos como “non-NFPA, industrial use only”</strong>, con la misma pieza facial. Dos configuraciones que se ven casi iguales y solo una sirve para combate estructural."
    ],
    "lista": [
      { "t": "Entre marcas", "d": "No. Ni pieza facial de una marca con regulador de otra, ni al revés, aunque la conexión embone." },
      { "t": "Dentro de la marca", "d": "Solo lo que esté en la matriz de la etiqueta. El arnés, el nosecup y el visor tienen número de parte y aparecen ahí." },
      { "t": "Lo que sí se puede", "d": "Reponer con el número de parte publicado por el fabricante para esa configuración. Es la única forma de mantener el conjunto dentro de lo aprobado." },
      { "t": "Cómo se verifica", "d": "Con la <strong>etiqueta de aprobación del equipo</strong>, que lista los componentes con su clave. No con el certificado del modelo." }
    ],
    "nota": "En una recepción esto se traduce en una revisión de dos minutos: que la clave del arnés y la del nosecup que llegaron <strong>estén en la matriz</strong>. Si llegó un arnés industrial en un equipo de bomberos, se ve ahí y no en la foto."
  },
  {
    "id": "doble-uso",
    "eyebrow": "Una cara, cuatro modos",
    "titulo": "La misma pieza facial para purificador, línea de aire y autónomo",
    "parrafos": [
      "Para una brigada industrial esta es probablemente la decisión con mejor retorno de toda la categoría, y está publicada: hay piezas faciales aprobadas <strong>de arriba hacia abajo</strong>, desde el purificador de aire hasta el equipo autónomo, pasando por línea de aire y por motorizado. La conversión se hace con un <strong>adaptador roscado de 40 milímetros</strong> del mismo fabricante, con número de parte.",
      "La ventaja no es de inventario, aunque también: es que <strong>el usuario se ajusta a una sola cara de sello</strong>. La prueba de ajuste que se le hizo sirve para los cuatro modos, en lugar de repetirse por cada tipo de respirador. En una planta con brigada eso reduce a la mitad el trabajo del programa y elimina la escena de un elemento con dos tallas distintas según qué equipo tome."
    ],
    "nota": "El matiz que evita un error caro: el doble uso vale <strong>dentro de la matriz de aprobación del mismo fabricante y con su propio adaptador</strong>. Un adaptador no convierte una pieza facial en un respirador aprobado con filtros de otra marca."
  },
  {
    "id": "voz",
    "eyebrow": "Hacerse entender",
    "titulo": "Dos voicemitters, un amplificador y una norma que cambió de método",
    "parrafos": [
      "Toda pieza facial estructural trae <strong>diafragma o voicemitter mecánico</strong> —una o dos ventanas acústicas— y sobre eso se monta la comunicación electrónica, que ya no es accesorio de lujo. Un fabricante integra el amplificador en el propio equipo, con <strong>micrófono doble en el regulador</strong> —para cancelar el ruido de la inhalación— y bocina en la correa del hombro. Otro lo vende como módulo aparte con número de parte y <strong>50 horas de operación</strong> con tres pilas alcalinas, y por eso su pieza facial se pide con bracket derecho o izquierdo. Un tercero ofrece interfaz directa por radio, sin cable.",
      "Y hay un cambio de método que explica por qué las comparaciones viejas ya no sirven: la norma <strong>dejó de medir la inteligibilidad con una prueba de palabras leídas por personas</strong> y adoptó un índice instrumental de transmisión de voz, precisamente porque el método anterior era subjetivo y poco repetible."
    ],
    "nota": "Advertencia de dato: <strong>el valor mínimo que exige la norma para ese índice no está publicado</strong> fuera del texto de pago, y ningún fabricante publica decibeles de amplificación. Si una especificación pide “X dB de amplificación”, nadie puede acreditarlo con documento."
  },
  {
    "id": "cuidado",
    "eyebrow": "Ciclo de vida",
    "titulo": "Se lava después de cada uso, y con lo que el fabricante permite",
    "parrafos": [
      "Es la pieza que toca la cara, así que la limpieza no es mantenimiento: es higiene, y es obligatoria <strong>después de cada uso</strong> y <strong>entre usuarios</strong> cuando se comparte. Lo importante es con qué. Un fabricante nombra su germicida por número de parte y <strong>prohíbe el alcohol</strong> —deteriora las partes de hule— y los limpiadores con hidrocarburos o solventes. Otro publica hasta la <strong>concentración y la temperatura máxima</strong> de cada agente permitido, y prohíbe acetona, alcohol y limpiadores con partículas abrasivas. El secado va en gabinete <strong>por debajo de 60 °C</strong>, nunca al sol ni con calor radiante.",
      "Los intervalos de servicio también están publicados, y son más largos de lo que la gente supone: revisión antes y después de cada uso, <strong>inspección visual y prueba de fuga cada seis meses</strong>, cambio de discos de válvula <strong>cada cuatro años</strong> y de anillos y diafragma <strong>cada seis</strong>. Eso convierte a la pieza facial en una pieza con refacciones programables, no en un consumible."
    ],
    "lista": [
      { "t": "Lo que está prohibido", "d": "<strong>Alcohol, acetona, solventes e hidrocarburos</strong>, y cualquier limpiador con partículas abrasivas. Son la causa más común de un visor turbio y de un sello endurecido." },
      { "t": "El visor antivaho es distinto", "d": "No admite el procedimiento de lavado en máquina que sí aceptan otros visores. El procedimiento equivocado <strong>daña el recubrimiento</strong>." },
      { "t": "Refacciones con clave", "d": "Visor, válvula de exhalación, diafragma de voz, arnés, máscara interior y kit de anteojos tienen número de parte. Se cotizan por clave, no por descripción." },
      { "t": "Cuándo se retira", "d": "<strong>Ningún fabricante publica una vida útil ni una fecha de retiro</strong> para la pieza facial. El único criterio publicado es funcional: una máscara que fuga no se usa." }
    ],
    "nota": "Ese último vacío tiene una consecuencia presupuestal: como no hay fecha de caducidad, la pieza facial <strong>se reemplaza cuando falla la prueba de fuga o la de ajuste</strong>. Por eso el programa de pruebas no es un trámite: es el único mecanismo que detecta el final de vida de esta pieza."
  }
]
''')

L3['galeriaIntro'] = (
    'Referencias de la pieza en uso. Lo único que decide si protege no aparece en ninguna foto ni '
    'en ninguna ficha: <strong>el número que arroja la prueba de ajuste de ese usuario con esa '
    'talla</strong>. Dos personas con la misma pieza facial pueden tener resultados opuestos.'
)

L3['galeria'] = json.loads(r'''
[
  {
    "src": "/images/catalogo/1606613816768-1000x750.webp",
    "alt": "Dos bomberos con equipo de respiración autónoma en la calle",
    "caption": "El sello se verifica con capucha y casco puestos"
  },
  {
    "src": "/images/catalogo/1756112277157-1000x750.webp",
    "alt": "Equipo de protección alineado en el rack de la estación",
    "caption": "La talla se reconoce de un vistazo, o se confunde"
  },
  {
    "src": "/images/catalogo/1563062067-bb-600x450.webp",
    "alt": "Bombero de perfil con casco rojo y equipo de respiración",
    "caption": "Entre maniobras, sin pieza facial puesta"
  },
  {
    "src": "/images/catalogo/1705503729371-600x400.webp",
    "alt": "Equipo de protección colgado en el rack de la estación",
    "caption": "Limpieza después de cada uso y entre usuarios"
  }
]
''')

L3['aplicaciones'] = json.loads(r'''
[
  {
    "sector": "Cuerpos de bomberos",
    "desc": "Talla levantada por usuario con prueba de ajuste documentada, y el kit de anteojos cotizado aparte para quien usa lentes. Es la pieza donde un pedido por promedio de brigada garantiza que a alguien no le selle."
  },
  {
    "sector": "Espacios confinados",
    "desc": "Es el escenario donde la NOM-033-STPS obliga expresamente a realizar prueba de ajuste a quien usa equipo autónomo o línea de suministro de aire, y donde el procedimiento de seguridad debe incluir la revisión de ajuste y hermeticidad."
  },
  {
    "sector": "Industria química",
    "desc": "Donde más rinde una pieza facial convertible: aprobada desde purificador hasta equipo autónomo con adaptador de la misma marca, una sola prueba de ajuste por persona sirve para los cuatro modos de respirador."
  }
]
''')

L3['datoClave'] = collections.OrderedDict([
    ('titulo', 'La única prueba que sí exige una norma mexicana'),
    ('texto',
     'La <strong>NOM-033-STPS-2015, apartado 6.4</strong>, obliga a los trabajadores a realizar '
     '<strong>pruebas de ajuste</strong> cuando usen respiradores con línea de suministro de aire '
     'o equipo de respiración autónomo. Es en el contexto de espacios confinados, pero es el único '
     'requisito mexicano de prueba de ajuste que localizamos —y el método aplicable a una pieza '
     'facial completa es el <strong>cuantitativo, con factor mínimo de 500</strong>.'),
])

L3['normasRef'] = ['NIOSH 42 CFR 84', 'NFPA 1970', 'NOM-033-STPS', 'NOM-116-STPS',
                   'NOM-017-STPS', 'NFPA 1850']

L3['documentacion'] = [
    'Registro de prueba de ajuste cuantitativa por usuario, con marca, modelo, talla y factor obtenido',
    'Número de parte de la pieza facial por talla y de su arnés, dentro de la configuración aprobada',
    'Etiqueta de aprobación del equipo donde aparezca la clave de la pieza facial entregada',
    'Número de parte del kit de anteojos para cada usuario que use lentes',
    'Instrucciones de limpieza y desinfección del fabricante, con los agentes permitidos',
    'Programa de servicio con los intervalos de inspección y de cambio de válvulas y diafragma',
    'Números de parte de refacciones: visor, sello, arnés, máscara interior y diafragma de voz',
]

L3['blog'] = [
    'mascaras-scba-seleccion-guia',
    'guia-scba-equipos-respiracion-autonoma',
    'espacios-confinados-proteccion-respiratoria',
    'mantenimiento-scba-programa-anual',
    'scba-msa-g1-guia-tecnica',
    'nfpa-1981-mexico-equipos-respiracion',
]

L3['faqs'] = json.loads(r'''
[
  {
    "q": "¿La prueba de ajuste es obligatoria en México?",
    "a": "Sí, en un contexto concreto. La NOM-033-STPS-2015, sobre trabajos en espacios confinados, establece en su apartado 6.4 la obligación de los trabajadores de realizar pruebas de ajuste cuando utilicen respiradores con línea de suministro de aire o equipo de respiración autónomo, y en su apartado 9.4 pide que el procedimiento de seguridad incluya la revisión de ajuste y la prueba de hermeticidad. No localizamos una NOM que la exija de forma general para todo centro de trabajo, pero en la práctica una brigada que ya la hace para espacio confinado no tiene por qué no hacerla para combate estructural con el mismo equipo."
  },
  {
    "q": "¿Sirve la prueba con sacarina o con humo irritante?",
    "a": "No para esta pieza. El reglamento estadounidense es explícito: el método cualitativo solo puede usarse para respiradores purificadores de presión negativa que deban alcanzar un factor de 100 o menos. Una pieza facial completa requiere un factor mínimo de 500 y eso solo se acredita con método cuantitativo, que arroja un número medido. Y hay un detalle contraintuitivo: aunque el equipo trabaje con presión positiva, la prueba se realiza en modo de presión negativa, con un adaptador específico de la marca y el modelo."
  },
  {
    "q": "¿Cómo sé qué talla pedir para cada persona?",
    "a": "Probando. Revisamos hojas de especificación, bid specs y manuales de las tres marcas principales y ninguna publica una tabla antropométrica —largo de cara, ancho entre pómulos— para elegir talla antes de la prueba; una de ellas asigna la responsabilidad al administrador del programa sin darle criterios dimensionales. Hay tres tallas de cuerpo en general, y una marca que combina tres tallas de cuerpo con tres de máscara interior, lo que da más combinaciones para caras fuera del promedio. La consecuencia de compra es directa: el surtido de tallas no se puede definir sin la lista de usuarios."
  },
  {
    "q": "¿Se pueden usar anteojos debajo de la pieza facial?",
    "a": "Los comunes no. Dos de los tres fabricantes lo publican textualmente —los anteojos ordinarios no pueden usarse bajo la pieza facial— porque las patillas cruzan la línea de sellado y la rompen. Lo que sí existe es un kit de montaje interno con número de parte, un armazón que va dentro de la máscara y al que el óptico del usuario le coloca sus micas graduadas. Es un renglón aparte, con plazo propio, y conviene levantar quién usa lentes antes de cotizar: si no, se entrega equipo que parte del personal no va a poder usar."
  },
  {
    "q": "¿Puedo usar una pieza facial de una marca con el regulador de otra?",
    "a": "No. La aprobación del aparato respiratorio se emite al conjunto ensamblado y la pieza facial forma parte de esa lista de componentes; el instituto que la emite publica que las adiciones o modificaciones que puedan afectar el desempeño anulan la aprobación. La autoridad laboral estadounidense lo llevó a una interpretación oficial: los empleadores que usan componentes de otros fabricantes están anulando la aprobación de su equipo. La única concesión reconocida es el intercambio de cilindros en una emergencia para salvar vidas, con obligación de restituir la condición aprobada después."
  },
  {
    "q": "¿Puede la misma pieza facial servir para filtro y para equipo autónomo?",
    "a": "Sí, si el fabricante la publica así y se usa su propio adaptador. Hay piezas faciales aprobadas de arriba hacia abajo —purificador, línea de aire, motorizado y autónomo— que se convierten con un adaptador roscado de 40 milímetros con número de parte. La ventaja mayor no es de inventario sino de programa: el usuario se ajusta a una sola cara de sello, así que una prueba de ajuste sirve para los cuatro modos. El límite importa: el doble uso vale dentro de la matriz de aprobación del mismo fabricante; un adaptador no convierte la pieza facial en un respirador aprobado con filtros de otra marca."
  },
  {
    "q": "¿Con qué se limpia y qué la arruina?",
    "a": "Con lo que el fabricante permite, y hay diferencias entre marcas: una nombra su germicida por número de parte y prohíbe el alcohol porque deteriora las partes de hule, además de los limpiadores con hidrocarburos o solventes; otra publica hasta la concentración y la temperatura máxima de cada agente permitido y prohíbe acetona, alcohol y abrasivos. El secado va en gabinete por debajo de 60 °C, nunca al sol ni con calor radiante. Y hay una advertencia específica que se ignora seguido: los visores con recubrimiento antivaho no admiten el procedimiento de lavado en máquina, y el procedimiento equivocado daña el visor."
  },
  {
    "q": "¿Cada cuándo se reemplaza una pieza facial?",
    "a": "No hay fecha. Ningún fabricante consultado publica una vida útil ni un criterio de retiro por antigüedad para la pieza facial; el único criterio publicado es funcional, una máscara que fuga no se usa. Lo que sí publican son intervalos de servicio: revisión antes y después de cada uso, inspección visual y prueba de fuga cada seis meses, cambio de discos de válvula cada cuatro años y de anillos y diafragma cada seis. En la práctica eso significa que el programa de pruebas es el único mecanismo que detecta el final de vida de esta pieza, y por eso no es un trámite."
  }
]
''')

# ── Escritura ──────────────────────────────────────────────────────────────────
with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'equipos-de-respiracion')
prod = next(p for p in cat['productos'] if p['slug'] == 'mascaras-completas-3m')
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
assert not (set(ids) & {'ficha', 'galeria', 'sectores', 'preguntas', 'configuraciones', 'catalogo'})
for c in L3['catalogo']['cards']:
    assert len(c['specs']) == 4, 'la card %s no tiene 4 specs' % c['modelo']
imgs = [c['img'] for c in L3['catalogo']['cards']] + [g['src'] for g in L3['galeria']]
print('  imágenes repetidas en la página:',
      [i for i in set(imgs) if imgs.count(i) > 1] or 'ninguna')
codes = {n['code'] for n in cat.get('normas', [])}
print('  normasRef sin entrada en la categoría:',
      [c for c in L3['normasRef'] if c not in codes] or 'ninguna')
previas = {f['q'] for f in cat.get('faqs', [])}
for p2 in cat['productos']:
    if p2.get('l3') and p2['slug'] != prod['slug']:
        previas |= {f['q'] for f in p2['l3']['faqs']}
print('  FAQs repetidas de la L2 o de sus hermanas:',
      [q for q in (f['q'] for f in L3['faqs']) if q in previas] or 'ninguna')
