#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
La ficha del Cairns XF1 era la unica que seguia abajo del piso de 6 enlaces en el cuerpo.

No es un problema de reglas: es la ficha mas corta de la familia de cascos y su copy casi no
nombra al resto del conjunto. Se precisan dos frases donde el texto ya hablaba de la interfaz
—la careta del casco jet y el traje que va debajo del equipo con electronica— y una tercera
donde ya hablaba de dotar por funcion.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

CAMBIOS = [
    ('cuando-tiene-sentido', 'nota',
     'La línea de ataque con ala completa y el equipo de rescate técnico con jet.',
     'La línea de ataque con ala completa y el equipo de rescate técnico con jet. Y conviene '
     'decidir en el mismo movimiento la protección facial: en un jet sin ala, la careta y los '
     'goggles cargan un trabajo que en una tradicional reparte el ala.'),
    ('mantenimiento', 'parrafos', 0,
     'además de revisar coquilla, interior, barboquejo, visor y la interfaz con la pieza facial del equipo de respiración,',
     'además de revisar coquilla, interior, barboquejo, visor y la interfaz con la pieza facial '
     'del equipo de respiración —y con el cuello del chaquetón y la capucha, que es donde se '
     'cierra el conjunto—,'),
]


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
    prod = next(p for p in cat['productos'] if p['slug'] == 'cascos-bullard-y-msa')
    card = next(c for c in prod['l3']['catalogo']['cards'] if c['slug'] == 'msa-cairns-xf1')
    secs = {s['id']: s for s in card['l4']['secciones']}

    n = 0
    for cambio in CAMBIOS:
        sid, campo = cambio[0], cambio[1]
        if campo == 'parrafos':
            _, _, idx, viejo, nuevo = cambio
            actual = secs[sid]['parrafos'][idx]
        else:
            _, _, viejo, nuevo = cambio
            idx = None
            actual = secs[sid][campo]
        if nuevo in actual:
            print('  --  %s/%s ya estaba' % (sid, campo))
            continue
        assert viejo in actual, 'no se encontro en %s/%s: %r' % (sid, campo, viejo[:50])
        nuevo_txt = actual.replace(viejo, nuevo, 1)
        if idx is None:
            secs[sid][campo] = nuevo_txt
        else:
            secs[sid][campo][idx] = nuevo_txt
        n += 1
        print('  ok  %s/%s' % (sid, campo))

    if n:
        with io.open(RUTA, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
    print('cambios aplicados:', n)


if __name__ == '__main__':
    main()
