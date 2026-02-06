# Guía de Contenido para Estaciones de Bomberos

## Documento de Especificaciones Técnicas v1.0
**Firefighter México - Directorio Nacional de Estaciones de Bomberos**

---

## 1. Estructura del Archivo Markdown

Cada estación debe tener un archivo `.md` ubicado en:
```
src/content/stations/{estado-slug}/{nombre-estacion}.md
```

### 1.1 Nomenclatura de Archivos

| Formato | Ejemplo |
|---------|---------|
| `estacion-{numero}-{nombre-corto}.md` | `estacion-01-central.md` |
| `estacion-{nombre-zona}.md` | `estacion-tlalpan.md` |

---

## 2. Frontmatter (Metadatos YAML)

### 2.1 Campos Obligatorios

```yaml
---
name: "Nombre Completo de la Estación"
stationCode: "EB-{ESTADO}-{NUMERO}"
serviceType: "profesional | voluntario | industrial | aeroportuario | proteccion-civil"
status: "activa | inactiva | en-construccion"
state: "Nombre del Estado"
stateSlug: "estado-slug"
municipality: "Nombre del Municipio/Alcaldía"
city: "Nombre de la Ciudad"
address: "Calle y Número"
neighborhood: "Nombre de la Colonia"
postalCode: "00000"
latitude: 00.0000
longitude: -00.0000
phone: "+52 00 0000-0000"
emergencyPhone: "911"
operatingHours: "24/7"
services:
  - combate-incendios
  - atencion-medica
verified: true | false
lastUpdated: "YYYY-MM-DD"
metaTitle: "Título SEO (máx 60 caracteres)"
metaDescription: "Descripción SEO (máx 160 caracteres)"
---
```

### 2.2 Campos Opcionales

```yaml
adminPhone: "+52 00 0000-0000"
email: "correo@ejemplo.com"
website: "https://ejemplo.com"
totalPersonnel: 00
yearEstablished: 0000
equipment:
  fireTrucks: 0
  ambulances: 0
  rescueVehicles: 0
  ladderTrucks: 0
  hazmatUnits: 0
socialMedia:
  facebook: "url"
  twitter: "url"
```

### 2.3 Códigos de Estación

| Estado | Prefijo | Ejemplo |
|--------|---------|---------|
| Ciudad de México | EB-CDMX | EB-CDMX-001 |
| Jalisco | EB-JAL | EB-JAL-001 |
| Nuevo León | EB-NL | EB-NL-001 |
| Estado de México | EB-MEX | EB-MEX-001 |

### 2.4 Tipos de Servicio Válidos

| Valor | Descripción |
|-------|-------------|
| `profesional` | Bomberos de carrera con salario |
| `voluntario` | Bomberos voluntarios |
| `industrial` | Brigadas de empresas/industrias |
| `aeroportuario` | Servicios de rescate en aeropuertos |
| `proteccion-civil` | Dependientes de Protección Civil |

### 2.5 Servicios Disponibles

```yaml
services:
  - combate-incendios        # Combate de Incendios
  - atencion-medica          # Atención Médica Prehospitalaria
  - rescate-vehicular        # Rescate Vehicular y Extricación
  - rescate-acuatico         # Rescate Acuático
  - rescate-alturas          # Rescate en Alturas
  - materiales-peligrosos    # Materiales Peligrosos (HAZMAT)
  - proteccion-civil         # Protección Civil
  - capacitacion             # Capacitación y Prevención
  - prevencion               # Inspecciones de Seguridad
```

---

## 3. Estructura del Contenido Markdown

### 3.1 Secciones Obligatorias

El contenido debe seguir esta estructura exacta en orden:

```markdown
## Descripción General
[Párrafo introductorio de 80-120 palabras]

## Área de Cobertura Territorial
### Colonias Principales
[Lista de colonias con descripción breve]

### Puntos de Interés Estratégicos
[Lista de lugares importantes]

## Infraestructura y Equipamiento Operativo
### Flota Vehicular
[Tabla con unidades]

### Equipamiento Especializado
[Listas organizadas por categoría]

## Servicios Especializados
[Subsecciones por cada servicio]

## Estructura del Personal Operativo
[Tabla con rangos y funciones]

## Tiempos de Respuesta Estimados
[Tabla con zonas y tiempos]

## Coordinación Institucional
[Lista de instituciones]

## Cómo Reportar una Emergencia
### Paso a Paso
[Lista numerada]

### Información Útil para tu Reporte
[Lista de datos importantes]

---
[Nota de pie de página con fuentes]
```

---

## 4. Guía de Redacción por Sección

### 4.1 Descripción General

**Objetivo:** Presentar la estación de forma profesional y contextualizada.

**Debe incluir:**
- Nombre completo de la estación en **negritas**
- Importancia dentro del cuerpo de bomberos
- Ubicación estratégica y zona que cubre
- Año de fundación (si se conoce) en **negritas**
- Dato distintivo o relevante

**Ejemplo:**
```markdown
## Descripción General

La **Estación de Bomberos 02 Santa María la Ribera** es una de las unidades
operativas más importantes del Heroico Cuerpo de Bomberos de la Ciudad de México.
Ubicada estratégicamente en el corazón de la colonia Santa María la Ribera,
esta estación brinda cobertura a una de las zonas con mayor densidad poblacional
y actividad comercial del norte de la alcaldía Cuauhtémoc.

Fundada en **1922**, cuenta con más de un siglo de servicio ininterrumpido
a la comunidad, consolidándose como un pilar fundamental en la protección civil
y atención de emergencias de la zona centro-norte de la capital mexicana.
```

**Longitud:** 80-120 palabras

---

### 4.2 Área de Cobertura Territorial

**Objetivo:** Definir claramente la jurisdicción de la estación.

**Formato de Colonias:**
```markdown
### Colonias Principales
- **Nombre de Colonia** — Descripción breve (10-15 palabras)
- **Nombre de Colonia** — Descripción breve
```

**Formato de Puntos de Interés:**
```markdown
### Puntos de Interés Estratégicos
- Nombre del lugar
- Nombre del lugar (nota si aplica)
```

**Ejemplo:**
```markdown
## Área de Cobertura Territorial

La Estación 02 tiene jurisdicción sobre un área aproximada de **12.5 km²**,
atendiendo emergencias en las siguientes demarcaciones:

### Colonias Principales
- **Santa María la Ribera** — Zona histórica con edificaciones patrimoniales del siglo XIX
- **San Rafael** — Alta densidad comercial y residencial mixta
- **Buenavista** — Terminal de autobuses y estación de Tren Suburbano
- **Tabacalera** — Corredor comercial y zona hotelera
- **Guerrero** — Alta concentración poblacional y comercio informal

### Puntos de Interés Estratégicos
- Museo Universitario del Chopo
- Kiosco Morisco de Santa María la Ribera
- Alameda de Santa María la Ribera
- Estación Buenavista del Tren Suburbano
- Terminal de Autobuses del Norte (apoyo)
- Monumento a la Revolución (cobertura conjunta con Estación Central)
- Mercado de San Cosme
```

---

### 4.3 Infraestructura y Equipamiento

**Formato de Tabla de Flota Vehicular:**

```markdown
### Flota Vehicular

| Unidad | Tipo | Especificaciones Técnicas |
|--------|------|---------------------------|
| **Motobomba XX-A** | Autobomba Tipo I | Capacidad: X,000 L / Bomba: X,XXX GPM / Mangueras: XXXm |
| **Motobomba XX-B** | Autobomba Tipo II | Capacidad: X,000 L / Bomba: X,XXX GPM / Escalera: XXm |
| **Ambulancia XX** | SVB/SVA | Soporte Vital Básico/Avanzado / Desfibrilador / Oxígeno |
| **Rescate XX** | Unidad Pesada | Equipo hidráulico / Planta de luz / Generador |
```

**Categorías de Equipamiento:**

```markdown
### Equipamiento Especializado

**Protección Personal:**
- Trajes estructurales certificados NFPA 1971
- Cascos con protección facial y térmica
- Botas de seguridad con puntera de acero
- Guantes de intervención multinivel

**Equipo de Respiración Autónoma (ERA):**
- Equipos SCBA con cilindros de 45 minutos de autonomía
- Sistema de alarma de baja presión (PASS)
- Máscaras de visión panorámica

**Herramientas de Rescate:**
- Separador hidráulico (Quijadas de la Vida)
- Cortador hidráulico para columnas y techos
- Cilindros de expansión
- Cojines neumáticos de levantamiento

**Equipo de Altura:**
- Sistema de cuerdas estáticas y dinámicas
- Arneses de rescate clase III
- Poleas y descensores certificados
- Trípode de rescate para espacios confinados
```

---

### 4.4 Servicios Especializados

**Formato por servicio:**

```markdown
## Servicios Especializados

### Combate y Supresión de Incendios
Respuesta a incendios estructurales, vehiculares, forestales urbanos y en
espacios confinados. El personal está capacitado en:
- Técnicas de ventilación táctica (PPV/NPV)
- Búsqueda primaria y secundaria en estructuras
- Combate de incendios en sótanos y edificios de altura media
- Control de incendios con materiales peligrosos Nivel I

### Atención Prehospitalaria de Urgencias
Servicio de estabilización y traslado de pacientes con ambulancia equipada:
- Reanimación cardiopulmonar (RCP)
- Control de hemorragias y fracturas
- Manejo de vía aérea básica
- Coordinación con hospitales: [Nombres de hospitales cercanos]
```

**Servicios estándar a documentar:**
1. Combate y Supresión de Incendios
2. Atención Prehospitalaria de Urgencias
3. Rescate Vehicular y Extricación
4. Rescate Técnico en Alturas
5. Servicios Preventivos

---

### 4.5 Estructura del Personal

**Formato de tabla:**

```markdown
## Estructura del Personal Operativo

La estación opera con **XX elementos** distribuidos en guardias de 24x48 horas:

| Rango | Cantidad | Función |
|-------|----------|---------|
| Oficial de Guardia | 1 | Comando de operaciones y toma de decisiones |
| Sargento Primero | 1 | Segundo al mando, supervisión de cuadrillas |
| Sargento Segundo | 2 | Jefes de escuadra en campo |
| Cabo | X | Operadores de equipo especializado |
| Bombero de Línea | X | Combate directo de emergencias |
| Paramédico | X | Atención prehospitalaria |
| Operador de Unidad | X | Conducción de vehículos de emergencia |
```

---

### 4.6 Tiempos de Respuesta

**Formato de tabla:**

```markdown
## Tiempos de Respuesta Estimados

| Zona | Tiempo Promedio |
|------|-----------------|
| Área primaria (colonias principales) | 3-5 minutos |
| Área secundaria (colonias adyacentes) | 5-7 minutos |
| Apoyo a estaciones vecinas | 8-12 minutos |
```

---

### 4.7 Coordinación Institucional

**Formato de lista:**

```markdown
## Coordinación Institucional

La Estación XX mantiene comunicación y coordinación permanente con:

- **C5 CDMX** — Centro de Comando, Control, Cómputo, Comunicaciones y Contacto Ciudadano
- **ERUM** — Escuadrón de Rescate y Urgencias Médicas
- **SSC-CDMX** — Secretaría de Seguridad Ciudadana
- **Protección Civil [Alcaldía]** — Coordinación con la alcaldía
- **Cruz Roja Mexicana** — Apoyo en emergencias masivas
- **SEDENA** — Plan DN-III-E en contingencias mayores
```

---

### 4.8 Cómo Reportar una Emergencia

**Contenido estándar (copiar exacto):**

```markdown
## Cómo Reportar una Emergencia

### Paso a Paso

1. **Marca 911** desde cualquier teléfono (la llamada es gratuita)
2. **Mantén la calma** y habla con claridad
3. **Indica el tipo de emergencia:** incendio, accidente, emergencia médica, fuga de gas
4. **Proporciona la ubicación exacta:** calle, número, colonia, referencias visuales
5. **Describe la situación:** personas atrapadas, heridos, magnitud del fuego
6. **Sigue las instrucciones** del operador de emergencias
7. **No cuelgues** hasta que te lo indiquen

### Información Útil para tu Reporte
- Número de personas afectadas
- Si hay niños, adultos mayores o personas con discapacidad
- Si hay riesgo de explosión (tanques de gas, materiales inflamables)
- Punto de referencia para que lleguen las unidades
```

---

### 4.9 Nota de Pie de Página

**Formato estándar:**

```markdown
---

*Ficha técnica elaborada con información de fuentes públicas del Heroico Cuerpo
de Bomberos de [Ciudad/Estado]. La información está sujeta a actualizaciones.
Última revisión: [Mes Año].*
```

---

## 5. Reglas de Estilo

### 5.1 Formato de Texto

| Elemento | Formato |
|----------|---------|
| Nombres de estaciones | **Negritas** |
| Años | **Negritas** |
| Datos numéricos importantes | **Negritas** |
| Nombres de colonias en listas | **Negritas** |
| Nombres de unidades vehiculares | **Negritas** |
| Términos técnicos | Normal (primera mención puede ir en *cursivas*) |
| Acrónimos | Definir en primera mención: SCBA (Self-Contained Breathing Apparatus) |

### 5.2 Formato de Números

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Años | Sin comas | 1922 |
| Cantidades grandes | Con comas | 3,000 L |
| Porcentajes | Símbolo % | 95% |
| Teléfonos | +52 XX XXXX-XXXX | +52 55 5541-2820 |
| Coordenadas | 4 decimales | 19.4515, -99.1608 |

### 5.3 Separadores en Listas

- Usar guión largo (—) para descripciones: `**Colonia** — Descripción`
- Usar dos puntos (:) para especificaciones: `Capacidad: 3,000 L`
- Usar barra (/) para múltiples valores: `Bomba: 1,500 GPM / Mangueras: 300m`

---

## 6. SEO y Metadatos

### 6.1 Meta Title

**Formato:**
```
Estación de Bomberos [Nombre] | [Ciudad] | Heroico Cuerpo de Bomberos
```

**Ejemplo:**
```
Estación de Bomberos 02 Santa María la Ribera | CDMX | Heroico Cuerpo de Bomberos
```

**Límite:** 60 caracteres

### 6.2 Meta Description

**Debe incluir:**
- Nombre de la estación
- Ubicación (colonia, ciudad)
- Teléfono de emergencia
- Call to action

**Formato:**
```
Estación de Bomberos [Nombre] en [Colonia], [Ciudad]. Teléfono de emergencia,
ubicación exacta, servicios especializados y área de cobertura. Emergencias: 911.
```

**Límite:** 160 caracteres

---

## 7. Checklist de Validación

Antes de publicar, verificar:

### Frontmatter
- [ ] Todos los campos obligatorios completados
- [ ] Coordenadas verificadas en Google Maps
- [ ] Teléfono en formato correcto
- [ ] stateSlug coincide con la carpeta
- [ ] lastUpdated con fecha actual

### Contenido
- [ ] Todas las secciones obligatorias presentes
- [ ] Tablas con formato correcto
- [ ] Listas con formato consistente
- [ ] Sin errores ortográficos
- [ ] Información verificada con fuentes oficiales

### SEO
- [ ] metaTitle < 60 caracteres
- [ ] metaDescription < 160 caracteres
- [ ] Incluye keywords: bomberos, estación, [ciudad], emergencias

---

## 8. Ejemplo Completo

Ver archivo de referencia:
```
src/content/stations/ciudad-de-mexico/estacion-02-santa-maria.md
```

---

## 9. Actualizaciones del Documento

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2026-02-06 | Documento inicial |

---

**Documento elaborado por:** Firefighter México
**Última actualización:** Febrero 2026
