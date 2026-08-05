# -*- coding: utf-8 -*-
"""Auditoria de las 5 fichas L4: errores, interlinking y SEO."""
import re, json, os, glob, collections, itertools

DIST = 'dist'
BASE = f'{DIST}/productos/epp-para-bomberos/trajes-estructurales-nomex-pbi'
SLUGS = ['skold-hero-pbi-max-7-0', 'skold-hero-advance', 'skold-hero-kombat-flex',
         'skold-hero-pioneer', 'skold-hero-defender-750']

def leer(p):
    return io_open(p)

def io_open(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def sin_scripts(h):
    """Quita <script> y <style>: sus template literals no son enlaces reales."""
    h = re.sub(r'<script\b.*?</script>', '', h, flags=re.S | re.I)
    return re.sub(r'<style\b.*?</style>', '', h, flags=re.S | re.I)

# Rutas realmente publicadas
publicadas = set()
for p in glob.glob(f'{DIST}/**/index.html', recursive=True):
    r = '/' + os.path.relpath(p, DIST).replace('/index.html', '')
    publicadas.add('/' if r == '/.' else r)
# Tambien los archivos servidos tal cual: sitemap, robots, manifest, sw...
for p in glob.glob(f'{DIST}/**/*', recursive=True):
    if os.path.isfile(p) and not p.endswith('index.html'):
        publicadas.add('/' + os.path.relpath(p, DIST))
publicadas.add('/')

print('=' * 78)
print('AUDITORIA L4 — 5 fichas SKOLD HERO')
print('=' * 78)

problemas = collections.defaultdict(list)
paginas = {}

for s in SLUGS:
    p = f'{BASE}/{s}/index.html'
    h = io_open(p)
    paginas[s] = h
    main = re.search(r'<main.*?</main>', h, re.S).group(0)
    body = re.search(r'class="l3-body"(.*?)class="l3-aside"', h, re.S).group(1)
    aside = re.search(r'class="l3-aside"(.*?)</aside>', h, re.S).group(1)

    # ── enlaces internos
    links = re.findall(r'<a[^>]+href="(/[^"#?][^"]*|/)"', main)
    links_body = re.findall(r'<a[^>]+href="([^"]+)"', body)
    anclas_out = re.findall(r'<a[^>]+href="(#[^"]+)"', main)

    # rutas rotas
    rotas = []
    for l in set(links):
        ruta = l.split('#')[0].split('?')[0].rstrip('/')
        if ruta == '':
            ruta = '/'
        if ruta not in publicadas:
            rotas.append(l)
    if rotas:
        problemas['enlaces rotos'].append((s, sorted(rotas)))

    # anclas que no existen en la pagina
    ids = set(re.findall(r'\sid="([^"]+)"', h))
    anclas_muertas = sorted({a[1:] for a in anclas_out} - ids)
    if anclas_muertas:
        problemas['anclas inexistentes'].append((s, anclas_muertas))

    # ids duplicados
    todos_ids = re.findall(r'\sid="([^"]+)"', h)
    dup = [k for k, v in collections.Counter(todos_ids).items() if v > 1]
    if dup:
        problemas['ids duplicados'].append((s, dup))

    # imagenes
    imgs = re.findall(r'<img[^>]+>', h)
    sin_alt = [i for i in imgs if 'alt=' not in i]
    if sin_alt:
        problemas['img sin alt'].append((s, len(sin_alt)))
    srcs = re.findall(r'<img[^>]+src="([^"]+)"', h)
    bg = re.findall(r"background-image:url\('([^']+)'\)", h)
    faltantes = [x for x in set(srcs + bg) if x.startswith('/') and not os.path.exists('public' + x)]
    if faltantes:
        problemas['imagenes inexistentes'].append((s, faltantes))

    # encabezados
    h1 = re.findall(r'<h1', h)
    if len(h1) != 1:
        problemas['h1 != 1'].append((s, len(h1)))

    # schema
    sc = [json.loads(m) for m in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', h, re.S)]
    tipos = [x.get('@type') for x in sc]
    for req in ('BreadcrumbList', 'Product', 'FAQPage'):
        if req not in tipos:
            problemas['schema faltante'].append((s, req))

    # tablas: primera columna deberia ser th scope=row
    tablas = re.findall(r'<table class="l3-tabla">.*?</table>', h, re.S)
    filas_sin_th = 0
    for t in tablas:
        for tr in re.findall(r'<tr>(.*?)</tr>', t, re.S):
            if '<th' not in tr and tr.strip().startswith('<td'):
                filas_sin_th += 1
    if filas_sin_th:
        problemas['tabla sin th de fila'].append((s, filas_sin_th))

    # SEO
    t = re.search(r'<title>(.*?)</title>', h, re.S).group(1)
    d = re.search(r'<meta name="description" content="(.*?)"', h, re.S).group(1)
    if not (55 <= len(t) <= 65):
        problemas['title fuera de 55-65'].append((s, len(t)))
    if not (140 <= len(d) <= 160):
        problemas['description fuera de 140-160'].append((s, len(d)))

    # enlaces contextuales dentro del cuerpo editorial
    ctx = [l for l in links_body if l.startswith('/') or l.startswith('http')]
    print(f'\n{s}')
    print(f'  enlaces internos en <main>: {len(set(links))} únicos, {len(links)} totales')
    print(f'  enlaces en el CUERPO editorial: {len(ctx)}   ← interlinking contextual')
    print(f'  enlaces en el sidebar: {len(re.findall(chr(60)+"a ", aside))}')
    print(f'  anclas internas: {len(set(anclas_out))} · ids: {len(ids)}')
    print(f'  imgs: {len(imgs)} · tablas: {len(tablas)}')
    if ctx:
        for c in sorted(set(ctx)):
            print('     ·', c)

# ── enlaces entre las 5 fichas
print('\n' + '=' * 78)
print('MATRIZ DE ENLACES ENTRE LAS 5 FICHAS')
print('=' * 78)
prefijo = '/productos/epp-para-bomberos/trajes-estructurales-nomex-pbi/'
print(f'{"desde \\ hacia":26}' + ''.join(f'{x[11:18]:>10}' for x in SLUGS))
for a in SLUGS:
    fila = f'{a[11:]:26}'
    for b in SLUGS:
        if a == b:
            fila += f'{"—":>10}'
        else:
            n = paginas[a].count(f'href="{prefijo}{b}"')
            fila += f'{n if n else "✗":>10}'
    print(fila)

# ── titles y descriptions unicos
tits = {s: re.search(r'<title>(.*?)</title>', paginas[s], re.S).group(1) for s in SLUGS}
descs = {s: re.search(r'<meta name="description" content="(.*?)"', paginas[s], re.S).group(1) for s in SLUGS}
print(f'\ntitles únicos: {len(set(tits.values()))}/5 · descriptions únicas: {len(set(descs.values()))}/5')

# ── blog slugs referenciados existen?
print('\n' + '=' * 78)
print('ENLACES A BLOG')
print('=' * 78)
for s in SLUGS:
    bl = sorted(set(re.findall(r'href="/blog/([^"]+)"', paginas[s])))
    malos = [b for b in bl if f'/blog/{b}' not in publicadas]
    print(f'  {s[11:]:22} {len(bl)} posts' + (f'  ROTOS: {malos}' if malos else ''))

# ── quien enlaza HACIA las fichas L4
print('\n' + '=' * 78)
print('ENLACES ENTRANTES HACIA LAS FICHAS L4 (desde todo el sitio)')
print('=' * 78)
entrantes = collections.defaultdict(set)
for p in glob.glob(f'{DIST}/**/index.html', recursive=True):
    r = '/' + os.path.relpath(p, DIST).replace('/index.html', '')
    if any(f'{prefijo}{s}' in r for s in SLUGS):
        continue
    h = io_open(p)
    for s in SLUGS:
        if f'href="{prefijo}{s}"' in h:
            entrantes[s].add(r)
for s in SLUGS:
    orig = sorted(entrantes[s])
    print(f'  {s[11:]:22} {len(orig)} páginas: {", ".join(o.replace("/productos/epp-para-bomberos","...") for o in orig) or "NINGUNA"}')

# ── resumen de problemas
print('\n' + '=' * 78)
print('PROBLEMAS DETECTADOS')
print('=' * 78)
if not problemas:
    print('  ninguno')
for k, v in problemas.items():
    print(f'\n  ▸ {k}')
    for item in v:
        print(f'      {item}')

# ══════════════════════════════════════════════════════════════════════════════
# AUDITORIA DE ENLACES INTERNOS DE TODO EL SITIO
# Un enlace interno nunca debe apuntar a un 404 ni a un redirect: el 404 se pierde
# y el redirect desperdicia el salto. Esto revisa las dos cosas en todas las paginas.
# ══════════════════════════════════════════════════════════════════════════════
REDIRIGIDOS = {
    '/productos/equipos-bomberos', '/productos/scba-respiracion', '/productos/extintores',
    '/productos/sistemas-fijos', '/productos/herramientas-rescate',
    '/productos/deteccion-alarma', '/productos/gabinetes-mangueras',
}

print('\n' + '=' * 78)
print('ENLACES INTERNOS DE TODO EL SITIO')
print('=' * 78)

a_redirect = collections.defaultdict(set)
a_404 = collections.defaultdict(set)
revisadas = 0

for p in glob.glob(f'{DIST}/**/index.html', recursive=True):
    origen = '/' + os.path.relpath(p, DIST).replace('/index.html', '')
    h = sin_scripts(io_open(p))
    revisadas += 1
    for l in set(re.findall(r'<a[^>]+href="(/[^"]*)"', h)):
        ruta = l.split('#')[0].split('?')[0].rstrip('/') or '/'
        if ruta in REDIRIGIDOS:
            a_redirect[ruta].add(origen)
        elif ruta not in publicadas and not ruta.startswith('/images'):
            a_404[ruta].add(origen)

print(f'  paginas revisadas: {revisadas}')
print(f'\n  > enlaces a slugs REDIRIGIDOS (301 innecesario): {sum(len(v) for v in a_redirect.values())}')
for r, orig in sorted(a_redirect.items()):
    print(f'      {r} <- {len(orig)} paginas')
if not a_redirect:
    print('      ninguno')

print(f'\n  > enlaces a rutas INEXISTENTES (404): {sum(len(v) for v in a_404.values())}')
for r, orig in sorted(a_404.items()):
    print(f'      {r} <- {len(orig)} paginas: {", ".join(sorted(orig)[:3])}')
if not a_404:
    print('      ninguno')

print('\n' + '=' * 78)
print('INTERLINKING BLOG -> CATALOGO (plugin rehypeInterlink)')
print('=' * 78)
posts = [p for p in sorted(glob.glob(f'{DIST}/blog/*/index.html'))
         if '/blog/pagina/' not in p and '/blog/tema/' not in p]
por_post = collections.Counter()
destinos = collections.Counter()
for p in posts:
    il = re.findall(r'<a href="([^"]+)" class="art-il"', io_open(p))
    por_post[len(il)] += 1
    for x in il:
        destinos[x] += 1
con = len(posts) - por_post[0]
print(f'  posts: {len(posts)} · con al menos un enlace al catalogo: {con} '
      f'({round(100 * con / max(1, len(posts)))} %)')
print(f'  enlaces insertados: {sum(destinos.values())}')
print(f'  distribucion por post: {dict(sorted(por_post.items()))}')
for x, n in destinos.most_common():
    print(f'      {n:4}  {x}')
