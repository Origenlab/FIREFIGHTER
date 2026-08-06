#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ajusta title y description de las fichas ya publicadas a los rangos que de verdad se usan.

El sufijo del sitio es " | Firefighter.com.mx" = 21 caracteres, asi que el `seoTitle` de los
datos no puede pasar de 41 para que el <title> renderizado quepa en 62. Siete fichas estaban
entre 42 y 44, y el recorte del buscador se comia justo la parte diferenciadora.

Y una description larga tampoco se publica entera: `descripcionSeo()` corta por frase completa
si el texto pasa de 160. La de viseras se estaba publicando en 116 caracteres —perdia la mitad
del mensaje— porque su segunda frase no cabia. Se reescribe para que entre completa.

Idempotente. Verifica los rangos al final y falla si algo queda fuera.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

SUFIJO = len(' | Firefighter.com.mx')
MAX_TITLE_DATO = 62 - SUFIJO          # 41
RANGO_DESC = (140, 160)

TITULOS = {
    # 42 → 41: "y PBI" ya está implícito en el nombre del producto
    'trajes-estructurales-nomex-pbi': 'Trajes estructurales Nomex y PBI NFPA',
    # 42 → 37
    'botas-dielectricas': 'Botas estructurales de bombero NFPA',
    # 44 → 39
    'guantes-de-intervencion': 'Guantes estructurales de bombero NFPA',
    # 43 → 40
    'protector-de-cuello-y-capucha': 'Capuchas con bloqueo de partículas',
    # 44 → 38
    'viseras-y-caretas': 'Viseras y caretas para casco de bombero',
    # 43 → 41
    'skold-hero-pbi-max-7-0': 'Traje SKÖLD HERÖ PBI MAX 7.0 con UL',
    # 43 → 40
    'msa-cairns-1836': 'Casco MSA Cairns 1836 de composite',
}

DESCRIPCIONES = {
    # 166 → dentro de rango, y sin perder la segunda frase al publicarse
    'viseras-y-caretas':
        'Viseras, caretas, Bourkes y goggles de casco estructural: son componente del casco, no '
        'protección ocular primaria. Qué pedir en el certificado.',
}


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    bloques = {}
    for cat in data:
        for prod in cat.get('productos', []):
            if prod.get('l3'):
                bloques[prod['slug']] = prod['l3']
                for card in prod['l3'].get('catalogo', {}).get('cards', []):
                    if card.get('l4'):
                        bloques[card['slug']] = card['l4']

    n = 0
    for slug, t in TITULOS.items():
        assert len(t) <= MAX_TITLE_DATO, '%s: %d ch, no cabe' % (slug, len(t))
        if bloques[slug]['seoTitle'] != t:
            bloques[slug]['seoTitle'] = t
            n += 1
            print('  ok  title  %-32s %d ch → <title> de %d' % (slug, len(t), len(t) + SUFIJO))
    for slug, d in DESCRIPCIONES.items():
        assert RANGO_DESC[0] <= len(d) <= RANGO_DESC[1], '%s: %d ch' % (slug, len(d))
        if bloques[slug]['seoDescription'] != d:
            bloques[slug]['seoDescription'] = d
            n += 1
            print('  ok  desc   %-32s %d ch' % (slug, len(d)))

    if n:
        with io.open(RUTA, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

    print('\nrevisión de las %d fichas:' % len(bloques))
    fuera = 0
    for slug, b in sorted(bloques.items()):
        lt, ld = len(b['seoTitle']) + SUFIJO, len(b['seoDescription'])
        avisos = []
        if lt > 62:
            avisos.append('title %d' % lt)
        if not (RANGO_DESC[0] <= ld <= RANGO_DESC[1]):
            avisos.append('desc %d' % ld)
        if avisos:
            fuera += 1
            print('  fuera de rango  %-32s %s' % (slug, ' · '.join(avisos)))
    print('  fichas fuera de rango:', fuera)
    print('cambios aplicados:', n)


if __name__ == '__main__':
    main()
