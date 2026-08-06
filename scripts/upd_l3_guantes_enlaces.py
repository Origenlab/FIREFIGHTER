#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Precisa el copy de la L3 de guantes para que el interlinker encuentre a las piezas hermanas.

El problema: la ficha de guantes salio con 3 enlaces en el cuerpo contra 5-11 de las otras
L3, porque el copy hablaba de "trajes", "cascos" y "botas" a secas y las reglas de
interlink.ts exigen a proposito el adjetivo ("traje estructural", "casco estructural") para
no capturar menciones de forestal o industrial. La correccion no es aflojar las reglas: es
escribir el nombre completo de la pieza donde ya se la estaba mencionando.

Idempotente: si el texto ya esta corregido, no hace nada.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

CAMBIOS = [
    # seccion, campo (ruta), viejo, nuevo
    ('barrera', ('nota',),
     'ya aparece en esta línea, igual que en trajes.',
     'ya aparece en esta línea, igual que en los trajes estructurales.'),
    ('declaraciones', ('parrafos', 0),
     'En cascos y en botas casi todos los fabricantes siguen citando ediciones previas.',
     'En los cascos estructurales y en las botas estructurales casi todos los fabricantes '
     'siguen citando ediciones previas.'),
    ('puno', ('parrafos', 0),
     'cubre por fuera la manga del chaquetón',
     'cubre por fuera la manga del chaquetón del traje estructural'),
]


def aplicar(seccion, ruta, viejo, nuevo):
    if len(ruta) == 1:
        actual = seccion[ruta[0]]
        if nuevo in actual:
            return False
        assert viejo in actual, 'no se encontro: %r' % viejo
        seccion[ruta[0]] = actual.replace(viejo, nuevo, 1)
        return True
    campo, idx = ruta
    actual = seccion[campo][idx]
    if nuevo in actual:
        return False
    assert viejo in actual, 'no se encontro: %r' % viejo
    seccion[campo][idx] = actual.replace(viejo, nuevo, 1)
    return True


with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'guantes-de-intervencion')
secciones = {s['id']: s for s in prod['l3']['secciones']}

hechos = 0
for sid, ruta, viejo, nuevo in CAMBIOS:
    if aplicar(secciones[sid], ruta, viejo, nuevo):
        hechos += 1
        print('  ok  %s.%s' % (sid, '.'.join(str(x) for x in ruta)))
    else:
        print('  --  %s.%s ya estaba' % (sid, '.'.join(str(x) for x in ruta)))

if hechos:
    with io.open(RUTA, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

print('cambios aplicados:', hechos)
