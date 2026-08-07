#!/usr/bin/env python3
"""
Linter de datos de src/data/cumplimiento-estados.json.

Por qué existe: la ficha de un estado se ve bien en el navegador aunque tenga
defectos que solo se notan al compararla con las otras 31. Este script codifica
las invariantes que fuimos descubriendo al levantar Aguascalientes, Nuevo León,
Guanajuato, Jalisco y Querétaro, para que el estado 33 no las vuelva a romper.

Cada regla nació de un defecto real, no de una idea de cómo debería ser.

Uso:
    python3 scripts/lint_cumplimiento.py            # revisa el JSON
    python3 scripts/lint_cumplimiento.py --estricto # los avisos también fallan

Sale con 1 si hay errores. Los avisos no fallan salvo con --estricto.
"""

from __future__ import annotations

import json
import os
import re
import sys
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_ESTADOS = os.path.join(RAIZ, 'src', 'data', 'cumplimiento-estados.json')
JSON_GEO = os.path.join(RAIZ, 'src', 'data', 'states.json')
JSON_PRODUCTOS = os.path.join(RAIZ, 'src', 'data', 'productos.json')

CAMPOS_BASE = [
    'estado', 'slug', 'ley', 'leyFecha', 'leyUrl', 'autoridad', 'bomberos',
    'pipcVigencia', 'simulacros', 'simulacrosMin', 'consultor', 'distintivo',
    'confianza',
]

# Primeras palabras que `modeloDeBomberos()` sabe mapear. Si el campo empieza
# con otra cosa, la card muestra la etiqueta por defecto 'Municipal' y miente.
ARRANQUES_BOMBEROS = (
    'municipal', 'municipal por convenio', 'estatal', 'coexisten', 'integrado',
    'asistencia privada', 'no hay cuerpo', 'la ley', 'la nueva ley',
)

# Longitudes de referencia, tomadas de las fichas ya publicadas. No son reglas
# de estilo: por debajo de esto el campo no alcanza a decir nada útil.
MINIMOS = {
    'autoridad': 140,
    'bomberos': 120,
    'pipcVigencia': 90,
    'simulacros': 60,
    'consultor': 90,
    'distintivo': 200,
}

# La card del hub corta estos campos en el primer punto. Si esa primera frase
# se desborda, la tarjeta se rompe.
#
# El piso es deliberadamente bajo: la card ya trae la etiqueta ("PIPC",
# "Simulacros"), así que un "Anual" de cinco letras se entiende perfectamente.
# Un umbral alto aquí solo produce falsos positivos y empuja a alargar textos
# que estaban bien.
CORTA_EN_PUNTO = {'pipcVigencia': (4, 120), 'simulacros': (4, 120)}


def cargar(path):
    with open(path, encoding='utf8') as f:
        return json.load(f)


class Reporte:
    def __init__(self):
        self.errores: list[str] = []
        self.avisos: list[str] = []

    def error(self, slug, msg):
        self.errores.append(f'{slug:22} {msg}')

    def aviso(self, slug, msg):
        self.avisos.append(f'{slug:22} {msg}')


def revisar(estados, geo_slugs, producto_slugs, r: Reporte):
    vistos = set()

    for e in estados:
        slug = e.get('slug', '??')

        # ── Integridad estructural ───────────────────────────────────────
        for campo in CAMPOS_BASE:
            if campo not in e:
                r.error(slug, f'falta el campo obligatorio `{campo}`')
        if slug in vistos:
            r.error(slug, 'slug duplicado')
        vistos.add(slug)
        if slug not in geo_slugs:
            r.error(slug, 'el slug no existe en states.json, la ficha saldría sin code ni capital')

        if e.get('confianza') not in ('alta', 'media'):
            r.error(slug, f"confianza inválida: {e.get('confianza')!r}")

        # ── Ley y fuente ─────────────────────────────────────────────────
        url = e.get('leyUrl', '')
        if url:
            p = urlparse(url)
            if not p.scheme.startswith('http'):
                r.error(slug, 'leyUrl no es una URL')
            # Una home de congreso no sirve para verificar un artículo.
            elif p.path in ('', '/'):
                r.error(slug, f'leyUrl es un portal genérico, no el texto: {url}')
        else:
            r.error(slug, 'leyUrl vacío')

        fecha = e.get('leyFecha', '')
        if 'reforma' not in fecha.lower():
            r.aviso(slug, 'leyFecha no menciona la última reforma')
        if re.search(r'\b(19|20)\d{2}\b', fecha) is None:
            r.error(slug, 'leyFecha no contiene ningún año')

        # ── Campos que alimentan lógica, no solo texto ───────────────────
        cons = e.get('consultor', '').strip()
        if not re.match(r'^(s[ií]|no)\b', cons, re.I):
            r.error(slug, "consultor debe empezar con 'Sí' o 'No': de ahí sale el filtro del hub")

        bom = e.get('bomberos', '').strip().lower()
        if not any(bom.startswith(a) for a in ARRANQUES_BOMBEROS):
            r.error(slug, f'bomberos empieza con "{bom[:28]}…" y modeloDeBomberos() no lo reconoce')

        sm = e.get('simulacrosMin')
        if not isinstance(sm, int) or sm < 0 or sm > 12:
            r.error(slug, f'simulacrosMin fuera de rango: {sm!r}')
        else:
            # El número y el texto tienen que contar la misma historia.
            txt = e.get('simulacros', '').lower()
            palabra = {0: None, 1: 'un', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco', 6: 'seis'}.get(sm)
            if sm == 0 and not re.search(r'no fija|no establec|no lo fija|sin mínimo|no exist', txt):
                r.aviso(slug, 'simulacrosMin es 0 pero el texto no explica que la ley no fija mínimo')
            if palabra and palabra not in txt and str(sm) not in txt:
                r.aviso(slug, f'simulacrosMin={sm} pero el texto no dice "{palabra}" ni "{sm}"')

        # ── Longitud y primera frase ─────────────────────────────────────
        for campo, minimo in MINIMOS.items():
            v = e.get(campo, '')
            if isinstance(v, str) and len(v) < minimo:
                r.aviso(slug, f'`{campo}` tiene {len(v)} caracteres, por debajo del mínimo útil de {minimo}')

        for campo, (lo, hi) in CORTA_EN_PUNTO.items():
            v = e.get(campo, '')
            if not isinstance(v, str) or not v:
                continue
            primera = v.split('.')[0].split(':')[0].split(';')[0].split('(')[0].strip()
            if len(primera) < lo:
                r.aviso(slug, f'`{campo}`: la card corta en "{primera}", demasiado corto para entenderse')
            elif len(primera) > hi:
                r.aviso(slug, f'`{campo}`: la card corta en {len(primera)} caracteres, no cabe en la tarjeta')

        # ── Bloques ampliados ────────────────────────────────────────────
        s = e.get('sanciones')
        if s:
            if 'umaMax' not in s:
                r.error(slug, 'sanciones sin umaMax')
            if 'umaMin' in s and s['umaMin'] > s['umaMax']:
                r.error(slug, 'sanciones: el mínimo supera al máximo')
            if s.get('reincidenciaUma') and s['reincidenciaUma'] < s['umaMax']:
                r.error(slug, 'sanciones: el tope de reincidencia es menor que el máximo ordinario')
            if not s.get('fundamento'):
                r.error(slug, 'sanciones sin fundamento: no se publica un monto sin su artículo')
            if not s.get('otras'):
                r.aviso(slug, 'sanciones sin `otras`: casi siempre hay clausura o suspensión')

        for i, p in enumerate(e.get('plazos') or []):
            for k in ('que', 'plazo', 'fundamento', 'ambito'):
                if not p.get(k):
                    r.error(slug, f'plazos[{i}] sin `{k}`')
            if p.get('ambito') not in ('estatal', 'municipal'):
                r.error(slug, f"plazos[{i}] ámbito inválido: {p.get('ambito')!r}")

        muni = e.get('municipios') or []
        for i, m in enumerate(muni):
            for k in ('nombre', 'tramite', 'dependencia', 'vigencia'):
                if not m.get(k):
                    r.error(slug, f'municipios[{i}] sin `{k}`')
            if 'costo' not in m:
                r.error(slug, f"municipios[{i}] ({m.get('nombre')}) sin `costo`: usa null si no está publicado")
            costo = m.get('costo')
            # El badge se calcula del resumen; sin él, un costo largo que dice
            # que NO hay tarifa sale con badge verde de "Costo publicado".
            if costo and len(costo) > 34 and not m.get('costoResumen'):
                r.error(slug, f"municipios[{i}] ({m.get('nombre')}) necesita `costoResumen`: su costo tiene {len(costo)} caracteres")
            if m.get('costoResumen') and len(m['costoResumen']) > 32:
                r.aviso(slug, f"municipios[{i}] costoResumen de {len(m['costoResumen'])} caracteres, el badge se desborda")
            if m.get('url', '').startswith('http') is False and m.get('url'):
                r.error(slug, f'municipios[{i}] url inválida')
        if muni and not e.get('municipiosNota'):
            r.aviso(slug, 'tiene municipios pero no `municipiosNota`: falta la conclusión accionable')

        faqs = e.get('faqs') or []
        if faqs:
            if len(faqs) < 5:
                r.aviso(slug, f'solo {len(faqs)} FAQs; el estándar de las fichas ampliadas es de 6 a 8')
            for i, f in enumerate(faqs):
                if not f.get('q', '').strip().endswith('?'):
                    r.aviso(slug, f'faqs[{i}] no termina en signo de interrogación')
                if len(f.get('a', '')) < 120:
                    r.aviso(slug, f'faqs[{i}] con respuesta de {len(f.get("a", ""))} caracteres, demasiado corta para el schema')

        for i, x in enumerate(e.get('equipo') or []):
            if x.get('categoria') not in producto_slugs:
                r.error(slug, f"equipo[{i}] apunta a la categoría inexistente '{x.get('categoria')}'")
            if not x.get('porque'):
                r.error(slug, f'equipo[{i}] sin `porque`: no se recomienda equipo sin fundamento')

        for i, f in enumerate(e.get('fuentes') or []):
            if not f.get('url', '').startswith('http'):
                r.error(slug, f'fuentes[{i}] url inválida')

        # ── Coherencia del conjunto ──────────────────────────────────────
        ampliada = bool(e.get('municipios') or e.get('sanciones') or e.get('faqs'))
        if ampliada and e.get('confianza') != 'alta':
            r.error(slug, 'tiene bloques ampliados pero sigue en confianza media: saldría con noindex')
        if ampliada and not e.get('revisado'):
            r.aviso(slug, 'ficha ampliada sin `revisado` propio')
        if ampliada and not e.get('fuentes'):
            r.aviso(slug, 'ficha ampliada sin `fuentes`')

        # Tipografía: comillas rectas y dobles espacios se ven mal en prosa.
        for campo in ('autoridad', 'bomberos', 'pipcVigencia', 'simulacros', 'consultor', 'distintivo'):
            v = e.get(campo, '')
            if isinstance(v, str):
                if '  ' in v:
                    r.aviso(slug, f'`{campo}` tiene doble espacio')
                if '"' in v:
                    r.aviso(slug, f'`{campo}` tiene comillas rectas')


def main() -> int:
    estricto = '--estricto' in sys.argv
    estados = cargar(JSON_ESTADOS)
    geo_slugs = {x['slug'] for x in cargar(JSON_GEO)}
    producto_slugs = {x['slug'] for x in cargar(JSON_PRODUCTOS)}

    r = Reporte()
    revisar(estados, geo_slugs, producto_slugs, r)

    altas = [e for e in estados if e.get('confianza') == 'alta']
    ampliadas = [e for e in estados if e.get('municipios')]
    print(f'Entidades: {len(estados)}  ·  verificadas: {len(altas)}  ·  ampliadas: {len(ampliadas)}')
    faltan = [e['slug'] for e in estados if e.get('confianza') != 'alta']
    if faltan:
        print(f'Pendientes de verificar: {", ".join(faltan)}')
    print()

    if r.errores:
        print(f'=== ERRORES ({len(r.errores)}) ===')
        for x in r.errores:
            print(' ', x)
        print()
    if r.avisos:
        print(f'=== AVISOS ({len(r.avisos)}) ===')
        for x in r.avisos:
            print(' ', x)
        print()

    if not r.errores and not r.avisos:
        print('Sin hallazgos: las 32 fichas cumplen todas las invariantes.')
        return 0
    if r.errores or (estricto and r.avisos):
        return 1
    print('Sin errores. Los avisos no bloquean; revísalos cuando toques esa ficha.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
