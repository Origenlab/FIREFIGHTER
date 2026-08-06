/**
 * ═══════════════════════════════════════════════════════════════════════════
 * MARCA — Fuente única de verdad de la identidad de FIREFIGHTER.COM.MX
 * ═══════════════════════════════════════════════════════════════════════════
 *
 * REGLA: el sitio se llama FIREFIGHTER.COM.MX. Escrito así, en mayúsculas y con
 * el dominio completo, en logo, footer, títulos, meta, JSON-LD y copy. No se usan
 * las variantes «FIREFIGHTER Mexico», «Firefighter Mexico» ni «FirefighterMX»:
 * el dominio ES la marca y es lo que diferencia al sitio de cualquier otro.
 *
 * Todo dato corporativo, comercial o normativo que se repita en más de una
 * página vive aquí. Si un dato cambia, se cambia en este archivo y en ningún
 * otro lugar.
 */

/* ── Identidad ───────────────────────────────────────────────────────────── */

/** Marca comercial. Única forma correcta de escribirla. */
export const MARCA = 'FIREFIGHTER.COM.MX';

/** Partes del wordmark para renderizarlo con dos colores en el logo. */
export const MARCA_PARTES = { nombre: 'FIREFIGHTER', tld: '.COM.MX' } as const;

/** Dominio sin protocolo (para mostrar en texto). */
export const DOMINIO = 'firefighter.com.mx';

/** URL canónica del sitio, sin barra final. */
export const SITE = 'https://firefighter.com.mx';

/** Descriptor corto bajo el logo y en el header. */
export const TAGLINE = 'Equipo contra incendios y para bomberos';

/** Descriptor largo, para meta description del home y schema Organization. */
export const DESCRIPTOR =
  'Distribuidor de equipo contra incendios y equipo de protección para bomberos en México: ' +
  'EPP estructural, equipos de respiración autónoma, extintores, sistemas fijos, detección y ' +
  'alarma, herramientas de rescate y equipo forestal, bajo normas NFPA, NOM y UL, con ' +
  'documentación completa para licitaciones públicas y auditorías de protección civil.';

/** Giro declarado, en una línea. Se usa en /acerca-de, footer y legales. */
export const GIRO =
  'Venta, distribución, capacitación y mantenimiento de equipo contra incendios y equipo ' +
  'de protección personal para bomberos y brigadas.';

/* ── Contacto ────────────────────────────────────────────────────────────── */

export const CONTACTO = {
  telefonoVentas: '55 5555 5555',
  telefonoVentasHref: 'tel:5555555555',
  whatsapp: '525500000000',
  whatsappBase: 'https://wa.me/525500000000',
  emailGeneral: 'contacto@firefighter.com.mx',
  emailVentas: 'ventas@firefighter.com.mx',
  emailLicitaciones: 'licitaciones@firefighter.com.mx',
  emailSoporte: 'soporte@firefighter.com.mx',
  horarioComercial: 'Lunes a viernes de 9:00 a 18:00 h · Sábados de 9:00 a 14:00 h (hora del centro de México)',
  horarioComercialCorto: 'Lun–Vie 9:00–18:00 · Sáb 9:00–14:00',
  horarioSchema: [
    { dias: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], abre: '09:00', cierra: '18:00' },
    { dias: ['Saturday'], abre: '09:00', cierra: '14:00' },
  ],
  paisOperacion: 'México',
  emergencias: '911',
} as const;

/** Construye un enlace de WhatsApp con mensaje prellenado. */
export function wa(mensaje: string): string {
  return `${CONTACTO.whatsappBase}?text=${encodeURIComponent(mensaje)}`;
}

/* ── Perfil corporativo ──────────────────────────────────────────────────── */

export const EMPRESA = {
  nombreComercial: MARCA,
  giro: GIRO,
  cobertura: 'Cobertura de venta y entrega en los 32 estados de la República Mexicana',
  coberturaCorta: 'Los 32 estados de México',
  tipoDeCliente: [
    'Cuerpos de bomberos municipales, estatales y voluntarios',
    'Brigadas industriales y de emergencia',
    'Unidades de protección civil',
    'Industria, manufactura y parques industriales',
    'Hospitales, hoteles, escuelas y centros comerciales',
    'Dependencias de gobierno y licitaciones públicas',
  ],
  idiomaAtencion: 'Español',
  monedaOperacion: 'MXN',
} as const;

/** Marcas que se distribuyen. Fuente única: se usa en footer, home y /acerca-de. */
export const MARCAS_DISTRIBUIDAS = [
  'MSA Safety',
  'Scott Safety',
  'Bullard',
  'Holmatro',
  'Amerex',
  'Notifier',
  'Haix',
] as const;

/* ── Marco normativo ─────────────────────────────────────────────────────── */

export interface Norma {
  clave: string;
  nombre: string;
  aplica: string;
  href?: string;
}

/** Normas de referencia del catálogo. Se muestran en footer y fichas técnicas. */
export const NORMAS: Norma[] = [
  { clave: 'NFPA 1970', nombre: 'EPP estructural para bomberos', aplica: 'Trajes, cascos, botas, guantes y capuchas' },
  { clave: 'NFPA 1981', nombre: 'Equipos de respiración autónoma', aplica: 'SCBA de circuito abierto' },
  { clave: 'NFPA 1977', nombre: 'EPP para incendios forestales', aplica: 'Overoles, cascos y equipo de brigada forestal' },
  { clave: 'NFPA 13', nombre: 'Sistemas de rociadores automáticos', aplica: 'Diseño e instalación de sprinklers' },
  { clave: 'NFPA 72', nombre: 'Código nacional de alarmas de incendio', aplica: 'Detección, alarma y notificación' },
  { clave: 'NFPA 20', nombre: 'Bombas estacionarias contra incendio', aplica: 'Sistemas de bombeo' },
  { clave: 'NFPA 2001', nombre: 'Sistemas de agente limpio', aplica: 'Supresión en salas de servidores y equipo crítico' },
  { clave: 'NOM-002-STPS-2010', nombre: 'Prevención y protección contra incendios en centros de trabajo', aplica: 'Brigadas industriales y equipo obligatorio', href: '/cumplimiento/normas/nom-002-stps-2010' },
  { clave: 'NOM-154-SCFI-2005', nombre: 'Extintores contra incendio', aplica: 'Servicio, mantenimiento y recarga' },
  { clave: 'UL Listed', nombre: 'Underwriters Laboratories', aplica: 'Producto certificado por laboratorio tercero' },
  { clave: 'FM Approvals', nombre: 'Factory Mutual', aplica: 'Componentes de sistemas fijos' },
];

/* ── Condiciones comerciales ─────────────────────────────────────────────── */

export interface Condicion {
  titulo: string;
  detalle: string;
}

/**
 * Condiciones comerciales publicadas. Son las mismas que se citan en cotización,
 * /contacto, /acerca-de y las fichas de producto: si cambian, se cambian aquí.
 */
export const CONDICIONES: Condicion[] = [
  {
    titulo: 'Respuesta a cotización',
    detalle: 'Propuesta técnica y económica en un máximo de 24 horas hábiles desde la recepción del requerimiento completo.',
  },
  {
    titulo: 'Vigencia de la cotización',
    detalle: '15 días naturales. Los precios de equipo de importación se confirman contra tipo de cambio del día de la orden.',
  },
  {
    titulo: 'Tiempo de entrega',
    detalle: 'Producto en existencia: de 3 a 5 días hábiles. Equipo sobre pedido o de importación: de 4 a 8 semanas, confirmado por escrito en la propuesta.',
  },
  {
    titulo: 'Cobertura de entrega',
    detalle: 'Los 32 estados de la República Mexicana. Entrega en sitio, en estación o en almacén del cliente según se especifique.',
  },
  {
    titulo: 'Garantía',
    detalle: 'Garantía directa del fabricante, entre 12 y 60 meses según línea de producto. La póliza y el número de serie se entregan con el equipo.',
  },
  {
    titulo: 'Formas de pago',
    detalle: 'Transferencia electrónica y depósito. Crédito sujeto a aprobación para dependencias de gobierno y clientes recurrentes.',
  },
  {
    titulo: 'Facturación',
    detalle: 'Factura CFDI 4.0 desglosada por partida, con descripción, marca, modelo y número de parte de cada concepto.',
  },
  {
    titulo: 'Capacitación',
    detalle: 'Capacitación de uso incluida en la entrega y prueba de ajuste facial cuando la línea de producto lo requiere.',
  },
];

/* ── Documentación para licitación y auditoría ───────────────────────────── */

export const DOCUMENTACION = [
  'Carta de distribuidor autorizado emitida por el fabricante',
  'Ficha técnica en español de cada partida',
  'Certificado de laboratorio tercero (UL, FM, SEI o equivalente)',
  'Certificado de origen y número de serie trazable',
  'Clave CABMS y partida presupuestal cuando la convocatoria lo pide',
  'Manual de operación y de mantenimiento del fabricante',
  'Póliza de garantía a nombre de la dependencia o empresa compradora',
  'Constancia de capacitación al personal usuario',
] as const;

/* ── Servicios ───────────────────────────────────────────────────────────── */

export const SERVICIOS_CLAVE = [
  { titulo: 'Venta y distribución', detalle: 'Equipo nuevo de marcas autorizadas, con documentación completa por partida.' },
  { titulo: 'Asesoría técnica', detalle: 'Dimensionamiento del equipo por tipo de riesgo, norma aplicable y tamaño de brigada.' },
  { titulo: 'Mantenimiento y recarga', detalle: 'Servicio a extintores, pruebas hidrostáticas, mantenimiento de SCBA en banco y bitácora de inspección.' },
  { titulo: 'Capacitación', detalle: 'Uso de equipo, integración de brigada y prueba de ajuste facial para protección respiratoria.' },
] as const;

/* ── Avisos obligatorios ─────────────────────────────────────────────────── */

export const AVISO_NO_EMERGENCIAS =
  `${MARCA} es una empresa de equipamiento contra incendios, no una autoridad ni una línea de auxilio. ` +
  `Si hay una emergencia en curso marca ${CONTACTO.emergencias} desde cualquier teléfono: la llamada es gratuita y atiende las 24 horas.`;

export const AVISO_DIRECTORIO =
  `El directorio nacional de estaciones de bomberos que publica ${MARCA} se integra con información de ` +
  'fuentes públicas y aportaciones de la comunidad. Es un servicio gratuito de consulta y no sustituye ' +
  `la comunicación directa con la autoridad ni la llamada al ${CONTACTO.emergencias}.`;

export const AVISO_PRECIOS =
  'Los precios y tiempos de entrega publicados o cotizados están expresados en pesos mexicanos, no incluyen ' +
  'IVA salvo que se indique, y se confirman por escrito en la propuesta formal.';
