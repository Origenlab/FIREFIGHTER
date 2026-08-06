/**
 * Utilidades de SEO de FIREFIGHTER.COM.MX
 * Genera el JSON-LD estructurado que consumen los buscadores.
 * El nombre de marca y la URL base salen de src/data/marca.ts.
 */
import { MARCA, NOMBRE_EMPRESA, SITE, DESCRIPTOR, TAGLINE } from '../data/marca';

export interface StationData {
  name: string;
  address?: string;
  neighborhood?: string;
  municipality: string;
  city: string;
  state: string;
  postalCode?: string;
  phone?: string;
  emergencyPhone?: string;
  email?: string;
  website?: string;
  latitude?: number;
  longitude?: number;
  services: string[];
  operatingHours: string;
  description?: string;
}

export interface BreadcrumbItem {
  name: string;
  url: string;
}

/**
 * Generates EmergencyService JSON-LD schema for fire stations
 * @see https://schema.org/EmergencyService
 */
export function generateEmergencyServiceSchema(
  station: StationData,
  pageUrl: string
): object {
  const serviceLabels: Record<string, string> = {
    'combate-incendios': 'Combate de incendios',
    'atencion-medica': 'Atención médica prehospitalaria',
    'rescate-vehicular': 'Rescate vehicular',
    'rescate-acuatico': 'Rescate acuático',
    'rescate-alturas': 'Rescate en alturas',
    'rescate-montaña': 'Rescate en montaña',
    'rescate-forestal': 'Rescate forestal',
    'materiales-peligrosos': 'Materiales peligrosos (HAZMAT)',
    'proteccion-civil': 'Protección civil',
    'explosivos': 'Manejo de explosivos',
  };

  const servicesDescription = station.services
    .map(s => serviceLabels[s] || s)
    .join(', ');

  return {
    '@context': 'https://schema.org',
    '@type': 'EmergencyService',
    '@id': pageUrl,
    name: station.name,
    description: station.description ||
      `${station.name} - Estación de bomberos en ${station.municipality}, ${station.state}. Servicios: ${servicesDescription}. Emergencias: 911.`,
    address: {
      '@type': 'PostalAddress',
      ...(station.address
        ? { streetAddress: [station.address, station.neighborhood].filter(Boolean).join(', ') }
        : {}),
      addressLocality: station.municipality,
      addressRegion: station.state,
      ...(station.postalCode ? { postalCode: station.postalCode } : {}),
      addressCountry: 'MX',
    },
    ...(station.phone ? { telephone: station.phone } : {}),
    url: pageUrl,
    ...(station.latitude != null && station.longitude != null
      ? {
          geo: {
            '@type': 'GeoCoordinates',
            latitude: station.latitude,
            longitude: station.longitude,
          },
        }
      : {}),
    openingHoursSpecification: {
      '@type': 'OpeningHoursSpecification',
      dayOfWeek: [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
      ],
      opens: '00:00',
      closes: '23:59',
    },
    areaServed: {
      '@type': 'City',
      name: `${station.municipality}, ${station.state}`,
    },
    availableLanguage: {
      '@type': 'Language',
      name: 'Spanish',
      alternateName: 'es',
    },
    priceRange: 'Gratuito',
    ...(station.email && { email: station.email }),
    ...(station.website && { sameAs: station.website }),
  };
}

/**
 * Generates BreadcrumbList JSON-LD schema
 * @see https://schema.org/BreadcrumbList
 */
export function generateBreadcrumbSchema(
  items: BreadcrumbItem[],
  baseUrl: string = SITE
): object {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      // El último crumb (página actual) puede venir sin URL: omitir `item`
      // en vez de apuntarlo al home (URL incorrecta en el schema).
      ...(item.url
        ? { item: item.url.startsWith('http') ? item.url : `${baseUrl}${item.url}` }
        : {}),
    })),
  };
}

/**
 * Generates WebSite JSON-LD schema for the homepage
 * @see https://schema.org/WebSite
 */
export function generateWebSiteSchema(baseUrl: string = SITE): object {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    '@id': `${baseUrl}/#website`,
    name: MARCA,
    alternateName: [NOMBRE_EMPRESA, 'firefighter.com.mx'],
    description:
      'Equipo contra incendios y para bomberos en México: EPP, SCBA, extintores, sistemas, detección y rescate certificados NFPA, NOM y UL. Incluye el directorio nacional de estaciones de bomberos.',
    url: baseUrl,
    publisher: { '@id': `${baseUrl}/#organization` },
    inLanguage: 'es-MX',
    potentialAction: {
      '@type': 'SearchAction',
      target: {
        '@type': 'EntryPoint',
        urlTemplate: `${baseUrl}/directorio/?q={search_term_string}`,
      },
      'query-input': 'required name=search_term_string',
    },
  };
}

/**
 * Generates Organization JSON-LD schema
 * @see https://schema.org/Organization
 */
export function generateOrganizationSchema(baseUrl: string = SITE): object {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    '@id': `${baseUrl}/#organization`,
    // La entidad tiene dos nombres válidos: el dominio es la marca visible y
    // «FIREFIGHTER México» es la razón comercial —y la frase que la gente busca—.
    // Declarar las dos es lo que permite que el buscador reconozca a la misma
    // entidad escrita de las dos formas.
    name: MARCA,
    alternateName: [NOMBRE_EMPRESA, 'firefighter.com.mx'],
    url: baseUrl,
    logo: {
      '@type': 'ImageObject',
      url: `${baseUrl}/images/logo-firefighter-mexico.svg`,
      width: 200,
      height: 50,
    },
    slogan: TAGLINE,
    description: DESCRIPTOR,
    areaServed: {
      '@type': 'Country',
      name: 'México',
      identifier: 'MX',
    },
    contactPoint: {
      '@type': 'ContactPoint',
      contactType: 'customer service',
      availableLanguage: 'Spanish',
    },
  };
}

/**
 * Generates Article JSON-LD schema for blog posts
 * @see https://schema.org/Article
 */
export function generateArticleSchema(
  article: {
    title: string;
    description: string;
    author: string;
    publishDate: string;
    modifiedDate?: string;
    image?: string;
  },
  pageUrl: string,
  baseUrl: string = SITE
): object {
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: article.title,
    description: article.description,
    // Autoría institucional: los artículos los firma el área técnica de la empresa, no una
    // persona física. Va con su PROPIO @id y como parte de la organización: reusar el @id del
    // nodo Organization con otro `name` declaraba dos nombres para la misma entidad, que es
    // justo lo que confunde a un buscador cuando intenta resolverla.
    author: {
      '@type': 'Organization',
      '@id': `${baseUrl}/#area-tecnica`,
      name: article.author,
      url: baseUrl,
      parentOrganization: { '@id': `${baseUrl}/#organization` },
    },
    publisher: {
      '@type': 'Organization',
      '@id': `${baseUrl}/#organization`,
      name: MARCA,
      logo: {
        '@type': 'ImageObject',
        url: `${baseUrl}/images/logo-firefighter-mexico.svg`,
        width: 200,
        height: 50,
      },
    },
    datePublished: article.publishDate,
    dateModified: article.modifiedDate || article.publishDate,
    mainEntityOfPage: {
      '@type': 'WebPage',
      '@id': pageUrl,
    },
    ...(article.image && {
      image: {
        '@type': 'ImageObject',
        url: article.image.startsWith('http') ? article.image : `${baseUrl}${article.image}`,
      },
    }),
  };
}

/**
 * Generates LocalBusiness JSON-LD schema for state/municipality pages
 * @see https://schema.org/GovernmentOrganization
 */
export function generateStateDirectorySchema(
  stateName: string,
  stationCount: number,
  pageUrl: string
): object {
  return {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: `Estaciones de Bomberos en ${stateName}`,
    description: `Directorio de ${stationCount} estaciones de bomberos en ${stateName}, México. Teléfonos, direcciones y servicios de emergencia.`,
    url: pageUrl,
    numberOfItems: stationCount,
    itemListOrder: 'https://schema.org/ItemListUnordered',
  };
}

/**
 * Formats a phone number for schema.org telephone format
 */
export function formatPhoneForSchema(phone: string): string {
  // Remove all non-numeric characters except +
  const cleaned = phone.replace(/[^\d+]/g, '');

  // If it starts with +52, keep it; otherwise add it
  if (cleaned.startsWith('+52')) {
    return cleaned;
  } else if (cleaned.startsWith('52')) {
    return `+${cleaned}`;
  } else {
    return `+52${cleaned}`;
  }
}

/**
 * Generates meta description from station data
 */
export function generateStationMetaDescription(station: StationData): string {
  const serviceLabels: Record<string, string> = {
    'combate-incendios': 'incendios',
    'atencion-medica': 'atención médica',
    'rescate-vehicular': 'rescate vehicular',
    'rescate-acuatico': 'rescate acuático',
    'materiales-peligrosos': 'HAZMAT',
  };

  const mainServices = station.services
    .slice(0, 3)
    .map(s => serviceLabels[s] || s)
    .join(', ');

  return `${station.name} en ${station.municipality}, ${station.state}. Servicios: ${mainServices}. Tel: ${station.phone}. Emergencias: 911.`.slice(0, 160);
}
