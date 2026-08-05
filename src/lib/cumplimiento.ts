/**
 * Datos de la sección /cumplimiento — directorio normativo para empresas.
 *
 * REGLA DE ORO DE ESTE ARCHIVO: aquí solo entra lo verificado contra fuente
 * oficial (DOF, SIDOF, PLATIICA, ASINOM, Cámara de Diputados, INEGI).
 * La investigación completa vive en docs/investigacion-cumplimiento/.
 * Nada marcado "POR VERIFICAR" en esa investigación debe llegar a este archivo.
 */

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

export interface Giro {
  slug: string;
  nombre: string;
  icono: string;
  gancho: string;
  listo: boolean;
}

export const GIROS: Giro[] = [
  { slug: 'restaurante', nombre: 'Restaurante y cocina comercial', icono: '🍳', gancho: 'Extintor Clase K y supresión en campana', listo: false },
  { slug: 'hotel', nombre: 'Hotel y hospedaje', icono: '🏨', gancho: 'Rutas de evacuación y detección por habitación', listo: false },
  { slug: 'industria', nombre: 'Industria y manufactura', icono: '🏭', gancho: 'Riesgo alto casi siempre: brigada y sistemas fijos', listo: false },
  { slug: 'almacen', nombre: 'Almacén y centro de distribución', icono: '📦', gancho: 'Altura de estiba, racks y carga combustible', listo: false },
  { slug: 'hospital', nombre: 'Hospital y clínica', icono: '🏥', gancho: 'Evacuación de personas no ambulatorias', listo: false },
  { slug: 'escuela', nombre: 'Escuela y guardería', icono: '🎓', gancho: 'Simulacros y programa interno reforzado', listo: false },
  { slug: 'centro-comercial', nombre: 'Centro comercial y cine', icono: '🛍️', gancho: 'Afluencia masiva y salidas por aforo', listo: false },
  { slug: 'oficina', nombre: 'Oficina corporativa', icono: '🏢', gancho: '60 kg de sólidos combustibles por trabajador', listo: false },
];

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
