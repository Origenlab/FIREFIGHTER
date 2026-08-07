# -*- coding: utf-8 -*-
"""Audita el directorio en dist/: titulos y descripciones duplicadas en todo el
sitio, y H1 / canonical / JSON-LD / longitudes en el estado que se le pase.

Uso:  python3 scripts/auditoria/audit-directorio.py [slug-del-estado]
"""
import re, os, sys, glob, json, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(ROOT)
estado = sys.argv[1] if len(sys.argv) > 1 else None

files = glob.glob('dist/**/*.html', recursive=True)
T = collections.defaultdict(list)
D = collections.defaultdict(list)
probl = []
n_estado = 0

for f in files:
    try:
        h = open(f, encoding='utf-8').read()
    except FileNotFoundError:
        continue
    if 'Redirecting to' in h[:200]:
        continue
    m = re.search(r'<title>(.*?)</title>', h, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    if m:
        T[m.group(1)].append(f)
    if d:
        D[d.group(1)].append(f)
    if estado and ('/directorio/%s' % estado) in f:
        n_estado += 1
        if not m:
            probl.append(('sin title', f))
        elif len(m.group(1)) > 65:
            probl.append(('title %d ch' % len(m.group(1)), f))
        if not d:
            probl.append(('sin description', f))
        elif not (110 <= len(d.group(1)) <= 160):
            probl.append(('description %d ch' % len(d.group(1)), f))
        n1 = len(re.findall(r'<h1', h))
        if n1 != 1:
            probl.append(('h1 x%d' % n1, f))
        if not re.search(r'rel="canonical" href="(.*?)"', h):
            probl.append(('sin canonical', f))
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try:
                json.loads(blk)
            except Exception as e:
                probl.append(('json-ld invalido: %s' % str(e)[:40], f))

dt = [(k, v) for k, v in T.items() if len(v) > 1]
dd = [(k, v) for k, v in D.items() if len(v) > 1]

print('paginas analizadas: %d' % len(files))
print('titles duplicados: %d' % len(dt))
for k, v in dt:
    print('   x%d  %r' % (len(v), k[:70]))
    for x in v[:4]:
        print('        %s' % x)
print('descriptions duplicadas: %d' % len(dd))
for k, v in dd:
    print('   x%d  %r' % (len(v), k[:70]))
    for x in v[:4]:
        print('        %s' % x)
if estado:
    print('paginas de /directorio/%s: %d' % (estado, n_estado))
    print('problemas: %d' % len(probl))
    for p in probl:
        print('   %s  ->  %s' % p)
