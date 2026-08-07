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

    // 2 · descartar solapes y destinos repetidos DENTRO del mismo nodo de texto.
    //     El filtro `usados` de arriba solo ve los destinos ya insertados en nodos anteriores,
    //     así que dos reglas distintas con el mismo href —"pieza facial" y "equipo de
    //     respiración", por ejemplo— podían enlazar dos veces al mismo destino en un párrafo.
    const firmes: Cand[] = [];
    const enEsteNodo = new Set<string>();
    let corte = -1;
    for (const c of cands) {
      if (c.inicio < corte || enEsteNodo.has(c.href)) continue;
      firmes.push(c);
      enEsteNodo.add(c.href);
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
  // ── L4 · configuraciones con ficha propia. Lo más específico del sitio.
  { termino: 'Bullard PX Series', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa/bullard-px-series', titulo: 'Casco estructural Bullard PX Series' },
  { termino: 'PX Series', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa/bullard-px-series', titulo: 'Casco estructural Bullard PX Series' },
  { termino: 'UST Traditional', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa/bullard-ust-traditional', titulo: 'Casco estructural Bullard UST Traditional' },
  { termino: 'UST LowRider', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa/bullard-ust-traditional', titulo: 'Casco estructural Bullard UST Traditional' },
  { termino: 'LT Series', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa/bullard-lt-series', titulo: 'Casco estructural Bullard LT Series' },
  { termino: 'Cairns 1836', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa/msa-cairns-1836', titulo: 'Casco estructural MSA Cairns 1836' },
  { termino: '660C Metro', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa/msa-cairns-660c-metro', titulo: 'Casco estructural MSA Cairns 660C Metro' },
  { termino: 'Cairns XF1', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa/msa-cairns-xf1', titulo: 'Casco estructural MSA Cairns XF1' },

  // ── L3 · fichas de producto publicadas. Van después: son menos específicas y
  // la plantilla filtra la regla de la propia página para no autoenlazarse.
  { termino: 'cascos estructurales', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa', titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'casco estructural', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa', titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'capuchas de bloqueo de partículas', href: '/productos/epp-para-bomberos/protector-de-cuello-y-capucha', titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'capucha de bloqueo de partículas', href: '/productos/epp-para-bomberos/protector-de-cuello-y-capucha', titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'botas estructurales', href: '/productos/epp-para-bomberos/botas-dielectricas', titulo: 'Botas estructurales para bombero certificadas' },
  { termino: 'bota estructural', href: '/productos/epp-para-bomberos/botas-dielectricas', titulo: 'Botas estructurales para bombero certificadas' },
  { termino: 'trajes estructurales', href: '/productos/epp-para-bomberos/trajes-estructurales-nomex-pbi', titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'traje estructural', href: '/productos/epp-para-bomberos/trajes-estructurales-nomex-pbi', titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'guantes estructurales', href: '/productos/epp-para-bomberos/guantes-de-intervencion', titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'guante estructural', href: '/productos/epp-para-bomberos/guantes-de-intervencion', titulo: 'Guantes estructurales para bombero certificados' },

  // ── Cumplimiento · normativa mexicana. Va antes que las NFPA porque la NOM
  // es la que tiene fuerza legal en México y es el destino que queremos reforzar.
  { termino: 'NOM-002-STPS-2010', href: '/cumplimiento/normas/nom-002-stps-2010', titulo: 'NOM-002-STPS-2010: qué obliga y con qué numeral' },
  { termino: 'NOM-002-STPS', href: '/cumplimiento/normas/nom-002-stps-2010', titulo: 'NOM-002-STPS-2010: qué obliga y con qué numeral' },
  { termino: 'clasificación de riesgo de incendio', href: '/cumplimiento/normas/nom-002-stps-2010#clasificacion', titulo: 'Riesgo ordinario o alto: la Tabla A.1 de la NOM-002' },
  { termino: 'Programa Interno de Protección Civil', href: '/cumplimiento#estados', titulo: 'Quién autoriza el Programa Interno en cada estado' },
  { termino: 'protección civil', href: '/cumplimiento#estados', titulo: 'Normativa de protección civil por entidad federativa' },
  { termino: 'brigada contra incendio', href: '/cumplimiento/normas/nom-002-stps-2010#brigadas', titulo: 'Cuándo la NOM-002 obliga a constituir brigada' },

  // ── Sustantivo a secas. Estas reglas SOLO corren en el cuerpo de las fichas L3 y L4, donde
  // el contexto ya es estructural: cuando la ficha del traje dice "la bota" o la del casco dice
  // "la careta", habla de la pieza hermana del mismo conjunto. En el blog serían peligrosas
  // (hay artículos de forestal, industrial y rescate) y por eso no están en REGLAS_CATALOGO.
  // Van después de las versiones con adjetivo para que gane siempre la más específica.
  { termino: 'chaquetones', href: '/productos/epp-para-bomberos/trajes-estructurales-nomex-pbi', titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'chaquetón', href: '/productos/epp-para-bomberos/trajes-estructurales-nomex-pbi', titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'cascos', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa', titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'casco', href: '/productos/epp-para-bomberos/cascos-bullard-y-msa', titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'botas', href: '/productos/epp-para-bomberos/botas-dielectricas', titulo: 'Botas estructurales para bombero certificadas' },
  { termino: 'guantes', href: '/productos/epp-para-bomberos/guantes-de-intervencion', titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'capuchas', href: '/productos/epp-para-bomberos/protector-de-cuello-y-capucha', titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'protector de cuello', href: '/productos/epp-para-bomberos/protector-de-cuello-y-capucha', titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'caretas', href: '/productos/epp-para-bomberos/viseras-y-caretas', titulo: 'Viseras, caretas y goggles para casco estructural' },
  // ── L3 de equipos de respiración. La categoría abrió el 2026-08-06. Estas reglas van antes
  // que la de la categoría ('equipo de respiración') para que gane la ficha, que es más
  // específica y es la que tiene el detalle de NIOSH y de la configuración aprobada.
  { termino: 'equipos de respiración autónoma', href: '/productos/equipos-de-respiracion/scba-scott-air-pak', titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'equipo de respiración autónomo', href: '/productos/equipos-de-respiracion/scba-scott-air-pak', titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'ERA de circuito abierto', href: '/productos/equipos-de-respiracion/scba-scott-air-pak', titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'cilindros de aire respirable', href: '/productos/equipos-de-respiracion/cilindros-30-45-60-min', titulo: 'Cilindros de aire respirable para equipos autónomos' },
  { termino: 'cilindro de aire respirable', href: '/productos/equipos-de-respiracion/cilindros-30-45-60-min', titulo: 'Cilindros de aire respirable para equipos autónomos' },
  { termino: 'cilindros', href: '/productos/equipos-de-respiracion/cilindros-30-45-60-min', titulo: 'Cilindros de aire respirable para equipos autónomos' },
  { termino: 'cilindro', href: '/productos/equipos-de-respiracion/cilindros-30-45-60-min', titulo: 'Cilindros de aire respirable para equipos autónomos' },
  { termino: 'piezas faciales', href: '/productos/equipos-de-respiracion/mascaras-completas-3m', titulo: 'Piezas faciales de presión positiva y prueba de ajuste' },
  { termino: 'prueba de ajuste', href: '/productos/equipos-de-respiracion/mascaras-completas-3m', titulo: 'Piezas faciales de presión positiva y prueba de ajuste' },
  { termino: 'careta', href: '/productos/epp-para-bomberos/viseras-y-caretas', titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'goggles', href: '/productos/epp-para-bomberos/viseras-y-caretas', titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'pieza facial', href: '/productos/equipos-de-respiracion/mascaras-completas-3m', titulo: 'Piezas faciales de presión positiva y prueba de ajuste' },
  { termino: 'sistemas RIT', href: '/productos/equipos-de-respiracion/sistemas-rit-de-rescate', titulo: 'Sistemas RIT de aire de rescate para bomberos' },
  { termino: 'sistema RIT', href: '/productos/equipos-de-respiracion/sistemas-rit-de-rescate', titulo: 'Sistemas RIT de aire de rescate para bomberos' },
  { termino: 'paquete RIT', href: '/productos/equipos-de-respiracion/sistemas-rit-de-rescate', titulo: 'Sistemas RIT de aire de rescate para bomberos' },
  { termino: 'aire de rescate', href: '/productos/equipos-de-respiracion/sistemas-rit-de-rescate', titulo: 'Sistemas RIT de aire de rescate para bomberos' },
  { termino: 'transllenado', href: '/productos/equipos-de-respiracion/sistemas-rit-de-rescate', titulo: 'Sistemas RIT de aire de rescate para bomberos' },

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
