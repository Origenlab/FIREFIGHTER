/**
 * rehype-interlink — enlaza términos del catálogo dentro del cuerpo de los artículos del blog.
 *
 * Por qué un plugin de rehype y no editar los .md a mano:
 *   · aplica a los 106 posts a la vez y a cualquiera que se escriba después
 *   · trabaja sobre el árbol HAST, no sobre cadenas de texto, así que **no puede romper el HTML**
 *   · si cambia una URL del catálogo se corrige en un solo lugar
 *
 * Dirección del enlace: blog → catálogo y blog → /cumplimiento. Es la que importa, porque el
 * blog tiene más páginas y más antigüedad que las fichas de producto y que la sección normativa.
 * El camino inverso (ficha → blog) ya lo cubren el sidebar de guías y el interlinker de
 * `src/lib/interlink.ts`.
 *
 * Reglas:
 *   · solo la PRIMERA aparición de cada término, y un enlace por destino por artículo
 *   · el tope es **proporcional al largo del artículo**, no fijo (ver TOPE)
 *   · nunca dentro de <a>, <code>, <pre>, <h1>…<h6> ni <blockquote>
 *   · nunca enlaza un artículo a sí mismo ni a la página en la que ya está
 *   · solo apunta a páginas indexables: las L3/L4 en borrador con noindex quedan fuera
 */

/**
 * Tope proporcional. Un tope fijo trataba igual a una nota de 600 palabras y a una guía de
 * 3,000: en la corta se leía como sobreoptimización y en la larga dejaba fuera a las fichas
 * L4, que son las más específicas del sitio y las últimas de la lista.
 * Densidad objetivo: ~1 enlace cada 400 palabras, con piso de 4 y techo de 10.
 */
const TOPE = { palabrasPorEnlace: 300, min: 4, max: 10 };

/** Se conserva como default del parámetro `max` para llamadas fuera del pipeline del blog. */
const MAX_ENLACES = 6;

const topePorLargo = (palabras) =>
  Math.max(TOPE.min, Math.min(TOPE.max, Math.floor(palabras / TOPE.palabrasPorEnlace)));

const P = '/productos';
const TRAJES = `${P}/epp-para-bomberos/trajes-estructurales-nomex-pbi`;
const CASCOS = `${P}/epp-para-bomberos/cascos-bullard-y-msa`;
const BOTAS = `${P}/epp-para-bomberos/botas-dielectricas`;
const CAPUCHA = `${P}/epp-para-bomberos/protector-de-cuello-y-capucha`;
const GUANTES = `${P}/epp-para-bomberos/guantes-de-intervencion`;
const VISERAS = `${P}/epp-para-bomberos/viseras-y-caretas`;
const ERA = `${P}/equipos-de-respiracion/scba-scott-air-pak`;
const C = '/cumplimiento';

/**
 * El orden importa: lo más específico primero. En un solape gana el término que empieza antes
 * y, a igualdad de inicio, el más largo.
 */
export const REGLAS_CATALOGO = [
  // ── L4 · configuraciones de marca
  { termino: 'PBI MAX 7.0', href: `${TRAJES}/skold-hero-pbi-max-7-0`, titulo: 'Traje estructural SKÖLD HERÖ con barrera PBI MAX 7.0' },
  { termino: 'PBI MAX', href: `${TRAJES}/skold-hero-pbi-max-7-0`, titulo: 'Traje estructural SKÖLD HERÖ con barrera PBI MAX 7.0' },
  { termino: 'SKÖLD HERÖ', href: `${TRAJES}/skold-hero-pbi-max-7-0`, titulo: 'Traje estructural SKÖLD HERÖ con barrera PBI MAX 7.0' },
  // Las otras cuatro barreras exteriores de la misma línea. Se exige la palabra "barrera" o el
  // nombre compuesto: "Advance" y "Pioneer" a secas son demasiado comunes en español técnico.
  { termino: 'barrera Advance', href: `${TRAJES}/skold-hero-advance`, titulo: 'Traje estructural SKÖLD HERÖ con barrera Advance' },
  { termino: 'Kombat Flex', href: `${TRAJES}/skold-hero-kombat-flex`, titulo: 'Traje estructural SKÖLD HERÖ con barrera Kombat Flex' },
  { termino: 'barrera Pioneer', href: `${TRAJES}/skold-hero-pioneer`, titulo: 'Traje estructural SKÖLD HERÖ con barrera Pioneer' },
  { termino: 'Defender 750', href: `${TRAJES}/skold-hero-defender-750`, titulo: 'Traje estructural SKÖLD HERÖ con barrera Defender 750' },
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

  // Viseras y caretas. "visera" a secas es ambigua en español mexicano —la NOM de cascos llama
  // visera al ala—, así que se enlaza por la pieza óptica o por la función.
  { termino: 'viseras y caretas', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'visera del casco', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'careta del casco', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'careta de policarbonato', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'visera abatible', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'visera facial', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'visera protectora', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'protección ocular', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'goggles para bombero', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'goggles estructurales', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },
  { termino: 'Bourkes', href: VISERAS, titulo: 'Viseras, caretas y goggles para casco estructural' },

  // Equipos de respiración autónoma. Van ANTES de la regla de categoría 'SCBA' para que la
  // ficha gane: es la que explica la doble certificación NIOSH + NFPA. Se exige "autónomo",
  // "ERA" o el nombre de plataforma; "respiración" a secas aparece en artículos de espacios
  // confinados y de líneas de aire, que son otro producto.
  { termino: 'equipos de respiración autónoma', href: ERA, titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'equipo de respiración autónomo', href: ERA, titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'equipo de respiración autónoma', href: ERA, titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'ERA de circuito abierto', href: ERA, titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'MSA G1', href: ERA, titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'Air-Pak', href: ERA, titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'NIOSH', href: ERA, titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },
  { termino: 'NFPA 1981', href: ERA, titulo: 'Equipos de respiración autónoma certificados NFPA 1970 y NIOSH' },

  // ── L2 · categorías
  { termino: 'EPP para bomberos', href: `${P}/epp-para-bomberos`, titulo: 'EPP para bomberos certificado NFPA 1970' },
  { termino: 'EPP estructural', href: `${P}/epp-para-bomberos`, titulo: 'EPP para bomberos certificado NFPA 1970' },
  { termino: 'equipo de protección personal', href: `${P}/epp-para-bomberos`, titulo: 'EPP para bomberos certificado NFPA 1970' },
  // Las dos variantes de "equipo de respiración autónoma" ahora apuntan a la ficha L3, que es
  // más específica; se quitaron de aquí para no dejar reglas muertas apuntando a la categoría.
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

  // ── Vocabulario real de los artículos técnicos de las otras siete líneas.
  // Sin estos términos, 22 de los 100 posts no tenían un solo enlace al catálogo: hablan de
  // sprinklers, paneles y acoples, no de "sistemas fijos" ni de "detección y alarma".
  // Detección y alarma
  { termino: 'detector de humo', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'detectores de humo', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'detector de calor', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'detectores de calor', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'detector de gas', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'detectores de gas', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'panel de alarma', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'panel direccionable', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'Notifier', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'SpectrAlert', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'sirenas y estrobos', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  { termino: 'NFPA 72', href: `${P}/deteccion-y-alarma`, titulo: 'Sistemas de detección y alarma de incendio' },
  // Sistemas fijos, mangueras y gabinetes
  { termino: 'sprinklers', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'rociadores', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'NFPA 13', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'bomba contra incendio', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'bombas contra incendio', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'NFPA 20', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'gabinete contra incendio', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'gabinetes contra incendio', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'manguera contra incendio', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'mangueras contra incendio', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'acoples Storz', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'acople Storz', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'válvula OS&Y', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'válvulas OS&Y', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'agente limpio', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'agentes limpios', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'NFPA 2001', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  { termino: 'supresión automática', href: `${P}/sistemas-contra-incendio`, titulo: 'Sistemas fijos contra incendio' },
  // Herramientas de rescate
  { termino: 'herramienta hidráulica', href: `${P}/herramientas-de-rescate`, titulo: 'Herramientas de rescate hidráulicas y manuales' },
  { termino: 'herramientas hidráulicas', href: `${P}/herramientas-de-rescate`, titulo: 'Herramientas de rescate hidráulicas y manuales' },
  { termino: 'generador hidráulico', href: `${P}/herramientas-de-rescate`, titulo: 'Herramientas de rescate hidráulicas y manuales' },
  { termino: 'Holmatro', href: `${P}/herramientas-de-rescate`, titulo: 'Herramientas de rescate hidráulicas y manuales' },
  { termino: 'NFPA 1936', href: `${P}/herramientas-de-rescate`, titulo: 'Herramientas de rescate hidráulicas y manuales' },
  // Forestal
  { termino: 'McLeod', href: `${P}/equipo-forestal`, titulo: 'Equipo para incendios forestales' },
  { termino: 'línea de defensa', href: `${P}/equipo-forestal`, titulo: 'Equipo para incendios forestales' },
  { termino: 'mochila aspersora', href: `${P}/equipo-forestal`, titulo: 'Equipo para incendios forestales' },
  { termino: 'NFPA 1977', href: `${P}/equipo-forestal`, titulo: 'Equipo para incendios forestales' },
  // Extintores
  { termino: 'extintor', href: `${P}/extintores-y-extincion`, titulo: 'Extintores y equipos de extinción' },
  { termino: 'recarga de extintores', href: `${P}/extintores-y-extincion`, titulo: 'Extintores y equipos de extinción' },
  { termino: 'NOM-154-SCFI', href: `${P}/extintores-y-extincion`, titulo: 'Extintores y equipos de extinción' },
  // Señalética
  { termino: 'señalización de emergencia', href: `${P}/senaletica-y-seguridad`, titulo: 'Señalética y seguridad' },
  { termino: 'ruta de evacuación', href: `${P}/senaletica-y-seguridad`, titulo: 'Señalética y seguridad' },
  { termino: 'NOM-003-SEGOB', href: `${P}/senaletica-y-seguridad`, titulo: 'Señalética y seguridad' },

  // ── Cumplimiento. Van al final a propósito: son el destino menos específico de la lista y
  // no deben ganarle a una regla de catálogo cuando ambas coinciden en el mismo párrafo.
  // Sin ellas la sección /cumplimiento no recibía un solo enlace del blog, que son 117 páginas.
  // Los términos son de vocabulario legal, no comercial: no se solapan con el catálogo.
  { termino: 'NOM-002-STPS-2010', href: `${C}/normas/nom-002-stps-2010`, titulo: 'NOM-002-STPS-2010: qué obliga y con qué numeral' },
  { termino: 'NOM-002-STPS', href: `${C}/normas/nom-002-stps-2010`, titulo: 'NOM-002-STPS-2010: qué obliga y con qué numeral' },
  { termino: 'clasificación de riesgo de incendio', href: `${C}/normas/nom-002-stps-2010#clasificacion`, titulo: 'Riesgo ordinario o alto: la Tabla A.1 de la NOM-002' },
  { termino: 'riesgo de incendio alto', href: `${C}/normas/nom-002-stps-2010#clasificacion`, titulo: 'Riesgo ordinario o alto: la Tabla A.1 de la NOM-002' },
  { termino: 'Programa Interno de Protección Civil', href: `${C}#estados`, titulo: 'Quién autoriza el Programa Interno en cada estado' },
  { termino: 'programa interno de protección civil', href: `${C}#estados`, titulo: 'Quién autoriza el Programa Interno en cada estado' },
  { termino: 'protección civil', href: `${C}#estados`, titulo: 'Normativa de protección civil por entidad federativa' },
  { termino: 'brigada contra incendio', href: `${C}/normas/nom-002-stps-2010#brigadas`, titulo: 'Cuándo la NOM-002 obliga a constituir brigada' },
  { termino: 'brigadas contra incendio', href: `${C}/normas/nom-002-stps-2010#brigadas`, titulo: 'Cuándo la NOM-002 obliga a constituir brigada' },
  { termino: 'simulacros de evacuación', href: `${C}#calendario`, titulo: 'Calendario de cumplimiento: qué se vence y cada cuánto' },
  { termino: 'cocina comercial', href: `${C}/giro/restaurante`, titulo: 'Protección contra incendios en restaurantes y cocinas comerciales' },
  { termino: 'brigada industrial', href: `${C}/giro/industria`, titulo: 'Protección contra incendios en industria y parques industriales' },
];

/** Nodos cuyo interior no se toca. */
const PROHIBIDOS = new Set(['a', 'code', 'pre', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote']);

const escapar = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** Límite de palabra tolerante con acentos: \b de JS no los maneja. */
const construirRegex = (t) =>
  new RegExp(`(^|[^\\p{L}\\p{N}_-])(${escapar(t)})(?![\\p{L}\\p{N}_-])`, 'iu');

export default function rehypeInterlink(opciones = {}) {
  const reglas = opciones.reglas ?? REGLAS_CATALOGO;

  return function transformador(tree, file) {
    // La página en la que estamos: para no enlazarla a sí misma
    const rutaArchivo = String(file?.history?.[0] ?? file?.path ?? '');
    const propio = rutaArchivo.split('/').pop()?.replace(/\.mdx?$/, '') ?? '';

    // Tope proporcional al largo real del artículo. Se cuenta antes de tocar el árbol.
    let palabras = 0;
    const contar = (n) => {
      if (n.type === 'text') palabras += n.value.split(/\s+/).filter(Boolean).length;
      (n.children ?? []).forEach(contar);
    };
    contar(tree);
    const max = opciones.max ?? topePorLargo(palabras);

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

      // descartar solapes y destinos repetidos dentro del mismo nodo de texto: el filtro
      // `usados` solo ve lo ya insertado en nodos anteriores, así que dos reglas con el mismo
      // href podían enlazar dos veces al mismo destino en un párrafo.
      const firmes = [];
      const enEsteNodo = new Set();
      let corte = -1;
      for (const c of cands) {
        if (c.inicio < corte || enEsteNodo.has(c.href)) continue;
        firmes.push(c);
        enEsteNodo.add(c.href);
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
