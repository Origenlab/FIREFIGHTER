#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
La ficha del ERA salio con 4 enlaces en el cuerpo y solo uno al catalogo.

Es el mismo patron que en trajes y en botas: es la primera ficha de su categoria y su copy no
nombra a las piezas con las que el equipo hace interfaz. Y aqui la interfaz es literal —la pieza
facial sella contra la cara, debajo de la capucha y del casco, y es la que la norma reconoce
como proteccion ocular primaria—, asi que las menciones no son de relleno: son el tema.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

CAMBIOS = [
    # La pieza facial es proteccion ocular primaria: es el puente con la ficha de viseras.
    ('doble-marco', 'parrafos', 1,
     'porque nadie evaluó su lente frente a calor radiante ni su conexión de rescate.',
     'porque nadie evaluó su lente frente a calor radiante ni su conexión de rescate. Y esa '
     'pieza facial hace doble trabajo: mientras se usa, es la que la norma reconoce como '
     '<strong>protección ocular</strong> primaria, por encima de la careta del casco.'),
    # El peso del conjunto: interfaz con traje y casco.
    ('duracion', 'parrafos', 0,
     'forzando una puerta o subiendo escalera con 20 kilos encima',
     'forzando una puerta o subiendo escalera con el peso del <strong>traje estructural</strong>, '
     'el casco y el cilindro encima'),
    # El sello de la pieza facial vive debajo de la capucha: es la interfaz que mas se rompe.
    ('ajuste', 'lista', 2,
     'Para anteojos existen kits de montaje interno.',
     'Para anteojos existen kits de montaje interno. Y el sello se verifica <strong>con la '
     'capucha y el casco puestos</strong>, en ese orden, porque es así como se usa: la capucha '
     'va por encima de las correas y el casco por encima de todo.'),
]


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    cat = next(c for c in data if c['slug'] == 'equipos-de-respiracion')
    prod = next(p for p in cat['productos'] if p['slug'] == 'scba-scott-air-pak')
    secs = {s['id']: s for s in prod['l3']['secciones']}

    n = 0
    for sid, campo, idx, viejo, nuevo in CAMBIOS:
        s = secs[sid]
        actual = s[campo][idx] if campo == 'parrafos' else s[campo][idx]['d']
        if nuevo in actual:
            print('  --  %s/%s[%d] ya estaba' % (sid, campo, idx))
            continue
        assert viejo in actual, 'no se encontro en %s/%s[%d]: %r' % (sid, campo, idx, viejo[:50])
        nuevo_txt = actual.replace(viejo, nuevo, 1)
        if campo == 'parrafos':
            s[campo][idx] = nuevo_txt
        else:
            s[campo][idx]['d'] = nuevo_txt
        n += 1
        print('  ok  %s/%s[%d]' % (sid, campo, idx))

    if n:
        with io.open(RUTA, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
    print('cambios aplicados:', n)


if __name__ == '__main__':
    main()
