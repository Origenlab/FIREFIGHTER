#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Devuelve el nombre de la empresa a la firma editorial de los 100 posts.

Contexto: la empresa tiene dos nombres y los dos son correctos —FIREFIGHTER.COM.MX es la marca
del sitio y FIREFIGHTER México es la razon comercial—. Una homologacion anterior dejo el nombre
en cero apariciones, y donde mas se notaba era en la firma: «Area tecnica de FIREFIGHTER.COM.MX»
no es algo que una persona diga, y ademas es el valor que alimenta el `author` del schema
Article, donde lo correcto es la entidad, no el dominio.

Lo que NO se toca: la prosa. «En FIREFIGHTER.COM.MX llevamos esta conversacion cientos de veces
al ano» o «cotiza con FIREFIGHTER.COM.MX» se leen bien y el dominio ahi funciona como sujeto.
Cambiar eso seria reescribir 100 articulos sin necesidad.

Idempotente. Solo toca la linea `author:` del frontmatter.
"""
import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(RAIZ, 'src', 'content', 'blog')

VIEJO = 'Área técnica de FIREFIGHTER.COM.MX'
NUEVO = 'Área técnica de FIREFIGHTER México'

cambiados, ya, otros = 0, 0, []
for nombre in sorted(os.listdir(BLOG)):
    if not nombre.endswith('.md'):
        continue
    ruta = os.path.join(BLOG, nombre)
    with io.open(ruta, encoding='utf-8') as f:
        texto = f.read()

    m = re.search(r'^author:\s*"?(.*?)"?\s*$', texto, re.M)
    if not m:
        otros.append((nombre, 'sin campo author'))
        continue
    actual = m.group(1)
    if actual == NUEVO:
        ya += 1
        continue
    if actual != VIEJO:
        otros.append((nombre, actual))
        continue

    inicio, fin = m.span(1)
    texto = texto[:inicio] + NUEVO + texto[fin:]
    with io.open(ruta, 'w', encoding='utf-8') as f:
        f.write(texto)
    cambiados += 1

print('firmas actualizadas:', cambiados)
print('ya estaban:', ya)
if otros:
    print('con otra firma (no se tocaron):')
    for n, a in otros:
        print('   %-52s %s' % (n, a))
