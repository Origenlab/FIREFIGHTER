# Módulos del Homepage — FIREFIGHTER México

> Arquitectura completa del `index.astro`. Cada sección documentada con función, estructura, datos y estado de implementación.

---

## Orden en index.astro

```
Hero → QuickNav → ProductCategories → WhyFirefighter → Sectors
→ HowItWorks → ContactChannels → Testimonials → FAQ → [Footer en BaseLayout]
```

---

## 01 · Hero
**Archivo**: `src/components/home/Hero.astro`
**Fondo**: Oscuro / imagen impactante
**Función**: Primera impresión. Propuesta de valor + CTA primarios.

### Debe contener
- H1 con propuesta de valor principal (equipos profesionales contra incendios en México)
- Subtítulo con diferenciadores clave
- CTA primario → WhatsApp
- CTA secundario → Cotización / catálogo
- Trust badges: NFPA · NOM · UL · Entrega 32 estados
- Estadística rápida (500+ proyectos / 50+ años)

**Estado**: ⚠️ Existente — pendiente revisión y mejora visual

---

## 02 · QuickNav
**Archivo**: `src/components/home/QuickNav.astro`
**Función**: Navegación rápida post-hero a las categorías.

### Debe contener
- Barra de acceso rápido a: Equipos Bomberos | SCBA | Extintores | Sistemas Fijos | Rescate | Detección | Gabinetes | Forestal
- Cada link con ícono + label + link a WhatsApp o sección

**Estado**: ⚠️ Existente — pendiente revisión

---

## 03 · ProductCategories
**Archivo**: `src/components/home/ProductCategories.astro`
**Fondo**: `#ffffff` | Padding: 96px 0
**Función**: Catálogo de las 8 categorías principales de producto.

### Header 50/50
- **Izquierda**: Eyebrow "Catálogo de Productos" + H2 "Equipos certificados para cada operación"
- **Derecha**:
  - *Distribución Autorizada en México* — párrafo sobre marcas MSA, Scott, Holmatro, Amerex
  - *Asesoría Técnica Especializada sin Costo* — párrafo sobre ingenieros NFPA

### Grid de cards
`grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6`

### Las 8 categorías

| # | Nombre | Badge (norma) | CTA |
|---|---|---|---|
| 1 | Equipos para Bomberos | NFPA 1971 | WhatsApp |
| 2 | SCBA y Respiración | NFPA 1981 | WhatsApp |
| 3 | Extintores | NOM-154-SCFI | WhatsApp |
| 4 | Sistemas de Supresión Fija | NFPA 13 | WhatsApp |
| 5 | Herramientas de Rescate | NFPA 1936 | WhatsApp |
| 6 | Detección y Alarma | NFPA 72 | WhatsApp |
| 7 | Gabinetes y Mangueras | NOM-002 | WhatsApp |
| 8 | Equipo Forestal | Brigadas | WhatsApp |

**Estado**: ✅ Implementado y homologado

---

## 04 · WhyFirefighter
**Archivo**: `src/components/home/WhyFirefighter.astro`
**Fondo**: `#f8fafc` | Border-top: `1px solid #e4e4e7`
**Función**: 6 razones diferenciadoras de la empresa.

### Header 50/50
- **Izquierda**: Eyebrow "Por Qué Elegirnos" + H2 "La diferencia que protege vidas"
- **Derecha**: 2 párrafos SEO (experiencia + documentación)

### Stats strip (4 números)
`500+ Proyectos · 50+ Años · 32 Estados · <24h Respuesta`

### Grid de cards
`md:grid-cols-2 lg:grid-cols-3 gap-6`

### Las 6 razones

| # | Badge | Título | Highlight |
|---|---|---|---|
| 01 | 01 | Distribución Autorizada | Directo del fabricante |
| 02 | 02 | Documentación Técnica Completa | Lista para licitaciones |
| 03 | 03 | Asesoría Técnica sin Costo | Ingenieros NFPA certificados |
| 04 | 04 | Entrega en 32 Estados | Logística nacional |
| 05 | 05 | Soporte Posventa | Refacciones OEM originales |
| 06 | 06 | Respuesta en <24 Horas | Propuesta técnica urgente |

**Estado**: ✅ Implementado y homologado

---

## 05 · Sectors
**Archivo**: `src/components/home/Sectors.astro`
**Fondo**: `#f8fafc` | Border-top: `1px solid #e4e4e7`
**Función**: 6 sectores atendidos con equipo y norma específica por industria.

### Header 50/50
- **Izquierda**: Eyebrow "Sectores que Atendemos" + H2 "Soluciones para cada industria"
- **Derecha**: 2 párrafos SEO (cobertura nacional + cumplimiento normativo)

### Grid de cards
`md:grid-cols-2 lg:grid-cols-3 gap-6`

### Los 6 sectores

| # | Título | Badge (norma) | Highlight |
|---|---|---|---|
| 1 | Cuerpos de Bomberos | NFPA 1971 · 1977 · 1981 | EPP completo certificado NFPA |
| 2 | Industria y Manufactura | NOM-002-STPS | Cumplimiento NOM-002-STPS garantizado |
| 3 | Hospitales y Salud | NOM-003-SEGOB | Sistemas sin residuos para equipos médicos |
| 4 | Hoteles y Centros Comerciales | NOM-002 · NOM-003 | Documentación para verificaciones PC |
| 5 | Construcción y Proyectos | NFPA 13 · FM Approvals | Diseño + suministro + instalación |
| 6 | Gobierno y Protección Civil | LAASSP · LOPSRM | Documentación completa para licitaciones |

**Estado**: ✅ Implementado y homologado

---

## 06 · HowItWorks
**Archivo**: `src/components/home/HowItWorks.astro`
**Fondo**: Oscuro (dark theme)
**Función**: Proceso de compra en 4 pasos. Reduce fricción para nuevos clientes.

### Header 50/50 (dark variant)
- Colores de texto adaptados para fondo oscuro
- Párrafos: `color:#71717a` con `strong color:#a1a1aa`

### Los 4 pasos
1. **Contacto** — Escríbenos por WhatsApp o email con tu necesidad
2. **Análisis** — Nuestros ingenieros analizan tu riesgo y norma aplicable
3. **Propuesta** — Enviamos propuesta técnica y comercial en < 24 h
4. **Entrega** — Coordinamos logística y entregamos con documentación completa

**Cards**: padding 44px 36px, gap 22px

**Estado**: ✅ Implementado

---

## 07 · ContactChannels
**Archivo**: `src/components/home/ContactChannels.astro`
**Fondo**: `#f8fafc` | Border-top: `1px solid #e4e4e7`
**Función**: 3 canales de atención según el tipo de cliente/necesidad.

### Header 50/50
- **Izquierda**: Eyebrow "Atención Especializada" + H2 "Canal correcto según tu necesidad"
- **Derecha**: 2 párrafos SEO (atención personalizada + respuesta < 2 h)

### Grid de cards
`md:grid-cols-3 gap-6`

### Los 3 canales

| # | Badge | Título | CTA |
|---|---|---|---|
| 1 | Gobierno · Compras públicas | Licitaciones Públicas | licitaciones@firefighter.mx |
| 2 | Sin costo · Respuesta inmediata | Asesoría Técnica | WhatsApp |
| 3 | Posventa · Primer nivel | Soporte y Garantía | soporte@firefighter.mx |

**Estado**: ✅ Implementado y homologado

---

## 08 · Testimonials
**Archivo**: `src/components/home/Testimonials.astro`
**Fondo**: `#f8fafc` | Border-top: `1px solid #e4e4e7`
**Función**: Prueba social. 8 reseñas de clientes por segmento.

### Header 50/50
- **Izquierda**: Eyebrow "Reseñas de Clientes" + H2 "Lo que dicen quienes confían en FIREFIGHTER"
- **Derecha**: 2 párrafos SEO (clientes reales + satisfacción en cada etapa)

### Stats strip
`4.9 Calificación · 500+ Proyectos · 98% Satisfechos · <24h Respuesta`

### Grid de cards
`grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6`

### Estructura de cada card
- Estrellas (5 SVG amarillas `#f59e0b`) + badge "Verificado" verde
- Quote en itálica `font-style:italic`
- Separador 1px
- Avatar: círculo rojo con iniciales del nombre
- Nombre + Rol + Empresa
- Tag sector (chip `#fef2f2`)

### Los 8 perfiles

| Tag sector | Nombre | Empresa |
|---|---|---|
| Brigada industrial | Ing. Roberto Garza | Grupo Alfa — Monterrey |
| Licitación pública | C. Miguel Ángel Torres | Municipio de Querétaro |
| Sistemas fijos | Lic. Andrea Vázquez | Hospital Ángeles — CDMX |
| Herramientas rescate | Cdte. Ernesto Sandoval | H. Bomberos Guadalajara |
| Equipamiento masivo | Ing. Carmen Reyes | Plásticos del Norte |
| Cuerpo voluntario | Tte. Luis Hernández | Bomberos Voluntarios Puebla |
| Detección y alarma | Arq. Sofía Morales | Hotel Grand Fiesta — Los Cabos |
| Gobierno federal | Lic. Jorge Medina | IMSS — Delegación Centro |

**Estado**: ✅ Implementado

---

## 09 · FAQ
**Archivo**: `src/components/home/FAQ.astro`
**Fondo**: `#ffffff` | Border-top: `1px solid #e4e4e7`
**Función**: Resolver objeciones + capturar leads al WhatsApp.

### Header 50/50
- **Izquierda**: Eyebrow "Preguntas Frecuentes" + H2 "Todo lo que necesitas saber antes de cotizar"
- **Derecha**: 2 párrafos SEO (dudas técnicas + pregunta diferente → formulario)

### Layout de dos columnas
`grid-cols-1 lg:grid-cols-2 gap-12` con `align-items:start`

### Columna izquierda — Accordion (8 preguntas)
Comportamiento JS: toggle maxHeight, aria-expanded, rotación ícono, border rojo al abrir. Solo una abierta a la vez.

| # | Pregunta |
|---|---|
| 1 | ¿Cuánto tiempo tardan en entregar una cotización? |
| 2 | ¿Los equipos incluyen certificado de origen y ficha técnica? |
| 3 | ¿Hacen entregas en toda la República Mexicana? |
| 4 | ¿Qué normas y certificaciones cubren sus equipos? |
| 5 | ¿Pueden participar en licitaciones públicas bajo LAASSP? |
| 6 | ¿Ofrecen asesoría técnica para seleccionar el equipo correcto? |
| 7 | ¿Qué marcas distribuyen de forma autorizada? |
| 8 | ¿Tienen soporte posventa y servicio de garantía? |

### Columna derecha — Formulario → WhatsApp (sticky)
**Header**: `background:#09090b` con ícono WhatsApp + título

**Campos**:
- Nombre* (text)
- Empresa (text)
- Teléfono* (tel)
- Sector / Tipo de proyecto (select: 7 opciones)
- Mensaje / Pregunta* (textarea)

**Submit**: Construye URL `wa.me/525500000000?text=...` con campos en formato WhatsApp Markdown (*Nombre:* valor).
**Validación**: nombre, teléfono, mensaje requeridos.

**Estado**: ✅ Implementado

---

## 10 · Footer
**Archivo**: `src/components/layout/Footer.astro`
**Función**: Cierre profesional B2B. 4 bloques verticales.

### Bloque 1 — Pre-footer rojo (`#dc2626`, padding 56px)
- Grid 50/50: H2 CTA + párrafo SEO
- Botón [WhatsApp Cotizar] blanco + Botón [Licitaciones] oscuro semitransparente

### Bloque 2 — Main footer (`#09090b`, padding 72px top, 56px bottom)
Grid 5 cols: `grid-cols-1 md:grid-cols-2 lg:grid-cols-5`

**Col Brand (×2)**:
- Logo (cuadro rojo 44px + texto FIREFIGHTER / México · Equipo Profesional)
- Descripción con marcas distribuidoras
- 3 íconos de contacto: WhatsApp · ventas@ · licitaciones@
- 4 redes: Facebook, Instagram, LinkedIn, YouTube

**Col Productos** (8 links → WhatsApp por categoría):
Bomberos · Trajes EPP · SCBA · Extintores · Supresión · Rescate · Gabinetes · Detección

**Col Sectores** (8 links → WhatsApp por industria):
Bomberos · Industria · Hospitales · Hoteles · Construcción · Gobierno · Escuelas · Aeropuertos

**Col Empresa + Legal**:
- Empresa: Nosotros · Marcas · Casos · Blog · Cotización · Licitaciones · Soporte
- Legal: Privacidad · Términos · Garantías · Devoluciones · Sitemap

### Bloque 3 — Certifications strip (`#111`, padding 24px)
7 badges con label + sub:
`NFPA 1971 · NFPA 1981 · NFPA 13 · NFPA 72 · NOM-002-STPS · UL Listed · FM Approvals`

### Bloque 4 — Bottom bar (`#000`, padding 20px)
Grid 3 cols: Copyright · Distribuidores autorizados · Hecho en México 🇲🇽

**Estado**: ✅ Implementado

---

## Pendientes globales

- [ ] **Número WhatsApp real** — reemplazar `525500000000` en todos los archivos
- [ ] **Hero** — revisión y mejora visual
- [ ] **Mobile responsive overhaul** — aplicar skill `mobile-responsive-overhaul`
- [ ] **Imágenes de productos** — reemplazar placeholders con fotos reales
- [ ] **Páginas internas**: `/nosotros`, `/marcas`, `/casos`, `/blog`
- [ ] **Página detalle categoría** — template de categoría de producto
- [ ] **Formulario licitaciones** — página dedicada con campos extendidos
- [ ] **SEO técnico** — meta tags, OG, schema markup por página
- [ ] **Analytics** — Google Analytics / Tag Manager
- [ ] **CRM / Leads** — integración WhatsApp Business API o Google Sheets
