# -*- coding: utf-8 -*-
"""Corrige la card y el módulo L2 de cascos para que no contradigan la ficha L3.

La redacción anterior decía "suspensión ajustable de cuatro puntos" y atribuía a la
suspensión la absorción del impacto. Ningún fabricante consultado declara "cuatro puntos"
—Bullard describe tres tiras sobre seis llaves, MSA una suspensión de seis vías— y la pieza
que absorbe la energía es la cofia de impacto, no la suspensión. Idempotente.
"""
import json, io, collections

RUTA = 'src/data/productos.json'

DESC = ("Casco estructural con coquilla de composite termoestable o termoplástico de alta "
        "temperatura, cofia de impacto, suspensión con ratchet y ajuste de altura, protección "
        "facial abatible y orejeras desmontables. Compatible con pieza facial de SCBA.")

SPECS = [
    "Coquilla resistente a impacto, penetración y calor radiante",
    "Protección facial abatible, Bourkes o goggles según serie",
    "Suspensión, barboquejo y orejeras reemplazables por parte",
    "Alojamiento para lámpara y compatibilidad con pieza facial",
]

INTRO = [
    ("El <strong>casco de bombero</strong> resuelve tres riesgos a la vez: impacto por caída de "
     "material, penetración por objeto punzante y calor radiante. La coquilla desvía y reparte la "
     "carga sin deformarse, y la que absorbe la energía es la <strong>cofia de impacto</strong> "
     "que va por dentro —por eso un golpe puede comprometer el casco sin dejar marca visible—. La "
     "suspensión sostiene la separación entre cráneo y coquilla, define el rango de talla y se "
     "ajusta por elemento. Tenemos el estilo tradicional de ala completa y el perfil moderno tipo "
     "jet, que pesa menos y estorba menos en espacios reducidos."),
    ("Todos son compatibles con pieza facial de SCBA y traen alojamiento para lámpara, orejeras "
     "desmontables y protección facial abatible; los goggles se especifican aparte, porque la "
     "careta montada al casco no cuenta como protección ocular primaria. Personalizamos con número "
     "de unidad, nombre de la corporación y código de color por rango o función, algo que en una "
     "escena con varias corporaciones deja de ser estética y se vuelve control de mando. "
     "Distribuimos <strong>Bullard y MSA</strong> con refacciones de suspensión, barboquejo, "
     "orejeras y visera disponibles por número de parte."),
]

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
prod = next(p for p in cat['productos'] if p['slug'] == 'cascos-bullard-y-msa')
prod['desc'] = DESC
prod['specs'] = SPECS
prod['intro'] = INTRO

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('card L2 de', prod['slug'], 'actualizada')
print('  desc:', len(DESC), 'ch | specs:', len(SPECS), '| intro:', [len(p) for p in INTRO])
