/**
 * Recortes de título y descripción para SERP.
 * SEOHead añade " | Firefighter.com.mx" (22 caracteres) a todo título,
 * así que aquí se trabaja siempre sobre el presupuesto ya descontado.
 */

const SUFIJO = ' | Firefighter.com.mx'.length; // 21
export const MAX_TITULO = 65 - SUFIJO;         // 44 caracteres útiles
export const MAX_DESC = 158;

/** Corta en el último límite de palabra antes de `max`, sin dejar signos colgando. */
function cortarEnPalabra(texto: string, max: number): string {
  if (texto.length <= max) return texto;
  const trozo = texto.slice(0, max + 1);
  const corte = trozo.lastIndexOf(' ');
  return trozo.slice(0, corte > max * 0.6 ? corte : max).replace(/[\s,;:.\-–—]+$/, '');
}

/**
 * Título para <title>. Prioriza la parte anterior a ':' o '—', que en este
 * proyecto suele ser el titular real; el resto es subtítulo editorial.
 */
export function tituloSeo(titulo: string, max: number = MAX_TITULO): string {
  const limpio = titulo.trim();
  if (limpio.length <= max) return limpio;

  for (const sep of [':', ' — ', ' – ', ' | ']) {
    const i = limpio.indexOf(sep);
    if (i > 15 && i <= max) return limpio.slice(0, i).trim();
  }
  // -1 porque el '…' final también consume presupuesto en la SERP.
  return cortarEnPalabra(limpio, max - 1) + '…';
}

/** Piso útil de una meta description: por debajo de esto la SERP la rellena sola. */
export const MIN_DESC = 110;

/** Descripción para meta: corta en frase completa si cabe, si no en palabra. */
export function descripcionSeo(desc: string, max: number = MAX_DESC): string {
  const limpio = desc.replace(/\s+/g, ' ').trim();
  if (limpio.length <= max) return limpio;

  const frases = limpio.match(/[^.!?]+[.!?]+/g) ?? [];
  let acc = '';
  for (const f of frases) {
    if ((acc + f).trim().length > max) break;
    acc += f;
  }
  // El corte por frase solo gana si deja una descripción con longitud útil;
  // una primera frase corta y contundente no es una meta description.
  if (acc.trim().length >= MIN_DESC) return acc.trim();
  return cortarEnPalabra(limpio, max - 1) + '…';
}
