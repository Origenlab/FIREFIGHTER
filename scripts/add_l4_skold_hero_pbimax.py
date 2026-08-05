# -*- coding: utf-8 -*-
"""L4 — ficha de la configuracion SKOLD HERO · PBI MAX 7.0.

Ruta: /productos/epp-para-bomberos/trajes-estructurales-nomex-pbi/skold-hero-pbi-max-7-0

Todo el dato tecnico sale de la ficha FT_HEROPBI_2023(B) de SKOLD y de la pagina oficial
del modelo, ya verificadas en LGACONTRAINCENDIOS/src/data/productos/trajeSkoldHero.mjs
(fuente revisada 2026-07-20). Lo que el fabricante no publica se dice que no lo publica.
"""
import json, io, collections, os, re

RUTA = 'src/data/productos.json'

L4 = collections.OrderedDict([
  ("seoTitle", "Traje SKÖLD HERÖ PBI MAX 7.0 certificado UL"),
  ("seoDescription",
    "Traje estructural SKÖLD HERÖ con barrera PBI MAX de 7 oz, Stedair 3000 y Defender M. "
    "Certificación UL, expediente MH60435, tallas S a 4X y cotización en 24 h."),
  ("h1", "Traje estructural SKÖLD HERÖ con barrera PBI MAX 7.0"),
  ("subtitulo",
    "Chaquetón y pantalón del conjunto HERÖ en su única configuración documentada: exterior "
    "PBI MAX de 7 oz en 70 % PBI y 30 % Kevlar, barrera de humedad Stedair 3000 y barrera "
    "térmica Defender M, con certificación de laboratorio UL bajo el expediente MH60435."),

  ("heroImg", {
    "src": "/images/catalogo/1592235905030-1000x750.webp",
    "alt": "Bombero con ensamble estructural completo, casco y equipo de respiración autónoma",
  }),
  ("heroBloques", [
    {
      "label": "Por qué esta configuración es la referencia",
      "texto": (
        "SKÖLD lista cinco barreras exteriores para el HERÖ y <strong>solo esta publica "
        "composición y gramaje</strong>. La diferencia no es de marketing: cuando una "
        "convocatoria pide “traje estructural de PBI”, un anexo técnico se puede sostener con "
        "números —7 oz, 70 % PBI, 30 % Kevlar, Stedair 3000, Defender M— o se puede sostener "
        "con adjetivos. Solo lo primero aguanta una aclaración de bases o una impugnación."
      ),
    },
    {
      "label": "Distribución autorizada, no reventa",
      "texto": (
        "Entregamos el conjunto con <strong>certificado de laboratorio, expediente UL, "
        "número de serie y fecha de fabricación por prenda</strong>, etiqueta permanente con la "
        "composición de las tres capas y ficha técnica en español. Propuesta con partidas y "
        "clave de producto en menos de <strong>24 horas hábiles</strong>, con cobertura en los "
        "<strong>32 estados de la República</strong>."
      ),
    },
  ]),
  ("heroDatos", [
    {"label": "Certificación", "valor": "UL · expediente MH60435"},
    {"label": "Edición declarada", "valor": "NFPA 1971 · 2018"},
    {"label": "Tallas", "valor": "S a 4X"},
  ]),
  ("specStrip", [
    {"label": "Capa exterior", "valor": "PBI MAX 7 oz · 70 % PBI, 30 % Kevlar"},
    {"label": "Barrera de humedad", "valor": "Stedair 3000"},
    {"label": "Barrera térmica", "valor": "Defender M"},
    {"label": "Certificación", "valor": "UL · expediente MH60435"},
    {"label": "Colores", "valor": "Oro y negro"},
    {"label": "Presentaciones", "valor": "Chaquetón, pantalón o completo"},
  ]),

  ("secciones", [
    {
      "id": "el-conjunto",
      "eyebrow": "Qué estás comprando",
      "titulo": "El HERÖ y por qué esta configuración se puede defender por escrito",
      "parrafos": [
        "El <strong>SKÖLD HERÖ</strong> es un conjunto de protección para combate estructural: "
        "chaquetón y pantalón que se cotizan por separado o como traje completo, cada uno con su "
        "propia clave de producto. Sobre ese mismo conjunto el fabricante permite elegir entre "
        "cinco barreras exteriores, y ahí es donde la mayoría de las comparaciones se rompe: dos "
        "propuestas pueden decir “HERÖ” y no ser el mismo traje.",
        "Esta configuración —la de la ficha técnica <strong>FT_HEROPBI_2023(B)</strong>— es la "
        "única del modelo con composición y gramaje publicados capa por capa. Eso permite algo "
        "que en el mercado mexicano de EPP es más raro de lo que debería: escribir un anexo "
        "técnico con números verificables en lugar de una descripción que cualquier proveedor "
        "puede jurar que cumple.",
      ],
      "lista": [
        {
          "t": "Exterior PBI MAX, 7 oz",
          "d": "70 % PBI y 30 % Kevlar. El PBI no se funde ni gotea: carboniza y conserva la forma del tejido bajo llama directa. El Kevlar aporta la resistencia mecánica —desgarre y abrasión— que el PBI solo no da. El gramaje de 7 oz es el que define cuánto pesa el ensamble armado.",
        },
        {
          "t": "Barrera de humedad Stedair 3000",
          "d": "Membrana laminada que impide el paso de agua y de vapor sobrecalentado hacia la piel sin bloquear la salida del sudor. Es la capa que se degrada primero, la que casi nadie inspecciona y la responsable de la mayoría de las quemaduras por escaldadura dentro de un traje certificado.",
        },
        {
          "t": "Barrera térmica Defender M",
          "d": "Define el tiempo real de tolerancia térmica antes de que el elemento sienta el calor. Más barrera es más protección y también más carga térmica acumulada: por eso se especifica junto con las otras dos y no de forma aislada.",
        },
      ],
      "nota": "Las tres capas se certifican como <strong>ensamble</strong>. Sustituir una por otra “equivalente” invalida la certificación del conjunto, aunque la capa nueva esté aprobada por su cuenta.",
    },
    {
      "id": "certificacion",
      "eyebrow": "Certificación",
      "titulo": "Expediente MH60435: certificación de tercera parte, no autodeclaración",
      "parrafos": [
        "La ficha técnica del HERÖ declara <strong>certificación por laboratorio UL bajo NFPA "
        "1971, edición 2018</strong>, y publica el expediente <strong>MH60435</strong> impreso en "
        "todas las páginas del documento. Eso lo vuelve rastreable: el número se puede consultar "
        "en UL Product iQ y confirmar alcance, modelo y edición amparados. Es una diferencia de "
        "fondo frente a un proveedor que solo dice “cumple NFPA”.",
        "Vale la pena separar dos afirmaciones que el fabricante hace por separado y que se "
        "suelen leer como una sola: que <strong>las telas exceden</strong> los requisitos de la "
        "norma, y que <strong>existe certificación UL</strong> bajo esa norma. La primera habla de "
        "materiales; la segunda, del alcance certificado del conjunto. Las dos apuntan a la "
        "edición 2018.",
      ],
      "nota": "La verificación siempre es <strong>por unidad</strong>, no por catálogo: expediente, edición, modelo, configuración de barreras, talla y etiqueta permanente cosida al interior. Un certificado del modelo no acredita la prenda que llegó a tu estación.",
    },
    {
      "id": "edicion-normativa",
      "eyebrow": "Edición vigente",
      "titulo": "NFPA 1971 edición 2018 frente a NFPA 1970 edición 2025",
      "parrafos": [
        "NFPA 1971 fue consolidada en <strong>NFPA 1970 (1971) edición 2025</strong>, junto con "
        "las antiguas 1975, 1981 y 1982, y la transición <strong>cerró el 18 de marzo de "
        "2026</strong>. En consecuencia, ningún organismo puede emitir hoy una certificación "
        "nueva contra la edición 2018.",
        "Eso no invalida el inventario ya etiquetado: su permanencia en servicio se rige por "
        "<strong>NFPA 1850 (1851)</strong> —inspección, cuidado y retiro—, no por la edición de "
        "certificación. Lo que sí obliga es a precisar en la compra qué edición ampara el "
        "certificado que se entrega, y a no aceptar que se presente un traje certificado en 2018 "
        "como si estuviera certificado bajo la edición vigente.",
      ],
      "lista": [
        {"t": "Si compras hoy", "d": "Pide por escrito la edición del certificado que acompaña a las prendas y confirma si el fabricante ya liberó claves de producto referidas a la edición 2025."},
        {"t": "Si ya tienes inventario", "d": "No hay que retirarlo por el cambio de edición. Se rige por NFPA 1850 (1851): inspección documentada y retiro a los 10 años de la fecha de fabricación."},
        {"t": "Si estás en licitación", "d": "Que las bases digan qué edición se exige. Un anexo que solo dice “NFPA” abre la puerta a comparar equipos que no son comparables."},
      ],
    },
    {
      "id": "construccion",
      "eyebrow": "Construcción",
      "titulo": "Dónde puso SKÖLD el material",
      "parrafos": [
        "Un traje se encarece en los lugares donde se rompe. Estos son los elementos que el "
        "fabricante identifica en el HERÖ y que conviene revisar contra la prenda física cuando "
        "llega, porque la presencia de una característica en la familia visual del modelo no "
        "demuestra que venga en la unidad entregada."
      ],
      "lista": [
        {"t": "DRD integrado", "d": "Drag Rescue Device alojado en la espalda del chaquetón para extraer a un elemento inconsciente. Debe inspeccionarse, mantenerse accesible y usarse solo conforme a capacitación y procedimiento."},
        {"t": "Cuello tipo escudo 360°", "d": "Diseño de cobertura total sin partes expuestas alrededor del cuello. Su desempeño real depende del ajuste y de la interfaz con capucha, casco y chaquetón."},
        {"t": "Refuerzos Stedshield y Ultrashield", "d": "En mangas, hombros, codos y rodillas del chaquetón, y Stedshield en los tobillos del pantalón: las zonas de gateo, arrastre y apoyo."},
        {"t": "Arnés de Kevlar integrado", "d": "Incorporado a la prenda, no accesorio externo."},
        {"t": "Costura de Kevlar doble y triple", "d": "Hilo aramídico en todo el conjunto. El hilo común se derrite y abre un puente térmico donde se supone que hay costura."},
        {"t": "Puño de Kevlar con ojillo para pulgar", "d": "Mantiene la manga en posición al levantar el brazo y evita que el guante y el chaquetón dejen de traslaparse."},
        {"t": "Cierre frontal con salida de escape", "d": "Combinación de cremallera y velcro FR con cierre de escape. Define la velocidad de vestido y la hermeticidad del frente."},
      ],
    },
    {
      "id": "visibilidad",
      "eyebrow": "Visibilidad",
      "titulo": "La cinta está especificada por serie, no descrita con adjetivos",
      "parrafos": [
        "La ficha del HERÖ especifica cinta <strong>ORALITE® Ultra Brilliance™ serie "
        "FTP2575-S de 3″</strong> en amarillo verdoso fluorescente, más bies reflejante plata en "
        "pecho, espalda, brazos, bolsas y tobillos. Ese nivel de detalle importa por una razón "
        "práctica: la cinta reflejante es la pieza que más se degrada con el lavado y la que más "
        "se sustituye por una genérica en reparaciones fuera de taller autorizado.",
        "Cuando la ficha nombra la serie, la reposición se puede pedir igual dentro de cinco años. "
        "Cuando solo dice “cinta reflejante de alta visibilidad”, la reposición es lo que haya. "
        "Color, patrón y ubicación final se confirman en la orden.",
      ],
    },
    {
      "id": "bolsas-y-corte",
      "eyebrow": "Ergonomía",
      "titulo": "Bolsas, tirantes y corte: la parte que el elemento sí nota",
      "parrafos": [
        "La protección la define el ensamble; la aceptación en la estación la definen los "
        "detalles. Un traje que protege pero estorba se acaba usando mal, y un traje usado mal "
        "protege menos que uno de menor especificación bien puesto."
      ],
      "lista": [
        {"t": "Chaquetón · porta-radios", "d": "Bolsa tipo fuelle para radio, dos bolsillos inferiores y porta linternas."},
        {"t": "Pantalón · sujeción", "d": "Tirantes acolchados con conexión rápida y ajuste elástico posterior. La conexión rápida es lo que permite vestirse en la unidad en movimiento."},
        {"t": "Pantalón · corte tipo diamante", "d": "Corte en la entrepierna que amplía el rango de movimiento al subir, gatear y montar escalera."},
        {"t": "Pantalón · bolsillos", "d": "Dos bolsillos laterales tipo parche."},
      ],
    },
    {
      "id": "claves",
      "eyebrow": "Cómo se pide",
      "titulo": "Claves de producto y tallas publicadas",
      "parrafos": [
        "El chaquetón y el pantalón se cotizan por separado o como traje completo, y cada "
        "presentación tiene claves distintas. Poner la clave en la requisición es lo que evita "
        "que llegue una configuración distinta a la que se aprobó."
      ],
      "tabla": {
        "head": ["Presentación", "Claves", "Tallas"],
        "rows": [
          ["Chaquetón HERÖ 2018 PBI oro", "CHB910-S · -M · -L · -XL · -2X · -3X · -4X", "Siete tallas, de S a 4X"],
          ["Pantalón HERÖ 2018 oro", "PB910-S · -M · -L · -XL · -2X · -3X · -4X", "Siete tallas, de S a 4X"],
          ["Traje completo HERÖ 2018 PBI MAX", "TB910-M · -L · -XL · TB-910-2XL · -3XL · -4XL", "Seis tallas, de M a 4XL"],
          ["Combos de traje con bota", "FP-COM9/910 en L-BB08 · XL-BB09 · XL-B9.5 · XL-BB10 · L-BB11", "Asocian talla de traje con número de bota"],
        ],
      },
      "nota": "Las claves incluyen “2018” porque identifican <strong>la edición normativa bajo la que se certificó la configuración</strong>. Al cotizar conviene confirmar si el fabricante ya liberó claves referidas a NFPA 1970 (1971) edición 2025.",
    },
    {
      "id": "medidas",
      "eyebrow": "Tallaje",
      "titulo": "La tabla de medidas UL y por qué no sustituye medir al elemento",
      "parrafos": [
        "La ficha publica la tabla de medidas UL del exterior para las tallas S a 3XL. Son "
        "medidas de la <strong>prenda extendida</strong>, no del cuerpo del usuario: sirven para "
        "verificar que llegó lo que se pidió, no para asignar tallas."
      ],
      "tabla": {
        "head": ["Prenda", "Medida", "Rango publicado", "Tolerancia"],
        "rows": [
          ["Chaquetón", "Contorno de pecho", "47″ a 58″", "±½″"],
          ["Chaquetón", "Contorno de faldón", "47″ a 57″", "±½″"],
          ["Chaquetón", "Contorno de cuello", "Según talla", "±¼″"],
          ["Pantalón", "Contorno de cintura", "41″ a 51″", "±½″"],
          ["Pantalón", "Largo de entrepierna", "28″ a 32″ (sin diamante)", "±½″"],
        ],
      },
      "nota": "El tallaje se define midiendo a cada bombero <strong>con las capas que llevará en operación</strong> y verificando alcance, movilidad e interfaz con casco, capucha, guantes, botas y equipo de respiración. Enviamos juego de tallas de muestra antes de cerrar un pedido de brigada.",
    },
    {
      "id": "cbrn",
      "eyebrow": "Lo que el fabricante no publica",
      "titulo": "La declaración CBRN: qué dice y qué no",
      "parrafos": [
        "SKÖLD indica que el HERÖ cuenta con barreras interiores resistentes a agentes "
        "<strong>químicos, bacteriológicos, radiológicos y nucleares</strong>. Es una afirmación "
        "del fabricante, y la ficha <strong>no publica el ensayo, la norma ni el alcance</strong> "
        "de esa resistencia.",
        "Nuestra postura es decirlo así: si tu operación necesita capacidad CBRN acreditada, hay "
        "que pedir evidencia específica antes de asumirla, y probablemente hablar de un ensamble "
        "distinto. Repetir la frase del catálogo como si fuera una certificación es la clase de "
        "atajo que se cobra en una auditoría, no en la venta.",
      ],
      "nota": "Mismo criterio aplica a las otras cuatro barreras exteriores del HERÖ: están listadas por el fabricante, pero sin composición ni gramaje publicados. No las comparamos contra PBI MAX hasta tener su ficha.",
    },
    {
      "id": "cuidado",
      "eyebrow": "Ciclo de vida",
      "titulo": "Cuidado bajo NFPA 1850 (1851) y retiro a los diez años",
      "parrafos": [
        "Antes y después de cada uso hay que revisar contaminación, daño térmico, abrasión, "
        "cortes, costuras, cierres, cintas, refuerzos, DRD, barreras y etiquetado conforme a las "
        "instrucciones del fabricante. Además de la revisión rutinaria del propio elemento, la "
        "norma pide <strong>inspección avanzada documentada al menos una vez al año</strong> y "
        "lavado especializado. Lavadora doméstica, cloro y suavizante destruyen la barrera de "
        "humedad sin dejar señal visible.",
        "El retiro es obligatorio a los <strong>10 años de la fecha de fabricación</strong>, no de "
        "la compra. Entregamos con número de serie y fecha por prenda en bitácora para que la "
        "reposición se escalone por año y no llegue toda junta al mismo ejercicio "
        "presupuestal.",
      ],
      "nota": "La reparación la hace el fabricante o un taller verificado por él, con material e hilo del mismo tipo certificado. Un parche cosido con hilo común anula la certificación del ensamble.",
    },
  ]),

  ("galeria", [
    {"src": "/images/catalogo/1776648120640-1000x750.webp",
     "alt": "Trajes estructurales y cascos colgados en el vestidor de la estación",
     "caption": "Ensamble completo por turno"},
    {"src": "/images/catalogo/1669209285616-600x450.webp",
     "alt": "Chaquetones estructurales en rack de estación",
     "caption": "Chaquetón y pantalón por clave"},
    {"src": "/images/catalogo/1662121396496-600x400.webp",
     "alt": "Chaquetones estructurales colgados en el vestidor de la estación",
     "caption": "Control de tallas"},
    {"src": "/images/catalogo/1584033376442-600x450.webp",
     "alt": "Bombero equipado con herramienta de intervención durante una maniobra",
     "caption": "Desempeño en maniobra"},
  ]),

  ("aplicaciones", [
    {"sector": "Cuerpos de bomberos",
     "desc": "Dotación por elemento con clave de producto, talla verificada contra la tabla UL y bitácora por número de serie. La configuración documentada facilita la comprobación ante protección civil."},
    {"sector": "Brigadas industriales",
     "desc": "Para brigadas cuya matriz de riesgo y nivel de entrenamiento incluyan intervención estructural. El conjunto no sustituye equipo de respiración, evaluación atmosférica, comunicaciones ni respaldo."},
    {"sector": "Licitación pública",
     "desc": "Anexo técnico redactado con números publicados —gramaje, composición, barreras, expediente UL— en lugar de descripciones que cualquier proveedor puede declarar que cumple."},
  ]),

  ("datoClave", {
    "titulo": "Pide el expediente por escrito",
    "texto": "<strong>UL MH60435</strong> se puede rastrear en UL Product iQ. Un proveedor que no te entrega el número de expediente no está vendiendo certificación: está vendiendo una afirmación."
  }),

  ("referencias", [
    {"code": "UL · MH60435", "desc": "Expediente de certificación publicado por SKÖLD en la ficha del HERÖ. Permite confirmar alcance, modelo y edición amparados. Pídelo por escrito en la propuesta."},
    {"code": "NFPA 1971 · 2018", "desc": "Edición bajo la que está declarada la certificación UL de esta configuración. Fue sustituida."},
    {"code": "NFPA 1970 · 2025", "desc": "Estándar vigente que consolidó NFPA 1971, 1975, 1981 y 1982. La transición cerró el 18 de marzo de 2026."},
    {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento del conjunto en servicio. Es la norma que rige la permanencia del inventario, no la edición de certificación."},
    {"code": "NOM-017-STPS", "desc": "Selección, entrega y capacitación en el uso del equipo de protección personal según el riesgo del puesto."},
  ]),

  ("blog", [
    "guia-trajes-estructurales-nfpa-1971",
    "marcas-trajes-bomberos-comparativa-mexico",
    "mantenimiento-epp-estructural-nfpa-1851",
    "equipar-brigada-trajes-bomberos-tallaje-licitacion",
    "nfpa-1971-mexico-norma-bomberos",
    "precio-trajes-bomberos-mexico-2026",
  ]),

  ("faqs", [
    {"q": "¿Qué diferencia real hay entre PBI MAX 7.0 y las otras cuatro barreras del HERÖ?",
     "a": "La diferencia verificable es de información, no necesariamente de desempeño. PBI MAX 7.0 es la única configuración cuya ficha publica composición y gramaje: 70 % PBI, 30 % Kevlar, 7 oz, con Stedair 3000 y Defender M. Advance, Kombat Flex, Pioneer y Defender 750 están listadas por el fabricante como barreras seleccionables, pero sin esos datos no se puede comparar peso ni carga térmica. Antes de ponerlas en la misma tabla pedimos la ficha de cada configuración; comparar contra un dato que no existe es inventarlo."},
    {"q": "¿Por qué 70 % PBI y 30 % Kevlar y no 100 % PBI?",
     "a": "Porque cada fibra resuelve un problema distinto. El PBI aguanta la llama sin fundirse ni gotear —carboniza y conserva la forma del tejido—, pero por sí solo no da la resistencia mecánica que necesita una capa exterior sometida a desgarre, abrasión y arrastre. El Kevlar aporta esa tenacidad. La mezcla es la que permite que el traje siga siendo una barrera después de engancharse con una lámina, no solo después de una exposición térmica."},
    {"q": "¿El expediente MH60435 se puede verificar y cómo?",
     "a": "Sí. Es un número de expediente de UL, y por eso es una certificación de tercera parte y no una declaración de conformidad del propio fabricante. Se consulta en UL Product iQ contra el número de expediente y ahí se confirma alcance, modelo y edición amparados. Te entregamos el número en la propuesta y el certificado con el envío; si un proveedor no te da el expediente, no tienes con qué verificar nada."},
    {"q": "¿Sirve un traje certificado bajo NFPA 1971 edición 2018 si la vigente es NFPA 1970 edición 2025?",
     "a": "Para uso en servicio, sí: la permanencia del equipo se rige por NFPA 1850 (1851) —inspección, cuidado y retiro a los diez años de fabricación—, no por la edición de certificación. Lo que ya no ocurre es que se emitan certificaciones nuevas contra la edición 2018, porque la transición cerró el 18 de marzo de 2026. Para una compra hoy hay que precisar por escrito qué edición ampara el certificado que se entrega y no aceptar que se presente un certificado 2018 como si fuera de la edición vigente."},
    {"q": "¿Qué es el DRD y por qué importa que venga integrado?",
     "a": "El DRD —Drag Rescue Device— es un arnés de arrastre alojado en la espalda del chaquetón que permite extraer a un elemento inconsciente jalando de un punto diseñado para eso, en lugar de improvisar con la prenda. Que venga integrado significa que no depende de un accesorio que alguien recuerde colocar. A cambio, exige inspección: si el DRD está mal replegado o inaccesible, existe en el catálogo y no en la emergencia."},
    {"q": "¿Puedo comprar solo el chaquetón o solo el pantalón?",
     "a": "Sí. El chaquetón, el pantalón y el traje completo tienen claves de producto distintas —CHB910, PB910 y TB910— y se cotizan por separado. Es lo habitual cuando se repone por desgaste diferenciado: el pantalón suele salir antes por rodillas y tobillos. Solo hay que cuidar que la prenda nueva sea de la misma configuración de barreras que la que sigue en servicio, para no quedarse con un ensamble mezclado."},
    {"q": "¿El HERÖ protege contra agentes CBRN?",
     "a": "El fabricante indica que cuenta con barreras interiores resistentes a agentes químicos, bacteriológicos, radiológicos y nucleares, pero la ficha no publica el ensayo, la norma ni el alcance de esa resistencia. Preferimos decirlo con claridad: es una declaración, no una certificación acreditada. Si tu operación requiere capacidad CBRN comprobable, hay que pedir evidencia específica al fabricante y muy probablemente evaluar un ensamble diseñado para ese escenario."},
    {"q": "¿Qué datos necesitan para cotizar y de qué depende el tiempo de entrega?",
     "a": "Necesitamos número de usuarios y funciones, presentación por partida —chaquetón, pantalón o completo—, tallas o disposición para recibir juego de muestra, color, edición normativa y certificado que exige tu compra, accesorios, y fecha objetivo. El plazo depende de si las claves salen de inventario o entran a programa de producción del fabricante: tallas medias en configuración estándar suelen salir en días, y bordado institucional o tallas extremas entran a fabricación. Te damos fecha comprometida por partida y te decimos de qué depende, en lugar de un plazo único que después no se cumple."},
  ]),
])


with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')
catalogo = prod['l3']['catalogo']
card = next(c for c in catalogo['cards'] if c['variante'] == 'PBI MAX 7.0')

card['slug'] = 'skold-hero-pbi-max-7-0'
card['l4'] = L4

# Reordena la card para que slug quede junto a variante
orden = ['marca', 'modelo', 'variante', 'varianteLabel', 'slug', 'badge', 'estado',
         'img', 'alt', 'desc', 'specs', 'chip', 'l4']
nuevo = collections.OrderedDict((k, card[k]) for k in orden if k in card)
for k, v in card.items():
    if k not in nuevo:
        nuevo[k] = v
card.clear(); card.update(nuevo)

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

faltan = [g['src'] for g in L4['galeria'] if not os.path.exists('public' + g['src'])]
faltan += [] if os.path.exists('public' + L4['heroImg']['src']) else [L4['heroImg']['src']]
print('slug:', card['slug'])
print('secciones:', len(L4['secciones']), '| faqs:', len(L4['faqs']), '| referencias:', len(L4['referencias']))
print('seoTitle:', len(L4['seoTitle']) + len(' | Firefighter.com.mx'), 'ch')
print('seoDescription:', len(L4['seoDescription']), 'ch')
print('imagenes faltantes:', faltan or 'ninguna')
palabras = 0
for s in L4['secciones']:
    for p in s.get('parrafos', []): palabras += len(re.sub(r'<[^>]+>', '', p).split())
    for it in s.get('lista', []): palabras += len(re.sub(r'<[^>]+>', '', it['d']).split())
    if s.get('nota'): palabras += len(re.sub(r'<[^>]+>', '', s['nota']).split())
for f_ in L4['faqs']: palabras += len(f_['a'].split())
print('palabras de contenido aprox:', palabras)
