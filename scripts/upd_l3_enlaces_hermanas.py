#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cierra el hueco de interlinking de las dos L3 mas viejas: trajes y botas.

El diagnostico (scripts/auditoria/audit-editorial.py) las dejo en evidencia:

  trajes-estructurales-nomex-pbi   5 enlaces, CERO al catalogo
  botas-dielectricas               5 enlaces, uno al catalogo

No es un problema de reglas: son las dos primeras fichas que se escribieron, cuando todavia
no existian las paginas hermanas, asi que el copy nunca las menciona. La correccion es
editorial y va donde el texto ya hablaba de la interfaz entre piezas —el traslape del
chaqueton con el guante, el pantalon sobre la bota, el peso que se paga en el cuello o en cada
paso—, no en un parrafo agregado al final para colocar enlaces.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

# (slug del producto, id de seccion, campo, indice, viejo, nuevo)
CAMBIOS = [
    # ── TRAJES ────────────────────────────────────────────────────────────────
    # El traslape es literalmente la interfaz con las otras cuatro piezas.
    ('trajes-estructurales-nomex-pbi', 'tallaje', 'parrafos', 0,
     'y la norma exige un traslape mínimo entre chaquetón y pantalón que se pierde con dos tallas de más.',
     'y la norma exige un traslape mínimo entre chaquetón y pantalón que se pierde con dos tallas '
     'de más. El mismo criterio aplica hacia afuera: el traje cierra contra el guante '
     'estructural en la muñeca, contra la bota estructural en el empeine y contra la capucha de '
     'bloqueo de partículas en el cuello, y ninguna de esas tres uniones se resuelve sola.'),
    ('trajes-estructurales-nomex-pbi', 'tallaje', 'lista', 2,
     'Determina el largo del pantalón sobre la bota. Un pantalón corto expone el empeine.',
     'Determina el largo del pantalón sobre la bota estructural. Un pantalón corto expone el '
     'empeine, y ese hueco no lo cubre ninguna de las dos piezas.'),
    ('trajes-estructurales-nomex-pbi', 'tallaje', 'lista', 3,
     'Define el traslape con el guante y la posición de la cinta reflejante.',
     'Define el traslape con el guante —según se use puño gauntlet por fuera o wristlet por '
     'dentro— y la posición de la cinta reflejante.'),
    ('trajes-estructurales-nomex-pbi', 'pfas', 'parrafos', 1,
     'Nuestra postura es simple:',
     'Y no es exclusivo de esta línea: la barrera libre de PFAS ya aparece declarada en los '
     'guantes estructurales del catálogo, que es donde el mercado suele moverse primero. '
     'Nuestra postura es simple:'),
    # ── BOTAS ─────────────────────────────────────────────────────────────────
    ('botas-dielectricas', 'peso', 'parrafos', 0,
     'En una bota, el peso se paga en cada paso:',
     'El peso se paga distinto en cada pieza del conjunto: en el casco estructural se paga en el '
     'cuello después de una hora de trabajo con la cabeza girada, y en la bota se paga en cada '
     'paso, porque es la parte del ensamble que el elemento levanta miles de veces por turno. '
     'Dicho de otra forma:'),
    ('botas-dielectricas', 'ciclo-de-vida', 'lista', 1,
     'Un par de repuesto por',
     'Es la misma lógica del guante estructural, donde dos pares por elemento son lo que '
     'permite secar sin dejar a nadie sin equipo. Un par de repuesto por'),
]


def aplicar(secciones, aplicaciones, slug, sec_id, campo, idx, viejo, nuevo):
    s = secciones[sec_id]
    if campo == 'parrafos':
        actual = s['parrafos'][idx]
        if nuevo in actual:
            return False
        assert viejo in actual, 'no se encontro en %s/%s.p%d: %r' % (slug, sec_id, idx, viejo[:50])
        s['parrafos'][idx] = actual.replace(viejo, nuevo, 1)
    elif campo == 'lista':
        actual = s['lista'][idx]['d']
        if nuevo in actual:
            return False
        assert viejo in actual, 'no se encontro en %s/%s.l%d: %r' % (slug, sec_id, idx, viejo[:50])
        s['lista'][idx]['d'] = actual.replace(viejo, nuevo, 1)
    else:
        raise ValueError(campo)
    return True


with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
hechos = 0
for slug, sec_id, campo, idx, viejo, nuevo in CAMBIOS:
    prod = next(p for p in cat['productos'] if p['slug'] == slug)
    secciones = {s['id']: s for s in prod['l3']['secciones']}
    if aplicar(secciones, prod['l3']['aplicaciones'], slug, sec_id, campo, idx, viejo, nuevo):
        hechos += 1
        print('  ok  %s / %s.%s[%s]' % (slug, sec_id, campo, idx))
    else:
        print('  --  %s / %s.%s[%s] ya estaba' % (slug, sec_id, campo, idx))

if hechos:
    with io.open(RUTA, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

print('cambios aplicados:', hechos)
