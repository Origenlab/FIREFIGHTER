# Auditoría del sitio

Tres scripts sin dependencias. Correr **después** de `npm run build`, porque leen `dist/`.

```bash
npm run build
python3 scripts/auditoria/audit-catalogo.py   # homologación de las 8 categorías L2
python3 scripts/auditoria/audit-sitio.py      # títulos, descriptions, H1, imágenes, pesos
python3 scripts/auditoria/peso-gzip.py        # peso real transferido de páginas clave
```

## `audit-catalogo.py`

Lee `src/data/productos.json` y verifica que las 8 categorías cumplan el piso mínimo:
2 heroBloques, 3 párrafos de intro, 6+ normas, 3 aplicaciones, 6 productos con
`desc` + `specs` + `intro` + `galeria` + `slug`, 8 FAQs, `title` ≤ 65 con sufijo
y `description` entre 110 y 160.

También cruza todas las rutas de imagen y reporta **fotos usadas en más de una categoría**,
que es lo que hace que dos páginas se sientan la misma.

Salida esperada: `TODO EN ORDEN` y `imagenes compartidas entre categorias: 0`.

## `audit-sitio.py`

Recorre las 272 páginas de `dist/` y reporta títulos de más de 65 caracteres, descriptions
fuera del rango útil, páginas sin H1 o con varios, `img` sin `loading` o sin `alt`,
imágenes rotas y las páginas más pesadas.

Notas sobre falsos positivos conocidos:

- `blog/valvulas-osy-...` mide 67 porque `&amp;` cuenta 5 caracteres en el HTML y 1 en la SERP
- Las 7 páginas «sin H1» son los redirects de slugs viejos, excluidos del sitemap

## `peso-gzip.py`

Compara peso en disco contra peso gzipeado de tres páginas representativas y del sitio
completo. Útil antes de decidir una optimización: mucho de lo que parece pesado comprime
bien y no vale la pena tocarlo.

## Al agregar fotos

Descargar el JPG de Unsplash, revisarlo en contact sheet, convertir y borrar el JPG:

```bash
cwebp -q 80 -m 6 entrada.jpg -o public/images/catalogo/{id13}-{ancho}x{alto}.webp
```

Tamaños: card de producto `600x400`, galería grande `1000x750`, chicas `600x450`,
hero de categoría `1200x800`.
