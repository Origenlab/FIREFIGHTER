import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import { existsSync, statSync, readFileSync } from 'node:fs';
import rehypeInterlink from './src/lib/rehypeInterlink.mjs';

// ─── Sitemap lastmod dinámico ──────────────────────────────────────────────
// Resuelve URL → archivo fuente → fecha real (git log → mtime → omitir).
// Mejor omitir lastmod que mentir con la fecha del build (new Date()).
const ROOT = dirname(fileURLToPath(import.meta.url));
const _dateCache = new Map();

function sourceDate(relPath) {
  if (_dateCache.has(relPath)) return _dateCache.get(relPath);
  let date = null;
  const abs = join(ROOT, relPath);
  if (existsSync(abs)) {
    try {
      const out = execSync(`git log -1 --format=%cI -- "${relPath}"`, {
        cwd: ROOT,
        encoding: 'utf8',
        stdio: ['ignore', 'pipe', 'ignore'],
      }).trim();
      if (out) date = new Date(out);
    } catch {}
    if (!date) {
      try {
        date = statSync(abs).mtime;
      } catch {}
    }
  }
  _dateCache.set(relPath, date);
  return date;
}

function lastmodForUrl(url) {
  const path = new URL(url).pathname.replace(/\/+$/, '');
  const rel = path === '' ? 'index' : path.replace(/^\//, '');
  const candidates = [
    `src/pages/${rel}/index.astro`,
    `src/pages/${rel}.astro`,
  ];
  // Blog: /blog/<slug>/ → src/content/blog/<slug>.md
  if (rel.startsWith('blog/')) {
    const sub = rel.slice('blog/'.length);
    candidates.push(`src/content/blog/${sub}.md`, `src/content/blog/${sub}.mdx`);
  }
  // Estaciones: /directorio/<estado>/<estacion>/ → src/content/stations/<estado>/<estacion>.md
  if (rel.startsWith('directorio/')) {
    const sub = rel.slice('directorio/'.length);
    candidates.push(`src/content/stations/${sub}.md`);
  }
  for (const c of candidates) {
    const d = sourceDate(c);
    if (d) return d;
  }
  return null;
}

// Slugs antiguos que solo existen como redirect: no deben indexarse ni ir al sitemap
const SLUGS_REDIRIGIDOS = [
  'equipos-bomberos', 'scba-respiracion', 'extintores', 'sistemas-fijos',
  'herramientas-rescate', 'deteccion-alarma', 'gabinetes-mangueras',
].map((s) => `/productos/${s}`);

// Fichas L3 en borrador (sin bloque `l3` en productos.json): salen con noindex,
// asi que tampoco deben ir al sitemap. Se quitan de aqui al enriquecer la ficha.
// EPP para bomberos está cerrada: sus seis fichas tienen bloque `l3`.
// Equipos de respiración abrió el 2026-08-06 con la ficha del ERA; sus otros cinco productos
// salen con noindex hasta que se enriquezcan, y se van quitando de esta lista uno por uno.
const L3_BORRADOR = [
  '/productos/equipos-de-respiracion/sistemas-rit-de-rescate',
  '/productos/equipos-de-respiracion/reguladores-y-valvulas',
  '/productos/equipos-de-respiracion/maletines-de-mantenimiento',
];

// Fichas de estado sin verificacion contra texto legal consolidado (confianza != alta):
// salen con noindex, asi que tampoco deben ir al sitemap. Se quitan de aqui solas
// al cambiar "confianza" a "alta" en src/data/cumplimiento-estados.json.
const CUMPLIMIENTO_BORRADOR = JSON.parse(
  readFileSync(join(ROOT, 'src/data/cumplimiento-estados.json'), 'utf8')
)
  .filter((e) => e.confianza !== 'alta')
  .flatMap((e) => [
    `/cumplimiento/estado/${e.slug}`,
    ...JSON.parse(readFileSync(join(ROOT, 'src/data/cumplimiento-giros.json'), 'utf8')).map(
      (g) => `/cumplimiento/estado/${e.slug}/${g.slug}`,
    ),
  ]);

export default defineConfig({
  site: 'https://firefighter.com.mx',
  integrations: [
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
      filter: (page) => {
        const path = new URL(page).pathname.replace(/\/$/, '');
        return !SLUGS_REDIRIGIDOS.includes(path)
          && !L3_BORRADOR.includes(path)
          && !CUMPLIMIENTO_BORRADOR.includes(path);
      },
      serialize: (item) => {
        // lastmod real por archivo fuente; si no se resuelve, se omite
        const lm = lastmodForUrl(item.url);
        if (lm) {
          item.lastmod = lm.toISOString();
        } else {
          delete item.lastmod;
        }
        return item;
      },
    }),
  ],
  // Slugs antiguos de /productos → taxonomía unificada con el homepage
  redirects: {
    '/productos/equipos-bomberos': '/productos/epp-para-bomberos',
    '/productos/scba-respiracion': '/productos/equipos-de-respiracion',
    '/productos/extintores': '/productos/extintores-y-extincion',
    '/productos/sistemas-fijos': '/productos/sistemas-contra-incendio',
    '/productos/herramientas-rescate': '/productos/herramientas-de-rescate',
    '/productos/deteccion-alarma': '/productos/deteccion-y-alarma',
    '/productos/gabinetes-mangueras': '/productos/sistemas-contra-incendio',
  },

  markdown: {
    shikiConfig: {
      theme: 'github-dark',
      wrap: true,
    },
    // Enlaza terminos del catalogo dentro del cuerpo de los articulos del blog.
    // Trabaja sobre el arbol HAST, asi que no puede romper el HTML. Ver src/lib/rehypeInterlink.mjs
    rehypePlugins: [rehypeInterlink],
  },
  build: {
    inlineStylesheets: 'auto',
  },
  compressHTML: true,
  prefetch: {
    prefetchAll: true,
  },
});
