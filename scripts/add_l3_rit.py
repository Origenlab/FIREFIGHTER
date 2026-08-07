#!/usr/bin/env python3
"""L3 de sistemas RIT de aire de rescate. Cuarta ficha de equipos de respiración.

Eje editorial: el paquete RIT no es un producto certificado. Lo certificado es la
conexión RIC UAC del ERA de la víctima, no el maletín que se le conecta. Un fabricante
lo dice por escrito y en mayúsculas en su propio manual.

Todos los datos provienen de documentación publicada por el fabricante o del texto de
la norma. Lo que no está publicado se nombra como no publicado.
"""
import json, collections, pathlib

RUTA = pathlib.Path(__file__).resolve().parent.parent / 'src/data/productos.json'
SLUG_CAT = 'equipos-de-respiracion'
SLUG_PROD = 'sistemas-rit-de-rescate'

L3 = collections.OrderedDict()

L3['seoTitle'] = 'Sistemas RIT de aire de rescate para bomberos'
L3['seoDescription'] = (
    'Paquetes RIT de aire de rescate: por qué ninguno está certificado NFPA, qué hace '
    'realmente el transllenado por RIC UAC y qué revisar antes de firmar una partida.'
)
L3['h1'] = 'Sistemas RIT de aire de rescate'
L3['subtitulo'] = (
    'El paquete que se despliega cuando el que necesita aire es un bombero. Es también la '
    'única línea del catálogo donde el fabricante advierte, por escrito, que <strong>lo que '
    'usted está comprando no es un producto certificado</strong>.'
)
L3['heroImg'] = {
    'src': '/images/catalogo/1759673824678-600x400.webp',
    'alt': 'Bombero con equipo de respiración autónoma saliendo de una estructura durante una maniobra',
    'caption': 'El escenario para el que existe el RIT',
}

L3['heroBloques'] = [
    {
        'label': 'Por qué esta línea se compra distinto',
        'texto': (
            'Un <strong>paquete RIT</strong> no aparece en ninguna lista de productos '
            'certificados, y no es un descuido: no puede estarlo. Un cilindro con regulador y '
            'manguera <strong>no es un respirador completo</strong>, y la aprobación federal '
            'estadounidense se emite únicamente para ensambles completos. Uno de los tres '
            'fabricantes principales lo imprime en la segunda página de su manual, en un '
            'recuadro de advertencia: su paquete <em>no está aprobado por NIOSH ni por NFPA</em>. '
            'Lo que sí está normado es la <strong>conexión</strong> del equipo al que se conecta.'
        ),
    },
    {
        'label': 'Lo que cambia en la operación',
        'texto': (
            'El transllenado <strong>no llena: iguala</strong>. Un fabricante publica que la '
            'presión entre las dos botellas se empareja en <strong>unos 60 segundos</strong>, y '
            'otro advierte en mayúsculas que <strong>no se obtiene la duración nominal de '
            'ninguno de los dos cilindros</strong>. El manómetro del rescatado se va a detener '
            'por debajo de «lleno», y eso es el comportamiento correcto del sistema, no una falla.'
        ),
    },
]

L3['heroDatos'] = [
    {'label': 'Certificación del paquete', 'valor': 'Ninguno la tiene'},
    {'label': 'Transllenado', 'valor': 'Iguala presión, ~60 s'},
]

L3['specStrip'] = [
    {'label': 'Qué está normado', 'valor': 'La conexión, no el maletín'},
    {'label': 'Conexión', 'valor': 'RIC UAC, desde 2002'},
    {'label': 'Presiones', 'valor': '2216, 4500 y 5500 psi'},
    {'label': 'Manguera de rescate', 'valor': 'Entre 3 y 6 pies'},
    {'label': 'Pieza facial', 'valor': 'No siempre incluida'},
    {'label': 'Peso del paquete', 'valor': 'Casi nadie lo publica'},
]

L3['catalogo'] = collections.OrderedDict()
L3['catalogo']['eyebrow'] = 'Catálogo por configuración'
L3['catalogo']['titulo'] = 'Paquetes de aire de rescate, y qué trae realmente cada uno'
L3['catalogo']['intro'] = (
    'Los tres fabricantes que publican ficha resuelven el mismo problema de tres maneras '
    'distintas, y las diferencias no son de acabado: <strong>uno no incluye pieza facial</strong>, '
    'otro la entrega ya conectada a la válvula de demanda, y un tercero es el único que publica '
    'pesos. Antes de comparar precios conviene comparar <strong>qué renglones trae cada caja</strong> '
    'y qué presión de servicio maneja, porque la presión decide si el paquete puede o no donar aire '
    'a los equipos que su corporación ya opera.'
)
L3['catalogo']['imgRef'] = 'Imagen de referencia de la línea'
L3['catalogo']['nota'] = (
    'Ninguno de estos paquetes lleva número de aprobación propio, y eso es correcto: la aprobación '
    'federal se emite solo para <strong>respiradores completos</strong>. Si una convocatoria pide '
    '«sistema RIT certificado NFPA», está pidiendo un documento que no existe. Lo que sí se puede '
    'exigir por escrito es que <strong>los equipos de respiración autónoma de la corporación '
    'cumplan la norma vigente</strong> y traigan su conexión de rescate, que es donde vive el requisito.'
)

L3['catalogo']['cards'] = [
    collections.OrderedDict([
        ('marca', '3M Scott'),
        ('modelo', 'RIT-Pak III'),
        ('variante', 'Doce configuraciones'),
        ('varianteLabel', 'Referencias'),
        ('fichaLabel', 'el RIT-Pak III'),
        ('badge', 'Sin certificar'),
        ('estado', 'El que lo dice por escrito'),
        ('img', '/images/catalogo/1759673824678-600x400.webp'),
        ('alt', 'Bombero con equipo de respiración autónoma durante una maniobra de rescate'),
        ('desc',
         'Es la referencia honesta de la categoría, y no por lo que trae sino por lo que admite: '
         'su manual advierte en la página 2 que el paquete y sus accesorios <strong>no están '
         'aprobados por NIOSH ni por NFPA</strong> y que <strong>no es un respirador completo</strong>. '
         'Hasta la pieza facial de emergencia se declara como configuración no aprobada, de uso '
         'exclusivo dentro del paquete. Se pide en <strong>tres presiones de servicio</strong> —2216, '
         '4500 y 5500 psi— y el <strong>cilindro se cotiza aparte</strong>, con duraciones de 30, 45, '
         '60 y hasta 75 minutos según la presión.'),
        ('specs', [
            'Manguera de rescate de 6 pies y manguera de transllenado de 5 pies',
            'Manifold con válvula de alivio que ventea si se excede la presión del equipo',
            'Cilindro por separado: 2.2 L, 4.5 L o 5.5 L',
            'Alarma acústica de campana alrededor del 25 % de presión',
        ]),
        ('chip', 'Pedir el cilindro en la misma partida'),
    ]),
    collections.OrderedDict([
        ('marca', '3M Scott'),
        ('modelo', 'RIT-Pak Fast Attack'),
        ('variante', 'Bolsa chica o mediana'),
        ('varianteLabel', 'Tamaño'),
        ('fichaLabel', 'el RIT-Pak Fast Attack'),
        ('badge', 'Peso publicado'),
        ('estado', 'El único con cifras de peso'),
        ('img', '/images/catalogo/1606613816768-600x450.webp'),
        ('alt', 'Binomio de bomberos con equipo de respiración autónoma listo para entrar'),
        ('desc',
         'La versión compacta, y la única de toda la categoría donde el fabricante <strong>publica '
         'pesos</strong>: bolsa chica <strong>10.5 lb</strong> y mediana <strong>10.8 lb</strong>, '
         'ambas sin cilindro, más el cilindro que se elija —de <strong>7.16 a 14.15 lb</strong> '
         'lleno—. Nunca publica el total ensamblado, así que cualquier cifra de «paquete completo» '
         'que le citen es una suma hecha por un tercero. <strong>No existe versión de 2216 psi</strong>: '
         'solo 4500 y 5500.'),
        ('specs', [
            'Bolsa chica ≈ 22" y mediana ≈ 27" de largo',
            'Cilindros de 15, 30 y 45 minutos según presión',
            'Manómetro con silbato y correa de hombro',
            'Vara de carga universal con banda reflejante',
        ]),
        ('chip', 'Sumar bolsa más cilindro para el peso real'),
    ]),
    collections.OrderedDict([
        ('marca', 'MSA'),
        ('modelo', 'G1 RIT System'),
        ('variante', '2216, 4500 y 5500 psi'),
        ('varianteLabel', 'Presión'),
        ('fichaLabel', 'el G1 RIT System'),
        ('badge', 'Facial incluida'),
        ('estado', 'El más completo de caja'),
        ('img', '/images/catalogo/1592235905030-600x450.webp'),
        ('alt', 'Bombero con pieza facial de equipo de respiración bajo el casco estructural'),
        ('desc',
         'Es el que sale de la caja más listo para operar: incluye <strong>pieza facial talla '
         'mediana</strong> con arnés de cuatro puntos, regulador de segunda etapa de conexión rápida '
         'y manómetro remoto. Sus dos mangueras son de <strong>seis pies</strong> —la de alta presión '
         'y la de presión intermedia—, contra las de tres pies de su generación anterior. El fabricante '
         'publica además el dato que decide compras: <strong>un equipo de 5500 psi solo puede recibir '
         'aire, nunca donarlo</strong>.'),
        ('specs', [
            'Manguera de alta presión de 6 pies con conexión de llenado rápido',
            'Manguera de presión intermedia de 6 pies con manifold para segundo usuario',
            'Pieza facial talla mediana incluida en el paquete',
            'Cilindro por separado en las tres presiones',
        ]),
        ('chip', 'Verificar presión de servicio antes de pedir'),
    ]),
    collections.OrderedDict([
        ('marca', 'MSA'),
        ('modelo', 'RescueAire II'),
        ('variante', 'Baja y alta presión'),
        ('varianteLabel', 'Configuración'),
        ('fichaLabel', 'el RescueAire II'),
        ('badge', 'Sin pieza facial'),
        ('estado', 'Para flota de generación previa'),
        ('img', '/images/catalogo/1606613640173-600x450.webp'),
        ('alt', 'Bombero con cilindro de equipo de respiración autónoma en la espalda'),
        ('desc',
         'El paquete de la generación anterior, y el que más se malinterpreta en una partida: '
         'trae regulador montado en máscara y reductor de presión, pero <strong>no trae la pieza '
         'facial</strong> —el regulador se conecta a una facial de la misma marca que la corporación '
         'ya debe tener—. Sus mangueras son de <strong>36 pulgadas</strong>. Arnés de transporte de '
         'material resistente a flama y calor, y alarma acústica integrada.'),
        ('specs', [
            'Manguera de llenado rápido de 36 pulgadas',
            'Regulador montado en máscara, sin pieza facial',
            'Compatible con cilindros de 2216 y 4500 psi de la marca',
            'Arnés de transporte resistente a flama',
        ]),
        ('chip', 'Confirmar que la facial ya está en inventario'),
    ]),
    collections.OrderedDict([
        ('marca', 'Dräger'),
        ('modelo', 'RIT LifeGuard II'),
        ('variante', 'Kit completo'),
        ('varianteLabel', 'Presentación'),
        ('fichaLabel', 'el RIT LifeGuard II'),
        ('badge', 'Facial preconectada'),
        ('estado', 'El de despliegue más rápido'),
        ('img', '/images/catalogo/1705503828024-600x450.webp'),
        ('alt', 'Piezas faciales de equipo de respiración colgadas en el rack de la estación'),
        ('desc',
         'Su diferencia de diseño es de segundos ganados: la <strong>válvula de demanda ya viene '
         'conectada a la pieza facial completa</strong> dentro del maletín, con líneas interiores '
         'codificadas por color y manguera de rescate de <strong>tres pies</strong>. La de '
         'transllenado va fijada a la tapa. El punto a leer con cuidado está en el manual del equipo '
         'de esta marca: <strong>prohíbe expresamente usar la conexión de rescate para transferir '
         'aire de un equipo autónomo a otro</strong>, una restricción que sus competidores no imponen.'),
        ('specs', [
            'Válvula de demanda ya conectada a la pieza facial',
            'Manguera de rescate de 3 pies; la de transllenado va en la tapa',
            'Bolsa para cilindro de 45 o 60 minutos',
            'Líneas interiores codificadas por color',
        ]),
        ('chip', 'Revisar la política de transllenado de la marca'),
    ]),
    collections.OrderedDict([
        ('marca', 'Multimarca'),
        ('modelo', 'Bolsa RIT sin equipo'),
        ('variante', 'Solo el contenedor'),
        ('varianteLabel', 'Alcance'),
        ('fichaLabel', 'la bolsa RIT sin equipo'),
        ('badge', 'El renglón que engaña'),
        ('estado', 'Va aquí para que no lo compre por error'),
        ('img', '/images/catalogo/1705503831904-600x450.webp'),
        ('alt', 'Equipo de respiración autónoma preparado sobre la unidad de la estación'),
        ('desc',
         'Existe en el mercado un producto que se anuncia como «bolsa RIT» o «FAST bag» y que es '
         'exactamente eso: <strong>la bolsa vacía</strong>. Su propia ficha lo aclara —<em>equipo de '
         'respiración no incluido</em>—, con portaherramientas, anillos de sujeción y espacio para '
         'cuñas, pero <strong>sin cilindro, sin regulador, sin manguera y sin pieza facial</strong>. '
         'Cuesta una fracción de un paquete real y por eso aparece cotizado donde debía ir un sistema '
         'completo. La incluimos en el catálogo para que se reconozca a tiempo.'),
        ('specs', [
            'Es un contenedor, no un sistema de aire',
            'No incluye cilindro, regulador ni pieza facial',
            'Útil solo si el paquete de aire ya existe y falta el estuche',
            'Su precio bajo es la señal de alerta en una comparativa',
        ]),
        ('chip', 'Leer el alcance antes de comparar precios'),
    ]),
]

L3['secciones'] = [
    collections.OrderedDict([
        ('id', 'no-es-certificado'),
        ('eyebrow', 'La corrección de fondo'),
        ('titulo', 'El paquete RIT no es un producto certificado, y no puede serlo'),
        ('parrafos', [
            'Conviene decirlo antes que nada, porque ordena todo lo demás: <strong>no existe un '
            'paquete RIT certificado</strong>. La aprobación federal estadounidense de protección '
            'respiratoria se emite <strong>únicamente para ensambles de respirador completos</strong>, '
            'y un cilindro con reductor de presión y manguera no es un respirador: es una fuente de '
            'aire. Un fabricante lo imprime en la segunda página de su manual, dentro de un recuadro '
            'de advertencia, con estas palabras: su paquete y sus accesorios <em>no están aprobados '
            'por NIOSH ni por NFPA</em>, y <em>no es un respirador completo</em>. Añade que ni siquiera '
            'la pieza facial de emergencia que lo acompaña constituye una configuración aprobada.',
            'Los otros dos fabricantes no lo dicen: simplemente omiten toda mención de certificación en '
            'la ficha del paquete. Y uno de ellos lo confirma sin querer, porque publica una lista de '
            'sus productos certificados para bomberos y <strong>su propio paquete de rescate no '
            'aparece en ella</strong>. La omisión es coherente: no hay nada que declarar.',
            'Lo que sí está normado —y es la pieza clave de toda esta ficha— es la <strong>conexión de '
            'rescate del equipo de la víctima</strong>. Desde la edición 2002 de la norma de equipos '
            'de respiración autónoma, todo equipo certificado debe llevar una conexión universal de '
            'rescate en una posición determinada, para que cualquier fuente externa pueda reponerle '
            'aire. Esa conexión está en el equipo del rescatado, no en el maletín del rescatista. El '
            'requisito de <strong>NFPA 1970</strong> vive hoy en los capítulos de diseño, desempeño y '
            'métodos de prueba de esa norma, que incluye una prueba específica de velocidad de llenado.',
        ]),
        ('tabla', {
            'head': ['Elemento', '¿Está certificado?', 'Qué se puede exigir por escrito'],
            'rows': [
                ['Paquete RIT completo', 'No, en ninguna marca',
                 'Lista de contenido con número de parte por renglón'],
                ['Cilindro del paquete', 'Aprobación de transporte del recipiente',
                 'Designación grabada, prueba hidrostática y fecha de retiro'],
                ['Pieza facial de emergencia', 'Un fabricante la declara <strong>no aprobada</strong>',
                 'Qué configuración es y para qué uso la autoriza el fabricante'],
                ['Conexión de rescate del ERA', 'Sí, dentro de la certificación del equipo',
                 'Certificado del equipo con edición y organismo certificador'],
                ['Capacitación de la cuadrilla', 'No es certificación de producto',
                 'Constancia del programa y evaluación anual documentada'],
            ],
        }),
        ('nota',
         'Consecuencia práctica en una <strong>licitación</strong>: pedir «sistema RIT certificado '
         'NFPA» hace impugnable la partida, porque solicita un documento que ningún fabricante puede '
         'emitir. La redacción que sí se sostiene exige el certificado del <strong>equipo de '
         'respiración</strong> y la lista de contenido del paquete renglón por renglón.'),
    ]),
    collections.OrderedDict([
        ('id', 'transllenado'),
        ('eyebrow', 'Lo que realmente pasa'),
        ('titulo', 'El transllenado no llena: iguala'),
        ('parrafos', [
            'Es el malentendido más caro de la categoría, y el que más rápido se corrige con una '
            'frase: al conectar la fuente de rescate al equipo del bombero atrapado, el aire fluye '
            'hasta que <strong>las dos presiones se igualan</strong>, y ahí se detiene. No hay bomba, '
            'no hay compresor: hay una diferencia de presión que se agota. Un fabricante publica el '
            'tiempo —<strong>alrededor de 60 segundos</strong> para que las presiones se emparejen— '
            'y otro lo advierte en mayúsculas: <strong>no se obtiene la duración nominal de ninguno '
            'de los dos cilindros</strong>, y la cantidad transferida depende del tamaño de la botella '
            'receptora y de cuánto le quedaba.',
            'De ahí una escena que hay que anticipar en el entrenamiento: el manómetro del rescatado '
            'se va a <strong>estabilizar por debajo de «lleno»</strong>, y va a quedar aire en la '
            'botella de rescate. Ninguna de las dos cosas es una falla. Quien no lo sabe, insiste, '
            'pierde segundos y a veces desconecta y vuelve a conectar buscando un resultado que el '
            'sistema no puede dar.',
            'Por eso la doctrina de despliegue de varios cuerpos privilegia lo otro que trae el '
            'paquete: <strong>dar aire directo</strong> con la manguera de presión intermedia y, si '
            'hace falta, con una <strong>pieza facial</strong> de reemplazo, en lugar de intentar '
            'recargar el cilindro de aire respirable del rescatado. El transllenado sirve cuando hay '
            'que ganar autonomía para una extracción larga; el suministro directo sirve cuando hay '
            'que ganar los próximos treinta segundos.',
        ]),
        ('lista', [
            {'t': 'Lo que se recupera',
             'd': 'Presión intermedia entre las dos botellas, no una recarga. Con dos cilindros de la '
                  'misma capacidad, lo que uno gana el otro lo pierde.'},
            {'t': 'Cuánto tarda',
             'd': 'Un fabricante publica <strong>unos 60 segundos</strong> hasta igualar. Los otros dos '
                  'no publican tiempo, así que ese número no se puede generalizar a toda la flota.'},
            {'t': 'Qué protege al equipo',
             'd': 'El manifold lleva <strong>válvula de alivio</strong> que ventea si la presión de la '
                  'fuente excede la nominal del equipo receptor. Es una protección, no un permiso para '
                  'mezclar presiones.'},
            {'t': 'La advertencia al donante',
             'd': 'Si durante una transferencia entre equipos suena la alarma de baja presión del que '
                  'dona, el fabricante indica desconectar y <strong>preservar su propio aire de '
                  'escape</strong>.'},
        ]),
        ('nota',
         'Dato que no encontramos publicado por ningún fabricante: el <strong>caudal y el tiempo de '
         'llenado exigidos por la norma</strong>. La prueba existe y está nombrada en el método de '
         'ensayo, pero sus parámetros no son públicos. Si una especificación pide «llenado en X '
         'segundos», nadie puede acreditarlo con documento de fábrica.'),
    ]),
    collections.OrderedDict([
        ('id', 'compatibilidad'),
        ('eyebrow', 'Universal, con letra chica'),
        ('titulo', 'La conexión es universal; la política del fabricante, no'),
        ('parrafos', [
            'La conexión de rescate se diseñó explícitamente para ser universal, y lo es: un fabricante '
            'declara por escrito que su manguera de alta presión <strong>acopla con cualquier equipo '
            'que cumpla la norma en su edición 2002 o posterior</strong>, sea de la marca que sea. Ese '
            'es el logro real de la norma y conviene reconocerlo: en 2026, un maletín de una marca '
            'puede reponerle aire al equipo de otra.',
            'Lo que <strong>no</strong> es universal es lo que cada fabricante autoriza hacer con esa '
            'conexión. Aquí las tres marcas divergen, y la divergencia es de política documentada, no '
            'de diseño. Una <strong>prohíbe expresamente</strong> usar la conexión para transferir '
            'aire de un equipo autónomo a otro, y también para dar aire a un segundo usuario. Otra sí '
            'lo documenta y lo permite en 2216 y 4500 psi, pero establece que un equipo de <strong>5500 '
            'psi solo puede recibir aire, nunca donarlo</strong>. La tercera lo permite con advertencias '
            'sobre el comportamiento del manómetro y de las alarmas al mezclar presiones.',
            'Traducido a una compra: si su corporación opera <strong>equipos de respiración '
            'autónoma</strong> de dos marcas, el acople va a funcionar, pero el procedimiento escrito '
            'tiene que respetar la restricción más severa de las dos. Y si está migrando a 5500 psi, '
            'conviene saber antes de firmar que esos equipos, en al menos una marca, quedan fuera del '
            'esquema de transllenado entre bomberos.',
        ]),
        ('tabla', {
            'head': ['Situación', 'Qué dice la documentación de fábrica', 'Qué hacer en el procedimiento'],
            'rows': [
                ['Maletín de rescate a equipo de otra marca', 'Autorizado por diseño de la conexión',
                 'Verificar en campo con los equipos reales antes de confiar en el papel'],
                ['Equipo autónomo a equipo autónomo', 'Una marca lo <strong>prohíbe</strong>; otra lo permite',
                 'Adoptar la restricción más severa de la flota'],
                ['Equipo de 5500 psi como donante', 'Una marca lo prohíbe expresamente',
                 'Marcar esos equipos como receptores únicamente'],
                ['Fuente de mayor presión que la del equipo', 'Prohibido exceder la presión nominal',
                 'Confiar en la válvula de alivio solo como respaldo, no como método'],
                ['Segundo usuario en la misma fuente', 'Una marca lo prohíbe por esa conexión',
                 'Usar la línea de presión intermedia prevista para ello'],
            ],
        }),
        ('nota',
         'Dato que la norma tampoco resuelve del todo: la <strong>ubicación exacta</strong> de la '
         'conexión en el equipo. La norma exige una posición determinada, pero la cifra concreta que '
         'circula en la literatura del gremio no la pudimos verificar contra el texto normativo. En la '
         'práctica se resuelve entrenando con los equipos que se van a encontrar.'),
    ]),
]

L3['secciones'] += [
    collections.OrderedDict([
        ('id', 'que-trae'),
        ('eyebrow', 'Contenido real de la caja'),
        ('titulo', 'Dos de cinco paquetes no traen pieza facial, y eso decide el despliegue'),
        ('parrafos', [
            'Revisamos las fichas y los manuales publicados de las cinco configuraciones que se '
            'cotizan en México y el contenido no es equivalente. Dos de ellas <strong>no incluyen la '
            'pieza facial</strong>: entregan el regulador y esperan que la máscara la ponga la '
            'corporación, de la misma marca. Otras dos la incluyen en talla mediana. Y una la entrega '
            '<strong>ya conectada a la válvula de demanda</strong> dentro del maletín, que es la '
            'diferencia de diseño que más segundos ahorra en un despliegue real.',
            'La consecuencia operativa es incómoda y hay que decirla: si el paquete trae una sola '
            'máscara y es talla mediana, no va a sellar en todas las caras de la brigada. La '
            '<strong>prueba de ajuste</strong> se hace sobre la pieza facial asignada a cada persona, '
            'no sobre una máscara de emergencia que nadie ha probado nunca. En un rescate real esa '
            'máscara se usa igual, porque la alternativa es peor, pero conviene saber que el sello no '
            'está verificado y que ese es el motivo por el que el suministro directo a la máscara que '
            'el rescatado ya trae puesta suele ser la primera opción.',
            'La otra diferencia que separa marcas es la <strong>longitud de manguera</strong>, y no es '
            'un detalle de catálogo: define a qué distancia puede quedar el maletín del bombero '
            'atrapado. Van de <strong>tres a seis pies</strong> según fabricante y generación, y una '
            'misma marca pasó de 36 pulgadas a seis pies entre dos generaciones sin declararlo como '
            'cambio en ningún documento.',
        ]),
        ('lista', [
            {'t': 'Con pieza facial preconectada',
             'd': 'La válvula de demanda sale del maletín ya unida a la máscara. Menos pasos con guantes '
                  'puestos y en oscuridad.'},
            {'t': 'Con pieza facial suelta',
             'd': 'Talla mediana incluida. Sirve, pero no está ajustada a nadie en particular.'},
            {'t': 'Sin pieza facial',
             'd': 'Solo regulador. Requiere que la corporación tenga <strong>piezas faciales</strong> '
                  'compatibles de la misma marca en el inventario.'},
            {'t': 'Sin cilindro',
             'd': 'Casi todos los paquetes cotizan el <strong>cilindro de aire respirable</strong> por '
                  'separado. Es el error de partida más común.'},
        ]),
        ('nota',
         'Verificación de una línea que evita una compra incompleta: pedir la <strong>lista de '
         'contenido con número de parte por renglón</strong>. Si en esa lista no aparece el cilindro, '
         'no viene. Si no aparece la máscara, tampoco.'),
    ]),
    collections.OrderedDict([
        ('id', 'peso'),
        ('eyebrow', 'El dato que casi nadie publica'),
        ('titulo', 'Un solo fabricante publica pesos, y aun así no publica el total'),
        ('parrafos', [
            'Este paquete lo carga una persona que ya va vestida con <strong>traje estructural</strong>, '
            'casco y su propio equipo, y que va a entrar caminando o arrastrándose. El peso importa '
            'tanto como en cualquier otra pieza del conjunto. Y sin embargo, de las cinco '
            'configuraciones revisadas, <strong>solo una publica cifras</strong>.',
            'Los números que sí están publicados: bolsa chica <strong>10.5 lb</strong> y mediana '
            '<strong>10.8 lb</strong>, ambas <em>sin cilindro</em>, y cilindros de <strong>7.16 a '
            '14.15 lb</strong> llenos según capacidad y presión. El fabricante nunca suma. Es decir: '
            'incluso en el único caso donde hay datos, <strong>el peso del paquete ensamblado no está '
            'publicado por nadie</strong> —cualquier cifra de «paquete completo» en una comparativa es '
            'una suma hecha por un tercero, y conviene preguntar quién la hizo.',
            'La asimetría es llamativa porque ocurre dentro de la misma marca y la misma línea: el '
            'modelo compacto publica pesos y el modelo mayor de la misma familia no publica ninguno. '
            'No hay explicación publicada. Para una compra, lo honesto es pedir el peso por escrito al '
            'fabricante y, si no lo entrega, <strong>pesar el paquete armado en la recepción</strong> '
            'y dejarlo asentado en el acta.',
        ]),
        ('tabla', {
            'head': ['Componente', 'Peso publicado', 'Observación'],
            'rows': [
                ['Bolsa chica, sin cilindro', '10.5 lb', 'Largo aproximado de 22 pulgadas'],
                ['Bolsa mediana, sin cilindro', '10.8 lb', 'Largo aproximado de 27 pulgadas'],
                ['Cilindro de 15 min, 4500 psi', '7.16 lb', 'Lleno'],
                ['Cilindro de 30 min, 5500 psi', '10.44 lb', 'Lleno'],
                ['Cilindro de 45 min, 5500 psi', '14.15 lb', 'Lleno'],
                ['Paquete ensamblado', '<strong>No publicado</strong>', 'Ningún fabricante lo declara'],
            ],
        }),
        ('nota',
         'Comparación útil para dimensionar: el paquete más ligero de esa tabla ronda las 18 libras '
         'armado, y el más pesado se acerca a las 25. Son cifras que salen de sumar los renglones '
         'publicados, no de una ficha de fábrica, y así conviene citarlas.'),
    ]),
    collections.OrderedDict([
        ('id', 'entrenamiento'),
        ('eyebrow', 'La norma que cambió de número'),
        ('titulo', 'La norma de entrenamiento de estas cuadrillas ya no existe por separado'),
        ('parrafos', [
            'Aquí hay una corrección que afecta a muchas convocatorias vigentes, incluida la redacción '
            'que nosotros mismos teníamos publicada. La norma que se cita habitualmente para el '
            'entrenamiento de cuadrillas de intervención rápida <strong>fue consolidada</strong>: su '
            'contenido pasó a integrarse en una norma general de entrenamiento del servicio de '
            'bomberos, edición 2026, junto con otras seis normas de capacitación. Durante este año '
            'conviven en el mercado la edición 2020 de la norma vieja, que aún se vende, y la nueva '
            'norma consolidada. Citar el número viejo no está mal; citarlo <strong>sin la edición</strong> '
            'sí lo está.',
            'Más importante que el número es lo que esa norma es y lo que no es. Es una norma de '
            '<strong>entrenamiento</strong>, no de equipo, y lo dice en su alcance. Su artículo sobre '
            'herramientas establece que <strong>el equipo de la cuadrilla lo determina la autoridad '
            'competente</strong> según necesidad y recursos disponibles. El listado que sí menciona '
            'una fuente de aire de rescate está en el <strong>anexo informativo</strong>, que no es de '
            'cumplimiento obligatorio. En otras palabras: ninguna norma le obliga a comprar un paquete '
            'RIT; lo que se le exige es la capacidad, y el paquete es la forma habitual de tenerla.',
            'Lo que sí es exigible con numeral es la <strong>evaluación anual del desempeño</strong> '
            'de la cuadrilla y de sus miembros, y la designación de un oficial de seguridad para las '
            'prácticas. No localizamos en el texto una frecuencia mínima de sesiones de entrenamiento '
            '—ni mensual ni trimestral ni por horas—, así que quien la exija en una convocatoria está '
            'añadiendo un requisito propio, lo cual es legítimo, pero no debe presentarse como '
            'obligación normativa.',
        ]),
        ('lista', [
            {'t': 'Qué exige de verdad',
             'd': 'Un programa de entrenamiento documentado y <strong>evaluación anual</strong> del '
                  'desempeño de la cuadrilla y de cada integrante.'},
            {'t': 'Qué no exige',
             'd': 'Una lista de compra. El equipo lo determina la autoridad competente según necesidad '
                  'y recursos.'},
            {'t': 'Dónde vive el requisito de la cuadrilla',
             'd': 'En las normas de organización y despliegue, que también fueron renumeradas por '
                  'consolidación. Definen la cuadrilla completa como <strong>un oficial y tres '
                  'elementos</strong>, y la inicial como dos elementos del ataque inicial.'},
            {'t': 'Cómo redactarlo sin errar',
             'd': 'Citar la norma <strong>con edición</strong> y, si el documento es de años previos, '
                  'aclarar que la numeración cambió por consolidación.'},
        ]),
        ('nota',
         'Corrección a nuestra propia página de categoría: decíamos que la norma de entrenamiento '
         '«exige» capacitación específica como si fuera una condición de cumplimiento del producto. '
         'Exige un programa de entrenamiento a la corporación, no una característica del paquete, y '
         'además ya no es una norma independiente.'),
    ]),
]

L3['secciones'] += [
    collections.OrderedDict([
        ('id', 'mexico'),
        ('eyebrow', 'Qué aplica en México'),
        ('titulo', 'No hay NOM que obligue a un cuerpo de bomberos a tener cuadrilla de rescate'),
        ('parrafos', [
            'Conviene decirlo con precisión y sin adornos, porque en este punto casi todo el material '
            'que circula es traducción de doctrina estadounidense. <strong>No localizamos ninguna Norma '
            'Oficial Mexicana dirigida a cuerpos de bomberos</strong> como sujeto obligado, ni una que '
            'imponga cuadrilla de intervención rápida en incendio estructural. Tampoco existe una ley '
            'general de bomberos federal: la regulación es estatal y municipal, y varía por entidad. '
            'La regla estadounidense de «dos adentro, dos afuera», que muchos documentos citan como si '
            'aplicara aquí, ni siquiera alcanza federalmente a los bomberos municipales de aquel país '
            '—solo llega a ellos por planes estatales.',
            'Lo que sí existe en México, y con numeral, es la obligación del <strong>patrón de un '
            'centro de trabajo</strong> en espacios confinados. La <strong>NOM-033-STPS</strong> exige '
            'designar <strong>al menos un vigía</strong> que permanezca fuera del espacio durante todo '
            'el trabajo, en comunicación con quienes están adentro, con facultad de ordenar la '
            'evacuación. Exige también un <strong>plan de atención a emergencias y rescate</strong> que '
            'nombre a los trabajadores designados y capacitados, especifique el equipo de rescate '
            'requerido y establezca en qué condiciones el personal de rescate —interno o externo— puede '
            'o no ingresar.',
            'Y exige algo que en la práctica es el equivalente funcional del despliegue de un RIT: que '
            '<strong>los recursos para la atención a emergencias estén disponibles antes de iniciar '
            'los trabajos</strong>, no después. Súmele la capacitación específica de la brigada de '
            'rescate, el refuerzo <strong>al menos una vez al año</strong> o tras cualquier incidente, '
            'y los simulacros. Es un marco menos exigente que el estadounidense en número de personas, '
            'pero es exigible con numeral y es el que un inspector va a revisar.',
        ]),
        ('tabla', {
            'head': ['Requisito mexicano', 'Dónde vive', 'Qué se documenta'],
            'rows': [
                ['Vigía permanente fuera del espacio', 'Obligaciones del patrón y funciones del vigía',
                 'Designación por escrito y constancia de capacitación'],
                ['Plan de rescate con personal nombrado', 'Capítulo de plan de atención a emergencias',
                 'Nombres, funciones y equipo de rescate asignado'],
                ['Recursos disponibles antes de iniciar', 'Funciones del responsable de los trabajos',
                 'Verificación previa asentada en el permiso de entrada'],
                ['Equipo autónomo cuando no hay atmósfera confirmada', 'Condiciones de seguridad',
                 'Asignación del equipo y su ficha'],
                ['Refuerzo anual y simulacros', 'Capítulo de capacitación',
                 'Registro de simulacros y de evaluación'],
            ],
        }),
        ('nota',
         'Lo que la NOM <strong>no</strong> fija: número mínimo de rescatistas en sitio, tiempo de '
         'respuesta, ni una figura equivalente a la cuadrilla de intervención rápida. Y admite '
         'expresamente el rescate por servicio externo. Quien redacte una especificación mexicana '
         'apoyándose solo en doctrina extranjera va a pedir cosas que aquí nadie está obligado a '
         'cumplir, y va a dejar fuera las que sí.'),
    ]),
    collections.OrderedDict([
        ('id', 'uebss'),
        ('eyebrow', 'Hacia dónde va'),
        ('titulo', 'El cambio de fondo: compartir aire dejó de estar prohibido'),
        ('parrafos', [
            'Durante dos décadas la postura fue tajante y está documentada por la propia organización '
            'normalizadora: la conexión de rescate <strong>no es un sistema para compartir aire entre '
            'dos personas</strong>, y no podía serlo porque la aprobación federal no certifica ningún '
            'sistema que permita a dos usuarios respirar de una sola fuente. La norma lo explicaba así, '
            'con esas palabras, en su propia reseña histórica.',
            'La edición 2025 de la norma vigente introduce algo distinto: define y normaliza un '
            '<strong>sistema universal de respiración de emergencia</strong>, descrito como un '
            'dispositivo del equipo que permite a los usuarios compartir su aire disponible en una '
            'emergencia a través de una conexión interoperable normalizada. Tiene capítulo de diseño '
            'propio. Es, en los hechos, el reconocimiento normativo de lo que antes se declaraba '
            'incompatible con la certificación.',
            'Somos honestos sobre el límite de lo que pudimos verificar: <strong>no localizamos '
            'públicamente el texto normativo completo</strong> de ese capítulo, ni un pronunciamiento '
            'del organismo de aprobación federal que resuelva la aparente contradicción con su postura '
            'histórica. Lo que sí es verificable es que la definición existe en la edición 2025 y que '
            'la norma de entrenamiento en su edición 2020 ya pedía entrenar en el uso de estos sistemas '
            '«donde estén disponibles». Para una corporación que compra hoy, la pregunta correcta al '
            'fabricante es concreta: <strong>¿este equipo trae ese sistema, con qué número de parte, y '
            'está dentro de su configuración aprobada?</strong>',
        ]),
        ('nota',
         'Dato de campo que ordena las prioridades, y que viene de investigaciones oficiales de muertes '
         'de bomberos: en al menos un caso documentado los factores contribuyentes citados fueron, '
         'textualmente, que la cuadrilla de intervención rápida <strong>no estaba disponible en '
         'escena</strong> y que la <strong>gestión del aire fue inadecuada</strong>. Ninguno de los dos '
         'se resuelve comprando un maletín.'),
    ]),
    collections.OrderedDict([
        ('id', 'despliegue'),
        ('eyebrow', 'Cómo se guarda y se revisa'),
        ('titulo', 'Un paquete que se revisa como equipo, no como refacción'),
        ('parrafos', [
            'Un paquete de rescate pasa años sin usarse y luego tiene que funcionar a la primera, en '
            'oscuridad, con guantes puestos y con alguien apurando. Eso lo convierte en el elemento del '
            'inventario con mayor riesgo de degradarse en silencio. El <strong>cilindro</strong> que '
            'lleva adentro está sujeto exactamente a la misma disciplina que cualquier otro: prueba '
            'hidrostática vigente y fecha de retiro grabada. Un maletín guardado con la botella fuera '
            'de prueba es un maletín inservible que se ve perfecto.',
            'A eso se suma lo que sí es específico de esta línea. La conexión de rescate exige '
            '<strong>limpieza absoluta</strong>: el fabricante advierte que no debe entrar en contacto '
            'con aceite, grasa ni contaminantes, y un maletín que vive en un compartimento de unidad '
            'los tiene cerca todo el tiempo. La presión de la botella se revisa con la misma frecuencia '
            'que la de los equipos en servicio, no cuando toca inventario anual.',
        ]),
        ('lista', [
            {'t': 'Revisión con la unidad',
             'd': 'Presión de la botella y estado del manómetro, en la misma rutina que los '
                  '<strong>equipos de respiración autónoma</strong> de la unidad.'},
            {'t': 'Vigencia del recipiente',
             'd': 'Prueba hidrostática y fecha de retiro del <strong>cilindro</strong>. Se vence igual '
                  'guardado que en uso.'},
            {'t': 'Estado de la conexión',
             'd': 'Sin aceite ni grasa, tapa puesta, rosca y acople sin golpes. Es la pieza que decide '
                  'si el sistema sirve.'},
            {'t': 'Orden interno del maletín',
             'd': 'Mangueras codificadas y ruteadas igual siempre. En despliegue nadie va a buscar qué '
                  'manguera es cuál.'},
            {'t': 'Práctica de despliegue',
             'd': 'Con guantes, casco y visibilidad reducida. Un despliegue practicado a plena luz sobre '
                  'una mesa no mide nada.'},
        ]),
        ('nota',
         'Registro que vale la pena llevar aunque nadie lo pida: fecha de cada apertura del maletín, '
         'presión encontrada y quién lo revisó. Es el único documento que demuestra que el paquete '
         'estuvo listo <strong>todos los días</strong>, no solo el de la auditoría.'),
    ]),
]

L3['galeriaIntro'] = (
    'Referencias de la línea en operación. Lo que decide si un paquete de rescate sirve no aparece en '
    'ninguna foto: la presión que tenía la botella el día que se abrió, si la conexión estaba limpia y '
    'si la cuadrilla lo había desplegado antes con guantes puestos.'
)
L3['galeria'] = [
    {'src': '/images/catalogo/1759673824678-1000x750.webp',
     'alt': 'Bombero equipado saliendo de una estructura durante una maniobra de rescate',
     'caption': 'El escenario para el que existe el RIT'},
    {'src': '/images/catalogo/1606613816768-600x450.webp',
     'alt': 'Binomio de bomberos con equipo de respiración autónoma listo para entrar',
     'caption': 'La cuadrilla espera fuera, equipada y sin tarea asignada'},
    {'src': '/images/catalogo/1606613640173-600x450.webp',
     'alt': 'Bombero con equipo de respiración autónoma desplegando desde la unidad',
     'caption': 'El maletín sale con la unidad, no se arma en escena'},
    {'src': '/images/catalogo/1705503828024-600x450.webp',
     'alt': 'Piezas faciales de equipo de respiración colgadas en el rack de la estación',
     'caption': 'La máscara de emergencia no está ajustada a nadie'},
]

L3['aplicaciones'] = [
    {'sector': 'Cuerpos de bomberos',
     'desc': 'Un paquete por unidad de ataque, con el cilindro incluido en la misma partida y la '
             'lista de contenido renglón por renglón. Es la línea donde la capacitación pesa más que '
             'la marca: el equipo se compra una vez y se despliega bajo presión años después.'},
    {'sector': 'Espacios confinados',
     'desc': 'Es el escenario donde el marco mexicano sí es exigible: vigía permanente fuera del '
             'espacio, plan de rescate con personal nombrado y recursos de emergencia disponibles '
             'antes de iniciar los trabajos, no después.'},
    {'sector': 'Industria con brigada propia',
     'desc': 'Donde conviene definir por escrito si el rescate lo hace la brigada interna o un '
             'servicio externo, porque de esa decisión depende si el paquete se compra o se contrata '
             'la capacidad.'},
]

L3['datoClave'] = {
    'titulo': 'Ningún paquete RIT está certificado, y así debe ser',
    'texto': (
        'La aprobación federal de protección respiratoria se emite <strong>solo para ensambles de '
        'respirador completos</strong>, y un maletín con cilindro, reductor y manguera no lo es. Un '
        'fabricante lo declara textualmente en su manual: su paquete <strong>no está aprobado por '
        'NIOSH ni por NFPA</strong> y <strong>no es un respirador completo</strong>. Lo que sí está '
        'normado es la conexión universal de rescate del equipo de la víctima, obligatoria desde la '
        'edición 2002. Pedir «RIT certificado» en una convocatoria es pedir un papel que no existe.'
    ),
}

L3['normasRef'] = [
    'NFPA 1970',
    'NIOSH 42 CFR 84',
    'NFPA 1407',
    'NOM-033-STPS',
    'NFPA 1989',
    'NOM-017-STPS',
]

L3['documentacion'] = [
    'Lista de contenido del paquete con número de parte por renglón, incluyendo si trae o no cilindro y pieza facial',
    'Presión de servicio del paquete y de los equipos de la corporación, declaradas por escrito',
    'Designación del cilindro, prueba hidrostática vigente y fecha de retiro grabada',
    'Longitud de las mangueras de rescate y de transllenado, por número de parte',
    'Manual del fabricante con su política de transllenado entre equipos y sus restricciones por presión',
    'Certificado del equipo de respiración autónoma de la corporación, con edición y organismo certificador',
    'Constancia del programa de entrenamiento de la cuadrilla y de su evaluación anual',
]

L3['blog'] = [
    'pass-devices-nfpa-1982-seguridad',
    'guia-scba-equipos-respiracion-autonoma',
    'cilindros-fibra-carbono-scba-guia',
    'lineas-suministro-aire-espacios-confinados',
    'equipamiento-unidad-rescate-completa',
    'nfpa-1981-mexico-equipos-respiracion',
]

L3['faqs'] = [
    {'q': '¿Existe un paquete RIT certificado NFPA?',
     'a': 'No, y no puede existir. La aprobación federal de protección respiratoria se emite solo para '
          'ensambles de respirador completos, y un cilindro con reductor de presión y manguera no es un '
          'respirador completo. Un fabricante lo declara textualmente en su manual —dice que su paquete '
          'no está aprobado por NIOSH ni por NFPA— y los otros dos simplemente no mencionan '
          'certificación alguna en la ficha del paquete. Uno de ellos lo confirma por exclusión: publica '
          'la lista de sus productos certificados para bomberos y su paquete de rescate no aparece. Lo '
          'que sí está certificado es la conexión de rescate del equipo de la víctima.'},
    {'q': '¿Por qué el manómetro no llega a lleno después de transllenar?',
     'a': 'Porque el sistema no llena, iguala. El aire fluye de la botella con más presión a la que tiene '
          'menos hasta que las dos quedan parejas, y ahí se detiene. Un fabricante publica que eso ocurre '
          'en unos 60 segundos, y otro advierte en mayúsculas que no se obtiene la duración nominal de '
          'ninguno de los dos cilindros. Que el manómetro se estabilice por debajo de lleno y que quede '
          'aire en la botella de rescate es el comportamiento correcto, no una falla. Vale la pena '
          'anticiparlo en el entrenamiento, porque quien no lo sabe pierde segundos insistiendo.'},
    {'q': '¿La manguera de rescate de una marca sirve en el equipo de otra?',
     'a': 'Sí en el acople, y esa es la razón de ser de la conexión universal: un fabricante declara por '
          'escrito que su manguera de alta presión funciona con cualquier equipo que cumpla la norma en '
          'su edición 2002 o posterior, sea de la marca que sea. Lo que no es universal es lo que cada '
          'fabricante autoriza. Una marca prohíbe expresamente usar esa conexión para pasar aire de un '
          'equipo autónomo a otro; otra lo permite en 2216 y 4500 psi pero establece que un equipo de '
          '5500 psi solo puede recibir, nunca donar. Si su flota mezcla marcas, el procedimiento escrito '
          'debe adoptar la restricción más severa.'},
    {'q': '¿Cuánto pesa un paquete RIT armado?',
     'a': 'Ningún fabricante lo publica. De las cinco configuraciones que revisamos, una sola publica '
          'pesos y lo hace desglosado: bolsa chica 10.5 lb y mediana 10.8 lb, ambas sin cilindro, más '
          'cilindros de 7.16 a 14.15 lb llenos. Nunca suma. Con esos renglones, el paquete más ligero '
          'ronda las 18 libras y el más pesado se acerca a 25, pero esas cifras son una suma nuestra, no '
          'un dato de fábrica. Si el peso es un criterio de su compra, pídalo por escrito y, si no se lo '
          'entregan, pese el paquete armado en la recepción y déjelo en el acta.'},
    {'q': '¿El paquete incluye la máscara?',
     'a': 'Depende de la configuración, y es el error de partida más frecuente después del cilindro. De '
          'las cinco que se cotizan en México, dos no incluyen pieza facial —entregan el regulador y '
          'esperan que la máscara la ponga la corporación, de la misma marca—, dos la incluyen suelta en '
          'talla mediana y una la entrega ya conectada a la válvula de demanda dentro del maletín. Esa '
          'última es la que menos pasos exige en despliegue. Antes de comparar precios, pida la lista de '
          'contenido con número de parte por renglón.'},
    {'q': '¿Hay una NOM que obligue a tener cuadrilla de intervención rápida?',
     'a': 'No localizamos ninguna dirigida a cuerpos de bomberos, ni una ley general de bomberos federal '
          '—esa regulación es estatal y municipal—. Lo que sí existe con numeral es la obligación del '
          'patrón de un centro de trabajo en espacios confinados: la NOM-033-STPS exige designar al menos '
          'un vigía que permanezca fuera del espacio en comunicación con quienes están adentro, un plan '
          'de rescate que nombre al personal designado y su equipo, y que los recursos de emergencia '
          'estén disponibles antes de iniciar los trabajos. No fija número de rescatistas ni tiempos de '
          'respuesta, y admite el rescate por servicio externo.'},
    {'q': '¿Sigue vigente la NFPA 1407 para el entrenamiento de la cuadrilla?',
     'a': 'Cambió de casa. Su contenido fue consolidado en una norma general de entrenamiento del '
          'servicio de bomberos, edición 2026, junto con otras seis normas de capacitación, aunque la '
          'edición 2020 de la norma anterior sigue a la venta y conviven durante la transición. Más '
          'importante que el número: es una norma de entrenamiento, no de equipo. Su propio articulado '
          'dice que las herramientas de la cuadrilla las determina la autoridad competente según '
          'necesidad y recursos; la mención de una fuente de aire de rescate está en el anexo '
          'informativo, que no obliga. Lo exigible con numeral es la evaluación anual del desempeño.'},
    {'q': '¿Cada cuándo se revisa un paquete que casi nunca se abre?',
     'a': 'Con la misma frecuencia que los equipos en servicio de la unidad, no en el inventario anual. '
          'Es la pieza del inventario que más se degrada en silencio, porque se ve perfecta mientras la '
          'botella se vence. Revise presión y manómetro en la rutina de la unidad, vigencia de prueba '
          'hidrostática y fecha de retiro del cilindro, y el estado de la conexión de rescate: el '
          'fabricante advierte que no debe tener contacto con aceite ni grasa, y un maletín que vive en '
          'un compartimento los tiene cerca. Lleve registro de cada apertura con presión encontrada y '
          'responsable.'},
]


def main():
    datos = json.loads(RUTA.read_text(encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    cats = datos['categorias'] if isinstance(datos, dict) else datos
    for cat in cats:
        if cat.get('slug') != SLUG_CAT:
            continue
        for prod in cat.get('productos', []):
            if prod.get('slug') != SLUG_PROD:
                continue
            prod['l3'] = L3
            RUTA.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            print(f'l3 escrito en {SLUG_PROD}: '
                  f'{len(L3["secciones"])} secciones, {len(L3["catalogo"]["cards"])} cards, '
                  f'{len(L3["faqs"])} FAQs')
            return
    raise SystemExit('no se encontró el producto')


if __name__ == '__main__':
    main()
