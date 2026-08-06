#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dos correcciones que obliga a hacer la L3 de viseras y caretas.

1) La card L2 del producto vendia "antirrayadura" como si fuera una especificacion, y prometia
   "montaje directo al casco" y "reemplazable sin herramienta" para toda la linea. Verificado
   contra fuente primaria:
     · ningun fabricante del mercado NFPA publica un dato de abrasion (ni marcado EN 166 "K"
       ni ciclos ni dispersion de luz): "antirrayadura" es adjetivo de folleto;
     · "sin herramienta" aplica a los visores retractiles y a los sistemas de acople rapido,
       NO a las caretas externas, que se ajustan con perillas y cuyo herraje se vende aparte;
       y hay un casco tipo jet del mercado cuyo componente optico requiere herramienta Torx.
   Tambien se quita el implicito de que la careta protege los ojos: NFPA 1500 dice que usada
   sola no es proteccion ocular primaria.

2) La entrada NOM-115-STPS de `cat.normas` decia "criterios de retiro de servicio". El texto
   oficial de la norma (stps.gob.mx) clasifica cascos en clases G, E y C y prueba impacto,
   penetracion, tension electrica y combustion; no se localizo un apartado de retiro de
   servicio, y sobre todo NO cubre proteccion ocular ni facial. Se reescribe con lo verificable
   y se agregan las dos normas que esta linea necesita y que faltaban en la categoria:
   ANSI/ISEA Z87.1 y NFPA 1500.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

DESC = ('Protección facial para el casco estructural: visor retráctil integrado, careta externa '
        'de 4 y 6 pulgadas, Bourkes y goggles. Es componente del casco, se certifica con él y no '
        'sustituye a la pieza facial del equipo de respiración.')

SPECS = [
    'Visor retráctil, careta, Bourkes o goggles',
    'Componente del casco, no producto certificado',
    'Transmitancia mínima de 85 % en lente claro',
    'Lente de repuesto con número de parte publicado',
]

INTRO = [
    ('Careta y goggles no son lo mismo y ninguno de los dos sustituye a la pieza facial del '
     'equipo de respiración. La <strong>careta abatible</strong> montada al casco cubre el rostro '
     'de calor y proyecciones en maniobras sin equipo de respiración puesto; los '
     '<strong>goggles calificados Z87+</strong> son los que la norma reconoce como protección '
     'ocular primaria cuando no se trae la pieza facial. Por eso en una partida van '
     '<strong>dos renglones</strong>, no uno: protección facial y protección ocular.'),
    ('Para proximidad y rescate en aeronaves existe la <strong>careta chapada en oro</strong> con '
     'cubierta aluminizada, cuya reflectividad ningún fabricante publica —lo que sí exige la '
     'norma es transmitancia mínima de 30 %—. Todas estas piezas se cotizan contra la '
     '<strong>serie y el número de parte del casco</strong>, porque la certificación se emite '
     'para el casco completo y el herraje de montaje se vende aparte. Y el dato de compra que '
     'más se olvida es el <strong>número de parte del lente de repuesto</strong>: el componente '
     'óptico no se retira por antigüedad, se reemplaza cuando falla la inspección.'),
]

NOM115 = ('Cascos de protección: clases G, E y C, con métodos de prueba de impacto, penetración, '
          'tensión eléctrica y combustión. No cubre protección ocular ni facial, y llama '
          '“visera” al ala del casco.')

NUEVAS = [
    collections.OrderedDict([
        ('code', 'ANSI/ISEA Z87.1'),
        ('desc', 'Protección ocular y facial ocupacional. El marcado Z87+ indica alto impacto; no '
                 'aborda calor ni calor radiante, así que no sustituye a la certificación NFPA.'),
    ]),
    collections.OrderedDict([
        ('code', 'NFPA 1500'),
        ('desc', 'Programa de seguridad y salud. Es la que define qué cuenta como protección '
                 'ocular primaria: la pieza facial del SCBA y los goggles Z87+, no la visera sola.'),
    ]),
]

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'viseras-y-caretas')

cambios = []
if prod['desc'] != DESC:
    prod['desc'] = DESC
    cambios.append('desc')
if prod['specs'] != SPECS:
    prod['specs'] = SPECS
    cambios.append('specs')
if prod.get('intro') != INTRO:
    prod['intro'] = INTRO
    cambios.append('intro')

normas = cat.setdefault('normas', [])
n115 = next((n for n in normas if n['code'] == 'NOM-115-STPS'), None)
if n115 is not None and n115.get('desc') != NOM115:
    n115['desc'] = NOM115
    cambios.append('normas/NOM-115-STPS')

codes = {n['code'] for n in normas}
for nueva in NUEVAS:
    if nueva['code'] not in codes:
        normas.append(nueva)
        cambios.append('normas/+%s' % nueva['code'])

if cambios:
    with io.open(RUTA, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

print('cambios:', ', '.join(cambios) if cambios else 'ninguno, ya estaba corregido')
print('normas de la categoria:', ', '.join(n['code'] for n in normas))
