/**
 * rehype-interlink — enlaza términos del catálogo dentro del cuerpo de los artículos del blog.
 *
 * Por qué un plugin de rehype y no editar los .md a mano:
 *   · aplica a los 106 posts a la vez y a cualquiera que se escriba después
 *   · trabaja sobre el árbol HAST, no sobre cadenas de texto, así que **no puede romper el HTML**
 *   · si cambia una URL del catálogo se corrige en un solo lugar
 *
 * Dirección del enlace: blog → catálogo. Es la que importa, porque el blog tiene más páginas y
 * más antigüedad que las fichas de producto. El camino inverso (ficha → blog) ya lo cubren el
 * sidebar de guías y el interlinker de `src/lib/interlink.ts`.
 *
 * Reglas:
 *   · solo la PRIMERA aparición de cada término, y un enlace por destino por artículo
 *   · tope de MAX_ENLACES por artículo para que no se lea como sobreoptimización
 *   · nunca dentro de <a>, <code>, <pre>, <h1>…<h6> ni <blockquote>
 *   · nunca enlaza un artículo a sí mismo ni a la página en la que ya está
 *   · solo apunta a páginas indexables: las L3/L4 en borrador con noindex quedan fuera
 */

const MAX_ENLACES = 6;

const P = '/productos';
const TRAJES = `${P}/epp-para-bomberos/trajes-estructurales-nomex-pbi`;
const CASCOS = `${P}/epp-para-bomberos/cascos-bullard-y-msa`;
const BOTAS = `${P}/epp-para-bomberos/botas-dielectricas`;
const CAPUCHA = `${P}/epp-para-bomberos/protector-de-cuello-y-capucha`;
const GUANTES = `${P}/epp-para-bomberos/guantes-de-intervencion`;

/**
 * El orden importa: lo más específico primero. En un solape gana el término que empieza antes
 * y, a igualdad de inicio, el más largo.
 */
export const REGLAS_CATALOGO = [
  // ── L4 · configuraciones de marca
  { termino: 'SKÖLD HERÖ', href: `${TRAJES}/skold-hero-pbi-max-7-0`, titulo: 'Traje estructural SKÖLD HERÖ con barrera PBI MAX 7.0' },
  { termino: 'PBI MAX', href: `${TRAJES}/skold-hero-pbi-max-7-0`, titulo: 'Traje estructural SKÖLD HERÖ con barrera PBI MAX 7.0' },
  { termino: 'Bullard PX Series', href: `${CASCOS}/bullard-px-series`, titulo: 'Casco estructural Bullard PX Series' },
  { termino: 'PX Series', href: `${CASCOS}/bullard-px-series`, titulo: 'Casco estructural Bullard PX Series' },
  { termino: 'Bullard PX', href: `${CASCOS}/bullard-px-series`, titulo: 'Casco estructural Bullard PX Series' },
  { termino: 'UST Traditional', href: `${CASCOS}/bullard-ust-traditional`, titulo: 'Casco estructural Bullard UST Traditional' },
  { termino: 'UST LowRider', href: `${CASCOS}/bullard-ust-traditional`, titulo: 'Casco estructural Bullard UST Traditional' },
  { termino: 'Bullard UST', href: `${CASCOS}/bullard-ust-traditional`, titulo: 'Casco estructural Bullard UST Traditional' },
  { termino: 'Bullard LT', href: `${CASCOS}/bullard-lt-series`, titulo: 'Casco estructural Bullard LT Series' },
  { termino: 'LT Series', href: `${CASCOS}/bullard-lt-series`, titulo: 'Casco estructural Bullard LT Series' },
  { termino: 'Cairns 1836', href: `${CASCOS}/msa-cairns-1836`, titulo: 'Casco estructural MSA Cairns 1836' },
  { termino: 'Cairns 660C', href: `${CASCOS}/msa-cairns-660c-metro`, titulo: 'Casco estructural MSA Cairns 660C Metro' },
  { termino: '660C Metro', href: `${CASCOS}/msa-cairns-660c-metro`, titulo: 'Casco estructural MSA Cairns 660C Metro' },
  { termino: 'Cairns XF1', href: `${CASCOS}/msa-cairns-xf1`, titulo: 'Casco estructural MSA Cairns XF1' },

  // ── L3 · producto. Varias formas de decir lo mismo: cada post usa la suya, y como solo se
  // enlaza un destino por artículo, sumar variantes amplía cobertura sin subir densidad.
  { termino: 'trajes estructurales', href: TRAJES, titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'traje estructural', href: TRAJES, titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'trajes para bomberos', href: TRAJES, titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'traje para bombero', href: TRAJES, titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'trajes de bombero', href: TRAJES, titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'traje de bombero', href: TRAJES, titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'PBI Matrix', href: TRAJES, titulo: 'Trajes estructurales Nomex y PBI certificados' },
  { termino: 'Nomex IIIA', href: TRAJES, titulo: 'Trajes estructurales Nomex y PBI certificados' },

  // Cascos. Se enlaza con marca o con el adjetivo "estructural" a propósito: "casco" o
  // "cascos forestales" a secas mandarían a esta ficha desde artículos de otra línea.
  { termino: 'cascos estructurales', href: CASCOS, titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'casco estructural', href: CASCOS, titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'cascos de bombero', href: CASCOS, titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'casco de bombero', href: CASCOS, titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'cascos para bomberos', href: CASCOS, titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'casco para bombero', href: CASCOS, titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'cascos Bullard', href: CASCOS, titulo: 'Cascos estructurales Bullard y MSA certificados' },
  { termino: 'casco Bullard', href: CASCOS, titulo: 'Cascos estructurales Bullard y MSA certificados' },

  // Botas. Igual que en cascos: se exige "estructural", marca o "de bombero", porque "botas"
  // a secas aparece en artículos de forestal y de calzado industrial.
  { termino: 'botas estructurales', href: BOTAS, titulo: 'Botas estructurales para bombero certificadas' },
  { termino: 'bota estructural', href: BOTAS, titulo: 'Botas estructurales para bombero certificadas' },
  { termino: 'botas de bombero', href: BOTAS, titulo: 'Botas estructurales para bombero certificadas' },
  { termino: 'bota de bombero', href: BOTAS, titulo: 'Botas estructurales para bombero certificadas' },
  { termino: 'botas para bomberos', href: BOTAS, titulo: 'Botas estructurales para bombero certificadas' },
  { termino: 'HAIX', href: BOTAS, titulo: 'Botas estructurales para bombero certificadas' },

  // Capuchas. "capucha" a secas es demasiado genérico y ya está tomado por el post del blog;
  // aquí se enlaza la ficha solo cuando el texto habla de bloqueo de partículas o de la pieza.
  { termino: 'capuchas de bloqueo de partículas', href: CAPUCHA, titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'capucha de bloqueo de partículas', href: CAPUCHA, titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'capucha particulate blocking', href: CAPUCHA, titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'protector de cuello', href: CAPUCHA, titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'capuchas para bomberos', href: CAPUCHA, titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'capuchas Nomex', href: CAPUCHA, titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'capucha Nomex', href: CAPUCHA, titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'capucha de Nomex', href: CAPUCHA, titulo: 'Capuchas con bloqueo de partículas certificadas' },
  { termino: 'capucha aramídica', href: CAPUCHA, titulo: 'Capuchas con bloqueo de partículas certificadas' },

  // Guantes. Misma cautela: "guantes" a secas cubre nitrilo, extricación y forestal, así que
  // se exige "estructural", "de intervención", "de bombero" o la marca.
  { termino: 'guantes estructurales', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'guante estructural', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'guantes de intervención', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'guante de intervención', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'guantes de bombero', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'guante de bombero', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'guantes para bomberos', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'guantes gauntlet', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'Shelby', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },
  { termino: 'Pro-Tech 8', href: GUANTES, titulo: 'Guantes estructurales para bombero certificados' },

  // ── L2 · categorías
  { termino: 'EPP para bomberos', href: `${P}/epp-para-bomberos`, titulo: 'EPP para bomberos certificado NFPA 1970' },
  { termino: 'EPP estructural', href: `${P}/epp-para-bomberos`, titulo: 'EPP para bomberos certificado NFPA 1970' },
  { termino: 'equipo de protección personal', href: `${P}/epp-para-bomberos`, titulo: 'EPP para bomberos certificado NFPA 1970' },
  { termino: 'equipos de respiración autónoma', href: `${P}/equipos-de-respiracion`, titulo: 'Equipos de respiración autónoma SCBA' },
  { termino: 'equipo de respiración autónoma', href: `${P}/equipos-de-respiracion`, titulo: 'Equipos de respiración autónoma SCBA' },
  { termino: 'protección respiratoria', href: `${P}/equipos-de-respiracion`, titulo: 'Equipos de respiración autónoma SCBA' },
  { termino: 'SCBA', href: `${P}/equipos-de-respiracion`, titulo: 'Equipos de respiración autónoma SCBA' },
  { termino: 'sistemas fijos', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'rescate vehicular', href: `${P}/herramientas-de-rescate`, titulo: 'Herramientas de rescate hidráulicas y manuales' },
  { termino: 'incendios forestales', href: `${P}/equipo-forestal`, titulo: 'Equipo para incendios forestales' },
  { termino: 'herramientas de rescate', href: `${P}/herramientas-de-rescate`, titulo: 'Herramientas de rescate hidráulicas y manuales' },
  { termino: 'sistemas contra incendio', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'detección y alarma', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'equipo forestal', href: `${P}/equipo-forestal`, titulo: 'Equipo para incendios forestales' },
  { termino: 'extintores', href: `${P}/extintores-y-extincion`, titulo: 'Extintores y equipos de extinción' },
  { termino: 'señalética', href: `${P}/senaletica-y-seguridad`, titulo: 'Señalética y seguridad' },
];

/** Nodos cuyo interior no se toca. */
const PROHIBIDOS = new Set(['a', 'code', 'pre', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote']);

const escapar = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** Límite de palabra tolerante con acentos: \b de JS no los maneja. */
const construirRegex = (t) =>
  new RegExp(`(^|[^\\p{L}\\p{N}_-])(${escapar(t)})(?![\\p{L}\\p{N}_-])`, 'iu');

export default function rehypeInterlink(opciones = {}) {
  const reglas = opciones.reglas ?? REGLAS_CATALOGO;
  const max = opciones.max ?? MAX_ENLACES;

  return function transformador(tree, file) {
    // La página en la que estamos: para no enlazarla a sí misma
    const rutaArchivo = String(file?.history?.[0] ?? file?.path ?? '');
    const propio = rutaArchivo.split('/').pop()?.replace(/\.mdx?$/, '') ?? '';

    const pendientes = reglas
      .filter((r) => !r.href.endsWith(`/${propio}`))
      .map((r) => ({ ...r, re: construirRegex(r.termino) }));

    const usados = new Set();
    let insertados = 0;

    const enlazarTexto = (valor) => {
      const cands = [];
      for (const r of pendientes) {
        if (usados.has(r.href)) continue;
        if (insertados + cands.length >= max) break;
        const m = r.re.exec(valor);
        if (!m) continue;
        cands.push({
          inicio: m.index + m[1].length,
          largo: m[2].length,
          texto: m[2],
          href: r.href,
          titulo: r.titulo,
        });
      }
      if (!cands.length) return null;

      cands.sort((a, b) => a.inicio - b.inicio || b.largo - a.largo);

      // descartar solapes
      const firmes = [];
      let corte = -1;
      for (const c of cands) {
        if (c.inicio < corte) continue;
        firmes.push(c);
        corte = c.inicio + c.largo;
      }

      // reconstruir como lista de nodos
      const nodos = [];
      let cursor = 0;
      for (const c of firmes) {
        if (c.inicio > cursor) nodos.push({ type: 'text', value: valor.slice(cursor, c.inicio) });
        nodos.push({
          type: 'element',
          tagName: 'a',
          properties: { href: c.href, className: ['art-il'], title: c.titulo },
          children: [{ type: 'text', value: c.texto }],
        });
        usados.add(c.href);
        insertados++;
        cursor = c.inicio + c.largo;
      }
      if (cursor < valor.length) nodos.push({ type: 'text', value: valor.slice(cursor) });
      return nodos;
    };

    const visitar = (nodo) => {
      if (!nodo.children?.length) return;
      if (nodo.type === 'element' && PROHIBIDOS.has(nodo.tagName)) return;

      const salida = [];
      let cambio = false;
      for (const hijo of nodo.children) {
        if (hijo.type === 'text' && insertados < max && hijo.value.trim()) {
          const nodos = enlazarTexto(hijo.value);
          if (nodos) {
            salida.push(...nodos);
            cambio = true;
            continue;
          }
        }
        salida.push(hijo);
        if (hijo.type === 'element') visitar(hijo);
      }
      if (cambio) nodo.children = salida;
    };

    visitar(tree);
  };
}
