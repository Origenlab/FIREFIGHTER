#!/usr/bin/env python3
"""Reescribe el apartado mexicano de la L3 de RIT con el resultado de revisar las 32
entidades federativas contra texto.

La ficha se publicó (14bb31c) diciendo «no localizamos ninguna NOM dirigida a cuerpos de
bomberos», que era cierto pero incompleto: la investigación se había detenido en el nivel
federal. Esta pasada cierra el pendiente. Se revisaron las 32 leyes estatales de protección
civil, las cinco leyes estatales de bomberos que existen y una muestra de reglamentos
municipales. Resultado: cero requisitos de cuadrilla de intervención rápida, vigía de
control de personal, aire de rescate o regla equivalente a «dos adentro, dos afuera».

Todo lo que se afirma aquí está verificado contra el texto del ordenamiento citado.
"""
import json, collections, pathlib

RUTA = pathlib.Path(__file__).resolve().parent.parent / 'src/data/productos.json'

SECCION = collections.OrderedDict([
    ('id', 'mexico'),
    ('eyebrow', 'Revisamos las 32 entidades'),
    ('titulo', 'Ninguna ley mexicana exige cuadrilla de rescate, y una la quitó'),
    ('parrafos', [
        'La ficha se publicó diciendo que no localizábamos obligación mexicana, con la '
        'investigación detenida en el nivel federal. Cerramos el pendiente: revisamos contra '
        'texto las <strong>32 leyes estatales de protección civil</strong>, las cinco leyes '
        'estatales de bomberos que existen en el país y una muestra de reglamentos municipales. '
        'El resultado es claro y conviene publicarlo tal cual, porque nadie más lo tiene: '
        '<strong>ninguna norma mexicana exige una cuadrilla de intervención rápida, un vigía de '
        'control de personal en la entrada, equipo de aire de rescate, ni nada equivalente a la '
        'regla de «dos adentro, dos afuera»</strong>. Cero, en las 32.',
        'El concepto aparece literalmente <strong>una sola vez en todo el derecho mexicano '
        'localizable</strong>, en la ley de bomberos de Chihuahua de 2021, y aparece como '
        'facultad: los cuerpos <em>podrán</em> recurrir a personal con habilidades '
        'especializadas en intervención rápida. Podrán, no deberán. Esa misma ley es la única '
        'que fija una dotación mínima —<strong>pelotón de al menos tres personas por '
        'unidad</strong>—, pero es tripulación por vehículo, no una condición para entrar a una '
        'estructura.',
        'Hay un dato que ordena todo lo anterior mejor que cualquier argumento: <strong>en 2017 '
        'un municipio fronterizo derogó los artículos de su reglamento que obligaban al '
        'ayuntamiento a entregar equipo de respiración autónoma a cada bombero cada año</strong>. '
        'La obligación existía, con ese nombre y con plazo, y se quitó. En su lugar quedó una '
        'redacción genérica de equipo de protección personal. Vale la pena saberlo porque la '
        'versión derogada sigue circulando en portales secundarios y se cita como vigente.',
    ]),
    ('tabla', {
        'head': ['Lo que sí encontramos', 'Dónde', 'Qué tan exigible es'],
        'rows': [
            ['«Intervención rápida» como habilidad del personal',
             'Ley estatal de bomberos, Chihuahua 2021',
             'Potestativo: dice <strong>podrán</strong>, no deberán'],
            ['Pelotón de al menos tres personas por unidad',
             'Misma ley, Chihuahua',
             'Obligatorio, pero es tripulación, no regla de entrada'],
            ['Equipo de respiración autónoma nombrado como EPP',
             'Reglamento municipal, Sinaloa',
             'Debilitado por «en la medida de sus posibilidades»'],
            ['EPP certificado bajo normas nacionales o internacionales',
             'Ley estatal, Baja California',
             'Único mandato de certificación, acotado a materiales peligrosos'],
            ['EPP cada dos años y sin costo',
             'Ley estatal de bomberos, Estado de México 2021',
             'La única con periodicidad exigible. No nombra el ERA'],
            ['Lista taxativa de equipo obligatorio del bombero',
             'Reglamento municipal, Quintana Roo',
             'Enumera seis piezas y <strong>el ERA no está entre ellas</strong>'],
        ],
    }),
    ('nota',
     'El vacío es más profundo de lo que parece: en <strong>seis entidades la palabra «bombero» '
     'no aparece una sola vez</strong> en su ley de protección civil, y solo cinco estados tienen '
     'ley específica de bomberos —una de ellas es de 1948 y aplica a un municipio—. Donde la ley '
     'existe, suele remitir la seguridad del personal a los reglamentos municipales, y esos '
     'reglamentos casi siempre no la desarrollan.'),
])

SECCION_2 = collections.OrderedDict([
    ('id', 'mexico-exigible'),
    ('eyebrow', 'Entonces qué sí se puede exigir'),
    ('titulo', 'La obligación mexicana existe, pero cambia de sujeto'),
    ('parrafos', [
        'Que no haya norma dirigida al cuerpo de bomberos no significa que no haya nada '
        'exigible: significa que <strong>el obligado es otro</strong>. En el trabajo en espacios '
        'confinados la <strong>NOM-033-STPS</strong> obliga al <strong>patrón de un centro de '
        'trabajo</strong>, y ahí sí hay numerales. Exige designar <strong>al menos un vigía</strong> '
        'que permanezca fuera del espacio durante todo el trabajo, en comunicación con quienes '
        'están adentro y con facultad de ordenar la evacuación. Exige un <strong>plan de atención '
        'a emergencias y rescate</strong> que nombre a los trabajadores designados, especifique el '
        'equipo de rescate y establezca en qué condiciones el personal de rescate —interno o '
        'externo— puede o no ingresar.',
        'Y exige lo que en la práctica equivale al despliegue de una cuadrilla: que los '
        '<strong>recursos para la atención a emergencias estén disponibles antes de iniciar los '
        'trabajos</strong>, no después. Súmele capacitación específica de la brigada de rescate, '
        'refuerzo <strong>al menos una vez al año</strong> o tras cualquier incidente, y '
        'simulacros. Es menos exigente que el marco estadounidense en número de personas, pero es '
        'lo que un inspector va a pedir, y es citable con numeral.',
        'Una advertencia sobre lo que muchos documentos traducen mal: la regla estadounidense de '
        '«dos adentro, dos afuera» <strong>ni siquiera alcanza federalmente a los bomberos '
        'municipales de aquel país</strong>. Solo les llega a través de planes estatales. Copiarla '
        'a una especificación mexicana como si fuera obligación aquí es un error que se detecta '
        'fácil y debilita todo el documento.',
    ]),
    ('lista', [
        {'t': 'Vigía permanente fuera del espacio',
         'd': 'Designación por escrito y constancia de capacitación. Es la figura mexicana más '
              'cercana al control de personal en la entrada.'},
        {'t': 'Plan de rescate con personal nombrado',
         'd': 'Nombres, funciones y <strong>equipo de rescate</strong> asignado. Admite '
              'expresamente que el rescate lo preste un servicio externo.'},
        {'t': 'Recursos disponibles antes de iniciar',
         'd': 'Verificación previa asentada en el permiso de entrada. Es la exigencia con más '
              'filo del marco mexicano.'},
        {'t': 'Refuerzo anual y simulacros',
         'd': 'Al menos una vez al año, y antes si hubo un incidente o accidente.'},
        {'t': 'Lo que no fija ninguna norma mexicana',
         'd': 'Número mínimo de rescatistas en sitio, tiempo de respuesta y dotación de aire de '
              'rescate. Eso queda en el criterio de cada corporación.'},
    ]),
    ('nota',
     'Cómo redactar una especificación que se sostenga: apóyela en la <strong>NOM-033-STPS</strong> '
     'para el proceso, en la ley estatal de bomberos de su entidad si existe, y cite la norma '
     'extranjera como <strong>referencia técnica del equipo</strong>, no como obligación '
     'aplicable. Pedir «cumplimiento de NFPA 1500» a un cuerpo municipal mexicano no es exigible; '
     'pedir que el ERA esté certificado y traiga su conexión de rescate, sí.'),
])

FAQ_VIEJA = '¿Hay una NOM que obligue a tener cuadrilla de intervención rápida?'
FAQ_NUEVA_Q = '¿Alguna ley mexicana obliga a tener cuadrilla de intervención rápida?'
FAQ_NUEVA_A = (
    'No. Revisamos contra texto las 32 leyes estatales de protección civil, las cinco leyes '
    'estatales de bomberos que existen en el país y una muestra de reglamentos municipales: '
    'ninguna exige cuadrilla de intervención rápida, vigía de control de personal en la entrada, '
    'equipo de aire de rescate ni nada equivalente a «dos adentro, dos afuera». El concepto '
    'aparece literalmente una sola vez, en la ley de bomberos de Chihuahua de 2021, y como '
    'facultad: los cuerpos «podrán» recurrir a personal con habilidades especializadas en '
    'intervención rápida. Tampoco hay ley general de bomberos federal. Lo que sí es exigible con '
    'numeral corresponde al patrón de un centro de trabajo en espacios confinados: vigía fuera '
    'del espacio, plan de rescate con personal nombrado y recursos disponibles antes de iniciar '
    'los trabajos.'
)

FAQ_EXTRA = {
    'q': '¿Mi estado obliga a entregar equipo de respiración autónoma?',
    'a': 'Casi con seguridad no lo nombra. En las 32 entidades encontramos un solo reglamento '
         'vigente que menciona expresamente el «equipo de respiración autónoma» como equipo de '
         'protección personal del bombero, y lo hace condicionado a que el patronato lo entregue '
         '«en la medida de sus posibilidades». Hay un caso que conviene conocer al revés: un '
         'municipio fronterizo tenía artículos que obligaban al ayuntamiento a entregar ERA cada '
         'año, y los derogó en 2017 —la versión vieja sigue circulando en portales secundarios y '
         'se cita como vigente—. Y hay un reglamento municipal con lista taxativa de equipo '
         'obligatorio donde el ERA simplemente no aparece. Lo más fuerte que localizamos son '
         'obligaciones genéricas: EPP «sin costo alguno», EPP «cuando menos cada dos años» y, en '
         'una sola entidad, EPP «certificado por normas nacionales o internacionales».'
}


def main():
    datos = json.loads(RUTA.read_text(encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    cats = datos['categorias'] if isinstance(datos, dict) else datos
    for cat in cats:
        for prod in cat.get('productos', []):
            if prod.get('slug') != 'sistemas-rit-de-rescate':
                continue
            l3 = prod['l3']
            secs = l3['secciones']
            i = next(k for k, s in enumerate(secs) if s['id'] == 'mexico')
            secs[i] = SECCION
            if not any(s['id'] == 'mexico-exigible' for s in secs):
                secs.insert(i + 1, SECCION_2)
            faqs = l3['faqs']
            j = next(k for k, f in enumerate(faqs) if f['q'] == FAQ_VIEJA)
            faqs[j] = {'q': FAQ_NUEVA_Q, 'a': FAQ_NUEVA_A}
            if not any(f['q'] == FAQ_EXTRA['q'] for f in faqs):
                faqs.insert(j + 1, FAQ_EXTRA)
            RUTA.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            print(f'secciones: {len(secs)}  ·  faqs: {len(faqs)}')
            return
    raise SystemExit('producto no encontrado')


if __name__ == '__main__':
    main()
