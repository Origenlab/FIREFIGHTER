#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrige la card L2 de cilindros y precisa el nombre del producto.

Dos correcciones, verificadas contra fabricante y reglamento el 2026-08-06:

1. "Vida util de 15 anos desde fabricacion" se presentaba como si fuera de toda la linea. No lo
   es: los 15 anos son de la norma DOT-CFFC para COMPUESTO. El aluminio de Luxfer se publica
   como NLL —non-limited life, "as long as they pass required periodic testing"—, Drager publica
   20 y 30 anos de design life bajo regimen EN y vida no limitada en acero y en Type 4, y 3M
   Scott vende una linea aparte que anuncia "up to a 30-year life expectancy". La vida no es del
   material: es del PERMISO marcado en el cilindro.

2. El nombre "Cilindros 30 / 45 / 60 min" vende la unidad menos informativa que existe en esta
   pieza. Los minutos son una duracion nominal medida con maquina de respiracion, no una
   propiedad del cilindro; el fabricante del cilindro publica volumen de agua y capacidad de
   aire, y en varias de sus lineas deja la columna de duracion vacia. Se renombra a
   "Cilindros de aire respirable" y la ficha explica por que. El slug no cambia.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

NOMBRE = 'Cilindros de aire respirable'

DESC = ('Cilindros de aire respirable en aluminio, acero o fibra de carbono sobre camisa de '
        'aluminio, en 2216, 4500 y 5500 psig. Válvula con volante, manómetro propio y disco de '
        'ruptura. La vida de servicio la fija el permiso marcado en el cilindro, no el material.')

SPECS = [
    'Carbono, aluminio o acero: 8.3 lb contra 18.1 lb vacíos',
    'Capacidad publicada en pies cúbicos, no solo en minutos',
    'Recalificación cada cinco años por instalación autorizada',
    'Vida de servicio según el permiso DOT marcado',
]

INTRO = [
    ('El cilindro es la única pieza del conjunto que <strong>no la certifica NFPA ni NIOSH</strong>: '
     'es un recipiente a presión bajo jurisdicción del Departamento de Transporte, y por eso su '
     'documentación es otra. Manejamos <strong>fibra de carbono sobre camisa de aluminio</strong> '
     'en 2216, 4500 y 5500 psig, además de aluminio y acero, con válvula de volante, manómetro '
     'propio y disco de ruptura por sobrepresión.'),
    ('La diferencia de peso entre construcciones es la que se siente en turno: a la misma presión '
     'y la misma capacidad, un fabricante publica <strong>8.3 libras en carbono contra 18.1 en '
     'aluminio</strong>. Lo que no se ve en una foto es lo que decide si el cilindro sirve para tu '
     'equipo: el <strong>número de permiso DOT y la presión marcada</strong> tienen que '
     'corresponder al ERA de destino, porque la aprobación de NIOSH es del sistema completo, '
     'incluidos cilindro y válvula.'),
]


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    cat = next(c for c in data if c['slug'] == 'equipos-de-respiracion')
    prod = next(p for p in cat['productos'] if p['slug'] == 'cilindros-30-45-60-min')

    cambios = []
    if prod['nombre'] != NOMBRE:
        print('  nombre: «%s» → «%s»' % (prod['nombre'], NOMBRE))
        prod['nombre'] = NOMBRE
        cambios.append('nombre')
    for campo, valor in (('desc', DESC), ('specs', SPECS), ('intro', INTRO)):
        if prod.get(campo) != valor:
            prod[campo] = valor
            cambios.append(campo)

    if cambios:
        with io.open(RUTA, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
    print('cambios:', ', '.join(cambios) if cambios else 'ninguno, ya estaba')


if __name__ == '__main__':
    main()
