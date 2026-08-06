/**
 * Datos de la sección /cumplimiento — directorio normativo para empresas.
 *
 * REGLA DE ORO DE ESTE ARCHIVO: aquí solo entra lo verificado contra fuente
 * oficial (DOF, SIDOF, PLATIICA, ASINOM, Cámara de Diputados, INEGI).
 * La investigación completa vive en docs/investigacion-cumplimiento/.
 * Nada marcado "POR VERIFICAR" en esa investigación debe llegar a este archivo.
 */

import estadosData from '../data/cumplimiento-estados.json';
import statesGeo from '../data/states.json';
import girosData from '../data/cumplimiento-giros.json';

/** Fecha de última revisión normativa de la sección. Se muestra en cada página. */
export const REVISADO = '5 de agosto de 2026';

/** UMA vigente. INEGI, comunicado 1/26. Vigente desde el 1 de febrero de 2026. */
export const UMA = {
  diaria: 117.31,
  fuente: 'INEGI, comunicado de prensa 1/26',
  vigenciaDesde: '1 de febrero de 2026',
};

export const pesos = (umas: number) =>
  (umas * UMA.diaria).toLocaleString('es-MX', {
    style: 'currency',
    currency: 'MXN',
    maximumFractionDigits: 0,
  });

export interface Norma {
  slug: string;
  clave: string;
  nombre: string;
  corto: string;
  emisor: string;
  dof: string;
  estado: 'Vigente' | 'Vigente con abrogación anunciada';
  aplica: string;
  resumen: string;
  productoSlug?: string;
  listo: boolean;
}

/** Normas del directorio. `listo:false` = todavía no tiene ficha propia. */
export const NORMAS: Norma[] = [
  {
    slug: 'nom-002-stps-2010',
    clave: 'NOM-002-STPS-2010',
    nombre: 'Condiciones de seguridad — Prevención y protección contra incendios en los centros de trabajo',
    corto: 'Prevención y protección contra incendios',
    emisor: 'STPS',
    dof: '9 de diciembre de 2010',
    estado: 'Vigente',
    aplica: 'Todo centro de trabajo en México, sin importar giro ni tamaño',
    resumen:
      'La norma madre. Define si tu centro de trabajo es de riesgo ordinario o alto, y de esa clasificación cuelga todo lo demás: cuántos extintores, si necesitas brigada, cuántos simulacros al año y si te exigen sistemas fijos.',
    productoSlug: 'extintores-y-extincion',
    listo: true,
  },
  {
    slug: 'nom-017-stps-2024',
    clave: 'NOM-017-STPS-2024',
    nombre: 'Equipo de protección personal — Selección, uso y manejo en los centros de trabajo',
    corto: 'Equipo de protección personal',
    emisor: 'STPS',
    dof: '28 de marzo de 2025 · vigente desde el 28 de septiembre de 2025',
    estado: 'Vigente',
    aplica: 'Todo centro de trabajo donde se requiera EPP',
    resumen:
      'Sustituyó a la NOM-017-STPS-2008. Buena parte del material técnico que circula en México sigue citando la versión de 2008: es el error de cumplimiento más común del sector hoy.',
    productoSlug: 'epp-para-bomberos',
    listo: false,
  },
  {
    slug: 'nom-154-scfi-2005',
    clave: 'NOM-154-SCFI-2005',
    nombre: 'Extintores — Servicio de mantenimiento y recarga',
    corto: 'Mantenimiento y recarga de extintores',
    emisor: 'Secretaría de Economía',
    dof: '26 de diciembre de 2005 · modificación DOF 12 de julio de 2010',
    estado: 'Vigente',
    aplica: 'Prestadores del servicio de mantenimiento y recarga, y a quien los contrata',
    resumen:
      'Define qué debe cumplir quien le da servicio a tus extintores: etiqueta, collarín, orden de servicio foliada y prueba hidrostática al menos cada 5 años. Su revisión sistemática del 6 de octubre de 2025 la confirmó.',
    productoSlug: 'extintores-y-extincion',
    listo: false,
  },
  {
    slug: 'nom-026-stps-2008',
    clave: 'NOM-026-STPS-2008',
    nombre: 'Colores y señales de seguridad e higiene, e identificación de riesgos por fluidos conducidos en tuberías',
    corto: 'Colores y señales de seguridad',
    emisor: 'STPS',
    dof: '25 de noviembre de 2008',
    estado: 'Vigente',
    aplica: 'Todo centro de trabajo',
    resumen:
      'Qué color, qué forma y dónde va cada señal. Se sanciona en el rango alto del reglamento: la señalización no es un detalle estético.',
    listo: false,
  },
  {
    slug: 'nom-029-stps-2011',
    clave: 'NOM-029-STPS-2011',
    nombre: 'Mantenimiento de las instalaciones eléctricas en los centros de trabajo — Condiciones de seguridad',
    corto: 'Mantenimiento de instalaciones eléctricas',
    emisor: 'STPS',
    dof: '29 de diciembre de 2011',
    estado: 'Vigente',
    aplica: 'Centros de trabajo donde se realice mantenimiento eléctrico, propio o contratado',
    resumen:
      'Lo único con periodicidad anual explícita es la prueba de resistencia a tierra y continuidad. La "termografía anual obligatoria" que circula en material comercial no está en esta norma.',
    listo: false,
  },
  {
    slug: 'nfpa-en-mexico',
    clave: 'NFPA en México',
    nombre: '¿Las normas NFPA son obligatorias en México?',
    corto: 'Estatus legal de NFPA',
    emisor: 'National Fire Protection Association (EE. UU.)',
    dof: '—',
    estado: 'Vigente',
    aplica: 'Referencia técnica; obligatoria solo por remisión',
    resumen:
      'NFPA no es ley en México. Se vuelve exigible cuando una NOM la referencia, cuando un reglamento local la adopta, o cuando la aseguradora o el corporativo la ponen en el contrato. Esa distinción decide muchas licitaciones.',
    listo: false,
  },
];

export interface NormaDeGiro {
  clave: string;
  que: string;
  estatus: 'obligatoria' | 'depende' | 'referencia';
}

export interface ErrorDeGiro {
  titulo: string;
  detalle: string;
}

export interface Giro {
  slug: string;
  nombre: string;
  /** Nombre corto para títulos SEO y enlaces cruzados. */
  nombreCorto: string;
  /**
   * DEPRECADO. Emoji heredado de la primera versión de las cards.
   * Las cards de esta sección son tipográficas: NO se renderiza en ninguna
   * plantilla y no debe volver a usarse. Se conserva solo para no romper el JSON.
   */
  icono?: string;
  /** Frase corta que define el riesgo del giro. Se usa como badge. */
  gancho: string;
  resumen: string;
  riesgoTipico: string;
  /** Clasificación típica conforme a la Tabla A.1 de la NOM-002-STPS-2010. */
  riesgoNom: 'alto' | 'ordinario' | 'variable';
  normas: NormaDeGiro[];
  extintores: string[];
  sistemas: string[];
  evacuacion: string[];
  brigadas: string[];
  documentos: string[];
  errores: ErrorDeGiro[];
  /** El matiz que el mercado explica mal. Cadena vacía si no aplica. */
  aclaracion: string;
  productoSlug: string;
}

export const GIROS = girosData as Giro[];

export const getGiro = (slug: string) => GIROS.find(g => g.slug === slug);

export interface Tramite {
  slug: string;
  nombre: string;
  autoridad: string;
  gancho: string;
  listo: boolean;
}

export const TRAMITES: Tramite[] = [
  { slug: 'programa-interno-de-proteccion-civil', nombre: 'Programa Interno de Protección Civil', autoridad: 'Protección Civil estatal o municipal', gancho: 'El documento que más se pide y peor se entiende', listo: false },
  { slug: 'visto-bueno-de-bomberos', nombre: 'Visto bueno del Cuerpo de Bomberos', autoridad: 'Bomberos — casi siempre municipal', gancho: 'Cambia por municipio; en Jalisco es la misma dependencia que PC', listo: false },
  { slug: 'unidad-interna-y-brigadas', nombre: 'Unidad Interna y brigadas', autoridad: 'Interna, con acta y constancias', gancho: 'Acta de integración, capacitación y evidencia', listo: false },
  { slug: 'clasificacion-de-riesgo-de-incendio', nombre: 'Clasificación de riesgo de incendio', autoridad: 'La elabora el patrón', gancho: 'El estudio del que depende todo lo demás', listo: false },
];

export interface FilaCalendario {
  actividad: string;
  frecuencia: string;
  fundamento: string;
  destacada?: boolean;
}

/** Solo frecuencias verificadas contra el texto oficial. */
export const CALENDARIO: FilaCalendario[] = [
  { actividad: 'Revisión visual de extintores', frecuencia: 'Mensual', fundamento: 'NOM-002-STPS-2010 §7.2', destacada: true },
  { actividad: 'Mantenimiento de extintores', frecuencia: 'Al menos una vez al año', fundamento: 'NOM-002-STPS-2010 §7.18', destacada: true },
  { actividad: 'Prueba hidrostática del cilindro del extintor', frecuencia: 'Al menos cada 5 años', fundamento: 'NOM-154-SCFI-2005 §5.6' },
  { actividad: 'Programa de revisión y pruebas a equipos, detección, alarmas y sistemas fijos', frecuencia: 'Anual', fundamento: 'NOM-002-STPS-2010 §7.4' },
  { actividad: 'Programa de revisión a instalaciones eléctricas', frecuencia: 'Anual', fundamento: 'NOM-002-STPS-2010 §7.5' },
  { actividad: 'Prueba de resistencia a tierra y continuidad', frecuencia: 'Al menos una vez al año', fundamento: 'NOM-029-STPS-2011 §9.4' },
  { actividad: 'Simulacro de incendio — riesgo ordinario', frecuencia: '1 vez al año', fundamento: 'NOM-002-STPS-2010 §5.7', destacada: true },
  { actividad: 'Simulacro de incendio — riesgo alto', frecuencia: '2 veces al año', fundamento: 'NOM-002-STPS-2010 §5.7', destacada: true },
  { actividad: 'Programa de capacitación teórico-práctico', frecuencia: 'Anual', fundamento: 'NOM-002-STPS-2010, capítulo 11' },
  { actividad: 'Revisión del EPP por el propio trabajador', frecuencia: 'Antes, durante y al final de cada turno', fundamento: 'NOM-017-STPS' },
  { actividad: 'Conservación de registros de la NOM-002', frecuencia: '3 años', fundamento: 'NOM-002-STPS-2010 §13.6', destacada: true },
  { actividad: 'Nueva clasificación de riesgo de incendio', frecuencia: 'Al modificarse los inventarios máximos del año', fundamento: 'NOM-002-STPS-2010 §A.1.6' },
];

/** Umbrales de la Tabla A.1 del Apéndice A de la NOM-002-STPS-2010. */
export const UMBRALES = [
  { concepto: 'Superficie construida', ordinario: 'Menor de 3 000 m²', alto: 'Igual o mayor de 3 000 m²' },
  { concepto: 'Inventario de gases inflamables', ordinario: 'Menor de 3 000 L', alto: 'Igual o mayor de 3 000 L' },
  { concepto: 'Inventario de líquidos inflamables', ordinario: 'Menor de 1 400 L', alto: 'Igual o mayor de 1 400 L' },
  { concepto: 'Inventario de líquidos combustibles', ordinario: 'Menor de 2 000 L', alto: 'Igual o mayor de 2 000 L' },
  { concepto: 'Inventario de sólidos combustibles, incluido el mobiliario', ordinario: 'Menor de 15 000 kg', alto: 'Igual o mayor de 15 000 kg' },
  { concepto: 'Materiales pirofóricos y explosivos', ordinario: 'No aplica', alto: 'Cualquier cantidad' },
];

export const AVISO_LEGAL =
  'Este contenido es informativo y no constituye asesoría jurídica. La normativa cambia y muchos requisitos varían por estado y municipio: verifica siempre con la autoridad local antes de tomar decisiones.';

/* ════════════════════════════════════════════════════════════════════
   ESTADOS · marco de protección civil por entidad federativa
   Datos verificados contra congresos estatales, periódicos oficiales y
   portales de protección civil. Ver docs/investigacion-cumplimiento/.
   ════════════════════════════════════════════════════════════════════ */


export interface EstadoNormativa {
  estado: string;
  slug: string;
  ley: string;
  leyFecha: string;
  leyUrl: string;
  autoridad: string;
  bomberos: string;
  pipcVigencia: string;
  simulacros: string;
  /** Mínimo anual que fija la norma estatal. 0 = la ley no lo fija. Se captura a mano en el JSON. */
  simulacrosMin: number;
  consultor: string;
  distintivo: string;
  confianza: 'alta' | 'media';
}

export interface EstadoGeo {
  name: string;
  slug: string;
  code: string;
  capital: string;
  region: string;
  totalStations: number;
}

export interface Estado extends EstadoNormativa {
  code: string;
  capital: string;
  region: string;
  totalStations: number;
  /** Ficha indexable. Los de confianza media salen con noindex hasta cerrar su verificación. */
  listo: boolean;
  /** Etiqueta corta del modelo de bomberos, para la card del hub. */
  modeloBomberos: string;
  /** La norma estatal obliga a consultor o tercero acreditado registrado. */
  exigeConsultor: boolean;
  /** Nombre sin acentos ni mayúsculas, para el buscador del hub. */
  busqueda: string;
}

const geo = statesGeo as EstadoGeo[];

/** Resume el campo `bomberos` en una etiqueta de una palabra para las cards. */
function modeloDeBomberos(txt: string): string {
  const t = txt.toLowerCase();
  if (t.startsWith('integrado') || t.includes('misma dependencia') || t.includes('dentro de la coordinación estatal') || t.includes('dirección de bomberos'))
    return 'Integrado con PC';
  if (t.startsWith('estatal')) return 'Estatal';
  if (t.startsWith('no hay cuerpo') || t.includes('patronato')) return 'Patronato';
  if (t.startsWith('coexisten')) return 'Mixto';
  if (t.startsWith('municipal')) return 'Municipal';
  if (t.startsWith('la ley') || t.startsWith('la nueva ley')) return 'Sin definir en ley';
  return 'Municipal';
}

/** Quita acentos y baja a minúsculas, para el buscador. */
const normaliza = (t: string) =>
  t.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();

export const ESTADOS: Estado[] = (estadosData as EstadoNormativa[])
  .map(e => {
    const g = geo.find(x => x.slug === e.slug);
    return {
      ...e,
      code: g?.code ?? '',
      capital: g?.capital ?? '',
      region: g?.region ?? 'centro',
      totalStations: g?.totalStations ?? 0,
      listo: e.confianza === 'alta',
      modeloBomberos: modeloDeBomberos(e.bomberos),
      exigeConsultor: /^s[ií]/i.test(e.consultor.trim()),
      busqueda: normaliza(e.estado),
    };
  })
  .sort((a, b) => a.estado.localeCompare(b.estado, 'es'));

export const getEstado = (slug: string) => ESTADOS.find(e => e.slug === slug);

/** Rutas de estado en borrador: salen con noindex y fuera del sitemap. */
export const ESTADOS_BORRADOR = ESTADOS.filter(e => !e.listo).map(e => `/cumplimiento/estado/${e.slug}`);

export const REGIONES: { key: string; nombre: string }[] = [
  { key: 'centro', nombre: 'Centro' },
  { key: 'centro-occidente', nombre: 'Centro-occidente' },
  { key: 'noroeste', nombre: 'Noroeste' },
  { key: 'norte', nombre: 'Norte' },
  { key: 'noreste', nombre: 'Noreste' },
  { key: 'sur', nombre: 'Sur' },
  { key: 'sureste', nombre: 'Sureste' },
  { key: 'peninsula', nombre: 'Península' },
];

/** Cifras del panorama estatal, calculadas de los datos — nunca a mano. */
export const PANORAMA = {
  total: ESTADOS.length,
  documentados: ESTADOS.filter(e => e.listo).length,
  bomberosMunicipales: ESTADOS.filter(e => e.modeloBomberos === 'Municipal').length,
  consultorObligatorio: ESTADOS.filter(e => e.exigeConsultor).length,
  simulacrosMax: Math.max(...ESTADOS.map(e => e.simulacrosMin)),
};

/* ════════════════════════════════════════════════════════════════════
   CRUCE estado × giro
   Combina las dos obligaciones que corren en paralelo: la federal de la
   NOM-002-STPS-2010, que depende del riesgo del giro, y la estatal de
   protección civil. El número que se publica es el más exigente de los dos,
   porque cumplir el menor deja descubierta a la otra autoridad.
   ════════════════════════════════════════════════════════════════════ */

export interface Cruce {
  /** Simulacros que exige la NOM-002 según el riesgo del giro. */
  simulacrosFed: number;
  /** Simulacros que exige la norma estatal. 0 = no fija mínimo. */
  simulacrosEdo: number;
  /** El mayor de los dos: lo que hay que planear para quedar bien con ambas. */
  simulacrosPlan: number;
  /** Quién manda en la cifra anterior. */
  simulacrosOrigen: 'federal' | 'estatal' | 'ambas';
  /** Superficie máxima por extintor, en m². */
  m2PorExtintor: number;
  /** Distancia máxima de recorrido a un extintor clase A, C o D, en metros. */
  distanciaExtintor: number;
  brigadaObligatoria: boolean;
  sistemasFijos: boolean;
  riesgo: 'alto' | 'ordinario' | 'variable';
}

export function cruce(estado: Estado, giro: Giro): Cruce {
  const alto = giro.riesgoNom === 'alto';
  const simulacrosFed = giro.riesgoNom === 'ordinario' ? 1 : 2;
  const simulacrosEdo = estado.simulacrosMin;
  const simulacrosPlan = Math.max(simulacrosFed, simulacrosEdo);

  const simulacrosOrigen: Cruce['simulacrosOrigen'] =
    simulacrosEdo > simulacrosFed ? 'estatal'
    : simulacrosFed > simulacrosEdo ? 'federal'
    : 'ambas';

  return {
    simulacrosFed,
    simulacrosEdo,
    simulacrosPlan,
    simulacrosOrigen,
    m2PorExtintor: alto ? 200 : 300,
    distanciaExtintor: 23,
    brigadaObligatoria: alto,
    sistemasFijos: alto,
    riesgo: giro.riesgoNom,
  };
}

/** Etiqueta legible del riesgo del giro. */
export const etiquetaRiesgo = (r: Giro['riesgoNom']) =>
  r === 'alto' ? 'Riesgo alto' : r === 'ordinario' ? 'Riesgo ordinario' : 'Riesgo variable';

/** Clave de tres letras del riesgo, para la columna izquierda de los enlaces cruzados. */
export const claveRiesgo = (r: Giro['riesgoNom']) =>
  r === 'alto' ? 'ALT' : r === 'ordinario' ? 'ORD' : 'VAR';

/* ════════════════════════════════════════════════════════════════════
   INTERLINKING · helpers que usan TODAS las plantillas de /cumplimiento
   La sección es una malla de tres ejes —norma, giro y estado— y cada
   página tiene que poder saltar a los otros dos sin callejones sin salida.
   Estos helpers son la única fuente de esos enlaces: si se cambia aquí,
   cambia en las 363 páginas.
   ════════════════════════════════════════════════════════════════════ */

/** Estados con ficha indexable. Los de confianza media salen con noindex. */
export const ESTADOS_LISTOS = ESTADOS.filter(e => e.listo);

/** URL canónica de cada tipo de página de la sección. */
export const rutaEstado = (e: Pick<Estado, 'slug'>) => `/cumplimiento/estado/${e.slug}`;
export const rutaGiro = (g: Pick<Giro, 'slug'>) => `/cumplimiento/giro/${g.slug}`;
export const rutaCruce = (e: Pick<Estado, 'slug'>, g: Pick<Giro, 'slug'>) =>
  `/cumplimiento/estado/${e.slug}/${g.slug}`;

/** Estados agrupados por región, en el orden de REGIONES. Sin regiones vacías. */
export function estadosPorRegion(lista: Estado[] = ESTADOS) {
  return REGIONES
    .map(r => ({ ...r, estados: lista.filter(e => e.region === r.key) }))
    .filter(r => r.estados.length > 0);
}

/** Los demás estados de la misma región. Enlace lateral de la ficha de estado. */
export const vecinosDe = (e: Estado) =>
  ESTADOS.filter(x => x.region === e.region && x.slug !== e.slug);

/** Los demás giros, en el orden del catálogo. Enlace lateral de las fichas de giro. */
export const otrosGiros = (g: Giro) => GIROS.filter(x => x.slug !== g.slug);

/**
 * Giros cuya guía apunta a una categoría del catálogo.
 * Es el puente de /productos hacia /cumplimiento: sin él la sección normativa
 * no recibe enlaces entrantes del catálogo, que es donde está el tráfico.
 */
export const girosDeCategoria = (productoSlug: string) =>
  GIROS.filter(g => g.productoSlug === productoSlug);

/** Índice de dos dígitos para la cabecera tipográfica de las cards. */
export const indice = (i: number) => String(i + 1).padStart(2, '0');
