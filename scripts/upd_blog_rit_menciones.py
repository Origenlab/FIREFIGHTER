#!/usr/bin/env python3
"""La L3 de RIT nació con 0 enlaces entrantes desde el blog: ningún artículo nombraba
el paquete de aire de rescate en prosa (las dos menciones de «RIT» del corpus estaban
dentro de celdas de tabla, como «módulo RIT»).

Se corrige el contenido, no la regla. Cuatro artículos donde el tema encaja de verdad
reciben material nuevo y verificado, y de paso se arregla una imprecisión: el artículo
de PASS decía que la conexión de rescate «permite suministrar aire adicional», cuando
lo que hace es reponer aire al cilindro igualando presiones.
"""
import pathlib

BLOG = pathlib.Path(__file__).resolve().parent.parent / 'src/content/blog'

EDICIONES = [
    # ── 1. PASS: corrección de lo que hace la conexión, y el paquete que la usa
    ('pass-devices-nfpa-1982-seguridad.md',
     '5. Al contactar al bombero caído, la conexión UAC del SCBA permite suministrar aire '
     'adicional mientras se prepara la extracción\n',
     '5. Al contactar al bombero caído se le repone aire por la conexión RIC UAC de su propio '
     'SCBA, mientras se prepara la extracción\n'),
    ('pass-devices-nfpa-1982-seguridad.md',
     'Ninguno de esos pasos funciona si el PASS estaba apagado en el paso 1.\n',
     'Ninguno de esos pasos funciona si el PASS estaba apagado en el paso 1.\n'
     '\n'
     'Conviene precisar qué ocurre en el paso 5, porque se malinterpreta seguido. El aire no sale '
     'del equipo del rescatista: sale de un paquete RIT independiente que la cuadrilla lleva '
     'consigo, y la maniobra no llena el cilindro del caído —iguala las presiones de las dos '
     'botellas y se detiene ahí—. Un fabricante publica que la igualación tarda alrededor de 60 '
     'segundos, y otro advierte por escrito que después de la transferencia no se obtiene la '
     'duración nominal de ninguno de los dos cilindros. Que el manómetro del rescatado se '
     'estabilice por debajo de «lleno» es el comportamiento normal del sistema.\n'),

    # ── 2. Guía de SCBA: la conexión de rescate como componente del equipo
    ('guia-scba-equipos-respiracion-autonoma.md',
     '## Criterios de selección según perfil de brigada\n',
     '### Componente que casi nunca se revisa: la conexión de rescate\n'
     '\n'
     'Desde la edición 2002 de la norma de SCBA, todo equipo certificado debe llevar una conexión '
     'universal de rescate —la RIC UAC— en una posición determinada, para que una fuente externa '
     'pueda reponerle aire al cilindro cuando el usuario está atrapado y no se le puede sacar. Es '
     'un acople del equipo, no un accesorio opcional, y por diseño es interoperable entre marcas: '
     'un fabricante declara por escrito que su manguera funciona con cualquier SCBA que cumpla esa '
     'edición o una posterior.\n'
     '\n'
     'Dos cosas que conviene saber antes de escribirlas en un procedimiento. La primera es que la '
     'conexión debe mantenerse limpia: los fabricantes advierten que no debe tener contacto con '
     'aceite ni grasa. La segunda es que la universalidad es del acople, no de la política de cada '
     'marca: una prohíbe expresamente usar esa conexión para pasar aire de un equipo autónomo a '
     'otro, y otra establece que un equipo de 5,500 psi solo puede recibir aire, nunca donarlo. Si '
     'la flota mezcla marcas, el procedimiento escrito tiene que adoptar la restricción más '
     'severa.\n'
     '\n'
     '## Criterios de selección según perfil de brigada\n'),

    # ── 3. Unidad de rescate: el renglón de aire de rescate
    ('equipamiento-unidad-rescate-completa.md',
     '### Estabilización del Vehículo\n',
     '### Aire de Rescate para el Personal\n'
     '\n'
     'El renglón que casi nunca aparece en la lista de compra de una unidad, y que no protege a la '
     'víctima sino al rescatista: un paquete portátil de aire para reponerle aire a un bombero '
     'atrapado o sin autonomía. Lleva cilindro dedicado, reductor de presión y manguera con la '
     'conexión universal de rescate; según la configuración, también pieza facial de reemplazo.\n'
     '\n'
     'Dos advertencias antes de cotizarlo. Ninguno de estos paquetes está certificado, y no es un '
     'defecto: la aprobación de protección respiratoria se emite solo para respiradores completos, '
     'y un cilindro con manguera no lo es —un fabricante lo declara textualmente en su manual—. Y '
     'casi todos cotizan el cilindro por separado, así que una partida que dice «sistema RIT» sin '
     'desglose puede llegar sin botella. Existe además en el mercado la bolsa sola, anunciada como '
     '«bolsa RIT», que es exactamente eso: el contenedor vacío.\n'
     '\n'
     '### Estabilización del Vehículo\n'),

    # ── 4. Mantenimiento: el equipo que se degrada sin usarse
    ('mantenimiento-scba-programa-anual.md',
     '## El registro de mantenimiento como documento legal\n',
     '**El paquete de aire de rescate:** no es una pieza del SCBA, pero se degrada por la misma '
     'razón que la válvula de bypass —porque nadie lo abre—. Un maletín de aire de rescate puede '
     'pasar años cerrado y verse perfecto mientras su cilindro se vence: la prueba hidrostática y '
     'la fecha de retiro corren igual guardado que en uso. Revise presión de botella y estado de '
     'la conexión de rescate en la misma rutina de la unidad, no en el inventario anual, y lleve '
     'registro de cada apertura con la presión encontrada.\n'
     '\n'
     '## El registro de mantenimiento como documento legal\n'),
]


def main():
    hechos, faltantes = 0, []
    for archivo, viejo, nuevo in EDICIONES:
        ruta = BLOG / archivo
        txt = ruta.read_text(encoding='utf-8')
        if nuevo in txt:
            print(f'  ya aplicado · {archivo}')
            continue
        if txt.count(viejo) != 1:
            faltantes.append(f'{archivo}: {txt.count(viejo)} coincidencias')
            continue
        ruta.write_text(txt.replace(viejo, nuevo), encoding='utf-8')
        hechos += 1
        print(f'  editado · {archivo}')
    print(f'\nediciones aplicadas: {hechos} de {len(EDICIONES)}')
    if faltantes:
        raise SystemExit('sin aplicar:\n  ' + '\n  '.join(faltantes))


if __name__ == '__main__':
    main()
