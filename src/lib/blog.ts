/**
 * Taxonomia y utilidades del blog FIREFIGHTER.
 *
 * Los "temas" son espejo de las categorias del catalogo: cada articulo cae en
 * exactamente un tema y cada tema apunta a su categoria de producto. Eso crea
 * el circuito de trafico interno blog -> catalogo -> cotizacion.
 */

export interface Tema {
  slug: string;
  nombre: string;
  corto: string;
  eyebrow: string;
  badge: string;
  descripcion: string;
  intro: string;
  productoSlug: string | null;
  productoNombre: string | null;
  /** Palabras clave para clasificar automaticamente un post nuevo. */
  keywords: string[];
}

export const TEMAS: Tema[] = [
  {
    slug: 'epp-bomberos',
    nombre: 'EPP para Bomberos',
    corto: 'EPP',
    eyebrow: 'Protección personal estructural',
    badge: 'NFPA 1970',
    descripcion: 'Trajes estructurales, cascos, botas, guantes y capuchas: selección, tallaje, precio y mantenimiento bajo NFPA 1970/1971.',
    intro: 'El traje es la compra más cara por bombero y la que más se decide por costumbre. Aquí desarmamos esa decisión: qué significan TPP y THL cuando los ves en una ficha, por qué dos trajes con la misma norma no protegen igual, cuánto cuesta realmente por año de vida útil y qué revisar antes de firmar la recepción.',
    productoSlug: 'epp-para-bomberos',
    productoNombre: 'EPP para Bomberos',
    keywords: ['traje', 'casco', 'bota', 'guante', 'capucha', 'epp', 'nfpa-1971', 'nfpa 1971', 'nfpa-1970', 'nfpa 1970', 'nomex', 'nfpa-1851', 'nfpa 1850', 'tallaje', 'pbi'],
  },
  {
    slug: 'respiracion-scba',
    nombre: 'Respiración Autónoma y SCBA',
    corto: 'SCBA',
    eyebrow: 'Protección respiratoria',
    badge: 'NFPA 1981',
    descripcion: 'Equipos SCBA, máscaras, cilindros, líneas de aire y espacios confinados: comparativas técnicas y programas de mantenimiento.',
    intro: 'El SCBA es el equipo más complejo que carga un bombero y el que más se compra sin plan de mantenimiento. En este tema comparamos plataformas sin casarnos con ninguna, explicamos qué cilindro conviene según el tipo de intervención y qué te van a pedir en la próxima auditoría si tu bitácora no está al día.',
    productoSlug: 'equipos-de-respiracion',
    productoNombre: 'Equipos de Respiración',
    keywords: ['scba', 'respiracion', 'airpak', 'msa-g1', 'cilindros', 'mascaras', 'espacios-confinados', 'espacios confinados', 'suministro-aire', 'suministro aire', 'pass-devices', 'pass device', 'nfpa-1981', 'nfpa 1981'],
  },
  {
    slug: 'herramientas-rescate',
    nombre: 'Herramientas de Rescate',
    corto: 'Rescate',
    eyebrow: 'Extricación y rescate',
    badge: 'NFPA 1936',
    descripcion: 'Equipo hidráulico de excarcelación, generadores, iluminación de escena y equipamiento de unidades de rescate vehicular y urbano.',
    intro: 'Los autos cambiaron más rápido que las herramientas de muchas unidades: el acero UHSS de un vehículo de 2020 no cede con una tijera de hace quince años. Aquí está lo que hay que saber para actualizar el equipo sin comprar de más, y cómo armar una unidad de rescate completa por etapas cuando el presupuesto llega en partes.',
    productoSlug: 'herramientas-de-rescate',
    productoNombre: 'Herramientas de Rescate',
    keywords: ['rescate vehicular', 'rescate-vehicular', 'holmatro', 'tijeras', 'expansores', 'rams-', 'excarcelacion', 'nfpa-1936', 'nfpa 1936', 'combi-tool', 'iluminacion-led', 'unidad-rescate', 'generadores-hidraulicos', 'herramientas-rescate', 'herramientas de rescate', 'nfpa-1006'],
  },
  {
    slug: 'extintores',
    nombre: 'Extintores y Extinción Portátil',
    corto: 'Extintores',
    eyebrow: 'Extinción portátil',
    badge: 'NOM-154',
    descripcion: 'PQS, CO2, Clase K, espuma e industriales: selección por clase de fuego, cálculo de cantidad, recarga y NOM-154-SCFI.',
    intro: 'Casi nadie tiene los extintores mal por descuido: los tiene mal porque alguien compró por precio sin ver el tipo de riesgo. Este tema resuelve las preguntas que nos hacen cada semana: cuántos necesito para mi superficie, cuál va en la cocina, por qué el manómetro en verde no garantiza nada y qué exige la NOM-154 en cada recarga.',
    productoSlug: 'extintores-y-extincion',
    productoNombre: 'Extintores y Extinción',
    keywords: ['extintor', 'pqs', 'clase-k', 'clase k', 'nom-154', 'nom 154', 'recarga', 'clases de fuego', 'nfpa-10', 'nfpa 10'],
  },
  {
    slug: 'sistemas-contra-incendio',
    nombre: 'Sistemas Contra Incendio',
    corto: 'Sistemas fijos',
    eyebrow: 'Proyectos e instalación',
    badge: 'NFPA 13',
    descripcion: 'Rociadores, bombas NFPA 20, gabinetes, mangueras, válvulas, espuma AFFF y agentes limpios para sistemas fijos.',
    intro: 'Un sistema fijo se juzga el día que opera, pero se define años antes en el cálculo hidráulico y en las pruebas que nadie quiso documentar. Aquí escribimos para el que va a especificar, instalar o recibir un sistema: qué revisar en el diseño, qué exige la revisión anual y cuándo conviene un agente limpio en lugar de agua.',
    productoSlug: 'sistemas-contra-incendio',
    productoNombre: 'Sistemas Contra Incendio',
    keywords: ['sprinkler', 'nfpa-13', 'nfpa 13', 'nfpa-20', 'nfpa 20', 'bomba', 'espuma', 'fm200', 'fm-200', 'agentes limpios', 'agentes-limpios', 'supresion', 'nfpa-2001', 'nfpa 2001', 'novec', 'gabinete', 'manguera', 'lanza', 'valvula', 'storz', 'hidrostatica', 'nfpa-25', 'nfpa 25', 'nfpa-14', 'hangares', 'sala de servidores', 'salas-servidores', 'datacentro', 'revision-anual-sistemas', 'diseno-sistemas', 'distribucion-gabinetes', 'acoples'],
  },
  {
    slug: 'deteccion-alarma',
    nombre: 'Detección y Alarma',
    corto: 'Detección',
    eyebrow: 'Detección temprana',
    badge: 'NFPA 72',
    descripcion: 'Paneles direccionables, detectores de humo y calor, estaciones manuales, sirenas y estrobos bajo NFPA 72: diseño, audibilidad y mantenimiento.',
    intro: 'Una alarma que no detecta a tiempo cuesta lo mismo que una que sí. La diferencia está en la selección del detector para cada ambiente, en cómo se programó el lazo y en si alguien está haciendo las pruebas periódicas. De eso trata este tema, con ejemplos de instalaciones reales en hospitales, industria y hotelería.',
    productoSlug: 'deteccion-y-alarma',
    productoNombre: 'Detección y Alarma',
    keywords: ['detector', 'deteccion', 'alarma', 'notifier', 'nfs2', 'sirena', 'estrobo', 'estacion-manual', 'estaciones-manuales', 'modulos-monitor', 'nfpa-72', 'nfpa 72', 'slc', 'vesda', 'sd355', 'bg12lx'],
  },
  {
    slug: 'equipo-forestal',
    nombre: 'Incendios Forestales',
    corto: 'Forestal',
    eyebrow: 'Combate en zonas naturales',
    badge: 'NFPA 1977',
    descripcion: 'Brigadas forestales: herramienta manual, mochilas aspersoras, EPP FR y planificación de temporada con criterio CONAFOR.',
    intro: 'La brigada forestal casi siempre trabaja con menos presupuesto y más horas de las que debería. Por eso aquí priorizamos: qué comprar primero para una brigada de diez, qué herramienta aguanta la temporada completa y qué EPP no se puede sustituir por ropa de trabajo aunque el proveedor diga que sí.',
    productoSlug: 'equipo-forestal',
    productoNombre: 'Equipo Forestal',
    keywords: ['forestal', 'conafor', 'pulaski', 'mcleod', 'aspersora', 'nfpa-1977', 'nfpa 1977', 'overall-fr'],
  },
  {
    slug: 'normativa-y-brigadas',
    nombre: 'Normativa y Brigadas',
    corto: 'Normativa',
    eyebrow: 'Cumplimiento y licitaciones',
    badge: 'NOM-002-STPS',
    descripcion: 'NOM-002-STPS, protección civil, licitaciones públicas y cómo equipar una brigada industrial desde cero, con documentación completa.',
    intro: 'La parte que no es técnica pero tumba proyectos: la inspección de la STPS, el programa interno de protección civil y las convocatorias públicas. Publicamos lo que hemos visto funcionar —y lo que hemos visto descalificarse por un anexo— para que llegues preparado a la junta de aclaraciones.',
    productoSlug: null,
    productoNombre: null,
    keywords: [],
  },
];

export const TEMA_FALLBACK = 'normativa-y-brigadas';

function normalizar(texto: string): string {
  return texto
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase();
}

/** Clasifica un post en un tema unico. El orden de TEMAS define la prioridad. */
export function temaDePost(slug: string, title: string, tags: string[] = []): string {
  const heno = normalizar(`${slug} ${title} ${tags.join(' ')}`);
  const orden = ['equipo-forestal', 'respiracion-scba', 'herramientas-rescate', 'extintores', 'sistemas-contra-incendio', 'deteccion-alarma', 'epp-bomberos'];
  for (const slugTema of orden) {
    const tema = TEMAS.find(t => t.slug === slugTema);
    if (tema && tema.keywords.some(k => heno.includes(k))) return tema.slug;
  }
  return TEMA_FALLBACK;
}

export function getTema(slug: string): Tema {
  return TEMAS.find(t => t.slug === slug) ?? TEMAS[TEMAS.length - 1];
}

/** Minutos de lectura estimados (200 palabras/min, minimo 1). */
export function tiempoLectura(body: string = ''): number {
  const palabras = body.trim().split(/\s+/).length;
  return Math.max(1, Math.round(palabras / 200));
}

export function formatFecha(fecha: Date | string): string {
  return new Date(fecha).toLocaleDateString('es-MX', { year: 'numeric', month: 'long', day: 'numeric' });
}

export function formatFechaCorta(fecha: Date | string): string {
  return new Date(fecha).toLocaleDateString('es-MX', { year: 'numeric', month: 'short', day: 'numeric' });
}

export const WA_BASE = 'https://wa.me/525500000000';

export function waLink(texto: string): string {
  return `${WA_BASE}?text=${encodeURIComponent(`Hola, ${texto}`)}`;
}
