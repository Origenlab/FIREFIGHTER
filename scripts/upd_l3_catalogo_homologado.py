# -*- coding: utf-8 -*-
"""Homologa el catalogo de marca de la L3 al patron de card del index.

Cambios:
- Todas las cards iguales: se elimina la destacada horizontal.
- 4 specs exactos en todas.
- `marca` y `modelo` pasan a la CARD, no al catalogo: asi entran varias marcas.
- `variante` + `varianteLabel` describen la configuracion (barrera, presentacion, medida...).
- `badge` es la NORMA, como en el index.
"""
import json, io, collections, os

RUTA = 'src/data/productos.json'

CARDS = [
  collections.OrderedDict([
    ("marca", "SKÖLD"),
    ("modelo", "HERÖ"),
    ("variante", "PBI MAX 7.0"),
    ("varianteLabel", "Barrera exterior"),
    ("badge", "NFPA 1971 · 2018"),
    ("estado", "documentada"),
    ("img", "/images/catalogo/1592235905030-1000x750.webp"),
    ("alt", "Bombero con ensamble estructural completo, casco y equipo de respiración autónoma"),
    ("desc", (
      "La única configuración del HERÖ con composición y gramaje publicados. Exterior PBI MAX de "
      "7 oz en <strong>70 % PBI y 30 % Kevlar</strong>, con Stedair 3000 y Defender M. Es la "
      "referencia contra la que se compara cualquier otra propuesta."
    )),
    ("specs", [
      "Exterior 70 % PBI y 30 % Kevlar, 7 oz",
      "Barrera de humedad Stedair 3000",
      "Barrera térmica Defender M",
      "Tallas S a 4X · chaquetón, pantalón o completo",
    ]),
    ("chip", "Certificación UL · expediente MH60435"),
  ]),
  collections.OrderedDict([
    ("marca", "SKÖLD"),
    ("modelo", "HERÖ"),
    ("variante", "Advance"),
    ("varianteLabel", "Barrera exterior"),
    ("badge", "NFPA 1971 · 2018"),
    ("estado", "sin-ficha"),
    ("img", "/images/catalogo/1575507371089-600x450.webp"),
    ("alt", "Chaquetones y cascos estructurales colgados en la estación de bomberos"),
    ("desc", (
      "Barrera exterior seleccionable del HERÖ. La ficha del modelo no publica composición ni "
      "gramaje, y sin gramaje no se puede comparar peso ni carga térmica contra PBI MAX."
    )),
    ("specs", [
      "Barrera exterior seleccionable del HERÖ",
      "Composición y gramaje no publicados",
      "Mismo conjunto: DRD, cuello 360°, arnés Kevlar",
      "Se solicita ficha de la configuración",
    ]),
    ("chip", "Requiere ficha por configuración"),
  ]),
  collections.OrderedDict([
    ("marca", "SKÖLD"),
    ("modelo", "HERÖ"),
    ("variante", "Kombat Flex"),
    ("varianteLabel", "Barrera exterior"),
    ("badge", "NFPA 1971 · 2018"),
    ("estado", "sin-ficha"),
    ("img", "/images/catalogo/1705503831904-600x450.webp"),
    ("alt", "Detalle de cintas reflejantes trilaminadas y accesorios sobre un traje estructural"),
    ("desc", (
      "Barrera exterior seleccionable del HERÖ. El nombre comercial sugiere flexibilidad, pero el "
      "fabricante no publica ensayo que lo sostenga: no atribuimos desempeño a un nombre."
    )),
    ("specs", [
      "Barrera exterior seleccionable del HERÖ",
      "Composición y gramaje no publicados",
      "Mismo conjunto: DRD, cuello 360°, arnés Kevlar",
      "Sin ensayo publicado de flexibilidad",
    ]),
    ("chip", "Requiere ficha por configuración"),
  ]),
  collections.OrderedDict([
    ("marca", "SKÖLD"),
    ("modelo", "HERÖ"),
    ("variante", "Pioneer"),
    ("varianteLabel", "Barrera exterior"),
    ("badge", "NFPA 1971 · 2018"),
    ("estado", "sin-ficha"),
    ("img", "/images/catalogo/1651368615152-600x450.webp"),
    ("alt", "Rack de equipo de protección personal estructural listo por turno en la estación"),
    ("desc", (
      "Barrera exterior seleccionable del HERÖ. El certificado se emite sobre el "
      "<strong>ensamble completo</strong>: cambiar la capa exterior cambia el alcance del expediente."
    )),
    ("specs", [
      "Barrera exterior seleccionable del HERÖ",
      "Composición y gramaje no publicados",
      "El certificado aplica al ensamble, no a la capa",
      "Se solicita ficha de la configuración",
    ]),
    ("chip", "Requiere ficha por configuración"),
  ]),
  collections.OrderedDict([
    ("marca", "SKÖLD"),
    ("modelo", "HERÖ"),
    ("variante", "Defender 750"),
    ("varianteLabel", "Barrera exterior"),
    ("badge", "NFPA 1971 · 2018"),
    ("estado", "sin-ficha"),
    ("img", "/images/catalogo/1563062067-bb-600x450.webp"),
    ("alt", "Bombero de perfil con ensamble estructural completo y equipo de respiración"),
    ("desc", (
      "Barrera exterior seleccionable del HERÖ. <strong>No confundir con Defender M</strong>, que es "
      "la barrera térmica de la configuración PBI MAX: son capas distintas del ensamble."
    )),
    ("specs", [
      "Barrera exterior seleccionable del HERÖ",
      "Composición y gramaje no publicados",
      "Defender 750 es exterior; Defender M es térmica",
      "Se solicita ficha de la configuración",
    ]),
    ("chip", "Requiere ficha por configuración"),
  ]),
]

CATALOGO = collections.OrderedDict([
  ("eyebrow", "Catálogo por marca"),
  ("titulo", "Trajes estructurales<br>por marca y configuración"),
  ("intro", (
    "Cada marca nombra distinto lo mismo: unas venden por <strong>modelo</strong>, otras por "
    "<strong>barrera exterior</strong> y otras por presentación. Aquí cada card es una "
    "configuración cotizable, con la norma que declara el fabricante y el dato que hay que pedir "
    "antes de compararla contra otra. Hoy está publicado el <strong>SKÖLD HERÖ</strong> con sus "
    "cinco barreras exteriores; el catálogo crece por marca."
  )),
  ("imgRef", "Imagen de referencia del conjunto"),
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
  ("cards", CARDS),
])

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')
prod['l3']['catalogo'] = CATALOGO

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

faltan = [c['img'] for c in CARDS if not os.path.exists('public' + c['img'])]
marcas = sorted({c['marca'] for c in CARDS})
print('cards:', len(CARDS), '| marcas:', marcas, '| imagenes faltantes:', faltan or 'ninguna')
malos = [c['variante'] for c in CARDS if len(c['specs']) != 4]
print('cards que no traen exactamente 4 specs:', malos or 'ninguna')
