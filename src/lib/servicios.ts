/**
 * Servicios de FIREFIGHTER.COM.MX que se promueven desde el blog.
 * Solo afirmaciones que ya se sostienen en el catalogo del sitio:
 * distribucion autorizada, documentacion para licitaciones, mantenimiento
 * en banco, capacitacion e instalacion, cobertura en los 32 estados.
 */

export interface Servicio {
  slug: string;
  nombre: string;
  eyebrow: string;
  promesa: string;
  copy: string;
  entregables: string[];
  paraQuien: string;
  cta: string;
  ctaTexto: string;
  /** Temas del blog donde este servicio es el mas relevante. */
  temas: string[];
}

export const SERVICIOS: Servicio[] = [
  {
    slug: 'especificacion',
    nombre: 'Asesoría y especificación técnica',
    eyebrow: 'Antes de comprar',
    promesa: 'Te ayudamos a escribir la especificación correcta antes de que salga la requisición.',
    copy: 'La mayoría de las compras que salen mal no fallan en la entrega: fallan en el papel, cuando se pidió un equipo que no correspondía al riesgo real. Revisamos tu operación contigo —qué tipo de intervención, qué ambiente, cuánta gente— y te devolvemos la especificación redactada, con la norma que aplica y los criterios con los que deberías evaluar a cualquier proveedor, incluidos nosotros.',
    entregables: [
      'Memoria de especificación con norma aplicable',
      'Alcance y cantidades dimensionadas por riesgo',
      'Criterios de evaluación para comparar propuestas',
      'Segunda opinión si ya tienes una propuesta sobre la mesa',
    ],
    paraQuien: 'Jefes de brigada, compras industriales, protección civil municipal',
    cta: '/contacto',
    ctaTexto: 'Platicar mi caso',
    temas: ['epp-bomberos', 'respiracion-scba', 'equipo-forestal', 'herramientas-rescate'],
  },
  {
    slug: 'licitaciones',
    nombre: 'Licitaciones y compra pública',
    eyebrow: 'Papeleo que sí pasa',
    promesa: 'Armamos el paquete documental que piden CompraNet y las convocatorias estatales.',
    copy: 'Una propuesta se descalifica por un anexo faltante, no por el precio. Preparamos el expediente completo —carta de distribuidor autorizado del fabricante, certificados de laboratorio acreditado, fichas técnicas y factura desglosada por partida— y lo ajustamos al formato de la convocatoria. Si la convocatoria pide clave CABMS o partida específica, la incluimos.',
    entregables: [
      'Carta de distribuidor autorizado del fabricante',
      'Certificados de laboratorio y fichas técnicas',
      'Propuesta desglosada por partida, con clave CABMS',
      'Acompañamiento durante juntas de aclaraciones',
    ],
    paraQuien: 'Áreas de adquisiciones de gobierno, hospitales, universidades y paraestatales',
    cta: 'mailto:licitaciones@firefighter.com.mx',
    ctaTexto: 'Escribir a licitaciones',
    temas: ['normativa-y-brigadas'],
  },
  {
    slug: 'mantenimiento',
    nombre: 'Mantenimiento, recarga y pruebas',
    eyebrow: 'Después de la entrega',
    promesa: 'El equipo comprado sin programa de mantenimiento deja de ser equipo certificado.',
    copy: 'Un extintor sin recarga vigente, un cilindro sin prueba hidrostática o un SCBA sin revisión en banco son hallazgos de auditoría, no detalles menores. Damos el servicio recurrente y —lo que más te sirve el día de la inspección— la bitácora que lo documenta, en el formato que revisan STPS y protección civil.',
    entregables: [
      'Recarga de extintores y prueba hidrostática',
      'Mantenimiento de SCBA probado en banco',
      'Inspección de EPP estructural bajo NFPA 1851',
      'Revisión anual de sistemas fijos y detección',
    ],
    paraQuien: 'Plantas industriales, hoteles, hospitales y cuerpos de bomberos con equipo en servicio',
    cta: '/contacto',
    ctaTexto: 'Programar mantenimiento',
    temas: ['extintores', 'sistemas-contra-incendio', 'deteccion-alarma'],
  },
  {
    slug: 'capacitacion',
    nombre: 'Capacitación e instalación',
    eyebrow: 'Que el equipo se use bien',
    promesa: 'Entregamos en sitio, capacitamos a quien lo va a usar y dejamos el sistema operando.',
    copy: 'Hemos visto equipo bueno guardado en su caja porque nadie explicó cómo se ajusta. Por eso la entrega incluye capacitación de uso y pruebas de ajuste facial cuando aplica, y en sistemas fijos y de detección hacemos la instalación y la puesta en marcha con las pruebas que exige la norma.',
    entregables: [
      'Capacitación de uso al personal que opera el equipo',
      'Pruebas de ajuste facial para protección respiratoria',
      'Instalación de sistemas fijos y de detección',
      'Puesta en marcha con pruebas documentadas',
    ],
    paraQuien: 'Brigadas industriales, cuerpos de bomberos y responsables de protección civil interna',
    cta: '/contacto',
    ctaTexto: 'Agendar capacitación',
    temas: ['deteccion-alarma', 'sistemas-contra-incendio', 'respiracion-scba'],
  },
];

export function servicioDeTema(temaSlug: string): Servicio {
  return SERVICIOS.find((s) => s.temas.includes(temaSlug)) ?? SERVICIOS[0];
}
