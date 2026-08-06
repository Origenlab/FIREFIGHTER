#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Segunda pasada de humanizacion: los parrafos que quedaron calcados entre fichas hermanas.

Lo que sigue apareciendo repetido despues de la primera pasada es de dos tipos, y solo uno
es problema:

  · HECHOS NORMATIVOS ("diez anos desde la fecha de fabricacion", "la transicion cerro el 18
    de marzo de 2026", "lavadora domestica, cloro y suavizante destruyen la barrera"). Se
    repiten porque son ciertos en todas las piezas. NO se toca: cambiarlos por sinonimos
    empeora el texto y arriesga el dato.
  · COPY CALCADO: la misma descripcion de sector palabra por palabra en tres fichas, y el
    mismo arranque de nota o de cierre en tres fichas de la misma familia. Eso si se corrige,
    porque es lo que hace que las hermanas se lean como una sola pagina duplicada.

Aqui se corrige el segundo tipo. Cada texto pasa a hablar del riesgo concreto de ESA pieza.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

# ── Descripciones de sector, una por ficha ────────────────────────────────────
APLICACIONES = {
    'guantes-de-intervencion': {
        'Brigadas industriales':
            'Donde el entrenamiento contempla intervención con exposición térmica y no solo '
            'evacuación. El guante estructural no sustituye al de extricación, al de químicos ni '
            'al de superficie caliente: son cuatro renglones distintos de la misma dotación.'},
    'skold-hero-pbi-max-7-0': {
        'Brigadas industriales':
            'Instalaciones con carga de fuego alta y personal que entra, no solo que evacúa. El '
            'conjunto es una capa del sistema: sin equipo de respiración, evaluación atmosférica, '
            'comunicaciones y respaldo, la prenda no compensa lo que falta.'},
    'skold-hero-defender-750': {
        'Brigadas industriales':
            'Dotación con expediente completo bajo NOM-002-STPS, donde la auditoría revisa papeles '
            'antes que prendas. Aquí la configuración se declara capa por capa: “SKÖLD HERÖ '
            'Defender 750” nombra una familia y una barrera, no un ensamble.'},
    'skold-hero-pioneer': {
        'Brigadas industriales':
            'Plantas que documentan cada compra para auditoría interna y de cliente. El punto fino '
            'de esta configuración es que sin las tres capas declaradas no hay ensamble definido, '
            'y sin ensamble definido el expediente queda abierto.'},
    'trajes-estructurales-nomex-pbi': {
        'Brigadas industriales':
            'Dotación dimensionada por la carga de fuego de la planta, no por número de empleados. '
            'El expediente que pide una auditoría es el mismo que pide una licitación: certificado '
            'del ensamble, edición normativa y trazabilidad por prenda.'},
}

# ── Notas y cierres calcados entre las cinco fichas SKOLD ─────────────────────
TEXTOS = [
    # (slug, seccion, campo, indice|None, viejo, nuevo)
    ('skold-hero-pioneer', 'que-es', 'nota', None,
     'En la partida tiene que aparecer <strong>la configuración de barreras completa</strong>, no solo el modelo.',
     'Una partida que solo dice el modelo deja la decisión más importante en manos del proveedor: '
     '<strong>la configuración de barreras completa</strong> es lo que hay que escribir.'),
    ('skold-hero-defender-750', 'que-es', 'nota', None,
     'En la partida tiene que aparecer <strong>la configuración de barreras completa</strong>, no solo el modelo ni la familia comercial.',
     'Aquí el nombre engaña doble, así que conviene ser explícito: lo que va en la partida es '
     '<strong>la configuración de barreras completa</strong>, no el modelo ni la familia comercial.'),
    ('skold-hero-defender-750', 'siguiente-paso', 'parrafos', 1,
     'Si la ficha no llega o llega incompleta, te lo decimos y comparamos contra PBI MAX 7.0 con lo que sí está publicado.',
     'Cuando el fabricante no manda la ficha completa, lo decimos en la propuesta y armamos la '
     'comparación contra PBI MAX 7.0 solo con lo que está publicado.'),
]


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
    bloques = {}
    for prod in cat['productos']:
        if prod.get('l3'):
            bloques[prod['slug']] = prod['l3']
            for card in prod['l3'].get('catalogo', {}).get('cards', []):
                if card.get('l4'):
                    bloques[card['slug']] = card['l4']

    n = 0
    for slug, sectores in APLICACIONES.items():
        for sector, desc in sectores.items():
            ap = next(a for a in bloques[slug]['aplicaciones'] if a['sector'] == sector)
            if ap['desc'] != desc:
                ap['desc'] = desc
                n += 1
                print('  ok  %s / aplicaciones · %s' % (slug, sector))

    for slug, sid, campo, idx, viejo, nuevo in TEXTOS:
        sec = next(s for s in bloques[slug]['secciones'] if s['id'] == sid)
        actual = sec[campo] if idx is None else sec[campo][idx]
        if nuevo.split('.')[0] in actual:
            print('  --  %s / %s.%s ya estaba' % (slug, sid, campo))
            continue
        assert viejo in actual, 'no se encontro en %s/%s: %r' % (slug, sid, viejo[:60])
        nuevo_txt = actual.replace(viejo, nuevo, 1)
        if idx is None:
            sec[campo] = nuevo_txt
        else:
            sec[campo][idx] = nuevo_txt
        n += 1
        print('  ok  %s / %s.%s' % (slug, sid, campo))

    if n:
        with io.open(RUTA, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
    print('cambios aplicados:', n)


if __name__ == '__main__':
    main()
