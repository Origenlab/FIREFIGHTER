# -*- coding: utf-8 -*-
"""Agrega heroBloques al bloque l3 de trajes-estructurales-nomex-pbi.
El hero de la L3 deja de llevar foto y pasa a dos parrafos de marketing con SEO,
homologado al hero de la L2."""
import json, io, collections

RUTA = 'src/data/productos.json'

HERO_BLOQUES = [
    {
        "label": "Por qué la especificación importa",
        "texto": (
            "Un <strong>traje estructural para bombero</strong> mal especificado no falla en la bodega: "
            "falla dentro de una estructura, cuando una barrera de humedad vencida deja pasar vapor "
            "sobrecalentado y el elemento se quema con un ensamble que en papel cumplía. La verificación "
            "en México llega por dos frentes —<strong>NFPA 1970</strong> sobre el ensamble y "
            "<strong>NOM-017-STPS</strong> sobre su entrega y capacitación—, y un expediente incompleto "
            "detiene una licitación antes de que alguien mire el precio."
        ),
    },
    {
        "label": "Distribución autorizada, no reventa",
        "texto": (
            "Distribuimos chaquetón y pantalón en <strong>Nomex IIIA y PBI Matrix</strong> directo de "
            "fabricante, en tallas de XS a 4XL con corte para hombre y mujer, con certificado del ensamble, "
            "número de serie trazable y ficha técnica en español. Entregamos "
            "<strong>propuesta técnica en menos de 24 horas hábiles</strong> y equipamos cuerpos de bomberos, "
            "brigadas industriales y unidades de protección civil en los "
            "<strong>32 estados de la República</strong>."
        ),
    },
]

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')

# heroBloques va justo despues de heroImg para que el JSON se lea en orden
l3 = prod['l3']
nuevo = collections.OrderedDict()
for k, v in l3.items():
    nuevo[k] = v
    if k == 'heroImg':
        nuevo['heroBloques'] = HERO_BLOQUES
prod['l3'] = nuevo

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('heroBloques:', len(HERO_BLOQUES))
for b in HERO_BLOQUES:
    import re
    plano = re.sub(r'<[^>]+>', '', b['texto'])
    print(' -', b['label'], '|', len(plano), 'ch')
