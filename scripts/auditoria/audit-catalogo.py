import json, io, os, re
ROOT = __import__('os').path.abspath(
    __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..'))
os.chdir(ROOT)
cats = json.load(io.open('src/data/productos.json', encoding='utf-8'))
print('%-26s %3s %3s %3s %3s %3s %3s %4s %5s %s' %
      ('CATEGORIA', 'hB', 'int', 'nrm', 'apl', 'prd', 'faq', 'imgs', 'title', 'desc'))
ok = True
for c in cats:
    prods = c.get('productos', [])
    completos = sum(1 for p in prods if p.get('desc') and p.get('specs')
                    and p.get('intro') and p.get('galeria') and p.get('slug'))
    imgs = set([c['imagenes'][k]['src'] for k in ('hero', 'a', 'b', 'c')])
    for p in prods:
        imgs.add(p['img'])
        for g in p.get('galeria', []):
            imgs.add(g['src'])
    rotas = [i for i in imgs if not os.path.exists('public' + i)]
    t = len(c['seoTitle']) + 21
    d = len(c['seoDescription'])
    flag = ''
    if completos != 6 or len(c.get('faqs', [])) != 8 or len(c['normas']) < 6 or rotas or t > 65 or not (110 <= d <= 160):
        flag = '  <-- REVISAR'
        ok = False
    print('%-26s %3d %3d %3d %3d %3d %3d %4d %5d %4d%s' %
          (c['nombre'], len(c['heroBloques']), len(c['intro']), len(c['normas']),
           len(c['aplicaciones']), completos, len(c.get('faqs', [])), len(imgs), t, d, flag))
    if rotas:
        print('    rotas:', rotas)
print()
# duplicados de imagen entre categorias
uso = {}
for c in cats:
    s = json.dumps(c, ensure_ascii=False)
    for m in set(re.findall(r'/images/catalogo/[^"]+\.webp', s)):
        uso.setdefault(m, []).append(c['slug'])
dup = {k: v for k, v in uso.items() if len(v) > 1}
print('imagenes compartidas entre categorias:', len(dup))
for k, v in list(dup.items())[:6]:
    print('  ', k, v)
print()
print('TODO EN ORDEN' if ok and not dup else 'HAY PENDIENTES')
