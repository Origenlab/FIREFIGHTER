# -*- coding: utf-8 -*-
"""L4 — SKOLD HERO · barrera exterior Advance.

Ruta: /productos/epp-para-bomberos/trajes-estructurales-nomex-pbi/skold-hero-advance

Angulo distinto al de PBI MAX: SKOLD lista Advance como barrera seleccionable pero NO publica
composicion ni gramaje de esa configuracion. La pagina no rellena ese hueco: lo mapea.
Vale como contenido porque separa lo documentado de lo no documentado y entrega las preguntas
exactas que hay que enviarle al fabricante. No se le atribuye ninguna cifra.
"""
import json, io, collections, os, re

RUTA = 'src/data/productos.json'

L4 = collections.OrderedDict([
  ("seoTitle", "Traje SKÖLD HERÖ con barrera Advance"),
  ("seoDescription",
    "Barrera exterior Advance del conjunto SKÖLD HERÖ: qué está documentado, qué no publica el "
    "fabricante y las preguntas que hay que resolver antes de cotizar."),
  # El badge de la card es la edicion declarada del MODELO. Aqui el alcance por configuracion
  # no esta confirmado, asi que el hero lo dice en lugar de citar una norma que no aplica aun.
  ("badge", "Alcance por confirmar"),
  ("h1", "Traje estructural SKÖLD HERÖ con barrera exterior Advance"),
  ("subtitulo",
    "Advance es una de las cinco barreras exteriores que SKÖLD ofrece sobre el conjunto HERÖ. "
    "Todo el ensamble —DRD integrado, cuello de cobertura 360°, arnés de Kevlar y refuerzos— es "
    "el del modelo; lo que cambia es la capa exterior, y esa es justo la que el fabricante no "
    "documenta en la ficha pública."),

  ("heroImg", {
    "src": "/images/catalogo/1575507371089-600x450.webp",
    "alt": "Chaquetones y cascos estructurales colgados en la estación de bomberos",
  }),
  ("heroBloques", [
    {
      "label": "Por qué esta ficha se ve distinta",
      "texto": (
        "No vamos a inventarte una tabla. SKÖLD lista <strong>Advance</strong> entre las barreras "
        "exteriores del HERÖ, pero la ficha del modelo <strong>no publica su composición ni su "
        "gramaje</strong>, y sin gramaje no se puede estimar el peso del ensamble ni la carga "
        "térmica sobre el elemento. Lo que sí podemos hacer —y es lo que esta página hace— es "
        "separar con precisión lo que está documentado de lo que hay que pedir, y darte las "
        "preguntas exactas para pedirlo."
      ),
    },
    {
      "label": "Gestionamos la ficha, no la suponemos",
      "texto": (
        "Como distribuidores autorizados solicitamos al fabricante la <strong>ficha técnica de la "
        "configuración</strong> con composición, gramaje, barreras de humedad y térmica, valores "
        "de TPP y THL del ensamble armado y el alcance del certificado. Cuando llega, la propuesta "
        "sale con números; mientras no llega, te lo decimos así en lugar de copiar el catálogo. "
        "Cobertura en los <strong>32 estados de la República</strong>."
      ),
    },
  ]),
  ("heroDatos", [
    {"label": "Estado del dato", "valor": "Ficha por solicitar"},
    {"label": "Certificación del modelo", "valor": "UL · expediente MH60435"},
    {"label": "Alcance por configuración", "valor": "Por confirmar"},
  ]),
  ("specStrip", [
    {"label": "Capa exterior", "valor": "Advance · sin gramaje publicado"},
    {"label": "Barrera de humedad", "valor": "Por confirmar en la ficha"},
    {"label": "Barrera térmica", "valor": "Por confirmar en la ficha"},
    {"label": "Conjunto", "valor": "HERÖ · DRD, cuello 360°, Kevlar"},
    {"label": "Tallas", "valor": "S a 4X (nivel modelo)"},
    {"label": "Certificación", "valor": "UL MH60435 · alcance por confirmar"},
  ]),

  ("secciones", [
    {
      "id": "que-es",
      "eyebrow": "Qué estás evaluando",
      "titulo": "Advance no es otro traje: es otra capa exterior del mismo HERÖ",
      "parrafos": [
        "El <strong>SKÖLD HERÖ</strong> es un conjunto de protección para combate estructural, y "
        "sobre él el fabricante permite elegir entre cinco barreras exteriores: Advance, Kombat "
        "Flex, PBI MAX 7.0, Pioneer y Defender 750. Cuando cambias de barrera <strong>no cambias "
        "de traje</strong>: el DRD sigue en la espalda, el cuello sigue siendo el de cobertura "
        "360°, el arnés sigue siendo de Kevlar y las claves de producto siguen la misma "
        "estructura.",
        "Eso tiene una consecuencia útil para quien compra: buena parte de lo que hay que "
        "verificar en una propuesta ya está documentado a nivel de modelo. Y una consecuencia "
        "incómoda: la capa que define el peso, la mano y la resistencia mecánica del traje es "
        "precisamente la que aquí queda sin números.",
      ],
      "nota": "Dos propuestas pueden decir “SKÖLD HERÖ” y no ser el mismo traje. La configuración de barreras tiene que aparecer en la partida, no solo el modelo.",
    },
    {
      "id": "lo-documentado",
      "eyebrow": "Lo que sí está documentado",
      "titulo": "El conjunto: esto no depende de la barrera exterior",
      "parrafos": [
        "Estos elementos los publica SKÖLD a nivel de modelo, así que aplican también si eliges "
        "Advance. Son los que puedes exigir por escrito y verificar contra la prenda física "
        "cuando llegue."
      ],
      "lista": [
        {"t": "DRD integrado", "d": "Drag Rescue Device alojado en la espalda del chaquetón, para extraer a un elemento inconsciente desde un punto diseñado para eso."},
        {"t": "Cuello tipo escudo 360°", "d": "Cobertura total alrededor del cuello sin partes expuestas. Su desempeño real depende del ajuste y de la interfaz con capucha y casco."},
        {"t": "Arnés de Kevlar integrado", "d": "Incorporado a la prenda, no accesorio externo."},
        {"t": "Refuerzos Stedshield y Ultrashield", "d": "En mangas, hombros, codos y rodillas del chaquetón, y Stedshield en los tobillos del pantalón."},
        {"t": "Costura de Kevlar doble y triple", "d": "Hilo aramídico en todo el conjunto, con puño de Kevlar y ojillo para pulgar."},
        {"t": "Cinta ORALITE® FTP2575-S de 3″", "d": "Ultra Brilliance™ en amarillo verdoso fluorescente, más bies reflejante plata en pecho, espalda, brazos, bolsas y tobillos. Especificada por serie, lo que permite pedir la reposición igual años después."},
        {"t": "Bolsas y sujeción", "d": "Bolsa tipo fuelle porta-radios, dos bolsillos inferiores y porta linternas en el chaquetón. Tirantes acolchados con conexión rápida, corte tipo diamante y dos bolsillos laterales tipo parche en el pantalón."},
        {"t": "Tallas y presentaciones", "d": "S a 4X, en chaquetón, pantalón o traje completo, cada presentación con clave propia. La tabla de medidas UL del exterior se publica para S a 3XL."},
      ],
    },
    {
      "id": "lo-no-publicado",
      "eyebrow": "Lo que falta",
      "titulo": "Los cinco datos que la ficha no publica y qué decide cada uno",
      "parrafos": [
        "Esta es la parte que ningún catálogo te va a poner por escrito, así que la ponemos "
        "nosotros. No es una lista de defectos: es el mapa de lo que hay que resolver antes de "
        "firmar, y sirve igual para evaluar a cualquier proveedor que te ofrezca esta "
        "configuración."
      ],
      "tabla": {
        "head": ["Dato ausente", "Qué decide", "Consecuencia de no tenerlo"],
        "rows": [
          ["Composición de la tela", "Comportamiento ante llama y resistencia mecánica", "No se puede anticipar si encoge, si carboniza conservando estructura ni cómo responde al desgarre"],
          ["Gramaje en oz/yd²", "Peso del ensamble y carga térmica", "No hay forma de comparar fatiga del elemento contra PBI MAX 7.0 ni contra otra marca"],
          ["Barrera de humedad", "Paso de vapor sobrecalentado", "Es la capa que produce la mayoría de las quemaduras por escaldadura dentro de un traje certificado"],
          ["Barrera térmica", "Tiempo real de tolerancia térmica", "Sin ella no hay TPP del conjunto, y el TPP se certifica sobre el ensamble armado"],
          ["TPP y THL del ensamble", "Protección térmica y evacuación de calor metabólico", "Son los dos valores que la norma exige y que ordenan cualquier comparación seria"],
        ],
      },
      "nota": "Un traje puede ser excelente y no tener ficha pública: la ausencia del dato no es un defecto del producto, es un vacío de información. Lo que no se puede hacer es <strong>rellenarlo con supuestos</strong> y presentarlo como especificación en una requisición.",
    },
    {
      "id": "el-nombre",
      "eyebrow": "Autoridad técnica",
      "titulo": "“Advance” es un nombre comercial, no una especificación",
      "parrafos": [
        "En el mercado de telas para protección estructural el nombre Advance corresponde a una "
        "mezcla de aramidas, y las referencias que circulan <strong>no coinciden entre "
        "sí</strong>: una documentación forestal que manejamos la registra como 60 % Kevlar y "
        "40 % Nomex en 7.0 oz, y hay tablas comparativas que la atribuyen a un fabricante de "
        "fibra distinto. Cualquiera de esas cifras puede ser correcta para el producto de otra "
        "familia y equivocada para esta.",
        "Por eso no trasladamos ningún número a la configuración Advance del HERÖ. Un mismo "
        "nombre comercial se usa en gramajes distintos y para prendas distintas —forestal y "
        "estructural no son la misma tela aunque compartan marca—, y la única cifra válida en una "
        "compra es la de <strong>la ficha de la configuración que estás cotizando</strong>.",
      ],
      "nota": "Si un proveedor te entrega composición y gramaje de Advance para el HERÖ, pídele la fuente. Si viene de la ficha del fabricante, es un dato. Si viene de una tabla genérica de telas, es una suposición con formato de dato.",
    },
    {
      "id": "preguntas",
      "eyebrow": "Cómo se resuelve",
      "titulo": "Las ocho preguntas que hay que enviar al fabricante",
      "parrafos": [
        "Este es el cuestionario que usamos nosotros para pedir la ficha de una configuración sin "
        "ficha pública. Puedes copiarlo tal cual y mandarlo, con nosotros o con quien te esté "
        "cotizando. Las respuestas por escrito son lo que convierte una oferta en algo "
        "comparable."
      ],
      "lista": [
        {"t": "1 · Composición", "d": "¿Cuál es la composición exacta de la barrera exterior Advance en el HERÖ, con porcentajes por fibra?"},
        {"t": "2 · Gramaje", "d": "¿Cuál es el gramaje en oz/yd² de esa barrera exterior?"},
        {"t": "3 · Barreras interiores", "d": "¿Qué barrera de humedad y qué barrera térmica se combinan con Advance en la configuración estándar?"},
        {"t": "4 · TPP y THL", "d": "¿Cuáles son los valores de TPP y THL del ensamble armado con esa combinación de tres capas?"},
        {"t": "5 · Alcance del certificado", "d": "¿El expediente UL MH60435 cubre esta configuración específica, y bajo qué edición normativa?"},
        {"t": "6 · Claves de producto", "d": "¿Qué claves corresponden a chaquetón, pantalón y traje completo con Advance, y en qué tallas?"},
        {"t": "7 · Colores y opcionales", "d": "¿Qué colores están disponibles y qué opcionales cambian respecto a la configuración PBI MAX?"},
        {"t": "8 · Cuidado", "d": "¿El procedimiento de lavado y el criterio de retiro son los mismos que para el resto del modelo?"},
      ],
      "nota": "Con esas ocho respuestas se puede armar una tabla comparativa real contra PBI MAX 7.0 o contra cualquier otra marca. Sin ellas, cualquier comparación es una opinión bien redactada.",
    },
    {
      "id": "certificacion",
      "eyebrow": "Certificación",
      "titulo": "El expediente es del modelo; el alcance se confirma por configuración",
      "parrafos": [
        "SKÖLD publica para el HERÖ certificación por laboratorio <strong>UL bajo NFPA 1971 "
        "edición 2018</strong>, con expediente <strong>MH60435</strong>. Es certificación de "
        "tercera parte y se puede rastrear en UL Product iQ, lo que ya es una diferencia de fondo "
        "frente a una declaración de conformidad del propio fabricante.",
        "Lo que hay que precisar es el <strong>alcance</strong>: la certificación se emite sobre "
        "el ensamble, y la configuración documentada en la ficha que conocemos es la de PBI MAX "
        "7.0. Que el expediente exista no acredita automáticamente cualquier combinación de las "
        "cinco barreras. Es la pregunta 5 del cuestionario, y es la que no conviene dar por "
        "resuelta.",
      ],
      "nota": "Además, NFPA 1971 fue consolidada en <strong>NFPA 1970 (1971) edición 2025</strong> y la transición cerró el 18 de marzo de 2026: un certificado emitido hoy debe referirse a la edición vigente. El inventario ya etiquetado no se invalida —se rige por NFPA 1850 (1851)—, pero en la compra hay que precisar qué edición ampara el documento que se entrega.",
    },
    {
      "id": "anexo",
      "eyebrow": "Licitación",
      "titulo": "Cómo redactar la partida sin inventar datos",
      "parrafos": [
        "Si tu proceso ya está en marcha y no puedes esperar la ficha, hay una forma de escribir "
        "la partida que no te compromete con una cifra falsa ni te deja sin criterio de "
        "evaluación: especificar el conjunto y exigir el dato como entregable."
      ],
      "tabla": {
        "head": ["En la partida escribe", "En lugar de"],
        "rows": [
          ["Conjunto estructural con DRD integrado, cuello de cobertura 360° y arnés de Kevlar", "“Traje tipo SKÖLD”"],
          ["Barrera exterior en mezcla de aramidas, composición y gramaje declarados por el fabricante en ficha técnica", "“Barrera exterior Advance de 7 oz”"],
          ["Certificado de tercera parte con número de expediente y edición normativa vigente", "“Cumple NFPA”"],
          ["TPP y THL del ensamble armado, declarados por el fabricante", "sin mención"],
          ["Ficha técnica de la configuración en español como entregable de la propuesta", "sin mención"],
        ],
      },
      "nota": "Redactada así, la partida es <strong>comparable y auditable</strong>: quien no pueda entregar la ficha queda fuera por incumplimiento documental, no por una discusión de opiniones sobre telas.",
    },
    {
      "id": "cuando-conviene",
      "eyebrow": "Criterio de selección",
      "titulo": "Cuándo tiene sentido evaluar Advance",
      "parrafos": [
        "No descartamos una barrera por no tener ficha pública, y tampoco la recomendamos a "
        "ciegas. Estos son los escenarios en los que vale la pena pedir la ficha y ponerla en la "
        "mesa, y el escenario en el que conviene irse directo a la configuración documentada."
      ],
      "lista": [
        {"t": "Tiene sentido evaluarla", "d": "Cuando el fabricante puede entregar la ficha en el plazo de tu proceso y buscas alternativas de costo o disponibilidad frente a PBI MAX 7.0."},
        {"t": "Tiene sentido evaluarla", "d": "Cuando ya operas HERÖ en tu cuerpo y quieres ampliar la flota manteniendo modelo, claves y procedimiento de cuidado."},
        {"t": "Tiene sentido evaluarla", "d": "Cuando el requerimiento se define por conjunto —DRD, cuello 360°, refuerzos— y la barrera exterior es una variable abierta en tus bases."},
        {"t": "Conviene ir a PBI MAX 7.0", "d": "Cuando la compra es por licitación con anexo técnico cerrado y necesitas cifras verificables desde el primer día: ahí la configuración documentada te ahorra la discusión."},
      ],
    },
    {
      "id": "siguiente-paso",
      "eyebrow": "Qué hacemos nosotros",
      "titulo": "De una barrera listada a una propuesta con números",
      "parrafos": [
        "Solicitamos al fabricante la ficha de la configuración con las ocho respuestas, "
        "confirmamos el alcance del certificado y la edición normativa, y te devolvemos la "
        "propuesta con partidas, claves de producto y tallas verificadas contra la tabla de "
        "medidas. Si la ficha no llega o llega incompleta, te lo decimos y comparamos contra "
        "PBI MAX 7.0 con lo que sí está publicado.",
        "Antes de cerrar cualquier pedido de brigada enviamos <strong>juego de tallas de "
        "muestra</strong>: la tabla UL describe la prenda extendida, no el cuerpo del elemento, y "
        "esa diferencia es la que produce la escena de veinte trajes correctos y cinco imposibles "
        "de usar.",
      ],
      "nota": "Cada envío sale con certificado del ensamble, número de serie y fecha de fabricación por prenda, etiqueta permanente con la composición de las tres capas, procedimiento de lavado y retiro en español, carta de distribuidor autorizado y factura desglosada por partida y talla.",
    },
  ]),

  ("galeria", [
    {"src": "/images/catalogo/1669209285616-600x450.webp",
     "alt": "Chaquetones estructurales en rack de estación de bomberos",
     "caption": "El conjunto no cambia con la barrera"},
    {"src": "/images/catalogo/1503714964235-600x450.webp",
     "alt": "Bombero revisando y ajustando su equipo de protección antes de salir",
     "caption": "Verificación contra la prenda física"},
    {"src": "/images/catalogo/1606613817012-600x450.webp",
     "alt": "Bombero equipado junto a la unidad en escena",
     "caption": "Desempeño en operación"},
    {"src": "/images/catalogo/1662121396496-600x400.webp",
     "alt": "Chaquetones estructurales colgados en el vestidor de la estación",
     "caption": "Control de tallas por clave"},
  ]),

  ("aplicaciones", [
    {"sector": "Cuerpos de bomberos",
     "desc": "Para ampliar una flota que ya opera HERÖ manteniendo modelo, claves y procedimiento de cuidado. La barrera se define con la ficha en mano, no en la orden de compra."},
    {"sector": "Brigadas industriales",
     "desc": "Cuando el requerimiento se especifica por conjunto —DRD, cuello 360°, refuerzos— y la barrera exterior queda abierta a propuesta del proveedor con ficha respaldatoria."},
    {"sector": "Licitación pública",
     "desc": "Aquí conviene exigir la ficha de la configuración como entregable de la propuesta. Si el proceso no admite esperarla, la configuración documentada evita la impugnación."},
  ]),

  ("datoClave", {
    "titulo": "Sin gramaje no hay comparación",
    "texto": "El gramaje es lo que decide cuánto pesa el ensamble y cuánto tarda el elemento en agotarse. Dos trajes con la misma etiqueta de norma pueden diferir de forma notable en peso, y <strong>ese dato es justo el que no está publicado</strong> para esta barrera."
  }),

  ("referencias", [
    {"code": "UL · MH60435", "desc": "Expediente de certificación del HERÖ publicado por SKÖLD. Rastreable en UL Product iQ. Hay que confirmar si su alcance cubre la configuración Advance."},
    {"code": "NFPA 1971 · 2018", "desc": "Edición bajo la que está declarada la certificación UL del modelo. Fue sustituida."},
    {"code": "NFPA 1970 · 2025", "desc": "Estándar vigente que consolidó NFPA 1971, 1975, 1981 y 1982. La transición cerró el 18 de marzo de 2026."},
    {"code": "NFPA 1850 · 2026", "desc": "Selección, cuidado y mantenimiento del conjunto en servicio. Rige la permanencia del inventario, no la edición de certificación."},
    {"code": "NOM-017-STPS", "desc": "Selección, entrega y capacitación en el uso del equipo de protección personal según el riesgo del puesto."},
  ]),

  ("blog", [
    "guia-trajes-estructurales-nfpa-1971",
    "marcas-trajes-bomberos-comparativa-mexico",
    "equipar-brigada-trajes-bomberos-tallaje-licitacion",
    "licitaciones-equipos-contra-incendios-mexico",
    "nfpa-1971-mexico-norma-bomberos",
    "mantenimiento-epp-estructural-nfpa-1851",
  ]),

  ("faqs", [
    {"q": "¿Por qué esta ficha no trae composición ni gramaje?",
     "a": "Porque el fabricante no los publica para esta configuración. SKÖLD lista Advance entre las cinco barreras exteriores disponibles del HERÖ, pero la ficha técnica que documenta composición y gramaje capa por capa corresponde a la configuración PBI MAX 7.0. Podríamos copiar cifras de una tabla genérica de telas y presentarlas como especificación; no lo hacemos, porque en una licitación ese dato inventado lo firma el comprador, no el proveedor."},
    {"q": "¿Entonces Advance es peor que PBI MAX 7.0?",
     "a": "No hay base para afirmarlo, y tampoco lo contrario. La diferencia verificable hoy es de información, no de desempeño: de las cinco barreras del HERÖ solo PBI MAX publica sus números. Una barrera puede ser excelente y no tener ficha pública. Lo que no se puede es compararlas técnicamente mientras falten composición, gramaje, barreras interiores y los valores de TPP y THL del ensamble armado."},
    {"q": "¿Puedo comprar el HERÖ con barrera Advance de todas formas?",
     "a": "Sí. Es una configuración que el fabricante ofrece y la cotizamos. Lo que hacemos antes es solicitar la ficha de la configuración con las ocho preguntas que están en esta página, para que la propuesta salga con números y con el alcance del certificado confirmado. Si el proceso no admite esperar esa respuesta, te lo decimos y evaluamos ir a PBI MAX 7.0, que ya está documentada."},
    {"q": "¿Qué sí puedo exigir por escrito si elijo Advance?",
     "a": "Todo lo que el fabricante publica a nivel de modelo y que no depende de la barrera exterior: DRD integrado en la espalda, cuello de cobertura 360° sin partes expuestas, arnés de Kevlar integrado, refuerzos Stedshield y Ultrashield en mangas, hombros, codos, rodillas y tobillos, costura de Kevlar doble y triple, cinta ORALITE Ultra Brilliance serie FTP2575-S de 3″, configuración de bolsas y tirantes, tallas de S a 4X y las claves por presentación. Eso ya es un anexo técnico razonable."},
    {"q": "¿El expediente UL MH60435 cubre la configuración Advance?",
     "a": "Es exactamente lo que hay que confirmar por escrito. El expediente es del modelo HERÖ y la configuración documentada en la ficha que conocemos es la de PBI MAX 7.0. La certificación se emite sobre el ensamble completo, así que la existencia del expediente no acredita automáticamente cualquier combinación de las cinco barreras. Pedimos al fabricante que declare el alcance y la edición normativa aplicable a la configuración cotizada."},
    {"q": "Vi una tabla que dice que Advance es 60 % Kevlar y 40 % Nomex, ¿sirve?",
     "a": "Como referencia de industria sí; como especificación de compra, no. El nombre Advance aparece en documentación de prendas distintas —incluida ropa forestal, que no es la misma tela ni el mismo gramaje que una capa exterior estructural— y las fuentes que circulan no coinciden entre sí, ni siquiera en el fabricante de la fibra. Trasladar esa cifra a la configuración Advance del HERÖ sería una suposición con formato de dato. Si alguien te la entrega como especificación, pídele la fuente."},
    {"q": "¿Cómo redacto la partida si mi licitación ya está en curso?",
     "a": "Especifica el conjunto y exige el dato como entregable, en lugar de comprometerte con una cifra que no puedes sostener. Pide conjunto estructural con DRD, cuello 360° y arnés de Kevlar; barrera exterior en mezcla de aramidas con composición y gramaje declarados por el fabricante en ficha técnica; certificado de tercera parte con número de expediente y edición vigente; TPP y THL del ensamble armado; y la ficha de la configuración en español como entregable. Así la partida queda comparable y auditable."},
    {"q": "¿Cuánto tardan en conseguir la ficha y en cotizar?",
     "a": "La cotización sale en menos de 24 horas hábiles con lo que está publicado y con el estado de cada dato pendiente marcado como tal. El tiempo de la ficha depende del fabricante, y no vamos a prometerte un plazo que no controlamos: te decimos cuándo la solicitamos y te avisamos en cuanto llega o si no llega. Antes de cerrar un pedido de brigada enviamos juego de tallas de muestra."},
  ]),
])


with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')
catalogo = prod['l3']['catalogo']
card = next(c for c in catalogo['cards'] if c['variante'] == 'Advance')

card['slug'] = 'skold-hero-advance'
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

faltan = [g['src'] for g in L4['galeria'] if not os.path.exists('public' + g['src'])]
if not os.path.exists('public' + L4['heroImg']['src']):
    faltan.append(L4['heroImg']['src'])
print('slug:', card['slug'])
print('secciones:', len(L4['secciones']), '| faqs:', len(L4['faqs']), '| referencias:', len(L4['referencias']))
print('seoTitle:', len(L4['seoTitle']) + len(' | Firefighter.com.mx'), 'ch')
print('seoDescription:', len(L4['seoDescription']), 'ch')
print('imagenes faltantes:', faltan or 'ninguna')
palabras = 0
for s in L4['secciones']:
    for p in s.get('parrafos', []): palabras += len(re.sub(r'<[^>]+>', '', p).split())
    for it in s.get('lista', []): palabras += len(re.sub(r'<[^>]+>', '', it['d']).split())
    for r in s.get('tabla', {}).get('rows', []): palabras += sum(len(c.split()) for c in r)
    if s.get('nota'): palabras += len(re.sub(r'<[^>]+>', '', s['nota']).split())
for f_ in L4['faqs']: palabras += len(f_['a'].split())
print('palabras de contenido aprox:', palabras)

# Ninguna imagen repetida dentro de la pagina
srcs = [L4['heroImg']['src']] + [g['src'] for g in L4['galeria']]
print('imagenes distintas en la ficha:', len(set(srcs)), 'de', len(srcs))
