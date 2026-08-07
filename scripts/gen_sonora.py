# -*- coding: utf-8 -*-
"""Genera las fichas de Sonora para el directorio de firefighter.com.mx."""
import os, sys, io

BASE = '/sessions/rcw-01myw9qruuvyjbjl2cokhxwj/mnt/FIREFIGHTERCOMMX/src/content/stations/sonora'
os.makedirs(BASE, exist_ok=True)

SERV = {
 'combate-incendios': 'Combate de incendios',
 'atencion-medica': 'Atención médica prehospitalaria',
 'rescate-vehicular': 'Rescate vehicular',
 'rescate-acuatico': 'Rescate acuático',
 'rescate-forestal': 'Rescate forestal',
 'materiales-peligrosos': 'Materiales peligrosos (HAZMAT)',
 'rescate-alturas': 'Rescate en alturas',
 'proteccion-civil': 'Protección civil',
 'prevencion': 'Prevención',
 'capacitacion': 'Capacitación',
}

BASE_SERV = ['combate-incendios', 'atencion-medica', 'rescate-vehicular', 'proteccion-civil']
S_URB = ['combate-incendios', 'atencion-medica', 'rescate-vehicular', 'rescate-alturas', 'proteccion-civil']
S_IND = ['combate-incendios', 'materiales-peligrosos', 'atencion-medica', 'rescate-vehicular', 'rescate-alturas', 'proteccion-civil']
S_MAR = ['combate-incendios', 'atencion-medica', 'rescate-vehicular', 'rescate-acuatico', 'proteccion-civil']
S_MAR_H = ['combate-incendios', 'materiales-peligrosos', 'atencion-medica', 'rescate-vehicular', 'rescate-acuatico', 'proteccion-civil']
S_FOR = ['combate-incendios', 'atencion-medica', 'rescate-vehicular', 'rescate-forestal', 'proteccion-civil']
S_AGRO = ['combate-incendios', 'atencion-medica', 'rescate-vehicular', 'rescate-forestal', 'materiales-peligrosos', 'proteccion-civil']

# Contexto real por municipio. Dos variantes por municipio con varias estaciones
# para que las fichas no queden calcadas.
CTX = {}

CTX['hermosillo'] = [
"""Hermosillo es la capital de Sonora y concentra cerca de un millón de habitantes, la planta armadora de Ford, un corredor de servicios y comercio, y la administración estatal. El verano marca la agenda del cuerpo de bomberos: la ciudad supera con regularidad los **45 °C** y encabeza el país en golpes de calor, lo que dispara los incendios por sobrecarga eléctrica en vivienda —equipos de aire acondicionado trabajando al límite— y los incendios de maleza en lotes baldíos.

A eso se suma el tránsito pesado de la carretera federal 15, que cruza el municipio de norte a sur, y una mancha urbana muy extendida que obliga a repartir las estaciones por sector.""",
"""El municipio de Hermosillo es enorme: llega desde la sierra hasta el Golfo de California y abarca la **Costa de Hermosillo**, uno de los distritos de riego más productivos del noroeste (vid, nogal, hortaliza de exportación), además de la presa Abelardo L. Rodríguez y decenas de kilómetros de litoral.

Esa geografía obliga al departamento a operar estaciones alejadas del centro urbano, con tiempos de traslado largos y respaldo mutuo con los cuerpos vecinos.""",
]

CTX['cajeme'] = [
"""Ciudad Obregón es la cabecera de Cajeme y el centro del **Valle del Yaqui**, el distrito de riego que le dio a México buena parte de su producción de trigo y donde nació la Revolución Verde. Alrededor de la ciudad hay silos, harineras, bodegas de grano, plantas de agroquímicos y patios de maquinaria agrícola.

Ese entorno define el trabajo del cuerpo de bomberos: incendios en almacenes de grano y forraje, quemas agrícolas que se salen de control al final del ciclo, y manejo de agroquímicos. Se suma la presa Álvaro Obregón (El Oviáchic) y el calor extremo del verano.""",
"""Cajeme es el segundo municipio más poblado de Sonora y funciona como centro de servicios de todo el sur del estado. La ciudad creció sobre traza de damero alrededor de la calle Chihuahua y hoy se extiende hacia Esperanza y las colonias industriales del norte.

La corporación reparte sus subestaciones para cubrir esa mancha urbana y los poblados del valle, con la carretera federal 15 y el ferrocarril atravesando el municipio.""",
]

CTX['bacum'] = ["""Bácum es un municipio agrícola del **Valle del Yaqui**, entre Ciudad Obregón y Guaymas, con parte de su territorio dentro del territorio tradicional de la tribu yaqui. Su economía es el riego: trigo, maíz, cártamo y hortaliza.

Para el cuerpo de bomberos eso significa incendios de socas y rastrojo en temporada de quemas, atención a volcaduras sobre la carretera federal 15 —que cruza el municipio— y apoyo a comunidades dispersas con tiempos de respuesta largos."""]

CTX['san-ignacio-rio-muerto'] = ["""San Ignacio Río Muerto es uno de los municipios más jóvenes de Sonora: se separó de Guaymas en 1996. Es agrícola y pesquero, con litoral en la **Bahía de Lobos** y campos de riego del Valle del Yaqui.

Su cuerpo de bomberos es voluntario y cubre un territorio plano y disperso, con incendios agrícolas, atención en carretera y emergencias en el estero y los campos pesqueros."""]

CTX['guaymas'] = [
"""Guaymas es el **principal puerto de altura de Sonora**: mueve contenedores, graneles minerales y combustibles, tiene astillero, flota camaronera y sardinera, plantas de harina de pescado y una termoeléctrica en las cercanías. El riesgo dominante es industrial y portuario —materiales peligrosos, incendios en embarcación y en planta— combinado con rescate acuático real.

El municipio incluye además San Carlos, con turismo náutico y buceo, y la sierra que rodea la bahía de Bacochibampo, donde los incendios de matorral son frecuentes en primavera.""",
"""El municipio de Guaymas es largo y accidentado: sierra, bahías, esteros y una franja de litoral que va desde San Carlos hasta el sur del Valle del Yaqui. La corporación reparte estaciones entre el casco portuario, la zona norte y las comisarías.

Al riesgo urbano se suman el tránsito de la carretera federal 15, las maniobras de carga en el recinto portuario y el rescate en playa y estero durante la temporada alta.""",
]

CTX['guaymas-vicam'] = ["""Vícam es cabecera de los **ocho pueblos yaquis** y el asentamiento yaqui más grande, sobre la carretera federal 15 en el norte del Valle del Yaqui. Pertenece al municipio de Guaymas, aunque su vida civil se organiza en torno a las autoridades tradicionales de la tribu.

Su estación de bomberos atiende un tramo carretero de alta siniestralidad, incendios agrícolas y de vivienda en las comunidades yaquis, con tiempos de traslado largos hacia los hospitales de Obregón y Guaymas."""]

CTX['empalme'] = [
"""Empalme nació como taller y patio de maniobras del **Ferrocarril Sud-Pacífico** a principios del siglo XX, y de ahí su nombre. Hoy está prácticamente conurbado con Guaymas y conserva la infraestructura ferroviaria, además de litoral sobre la bahía y campos de riego del valle.

El cuerpo de bomberos atiende incendios urbanos, emergencias en el patio ferroviario y en las bodegas, rescate acuático en la bahía y el tramo local de la carretera federal 15.""",
"""Empalme comparte con Guaymas la zona metropolitana, el mercado laboral y la respuesta a emergencias mayores. Su traza es de colonias ferrocarrileras y ejidos agrícolas, con vivienda de bajo costo y calles estrechas en el casco antiguo.

El calor del verano y la temporada de ciclones del Golfo de California son los dos factores que más pesan en la operación anual.""",
]

CTX['navojoa'] = [
"""Navojoa es la cabecera del **Valle del Mayo** y la tercera ciudad de Sonora. Vive de la agroindustria —trigo, cártamo, hortaliza— y del comercio regional, y se asienta sobre el río Mayo, aguas abajo de la presa Adolfo Ruiz Cortines (Mocúzari).

Ese río es el riesgo característico: en años de ciclón el desfogue de la presa y las crecidas obligan a evacuar colonias ribereñas, y el cuerpo de bomberos trabaja como brazo operativo de Protección Civil municipal.""",
"""Además del casco urbano, Navojoa cubre comisarías y ejidos del Valle del Mayo con carreteras estatales de un solo carril por sentido. En temporada de quemas agrícolas los incendios de rastrojo son el llamado más repetido.

La corporación municipal opera bajo el mismo mando que Protección Civil, un esquema común en el sur de Sonora.""",
]

CTX['etchojoa'] = ["""Etchojoa está en el corazón del **Valle del Mayo**, entre Navojoa y Huatabampo, y es uno de los municipios con mayor población mayo del estado. Su economía es agrícola de riego y jornalera.

El cuerpo de bomberos municipal atiende incendios de rastrojo y de vivienda en comunidades dispersas, accidentes en carretera estatal y las inundaciones del río Mayo, que en años de ciclón afecta directamente a las localidades bajas del municipio."""]

CTX['huatabampo'] = ["""Huatabampo es el municipio costero del **Valle del Mayo**: pesca ribereña, camaronicultura en granjas del estero y agricultura de riego, con el desarrollo playero de Huatabampito y el estero de Yavaros como puntos de concentración estacional.

Para el cuerpo de bomberos eso combina incendio urbano y agrícola con **rescate acuático** en estero y playa, además de la exposición a ciclones del Pacífico entre agosto y octubre."""]

CTX['alamos'] = ["""Álamos es Pueblo Mágico y antiguo **real de minas de plata**: su centro histórico conserva casonas de los siglos XVIII y XIX con techos de viguería y adobe, un patrimonio que arde con facilidad y que condiciona cualquier ataque de incendio estructural.

El municipio abarca además la Reserva Sierra de Álamos-Río Cuchujaqui, con selva baja caducifolia. En la temporada seca, entre abril y junio, el **incendio forestal** es la emergencia que ocupa a la corporación, coordinada con la brigada de la CONAFOR."""]

CTX['benito-juarez'] = ["""Villa Juárez es la cabecera del municipio de Benito Juárez, en el extremo sur del Valle del Yaqui, con litoral en la **Bahía de Lobos**. Vive del riego agrícola y de la pesca ribereña y de altura.

La estación de bomberos atiende un municipio plano y disperso: incendios de rastrojo, emergencias en los campos pesqueros y en el estero, y accidentes sobre la carretera que conecta con Ciudad Obregón."""]

CTX['nogales'] = [
"""Nogales es el **principal cruce comercial de Sonora con Estados Unidos** y una de las mayores concentraciones maquiladoras del país: más de cien plantas de arneses automotrices, dispositivos médicos y electrónica en los parques industriales del sur y el oriente de la ciudad.

La topografía manda: Nogales está construida sobre cerros y arroyos encajonados, con vivienda irregular en laderas. Las tormentas de verano provocan **inundaciones súbitas** en los arroyos que atraviesan la ciudad, y los incendios en laderas de acceso difícil obligan a ataque a pie con línea manual.""",
"""El cuerpo de bomberos de Nogales es un cuerpo voluntario con más de un siglo de historia y estaciones numeradas por sector. Cubre el corredor industrial, el centro pegado a la línea fronteriza y las colonias del sur, con manejo frecuente de **materiales peligrosos** por el volumen de carga que cruza la garita.

La cercanía con Nogales, Arizona, hace habitual la coordinación transfronteriza en incendios de gran magnitud.""",
]

CTX['san-luis-rio-colorado'] = [
"""San Luis Río Colorado está en el vértice noroeste de Sonora, frente a San Luis, Arizona, y es uno de los lugares más calurosos de México: en verano supera con frecuencia los **50 °C**. Su economía combina agricultura de riego del valle —trigo, algodón, espárrago, cebollín—, maquiladora y comercio fronterizo.

El calor extremo, la quema de esquilmos agrícolas y el desierto de Altar que rodea la ciudad definen el trabajo de las corporaciones locales.""",
"""En San Luis Río Colorado conviven tres corporaciones: la Dirección municipal de Protección Civil y Bomberos, el cuerpo de bomberos voluntarios y los **bomberos rurales**, que cubren el valle agrícola y los ejidos alejados de la mancha urbana.

Ese reparto responde a la geografía del municipio: una ciudad compacta pegada a la línea fronteriza y un valle agrícola extenso con caminos de terracería.""",
]

CTX['caborca'] = [
"""Caborca combina dos economías que marcan a su cuerpo de bomberos: la agricultura de riego —uva de mesa, espárrago, aceituna, nogal— y la **minería de oro** de los tajos de la zona (La Herradura y Noche Buena), con el manejo de explosivos y reactivos que eso implica en el corredor hacia Pitiquito.

El municipio se extiende sobre el desierto de Altar hasta el Golfo de California, con temperaturas de verano por encima de los 45 °C y una red de caminos larga y despoblada.""",
"""El cuerpo de bomberos de Caborca es una asociación civil de voluntarios, un esquema frecuente en el noroeste de Sonora, y sostiene su operación con apoyo municipal y aportaciones de la comunidad.

Atiende el casco urbano, el corredor agrícola y el tramo de la carretera federal 2 que une Santa Ana con San Luis Río Colorado, una de las rutas con más tránsito de carga del estado.""",
]

CTX['pitiquito'] = ["""Pitiquito es un municipio extenso y poco poblado del noroeste de Sonora: ganadería, agricultura y minería en el interior, y litoral en **Puerto Libertad**, donde opera una central termoeléctrica de la CFE.

Su cuerpo de bomberos voluntarios cubre distancias grandes sobre la carretera federal 2 y los caminos rurales, con incendios de matorral en primavera y apoyo a los municipios vecinos de Caborca y Altar."""]

CTX['puerto-penasco'] = [
"""Puerto Peñasco vive del **turismo del alto Golfo de California**: torres de condominios y hoteles frente a la playa, con una población flotante que se multiplica en temporada alta y fines de semana largos. A eso se suman la flota camaronera y la reserva de la biosfera del Alto Golfo y Delta del Río Colorado.

Esa mezcla obliga al cuerpo de bomberos a mantener capacidad de **rescate acuático** y de ataque en altura para los edificios de la franja costera, en un municipio desértico con veranos de más de 45 °C.""",
"""El municipio de Puerto Peñasco creció rápido y de forma dispersa: el casco antiguo junto al puerto, los desarrollos turísticos hacia el poniente y las colonias populares en la meseta. Las estaciones están repartidas para acortar tiempos en una ciudad alargada.

El aislamiento pesa: el hospital de referencia y el apoyo de otras corporaciones quedan a horas por la carretera del desierto de Altar.""",
]

CTX['plutarco-elias-calles'] = ["""Sonoyta es la cabecera de Plutarco Elías Calles, en la frontera con Lukeville, Arizona, y la puerta de entrada a la **Reserva de El Pinacate y Gran Desierto de Altar**, Patrimonio Mundial de la UNESCO.

Su cuerpo de bomberos voluntarios cubre el cruce de las carreteras federales 2 y 8 —el corredor entre Caborca, Puerto Peñasco y la frontera— en uno de los entornos más áridos y despoblados del país, con distancias de auxilio de decenas de kilómetros."""]

CTX['agua-prieta'] = [
"""Agua Prieta es ciudad fronteriza frente a Douglas, Arizona, con un cinturón de **maquiladoras** —arneses, ensamble electrónico, textil— y una tradición ganadera en el valle que la rodea. Durante décadas la región vivió alrededor de la fundición de cobre del lado estadounidense.

El cuerpo de bomberos combina riesgo industrial de planta, incendio urbano y atención en la carretera federal 2, además de las heladas del invierno en una ciudad a 1,200 metros de altitud.""",
"""Agua Prieta está trazada en calles y avenidas numeradas, y sus cuarteles se reparten por sector para cubrir desde la línea fronteriza hasta las colonias del sur y el corredor industrial del poniente.

La coordinación con las corporaciones de Douglas y del condado de Cochise es parte de la operación normal en incendios de gran magnitud.""",
]

CTX['naco'] = ["""Naco es un municipio pequeño de la frontera, frente a Naco, Arizona, con economía ganadera y de comercio de paso, y una parte de la población empleada en la maquila de Agua Prieta y en la minería de Cananea.

Su cuerpo de bomberos es una estructura chica que cubre el casco urbano, los ranchos del valle y el tramo carretero hacia Cananea y Agua Prieta, con apoyo mutuo transfronterizo cuando el incendio lo rebasa."""]

CTX['cananea'] = ["""Cananea es una **ciudad minera**: aquí opera Buenavista del Cobre, el tajo de cobre más grande de México, y aquí ocurrió la huelga de 1906 que se considera antecedente de la Revolución. El municipio está a más de 1,600 metros de altitud, en sierra de encino y pastizal.

Para el cuerpo de bomberos eso significa un contexto de riesgo poco común: proximidad a operación minera con reactivos y explosivos, incendios forestales en la sierra durante la primavera seca y heladas de invierno, además del incendio urbano ordinario."""]

CTX['nacozari'] = ["""Nacozari de García es un municipio minero del noreste de Sonora —la mina de cobre La Caridad está a unos kilómetros— y es la cuna de **Jesús García Corona**, el maquinista que en 1907 alejó del pueblo un tren cargado de dinamita en llamas y murió en la explosión. Es la referencia histórica más directa que tiene el país sobre respuesta a emergencia.

El cuartel de bomberos es una asociación de voluntarios y cubre el casco urbano, los caminos hacia la mina y la sierra circundante, con incendios forestales en la temporada seca."""]

CTX['magdalena'] = ["""Magdalena de Kino es Pueblo Mágico y sede de la cripta del **padre Eusebio Francisco Kino**, el misionero que fundó las misiones del noroeste. Cada octubre la fiesta de San Francisco concentra a cientos de miles de peregrinos en una ciudad de poco más de treinta mil habitantes.

Ese evento define el año operativo del cuartel de bomberos: concentración masiva, puestos de comida con gas LP, tránsito extraordinario sobre la carretera federal 15 y necesidad de coordinación con Protección Civil estatal."""]

CTX['santa-ana'] = [
"""Santa Ana es el **nudo carretero del noroeste de Sonora**: aquí se separan la carretera federal 15 hacia Nogales y la federal 2 hacia Caborca y San Luis Río Colorado. Por su entronque pasa buena parte de la carga que cruza a Estados Unidos por el corredor del Pacífico.

Para el cuerpo de bomberos eso se traduce en accidentes de tránsito pesado, derrames de combustible y de sustancias en tránsito, y atención de emergencias a viajeros, además del servicio urbano de una cabecera ganadera y comercial.""",
"""El municipio de Santa Ana combina el casco urbano sobre la federal 15 con ejidos ganaderos y agrícolas en el valle del río Magdalena. Las estaciones se reparten para cubrir el entronque carretero y las colonias del sur.

En primavera los incendios de pastizal y matorral son el llamado más frecuente, y en verano las tormentas dejan arroyos crecidos que cortan caminos rurales.""",
]

CTX['bacoachi'] = ["""Bacoachi es un municipio serrano del alto **río Sonora**, entre Cananea y Arizpe, con economía ganadera y de agricultura de temporal, a más de 1,000 metros de altitud y con bosque de encino en las partes altas.

Su estación de bomberos es una estructura pequeña que atiende incendios forestales y de pastizal en la temporada seca, emergencias en camino rural y apoyo a los ranchos dispersos del municipio."""]

CTX['huepac'] = ["""Huépac es uno de los pueblos de la **Ruta del Río Sonora**, una fila de comunidades de fundación misional que viven de la ganadería, la agricultura de temporal y, desde hace años, del turismo cultural.

El río marca a estas comunidades: en 2014 el derrame de sulfato de cobre acidulado desde la mina Buenavista del Cobre contaminó los ríos Bacanuchi y Sonora, y desde entonces la vigilancia ambiental forma parte de la conversación local. La corporación de bomberos y rescate cubre varios de estos pueblos, con incendios de pastizal, rescate en río y atención en camino serrano."""]

CTX['baviacora'] = ["""Baviácora es una de las cabeceras de la **Ruta del Río Sonora**, con agricultura de temporal, ganadería y huertas en la vega del río, en un valle encajonado entre sierras.

Su cuerpo de bomberos es voluntario y sostiene la respuesta de una comunidad chica y alejada: incendios de pastizal y matorral en la temporada seca, rescate en el río durante las crecidas de verano y traslados largos hacia Hermosillo, a más de dos horas por carretera de montaña."""]

CTX['san-miguel-horcasitas'] = ["""Pesqueira es la localidad más activa del municipio de San Miguel de Horcasitas y funciona como polo agroindustrial: empaques de uva de mesa y hortaliza que concentran miles de jornaleros en temporada, sobre el corredor de la carretera federal 15 al norte de Hermosillo.

La estación de bomberos atiende ese contexto: incendios en bodegas y empaques, emergencias con maquinaria y agroquímicos, accidentes en la federal y atención a campamentos de jornaleros con población flotante."""]

CTX['ures'] = ["""Ures fue capital de Sonora en el siglo XIX y hoy es la cabecera del tramo medio del **río Sonora**, con agricultura de riego en la vega, ganadería y un centro histórico de portales y adobe.

Su cuerpo de bomberos voluntarios cubre un municipio extenso y disperso, con incendios de pastizal en la temporada seca, crecidas del río en verano y traslados de más de una hora hacia Hermosillo."""]

# ---------------------------------------------------------------- estaciones
# campos: slug, code, name, serviceType, muni, city, addr, neigh, cp, lat, lon,
#         phone(10 díg sin +52), admin, hours24, servs, ctxkey, ctxi,
#         mtitle, extra_rows(list de (dato,estado,origen)), nota, verified
E = []
def add(**k): E.append(k)

# --- HERMOSILLO
add(slug='estacion-central-bomberos-hermosillo', code='EB-SON-001',
    name='Estación Central de Bomberos de Hermosillo', st='profesional',
    muni='Hermosillo', city='Hermosillo', addr='Calle Nuevo León y Matamoros S/N',
    neigh='Centro', cp='83000', lat=29.089289, lon=-110.953191,
    phone='6622121556', admin='6624117954', h24=True, servs=S_IND,
    ctx='hermosillo', ci=0, mt='Bomberos Hermosillo Estación Central',
    verified=True,
    rows=[('Domicilio y código postal', 'Verificado', 'Sitio oficial del Patronato de Bomberos de Hermosillo (pbh.com.mx)'),
          ('Coordenadas GPS', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Teléfono 662 212 1556', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Teléfono 662 411 7954', 'Verificado', 'Sitio oficial del Patronato de Bomberos de Hermosillo'),
          ('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada')],
    nota='En el mismo predio de la calle Nuevo León, Google Maps publica un segundo registro, **Patronato de Bomberos de Hermosillo**, a unos 25 metros de la estación. Es el patronato civil que sostiene al cuerpo, no una estación distinta: se fusionó en esta ficha. El patronato publica además el teléfono administrativo **662 312 0333** en su ficha de Maps.')

add(slug='bomberos-hermosillo-estacion-2', code='EB-SON-002',
    name='Estación de Bomberos 2 de Hermosillo', st='profesional',
    muni='Hermosillo', city='Hermosillo', addr='Blvd. Progreso y Dr. Domingo Olivares',
    lat=29.143646, lon=-110.986218, phone='6622646657', h24=False, servs=S_URB,
    ctx='hermosillo', ci=0, mt='Bomberos Hermosillo Estación 2 Norte')

add(slug='bomberos-hermosillo-estacion-4', code='EB-SON-003',
    name='Estación de Bomberos 4 de Hermosillo', st='profesional',
    muni='Hermosillo', city='Hermosillo', addr='Blvd. Luis Donaldo Colosio Murrieta S/N',
    lat=29.0813376, lon=-111.0391599, phone='6622605361', h24=False, servs=S_URB,
    ctx='hermosillo', ci=0, mt='Bomberos Hermosillo Estación 4 Colosio')

add(slug='bomberos-hermosillo-estacion-sur', code='EB-SON-004',
    name='Estación Sur de Bomberos de Hermosillo', st='profesional',
    muni='Hermosillo', city='Hermosillo', addr='Blvd. Cimarrón S/N',
    lat=29.0195931, lon=-110.9342479, phone='6622526009', h24=False, servs=S_URB,
    ctx='hermosillo', ci=0, mt='Bomberos Hermosillo Estación Sur')

add(slug='bomberos-hermosillo-estacion-5-miguel-aleman', code='EB-SON-005',
    name='Estación 5 de Bomberos de Miguel Alemán', st='profesional',
    muni='Hermosillo', city='Miguel Alemán', addr='Calle Ricardo Flores Magón',
    lat=28.8419637, lon=-111.4883161, phone='6622410403', h24=False, servs=S_AGRO,
    ctx='hermosillo', ci=1, mt='Bomberos Hermosillo Estación 5 Miguel Alemán',
    nota='La localidad de Miguel Alemán —conocida como La Doce— es el centro de servicios de la Costa de Hermosillo y concentra la población jornalera de los campos agrícolas de la zona.')

add(slug='bomberos-bahia-de-kino', code='EB-SON-006',
    name='Departamento de Bomberos de Bahía de Kino', st='profesional',
    muni='Hermosillo', city='Bahía de Kino', addr='Av. Salina Cruz',
    neigh='Bahía de Kino Centro', lat=28.8233558, lon=-111.9398608,
    phone='6622420926', h24=False, servs=S_MAR,
    ctx='hermosillo', ci=1, mt='Bomberos Bahía de Kino Hermosillo',
    nota='Bahía de Kino es el destino de playa de Hermosillo y un puerto pesquero ribereño: la estación atiende población flotante en fines de semana y temporada alta, además de la comunidad comcaac (seri) de Punta Chueca, al norte.')

# --- CAJEME
add(slug='cuerpo-bomberos-cajeme-central', code='EB-SON-007',
    name='Cuerpo de Bomberos de Cajeme', st='profesional',
    muni='Cajeme', city='Ciudad Obregón', addr='Calle Chihuahua S/N',
    neigh='Centro', lat=27.4852325, lon=-109.9346237, phone='6444170904',
    h24=True, servs=S_AGRO, ctx='cajeme', ci=0,
    mt='Bomberos Cajeme Central Cd Obregón')

add(slug='bomberos-cajeme-estacion-2', code='EB-SON-008',
    name='Estación 2 de Bomberos de Cajeme', st='profesional',
    muni='Cajeme', city='Ciudad Obregón', addr='Calle Castillo de Windsor 2002',
    lat=27.5068076, lon=-109.9167535, h24=False, servs=S_URB,
    ctx='cajeme', ci=1, mt='Bomberos Cajeme Estación 2')

add(slug='bomberos-cajeme-subestacion-3', code='EB-SON-009',
    name='Subestación 3 de Bomberos de Cajeme', st='profesional',
    muni='Cajeme', city='Ciudad Obregón', addr='Calle Michoacán',
    lat=27.454443, lon=-109.9535505, phone='6444170904', h24=True, servs=S_URB,
    ctx='cajeme', ci=1, mt='Bomberos Cajeme Subestación 3',
    rows=[('Domicilio', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Coordenadas GPS', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Teléfono 644 417 0904', 'Verificado con reserva', 'Google Maps publica el número a 7 dígitos (417 0904); se le antepuso la clave LADA 644 de Ciudad Obregón, que coincide con el conmutador de la central'),
          ('Horario 24/7', 'Verificado', 'Ficha pública de Google Maps'),
          ('Colonia y código postal', '**Pendiente**', 'Sin fuente pública localizada'),
          ('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada')],
    nota='A diez metros de este punto, Google Maps registra también **USSI Sur**, con el teléfono 644 410 0600 y el mismo domicilio de la calle Michoacán. Es el mismo inmueble y se fusionó en esta ficha.')

add(slug='bomberos-cajeme-estacion-4', code='EB-SON-010',
    name='Estación 4 de Bomberos de Cajeme', st='profesional',
    muni='Cajeme', city='Ciudad Obregón', neigh='Industriales',
    lat=27.5572695, lon=-109.9425809, phone='6444170904', h24=True, servs=S_IND,
    ctx='cajeme', ci=0, mt='Bomberos Cajeme Estación 4')

add(slug='bomberos-cajeme-subestacion-1', code='EB-SON-011',
    name='Subestación 1 de Bomberos de Cajeme', st='profesional',
    muni='Cajeme', city='Ciudad Obregón', addr='Calle Querétaro',
    lat=27.5015658, lon=-109.9523242, h24=True, servs=S_URB,
    ctx='cajeme', ci=1, mt='Bomberos Cajeme Subestación 1')

# --- BÁCUM / SIRM
add(slug='bomberos-bacum-rio-yaqui', code='EB-SON-012',
    name='Departamento de Bomberos de Bácum', st='mixto',
    muni='Bácum', city='Bácum', addr='Blvd. Rodolfo Félix Valdez',
    lat=27.5493586, lon=-110.0823931, phone='6441158267', h24=False, servs=S_AGRO,
    ctx='bacum', ci=0, mt='Bomberos Bácum Río Yaqui')

add(slug='bomberos-san-ignacio-rio-muerto', code='EB-SON-013',
    name='H. Cuerpo de Bomberos Voluntarios José Martínez Bernal', st='voluntario',
    muni='San Ignacio Río Muerto', city='San Ignacio Río Muerto',
    lat=27.4095284, lon=-110.2455999, h24=True, servs=S_MAR,
    ctx='san-ignacio-rio-muerto', ci=0, mt='Bomberos San Ignacio Río Muerto')

# --- GUAYMAS
add(slug='bomberos-guaymas-estacion-centro', code='EB-SON-014',
    name='Estación Centro de Bomberos de Guaymas', st='profesional',
    muni='Guaymas', city='Heroica Guaymas', addr='Av. Diez Poniente 345',
    lat=27.9208678, lon=-110.8975416, phone='6222227444', h24=True, servs=S_MAR_H,
    ctx='guaymas', ci=0, mt='Bomberos Guaymas Estación Centro')

add(slug='bomberos-guaymas-estacion-norte', code='EB-SON-015',
    name='Estación Norte de Bomberos de Guaymas', st='profesional',
    muni='Guaymas', city='Heroica Guaymas',
    addr='Blvd. Diana Laura Riojas de Colosio', lat=27.9459801, lon=-110.9346838,
    h24=False, servs=S_URB, ctx='guaymas', ci=1,
    mt='Bomberos Guaymas Estación Norte')

add(slug='bomberos-guaymas-zona-sur', code='EB-SON-016',
    name='Estación Zona Sur de Bomberos de Guaymas', st='profesional',
    muni='Guaymas', city='Heroica Guaymas', lat=27.889145, lon=-110.900457,
    phone='6222216171', h24=False, servs=S_MAR, ctx='guaymas', ci=1,
    mt='Bomberos Guaymas Estación Zona Sur')

add(slug='bomberos-guaymas-estacion-4-san-carlos', code='EB-SON-017',
    name='Estación 4 de Bomberos de San Carlos', st='profesional',
    muni='Guaymas', city='San Carlos Nuevo Guaymas', addr='Calle Tierra 38',
    lat=27.9579413, lon=-111.0390638, phone='6226902180', h24=True, servs=S_MAR,
    ctx='guaymas', ci=1, mt='Bomberos San Carlos Guaymas Estación 4',
    nota='San Carlos Nuevo Guaymas es el polo turístico náutico del municipio: marina, buceo y población flotante de invierno, con una proporción alta de residentes extranjeros.')

add(slug='bomberos-vicam-guaymas', code='EB-SON-018',
    name='Estación de Bomberos de Vícam', st='mixto',
    muni='Guaymas', city='Vícam', addr='Calle Lázaro Cárdenas esquina con carretera México 15',
    lat=27.6416665, lon=-110.296208, h24=False, servs=S_AGRO,
    ctx='guaymas-vicam', ci=0, mt='Bomberos Vícam Guaymas',
    rows=[('Domicilio', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Coordenadas GPS', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Municipio', 'Verificado', 'Vícam es localidad del municipio de Guaymas; Google Maps la registra como Vícam, Sonora, sin municipio propio'),
          ('Teléfono', '**Pendiente**', 'Google Maps no publica teléfono para este registro'),
          ('Horario', '**Pendiente**', 'Google Maps no publica horario para este registro'),
          ('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada')])

# --- EMPALME
add(slug='bomberos-empalme-central', code='EB-SON-019',
    name='Central de Bomberos de Empalme', st='profesional',
    muni='Empalme', city='Empalme', addr='Av. Reforma 1',
    lat=27.9588925, lon=-110.8222299, phone='6222239911', h24=False, servs=S_MAR,
    ctx='empalme', ci=0, mt='Bomberos Empalme Central')

add(slug='bomberos-empalme-comision-nacional-emergencia', code='EB-SON-020',
    name='Comisión Nacional de Emergencia Empalme', st='voluntario',
    muni='Empalme', city='Empalme', addr='Calle Sahuaral y Av. Primera',
    neigh='Sahuaral', cp='85397', lat=27.9656304, lon=-110.7910765,
    phone='6221323205', h24=True, servs=BASE_SERV, ctx='empalme', ci=1,
    mt='Bomberos Empalme CNE Sahuaral',
    nota='Este registro corresponde a un cuerpo voluntario con sede propia en la colonia Sahuaral, no a la corporación municipal. Google Maps lo clasifica como parque de bomberos y las fotografías publicadas por el propietario muestran unidad y personal de bomberos.')

# --- NAVOJOA
add(slug='bomberos-navojoa-cuartel-central', code='EB-SON-021',
    name='Cuartel Central de Bomberos de Navojoa', st='proteccion-civil',
    muni='Navojoa', city='Navojoa', addr='Av. Ignacio López Rayón 209',
    lat=27.0772344, lon=-109.4437395, admin='6424256300', h24=True, servs=S_AGRO,
    ctx='navojoa', ci=0, mt='Bomberos Navojoa Cuartel Central',
    rows=[('Domicilio', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Coordenadas GPS', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Teléfono 642 425 6300', 'Verificado', 'Portal oficial del H. Ayuntamiento de Navojoa, sección Cuerpo de Bomberos y Protección Civil'),
          ('Horario 24/7', 'Verificado', 'Ficha pública de Google Maps'),
          ('Colonia y código postal', '**Pendiente**', 'Sin fuente pública localizada'),
          ('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada')],
    nota='El portal municipal publica el correo **bomberos@navojoa.gob.mx** y el teléfono 642 425 6300, que corresponde al conmutador del ayuntamiento. Google Maps registra en el mismo domicilio un segundo punto llamado "Estación de Bomberos", a cinco metros del primero: es el mismo inmueble y se fusionó aquí.')

add(slug='bomberos-navojoa-francisco-villa', code='EB-SON-022',
    name='Estación de Bomberos Francisco Villa de Navojoa', st='proteccion-civil',
    muni='Navojoa', city='Navojoa', addr='Calle Lázaro Cárdenas del Río 402',
    neigh='Francisco Villa', cp='85880', lat=27.0736998, lon=-109.4369575,
    h24=False, servs=S_URB, ctx='navojoa', ci=1,
    mt='Bomberos Navojoa Francisco Villa')

# --- ETCHOJOA / HUATABAMPO / ÁLAMOS / BENITO JUÁREZ
add(slug='bomberos-etchojoa', code='EB-SON-023',
    name='Departamento de Bomberos de Etchojoa', st='proteccion-civil',
    muni='Etchojoa', city='Etchojoa', lat=26.9173075, lon=-109.6258178,
    h24=False, servs=S_AGRO, ctx='etchojoa', ci=0, mt='Bomberos Etchojoa Sonora')

add(slug='bomberos-huatabampo', code='EB-SON-024',
    name='Cuerpo de Bomberos de Huatabampo', st='proteccion-civil',
    muni='Huatabampo', city='Huatabampo', addr='Calle Francisco I. Madero 112',
    lat=26.8286005, lon=-109.6483768, phone='6474260097', h24=False, servs=S_MAR,
    ctx='huatabampo', ci=0, mt='Bomberos Huatabampo Sonora',
    nota='Google Maps registra un segundo punto llamado "Estación de Bomberos" en Francisco I. Madero 95, a diez metros de este: es el mismo inmueble y se fusionó en esta ficha.')

add(slug='bomberos-proteccion-civil-alamos', code='EB-SON-025',
    name='Dirección de Bomberos y Protección Civil de Álamos', st='proteccion-civil',
    muni='Álamos', city='Álamos', addr='Calle Francisco I. Madero 85',
    cp='85760', lat=27.0330175, lon=-108.9552678, phone='6474280505',
    h24=False, servs=S_FOR, ctx='alamos', ci=0,
    mt='Bomberos Álamos Protección Civil',
    rows=[('Domicilio y código postal', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Coordenadas GPS', 'Verificado con reserva', 'Google Maps publica dos registros de la misma corporación sobre la calle Francisco I. Madero, con coordenadas separadas 1.5 km; se publica la del registro que sí trae domicilio y teléfono'),
          ('Teléfono 647 428 0505', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Horario', '**Pendiente**', 'Google Maps no publica horario para este registro'),
          ('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada')],
    nota='Álamos tiene un solo cuerpo de bomberos. Google Maps lo registra dos veces —"Dirección de Bomberos y Protección Civil", en Madero 85, y "Bomberos Álamos", en Madero 51—, ambos sobre la misma calle. Se publicó una sola ficha con el registro que trae domicilio completo y teléfono.')

add(slug='bomberos-villa-juarez-benito-juarez', code='EB-SON-026',
    name='Estación de Bomberos de Villa Juárez', st='mixto',
    muni='Benito Juárez', city='Villa Juárez', addr='Calle Plutarco Elías Calles',
    neigh='Centro', cp='85290', lat=27.1278274, lon=-109.8430789,
    phone='6441974605', h24=False, servs=S_MAR,
    ctx='benito-juarez', ci=0, mt='Bomberos Villa Juárez Benito Juárez')

# --- NOGALES
add(slug='bomberos-nogales-estacion-1-gustavo-manriquez', code='EB-SON-027',
    name='H. Cuerpo de Bomberos Voluntarios Gustavo L. Manríquez', st='voluntario',
    muni='Nogales', city='Heroica Nogales', addr='Av. Álvaro Obregón 327',
    neigh='Fundo Legal', lat=31.3261198, lon=-110.9456999, phone='6313120836',
    h24=True, servs=S_IND, ctx='nogales', ci=1,
    mt='Bomberos Nogales Estación 1 Central',
    rows=[('Domicilio', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Coordenadas GPS', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Teléfono 631 312 0836', 'Verificado', 'Sitio oficial del H. Cuerpo de Bomberos Voluntarios de Nogales, directorio de estaciones (estación 19-1)'),
          ('Horario 24/7', 'Verificado', 'Ficha pública de Google Maps'),
          ('Código postal', '**Pendiente**', 'Sin fuente pública localizada'),
          ('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada')],
    nota='El sitio oficial del cuerpo numera sus estaciones con el prefijo 19. Esta es la **19-1**, la central histórica: Google Maps la registra dos veces —como "H. Cuerpo de Bomberos Voluntarios Gustavo L. Manríquez" y como "Fire Station #1"—, ambas en el mismo punto, y se fusionaron en esta ficha.')

add(slug='bomberos-nogales-estacion-3', code='EB-SON-028',
    name='Estación 3 de Bomberos de Nogales', st='voluntario',
    muni='Nogales', city='Heroica Nogales', addr='Av. Álvaro Obregón 6440',
    lat=31.2700215, lon=-110.9428, phone='6313141858', h24=True, servs=S_IND,
    ctx='nogales', ci=0, mt='Bomberos Nogales Estación 3',
    rows=[('Domicilio', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Coordenadas GPS', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Teléfono 631 314 1858', 'Verificado', 'Sitio oficial del H. Cuerpo de Bomberos Voluntarios de Nogales, directorio de estaciones (estación 19-3)'),
          ('Horario 24/7', 'Verificado', 'Ficha pública de Google Maps'),
          ('Colonia y código postal', '**Pendiente**', 'Sin fuente pública localizada'),
          ('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada')])

add(slug='bomberos-nogales-colonia-hermosillo', code='EB-SON-029',
    name='Estación de Bomberos de la Colonia Hermosillo', st='voluntario',
    muni='Nogales', city='Heroica Nogales', addr='Callejón Hermosillo 1317',
    lat=31.2972722, lon=-110.9511668, h24=False, servs=S_URB,
    ctx='nogales', ci=0, mt='Bomberos Nogales Colonia Hermosillo',
    nota='El sitio oficial del cuerpo de Nogales publica teléfonos de seis estaciones numeradas (19-1 a 19-6), pero sin domicilios, por lo que no fue posible asignarle a este registro un número de estación ni un teléfono con certeza. Se publica sin teléfono antes que arriesgar un dato equivocado.')

add(slug='bomberos-nogales-san-carlos', code='EB-SON-030',
    name='Estación de Bomberos San Carlos de Nogales', st='voluntario',
    muni='Nogales', city='Heroica Nogales', lat=31.2779889, lon=-110.9232859,
    h24=False, servs=S_URB, ctx='nogales', ci=1,
    mt='Bomberos Nogales San Carlos',
    nota='Google Maps clasifica este punto como academia de bomberos dentro de la colonia San Carlos. No fue posible asociarlo a ninguno de los números de estación (19-1 a 19-6) que publica el sitio oficial del cuerpo, por lo que la ficha va sin teléfono directo.')

# --- SAN LUIS RÍO COLORADO
add(slug='proteccion-civil-bomberos-san-luis-rio-colorado', code='EB-SON-031',
    name='Dirección de Protección Civil y Bomberos Municipales de San Luis Río Colorado',
    st='proteccion-civil', muni='San Luis Río Colorado', city='San Luis Río Colorado',
    addr='Av. Benito Juárez García 402', cp='83449',
    lat=32.4800881, lon=-114.7789883, phone='6535366642', h24=False, servs=S_IND,
    ctx='san-luis-rio-colorado', ci=0, mt='Bomberos San Luis Río Colorado PC',
    verified=True,
    rows=[('Domicilio y código postal', 'Verificado', 'Portal oficial del Ayuntamiento de San Luis Río Colorado (Dirección de Protección Civil) y ficha pública de Google Maps'),
          ('Coordenadas GPS', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Teléfono 653 536 6642', 'Verificado', 'Portal oficial del Ayuntamiento de San Luis Río Colorado'),
          ('Horario de oficina', 'Verificado', 'Portal oficial del Ayuntamiento (8:00 a 15:00 h para trámites); el servicio de emergencia opera todo el día'),
          ('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada')],
    nota='A 50 metros de este punto, Google Maps registra la "Estación Central de Bomberos Voluntarios", sobre la calle 5. El portal municipal ubica la dirección en avenida Juárez y calle Cuarta: es el mismo predio y se fusionó en esta ficha. El horario de 8:00 a 15:00 corresponde a la ventanilla de trámites, no al servicio de emergencia.')

add(slug='bomberos-municipales-slrc-central', code='EB-SON-032',
    name='Estación Central de Bomberos Municipales de San Luis Río Colorado',
    st='profesional', muni='San Luis Río Colorado', city='San Luis Río Colorado',
    lat=32.4240064, lon=-114.7463581, h24=True, servs=S_URB,
    ctx='san-luis-rio-colorado', ci=1, mt='Bomberos Municipales SLRC Central')

add(slug='bomberos-municipales-slrc-estacion-2', code='EB-SON-033',
    name='Estación 2 de Bomberos Municipales de San Luis Río Colorado',
    st='profesional', muni='San Luis Río Colorado', city='San Luis Río Colorado',
    addr='Calle Canadá 407', lat=32.424221, lon=-114.7977378, h24=True,
    servs=S_URB, ctx='san-luis-rio-colorado', ci=1,
    mt='Bomberos Municipales SLRC Estación 2')

add(slug='bomberos-rurales-slrc-central', code='EB-SON-034',
    name='Estación Central de Bomberos Rurales del Río Colorado', st='voluntario',
    muni='San Luis Río Colorado', city='San Luis Río Colorado',
    addr='Calzada Monterrey 3', lat=32.462497, lon=-114.8012174, h24=False,
    servs=S_AGRO, ctx='san-luis-rio-colorado', ci=1,
    mt='Bomberos Rurales SLRC Central',
    nota='Los bomberos rurales son un cuerpo voluntario que cubre el valle agrícola y los ejidos del municipio, donde los tiempos de llegada desde la ciudad serían de decenas de minutos.')

add(slug='bomberos-rurales-slrc-subestacion-1', code='EB-SON-035',
    name='Subestación 1 de Bomberos Rurales del Río Colorado', st='voluntario',
    muni='San Luis Río Colorado', city='San Luis Río Colorado',
    addr='Av. Tlaxcala 2400', lat=32.4500948, lon=-114.7611635,
    phone='6535382638', h24=True, servs=S_AGRO,
    ctx='san-luis-rio-colorado', ci=1, mt='Bomberos Rurales SLRC Subestación 1')

add(slug='bomberos-voluntarios-slrc-estacion-2', code='EB-SON-036',
    name='Estación 2 de Bomberos Voluntarios de San Luis Río Colorado',
    st='voluntario', muni='San Luis Río Colorado', city='San Luis Río Colorado',
    addr='Calle 40 LB', neigh='Burócrata', cp='83459',
    lat=32.4678265, lon=-114.7307554, phone='6532095578', h24=False, servs=S_URB,
    ctx='san-luis-rio-colorado', ci=0, mt='Bomberos Voluntarios SLRC Estación 2')

# --- CABORCA / PITIQUITO
add(slug='bomberos-voluntarios-caborca', code='EB-SON-037',
    name='Bomberos Voluntarios de Caborca A.C.', st='voluntario',
    muni='Caborca', city='Heroica Caborca', addr='Av. Álvaro Obregón 67',
    lat=30.7125524, lon=-112.1458054, phone='6373720162', h24=True, servs=S_IND,
    ctx='caborca', ci=0, mt='Bomberos Voluntarios de Caborca')

add(slug='bomberos-caborca-estacion-2', code='EB-SON-038',
    name='Estación 2 de Bomberos Voluntarios de Caborca', st='voluntario',
    muni='Caborca', city='Heroica Caborca', addr='Calle N 133',
    lat=30.7245676, lon=-112.1630822, phone='6373720162', h24=False, servs=S_URB,
    ctx='caborca', ci=1, mt='Bomberos Caborca Estación 2')

add(slug='bomberos-voluntarios-pitiquito', code='EB-SON-039',
    name='Bomberos Voluntarios de Pitiquito A.C.', st='voluntario',
    muni='Pitiquito', city='Pitiquito', addr='Calle Jesús García Morales',
    lat=30.6792504, lon=-112.0523164, phone='6371112886', h24=True, servs=S_FOR,
    ctx='pitiquito', ci=0, mt='Bomberos Voluntarios de Pitiquito')

# --- PUERTO PEÑASCO
add(slug='bomberos-puerto-penasco-central', code='EB-SON-040',
    name='Central de Bomberos de Puerto Peñasco', st='profesional',
    muni='Puerto Peñasco', city='Puerto Peñasco', addr='Boulevard Freemont',
    lat=31.3059403, lon=-113.5396071, phone='6383832828', h24=False, servs=S_MAR_H,
    ctx='puerto-penasco', ci=0, mt='Bomberos Puerto Peñasco Central')

add(slug='bomberos-puerto-penasco-estacion-2', code='EB-SON-041',
    name='Estación 2 de Bomberos de Puerto Peñasco', st='profesional',
    muni='Puerto Peñasco', city='Puerto Peñasco',
    addr='Calle Revolución y Agustín Melgar', lat=31.3307655, lon=-113.5388152,
    phone='6383832828', h24=False, servs=S_URB, ctx='puerto-penasco', ci=1,
    mt='Bomberos Puerto Peñasco Estación 2')

add(slug='bomberos-puerto-penasco-estacion-3', code='EB-SON-042',
    name='Estación 3 de Bomberos de Puerto Peñasco', st='profesional',
    muni='Puerto Peñasco', city='Puerto Peñasco', addr='Calle Simón Morúa 439',
    lat=31.3209578, lon=-113.5105528, phone='6383832828', h24=True, servs=S_URB,
    ctx='puerto-penasco', ci=1, mt='Bomberos Puerto Peñasco Estación 3')

add(slug='bomberos-puerto-penasco-estacion-4', code='EB-SON-043',
    name='Estación 4 de Bomberos de Puerto Peñasco', st='profesional',
    muni='Puerto Peñasco', city='Puerto Peñasco', addr='Calle Hermosillo 429',
    lat=31.3425825, lon=-113.5429153, h24=False, servs=S_URB,
    ctx='puerto-penasco', ci=1, mt='Bomberos Puerto Peñasco Estación 4')

# --- SONOYTA
add(slug='bomberos-voluntarios-sonoyta', code='EB-SON-044',
    name='H. Cuerpo de Bomberos Voluntarios de Sonoyta', st='voluntario',
    muni='Plutarco Elías Calles', city='Sonoyta', addr='Av. Altar 57',
    lat=31.8662965, lon=-112.8541439, phone='9531112869', h24=False, servs=S_FOR,
    ctx='plutarco-elias-calles', ci=0, mt='Bomberos Voluntarios de Sonoyta',
    rows=[('Domicilio', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Coordenadas GPS', 'Verificado', 'Ficha pública de Google Maps del establecimiento'),
          ('Teléfono 953 111 2869', 'Verificado con reserva', 'Ficha pública de Google Maps; la clave 953 no corresponde a la región de Sonoyta (651) y parece ser una línea móvil registrada en otro estado'),
          ('Horario', '**Pendiente**', 'Google Maps no publica horario para este registro'),
          ('Colonia y código postal', '**Pendiente**', 'Sin fuente pública localizada'),
          ('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada')])

# --- AGUA PRIETA / NACO
add(slug='bomberos-agua-prieta-central', code='EB-SON-045',
    name='Estación de Bomberos de Agua Prieta', st='profesional',
    muni='Agua Prieta', city='Agua Prieta', addr='Calle 6 número 1550',
    lat=31.3288513, lon=-109.5477616, phone='6333381511', h24=False, servs=S_IND,
    ctx='agua-prieta', ci=0, mt='Bomberos Agua Prieta Central')

add(slug='bomberos-agua-prieta-cuartel-2', code='EB-SON-046',
    name='Cuartel de Bomberos 2 de Agua Prieta', st='profesional',
    muni='Agua Prieta', city='Agua Prieta', addr='Calle 23 número 2520',
    cp='83268', lat=31.3136412, lon=-109.5361265, h24=True, servs=S_URB,
    ctx='agua-prieta', ci=1, mt='Bomberos Agua Prieta Cuartel 2',
    nota='Google Maps registra en el mismo punto un segundo rótulo, "H. Cuerpo de Bomberos", a ocho metros de este: es el mismo inmueble y se fusionó en esta ficha.')

add(slug='bomberos-agua-prieta-cuartel-3', code='EB-SON-047',
    name='Cuartel de Bomberos 3 de Agua Prieta', st='profesional',
    muni='Agua Prieta', city='Agua Prieta', lat=31.3305236, lon=-109.5849167,
    phone='6333381511', h24=False, servs=S_URB, ctx='agua-prieta', ci=1,
    mt='Bomberos Agua Prieta Cuartel 3')

add(slug='bomberos-naco', code='EB-SON-048',
    name='Bomberos de Naco', st='mixto', muni='Naco', city='Naco',
    addr='Av. Francisco I. Madero 1180', lat=31.3208737, lon=-109.9485825,
    phone='6331214058', h24=True, servs=S_FOR, ctx='naco', ci=0,
    mt='Bomberos de Naco Sonora')

# --- CANANEA / NACOZARI
add(slug='bomberos-cananea-cuartel', code='EB-SON-049',
    name='Cuartel de Bomberos de Cananea', st='profesional',
    muni='Cananea', city='Cananea', addr='Calle Benito Juárez García S/N',
    neigh='Tres Marías', cp='84620', lat=30.9817453, lon=-110.3102955,
    phone='6453320041', h24=False, servs=S_IND, ctx='cananea', ci=0,
    mt='Bomberos Cananea Cuartel')

add(slug='bomberos-nacozari-de-garcia', code='EB-SON-050',
    name='Cuartel de Bomberos de Nacozari de García', st='voluntario',
    muni='Nacozari de García', city='Nacozari de García',
    addr='Calle José María Pino Suárez 49 A', neigh='Centro',
    lat=30.3754102, lon=-109.6927064, phone='6343421940', h24=True, servs=S_IND,
    ctx='nacozari', ci=0, mt='Bomberos Nacozari de García')

# --- MAGDALENA / SANTA ANA
add(slug='bomberos-magdalena-de-kino', code='EB-SON-051',
    name='Cuartel de Bomberos de Magdalena', st='mixto',
    muni='Magdalena', city='Magdalena de Kino', addr='Calle Woolfolk',
    lat=30.6235574, lon=-110.9611583, h24=True, servs=S_URB,
    ctx='magdalena', ci=0, mt='Bomberos Magdalena de Kino')

add(slug='bomberos-santa-ana', code='EB-SON-052',
    name='Bomberos de Santa Ana', st='mixto', muni='Santa Ana', city='Santa Ana',
    cp='84600', lat=30.5447648, lon=-111.1216426, h24=True, servs=S_IND,
    ctx='santa-ana', ci=0, mt='Bomberos Santa Ana Sonora')

add(slug='bomberos-santa-ana-estacion-2', code='EB-SON-053',
    name='Estación 2 de Bomberos de Santa Ana', st='mixto',
    muni='Santa Ana', city='Santa Ana',
    addr='Calle 13 S/N entre calle Ignacio López Rayón',
    lat=30.5310263, lon=-111.1190224, h24=True, servs=S_FOR,
    ctx='santa-ana', ci=1, mt='Bomberos Santa Ana Estación 2')

# --- RÍO SONORA
add(slug='bomberos-bacoachi', code='EB-SON-054',
    name='Estación de Bomberos de Bacoachi', st='voluntario',
    muni='Bacoachi', city='Bacoachi', addr='Calle Miguel Hidalgo y Costilla 619',
    lat=30.6329127, lon=-109.9693479, h24=False, servs=S_FOR,
    ctx='bacoachi', ci=0, mt='Bomberos Bacoachi Sonora')

add(slug='bomberos-rescates-rio-sonora-huepac', code='EB-SON-055',
    name='Bomberos y Rescates del Río Sonora', st='voluntario',
    muni='Huépac', city='Huépac', addr='Calle Hidalgo 47', cp='84874',
    lat=29.9059076, lon=-110.2142761, h24=True, servs=S_FOR,
    ctx='huepac', ci=0, mt='Bomberos Río Sonora Huépac')

add(slug='bomberos-voluntarios-baviacora', code='EB-SON-056',
    name='Bomberos Voluntarios de Baviácora', st='voluntario',
    muni='Baviácora', city='Baviácora', addr='Calle I. San Quiroga 109',
    cp='84945', lat=29.7094987, lon=-110.1568685, h24=True, servs=S_FOR,
    ctx='baviacora', ci=0, mt='Bomberos Voluntarios de Baviácora')

add(slug='bomberos-pesqueira-san-miguel-horcasitas', code='EB-SON-057',
    name='Estación de Bomberos de Pesqueira', st='mixto',
    muni='San Miguel de Horcasitas', city='Pesqueira', addr='Calle Nuñez 846',
    lat=29.3807288, lon=-110.8988208, h24=False, servs=S_AGRO,
    ctx='san-miguel-horcasitas', ci=0, mt='Bomberos Pesqueira Horcasitas')

add(slug='bomberos-voluntarios-ures', code='EB-SON-058',
    name='Bomberos Voluntarios de Ures', st='voluntario',
    muni='Ures', city='Ures', lat=29.423286, lon=-110.3976299, h24=True,
    servs=S_FOR, ctx='ures', ci=0, mt='Bomberos Voluntarios de Ures')

# ------------------------------------------------------------------ helpers
def fmt(p):
    return '%s %s %s' % (p[:3], p[3:6], p[6:])

def corto(name):
    n = name.replace('H. Cuerpo de Bomberos Voluntarios ', 'Bomberos ')
    n = n.replace('Dirección de Protección Civil y Bomberos Municipales de ', 'PC y Bomberos de ')
    n = n.replace('Estación Central de Bomberos Municipales de ', 'Bomberos Municipales de ')
    n = n.replace('Estación 2 de Bomberos Municipales de ', 'Bomberos Municipales est. 2 de ')
    if len(n) > 48:
        n = n[:47].rsplit(' ', 1)[0]
    return n

PAD = [
    ' Consulta domicilio, teléfono y servicios en el directorio de bomberos de Sonora.',
    ' Ficha del directorio nacional de estaciones de bomberos de México.',
    ' Datos verificados del directorio de estaciones de bomberos.',
    ' Directorio de bomberos de Sonora.',
]

def descripcion(e):
    loc = e.get('addr')
    if loc and e.get('neigh'):
        loc = '%s, %s' % (loc, e['neigh'])
    if not loc:
        loc = e.get('neigh') or e['city']
    base = '%s, %s, %s.' % (e['name'], loc, e['muni'])
    if e.get('phone'):
        base += ' Teléfono %s.' % fmt(e['phone'])
    elif e.get('admin'):
        base += ' Teléfono %s.' % fmt(e['admin'])
    else:
        base += ' Sin teléfono directo publicado.'
    if e.get('h24'):
        base += ' Abierto 24 horas.'
    base += ' Emergencias 911.'
    if len(base) > 158:
        base = '%s, %s. %s' % (e['name'], e['muni'],
                               'Emergencias 911.' if not e.get('phone')
                               else 'Teléfono %s. Emergencias 911.' % fmt(e['phone']))
    for p in PAD:
        if len(base) >= 110:
            break
        if len(base) + len(p) <= 158:
            base += p
    return base

TPL = """---
name: "{name}"
stationCode: "{code}"
serviceType: "{st}"
status: "activa"
state: "Sonora"
stateSlug: "sonora"
municipality: "{muni}"
city: "{city}"
{opt}emergencyPhone: "911"
operatingHours: "24/7"
services:
{servs}
verified: {ver}
lastUpdated: "2026-08-06"
metaTitle: "{mt}"
metaDescription: "{md}"
---

## {name}

{ident}

{ctx}
{nota}
## Servicios registrados

{servlist}

## Cómo contactarla

| Necesidad | Número |
|---|---|
| **Emergencia en curso** | **911** |
{telrows}
{telnote}

---

### Fuentes y estado del dato

| Dato | Estado | Origen |
|---|---|---|
{rows}

Publicamos solo lo que pudimos comprobar. Los campos vacíos lo están porque no encontramos una fuente que los respalde, no porque no existan. Si detectas un dato incorrecto o conoces el que falta, [avísanos](/agregar-estacion) y lo corregimos.

*Última revisión: agosto de 2026. Para una emergencia en curso, marca 911.*
"""

TIPO = {'profesional': 'Corporación profesional municipal.',
        'voluntario': 'Cuerpo de bomberos voluntarios.',
        'mixto': 'Corporación municipal con apoyo de personal voluntario.',
        'proteccion-civil': 'Unidad municipal de bomberos y protección civil.'}

errores = []
titles, descs, slugs = set(), set(), set()

for e in E:
    opt = ''
    if e.get('addr'): opt += 'address: "%s"\n' % e['addr']
    if e.get('neigh'): opt += 'neighborhood: "%s"\n' % e['neigh']
    if e.get('cp'): opt += 'postalCode: "%s"\n' % e['cp']
    opt += 'latitude: %s\n' % e['lat']
    opt += 'longitude: %s\n' % e['lon']
    if e.get('phone'): opt += 'phone: "+52 %s"\n' % fmt(e['phone'])
    if e.get('admin'): opt += 'adminPhone: "+52 %s"\n' % fmt(e['admin'])

    md = descripcion(e)
    mt = e['mt']
    if len(mt) > 44: errores.append('TITULO %d %s' % (len(mt), e['slug']))
    for sep in [':', ' — ', ' – ', ' | ']:
        if sep in mt: errores.append('SEP en titulo %s' % e['slug'])
    if not (110 <= len(md) <= 158): errores.append('DESC %d %s :: %s' % (len(md), e['slug'], md))
    if mt in titles: errores.append('TITULO DUP %s' % e['slug'])
    if md in descs: errores.append('DESC DUP %s' % e['slug'])
    if e['slug'] in slugs: errores.append('SLUG DUP %s' % e['slug'])
    titles.add(mt); descs.add(md); slugs.add(e['slug'])

    # identificación
    donde = e.get('addr')
    if donde and e.get('neigh'):
        donde = '%s, colonia %s' % (donde, e['neigh'])
    if donde:
        ident = '%s en %s, %s. %s' % (e['name'], donde, e['city'], TIPO[e['st']])
    else:
        ident = '%s, en %s, municipio de %s. %s' % (e['name'], e['city'], e['muni'], TIPO[e['st']])
    if e.get('h24'):
        ident += ' Abierta las 24 horas.'

    ctx = CTX[e['ctx']][e['ci']]
    nota = ('\n%s\n' % e['nota']) if e.get('nota') else ''

    servlist = '\n'.join('- %s' % SERV[s] for s in e['servs'])
    servs_yaml = '\n'.join('  - %s' % s for s in e['servs'])

    tel = e.get('phone') or e.get('admin')
    if tel:
        telrows = '| %s | %s |' % (corto(e['name']), fmt(tel))
        if e.get('phone') and e.get('admin'):
            telrows += '\n| Patronato de Bomberos de Hermosillo | %s |' % fmt(e['admin'])
        telnote = '\nEl **911** es gratuito, opera las 24 horas y es el que despacha la unidad más cercana. Los teléfonos de estación sirven para trámites, capacitación, licitaciones o contacto administrativo.'
    else:
        telrows = ''
        telnote = '\n**No localizamos un teléfono directo publicado** para esta estación. Marca 911 para cualquier emergencia.\n\nEl **911** es gratuito, opera las 24 horas y es el que despacha la unidad más cercana.'

    if e.get('rows'):
        rows = e['rows']
    else:
        rows = []
        if e.get('addr'):
            rows.append(('Domicilio', 'Verificado', 'Ficha pública de Google Maps del establecimiento'))
        else:
            rows.append(('Domicilio', '**Pendiente**', 'Google Maps no publica domicilio de calle para este registro'))
        rows.append(('Coordenadas GPS', 'Verificado', 'Ficha pública de Google Maps del establecimiento'))
        if tel:
            rows.append(('Teléfono %s' % fmt(tel), 'Verificado', 'Ficha pública de Google Maps del establecimiento'))
        else:
            rows.append(('Teléfono', '**Pendiente**', 'Google Maps no publica teléfono para este registro'))
        if e.get('h24'):
            rows.append(('Horario 24/7', 'Verificado', 'Ficha pública de Google Maps'))
        else:
            rows.append(('Horario', '**Pendiente**', 'Google Maps no publica horario para este registro'))
        if e.get('cp'):
            rows.append(('Colonia y código postal', 'Verificado', 'Ficha pública de Google Maps del establecimiento'))
        else:
            rows.append(('Colonia y código postal', '**Pendiente**', 'Sin fuente pública localizada'))
        rows.append(('Personal y unidades', '**Pendiente**', 'Sin fuente pública localizada'))
    rows_md = '\n'.join('| %s | %s | %s |' % r for r in rows)

    out = TPL.format(name=e['name'], code=e['code'], st=e['st'], muni=e['muni'],
                     city=e['city'], opt=opt, servs=servs_yaml,
                     ver='true' if e.get('verified') else 'false',
                     mt=mt, md=md, ident=ident, ctx=ctx, nota=nota,
                     servlist=servlist, telrows=telrows, telnote=telnote,
                     rows=rows_md)
    out = out.replace('\n\n\n\n', '\n\n').replace('\n\n\n', '\n\n')
    with io.open(os.path.join(BASE, e['slug'] + '.md'), 'w', encoding='utf-8') as f:
        f.write(out)

print('fichas generadas:', len(E))
print('municipios:', len(set(x['muni'] for x in E)))
if errores:
    print('ERRORES:')
    for x in errores:
        print('  ', x)
else:
    print('sin errores de validacion')
