/**
 * Capa de datos del blog: normaliza la coleccion de contenido en objetos
 * listos para pintar (tema asignado, minutos de lectura, fechas).
 */
import { getCollection } from 'astro:content';
import { temaDePost, tiempoLectura, TEMAS } from './blog';

/** Articulos por pagina en el indice del blog. */
export const PER_PAGE = 12;

export interface PostIdx {
  slug: string;
  title: string;
  description: string;
  pubDate: Date;
  updatedDate?: Date;
  author: string;
  tags: string[];
  tema: string;
  minutos: number;
}

/** Articulos con mayor intencion comercial: se muestran como "mas consultados". */
export const DESTACADOS = [
  'precio-trajes-bomberos-mexico-2026',
  'guia-scba-equipos-respiracion-autonoma',
  'extintores-mexico-tipos-normas-seleccion',
  'licitaciones-equipos-contra-incendios-mexico',
  'nom-002-stps-guia-brigadas-industriales',
  'comprar-trajes-bomberos-mexico-guia',
];

export async function getPosts(): Promise<PostIdx[]> {
  const entradas = await getCollection('blog', ({ data }) => !data.draft);
  return entradas
    .map((e) => ({
      slug: e.id,
      title: e.data.title,
      description: e.data.description,
      pubDate: new Date(e.data.pubDate),
      updatedDate: e.data.updatedDate ? new Date(e.data.updatedDate) : undefined,
      author: e.data.author,
      tags: e.data.tags ?? [],
      tema: temaDePost(e.id, e.data.title, e.data.tags ?? []),
      minutos: tiempoLectura(e.body ?? ''),
    }))
    .sort((a, b) => b.pubDate.valueOf() - a.pubDate.valueOf());
}

export function conteoPorTema(posts: PostIdx[]): Record<string, number> {
  const conteo: Record<string, number> = {};
  for (const t of TEMAS) conteo[t.slug] = 0;
  for (const p of posts) conteo[p.tema] = (conteo[p.tema] ?? 0) + 1;
  return conteo;
}

export function masConsultados(posts: PostIdx[], n = 5): PostIdx[] {
  const porSlug = new Map(posts.map((p) => [p.slug, p]));
  const curados = DESTACADOS.map((s) => porSlug.get(s)).filter(Boolean) as PostIdx[];
  const resto = posts.filter((p) => !DESTACADOS.includes(p.slug));
  return [...curados, ...resto].slice(0, n);
}

/** Relacionados: mismo tema primero, luego tags en comun. */
export function relacionados(posts: PostIdx[], actual: PostIdx, n = 4): PostIdx[] {
  const otros = posts.filter((p) => p.slug !== actual.slug);
  const puntuar = (p: PostIdx) =>
    (p.tema === actual.tema ? 10 : 0) + p.tags.filter((t) => actual.tags.includes(t)).length;
  return otros
    .map((p) => ({ p, s: puntuar(p) }))
    .filter((x) => x.s > 0)
    .sort((a, b) => b.s - a.s || b.p.pubDate.valueOf() - a.p.pubDate.valueOf())
    .slice(0, n)
    .map((x) => x.p);
}
