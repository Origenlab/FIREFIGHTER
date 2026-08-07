#!/usr/bin/env python3
"""Metas del RIT fuera de rango: el title rendereaba en 66 (tope 62) y la description
se cortaba con puntos suspensivos a mitad de frase."""
import json, collections, pathlib

RUTA = pathlib.Path(__file__).resolve().parent.parent / 'src/data/productos.json'
SUFIJO = ' | FIREFIGHTER.COM.MX'

TITLE = 'Sistemas RIT de aire de rescate SCBA'
DESC = ('Paquetes RIT de aire de rescate: por qué ninguno está certificado, qué hace de verdad '
        'el transllenado y qué exigir por escrito antes de firmar.')


def main():
    datos = json.loads(RUTA.read_text(encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    cats = datos['categorias'] if isinstance(datos, dict) else datos
    for cat in cats:
        for prod in cat.get('productos', []):
            if prod.get('slug') != 'sistemas-rit-de-rescate':
                continue
            prod['l3']['seoTitle'] = TITLE
            prod['l3']['seoDescription'] = DESC
            RUTA.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            print(f'title rendereado: {len(TITLE + SUFIJO)}  (rango 50-62)')
            print(f'description:      {len(DESC)}  (rango 140-160)')
            return
    raise SystemExit('producto no encontrado')


if __name__ == '__main__':
    main()
