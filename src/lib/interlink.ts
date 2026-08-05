/**
 * Interlinking contextual del cuerpo editorial de las fichas L3 y L4.
 *
 * El problema que resuelve: el copy menciona configuraciones hermanas, normas y conceptos
 * que ya tienen página propia en el sitio, pero escribir los <a> a mano en cada párrafo del
 * JSON es inmantenible y se rompe en cuanto cambia una URL.
 *
 * Cómo funciona: se declara un mapa de términos → destino y el interlinker enlaza la
 * PRIMERA aparición de cada término en el cuerpo de la página, una sola vez por destino,
 * con un tope de enlaces para que no se lea como spam.
 *
 * Reglas de seguridad:
 *  - Nunca toca el interior de una etiqueta HTML: separa nodos de texto de nodos de marcado.
 *  - Nunca enlaza dentro de un <a> ya existente.
 *  - Resuelve solapes: si dos términos coinciden en la misma zona, gana el que empieza antes
 *    y, a igualdad, el más largo.
 */

export interface ReglaEnlace {
  /** Término tal como aparece en el copy. Se usa con límites de palabra. */
  termino: string;
  href: string;
  /** Texto del atributo title. Opcional. */
  titulo?: string;
}

const escapar = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** Límite de palabra tolerante con acentos, que \b de JS no maneja bien. */
function construirRegex(termino: string): RegExp {
  return new RegExp(`(^|[^\\p{L}\\p{N}_-])(${escapar(termino)})(?![\\p{L}\\p{N}_-])`, 'u');
}

export interface Interlinker {
  /** Enlaza los términos pendientes en un fragmento de HTML. */
  (html: string): string;
  /** Cuántos enlaces se insertaron. Útil para verificar en build. */
  total: () => number;
}

/**
 * Crea un interlinker con estado: recuerda qué destinos ya enlazó para no repetirlos
 * a lo largo de toda la página. Hay que crear uno nuevo por página.
 */
export function crearInterlinker(reglas: ReglaEnlace[], maxEnlaces = 12): Interlinker {
  const pendientes = reglas
    .filter((r) => r.termino && r.href)
    .map((r) => ({ ...r, re: construirRegex(r.termino) }));
  const usados = new Set<string>();
  let insertados = 0;

  const enlazarTexto = (texto: string): string => {
    if (!texto.trim()) return texto;

    // 1 · recolectar candidatos sin solape
    type Cand = { inicio: number; largo: number; texto: string; href: string; titulo?: string };
    const cands: Cand[] = [];
    for (const r of pendientes) {
      if (usados.has(r.href) || insertados + cands.length >= maxEnlaces) continue;
      const m = r.re.exec(texto);
      if (!m) continue;
      const inicio = m.index + m[1].length;
      cands.push({ inicio, largo: m[2].length, texto: m[2], href: r.href, titulo: r.titulo });
    }
    if (!cands.length) return texto;

    cands.sort((a, b) => a.inicio - b.inicio || b.largo - a.largo);

    // 2 · descartar solapes
    const firmes: Cand[] = [];
    let corte = -1;
    for (const c of cands) {
      if (c.inicio < corte) continue;
      firmes.push(c);
      corte = c.inicio + c.largo;
    }

    // 3 · construir de atrás hacia adelante para no mover los índices
    let salida = texto;
    for (const c of [...firmes].reverse()) {
      const attrTitulo = c.titulo ? ` title="${c.titulo.replace(/"/g, '&quot;')}"` : '';
      salida =
        salida.slice(0, c.inicio) +
        `<a class="l3-il" href="${c.href}"${attrTitulo}>${c.texto}</a>` +
        salida.slice(c.inicio + c.largo);
    }
    firmes.forEach((c) => usados.add(c.href));
    insertados += firmes.length;
    return salida;
  };

  const fn = ((html: string): string => {
    if (!html) return html;
    if (insertados >= maxEnlaces) return html;

    const partes = html.split(/(<[^>]+>)/);
    let dentroDeAncla = 0;

    for (let i = 0; i < partes.length; i++) {
      const p = partes[i];
      if (p.startsWith('<')) {
        if (/^<a[\s>]/i.test(p)) dentroDeAncla++;
        else if (/^<\/a>/i.test(p)) dentroDeAncla = Math.max(0, dentroDeAncla - 1);
        continue;
      }
      if (dentroDeAncla > 0) continue;
      partes[i] = enlazarTexto(p);
    }
    return partes.join('');
  }) as Interlinker;

  fn.total = () => insertados;
  return fn;
}

/**
 * Reglas de sitio: normas y conceptos que ya tienen artículo propio en el blog,
 * más categorías del catálogo. Se combinan con las reglas dinámicas de cada página
 * (configuraciones hermanas, producto padre) que se arman en la plantilla.
 *
 * El orden importa: lo más específico primero, porque en un solape gana el término
 * que empieza antes y, a igualdad de inicio, el más largo.
 */
export const REGLAS_SITIO: ReglaEnlace[] = [
  { termino: 'NFPA 1970', href: '/blog/nfpa-1971-mexico-norma-bomberos', titulo: 'NFPA 1970 en México: qué certifica y cómo leer un certificado' },
  { termino: 'NFPA 1971', href: '/blog/nfpa-1971-mexico-norma-bomberos', titulo: 'NFPA 1970 en México: qué certifica y cómo leer un certificado' },
  { termino: 'NFPA 1850', href: '/blog/mantenimiento-epp-estructural-nfpa-1851', titulo: 'Mantenimiento de EPP estructural bajo NFPA 1850' },
  { termino: 'NFPA 1851', href: '/blog/mantenimiento-epp-estructural-nfpa-1851', titulo: 'Mantenimiento de EPP estructural bajo NFPA 1850' },
  { termino: 'THL', href: '/blog/guia-trajes-estructurales-nfpa-1971', titulo: 'Guía de trajes estructurales: TPP, THL y cómo comparar' },
  { termino: 'TPP', href: '/blog/guia-trajes-estructurales-nfpa-1971', titulo: 'Guía de trajes estructurales: TPP, THL y cómo comparar' },
  { termino: 'tallaje', href: '/blog/equipar-brigada-trajes-bomberos-tallaje-licitacion', titulo: 'Equipar una brigada: tallaje, volumen y licitación' },
  { termino: 'licitación', href: '/blog/licitaciones-equipos-contra-incendios-mexico', titulo: 'Licitaciones públicas de equipos contra incendios en México' },
  { termino: 'capucha', href: '/blog/capucha-nomex-pbi-proteccion-cuello-cara', titulo: 'Capucha Nomex y PBI: protección de cuello y cara' },
  { termino: 'Nomex', href: '/blog/traje-bombero-nomex-guia-completa', titulo: 'Traje de bombero Nomex: guía técnica completa' },
  { termino: 'equipo de respiración', href: '/productos/equipos-de-respiracion', titulo: 'Equipos de respiración autónoma certificados' },
];
