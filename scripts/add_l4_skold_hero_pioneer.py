# -*- coding: utf-8 -*-
"""L4 — SKOLD HERO · barrera exterior Pioneer.

Patron "ficha sin ficha". Angulo propio: EL CERTIFICADO SE EMITE SOBRE EL ENSAMBLE,
NO SOBRE LA CAPA. Aporta como leer un certificado y como rastrearlo, que es el contenido
mas util de las cinco fichas para un comprador de gobierno.
"""
import json, io, collections, os, re

RUTA = 'src/data/productos.json'
SLUG = 'skold-hero-pioneer'
VARIANTE = 'Pioneer'

L4 = collections.OrderedDict([
  ("seoTitle", "Traje SKÖLD HERÖ con barrera Pioneer"),
  ("seoDescription",
    "Barrera exterior Pioneer del SKÖLD HERÖ: por qué el certificado se emite sobre el ensamble "
    "y no sobre la capa, cómo leerlo y qué exigir antes de comprar."),
  ("badge", "Alcance por confirmar"),
  ("h1", "Traje estructural SKÖLD HERÖ con barrera exterior Pioneer"),
  ("subtitulo",
    "Pioneer es una de las cinco barreras exteriores seleccionables del conjunto HERÖ. El "
    "fabricante no publica su composición ni su gramaje, y hay algo más importante que eso: "
    "cambiar la capa exterior cambia el ensamble certificado, así que el alcance del certificado "
    "se confirma por configuración y no por modelo."),

  ("heroImg", {
    "src": "/images/catalogo/1651368615152-600x450.webp",
    "alt": "Rack de equipo de protección personal estructural listo en una estación de bomberos",
  }),
  ("heroBloques", [
    {
      "label": "El error de compra más caro no es el precio",
      "texto": (
        "Es aceptar un certificado que no ampara lo que te entregaron. NFPA no certifica telas: "
        "certifica <strong>el ensamble armado</strong> —capa exterior, barrera de humedad y "
        "barrera térmica trabajando juntas—. Sustituir una capa por otra “equivalente” produce un "
        "ensamble distinto que necesita su propio alcance certificado, aunque el modelo y el "
        "número de expediente sean los mismos."
      ),
    },
    {
      "label": "Pedimos el alcance por escrito, siempre",
      "texto": (
        "Como distribuidores autorizados solicitamos al fabricante que declare si el expediente "
        "<strong>UL MH60435</strong> cubre la configuración con Pioneer y bajo qué edición "
        "normativa, además de composición, gramaje y barreras interiores. Con eso tu expediente "
        "de compra aguanta una auditoría de protección civil o una verificación STPS. Cobertura "
        "en los <strong>32 estados de la República</strong>."
      ),
    },
  ]),
  ("heroDatos", [
    {"label": "Estado del dato", "valor": "Ficha por solicitar"},
    {"label": "Certificación del modelo", "valor": "UL · expediente MH60435"},
    {"label": "Alcance del ensamble", "valor": "Por confirmar"},
  ]),
  ("specStrip", [
    {"label": "Capa exterior", "valor": "Pioneer · sin gramaje publicado"},
    {"label": "Barrera de humedad", "valor": "Por confirmar en la ficha"},
    {"label": "Barrera térmica", "valor": "Por confirmar en la ficha"},
    {"label": "Ensamble certificado", "valor": "Se confirma por configuración"},
    {"label": "Conjunto", "valor": "HERÖ · DRD, cuello 360°, Kevlar"},
    {"label": "Expediente", "valor": "UL MH60435 · rastreable"},
  ]),

  ("secciones", [
    {
      "id": "que-es",
      "eyebrow": "Qué estás evaluando",
      "titulo": "Pioneer es una capa exterior del HERÖ, y eso tiene consecuencias documentales",
      "parrafos": [
        "El <strong>SKÖLD HERÖ</strong> admite cinco barreras exteriores: Advance, Kombat Flex, "
        "PBI MAX 7.0, Pioneer y Defender 750. El conjunto no cambia —DRD en la espalda, cuello de "
        "cobertura 360°, arnés de Kevlar, refuerzos y claves de producto siguen siendo los del "
        "modelo—, pero sí cambia la combinación de tres capas que se certifica.",
        "Esa distinción es la que hace que esta ficha exista. No es un detalle burocrático: es la "
        "diferencia entre entregar un expediente que resiste una auditoría y entregar un "
        "expediente que se cae en la primera pregunta. Y aplica igual a cualquier marca, no solo "
        "a SKÖLD.",
      ],
      "nota": "En la partida tiene que aparecer <strong>la configuración de barreras completa</strong>, no solo el modelo. “SKÖLD HERÖ” describe una familia, no un ensamble certificado.",
    },
    {
      "id": "como-funciona",
      "eyebrow": "Autoridad técnica",
      "titulo": "Cómo funciona una certificación de ensamble",
      "parrafos": [
        "Los requisitos de desempeño térmico de un traje estructural no se pueden verificar capa "
        "por capa, porque el desempeño lo produce la interacción entre ellas. El aire atrapado "
        "entre capas, la conducción a través de las costuras y la forma en que la barrera de "
        "humedad frena el vapor solo existen en el conjunto armado.",
        "Por eso los dos números que la norma exige —<strong>TPP</strong>, que mide la protección "
        "térmica, y <strong>THL</strong>, que mide cuánto calor metabólico evacua el traje— se "
        "ensayan sobre el <strong>composite</strong>: la muestra de las tres capas en el orden y "
        "con los materiales de la configuración real. Cambia una capa y el composite es otro.",
      ],
      "lista": [
        {"t": "Certificado de tela ≠ certificado de traje", "d": "Un fabricante de tejidos puede acreditar que su tela cumple ciertos requisitos. Eso no acredita el ensamble, y una propuesta que presenta el certificado de la tela como certificado del traje está cambiando una cosa por otra."},
        {"t": "El expediente es del modelo; el alcance, de la configuración", "d": "Un mismo número de expediente puede amparar varias configuraciones, algunas o solo una. La existencia del expediente no dice cuáles. Eso se pregunta."},
        {"t": "Sustituir una capa invalida el conjunto certificado", "d": "Aunque la capa nueva esté aprobada por su cuenta. Aplica en compra y también en reparación: un parche con material distinto rompe el ensamble."},
        {"t": "La etiqueta permanente es la prueba por unidad", "d": "Cosida al interior, con fabricante, modelo, fecha, número de serie, composición de las tres capas y marca del organismo certificador. Sin etiqueta no hay certificación, por buena que sea la propuesta."},
      ],
      "nota": "Este criterio no es opinión nuestra: es la razón por la que NFPA especifica ensayos sobre el composite y no sobre materiales aislados. Sirve para evaluar a cualquier proveedor, incluidos nosotros.",
    },
    {
      "id": "leer-certificado",
      "eyebrow": "Cómo se verifica",
      "titulo": "Cómo leer un certificado y rastrearlo",
      "parrafos": [
        "Un certificado útil se puede verificar sin depender de quien te lo entrega. Estos son los "
        "campos que hay que buscar y en ese orden; si falta uno, ese es el que hay que pedir.",
      ],
      "lista": [
        {"t": "1 · Organismo certificador", "d": "Quién emitió el documento. Si el emisor es el propio fabricante, es una declaración de conformidad, no una certificación de tercera parte. Son cosas distintas y ambas tienen su lugar, pero no se sustituyen."},
        {"t": "2 · Número de expediente", "d": "En el HERÖ, UL MH60435. Es lo que permite rastrear el registro en UL Product iQ y confirmar alcance, modelo y edición amparados sin intermediarios."},
        {"t": "3 · Edición normativa citada", "d": "Debe decir norma y año. “Cumple NFPA” sin edición no es verificable, y una edición sustituida cambia lo que significa el documento."},
        {"t": "4 · Modelo y configuración amparados", "d": "Aquí es donde se confirma si tu combinación de barreras está incluida. Es el campo que más se omite y el que más importa en esta ficha."},
        {"t": "5 · Vigencia y trazabilidad a la unidad", "d": "Que lo declarado en el certificado coincida con la etiqueta permanente de la prenda que recibiste, incluyendo número de serie y fecha de fabricación."},
      ],
      "nota": "Guarda el certificado <strong>junto con la lista de números de serie recibidos</strong>. En una auditoría lo que se revisa es la correspondencia entre documento y prenda, no la existencia del documento.",
    },
    {
      "id": "lo-documentado",
      "eyebrow": "Lo que sí está documentado",
      "titulo": "El conjunto: esto no depende de la barrera exterior",
      "parrafos": [
        "Estos elementos los publica SKÖLD a nivel de modelo, así que aplican también con Pioneer. "
        "Son los que puedes especificar y verificar contra la prenda física cuando llegue.",
      ],
      "lista": [
        {"t": "DRD integrado", "d": "Drag Rescue Device alojado en la espalda del chaquetón, para extraer a un elemento inconsciente desde un punto diseñado para eso."},
        {"t": "Cuello tipo escudo 360°", "d": "Cobertura total alrededor del cuello sin partes expuestas."},
        {"t": "Arnés de Kevlar integrado", "d": "Incorporado a la prenda, no accesorio externo."},
        {"t": "Refuerzos Stedshield y Ultrashield", "d": "En mangas, hombros, codos y rodillas del chaquetón, y Stedshield en los tobillos del pantalón."},
        {"t": "Costura de Kevlar doble y triple", "d": "Hilo aramídico en todo el conjunto, con puño de Kevlar y ojillo para pulgar."},
        {"t": "Cinta ORALITE® FTP2575-S de 3″", "d": "Ultra Brilliance™ en amarillo verdoso fluorescente, más bies reflejante plata. Especificada por serie, lo que permite pedir la reposición igual años después."},
        {"t": "Claves y tallas", "d": "Chaquetón CHB910, pantalón PB910 y traje completo TB910, en tallas de S a 4X. La tabla de medidas UL del exterior se publica para S a 3XL."},
      ],
    },
    {
      "id": "lo-no-publicado",
      "eyebrow": "Lo que falta",
      "titulo": "Sin las tres capas no se sabe qué composite se certificó",
      "parrafos": [
        "Los datos ausentes de esta configuración no son solo un problema de comparación: son "
        "exactamente los que definen el ensamble que un certificado tendría que amparar.",
      ],
      "tabla": {
        "head": ["Dato ausente", "Qué decide", "Consecuencia de no tenerlo"],
        "rows": [
          ["Composición de la capa exterior", "Comportamiento ante llama y abrasión", "No se identifica el material que forma parte del composite certificado"],
          ["Gramaje en oz/yd²", "Peso del ensamble y carga térmica", "No hay forma de comparar fatiga del elemento contra PBI MAX 7.0"],
          ["Barrera de humedad", "Paso de vapor sobrecalentado", "Es una de las tres capas del composite: sin ella el ensamble no está definido"],
          ["Barrera térmica", "Tiempo real de tolerancia térmica", "Cierra el composite; sin las tres capas no hay TPP del conjunto"],
          ["TPP y THL del ensamble", "Los dos valores que exige la norma", "Sin ellos no hay base técnica para aceptar ni rechazar la propuesta"],
          ["Alcance del certificado", "Si el expediente ampara esta combinación", "El expediente puede existir y no cubrir la configuración entregada"],
        ],
      },
      "nota": "Un traje puede ser excelente y no tener ficha pública: la ausencia del dato no es un defecto del producto, es un vacío de información. Lo que no se puede hacer es <strong>rellenarlo con supuestos</strong> y presentarlo como especificación en una requisición.",
    },
    {
      "id": "reparacion",
      "eyebrow": "Después de la compra",
      "titulo": "El ensamble también se rompe en el taller",
      "parrafos": [
        "El criterio de “certificación sobre el ensamble” no termina en la entrega. Cada "
        "reparación es una intervención sobre el conjunto certificado, y ahí es donde muchos "
        "cuerpos pierden sin saberlo la condición que pagaron.",
        "<strong>NFPA 1850 (1851)</strong> exige que la reparación la haga el fabricante o un "
        "taller verificado por él, con material e hilo del mismo tipo certificado. Un parche "
        "cosido con hilo común abre un puente térmico donde se supone que hay costura, y una cinta "
        "reflejante genérica sustituyendo la serie especificada cambia el conjunto que se evaluó.",
      ],
      "lista": [
        {"t": "Reparación con material equivalente", "d": "“Equivalente” no es una categoría certificada. El material tiene que ser el mismo tipo aprobado para ese ensamble."},
        {"t": "Cambio de barrera de humedad", "d": "Casi siempre significa reemplazo de la prenda, no reparación. Es la capa que más se degrada y la que menos se inspecciona."},
        {"t": "Lavado no especializado", "d": "Lavadora doméstica, cloro y suavizante destruyen la barrera de humedad sin dejar señal visible. El traje sigue viéndose bien y ya no protege igual."},
        {"t": "Retiro obligatorio", "d": "A los 10 años de la fecha de fabricación, no de la compra. Pide la fecha por número de serie antes de firmar."},
      ],
    },
    {
      "id": "anexo",
      "eyebrow": "Licitación",
      "titulo": "Cómo exigir alcance certificado en una partida",
      "parrafos": [
        "Estas redacciones cierran la puerta a que te entreguen un certificado que no ampara lo "
        "que compraste, y son evaluables sin discutir de telas.",
      ],
      "tabla": {
        "head": ["En la partida escribe", "En lugar de"],
        "rows": [
          ["Certificado de tercera parte con número de expediente, organismo emisor y edición normativa vigente", "“Cumple NFPA”"],
          ["Declaración del fabricante de que el expediente ampara la configuración de barreras cotizada", "“Modelo certificado”"],
          ["Composición de las tres capas declarada en ficha técnica y coincidente con la etiqueta permanente", "“Barrera exterior de aramida”"],
          ["TPP y THL del ensamble armado, declarados por el fabricante", "sin mención"],
          ["Listado de números de serie y fechas de fabricación por prenda entregada", "sin mención"],
          ["Carta de taller autorizado para reparación con material del mismo tipo certificado", "sin mención"],
        ],
      },
      "nota": "Con esas seis líneas la evaluación se vuelve <strong>documental y objetiva</strong>: quien no pueda entregarlas queda fuera por incumplimiento, no por una discusión de criterios.",
    },
    {
      "id": "cuando-conviene",
      "eyebrow": "Criterio de selección",
      "titulo": "Cuándo tiene sentido evaluar Pioneer",
      "parrafos": [
        "No descartamos una barrera por no tener ficha pública, y tampoco la recomendamos a "
        "ciegas. Estos son los escenarios donde vale la pena pedir la ficha y el alcance, y el "
        "escenario donde conviene ir directo a la configuración documentada.",
      ],
      "lista": [
        {"t": "Tiene sentido evaluarla", "d": "Cuando el fabricante puede declarar por escrito el alcance del certificado para esta configuración dentro del plazo de tu proceso."},
        {"t": "Tiene sentido evaluarla", "d": "Cuando ya operas HERÖ y quieres ampliar la flota manteniendo modelo, claves, taller de reparación y programa de cuidado."},
        {"t": "Tiene sentido evaluarla", "d": "Cuando buscas alternativas de costo o disponibilidad y tienes margen para verificar documentación antes de comprometer presupuesto."},
        {"t": "Conviene ir a PBI MAX 7.0", "d": "Cuando la compra es por licitación con anexo técnico cerrado o cuando el expediente va a auditoría. Ahí la configuración con ficha y alcance publicados evita la impugnación."},
      ],
    },
    {
      "id": "siguiente-paso",
      "eyebrow": "Qué hacemos nosotros",
      "titulo": "De un expediente de modelo a un alcance por configuración",
      "parrafos": [
        "Solicitamos al fabricante la ficha de la configuración y, sobre todo, la declaración de "
        "alcance: si el expediente UL MH60435 cubre la combinación con Pioneer y bajo qué edición. "
        "Con esa respuesta te armamos la propuesta con partidas, claves de producto y tallas "
        "verificadas contra la tabla de medidas.",
        "Si el alcance no se confirma, te lo decimos y comparamos contra PBI MAX 7.0 con lo que sí "
        "está publicado. No vamos a presentarte un certificado de modelo como si fuera un "
        "certificado de tu configuración: ese atajo lo paga el comprador en la auditoría, no el "
        "proveedor en la venta.",
      ],
      "nota": "Cada envío sale con certificado del ensamble, número de serie y fecha de fabricación por prenda, etiqueta permanente con la composición de las tres capas, procedimiento de lavado y retiro en español, carta de distribuidor autorizado y factura desglosada por partida y talla.",
    },
  ]),

  ("galeria", [
    {"src": "/images/catalogo/1563062067-77-600x450.webp",
     "alt": "Bombero con traje estructural completo frente a un incendio",
     "caption": "El ensamble en servicio"},
    {"src": "/images/catalogo/1592235905030-600x450.webp",
     "alt": "Bombero con máscara facial y capucha bajo el casco estructural",
     "caption": "Interfaz entre elementos del conjunto"},
    {"src": "/images/catalogo/1735107673023-600x400.webp",
     "alt": "Bombero con capucha aramídica y protector bajo el casco",
     "caption": "Continuidad de la protección"},
    {"src": "/images/catalogo/1575507371202-600x450.webp",
     "alt": "Cascos amarillos con visera abatible en primer plano",
     "caption": "Verificación por unidad"},
  ]),

  ("aplicaciones", [
    {"sector": "Licitación pública",
     "desc": "Aquí es donde el alcance del certificado decide el proceso. Exige declaración del fabricante de que el expediente ampara la configuración cotizada, y listado de números de serie contra el certificado entregado."},
    {"sector": "Cuerpos de bomberos",
     "desc": "Para ampliar una flota que ya opera HERÖ manteniendo modelo, claves y taller de reparación autorizado. El expediente de compra debe resistir una auditoría de protección civil."},
    {"sector": "Brigadas industriales",
     "desc": "Dotación conforme a NOM-002-STPS con expediente documental completo para auditoría interna y de cliente. La configuración de barreras se declara, no se asume."},
  ]),

  ("datoClave", {
    "titulo": "Un expediente no es un alcance",
    "texto": "<strong>UL MH60435</strong> es el expediente del modelo HERÖ. Que exista no acredita que cubra la combinación con Pioneer: la certificación se emite sobre el ensamble de tres capas. Pide la <strong>declaración de alcance por configuración</strong> por escrito."
  }),

  ("referencias", [
    {"code": "UL · MH60435", "desc": "Expediente de certificación del HERÖ publicado por SKÖLD. Rastreable en UL Product iQ: ahí se confirma alcance, modelo y edición amparados."},
    {"code": "NFPA 1971 · 2018", "desc": "Edición bajo la que está declarada la certificación UL del modelo. Establecía requisitos de diseño, desempeño, ensayo y certificación de conjuntos estructurales. Fue sustituida."},
    {"code": "NFPA 1970 · 2025", "desc": "Estándar vigente que consolidó NFPA 1971, 1975, 1981 y 1982. La transición cerró el 18 de marzo de 2026, así que un certificado emitido hoy debe citar esta edición."},
    {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento. Es la norma que rige la permanencia del inventario en servicio y las condiciones de reparación."},
    {"code": "NOM-017-STPS", "desc": "Selección, entrega y capacitación en el uso del equipo de protección personal según el riesgo del puesto."},
  ]),

  ("blog", [
    "nfpa-1971-mexico-norma-bomberos",
    "guia-trajes-estructurales-nfpa-1971",
    "licitaciones-equipos-contra-incendios-mexico",
    "mantenimiento-epp-estructural-nfpa-1851",
    "marcas-trajes-bomberos-comparativa-mexico",
    "equipar-brigada-trajes-bomberos-tallaje-licitacion",
  ]),

  ("faqs", [
    {"q": "¿Por qué el certificado no se emite sobre la tela?",
     "a": "Porque el desempeño térmico de un traje lo produce la interacción entre las tres capas, no cada una por separado. El aire atrapado entre capas, la conducción a través de las costuras y la forma en que la barrera de humedad frena el vapor solo existen en el conjunto armado. Por eso los dos valores que exige la norma —TPP y THL— se ensayan sobre el composite: la muestra de las tres capas en el orden y con los materiales de la configuración real. Cambia una capa y el composite es otro."},
    {"q": "¿El expediente UL MH60435 cubre la configuración Pioneer?",
     "a": "Es exactamente lo que hay que confirmar por escrito, y es la razón de ser de esta ficha. El expediente es del modelo HERÖ y la configuración documentada en la ficha que conocemos es la de PBI MAX 7.0. Un mismo número de expediente puede amparar varias configuraciones, algunas o solo una, y su existencia no dice cuáles. Pedimos al fabricante que declare el alcance y la edición normativa aplicables a la configuración cotizada."},
    {"q": "¿Qué campos debe traer un certificado para que sirva?",
     "a": "Cinco: organismo certificador emisor —si lo emite el propio fabricante es una declaración de conformidad, no una certificación de tercera parte—, número de expediente rastreable, edición normativa con año, modelo y configuración amparados, y correspondencia con la etiqueta permanente de la prenda recibida, incluyendo número de serie y fecha de fabricación. Si falta uno, ese es el que hay que pedir."},
    {"q": "¿Puedo verificar la certificación por mi cuenta?",
     "a": "Sí, y conviene hacerlo. El número de expediente UL se consulta en UL Product iQ y ahí se confirma alcance, modelo y edición amparados sin depender de quien te entregó el documento. Esa posibilidad de verificación independiente es precisamente lo que distingue a una certificación de tercera parte de una declaración del fabricante. Te entregamos el número en la propuesta."},
    {"q": "Si repongo una prenda con otra barrera, ¿pasa algo?",
     "a": "Te queda una flota con ensambles mezclados y expedientes distintos, lo que complica la comprobación documental y la comparación de estado en la inspección anual. No es un problema de seguridad inmediato si cada prenda está certificada por su cuenta, pero sí de administración: cada configuración tiene su alcance y su ficha. Conviene reponer manteniendo la configuración que ya está en servicio."},
    {"q": "¿Qué pasa si el traje se repara con material distinto?",
     "a": "Se pierde la condición del ensamble certificado. NFPA 1850 (1851) exige que la reparación la haga el fabricante o un taller verificado por él, con material e hilo del mismo tipo certificado. Un parche cosido con hilo común abre un puente térmico donde se supone que hay costura, y una cinta reflejante genérica sustituyendo la serie especificada cambia el conjunto que se evaluó. Pide carta de taller autorizado como parte de la compra."},
    {"q": "¿Entonces Pioneer es peor que PBI MAX 7.0?",
     "a": "No hay base para afirmarlo, ni tampoco lo contrario. La diferencia verificable hoy es documental: de las cinco barreras del HERÖ solo PBI MAX publica composición, gramaje y la combinación de barreras interiores de su configuración. Una barrera puede ser excelente y no tener ficha pública. Lo que no se puede es compararlas técnicamente ni sostener su alcance certificado mientras falten esos datos."},
    {"q": "¿Cuánto tardan en conseguir la declaración de alcance y en cotizar?",
     "a": "La cotización sale en menos de 24 horas hábiles con lo que está publicado y con el estado de cada dato pendiente marcado como tal. El tiempo de respuesta del fabricante para la ficha y la declaración de alcance no lo controlamos y no vamos a prometerte un plazo: te decimos cuándo lo solicitamos y te avisamos en cuanto llega o si no llega. Si tu proceso no admite esperar, evaluamos PBI MAX 7.0."},
  ]),
])


with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')
card = next(c for c in prod['l3']['catalogo']['cards'] if c['variante'] == VARIANTE)

card['slug'] = SLUG
card['l4'] = L4

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

srcs = [L4['heroImg']['src']] + [g['src'] for g in L4['galeria']]
faltan = [s for s in srcs if not os.path.exists('public' + s)]
palabras = 0
for s in L4['secciones']:
    for p in s.get('parrafos', []): palabras += len(re.sub(r'<[^>]+>', '', p).split())
    for it in s.get('lista', []): palabras += len(re.sub(r'<[^>]+>', '', it['d']).split())
    for r in s.get('tabla', {}).get('rows', []): palabras += sum(len(c.split()) for c in r)
    if s.get('nota'): palabras += len(re.sub(r'<[^>]+>', '', s['nota']).split())
for f_ in L4['faqs']: palabras += len(f_['a'].split())

print(SLUG, '| secciones:', len(L4['secciones']), '| faqs:', len(L4['faqs']))
print('  seoTitle:', len(L4['seoTitle']) + 21, 'ch | seoDescription:', len(L4['seoDescription']), 'ch')
print('  imagenes distintas:', len(set(srcs)), 'de', len(srcs), '| faltantes:', faltan or 'ninguna')
print('  palabras:', palabras)
