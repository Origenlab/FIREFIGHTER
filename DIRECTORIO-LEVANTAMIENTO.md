# Directorio de estaciones de bomberos — bitácora del levantamiento

Registro del proceso de captura estado por estado. Sirve para no repetir búsquedas,
para saber qué quedó pendiente y para poder defender cada dato publicado.

## Criterio de publicación

Publicamos **solo datos verificables**. Si un domicilio, teléfono o coordenada no tiene
una fuente pública comprobable, el campo va vacío y se marca como pendiente en la ficha.
Un teléfono equivocado en un directorio de emergencia es peor que un campo en blanco.

Nunca se inventan teléfonos, domicilios ni coordenadas.

## Orden de trabajo por estado

1. **Portal oficial primero.** Ha sido la mejor fuente en todos los estados. Suele dar
   colonia, CP y teléfonos que Maps no trae, y a veces revela estaciones que Maps no lista.
2. Barrido por región en Google Maps, una búsqueda a la vez, con scroll hasta el final.
3. Apertura de ficha para domicilio completo en las estaciones principales.
4. Redacción de fichas con contexto por municipio.
5. `npm run build`, luego `python3 scripts/auditoria/audit-sitio.py` y
   `python3 scripts/auditoria/audit-directorio.py <slug-del-estado>`, que revisa títulos y
   descripciones duplicadas en todo el sitio y H1, canonical, JSON-LD y longitudes en el
   estado recién publicado.
6. Actualización de `src/data/states.json` (`totalStations`) con el conteo real.

## Reglas de resolución

- **Duplicados:** dos registros de Maps a menos de ~150 m que comparten domicilio o
  teléfono son la misma corporación (estación + patronato, o central + unidad municipal).
- **Ambigüedad de municipio:** si una coordenada cae en un límite municipal y no se puede
  resolver, se excluye y se documenta, en vez de arriesgar un municipio equivocado.
- **Se excluyen:** brigadas industriales de empresa, servicios privados de ambulancia,
  grupos de rescate que no sean bomberos, negocios con "bomberos" en el nombre y
  registros cerrados.

## Fuentes no confiables

`bombero.mx` y `firefighter.mx` publican estaciones fabricadas, con teléfonos de dígitos
secuenciales. No usar como fuente.

## Estados levantados

| Estado | Fichas | Municipios | Fecha |
|---|---|---|---|
| Sonora | 58 | 28 | ago 2026 |
| Sinaloa | 35 | 14 | ago 2026 |
| Baja California | 45 | 7 de 7 | ago 2026 |
| Baja California Sur | 22 | 5 de 5 | ago 2026 |
| Estado de México | 45 | — | — |
| Jalisco | 40 | — | — |
| Coahuila | 39 | 19 | ago 2026 |
| Tamaulipas | 33 | 18 | ago 2026 |
| Guanajuato | 32 | — | — |
| Nuevo León | 31 | — | — |
| Chihuahua | 30 | — | — |
| Puebla | 26 | — | — |
| Veracruz | 24 | — | — |
| Ciudad de México | 21 | — | — |
| Nayarit | 19 | 11 de 20 | ago 2026 |
| Aguascalientes | 13 | — | — |

**Total: 513 fichas en 16 de 32 estados.**

---

## Coahuila — agosto 2026

39 fichas en 19 municipios: Saltillo 7, Torreón 7, Piedras Negras 3, Acuña 3,
Monclova 2, Frontera 2, Castaños 2, y una cada uno en Ramos Arizpe, Arteaga, Matamoros,
San Pedro, Francisco I. Madero, Parras, San Buenaventura, Nava, Allende, Zaragoza,
Sabinas, San Juan de Sabinas y Múzquiz.

### Fuente oficial encontrada

`torreon.gob.mx/proteccioncivil/` publica las **7 estaciones de Torreón** con domicilio,
colonia y teléfono. Es la única fuente oficial de Coahuila que dio un listado completo;
esas 7 fichas van marcadas `verified: true`.

No dieron listado: el portal del Patronato de Saltillo (`patbomberos.com`, solo un
teléfono general) ni `tramitescoahuila.gob.mx`. El portal de la **Subsecretaría de
Protección Civil de Coahuila** (`proteccioncivil.sfpcoahuila.gob.mx/modulo22.php?opcion=8`)
estaba **caído** al momento del levantamiento, con certificado SSL expirado —
**vale la pena reintentarlo**: por su estructura parecería contener el directorio
estatal de unidades municipales.

### Ambigüedad resuelta: la central de Torreón

Maps tiene dos registros con el mismo teléfono (871 712 0066) y ambos sobre Degollado,
a 2.4 km uno del otro:

- `25.5345707, -103.4478298` — "degollado s/n col. luis echeverria"
- `25.5526266, -103.4352358` — "C. Degollado SN, Tercero de Cobián Centro, 27220"

Se publicó el primero porque su colonia coincide con la que informa el ayuntamiento
(Luis Echeverría Álvarez). Lo confirma un tercer registro, la **Coordinación Municipal
de Protección Civil de Torreón**, a 65 m del primer punto.

### Registros descartados

| Registro | Motivo |
|---|---|
| Bomberos AHMSA 2, Monclova | Brigada industrial de empresa |
| Plaza de Bomberos, Monclova | Parque público, no estación |
| "Hidrrante", Piedras Negras | Registro basura a 19 m de la Subestación Centro Histórico |
| Patronato de Bomberos Coahuila, Saltillo | Mismo punto que la Estación Norte |
| Coordinación Municipal de PC de Torreón | Fusionada con la Central Colón (65 m) |
| Estación de Ferrocarriles, Saltillo | No es bomberos |
| Oxxo Bomberos, Acuña | Tienda |
| "Bomberos Protección - Civil" `25.8315278,-103.2764013` | Nombre genérico, sin categoría ni teléfono. Probablemente Francisco I. Madero, sin confirmar |
| Gómez Palacio, Lerdo | Durango |
| Eagle Pass, Del Río, US Air Force | Texas |

### Municipios buscados sin resultado

Cuatro Ciénegas, Viesca, General Cepeda, Ocampo, Sierra Mojada, Nadadores, Abasolo,
Escobedo, Candela, Lamadrid, Sacramento, Progreso, Juárez, Guerrero, Hidalgo, Jiménez,
Villa Unión y Morelos. Se buscó y Maps no registra estación ni unidad de protección civil.

### Pendientes de Coahuila

- Reintentar el portal de la Subsecretaría de Protección Civil de Coahuila cuando
  responda: daría teléfonos para Monclova, Frontera, San Buenaventura y los municipios
  sin resultado.
- Teléfono directo de: Estación Poniente y Estación 6 de Saltillo, Central y Subestación
  de Monclova, Bomberos y Protección Civil de Ciudad Frontera, San Buenaventura,
  y las estaciones 2 y 3 de Acuña.
- San Pedro: aclarar si "Bomberos y Rescate Voluntarios de San Pedro" (872 120 3406,
  a 190 m de la central) es el patronato del mismo cuerpo o una agrupación aparte.

---

## Tamaulipas — agosto 2026

33 fichas en 18 municipios: Nuevo Laredo 5, Matamoros 5, Victoria 4, Tampico 3,
Ciudad Madero 2, Altamira 2, Reynosa 2, y una cada uno en Río Bravo, El Mante,
Miguel Alemán, Mier, San Fernando, Valle Hermoso, Soto la Marina, Xicoténcatl,
Llera y Aldama.

### Fuentes oficiales encontradas — las mejores hasta ahora

Tamaulipas resultó el estado mejor documentado del levantamiento. Dos fuentes oficiales,
ambas de la Coordinación Estatal de Protección Civil:

1. **Directorio de unidades municipales**
   (`tamaulipas.gob.mx/proteccioncivil/directorio/`): tabla con los **43 municipios**,
   nombre del director y teléfono de oficina. 28 municipios traen teléfono.
2. **PDF de teléfonos de emergencia**
   (`tamaulipas.gob.mx/proteccioncivil/.../telefonos-de-emergencias.pdf`): teléfonos
   separados de **bomberos y de protección civil** para los 8 municipios más poblados
   (Altamira, Cd. Madero, El Mante, Matamoros, Nuevo Laredo, Reynosa, Victoria y Tampico).

Ese cruce permitió publicar **11 fichas `verified: true`**, la proporción más alta de
cualquier estado hasta ahora. Los nombres de los directores municipales **no se publican**:
rotan cada trienio y quedarían obsoletos antes que cualquier otro campo.

### Discrepancias documentadas

| Municipio | Directorio oficial | Google Maps | Qué publicamos |
|---|---|---|---|
| Tampico | 833 305 2623 | 833 305 2624 | El oficial; parecen líneas del mismo conmutador |
| San Fernando (PC) | 841 842 3582 | 841 852 3582 | El oficial; difieren en un dígito |
| Xicoténcatl | 832 235 0004 | 832 265 0036 | El oficial; el otro queda anotado en la ficha |

### Registros descartados

| Registro | Motivo |
|---|---|
| Casa del Bombero, Tampico | Tienda de equipo de seguridad |
| El Bombero, Reynosa | Negocio |
| Terminal de Almacenamiento Pemex, Reynosa | Brigada industrial de empresa |
| Copa de Agua de los Bomberos, Matamoros | Torre de agua |
| DIF Municipal y Delegación de Policías, Victoria | No son bomberos |
| Despacho jurídico, Matamoros | Negocio que solo menciona a los bomberos en su dirección |
| Subdirección Regional San Fernando | Oficina administrativa estatal, sin teléfono ni categoría operativa |
| Brownsville, Laredo, McAllen, Mission, Pharr, Del Río | Texas |

### Municipios buscados sin resultado

Abasolo, Antiguo Morelos, Burgos, Bustamante, Camargo, Casas, Cruillas, Gómez Farías,
González, Guerrero, Güémez, Gustavo Díaz Ordaz, Hidalgo, Jaumave, Jiménez, Mainero,
Méndez, Miquihuana, Nuevo Morelos, Ocampo, Padilla, Palmillas, San Carlos, San Nicolás,
Tula y Villagrán. Se buscó en Maps y no aparece estación ni unidad con ficha propia,
aunque **14 de ellos sí tienen teléfono en el directorio estatal**: existen como unidad
municipal, pero sin registro geolocalizado.

### Pendientes de Tamaulipas

- Los 14 municipios con teléfono en el directorio estatal pero sin ficha en Maps
  (Abasolo, Camargo, Cruillas, Guerrero, Jaumave, Méndez, Miquihuana, Palmillas,
  San Carlos, Villagrán, entre otros): faltan domicilio y coordenadas para publicarlos.
- Nuevo Laredo: la **estación 2** no aparece en Maps pese a que la numeración de las
  otras cuatro la presupone.
- Teléfono directo de: Tampico Zona Centro y Colonia Roma, Bomberos Sagitario,
  Centro Regional de Reynosa, Matamoros estación 2 y las dos bases de Brigada Matamoros,
  y Nuevo Laredo estación 5.
- Aclarar si **Brigada Matamoros** es una agrupación voluntaria independiente o parte
  del cuerpo municipal.

---

## Baja California — agosto 2026

45 fichas en **los 7 municipios del estado**: Tijuana 19, Ensenada 11, Mexicali 8,
Playas de Rosarito 3, Tecate 2, San Quintín 1 y San Felipe 1. Es el primer estado
del levantamiento con cobertura municipal completa.

### La mejor fuente oficial hasta ahora

El portal de la **Dirección de Bomberos del Ayuntamiento de Tijuana**
(`bomberos.tijuana.gob.mx/central.aspx`) publica una tabla con las **19 estaciones**
del cuerpo —Central y estaciones 1 a 18— con domicilio, colonia y teléfono de cada una.
Ninguna otra fuente municipal del país nos había dado un listado tan completo.

Las 19 fichas de Tijuana van `verified: true` con domicilio y teléfono del portal
oficial. Google Maps solo registra 7 de esas estaciones, así que **12 se publican sin
coordenadas GPS**: preferimos una ficha sin mapa a una con el pin equivocado. El portal
además marca expresamente como "sin teléfono" a las estaciones 15 y 18, y así lo
publicamos.

El portal de Mexicali (`mexicali.gob.mx`) solo publica la dirección de la central. El
manual de organización de Ensenada y el anuario de COPLADEMM están bloqueados por robots.

### Ambigüedades resueltas

- **Tijuana, Playas.** El registro *Estación de Bomberos Playas* de Maps podía ser la
  estación 10 o la 14 (ambas en Playas de Tijuana). Su domicilio —P.º del Pedregal 56—
  y su teléfono —664 631 8996— coinciden exactamente con los que el ayuntamiento publica
  para la **estación 10**.
- **Tijuana, central.** Maps publica *Av. Alberto Aldrete 8205* y el teléfono
  664 688 5705; el ayuntamiento, *Av. Aldrete y Madero 8298* y 664 685 5555. Publicamos
  el dato oficial y anotamos el otro.
- **Fusiones por proximidad:** estación 13 / El Refugio en Tijuana, estación 8 / Zarco
  en el Valle de Guadalupe, central / dirección en Rosarito, estación / dirección en
  San Quintín, y central / dirección en San Felipe.

### Registros descartados

| Registro | Motivo |
|---|---|
| Cuerpo de Rescate de Ensenada A.C. | Grupo de rescate voluntario, no cuerpo de bomberos |
| Bomberos de Ensenada `31.8961,-116.5890` | Marcado **cerrado temporalmente** en Maps |
| ASIPONA (Bomberos), Ensenada | Brigada de la administración portuaria |
| Pro Bomberos Rosarito | Patronato; Maps ni siquiera lo categoriza como establecimiento |
| Oxxo Bomberos, hidrante, extinguidores, DP3, Sindicatura | No son estaciones |

### Pendientes de Baja California

- **Coordenadas GPS de 12 estaciones de Tijuana** (1, 3, 5, 6, 7, 9, 11, 14, 15, 16, 17
  y 18): el ayuntamiento publica sus domicilios, pero Maps no las registra. Habría que
  geolocalizarlas por domicilio con una fuente confiable.
- **Mexicali:** la numeración de sus estaciones llega al menos al 23, pero Maps solo
  registra 8. Falta una fuente oficial con el listado completo — el anuario de
  COPLADEMM podría tenerlo si se logra abrir.
- Teléfono directo de las estaciones 3 y 23 de Mexicali, la 2 y la Norte de Ensenada,
  Punta Banda, San Antonio de las Minas, Valle de Guadalupe y la subestación Club
  Rotario de Tecate.
- Confirmar la categoría de la estación Chapultepec de Ensenada, que Maps clasifica
  como institución educativa.

---

## Sonora — agosto 2026

58 fichas en **28 municipios**: San Luis Río Colorado 6, Hermosillo 6, Cajeme 5,
Guaymas 5, Nogales 4, Puerto Peñasco 4, Agua Prieta 3, Caborca 2, Empalme 2,
Navojoa 2, Santa Ana 2, y una ficha en cada uno de Álamos, Bacoachi, Bácum,
Baviácora, Benito Juárez, Cananea, Etchojoa, Huatabampo, Huépac, Magdalena, Naco,
Nacozari de García, Pitiquito, Plutarco Elías Calles (Sonoyta), San Ignacio Río
Muerto, San Miguel de Horcasitas (Pesqueira) y Ures.

Sonora es el primer estado del levantamiento donde la fuente oficial rindió poco y el
barrido de Maps por región cargó con casi todo el trabajo. **Solo 2 fichas quedaron
`verified: true`** —la central de Hermosillo y la Dirección de Protección Civil y
Bomberos Municipales de San Luis Río Colorado—, que son las dos únicas donde domicilio
y teléfono provienen de un portal oficial.

### Fuentes oficiales que sí funcionaron

- **`bomberosnogales.com.mx`** — sitio del H. Cuerpo de Bomberos Voluntarios de Nogales.
  Publica los teléfonos de sus seis estaciones numeradas con el prefijo 19
  (19-1 631 312 0836, 19-2 631 314 6320, 19-3 631 314 1858, 19-4 631 315 7862,
  19-5 solo 911, 19-6 en construcción), **pero sin domicilios**. Solo se pudieron
  asignar con certeza los teléfonos de la 19-1 (la central, que Maps duplica como
  "Fire Station #1") y de la 19-3 (que Maps nombra "Estación 3 Bomberos Nogales").
- **`pbh.com.mx`** — Patronato de Bomberos de Hermosillo. Da domicilio con CP
  (Calle Nuevo León s/n, Centro, 83000) y el teléfono 662 411 7954.
- **`sanluisrc.gob.mx`** — Dirección de Protección Civil de San Luis Río Colorado.
  Domicilio (Av. Juárez y calle Cuarta), teléfono 653 536 6642 y horario de ventanilla.
- **`navojoa.gob.mx`** — sección de Bomberos y Protección Civil. Teléfono 642 425 6300
  (conmutador del ayuntamiento) y correo `bomberos@navojoa.gob.mx`; el domicilio que
  publica es el del palacio municipal, no el del cuartel.

### Fuentes oficiales que fallaron

| Fuente | Qué pasó |
|---|---|
| `bomberoscajeme.mx` | **El dominio caducó y hoy aloja un portal de casas de apuestas en España.** Los resultados de búsqueda todavía apuntan a `localizacion.htm` y `contacto.htm`, pero el contenido de bomberos ya no existe. No usar |
| `proteccioncivil.sonora.gob.mx` | La ruta `/directorios/ubicaciones.html` que aparece indexada devuelve **404**; el portal actual solo publica los datos de la Coordinación Estatal (Av. Morelia 37, Centro, Hermosillo; 662 236 4407 oficinas y 662 236 4400 emergencias). **No hay directorio estatal de unidades municipales** |
| `guaymas.gob.mx` | Solo boletines de prensa de la sección Bomberos; ninguna página de estaciones |
| `heroicanogales.gob.mx` | El directorio municipal no desglosa estaciones de bomberos |

### Ambigüedades resueltas

- **Vícam.** Su estación aparece en Maps como "Vícam, Sonora", sin municipio. Vícam es
  cabecera de los ocho pueblos yaquis pero **no es municipio**: es localidad de Guaymas.
  Se publicó con `municipality: Guaymas`, `city: Vícam`.
- **Álamos.** Maps registra dos puntos de la misma corporación sobre la calle Francisco
  I. Madero —"Dirección de Bomberos y Protección Civil" en el 85 y "Bomberos Álamos" en
  el 51—, con las coordenadas separadas 1.5 km. Álamos tiene un solo cuerpo de bomberos:
  se publicó **una sola ficha**, con el registro que trae domicilio completo, CP 85760 y
  teléfono, y la reserva anotada en la tabla de fuentes.
- **Subestación 3 de Cajeme.** Maps publica el teléfono a 7 dígitos (417 0904). Se le
  antepuso la LADA 644 de Ciudad Obregón, que coincide con el conmutador de la central,
  y la reserva quedó anotada en la ficha.
- **Sonoyta.** El teléfono publicado (953 111 2869) tiene clave de Oaxaca, no la 651 de
  la región. Se publicó como *Verificado con reserva*, explicando que parece una línea
  móvil registrada en otro estado.
- **Comisión Nacional de Emergencia Empalme.** Se revisó su ficha antes de decidir: Maps
  la clasifica como parque de bomberos y las fotos del propietario muestran unidad y
  personal de bomberos, con sede propia en la colonia Sahuaral. Se incluyó como cuerpo
  **voluntario**, no como grupo privado de rescate.
- **Fusiones por proximidad (<150 m):** central de Hermosillo / Patronato de Bomberos
  (25 m, mismo predio de calle Nuevo León); subestación 3 de Cajeme / "USSI Sur" (10 m,
  misma calle Michoacán); cuartel central de Navojoa / "Estación de Bomberos" (5 m,
  Av. López Rayón 209); Huatabampo, Francisco I. Madero 112 / 95 (10 m); cuartel 2 de
  Agua Prieta / "H. Cuerpo de Bomberos" (8 m, calle 23); estación 19-1 de Nogales /
  "Fire Station #1" (2 m); Dirección de PC y Bomberos de SLRC / "Estación Central de
  Bomberos Voluntarios" (52 m, esquina de Juárez y calle 4-5).

### Registros descartados

| Registro | Coordenadas | Motivo |
|---|---|---|
| SSEI, Hermosillo | `29.0918,-111.0495` | Servicio de salvamento y extinción de incendios **interno del aeropuerto**; sin domicilio ni teléfono públicos y sin atención al público |
| Bomberos de la Costa A.C. | `29.0384,-110.9593` | Registro **inconsistente**: pin en Hermosillo pero CP 83600, LADA 637 y sitio web `caborcasonora.gob.mx`, todos de Caborca. No se pudo resolver el municipio. Teléfono publicado: 637 114 4565 |
| "Estación De Bomberos" al suroeste de SLRC | `32.3786,-114.8692` | Sin domicilio, CP ni teléfono; la coordenada cae cerca del límite **Sonora / Baja California** en el delta del Colorado y no se pudo resolver el municipio |
| "Bomberos", Ejido Hermosillo | `32.5122,-114.9184` | Maps confirma **Ejido Hermosillo, Baja California** (municipio de Mexicali); cayó en el viewport de SLRC |
| Nogales Fire Department Station 1 | `31.3454,-110.9314` | Nogales, **Arizona** |
| Douglas Fire Department | `31.3448,-109.5403` | Douglas, **Arizona** |
| Sunnyside Fire Department | `31.3675,-109.5279` | Cochise County, **Arizona** |
| Pirtleville Fire District | `31.3597,-109.5684` | Cochise County, **Arizona** |
| Sindicato Único de Bomberos del Ayuntamiento de Hermosillo | `29.1035,-110.9630` | Local sindical, no estación |
| "bomberos" (categoría Urbanización), Hermosillo | `29.0955,-110.9429` | No es establecimiento; Maps lo clasifica como urbanización |
| Los Bomberos, Ciudad Obregón | `27.4849,-109.9350` | Taquería |
| EXTINSON, Ciudad Obregón | `27.4914,-109.9455` | Empresa privada de seguridad contra incendios |
| OXXO Bomberos, Agua Prieta | `31.3163,-109.5572` | Tienda de conveniencia |
| Canal Las Pilas, Navojoa | `27.1390,-109.3851` | Canal de riego |
| Registros de CDMX y Edomex en el feed | varias | Relleno de Maps cuando la zona buscada no tiene resultados |

### Municipios buscados sin resultado

Barridos por nombre a 9-10z que **no devolvieron ninguna estación**: Sahuaripa, Yécora,
Bacanora, Nácori Chico, Huásabas, Granados, Moctezuma, Cumpas, Fronteras, Bavispe,
Arizpe, Quiriego, Rosario Tesopaco y Altar. En esos casos Maps rellenó el feed con
resultados de la Ciudad de México, señal de que no hay registro local.

### Pendientes de Sonora

- **Hermosillo:** el municipio numera al menos seis estaciones y la prensa local reporta
  una séptima en construcción en la salida a Nogales. Maps solo registra la central, la
  2, la 4, la Sur, la 5 de Miguel Alemán y Bahía de Kino. Faltan localizar la 3 y la 6.
- **Nogales:** faltan domicilios oficiales para las seis estaciones numeradas. Dos
  registros de Maps —Callejón Hermosillo 1317 y la colonia San Carlos— quedaron **sin
  teléfono** porque no se pudo determinar a qué número de estación corresponden. La
  estación 4 (San Miguel), que tiene página propia en Facebook, no aparece en Maps.
- **Cajeme:** confirmar si "USSI Sur" es una unidad distinta que comparte inmueble con
  la subestación 3.
- **Guaymas y Empalme:** ninguna de las dos corporaciones publica portal propio; los
  teléfonos vienen todos de Maps.
- **Sin teléfono publicado:** 22 fichas, la mayoría de municipios chicos y de las
  estaciones secundarias de Cajeme, Guaymas, Nogales, Peñasco y SLRC.
- Colonia y código postal siguen pendientes en la mayoría de las fichas: Maps rara vez
  los publica en Sonora y no hay directorio estatal que los aporte.

---

## Sinaloa — agosto 2026

35 fichas en **14 municipios**: Mazatlán 8, Culiacán 7, Ahome 6, Guasave 2, El Fuerte 2,
Escuinapa 2, y una ficha en cada uno de Angostura, Badiraguato, Choix, Elota (La Cruz),
Mocorito, Navolato, Salvador Alvarado (Guamúchil) y Sinaloa (Sinaloa de Leyva).

**Ninguna ficha quedó `verified: true`.** Es el primer estado del levantamiento en el que
no se localizó una sola fuente oficial vigente con domicilio y teléfono: los tres cuerpos
grandes son patronatos civiles sin portal activo y el estado no publica directorio de
unidades municipales de protección civil. Todas las fichas se sostienen en el registro
público del establecimiento en Google Maps y así queda dicho en cada tabla de fuentes.

Rasgo del estado: los tres cuerpos principales —Culiacán, Mazatlán y Los Mochis— son
**patronatos civiles**, no direcciones del ayuntamiento, y en las tres ciudades convive
además una corporación separada de **Bomberos Veteranos** constituida como asociación
civil, con base propia y, en Mazatlán y Ahome, con destacamentos fuera de la cabecera.
Eso obliga a distinguir dos corporaciones por ciudad, no a fusionarlas.

### Fuentes oficiales que fallaron

| Fuente | Qué pasó |
|---|---|
| `bomberosculiacan.org.mx` | Dominio vivo pero **el hosting expiró**: solo devuelve el aviso de renovación del proveedor. No hay contenido de estaciones |
| `proteccioncivil.sinaloa.gob.mx/p/coordinaciones-municipales-de-proteccion-civil` | La página existe pero el directorio está publicado **solo como imágenes**, sin texto ni PDF descargable. No aporta domicilios ni teléfonos legibles |
| `web.pcsinaloa.gob.mx/directorio/` | Directorio del Instituto Estatal: solo nombres y cargos de mandos estatales. **Sin teléfonos, sin domicilios y sin coordinaciones municipales** |
| `proteccioncivil.gob.mx` — «Servicios de emergencia Sinaloa» | PDF federal **de noviembre de 2012**, bloqueado por robots y anterior a la homologación a 10 dígitos de 2019. Descartado por obsoleto aun si se hubiera podido abrir |
| `tics.mazatlan.gob.mx/tourist/es/emergencia` | Portal turístico municipal: remite todo a Contacto Ciudadano (669 986 8126) y al 911; **no publica datos de bomberos ni de protección civil** |
| `ahome.gob.mx/.../proteccion-civil.pdf` | PDF sin capa de texto; no se pudo extraer nada |
| Directorio nacional de CMPC alojado en `upbicentenario.edu.mx` | Contiene únicamente los 46 municipios de Guanajuato; **no incluye Sinaloa** |

No se usó `bombero.mx` ni `firefighter.mx`, y se verificó que ningún dominio abierto
fuera un dominio caducado reutilizado, como pasó en Sonora con `bomberoscajeme.mx`.

### Ambigüedades resueltas

- **La Constancia.** El registro «Bomberos Veteranos Voluntarios La Constancia A.C.»
  (`25.9657917,-108.903786`) no trae municipio. Maps solo devuelve «Constancia, Sinaloa».
  La localidad **no existe en el catálogo de localidades de Ahome**, sí en el de El Fuerte
  (Constancia, ~6,800 habitantes), y la LADA 698 del teléfono es la de El Fuerte y Choix,
  no la 668 de Los Mochis. Se publicó con `municipality: El Fuerte`, `city: Constancia`.
- **«Bomberos de Los Mochis» cerca de la villa de Ahome** (`25.9182748,-109.1625945`).
  Publica el **mismo domicilio y el mismo teléfono** (Marcial Ordóñez s/n, 668 812 0100)
  que la estación central de Los Mochis, 20 km al sur. Error de geocodificación: se
  descartó y se anotó en la ficha de la central.
- **Los cuatro registros del mismo cuartel de Los Mochis.** «Bomberos» (Degollado s/n),
  «Dpto central, Bomberos» (Degollado y Marcial Ordóñez), «Patronato de Administración
  del HC Vol de Bomberos de los Mochis» y «Heroico Cuerpo Voluntario de Bomberos» apuntan
  a la misma esquina con geocodificación dispersa (30 m, 730 m y 1.1 km). Se publicó
  **una sola ficha**, la de la central, con los cuatro registros documentados.
- **Patronato de Guamúchil.** El «Patronato de Administración del Cuerpo de Bomberos»
  (`25.4578855,-108.0588357`) está a 1.5 km de la estación pero **comparte el teléfono
  673 732 1027**. Es la oficina administrativa de la misma corporación: se fusionó en la
  ficha de la estación y la segunda dirección quedó anotada, no se abrió ficha aparte.
- **Estación 2 de Mazatlán.** Maps publica «El Quelite» como vialidad del domicilio. **No
  es la localidad de El Quelite**, al norte del municipio: la coordenada cae en Villa
  Florida, dentro de la ciudad. Se publicó con la reserva anotada.
- **Estación Central de Mazatlán.** Dos registros en el mismo punto (2 m) con distinto
  número exterior sobre Av. Insurgentes, 72 y 4245. Se fusionaron y se publicó el 72,
  con la discrepancia anotada en la tabla de fuentes.
- **Protección Civil de Mazatlán.** Dos registros distintos a 2.5 km: Juan Escutia 602
  (669 239 2533) y Av. Luis Donaldo Colosio esq. Toledo Corro, Huertos Familiares, CP
  82155 (669 132 8651). Se publicó **una sola ficha**, la del domicilio con CP, y el
  segundo registro quedó documentado con teléfono y coordenadas.
- **Bomberos Navolato.** El pin (`24.757479,-107.6793613`) está sobre la carretera a
  Culiacán, en La Arrocera, y Maps lo ubica en **General Ángel Flores, CP 80372**, no en
  la cabecera. Se publicó con `municipality: Navolato`, `city: General Ángel Flores`.
- **Fusiones por proximidad (<150 m):** Estación 1 de Mazatlán / «Central De Bomberos»
  (30 m, Av. Gabriel Leyva 1935); estación central de Los Mochis / «Dpto central,
  Bomberos» (30 m, Degollado y Marcial Ordóñez); H. Cuerpo de Bomberos de Choix /
  «Protección civil Choix» (7 m, mismo predio, se publicó como una sola corporación).

### Registros descartados

| Registro | Coordenadas | Motivo |
|---|---|---|
| Bomberos Amigos I.A.P., Culiacán | `24.8046696,-107.4039138` | Registro **inconsistente**: publica el domicilio de la Estación 1 (Gabriel Leyva Solano 444 Ote.) pero con la coordenada a 1.5 km y teléfono 687 713 4533, con LADA de Guasave. No se pudo resolver si es una segunda base o un duplicado mal geocodificado |
| «Estación de Bomberos Costa Rica» | `24.5923103,-107.3952714` | Segundo registro en Costa Rica a 1.3 km de la Estación 4, con domicilio y teléfono distintos (San Rafael 43, 667 581 3256). Con dos estaciones en una sindicatura de ese tamaño no se pudo confirmar cuál está vigente; se publicó solo la numerada |
| «Bomberos» al oriente de Los Mochis | `25.8146893,-108.9350984` | Pin **sin domicilio, sin teléfono, sin horario y sin reseñas**; no hay nada que verificar |
| «Bomberos de Los Mochis», villa de Ahome | `25.9182748,-109.1625945` | Duplicado geocodificado de la central de Los Mochis (mismo domicilio y mismo teléfono, 20 km de distancia) |
| «proteccion civil delegacion choix» | `26.7110878,-108.3245726` | Maps lo marca **cerrado permanentemente** |
| Base de Bomberos y Emergencias del Valle «Don José Bedolla» CNERNC A.C. | `22.7452545,-105.8603825` | Isla del Bosque, Escuinapa. **Sin categoría, sin domicilio y sin teléfono**; no se pudo confirmar que sea un cuerpo de bomberos y no un grupo de rescate |
| Oficina de Bomberos Veteranos Voluntarios de La Constancia | `25.9680861,-108.8979877` | Oficina administrativa de la misma A.C., a 700 m de la base; documentada en su ficha |
| Taquería Los Bomberos, Culiacán | `24.8033476,-107.3891013` | Negocio |
| Tacos los bomberos, Culiacán | `24.8390242,-107.3943426` | Negocio |
| Taquería los bomberos, Guasave | `25.5645591,-108.4754892` | Negocio |
| Construnavo, Navolato | `24.7578413,-107.6756421` | Ferretería |
| Río Évora, Angostura | `25.3662668,-108.1471553` | Parque público |
| Registros de CDMX y Edomex en el feed | varias | Relleno de Maps cuando la zona buscada no tiene resultados |

### Municipios buscados sin resultado

Barridos a 11-14z centrados en la cabecera que **no devolvieron ninguna estación ni
unidad de protección civil**: **El Rosario**, **Concordia**, **San Ignacio** y
**Cosalá**. En los cuatro casos Maps devolvió la presidencia municipal o rellenó el feed
con resultados de la Ciudad de México. Tampoco aparecieron estaciones en **Topolobampo**
(pese al puerto de altura y la termoeléctrica), ni en las sindicaturas de **Eldorado** y
**Quilá**, en Culiacán, ni en **Higuera de Zaragoza**, en Ahome.

### Pendientes de Sinaloa

- **Verificación oficial de los tres patronatos.** Culiacán, Mazatlán y Los Mochis
  administran el servicio por patronato y ninguno tiene portal vigente. Vale la pena
  reintentar `bomberosculiacan.org.mx` más adelante, por si renuevan el hosting.
- **Directorio estatal.** El de Protección Civil de Sinaloa está publicado como imagen.
  Si aparece una versión en texto o PDF, subiría a `verified: true` buena parte de las
  35 fichas de golpe.
- **Sin teléfono publicado:** 10 fichas — Bomberos Veteranos de Culiacán, El Castillo,
  Villa Unión, Estación Macario Gaxiola y Estación Poniente de Los Mochis, Protección
  Civil de Ahome, Sinaloa de Leyva, Badiraguato, Choix y los Bomberos Voluntarios de
  Escuinapa.
- **Sin domicilio publicado:** 4 fichas — El Carrizo, Sinaloa de Leyva, Choix y Elota.
  En las cuatro, Maps solo aporta coordenadas (y código postal en Sinaloa de Leyva y Elota).
- **Cuatro municipios sin cobertura.** El Rosario, Concordia, San Ignacio y Cosalá tienen
  cabecera y cuerpo de emergencia, pero no hay registro público que los respalde. Habría
  que buscarlos por prensa local o por el ayuntamiento.
- **Costa Rica, Culiacán.** Resolver cuál de los dos registros es la estación vigente.
- Colonia y código postal siguen pendientes en la mayoría de las fichas: Maps casi no los
  publica en Sinaloa y no hay directorio estatal que los aporte.

---

## Baja California Sur — agosto 2026

22 fichas en **los 5 municipios del estado**, cobertura completa: Los Cabos 9
(Cabo San Lucas 4, San José del Cabo 4, Santiago 1), La Paz 5 (La Paz ciudad 3,
Todos Santos 1, El Centenario 1), Mulegé 4 (Santa Rosalía, Heroica Mulegé,
Guerrero Negro, San Ignacio), Loreto 2 y Comondú 2 (Ciudad Constitución).

**11 fichas quedaron `verified: true`**, todas por teléfono de fuente oficial: el
directorio de emergencias por municipio del Gobierno del Estado, el directorio de
números de emergencia del Ayuntamiento de Los Cabos y los sitios propios de tres
corporaciones (Cabo San Lucas, San José del Cabo y El Centenario).

Rasgo del estado: **pocos municipios pero enormes**. Mulegé solo tiene más de 33 mil km²
—más que varios estados del país— y sus cuatro estaciones están separadas por cientos de
kilómetros de carretera transpeninsular, sin apoyo cercano posible. Eso, más la
temporada de ciclones del Pacífico que entra de frente por el sur de la península, es lo
que define el trabajo de estas corporaciones y así se redactó el contexto de cada ficha.
Los dos cuerpos grandes de Los Cabos —Cabo San Lucas y San José del Cabo— son
**voluntarios**, no direcciones del ayuntamiento, y cada uno mantiene su propio sitio y
su propio conmutador.

### Fuentes oficiales que funcionaron

| Fuente | Qué aportó |
|---|---|
| `bcs.gob.mx/ciclones-tropicales-2024/inicio-ciclones-trop/` | **La mejor fuente del estado.** Directorio de emergencias por municipio con teléfonos de bomberos de La Paz (165 4343 / 122 0054), Los Cabos (624 143 3577), Comondú (613 132 0955), Loreto (613 135 1566) y Protección Civil de Guerrero Negro (615 159 8969) |
| `loscabos.gob.mx/numeros-emergencia/` | Teléfonos de bomberos y protección civil por localidad: CSL 624 143 3577, SJC 624 142 2466, PC municipal 624 143 5123 / 624 143 9120, PC San José 624 142 3748 / 624 142 0067 |
| `bomberoscsl.com` (sitio propio) | Fundación en 1982, 60 elementos activos, **listado de estaciones** (El Médano, Lomas del Sol y Jacarandas en obra) y los tres teléfonos del cuerpo |
| `bomberossjc.com` (sitio propio) | Domicilio de la central, teléfono 624 189 1082 y **cobertura declarada**: del arroyo El Tule al poblado de Santiago, con dos estaciones operativas (Centro y El Zacatal) |
| `ecbomberos.com` (sitio propio) | Nombre, domicilio (Calle Seis y Palo Escopeta 901) y teléfono (612 296 8780) del cuerpo voluntario de El Centenario, más su cobertura del Sector 6 (El Centenario y Chametla) |
| `lapaz.gob.mx/catalogo-tramites-servicios/0001` | Domicilio y teléfono (612 123 7900) de la Dirección de Protección Civil municipal, que comparte el complejo de Donceles 28 con la estación central de bomberos |
| `loscabos.gob.mx` (boletines) | Volumen de operación de los bomberos de San José del Cabo: 866 emergencias en el primer trimestre de 2026 |

### Fuentes que fallaron

| Fuente | Qué pasó |
|---|---|
| `guerreronegro.org/bomberos.html` | **Dominio caducado reutilizado**: hoy es un sitio de reseñas de casinos en azerbaiyano. Exactamente el caso de `bomberoscajeme.mx` en Sonora. Descartado |
| `lapaz.gob.mx/directorio` | El directorio del ayuntamiento **no lista** la Dirección de Bomberos ni la de Protección Civil |
| `sgg.bcs.gob.mx/proteccioncivil/` | Página de la Subsecretaría estatal **sin domicilio propio ni teléfonos**; solo remite al domicilio general de la Secretaría General de Gobierno |
| Portal municipal de Comondú, Mulegé y Loreto | No se localizó portal con sección de bomberos o de protección civil con datos de contacto |

No se usó `bombero.mx` ni `firefighter.mx`.

### Ambigüedades resueltas

- **El Centenario, dos registros con teléfonos distintos.** Maps publica «Bomberos
  Centenario» (`24.1061728,-110.4273491`, 612 452 0003) y «Bomberos Voluntarios De El
  Centenario» (`24.1053477,-110.42035`, 612 142 2940), separados unos 700 m —fuera de la
  regla de fusión de 150 m—. El sitio propio de la corporación (`ecbomberos.com`) resolvió
  el caso: hay **un solo cuerpo**, con domicilio en Calle Seis y Palo Escopeta 901 y
  teléfono 612 296 8780. La intersección Calle Seis y Palo Escopeta cae a ~35 m del primer
  registro. Se publicó una ficha con el dato oficial y los dos teléfonos de Maps quedaron
  documentados en la nota de la ficha.
- **Estación El Zacatal, marcada «cerrado temporalmente» en Maps.** El sitio del propio
  Departamento de Bomberos de San José del Cabo la enumera como **una de sus dos
  estaciones en operación**. Se publicó por jerarquía de fuente, con la discrepancia
  anotada de forma explícita en la ficha.
- **«Unidad de Protección Civil», Sierra de la Victoria 138, La Paz** (`24.1146167,-110.3142093`,
  612 121 3214). No se pudo determinar si es la unidad **estatal o la municipal**: el sitio
  web que declara es el federal `proteccioncivil.gob.mx`, el teléfono no coincide ni con el
  de PC Estatal (122 9008) ni con el de PC Municipal (121 3634) del directorio estatal, y el
  domicilio no aparece en ningún portal oficial. **Se excluyó.** La Dirección de Protección
  Civil municipal sí quedó documentada, como teléfono administrativo de la ficha de la
  estación central, con el domicilio que publica `lapaz.gob.mx` (Donceles 28, el mismo
  complejo de la estación).
- **Santa Rosalía, dos registros en el mismo punto.** «bomberos de santa rosalia»
  (Av. Manuel F. Montoya 17) y «H.Cuerpo De Bomberos Y Rescate» (Emilio Carranza) están a
  menos de 5 m. Fusionados en una ficha.
- **Mulegé, dos registros a ~150 m.** «Cuartel de Bomberos» (`26.8909176,-111.9825808`) y
  «Heroico Cuerpo de Bomberos Voluntarios» (`26.890594,-111.981083`, calle Gral. Martínez).
  Misma corporación. Fusionados.
- **La Paz, sub-estación Eco-01.** «Sub-Estación de bomberos Eco-01 Navarro Ruibio» y
  «H. Cuerpo de Bomberos. Col. Navarro Rubio» comparten coordenada exacta y domicilio
  (República 1625). Fusionados.
- **Cabo San Lucas, protección civil.** «Protección Civil Cabo San Lucas» y «Coordinacion
  de Proteccion Civil», ambos sobre calle Constituyentes y con el mismo teléfono
  (624 143 9120). Fusionados.
- **Teléfonos a 7 dígitos de La Paz.** El directorio estatal publica 165 4343 y 122 0054
  sin LADA. Se les antepuso la clave 612 de La Paz y la reserva quedó anotada en la ficha.

### Registros descartados

| Registro | Coordenadas | Motivo |
|---|---|---|
| ANCLA SEGURIDAD INDUSTRIAL, La Paz | `24.1412268,-110.3049965` | Negocio de seguridad, no cuerpo de bomberos |
| La Montaña, La Paz | `24.1059724,-110.307882` | Edificio de apartamentos; apareció por proximidad |
| Campo de Entrenamiento — Departamento de Bomberos San José del Cabo | `23.0858658,-109.7155961` | Academia y campo de entrenamiento, no estación operativa |
| BOMBEROS Y RESCATES SAN IGNACIO | `27.3019785,-112.8949139` | Registrado como «oficinas de empresa» en la localidad de **San Lino**, y la única actualización de visitantes describe una cancha deportiva. Pin no confiable |
| Unidad de Protección Civil, Sierra de la Victoria 138, La Paz | `24.1146167,-110.3142093` | Ambigüedad estatal/municipal sin resolver (ver arriba) |

### Localidades buscadas sin resultado

Puerto San Carlos, Ciudad Insurgentes y Villa Ignacio Zaragoza (Comondú); Vizcaíno,
Bahía Asunción y Bahía Tortugas (Mulegé); Los Barriles, Los Planes, El Sargento y
La Ventana (La Paz); Cabo Pulmo, La Ribera y Miraflores (Los Cabos); El Pescadero
(La Paz). **Ninguna tiene registro público de estación de bomberos ni de unidad
municipal de protección civil.** Se hicieron barridos dedicados por zona en cada caso.

### Pendientes

- **Guerrero Negro:** conseguir el teléfono directo de la estación de bomberos. El
  directorio estatal solo publica el de Protección Civil de la localidad (615 159 8969).
- **Estación Manuel Basauri, Cabo San Lucas** (`22.9653441,-110.0131942`): no figura en el
  listado de sedes del cuerpo voluntario de CSL (El Médano, Lomas del Sol, Jacarandas).
  Confirmar a qué corporación pertenece y si es la estación de Jacarandas ya terminada.
- **San Ignacio:** la ficha pública no da calle, número ni teléfono. Buscar por
  ayuntamiento de Mulegé o prensa local.
- **Estación Jacarandas, Cabo San Lucas:** el cuerpo la reporta en obra. Verificar si ya
  entró en operación y con qué domicilio.
- **Comondú:** el directorio estatal no publica teléfono de la Dirección de Protección
  Civil municipal ni de ninguna localidad fuera de Ciudad Constitución.
- Colonia y código postal siguen pendientes en las fichas de Santiago y Manuel Basauri:
  Maps no publica calle ni número en ninguna de las dos.

---

## Nayarit — agosto 2026

19 fichas en 11 de los 20 municipios: Bahía de Banderas 4 (Bucerías, Nuevo Nayarit,
La Cruz de Huanacaxtle, Punta de Mita), Tepic 3 (base central estatal, unidad municipal
y sub-estación Topacio), Compostela 3 (cabecera, Rincón de Guayabitos y Las Varas),
San Blas 2 (base regional estatal y unidad municipal), y una cada uno en Xalisco,
Santiago Ixcuintla, Tuxpan, Ruíz, Acaponeta, Huajicori e Ixtlán del Río.

**1 ficha quedó `verified: true`**: la base central del estado en Tepic, única con
domicilio y teléfonos publicados por fuente oficial estatal.

Rasgo del estado: en Nayarit **el servicio de bomberos lo presta el gobierno del
estado**, no los ayuntamientos. La Dirección General de Protección Ciudadana y Bomberos
opera una base central en Tepic y seis bases regionales —Acaponeta, San Blas, Rincón de
Guayabitos, Nuevo Nayarit, La Cruz de Huanacaxtle e Ixtlán del Río—, y los municipios
mantienen unidades de protección civil que en la mayoría de los casos no tienen equipo
de bombero propio. El propio Programa Red de Protección Civil del estado lo dice: solo
Tepic y Compostela cuentan con estructura municipal con personal y algo de equipo. Eso
se reflejó en el `serviceType` de cada ficha: `profesional` para las bases estatales,
`proteccion-civil` para las unidades municipales.

Los tres frentes geográficos del estado quedaron escritos en el contexto de las fichas:
la **Riviera Nayarit** en Bahía de Banderas y Compostela, con población flotante que
multiplica a la fija, rescate acuático real y carretera federal 200 saturada de carga;
la **llanura agrícola de Santiago Ixcuintla, Tuxpan y Ruíz**, con tabaco, caña y frijol,
quemas de esquilmos en la seca y crecidas de los ríos Santiago y San Pedro en el
temporal; y la **sierra huichola de Del Nayar y La Yesca** más el norte de Huajicori,
sin ninguna corporación registrada. San Blas se documentó como puerto histórico y zona
de estero y manglar. Toda la costa entra en temporada de ciclones del Pacífico de junio
a noviembre.

### Fuentes oficiales que funcionaron

| Fuente | Qué aportó |
|---|---|
| `tramites.nayarit.gob.mx/ciudadano/ficha/6` | **La mejor fuente del estado.** Domicilio, horario («lunes a domingo las 24:00 horas, solo emergencias») y los tres teléfonos oficiales de la Dirección General de Protección Ciudadana y Bomberos: 311 133 0369, 311 133 0381 y 311 213 1607 |
| `transparencia.nayarit.gob.mx` (ficha de la Dirección del Heroico Cuerpo de Bomberos) | Domicilio de la base central y **listado de las seis bases regionales**: Acaponeta, San Blas, Rincón de Guayabitos, Cruz de Huanacaxtle, Nuevo Nayarit e Ixtlán del Río. Es la única fuente que confirma la base de Ixtlán |
| `iplanay.gob.mx` — Programa de Red de Protección Civil (Periódico Oficial del Estado, 30 sep 2019) | Estructura completa: base central con 42 elementos y 7 unidades, Acaponeta con 20 y 4, San Blas con 10, Guayabitos con 15 y 5, Nuevo Vallarta con 15 y 5, Cruz de Huanacaxtle con 15 y 3. También el reconocimiento explícito de que apoyan a Puerto Vallarta, Jalisco, y de que solo Tepic y Compostela tienen estructura municipal |
| `compostela.gob.mx/directorio/` | Domicilio oficial de la Dirección General de Protección Civil de Compostela: Hidalgo #480 interior Unidad Deportiva. Coincide exactamente con la ficha de Maps |
| `sanblasnayarit.gob.mx/directorio/` | Confirma la existencia de la Dirección de Protección Civil municipal de San Blas y el conmutador del ayuntamiento (323 114 1412), sin línea directa |
| `transparencia.bahiadebanderas.gob.mx` | Confirma la Dirección de Protección Civil y Bomberos de Bahía de Banderas y su estructura de coordinaciones (incluye Coordinación de Salvamento Acuático) |
| Tribuna de la Bahía (prensa local) | Anuncio de la propia Dirección de Bahía de Banderas: nueva línea de emergencias **329 298 3650**, traslado de la base de Jarretaderas a la Unidad Deportiva de Bucerías, y baja de los números 322 113 3255 y 322 113 3256 |

### Fuentes que fallaron

| Fuente | Qué pasó |
|---|---|
| `tepic.gob.mx` | El portal del ayuntamiento **no publica directorio de dependencias**: la página es un cascarón JS con solo el domicilio de presidencia y el número de denuncias |
| `santiago-ixcuintla.gob.mx` | Detrás de una **verificación anti-robots** permanente; no se pudo leer en ningún intento |
| `bahiadebanderas.gob.mx/x/docs/proteccion_civil/Atencion_y_Respuesta_a_Emergencias.pdf` | El PDF de atención y respuesta a emergencias que aparece indexado devuelve **404**; el dominio además tiene la cadena SSL incompleta |
| `ssypc.nayarit.gob.mx/directorio/` | El directorio de la Secretaría de Seguridad y Protección Ciudadana está **vacío** |
| `ieenayarit.org` — directorios municipales | Los PDF por municipio son **escaneos sin capa de texto** y no incluyen protección civil ni bomberos |
| `ceja207.wixsite.com/pcnayarit` | Sitio en Wix titulado «Proteccion Civil y Bomberos Nayarit» con una página de «Bases Regionales». **No es dominio oficial** y no publica un solo domicilio ni teléfono: solo fichas geográficas de los municipios. Descartado como fuente |

No se usó `bombero.mx` ni `firefighter.mx`. Se aplicó la verificación de dominios
caducados a todos los portales consultados; ninguno resultó secuestrado en este estado.

### Ambigüedades resueltas

- **El límite Puerto Vallarta (Jalisco) – Bahía de Banderas (Nayarit).** Google Maps
  mezcla las dos entidades en cualquier barrido de la bahía. El criterio aplicado fue el
  **río Ameca**: al sur es Jalisco, al norte es Nayarit. Cada registro dudoso se resolvió
  abriendo su ficha y leyendo el estado y el Código Plus, no por latitud, porque el
  Ameca corre al nororiente y el límite no es una paralela. Quedaron **fuera de Nayarit**
  la Base 3 Ixtapa (`20.7124156,-105.2135806`, C. Colima 155, CP 48280 Ixtapa, **Jal.**),
  la base 4 Las Palmas (`20.8240477,-105.1034085`, Javier Mina 322, CP 48260 Las Palmas
  de Arriba, **Jal.**) —que está más al norte que Bucerías y aun así es Jalisco— y las
  cuatro estaciones de Puerto Vallarta ya publicadas en el estado de Jalisco. Quedaron
  **dentro de Nayarit** Nuevo Nayarit (CP 63735), Bucerías (CP 63732), La Cruz de
  Huanacaxtle (CP 63734) y Punta de Mita (CP 63727).
- **Bahía de Banderas, la base de Jarretaderas.** Maps conserva «Protección Civil y
  Bomberos Bahía de Banderas» (`20.6971046,-105.2677134`, Carretera Federal S/N
  Jarretaderas, 322 113 3255) marcada como cerrada permanentemente. El anuncio de la
  propia corporación explica el caso: **se mudó a la Unidad Deportiva de Bucerías** y
  dio de baja esos números. Se publicó la sede nueva y el registro viejo quedó
  documentado en la ficha.
- **San Blas, dos registros de la base estatal a ~170 m.** «Proteccion Civil Y Bomberos
  Del Estado» (`21.5289209,-105.2839819`, Playa del Borrego 19, 323 258 0079) y
  «Direccion de Protección Civil y Bomberos De Nayarit» (`21.5303906,-105.2836692`,
  calle Vallarta 7). La distancia rebasa por poco la regla de fusión de 150 m, pero el
  programa estatal documenta **una sola base** en el municipio. Fusionados, con el
  segundo registro anotado en la ficha. La unidad municipal (Clavel 359, a un kilómetro)
  sí es corporación distinta y va en ficha aparte.
- **Tepic, base central y «Sistema Nacional de Protección Civil».** Los dos puntos
  (`21.4864935,-104.8774413` y `21.4864351,-104.877456`) están a menos de 10 m y
  comparten el teléfono oficial 311 133 0369. Fusionados.
- **Tepic, tres colonias y tres códigos postales para la misma base.** Transparencia
  estatal dice Col. Burócratas Federal CP 63156; el registro de trámites dice Col. Ciudad
  del Valle CP 63157; Maps dice Los Llanitos CP 63176. Se publicó **solo la calle** y la
  discrepancia quedó anotada en la ficha.
- **Huajicori.** La ficha «Dirección de Protección Civil» (`22.637125,-105.3201486`) no
  cae sobre ninguna cabecera conocida. Se resolvió por Código Plus: **JMPH+RW Huajicori,
  Nayarit**, calle Abasolo, Centro, CP 63480.
- **Rincón de Guayabitos.** Maps geocodifica la base regional dentro del código postal
  63724 de **La Peñita de Jaltemba**, la localidad contigua. Ambas están en el municipio
  de Compostela, así que no hay ambigüedad municipal; se publicó como Rincón de
  Guayabitos, que es el nombre oficial de la base, con el CP anotado.
- **Las Varas y Punta de Mita, adscripción.** Ninguna de las dos aparece en el listado
  estatal de bases regionales. Se atribuyeron a las direcciones municipales de Compostela
  y de Bahía de Banderas respectivamente, con la reserva anotada en cada ficha.
- **Teléfono 322 168 6205 de Las Varas.** La clave 322 es de Puerto Vallarta, no de Las
  Varas (327). Se publicó como verificado con reserva por ser plausiblemente una línea
  móvil, con la observación explícita en la ficha.

### Registros descartados

| Registro | Coordenadas | Motivo |
|---|---|---|
| PROTECCIÓN CIVIL Y BOMBEROS. BASE 3 IXTAPA | `20.7124156,-105.2135806` | Es de **Jalisco**: C. Colima 155, CP 48280 Ixtapa, Puerto Vallarta |
| Bomberos (registro duplicado de Base 3 Ixtapa) | `20.7127588,-105.2137193` | Mismo punto que el anterior, a menos de 5 m. Jalisco |
| Protección civil y bomberos las palmas base 4 | `20.8240477,-105.1034085` | Es de **Jalisco**: Javier Mina 322, CP 48260 Las Palmas de Arriba, Puerto Vallarta |
| Sub dirección de protección civil y bomberos base joyas | `20.6677295,-105.1928032` | Jalisco; ya publicada en el estado de Jalisco |
| Proteccion Civil Del Estado Puerto Vallarta | `20.6482005,-105.2354746` | Jalisco; ya publicada |
| Unidad Protección Civíl y Bomberos Subestación Gaviotas | `20.6356972,-105.2232027` | Jalisco; ya publicada |
| Protección Civil y Bomberos Vallarta | `20.6249291,-105.224523` | Jalisco; ya publicada |
| Protección Civil y Bomberos Bahía de Banderas (Jarretaderas) | `20.6971046,-105.2677134` | **Cerrado permanentemente**; la corporación se mudó a Bucerías |
| Proteccion civil y bomberos, Michoacán 42 | `20.7577768,-105.2345005` | **Cerrado permanentemente** |
| ASOCIACION DE BOMBEROS VOLUNTARIOS DE BAHÍA DE BANDERAS | `20.7528585,-105.239061` | **Cerrado permanentemente**; registrado como asociación, sin sede operativa |
| Protección Civil y Bomberos, Carretera a Tepic km 164 | `21.5225031,-104.8828144` | **Cerrado temporalmente**; además publica un teléfono con clave 322, de Puerto Vallarta, incongruente con la ubicación |
| Comisión Forestal de Nayarit (COFONAY), Tepic | `21.4704833,-104.8468757` | Organismo estatal forestal, no cuerpo de bomberos ni unidad de protección civil |
| Consultores Especializados en Prevención e Investigación de Incendios | `21.467897,-104.868613` | Empresa privada de consultoría |
| Super Colchones Bomberos, Tepic | `21.486347,-104.876792` | Negocio; aparece por estar sobre la avenida frente a la estación |
| FARMACIAS DEL AHORRO Bomberos, Tepic | `21.486433,-104.8769303` | Negocio; mismo caso |

### Municipios buscados sin resultado

**Tecuala, Rosamorada, Ahuacatlán, Amatlán de Cañas, Jala, San Pedro Lagunillas, Santa
María del Oro, Del Nayar y La Yesca.** Se hizo barrido dedicado por zona en cada caso
—norte a 10z y 11z, oriente a 9z y 10z, sierra a 9z— y ninguno tiene registro público
de estación de bomberos ni de unidad municipal de protección civil con sede localizable.
Tecuala y Rosamorada dependen de la base regional de Acaponeta; Ahuacatlán, Jala,
Amatlán de Cañas y San Pedro Lagunillas, de la base de Ixtlán del Río; Santa María del
Oro, de la base central de Tepic. Del Nayar y La Yesca, los dos municipios de la sierra
huichola, no tienen ninguna cobertura con sede en su territorio.

También se buscó sin resultado en las localidades de **Sayulita, San Francisco (San
Pancho), Lo de Marcos, Valle de Banderas, San Juan de Abajo, San Vicente y Mezcales**
(Bahía de Banderas) y **Zacualpan y Chacala** (Compostela).

### Pendientes

- **Teléfonos de las bases regionales.** Ni el registro de trámites ni el portal de
  transparencia publican línea directa de Nuevo Nayarit ni de Ixtlán del Río. Los de
  Acaponeta, Guayabitos, Cruz de Huanacaxtle y San Blas salen de Maps y quedaron como
  verificados con reserva.
- **Compostela:** conseguir el teléfono de la Dirección General de Protección Civil. El
  directorio municipal solo publica el correo `proteccionciudadana@compostela.gob.mx`.
- **Santiago Ixcuintla:** falta calle, número y teléfono. El portal del ayuntamiento está
  bloqueado por verificación anti-robots; reintentar con Claude in Chrome o por prensa
  local.
- **Sub-estación Topacio, Tepic** (`21.4913324,-104.8334933`): confirmar si depende de la
  Dirección General estatal o de la unidad municipal de Tepic, y conseguir teléfono.
- **Tuxpan:** la ficha pública registra la corporación como asociación. Confirmar si es
  dependencia del ayuntamiento y conseguir teléfono.
- **Bahía de Banderas:** confirmar si la Dirección municipal mantiene bases además de la
  de Bucerías; el registro de Punta de Mita no aparece en ningún listado oficial.
- **Sayulita y San Francisco:** las dos localidades turísticas de mayor crecimiento del
  municipio no tienen estación registrada. Verificar por ayuntamiento si existe destacamento.
- **Del Nayar y La Yesca:** buscar por la Comisión Nacional Forestal y por las brigadas
  comunitarias wixárikas, que son las que atienden incendio forestal en la sierra.

---

## Pendientes de otros estados

- **Chihuahua:** reintentar el ArcGIS FeatureServer del IMIP Ciudad Juárez (devolvía 503
  "Wait timeout"). Permitiría subir las 10 fichas de Juárez a `verified: true`.
- **Veracruz:** resolver los 3 registros excluidos de la región de Altas Montañas por
  ambigüedad de municipio.
- **Guanajuato:** conseguir el PDF estatal de la UMPC (bloqueado por robots) para
  completar sus 46 municipios.
- **Sinaloa:** buscar por prensa local o por ayuntamiento las corporaciones de El Rosario,
  Concordia, San Ignacio y Cosalá, que no tienen ningún registro público localizable.
- **Baja California Sur:** conseguir el teléfono directo de la estación de Guerrero Negro
  y confirmar la adscripción de la estación Manuel Basauri de Cabo San Lucas.
- **Nayarit:** conseguir los teléfonos directos de las bases regionales de Nuevo Nayarit
  e Ixtlán del Río, y abrir el portal del Ayuntamiento de Santiago Ixcuintla, bloqueado
  por verificación anti-robots.
