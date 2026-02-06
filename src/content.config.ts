import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Stations collection
const stations = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/stations' }),
  schema: z.object({
    name: z.string(),
    stationCode: z.string().optional(),
    serviceType: z.enum(['profesional', 'voluntario', 'industrial', 'aeroportuario', 'proteccion-civil']),
    status: z.enum(['activa', 'inactiva', 'en-construccion']).default('activa'),
    state: z.string(),
    stateSlug: z.string(),
    municipality: z.string(),
    city: z.string(),
    address: z.string(),
    neighborhood: z.string().optional(),
    postalCode: z.string().optional(),
    latitude: z.number(),
    longitude: z.number(),
    phone: z.string(),
    emergencyPhone: z.string().default('911'),
    adminPhone: z.string().optional(),
    email: z.string().optional(),
    website: z.string().optional(),
    operatingHours: z.string().default('24/7'),
    chiefName: z.string().optional(),
    totalPersonnel: z.number().optional(),
    yearEstablished: z.number().optional(),
    services: z.array(z.enum([
      'combate-incendios',
      'atencion-medica',
      'rescate-vehicular',
      'rescate-acuatico',
      'materiales-peligrosos',
      'rescate-alturas',
      'proteccion-civil',
      'capacitacion',
      'prevencion'
    ])).default(['combate-incendios']),
    equipment: z.object({
      fireTrucks: z.number().default(0),
      ambulances: z.number().default(0),
      rescueVehicles: z.number().default(0),
      other: z.string().optional(),
    }).optional(),
    image: z.string().optional(),
    verified: z.boolean().default(false),
    lastUpdated: z.string(),
    metaTitle: z.string().optional(),
    metaDescription: z.string().optional(),
  }),
});

// States collection
const states = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/states' }),
  schema: z.object({
    name: z.string(),
    code: z.string(),
    capital: z.string(),
    region: z.string(),
    emergencyPhone: z.string().default('911'),
    civilProtectionPhone: z.string().optional(),
    image: z.string().optional(),
    metaTitle: z.string().optional(),
    metaDescription: z.string().optional(),
  }),
});

// Blog collection
const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    author: z.string().default('Firefighter México'),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = {
  stations,
  states,
  blog,
};
