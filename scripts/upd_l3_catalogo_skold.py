# -*- coding: utf-8 -*-
"""Segunda pasada del catalogo SKOLD: imagen por card, card destacada horizontal y boton.

Las cinco fotos NO se repiten con la galeria de esta ficha:
  1592235905030-1000x750  libre en todo el sitio
  1575507371089 / 1705503831904 / 1651368615152  son cat.imagenes de la L2, no de esta L3
  1563062067-bb  pertenece a la ficha de capucha, no a esta

Son fotos de referencia del conjunto estructural, no de cada barrera: cada card lo rotula.
"""
import json, io, collections

RUTA = 'src/data/productos.json'

IMGS = {
  "PBI MAX 7.0": {
    "src": "/images/catalogo/1592235905030-1000x750.webp",
    "alt": "Bombero con ensamble estructural completo, casco y equipo de respiración autónoma certificado NFPA",
  },
  "Advance": {
    "src": "/images/catalogo/1575507371089-600x450.webp",
    "alt": "Chaquetones y cascos estructurales colgados en la estación de bomberos",
  },
  "Kombat Flex": {
    "src": "/images/catalogo/1705503831904-600x450.webp",
    "alt": "Detalle de cintas reflejantes trilaminadas y accesorios sobre un traje estructural",
  },
  "Pioneer": {
    "src": "/images/catalogo/1651368615152-600x450.webp",
    "alt": "Rack de equipo de protección personal estructural listo por turno en la estación",
  },
  "Defender 750": {
    "src": "/images/catalogo/1563062067-bb-600x450.webp",
    "alt": "Bombero de perfil con ensamble estructural completo y equipo de respiración",
  },
}

# Textos mas cortos: la card ahora carga imagen y boton, el parrafo no puede ser un ladrillo
DESCS = {
  "PBI MAX 7.0": (
    "La única de las cinco con composición y gramaje publicados. Exterior PBI MAX de 7 oz en "
    "<strong>70 % PBI y 30 % Kevlar</strong>, barrera de humedad Stedair 3000 y barrera térmica "
    "Defender M, sobre el conjunto HERÖ completo: DRD integrado, cuello de cobertura 360°, arnés "
    "de Kevlar y costura de Kevlar doble y triple. Es la configuración de referencia para "
    "comparar cualquier otra propuesta."
  ),
  "Advance": (
    "Barrera exterior seleccionable del HERÖ. La ficha del modelo no publica composición ni "
    "gramaje, y sin gramaje no se puede comparar peso ni carga térmica contra PBI MAX."
  ),
  "Kombat Flex": (
    "Barrera exterior seleccionable del HERÖ. El nombre comercial sugiere flexibilidad, pero el "
    "fabricante no publica ensayo que lo sostenga: no atribuimos desempeño a un nombre."
  ),
  "Pioneer": (
    "Barrera exterior seleccionable del HERÖ. El certificado se emite sobre el "
    "<strong>ensamble completo</strong>: cambiar la capa exterior cambia el alcance del expediente."
  ),
  "Defender 750": (
    "Barrera exterior seleccionable del HERÖ. <strong>No confundir con Defender M</strong>, que es "
    "la barrera térmica de la configuración PBI MAX: son capas distintas del ensamble."
  ),
}

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')
catalogo = prod['l3']['catalogo']

catalogo['imgRef'] = 'Imagen de referencia del conjunto'
catalogo['intro'] = (
    "El <strong>SKÖLD HERÖ</strong> no es una sola tela: el fabricante lista cinco barreras "
    "exteriores seleccionables sobre el mismo conjunto estructural. Cambiar la barrera cambia el "
    "peso, el desempeño y el certificado aplicable, así que la cotización tiene que nombrarla "
    "junto con el color, la talla y la clave de producto."
)

for c in catalogo['cards']:
    c['img'] = IMGS[c['barrera']]['src']
    c['alt'] = IMGS[c['barrera']]['alt']
    c['desc'] = DESCS[c['barrera']]
    # Orden de llaves estable para que el JSON se lea bien
    orden = ['n', 'barrera', 'badge', 'estado', 'img', 'alt', 'desc', 'specs', 'chip']
    nuevo = collections.OrderedDict((k, c[k]) for k in orden if k in c)
    for k, v in c.items():
        if k not in nuevo:
            nuevo[k] = v
    c.clear()
    c.update(nuevo)

# La card destacada gana una linea mas de specs: es la unica con datos publicados
ref = next(c for c in catalogo['cards'] if c['estado'] == 'ficha')
ref['specs'] = [
    "Exterior 70 % PBI y 30 % Kevlar, 7 oz",
    "Barrera de humedad Stedair 3000",
    "Barrera térmica Defender M",
    "DRD integrado y arnés de Kevlar",
    "Cuello de cobertura 360° sin partes expuestas",
    "Tallas S a 4X · chaquetón, pantalón o traje completo",
]

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

import os
faltan = [c['img'] for c in catalogo['cards'] if not os.path.exists('public' + c['img'])]
print('cards:', len(catalogo['cards']), '| imagenes faltantes:', faltan or 'ninguna')
for c in catalogo['cards']:
    print(' ', c['n'], c['barrera'].ljust(14), c['img'], '·', len(c['specs']), 'specs')
