# -*- coding: utf-8 -*-
"""Corrige la card y el módulo L2 de botas para que no contradigan la ficha L3.

La redacción anterior decía "suela dieléctrica que aísla del contacto eléctrico". Ningún
fabricante consultado declara aislamiento eléctrico permanente: declaran resistencia eléctrica
medida en un ENSAYO (18 kV en HAIX Fire Hero Xtreme, 14 kV en Fire Flash Xtreme), que no
equivale al calzado dieléctrico que regula la NOM-113-STPS para tarea eléctrica. Idempotente.
"""
import json, io, collections

RUTA = 'src/data/productos.json'

DESC = ("Bota estructural de caña alta con puntera compuesta o de acero, plantilla antipunción, "
        "barrera de humedad y suela con resistencia eléctrica declarada en ensayo del fabricante. "
        "En piel o en caucho vulcanizado, con anchos publicados además de la curva de tallas.")

SPECS = [
    "Caña de 11\" a 16\" según modelo",
    "Puntera compuesta o de acero",
    "Plantilla antipunción de acero o composite",
    "Anchos publicados, no solo curva de tallas",
]

INTRO = [
    ("En una estructura incendiada el piso es el peligro que nadie ve: clavos, varilla expuesta, "
     "vidrio y cable bajo el agua. La <strong>bota estructural para bombero</strong> responde con "
     "cuatro protecciones simultáneas —<strong>puntera</strong> contra aplastamiento, "
     "<strong>plantilla antipunción</strong> de acero o composite, <strong>barrera de humedad</strong> "
     "y una suela con <strong>resistencia eléctrica declarada en ensayo</strong>—. Ese último punto "
     "es el más malentendido del rubro: un valor de ensayo no es lo mismo que el calzado dieléctrico "
     "que regula la <strong>NOM-113-STPS</strong> para tarea eléctrica, y confundir las dos "
     "categorías es lo que aparece en verificación."),
    ("Surtimos la versión en piel, más ligera para jornadas largas, y la de caucho vulcanizado, que "
     "se calza en segundos y resiste mejor la inmersión, con caña de 11\" a 16\" según modelo. La "
     "caña alta traslapa con el pantalón estructural para que no quede zona expuesta. Levantamos "
     "<strong>talla y ancho por usuario</strong>, no solo la curva de tallas: los sistemas de ancho "
     "de cada marca no son equivalentes y una talla correcta con ancho incorrecto sigue produciendo "
     "calzado inservible. Un calzado genérico de seguridad industrial <strong>no sustituye</strong> "
     "a una bota estructural."),
]

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'botas-dielectricas')
# El nombre se homologa con el H1 de la ficha: la categoria de producto es "bota estructural".
# El slug se conserva (`botas-dielectricas`) porque es el termino que se busca en Mexico y
# porque cambiarlo rompe la URL; el termino sigue cubierto en el cuerpo de la ficha.
prod['nombre'] = 'Botas estructurales'
prod['desc'] = DESC
prod['specs'] = SPECS
prod['intro'] = INTRO

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('card L2 de', prod['slug'], 'actualizada')
print('  desc:', len(DESC), 'ch | specs:', len(SPECS), '| intro:', [len(p) for p in INTRO])
