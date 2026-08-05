# -*- coding: utf-8 -*-
"""Catalogo de 5 cards SKOLD HERO en la ficha L3 de trajes estructurales.

Fuente: ficha tecnica FT_HEROPBI_2023(B) de SKOLD + pagina oficial del modelo HERO.
Datos ya verificados en el proyecto LGACONTRAINCENDIOS (src/data/productos/trajeSkoldHero.mjs).
Solo PBI MAX 7.0 tiene composicion y gramaje publicados; las otras cuatro barreras estan
listadas por el fabricante sin ficha publica. No se inventa nada.
"""
import json, io, collections

RUTA = 'src/data/productos.json'

CATALOGO = collections.OrderedDict([
  ("eyebrow", "Catálogo SKÖLD"),
  ("titulo", "SKÖLD HERÖ en sus<br>5 configuraciones"),
  ("label", "La barrera exterior define el certificado"),
  ("intro", (
    "El <strong>SKÖLD HERÖ</strong> no es una sola tela: el fabricante lista cinco barreras "
    "exteriores seleccionables sobre el mismo conjunto estructural —DRD integrado, cuello de "
    "cobertura 360°, arnés de Kevlar y costura de Kevlar doble y triple—. "
    "Cambiar la barrera cambia el peso, el desempeño y el certificado aplicable, así que la "
    "cotización debe nombrarla junto con el color, la talla y la clave de producto."
  )),
  ("marca", "SKÖLD"),
  ("modelo", "HERÖ"),
  ("nota", (
    "La certificación UL publicada por SKÖLD para el HERÖ está declarada bajo "
    "<strong>NFPA 1971 edición 2018</strong>, expediente <strong>MH60435</strong>. "
    "Esa edición fue consolidada en <strong>NFPA 1970 (1971) edición 2025</strong> y la "
    "transición cerró el 18 de marzo de 2026, por lo que un certificado emitido hoy debe "
    "referirse a la edición vigente. El inventario ya etiquetado no se invalida —su uso en "
    "campo se rige por NFPA 1850 (1851)—, pero en la compra hay que precisar qué edición "
    "ampara el certificado que se entrega. La verificación es por unidad: expediente, edición, "
    "modelo, configuración de barreras, talla y etiqueta cosida."
  )),
  ("cards", [
    {
      "n": "01",
      "barrera": "PBI MAX 7.0",
      "badge": "Configuración documentada",
      "estado": "ficha",
      "desc": (
        "La única de las cinco con composición y gramaje publicados. Es la configuración de la "
        "ficha técnica FT_HEROPBI_2023(B): exterior PBI MAX de 7 oz en 70 % PBI y 30 % Kevlar, "
        "barrera de humedad Stedair 3000 y barrera térmica Defender M."
      ),
      "specs": [
        "Exterior 70 % PBI y 30 % Kevlar, 7 oz",
        "Barrera de humedad Stedair 3000",
        "Barrera térmica Defender M",
        "Tallas S a 4X · chaquetón, pantalón o traje completo",
      ],
      "chip": "Certificación UL · expediente MH60435",
    },
    {
      "n": "02",
      "barrera": "Advance",
      "badge": "Barrera seleccionable",
      "estado": "ficha-pendiente",
      "desc": (
        "Listada por SKÖLD entre las cinco barreras exteriores del HERÖ. La ficha del modelo no "
        "publica composición ni gramaje, y sin gramaje no se puede comparar peso ni carga térmica "
        "contra PBI MAX. Pedimos la ficha de la configuración antes de ponerlas en la misma tabla."
      ),
      "specs": [
        "Barrera exterior seleccionable del HERÖ",
        "Composición y gramaje no publicados",
        "Mismo conjunto: DRD, cuello 360°, arnés de Kevlar",
        "Se solicita ficha técnica de la configuración",
      ],
      "chip": "Requiere ficha por configuración",
    },
    {
      "n": "03",
      "barrera": "Kombat Flex",
      "badge": "Barrera seleccionable",
      "estado": "ficha-pendiente",
      "desc": (
        "Listada por SKÖLD entre las cinco barreras exteriores del HERÖ. El nombre comercial "
        "sugiere flexibilidad, pero el fabricante no publica ensayo ni gramaje que lo sostenga: "
        "no atribuimos desempeño a un nombre. La afirmación tiene que venir en la ficha."
      ),
      "specs": [
        "Barrera exterior seleccionable del HERÖ",
        "Composición y gramaje no publicados",
        "Mismo conjunto: DRD, cuello 360°, arnés de Kevlar",
        "Sin ensayo publicado de flexibilidad",
      ],
      "chip": "Requiere ficha por configuración",
    },
    {
      "n": "04",
      "barrera": "Pioneer",
      "badge": "Barrera seleccionable",
      "estado": "ficha-pendiente",
      "desc": (
        "Listada por SKÖLD entre las cinco barreras exteriores del HERÖ. Conviene recordar que el "
        "certificado se emite sobre el <strong>ensamble completo</strong>: sustituir la barrera "
        "exterior cambia el alcance del expediente, aunque el modelo y el resto de las capas sean "
        "los mismos."
      ),
      "specs": [
        "Barrera exterior seleccionable del HERÖ",
        "Composición y gramaje no publicados",
        "El certificado aplica al ensamble, no a la capa",
        "Se solicita ficha técnica de la configuración",
      ],
      "chip": "Requiere ficha por configuración",
    },
    {
      "n": "05",
      "barrera": "Defender 750",
      "badge": "Barrera seleccionable",
      "estado": "ficha-pendiente",
      "desc": (
        "Listada por SKÖLD entre las cinco barreras exteriores del HERÖ. <strong>No confundir con "
        "Defender M</strong>, que es la barrera térmica de la configuración PBI MAX: son capas "
        "distintas del ensamble y se han pedido mal en más de una requisición."
      ),
      "specs": [
        "Barrera exterior seleccionable del HERÖ",
        "Composición y gramaje no publicados",
        "Defender 750 es exterior; Defender M es térmica",
        "Se solicita ficha técnica de la configuración",
      ],
      "chip": "Requiere ficha por configuración",
    },
  ]),
])

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')

l3 = prod['l3']
nuevo = collections.OrderedDict()
for k, v in l3.items():
    nuevo[k] = v
    if k == 'specStrip':
        nuevo['catalogo'] = CATALOGO
prod['l3'] = nuevo

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('cards:', len(CATALOGO['cards']))
for c in CATALOGO['cards']:
    print(' ', c['n'], c['barrera'], '·', len(c['specs']), 'specs')
