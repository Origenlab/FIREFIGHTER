#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
La ficha de cilindros salio con 2 enlaces en el cuerpo: recibe 15 del blog y devuelve casi nada.

Causa conocida y ya documentada: el copy dice "el ERA de destino" y "el equipo", que son formas
cortas, y las reglas de interlink exigen el nombre completo. Se precisan cuatro frases donde el
texto ya hablaba de la pieza vecina, del programa de mantenimiento o de la licitacion.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

CAMBIOS = [
    ('quien-certifica', 'parrafos', 0,
     'Todo el resto del equipo de respiración se documenta con dos papeles',
     'El resto de un equipo de respiración autónomo se documenta con dos papeles'),
    ('compatibilidad', 'parrafos', 0,
     'deja el conjunto fuera de lo aprobado. Por eso las válvulas no se cruzan entre marcas,',
     'deja el conjunto fuera de lo aprobado —es la misma regla que gobierna cualquier refacción de '
     'un equipo de respiración autónomo—. Por eso las válvulas no se cruzan entre marcas,'),
    ('marcado', 'lista', 2,
     'Va cerca de los marcados originales.',
     'Va cerca de los marcados originales y es la fecha que el programa de cuidado y '
     'mantenimiento de <strong>NFPA 1850</strong> obliga a tener bajo control.'),
    ('mexico', 'lista', 3,
     'Por <strong>capacidad y presión</strong>, con número de parte y permiso,',
     'En una licitación, por <strong>capacidad y presión</strong>, con número de parte y permiso,'),
    ('quien-certifica', 'parrafos', 0,
     'se documenta con dos papeles —certificado NFPA y aprobación NIOSH—',
     'se documenta con dos papeles —certificado NFPA 1970 y aprobación NIOSH—'),
    ('peso', 'parrafos', 0,
     'Es más del doble, y es peso que se carga en la espalda toda la jornada.',
     'Es más del doble, y es peso que se suma al del traje estructural y el casco y que se carga '
     'en la espalda toda la jornada.'),
]


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    cat = next(c for c in data if c['slug'] == 'equipos-de-respiracion')
    prod = next(p for p in cat['productos'] if p['slug'] == 'cilindros-30-45-60-min')
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
