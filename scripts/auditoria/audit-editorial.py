#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditoria EDITORIAL del catalogo L3/L4: no mide si el HTML es valido, mide si el texto
se lee como escrito por una persona o como generado por una plantilla.

Seis cosas que revisa, en orden de importancia:

  1. ENLACES DEL CUERPO por pagina, con destino. Una ficha con 3 enlaces mientras sus
     hermanas tienen 9 no esta mal construida: esta mal escrita, porque no menciona a
     las piezas vecinas por su nombre completo.
  2. ENLACES ENTRANTES del blog hacia cada ficha.
  3. FORMULAS REPETIDAS entre fichas. Toma los primeros 6 tokens de cada oracion del
     cuerpo y busca los arranques que aparecen en mas de una ficha: son las muletillas
     que delatan la plantilla ("Es la confusion mas comun de la linea", "Lo que cambia
     es", "Redaccion que cierra la partida").
  4. DENSIDAD DE NEGRITAS. Arriba de ~6 <strong> por 100 palabras el texto se lee como
     folleto y el resaltado deja de significar algo.
  5. METAS: largo de title y description contra los rangos utiles.
  6. CANIBALIZACION DE FAQS entre la L2 de la categoria y sus L3.

Uso: python3 scripts/auditoria/audit-editorial.py
"""
import collections
import io
import json
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST = os.path.join(RAIZ, 'dist')
DATOS = os.path.join(RAIZ, 'src', 'data', 'productos.json')

ANCHO = 78
BARRA = '=' * ANCHO


def titulo(t):
    print('\n' + BARRA)
    print(t)
    print(BARRA)


def leer(ruta):
    with io.open(ruta, encoding='utf-8') as f:
        return f.read()


def sin_tildes(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def texto_plano(html):
    html = re.sub(r'<[^>]+>', ' ', html)
    html = re.sub(r'&nbsp;|&#160;', ' ', html)
    html = re.sub(r'&[a-z]+;|&#\d+;', ' ', html)
    return re.sub(r'\s+', ' ', html).strip()


def cuerpo(html):
    """El bloque editorial: de class="l3-body" a class="l3-aside"."""
    i = html.find('class="l3-body"')
    j = html.find('class="l3-aside"')
    return html[i:j] if i >= 0 and j > i else ''


# ── inventario de paginas ─────────────────────────────────────────────────────
with io.open(DATOS, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

paginas = []          # (nivel, ruta_url, ruta_html, nombre_corto)
for cat in data:
    if not cat.get('l3ok'):
        continue
    for prod in cat.get('productos', []):
        if not prod.get('l3'):
            continue
        url = '/productos/%s/%s' % (cat['slug'], prod['slug'])
        paginas.append(('L3', url, os.path.join(DIST, url.strip('/'), 'index.html'),
                        prod['slug']))
        for card in prod['l3'].get('catalogo', {}).get('cards', []):
            if card.get('slug') and card.get('l4'):
                u = '%s/%s' % (url, card['slug'])
                paginas.append(('L4', u, os.path.join(DIST, u.strip('/'), 'index.html'),
                                card['slug']))

faltan = [p for p in paginas if not os.path.exists(p[2])]
if faltan:
    print('Falta el build de %d paginas. Corre npm run build primero.' % len(faltan))
    for p in faltan[:5]:
        print('  ', p[1])
    sys.exit(1)

print('Paginas de catalogo con cuerpo editorial: %d  (%d L3 · %d L4)'
      % (len(paginas), sum(1 for p in paginas if p[0] == 'L3'),
         sum(1 for p in paginas if p[0] == 'L4')))

html_cache = {p[1]: leer(p[2]) for p in paginas}
cuerpo_cache = {u: cuerpo(h) for u, h in html_cache.items()}

# ── 1 · enlaces del cuerpo ────────────────────────────────────────────────────
titulo('1 · ENLACES DEL CUERPO EDITORIAL  (objetivo: 6 o mas, con hermanas)')

salientes = {}
duplicados = []
for nivel, url, _, corto in paginas:
    hrefs = re.findall(r'<a [^>]*href="(/[^"#]+)', cuerpo_cache[url])
    salientes[url] = hrefs
    catalogo = [h for h in hrefs if h.startswith('/productos')]
    blog = [h for h in hrefs if h.startswith('/blog')]
    repes = sorted(h for h in set(hrefs) if hrefs.count(h) > 1)
    if repes:
        duplicados.append((corto, repes))
    flag = '  <-- FLOJO' if len(hrefs) < 6 else ''
    if repes:
        flag += '  <-- DESTINO REPETIDO'
    print('%-3s %-58s %2d  (cat %d · blog %d)%s'
          % (nivel, corto, len(hrefs), len(catalogo), len(blog), flag))

# Un mismo destino enlazado dos veces en el cuerpo es siempre un defecto: gasta dos enlaces
# del tope en la misma página y se lee como relleno.
print('\ndestinos enlazados más de una vez en el mismo cuerpo: %d' % len(duplicados))
for corto, repes in duplicados:
    print('   %-40s %s' % (corto, ', '.join(repes)))

# ── 2 · enlaces entrantes ─────────────────────────────────────────────────────
titulo('2 · ENLACES ENTRANTES DESDE EL BLOG  (plugin rehypeInterlink)')

blog_dir = os.path.join(DIST, 'blog')
posts = []
for nombre in sorted(os.listdir(blog_dir)):
    idx = os.path.join(blog_dir, nombre, 'index.html')
    if os.path.isdir(os.path.join(blog_dir, nombre)) and os.path.exists(idx):
        posts.append((nombre, leer(idx)))

entrantes = collections.Counter()
sin_enlaces = []
for nombre, h in posts:
    hrefs = re.findall(r'<a [^>]*class="art-il"[^>]*href="([^"]+)"'
                       r'|<a [^>]*href="([^"]+)"[^>]*class="art-il"', h)
    hrefs = [a or b for a, b in hrefs]
    if not hrefs:
        sin_enlaces.append(nombre)
    for x in hrefs:
        entrantes[x.split('#')[0]] += 1

for nivel, url, _, corto in paginas:
    n = entrantes.get(url, 0)
    flag = '  <-- SIN ENLACES ENTRANTES' if n == 0 else ('  <-- pocos' if n < 2 else '')
    print('%-3s %-58s %2d%s' % (nivel, corto, n, flag))

print('\nposts sin un solo enlace al catalogo: %d de %d' % (len(sin_enlaces), len(posts)))
for p in sin_enlaces:
    print('   ', p)

# ── 3 · formulas repetidas entre fichas ───────────────────────────────────────
titulo('3 · FORMULAS REPETIDAS ENTRE FICHAS  (arranques de oracion compartidos)')

STOP = 6  # tokens del arranque


def oraciones(txt):
    for o in re.split(r'(?<=[.:;])\s+', txt):
        o = o.strip()
        if len(o.split()) >= STOP + 1:
            yield o


arranques = collections.defaultdict(set)
for nivel, url, _, corto in paginas:
    txt = texto_plano(cuerpo_cache[url])
    for o in oraciones(txt):
        toks = sin_tildes(o.lower()).split()[:STOP]
        toks = [re.sub(r'[^\wñ%°"]', '', t) for t in toks]
        clave = ' '.join(t for t in toks if t)
        if len(clave.split()) == STOP:
            arranques[clave].add(corto)

compartidos = sorted(((len(v), k, sorted(v)) for k, v in arranques.items() if len(v) > 1),
                     reverse=True)
if not compartidos:
    print('  ninguno: cada ficha arranca sus oraciones distinto')
for n, k, quienes in compartidos[:25]:
    print('  %d fichas · "%s…"' % (n, k))
    print('        %s' % ', '.join(quienes))

# frases hechas que ya sabemos que se repiten y conviene vigilar
titulo('3b · MULETILLAS VIGILADAS')
MULETILLAS = [
    'es la confusion mas comun', 'lo que cambia', 'redaccion que cierra',
    'no se deduce de la foto', 'y eso no se ve por fuera', 'la regla es simple',
    'conviene leer dos veces', 'lo que importa', 'aqui si', 'a secas',
    'no es un detalle', 'dos renglones', 'que nadie publica', 'en la partida se escribe',
    'no se negocia', 'vale la pena', 'sin rodeos',
]
for m in MULETILLAS:
    donde = []
    for nivel, url, _, corto in paginas:
        t = sin_tildes(texto_plano(cuerpo_cache[url]).lower())
        c = t.count(m)
        if c:
            donde.append('%s×%d' % (corto, c))
    if len(donde) > 1:
        print('  "%s" → %s' % (m, ', '.join(donde)))

# ── 4 · densidad de negritas ──────────────────────────────────────────────────
titulo('4 · DENSIDAD DE NEGRITAS  (objetivo: menos de 6 por 100 palabras)')

for nivel, url, _, corto in paginas:
    c = cuerpo_cache[url]
    palabras = len(texto_plano(c).split())
    strongs = len(re.findall(r'<strong>', c))
    dens = 100.0 * strongs / palabras if palabras else 0
    flag = '  <-- ALTA' if dens >= 6 else ''
    print('%-3s %-58s %5.1f  (%d strong / %d palabras)%s'
          % (nivel, corto, dens, strongs, palabras, flag))

# ── 5 · metas ─────────────────────────────────────────────────────────────────
titulo('5 · TITLE Y DESCRIPTION  (title 50-62 · description 140-160)')

for nivel, url, _, corto in paginas:
    h = html_cache[url]
    t = re.search(r'<title>(.*?)</title>', h, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    t = texto_plano(t.group(1)) if t else ''
    d = texto_plano(d.group(1)) if d else ''
    avisos = []
    if not (50 <= len(t) <= 62):
        avisos.append('title %d' % len(t))
    if not (140 <= len(d) <= 160):
        avisos.append('desc %d' % len(d))
    print('%-3s %-58s %s' % (nivel, corto, ' · '.join(avisos) if avisos else 'ok'))

# ── 6 · canibalizacion de FAQs ────────────────────────────────────────────────
titulo('6 · FAQS: SOLAPE ENTRE LA L2 Y SUS L3')


def norm_q(q):
    q = sin_tildes(q.lower())
    return set(re.findall(r'[a-z0-9]+', q)) - {
        'que', 'como', 'cual', 'cuales', 'un', 'una', 'el', 'la', 'los', 'las', 'de',
        'del', 'en', 'y', 'o', 'se', 'es', 'para', 'por', 'con', 'si', 'no', 'al'}


for cat in data:
    if not cat.get('l3ok'):
        continue
    faqs_cat = [f['q'] for f in cat.get('faqs', [])]
    for prod in cat.get('productos', []):
        if not prod.get('l3'):
            continue
        for f in prod['l3'].get('faqs', []):
            a = norm_q(f['q'])
            for qc in faqs_cat:
                b = norm_q(qc)
                if not a or not b:
                    continue
                jac = len(a & b) / float(len(a | b))
                if jac >= 0.45:
                    print('  %.2f  %s' % (jac, prod['slug']))
                    print('        L3: %s' % f['q'])
                    print('        L2: %s' % qc)

print('\n' + BARRA)
print('fin')
print(BARRA)
