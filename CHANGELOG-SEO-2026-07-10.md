# CHANGELOG SEO — firefighter.com.mx — 2026-07-10

Alcance: TÉCNICO (SOP Prompt Maestro SEO, Ola 3). Cero datos de negocio nuevos.
Commit principal: `8f09f16` sobre `main` (repo `Origenlab/FIREFIGHTER`, deploy Cloudflare Pages proyecto `firefightercommx` vía `deploy.yml`).

## Hallazgo CRÍTICO de infraestructura (patrón MEDEDUL) — REQUIERE ACCIÓN MANUAL

**El dominio firefighter.com.mx NO recibe los deploys de Cloudflare Pages.**

Evidencia (2026-07-10):
- `https://firefighter.com.mx/sitemap-0.xml` → lastmod `2026-06-16T17:16:18Z` + header `last-modified: Tue, 16 Jun 2026 17:16:49 GMT` (típico de GH Pages; CF Pages no manda last-modified).
- `https://firefightercommx.pages.dev/sitemap-0.xml` → lastmod `2026-06-22T17:58:28Z` (último deploy real).
- `gh api repos/Origenlab/FIREFIGHTER/pages` → **GH Pages ACTIVO con `cname: firefighter.com.mx`**, status `built`, build_type `workflow`. Es un zombi: el workflow de GH Pages ya no existe (se reemplazó por deploy.yml → CF Pages el 19-jun), así que el dominio sirve un build congelado del 16-jun para siempre.
- md5 del HTML de home apex ≠ pages.dev.

Fix manual (dashboard, en este orden — regla: nunca matar el origen viejo sin el nuevo verificado):
1. Cloudflare Pages → proyecto `firefightercommx` → Custom domains → agregar `firefighter.com.mx` (y `www.firefighter.com.mx`). Esto reapunta el DNS del proxy CF al proyecto Pages.
2. Verificar apex sirve el build nuevo (sitemap lastmod ya no es 2026-06-16).
3. Solo entonces: deshabilitar GH Pages en `Origenlab/FIREFIGHTER` (Settings → Pages) para matar el zombi.
4. www hoy da 301→apex cortesía del GH Pages zombi; al matarlo, el 301 lo debe dar el custom domain www del proyecto CF Pages (paso 1) o una Redirect Rule de Cloudflare.

**Hasta hacer esto, todos los fixes de este changelog solo son visibles en `firefightercommx.pages.dev`.**

## Cambios aplicados (código)

| # | Fix | Archivos |
|---|-----|----------|
| 1 | **OG default 404 → real**: `/images/og-image.jpg` no existía (404 en el og:image de las ~248 páginas). Generado `/images/og-image.png` 1200×630 branded (escudo+flama, paleta real del sitio #dc2626/#1e293b) y default actualizado. PNG por ser arte plano. | `public/images/og-image.png` (nuevo), `src/components/seo/SEOHead.astro` |
| 2 | **og:image:type dinámico** según extensión real de la imagen resuelta (antes ausente). | `SEOHead.astro` |
| 3 | **Organization duplicado en home**: SEOHead (includeWebsiteSchema) y Footer emitían dos Organization con el mismo `@id` y datos distintos. Se dejó solo el del Footer (más completo, site-wide). Home queda WebSite + Organization. | `SEOHead.astro` |
| 4 | **BreadcrumbList ×2 en páginas de estación** (222 págs): schema manual + el generado por SEOHead. Eliminado el manual. Ahora: home 0, resto máx 1. | `src/pages/directorio/[state]/[station].astro` |
| 5 | **BreadcrumbList con item incorrecto**: el crumb final (página actual, sin URL) apuntaba al home. Ahora se omite `item` (válido para Google). | `src/lib/seo.ts` |
| 6 | **Logos 404 en JSON-LD**: `/logo.svg` (Organization en seo.ts + publisher de Article) y `/images/logo-firefighter.svg` (Footer) no existen → remapeados a `/images/logo-firefighter-mexico.svg` (existe) como ImageObject con width/height reales 200×50 (viewBox del SVG). | `src/lib/seo.ts`, `src/components/layout/Footer.astro` |
| 7 | **Imagen 404 en FireStation schema**: `/images/og-station-default.jpg` no existe → remapeada al OG default real. | `[station].astro` |
| 8 | **apple-touch-icon 404**: `<link>` apuntaba a `/images/apple-touch-icon.png`; el archivo vive en `/apple-touch-icon.png`. | `src/layouts/BaseLayout.astro` |
| 9 | **Sitemap lastmod real**: `lastmod: new Date()` marcaba las 248 URLs con la fecha del build. Ahora resolver URL→fuente (src/pages, content blog y stations) → `git log -1 --format=%cI` → mtime → si no resuelve se OMITE. Resultado: 202 lastmod con 9 fechas reales distintas, 46 URLs dinámicas sin lastmod (honesto). | `astro.config.mjs` |
| 10 | **fetch-depth: 0** en el checkout del workflow (sin historia, git log devuelve la fecha del HEAD para todo). | `.github/workflows/deploy.yml` |
| 11 | **`public/_redirects`** con `www → apex 301` (solo surtirá efecto cuando www esté adjunto al proyecto CF Pages; hoy el 301 lo da el GH Pages zombi). | `public/_redirects` (nuevo) |

## Validación local (gates)

- `npx astro check`: **0 errores** (75 hints preexistentes).
- Build: verde, 249 páginas.
- Validador dist/: 0 og rotos, 0 og avif/webp, og:image:type en 100% de páginas, breadcrumbs OK, JSON-LD parseable, assets de JSON-LD existen, lastmod variado.
- Scan de secretos: limpio. Remote sin token.

## Hallazgos NO aplicados / anotados

- **Managed robots.txt de Cloudflare** activo en el dominio: antepone bloques `Disallow` para GPTBot, Google-Extended, meta-externalagent y CloudflareBrowserRenderingCrawler (visible solo live, pisa el robots.txt del repo). Contrario a la estrategia AI-readiness del portafolio → **manual dashboard**: Cloudflare → firefighter.com.mx → AI Crawl Control / robots.txt gestionado → desactivar.
- `og:image:width/height` hardcodeados 1200×630 en SEOHead: la única imagen no-default usada como og (`/images/blog/911-mexico.jpg`) mide 1200×675 → discrepancia menor, no bloqueante. Mejora futura: emitir dimensiones reales por imagen.
- `aggregateRating` condicional en FireStation schema (`data.verified`) es dato preexistente del negocio: NO tocado (fuera de alcance técnico).
- `sameAs` de redes sociales en Footer (instagram/linkedin/youtube @firefightermx): preexistente, no tocado.
- Páginas dinámicas sin archivo fuente 1:1 (índices de estado `/directorio/<estado>/`, categorías `/productos/<cat>/`) quedan sin lastmod por diseño (omitir > mentir).
- `deploy.yml.cfbak` es backup muerto; no se tocó.
- `AGENTS.md` untracked ajeno en el working tree: no commiteado.

## Verificación live post-deploy (contra pages.dev; el dominio sigue congelado — ver arriba)

Ver resultados al final de la Action en el reporte del orquestador. Esperado tras cutover del dominio: mismos resultados en firefighter.com.mx.
