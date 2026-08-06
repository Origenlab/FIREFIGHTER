#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Precisa el copy de la L3 de viseras para que el interlinker encuentre a las piezas hermanas.

Es el mismo check que enseño la ficha de guantes: contar los <a> del `l3-body` y compararlos
con las hermanas. Viseras salio con 3 enlaces porque el copy hablaba del "estandar consolidado"
sin nombrar NFPA 1850 y no mencionaba a ninguna otra pieza del conjunto por su nombre completo.

Dos notas de mecanica de la plantilla que conviene recordar:
  · el interlinker corre sobre `parrafos`, `lista[].d`, `nota` y `aplicaciones[].desc`;
  · NO corre sobre las tablas ni sobre `lista[].t`. Un termino que solo aparece en el titulo de
    un bullet o en una celda no genera enlace.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')


def sub(obj, campo, idx, viejo, nuevo):
    """Reemplaza una sola vez. Devuelve True si hubo cambio, False si ya estaba."""
    actual = obj[campo] if idx is None else obj[campo][idx]
    if nuevo in actual:
        return False
    assert viejo in actual, 'no se encontro: %r' % viejo[:60]
    nuevo_txt = actual.replace(viejo, nuevo, 1)
    if idx is None:
        obj[campo] = nuevo_txt
    else:
        obj[campo][idx] = nuevo_txt
    return True


with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'viseras-y-caretas')
S = {s['id']: s for s in prod['l3']['secciones']}
hechos = []

# 1 · La pieza vecina en la cara: la capucha. Es una precision editorial, no relleno.
if sub(S['primaria']['lista'][2], 'd', None,
       'pero no sustituye a las dos anteriores.',
       'pero no sustituye a las dos anteriores. Es el mismo reparto que con la '
       '<strong>capucha de bloqueo de partículas</strong>: cada pieza cubre una zona distinta y '
       'ninguna cubre por otra.'):
    hechos.append('primaria.lista[2].d')

# 2 · El criterio de "elemento" no es exclusivo del casco: nombrar las piezas hermanas.
if sub(S['componente'], 'parrafos', 0,
       'la certificación se declara siempre a nivel de casco</strong>.',
       'la certificación se declara siempre a nivel de casco</strong>. El criterio es el mismo en '
       'toda la línea: el elemento certificado es el <strong>traje estructural</strong> completo, '
       'el <strong>guante estructural</strong>, la <strong>bota estructural</strong> o el casco, '
       'nunca una de sus partes por separado.'):
    hechos.append('componente.parrafos[0]')

# 3 · Nombrar la norma de cuidado en lugar de aludirla.
if sub(S['cuidado'], 'parrafos', 0,
       '—hoy en el estándar consolidado, vigente desde septiembre de 2025—',
       '—hoy <strong>NFPA 1850</strong>, vigente desde septiembre de 2025—'):
    hechos.append('cuidado.parrafos[0]')

# 4 · La palabra que decide la partida vive en el titulo del bullet, donde no se enlaza.
if sub(prod['l3']['aplicaciones'][2], 'desc', None,
       'Es la línea donde una partida mal redactada',
       'En una licitación es la línea donde una partida mal redactada'):
    hechos.append('aplicaciones[2].desc')

if hechos:
    with io.open(RUTA, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

for h in hechos:
    print('  ok ', h)
print('cambios aplicados:', len(hechos) or 'ninguno, ya estaba')
