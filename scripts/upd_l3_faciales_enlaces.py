#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
La ficha de piezas faciales salio con 5 enlaces en el cuerpo: bajo el piso de 6.

Mismo patron de siempre en una ficha nueva: el copy usa formas cortas —"el equipo", "el casco"—
donde la regla exige el nombre completo. Se precisan cuatro frases donde el texto ya hablaba de
la pieza vecina, del cilindro o de la norma.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

CAMBIOS = [
    ('anteojos', 'lista', 3,
     'En una estación eso incluye la capucha y el casco, que van por encima.',
     'En una estación eso incluye la <strong>capucha de bloqueo de partículas</strong> y el '
     '<strong>casco estructural</strong>, que van por encima de las correas y del sello.'),
    ('configuracion', 'lista', 1,
     'El arnés, el nosecup y el visor tienen número de parte y aparecen ahí.',
     'El arnés, el nosecup, el visor y el cilindro tienen número de parte y aparecen ahí.'),
    ('visor', 'parrafos', 1,
     'Es el argumento más fuerte que existe para no comprar equipo de generaciones anteriores por precio.',
     'Es el argumento más fuerte que existe para no comprar un equipo de respiración autónomo de '
     'generaciones anteriores por precio.'),
    ('cuidado', 'parrafos', 1,
     'Los intervalos de servicio también están publicados,',
     'Los intervalos de servicio también están publicados —y conviven con el programa de '
     '<strong>NFPA 1850</strong> que cubre al conjunto—,'),
]


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    cat = next(c for c in data if c['slug'] == 'equipos-de-respiracion')
    prod = next(p for p in cat['productos'] if p['slug'] == 'mascaras-completas-3m')
    secs = {s['id']: s for s in prod['l3']['secciones']}

    n = 0
    for sid, campo, idx, viejo, nuevo in CAMBIOS:
        s = secs[sid]
        actual = s[campo][idx] if campo == 'parrafos' else s[campo][idx]['d']
        if nuevo in actual:
            print('  --  %s/%s[%d] ya estaba' % (sid, campo, idx))
            continue
        assert viejo in actual, 'no se encontro en %s/%s[%d]: %r' % (sid, campo, idx, viejo[:60])
        txt = actual.replace(viejo, nuevo, 1)
        if campo == 'parrafos':
            s[campo][idx] = txt
        else:
            s[campo][idx]['d'] = txt
        n += 1
        print('  ok  %s/%s[%d]' % (sid, campo, idx))

    if n:
        with io.open(RUTA, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
    print('cambios aplicados:', n)


if __name__ == '__main__':
    main()
