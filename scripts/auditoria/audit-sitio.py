import re, os, glob, collections
ROOT = __import__('os').path.abspath(
    __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
os.chdir(ROOT)
files = glob.glob('dist/**/*.html', recursive=True)
titulos_largos = []
desc_mal = []
sin_h1 = []
multi_h1 = []
pesos = []
sin_lazy = 0
alt_vacio = 0
roto = set()
for f in files:
    h = open(f, encoding='utf-8').read()
    pesos.append((len(h.encode()) / 1024, f))
    m = re.search(r'<title>(.*?)</title>', h, re.S)
    if m and len(m.group(1)) > 65:
        titulos_largos.append((len(m.group(1)), f))
    d = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    if not d or not (110 <= len(d.group(1)) <= 160):
        desc_mal.append((len(d.group(1)) if d else 0, f))
    n1 = len(re.findall(r'<h1', h))
    if n1 == 0:
        sin_h1.append(f)
    elif n1 > 1:
        multi_h1.append(f)
    imgs = re.findall(r'<img[^>]*>', h)
    sin_lazy += sum(1 for i in imgs if 'loading=' not in i)
    alt_vacio += sum(1 for i in imgs if 'alt=""' in i or 'alt=' not in i)
    for i in set(re.findall(r'src="(/images/[^"]+)"', h)):
        if not os.path.exists('public' + i):
            roto.add(i)
pesos.sort(reverse=True)
print('paginas:', len(files))
print('titulos >65 ch:', len(titulos_largos), titulos_largos[:3])
print('description fuera de 110-160:', len(desc_mal), desc_mal[:3])
print('sin H1:', len(sin_h1), sin_h1[:3])
print('con varios H1:', len(multi_h1), multi_h1[:3])
print('img sin loading:', sin_lazy, '| alt vacio o ausente:', alt_vacio)
print('imagenes rotas:', roto or 'ninguna')
print('paginas mas pesadas:')
for p, f in pesos[:6]:
    print('   %7.1f KB  %s' % (p, f))
print('peso total html: %.1f MB' % (sum(p for p, _ in pesos) / 1024))
print('peso imagenes: %.1f MB' % (sum(os.path.getsize(p) for p in glob.glob('public/images/**/*', recursive=True) if os.path.isfile(p)) / 1e6))
