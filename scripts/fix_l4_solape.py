# -*- coding: utf-8 -*-
"""Baja el solape de texto entre las cuatro fichas L4 "sin ficha".

Las cuatro comparten hechos (el conjunto del HERO es el mismo) pero no deben compartir frases.
Este script reescribe los cuatro pasajes que estaban casi identicos, cada uno desde el angulo
propio de su ficha, y elimina la nota de documentacion de envio que ya vive en el sidebar.

  lo-documentado   -> Advance: exigibilidad · Pioneer: verificacion · Defender: nomenclatura
                      (Kombat ya estaba reescrito hacia movilidad)
  lo-no-publicado  -> nota propia por ficha
  certificacion    -> parrafos y nota propios por ficha
  cuando-conviene  -> lead y lista propios por ficha
  siguiente-paso   -> se quita la nota (duplicaba el sidebar "Va con el envio")
"""
import json, io, collections, re, itertools

RUTA = 'src/data/productos.json'


def sec(l4, sid):
    """Devuelve la seccion o None si esa ficha no la trae."""
    return next((s for s in l4['secciones'] if s['id'] == sid), None)


def insertar_despues(l4, ref_id, nueva):
    """Inserta una seccion nueva justo despues de ref_id."""
    i = next(n for n, s in enumerate(l4['secciones']) if s['id'] == ref_id)
    l4['secciones'].insert(i + 1, nueva)


# ─────────────────────────── ADVANCE ───────────────────────────
ADVANCE = {
  'lo-documentado': {
    'eyebrow': 'Lo que sí es exigible',
    'titulo': 'El contrato se puede cerrar sobre esto',
    'parrafos': [
      "Aunque falte la ficha de la barrera, hay un cuerpo de especificaciones que el fabricante "
      "publica a nivel de modelo y que por lo tanto es <strong>exigible en el contrato</strong> "
      "con Advance igual que con cualquier otra configuración. Ponerlas en la partida ya te deja "
      "un anexo técnico defendible mientras llega el resto.",
    ],
    'lista': [
      {"t": "DRD integrado", "d": "Exigible como característica de diseño del chaquetón, no como accesorio. La norma lo requiere en ensambles estructurales, así que su ausencia sería motivo de rechazo, no de negociación."},
      {"t": "Cuello de cobertura 360°", "d": "Exigible como diseño sin partes expuestas alrededor del cuello. Se comprueba visualmente en la recepción, con capucha y casco puestos."},
      {"t": "Arnés de Kevlar", "d": "Exigible como elemento integrado a la prenda. Si la propuesta lo ofrece como accesorio aparte, no es la misma especificación."},
      {"t": "Refuerzos en zonas de desgaste", "d": "Stedshield y Ultrashield en mangas, hombros, codos y rodillas; Stedshield en tobillos. Exigible por ubicación, que es lo verificable al tacto."},
      {"t": "Hilo aramídico", "d": "Costura doble y triple en Kevlar, con puño de Kevlar y ojillo para pulgar. Exigible por material del hilo: es lo que se pierde primero en reparaciones fuera de taller autorizado."},
      {"t": "Cinta reflejante por serie", "d": "ORALITE® Ultra Brilliance™ FTP2575-S de 3″ y bies plata. Exigible por número de serie, no por descripción: así la reposición se pide idéntica años después."},
      {"t": "Claves de producto y tallas", "d": "Chaquetón CHB910, pantalón PB910, traje completo TB910, de S a 4X. Exigible por clave, que es el nivel de precisión con el que el fabricante despacha."},
    ],
  },
  'lo-no-publicado-nota':
    "La ausencia del dato no es un defecto del producto, es un hueco en la documentación. La "
    "diferencia importa porque un hueco se llena pidiendo la ficha; un defecto no. Lo que no se "
    "hace es <strong>cerrarlo con supuestos</strong> y firmarlo como si fuera especificación.",
  'certificacion': {
    'titulo': 'Certificación de tercera parte y por qué eso ya es mucho',
    'parrafos': [
      "SKÖLD publica para el HERÖ certificación por laboratorio <strong>UL bajo NFPA 1971 edición "
      "2018</strong> con expediente <strong>MH60435</strong>. La palabra clave es UL: el documento "
      "lo emite un organismo independiente y su registro se puede consultar sin depender del "
      "proveedor. En un mercado donde abundan las declaraciones de conformidad del propio "
      "fabricante, ese solo hecho ordena una comparación.",
      "Dicho eso, el expediente ampara <strong>ensambles</strong>, y la configuración que la ficha "
      "documenta es la de PBI MAX 7.0. Que el número exista no dice qué combinaciones cubre. "
      "Pídele al fabricante que lo declare por escrito para la configuración con Advance, con la "
      "edición normativa aplicable.",
    ],
    'nota':
      "NFPA 1971 fue consolidada en <strong>NFPA 1970 (1971) edición 2025</strong>; la transición "
      "cerró el 18 de marzo de 2026. Traducido a compra: hoy nadie puede emitir un certificado "
      "nuevo contra la edición 2018, y un documento que la cite tiene que venir acompañado de su "
      "fecha de emisión para saber qué representa.",
  },
  'cuando-conviene': {
    'titulo': 'En qué escenarios vale la pena pedir la ficha',
    'parrafos': [
      "La pregunta útil no es si Advance es buena, sino si tu proceso aguanta esperar el dato. "
      "Estos cuatro escenarios cubren la mayoría de los casos que nos llegan.",
    ],
    'lista': [
      {"t": "Sí, si tienes margen de tiempo", "d": "Tu calendario admite un ciclo de ida y vuelta con el fabricante antes de comprometer presupuesto. Ahí Advance entra en la comparación con todas las de la ley."},
      {"t": "Sí, si buscas costo o disponibilidad", "d": "Estás explorando alternativas a PBI MAX 7.0 por precio o por tiempos de entrega, y el criterio de decisión final será documental."},
      {"t": "Sí, si ya operas HERÖ", "d": "Ampliar flota manteniendo modelo, claves y procedimiento de cuidado tiene un valor operativo real que justifica pedir la ficha."},
      {"t": "No, si el anexo ya está cerrado", "d": "Licitación con especificación fija y fecha encima. Con la ficha pendiente el expediente queda expuesto: ahí PBI MAX 7.0 es la decisión sensata."},
    ],
  },
}

# ─────────────────────────── KOMBAT FLEX ───────────────────────────
KOMBAT = {
  'lo-no-publicado-nota':
    "Ninguno de estos huecos vuelve al traje inseguro: lo vuelve <strong>incomparable</strong>. Y "
    "en movilidad eso pesa doble, porque el argumento comercial de la configuración descansa "
    "justo en los dos datos que faltan —gramaje y peso del ensamble—.",
  'certificacion': {
    'titulo': 'El certificado no dice nada sobre movilidad',
    'parrafos': [
      "Conviene tenerlo claro antes de leer cualquier propuesta: <strong>ningún certificado "
      "acredita flexibilidad</strong>. Lo que SKÖLD publica para el HERÖ es certificación por "
      "laboratorio UL bajo NFPA 1971 edición 2018, expediente <strong>MH60435</strong>, y lo que "
      "esa certificación cubre es desempeño térmico y de diseño del ensamble, no rango de "
      "movimiento.",
      "De ahí que esta ficha insista en la demo. El papel resuelve la pregunta de protección; la "
      "prueba con el elemento vestido resuelve la de movilidad. Necesitas las dos, y para la "
      "primera hay que pedirle al fabricante que declare si el expediente cubre la combinación "
      "con Kombat Flex y bajo qué edición.",
    ],
    'nota':
      "El dato del certificado que sí se relaciona con movilidad es el <strong>THL</strong>: mide "
      "cuánto calor metabólico evacua el traje, y un THL bajo saca al elemento de operación por "
      "fatiga aunque el rango de movimiento sea excelente. Pídelo junto con el TPP.",
  },
  'cuando-conviene': {
    'titulo': 'Cuándo la demo justifica el esfuerzo',
    'parrafos': [
      "Esta configuración se decide en la prueba, no en la mesa. Estos son los casos donde montar "
      "la demo vale el tiempo que cuesta, y el caso donde no.",
    ],
    'lista': [
      {"t": "Vale la demo", "d": "Tu personal ya se quejó de movilidad y tienes la queja documentada. Una prueba con protocolo convierte una molestia en un criterio de compra."},
      {"t": "Vale la demo", "d": "Tu perfil operativo carga de rescate vehicular, espacios confinados o trabajo en posiciones forzadas, donde el rango de movimiento se cobra en cada salida."},
      {"t": "Vale la demo", "d": "Ya operas HERÖ y quieres comparar variantes sin cambiar modelo, claves ni taller de reparación."},
      {"t": "No vale esperar", "d": "Licitación con anexo cerrado y fecha encima. Ahí ni la demo ni la ficha llegan a tiempo, y PBI MAX 7.0 es la que sostiene el expediente."},
    ],
  },
}

# ─────────────────────────── PIONEER ───────────────────────────
PIONEER = {
  'lo-documentado': {
    'eyebrow': 'Lo que sí se verifica',
    'titulo': 'Lo que se comprueba en la recepción, prenda por prenda',
    'parrafos': [
      "Estas características son de modelo, así que aplican con Pioneer, y todas comparten una "
      "propiedad útil: <strong>se pueden confrontar contra la prenda física y contra la etiqueta "
      "permanente</strong> el día de la entrega. Es la parte del expediente que no depende de que "
      "llegue la ficha de la barrera.",
    ],
    'lista': [
      {"t": "DRD en la espalda", "d": "Abre el compartimento y confirma que el dispositivo está alojado y replegado. Un DRD inaccesible existe en el catálogo y no en la emergencia."},
      {"t": "Continuidad del cuello", "d": "Verifica con capucha y casco puestos que no queden partes expuestas alrededor del cuello. Es una comprobación de ajuste, no de ficha."},
      {"t": "Arnés integrado", "d": "Confirma que está incorporado a la prenda y no entregado como accesorio suelto. Son dos productos distintos con la misma descripción comercial."},
      {"t": "Ubicación de refuerzos", "d": "Stedshield y Ultrashield deben caer en mangas, hombros, codos y rodillas, y Stedshield en los tobillos. Se comprueba al tacto en dos minutos."},
      {"t": "Material del hilo", "d": "Costura de Kevlar doble y triple. Es lo primero que cambia una reparación no autorizada, así que conviene fotografiarlo en la recepción como línea base."},
      {"t": "Serie de la cinta", "d": "ORALITE® Ultra Brilliance™ FTP2575-S de 3″ más bies plata. Contrasta la serie contra la propuesta: es un dato verificable, no una descripción."},
      {"t": "Etiqueta permanente", "d": "Cosida al interior, con fabricante, modelo, fecha, número de serie, composición de las tres capas y marca del organismo certificador. Es la prueba por unidad de todo lo anterior."},
    ],
  },
  'lo-no-publicado-nota':
    "Fíjate en el patrón: cuatro de los seis huecos son <strong>capas o valores del composite</strong>. "
    "No es casualidad. Sin las tres capas declaradas no hay ensamble definido, y sin ensamble "
    "definido no hay alcance certificado que pueda confirmarse.",
  'certificacion': {
    'titulo': 'El caso concreto de Pioneer',
    'parrafos': [
      "Aplicando lo anterior a esta configuración: el expediente <strong>UL MH60435</strong> "
      "existe, es del modelo HERÖ y está declarado bajo NFPA 1971 edición 2018. La ficha que "
      "documenta un composite completo —capa exterior, barrera de humedad y barrera térmica— es "
      "la de PBI MAX 7.0. Para Pioneer, dos de las tres capas están sin declarar.",
      "Eso no significa que la configuración no esté certificada. Significa que <strong>no lo "
      "sabemos desde fuera</strong>, y que la única forma de saberlo es una declaración escrita "
      "del fabricante. Es la pregunta que hacemos antes de cotizar y la que te recomendamos "
      "incluir en tus bases.",
    ],
    'nota':
      "Además hay que fechar el documento: NFPA 1971 fue consolidada en <strong>NFPA 1970 (1971) "
      "edición 2025</strong> y la transición cerró el 18 de marzo de 2026. Un certificado nuevo "
      "tiene que citar la edición vigente; uno anterior sigue siendo válido para el inventario "
      "que ampara, bajo el régimen de NFPA 1850 (1851).",
  },
  'cuando-conviene': {
    'titulo': 'Cuándo el alcance se puede resolver a tiempo',
    'parrafos': [
      "Con esta configuración la decisión no es sobre la tela, es sobre si la documentación llega "
      "antes que tu fecha límite. Así lo ordenamos.",
    ],
    'lista': [
      {"t": "Adelante", "d": "El fabricante puede emitir la declaración de alcance dentro de tu calendario. Con ese documento en mano, Pioneer compite en igualdad."},
      {"t": "Adelante", "d": "Ya operas HERÖ y quieres ampliar flota conservando modelo, claves, taller autorizado y programa de cuidado."},
      {"t": "Adelante con reserva", "d": "Exploras costo o disponibilidad y tienes margen para verificar documentación antes de comprometer presupuesto."},
      {"t": "Mejor no", "d": "El expediente va a auditoría de protección civil o verificación STPS con fecha fija. Con dos capas sin declarar, ahí PBI MAX 7.0 es la opción que no te expone."},
    ],
  },
}

# ─────────────────────────── DEFENDER 750 ───────────────────────────
DEFENDER = {
  'lo-documentado': {
    'eyebrow': 'Lo que sí tiene nombre propio',
    'titulo': 'Cómo se nombra cada cosa sin margen de interpretación',
    'parrafos': [
      "Siguiendo la lógica de esta ficha, aquí está el conjunto documentado <strong>con el nombre "
      "que hay que escribir en la partida</strong> y no con la descripción que se usa al "
      "hablar. Cada línea es copiable tal cual a una requisición.",
    ],
    'lista': [
      {"t": "Escribe: “DRD integrado en espalda de chaquetón”", "d": "No “sistema de rescate” ni “arnés de arrastre”: DRD es la sigla que usa la norma y el fabricante. Drag Rescue Device, alojado dentro de la prenda."},
      {"t": "Escribe: “cuello con cobertura 360° sin partes expuestas”", "d": "No “cuello alto” ni “protector de cuello”, que en catálogo designan un accesorio distinto que se vende aparte."},
      {"t": "Escribe: “arnés de Kevlar integrado a la prenda”", "d": "La palabra integrado es la que evita que te entreguen un arnés externo cumpliendo la misma frase."},
      {"t": "Escribe: “refuerzo Stedshield / Ultrashield” por ubicación", "d": "Mangas, hombros, codos y rodillas en chaquetón; tobillos en pantalón. Refuerzo, no barrera: Stedshield y Stedair son familias distintas."},
      {"t": "Escribe: “costura con hilo de Kevlar, doble y triple”", "d": "Especifica el material del hilo, no “costura reforzada”. Es la diferencia que define si una reparación mantiene la certificación."},
      {"t": "Escribe: “cinta ORALITE® FTP2575-S de 3″”", "d": "Por serie y ancho, más bies reflejante plata. “Cinta reflejante de alta visibilidad” admite cualquier reposición."},
      {"t": "Escribe la clave, no la talla", "d": "CHB910-L, PB910-L, TB910-L. El fabricante despacha por clave; “talla L” es ambiguo entre presentaciones."},
    ],
  },
  'lo-no-publicado-nota':
    "Nota el orden de los problemas en esta configuración: primero el nombre, después el dato. "
    "Resolver la ambigüedad no llena los huecos, pero sin resolverla <strong>ni siquiera sabes "
    "qué estás pidiendo que te declaren</strong>.",
  'certificacion': {
    'titulo': 'Dos de las tres capas sin declarar',
    'parrafos': [
      "SKÖLD publica para el HERÖ certificación por laboratorio <strong>UL bajo NFPA 1971 edición "
      "2018</strong>, expediente <strong>MH60435</strong>, rastreable en UL Product iQ. Es "
      "certificación de tercera parte, no una declaración del propio fabricante, y eso cuenta.",
      "El punto delicado aquí es aritmético: la certificación se emite sobre el ensamble de tres "
      "capas y en esta configuración solo una está nombrada. Con la barrera de humedad y la "
      "térmica sin declarar, no hay forma externa de saber qué composite se evaluó. Es "
      "exactamente lo que hay que pedir por escrito antes de firmar.",
    ],
    'nota':
      "Y hay que fechar el documento: NFPA 1971 quedó consolidada en <strong>NFPA 1970 (1971) "
      "edición 2025</strong>, con transición cerrada el 18 de marzo de 2026. Es otro par de "
      "números que se confunden —1971 y 1970— y que cambian lo que un certificado significa.",
  },
  'cuando-conviene': {
    'titulo': 'Cuándo entra Defender 750 en la comparación',
    'parrafos': [
      "Con la partida bien escrita, la decisión se reduce a si la ficha de las tres capas llega a "
      "tiempo. Estos son los casos.",
    ],
    'lista': [
      {"t": "Entra", "d": "El fabricante puede entregar la ficha completa —las tres capas, no solo la exterior— dentro del plazo de tu proceso."},
      {"t": "Entra", "d": "Ya operas HERÖ y buscas alternativas de costo o disponibilidad conservando modelo, claves y programa de cuidado."},
      {"t": "Entra", "d": "Tus bases especifican por conjunto y dejan la configuración de barreras abierta a propuesta con ficha respaldatoria."},
      {"t": "No entra", "d": "Compra que va a auditoría o licitación con anexo cerrado. Con dos de las tres capas sin declarar el expediente queda débil, y PBI MAX 7.0 lo resuelve."},
    ],
  },
}


PATCH = {
  'skold-hero-advance': ADVANCE,
  'skold-hero-kombat-flex': KOMBAT,
  'skold-hero-pioneer': PIONEER,
  'skold-hero-defender-750': DEFENDER,
}

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')
cards = {c.get('slug'): c for c in prod['l3']['catalogo']['cards'] if c.get('slug')}

for slug, patch in PATCH.items():
    l4 = cards[slug]['l4']

    tocadas = []

    if 'lo-documentado' in patch:
        sec(l4, 'lo-documentado').update(patch['lo-documentado'])
        tocadas.append('lo-documentado')

    if 'lo-no-publicado-nota' in patch:
        sec(l4, 'lo-no-publicado')['nota'] = patch['lo-no-publicado-nota']
        tocadas.append('lo-no-publicado.nota')

    if 'certificacion' in patch:
        s = sec(l4, 'certificacion')
        if s is not None:
            s.update(patch['certificacion'])
            tocadas.append('certificacion')
        else:
            # Pioneer no tenia seccion de certificacion propia: su contenido de norma vive en
            # como-funciona y leer-certificado. Se le agrega el cierre concreto.
            nueva = collections.OrderedDict([('id', 'certificacion'), ('eyebrow', 'Certificación')])
            nueva.update(patch['certificacion'])
            insertar_despues(l4, 'leer-certificado', nueva)
            tocadas.append('certificacion (nueva)')

    if 'cuando-conviene' in patch:
        sec(l4, 'cuando-conviene').update(patch['cuando-conviene'])
        tocadas.append('cuando-conviene')

    # La nota de documentacion de envio ya vive en el sidebar: fuera del cuerpo
    sp = sec(l4, 'siguiente-paso')
    if sp is not None and sp.pop('nota', None) is not None:
        tocadas.append('siguiente-paso.nota quitada')

    print(slug, '·', len(l4['secciones']), 'secciones ·', ', '.join(tocadas))

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')
print('productos.json actualizado')
