#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrige la card L2 de guantes: describia UNA construccion como si fuera toda la linea.

El texto heredado decia "palma de piel tratada, dorso aramidico y membrana impermeable
transpirable" y "puno largo con ajuste de muneca". El catalogo que ahora publica la L3
desmiente las tres cosas:

  · la concha no siempre es piel: la Pro-Tech 8 Titan Pro es compuesto de Kevlar con Litex
    fusionado con silicon, SIN piel, y es la unica del catalogo con TPP declarado > 60;
  · la barrera no es una sola ni siempre se llama "membrana transpirable": hay poliuretano
    libre de PFAS, Porelle DXT PRO e inserto GORE CROSSTECH, y se declara POR MODELO;
  · el puno largo no es la unica opcion: gauntlet y wristlet son dos configuraciones y
    varios fabricantes publican el mismo guante en las dos (Shelby 5228/5227, Majestic
    M7G/M7W). Prometer "puno largo" en la card contradice la mitad del catalogo.

Se reescriben `desc` y `specs` con lo que si es comun a la linea y con lo que de verdad
diferencia un guante de otro. Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

DESC = ('Guante estructural en piel de canguro, koala o búfalo de agua, o en compuesto de '
        'Kevlar sin piel, con barrera de humedad declarada por modelo y puño gauntlet o '
        'wristlet. Curvas de tallas de XXS a Jumbo según fabricante.')

SPECS = [
    'Concha de piel de canguro, koala, búfalo o Kevlar sin piel',
    'Barrera de humedad declarada por modelo, no supuesta',
    'Gauntlet o wristlet: dos configuraciones, no una',
    'Talla por usuario, con curvas de hasta once tallas',
]

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'guantes-de-intervencion')

cambio = prod['desc'] != DESC or prod['specs'] != SPECS
prod['desc'] = DESC
prod['specs'] = SPECS

if cambio:
    with io.open(RUTA, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('card L2 de guantes corregida')
else:
    print('card L2 de guantes ya estaba corregida')

print('  desc:', prod['desc'])
for s in prod['specs']:
    print('  spec:', s)
