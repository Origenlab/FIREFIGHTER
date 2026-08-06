#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quita el olor a plantilla de las 17 fichas ya publicadas de EPP para bomberos.

Que detecto la auditoria editorial:

  · 11 de 11 fichas L4 cerraban la galeria con la MISMA frase, porque estaba escrita a mano
    dentro de la plantilla .astro. Igual las 6 L3 con otra frase identica entre ellas.
  · 10 fichas repetian el encabezado de tabla "Dato ausente · Que decide · ...", 4 el de
    "Decision · Opciones publicadas · Como se escribe en la partida" y 4 el de
    "En la partida escribe · En lugar de".
  · 6 fichas usaban el eyebrow "Lo que el fabricante no publica" y 4 el de "Lo que falta".

Nada de eso es un error de dato: es voz. Un catalogo profesional puede repetir la ESTRUCTURA
—de hecho conviene, el comprador aprende a leerla— pero no la LETRA, porque entonces las
fichas hermanas se leen como generadas y no como escritas.

Criterio de la correccion: cada encabezado y cada eyebrow nombra el objeto de ESA ficha.
Donde antes decia "Dato ausente" ahora dice "Lo que no dice la hoja del casco",
"Hueco de la ficha", "Dato que no aparece en el manual"... segun lo que la ficha tenga enfrente.

Idempotente: si un valor ya esta cambiado, lo deja.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

# ── 1 · Encabezados de tabla, uno por ficha ───────────────────────────────────
# slug de ficha -> { id de seccion: [nuevos encabezados] }
HEADS = {
    'skold-hero-advance': {'lo-no-publicado': ['Hueco de la ficha', 'De qué depende', 'Qué pasa si no llega'],
                           'anexo': ['Redacción que sirve', 'Redacción que se presta a interpretación']},
    'skold-hero-kombat-flex': {'lo-no-publicado': ['Dato sin publicar', 'Qué define en movilidad', 'Riesgo de no pedirlo'],
                               'anexo': ['Cómo pedirlo para que se cumpla', 'Cómo suele escribirse']},
    'skold-hero-pioneer': {'lo-no-publicado': ['Capa o valor ausente', 'Qué queda sin definir', 'Consecuencia en el certificado'],
                           'anexo': ['Texto que amarra el ensamble', 'Texto que lo deja abierto']},
    'skold-hero-defender-750': {'lo-no-publicado': ['Lo que no está en la hoja', 'Qué decide', 'Qué cuesta no tenerlo'],
                                'anexo': ['Cómo se escribe sin ambigüedad', 'Cómo se escribe hoy']},
    'bullard-px-series': {'claves': ['Qué se elige', 'Lo que Bullard publica', 'Cómo se escribe en la orden'],
                          'lo-no-publicado': ['Dato que la PX no trae', 'Para qué se necesita', 'Dónde se consigue']},
    'bullard-ust-traditional': {'configuracion': ['Punto de decisión', 'Alternativas de la serie', 'Cómo queda en la orden'],
                                'lo-no-publicado': ['Hueco de la hoja de licitación', 'Qué decide', 'Cómo se cierra']},
    'bullard-lt-series': {'lo-no-publicado': ['Cifra que el manual no da', 'Qué se compara con ella', 'Cómo se obtiene']},
    'msa-cairns-1836': {'lo-no-publicado': ['Dato fuera de la ficha técnica', 'Qué resuelve', 'Cómo pedirlo']},
    'msa-cairns-660c-metro': {'sin-peso-ni-edicion': ['Lo que MSA no publica del 660C', 'Qué decide', 'Cómo se suple'],
                              'configuracion': ['Qué se define', 'Configuraciones publicadas', 'Cómo se pide']},
    'msa-cairns-xf1': {'lo-no-publicado': ['Ausencia en la página de producto', 'Qué queda sin resolver', 'Cómo se pregunta'],
                       'configuracion': ['Qué hay que elegir', 'Lo que publica MSA', 'Cómo se redacta']},
}

# ── 2 · Eyebrows, uno por ficha ───────────────────────────────────────────────
EYEBROWS = {
    'skold-hero-advance': {'lo-no-publicado': 'Los cinco huecos'},
    'skold-hero-kombat-flex': {'lo-no-publicado': 'Movilidad sin cifras'},
    'skold-hero-pioneer': {'lo-no-publicado': 'Composite sin declarar'},
    'skold-hero-defender-750': {'lo-no-publicado': 'Después del nombre, el dato'},
    'bullard-px-series': {'lo-no-publicado': 'Cuatro preguntas al fabricante'},
    'bullard-ust-traditional': {'lo-no-publicado': 'Hasta la hoja más completa'},
    'bullard-lt-series': {'lo-no-publicado': 'Fuerte en operación, débil en cifras'},
    'msa-cairns-1836': {'lo-no-publicado': 'Tres huecos de la mejor documentada'},
    'msa-cairns-660c-metro': {'sin-peso-ni-edicion': 'Sin peso y sin edición'},
    'msa-cairns-xf1': {'lo-no-publicado': 'Lo que la página no dice'},
    'skold-hero-pbi-max-7-0': {'cbrn': 'La opción que no se documenta sola'},
}

# ── 3 · Intro de la galería, una por ficha ────────────────────────────────────
# Antes: una sola frase escrita a mano en la plantilla, igual en las 17 páginas.
# Ahora vive en los datos (`galeriaIntro`), y cada ficha dice de qué son sus fotos.
GALERIA = {
    'trajes-estructurales-nomex-pbi':
        'Referencias del conjunto en estación y en intervención. Lo que no se ve en ninguna foto '
        'es la barrera de humedad ni el forro térmico, que son las dos capas que deciden el TPP '
        'y el THL: esas van en la ficha, no en la imagen.',
    'cascos-bullard-y-msa':
        'Perfiles de casco en operación. La silueta —ala completa, perfil metro o jet— es lo único '
        'de esta pieza que una foto sí resuelve; la coquilla, la cofia y la edición certificada '
        'se leen en la etiqueta interior.',
    'botas-dielectricas':
        'Uso del calzado en escena. Ninguna imagen muestra lo que decide la compra: la altura de '
        'caña en pulgadas, el ancho y la resistencia eléctrica declarada en ensayo del fabricante.',
    'guantes-de-intervencion':
        'Manos en maniobra, que es donde se comprueba lo único que no se puede fotografiar: la '
        'destreza. El tipo de puño y el material de la concha sí se distinguen de cerca; la '
        'barrera de humedad, nunca.',
    'protector-de-cuello-y-capucha':
        'La pieza en uso, bajo el casco y sobre el cuello del chaquetón. La capa de bloqueo de '
        'partículas va por dentro y no se ve: se pide por eficiencia publicada y por retención '
        'después de lavados.',
    'viseras-y-caretas':
        'Configuraciones de protección facial en operación. Lo que una foto no puede mostrar es si '
        'ese componente quedó dentro del alcance del certificado del casco, que es justamente la '
        'pregunta de esta ficha.',
    'skold-hero-pbi-max-7-0':
        'Referencias del conjunto con la configuración de barrera exterior más resistente de la '
        'línea. El color y el patrón de cintas se eligen en la orden; la barrera, en la ficha.',
    'skold-hero-advance':
        'Imágenes de referencia del conjunto. La barrera Advance no se distingue a la vista de '
        'ninguna de sus hermanas: la diferencia está en el laminado y en el certificado.',
    'skold-hero-kombat-flex':
        'Referencias de uso donde importa esta configuración: gateo, arrastre y trabajo con los '
        'brazos por encima de la cabeza. La movilidad se evalúa vistiendo, no mirando.',
    'skold-hero-pioneer':
        'Referencias del conjunto. Las tres capas que definen esta configuración van una encima de '
        'la otra y ninguna es visible desde afuera.',
    'skold-hero-defender-750':
        'Referencias del conjunto. Conviene recordar aquí que el nombre de la barrera y el del '
        'modelo se parecen: la clave de producto de la orden es lo que evita recibir otra cosa.',
    'bullard-px-series':
        'Perfiles y detalles de la serie. El visor retráctil se ve; los 36 puntos de ajuste de la '
        'suspensión y la clave de la careta cotizada, no.',
    'bullard-ust-traditional':
        'La silueta tradicional de ala completa en operación. Entre la Traditional y la LowRider la '
        'diferencia de perfil es visible; la de peso solo está publicada para una de las dos.',
    'bullard-lt-series':
        'Referencias del perfil ligero en uso. El sistema de acople rápido de careta y goggles es '
        'lo que distingue a esta serie y es lo único que la foto alcanza a insinuar.',
    'msa-cairns-1836':
        'El perfil tradicional de composite en escena. Es el modelo mejor documentado del catálogo: '
        'casi todo lo que importa está en su ficha técnica, no en la imagen.',
    'msa-cairns-660c-metro':
        'Perfil metro en operación, que es la razón de existir de este modelo: menos ala, más '
        'espacio libre al girar la cabeza en un vano.',
    'msa-cairns-xf1':
        'El perfil jet sin ala en uso. La luz y la comunicación integradas van por dentro de la '
        'coquilla y se piden por número de parte, no por descripción.',
}


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
    bloques = {}   # slug -> bloque l3 o l4
    for prod in cat['productos']:
        if prod.get('l3'):
            bloques[prod['slug']] = prod['l3']
            for card in prod['l3'].get('catalogo', {}).get('cards', []):
                if card.get('l4'):
                    bloques[card['slug']] = card['l4']

    cambios = collections.Counter()

    for slug, tablas in HEADS.items():
        secs = {s['id']: s for s in bloques[slug]['secciones']}
        for sid, head in tablas.items():
            s = secs[sid]
            assert s.get('tabla'), '%s/%s no tiene tabla' % (slug, sid)
            largo = len(s['tabla']['rows'][0])
            assert len(head) == largo, \
                '%s/%s: %d encabezados para %d columnas' % (slug, sid, len(head), largo)
            if s['tabla']['head'] != head:
                s['tabla']['head'] = head
                cambios['head'] += 1

    for slug, eyes in EYEBROWS.items():
        secs = {s['id']: s for s in bloques[slug]['secciones']}
        for sid, eye in eyes.items():
            if secs[sid].get('eyebrow') != eye:
                secs[sid]['eyebrow'] = eye
                cambios['eyebrow'] += 1

    for slug, intro in GALERIA.items():
        if bloques[slug].get('galeriaIntro') != intro:
            bloques[slug]['galeriaIntro'] = intro
            cambios['galeriaIntro'] += 1

    faltan = [s for s in bloques if s not in GALERIA]
    assert not faltan, 'fichas sin galeriaIntro: %s' % faltan

    if cambios:
        with io.open(RUTA, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

    print('fichas revisadas:', len(bloques))
    for k, v in sorted(cambios.items()):
        print('  %-14s %d' % (k, v))
    if not cambios:
        print('  nada por cambiar: ya estaba humanizado')


if __name__ == '__main__':
    main()
