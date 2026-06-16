---
title: "Sirenas y Estrobos SpectralAlert: El Sistema de Notificación que Más Se Subpresupuesta"
description: "Guía técnica de notificación de alarma: 15 dB sobre ruido ambiental, sincronización de estrobos y epilepsia fotosensible, requisitos para cuartos de hotel, espaciado por candela y diseño para áreas industriales ruidosas."
pubDate: 2026-05-20
author: "FIREFIGHTER México"
tags: ["sirenas", "estrobos", "spectralert", "nfpa-72"]
draft: false
---

Un sistema de alarma que nadie puede escuchar desde su puesto de trabajo no es un sistema de alarma — es teatro de seguridad. El componente de notificación (sirenas y estrobos) es el que más se subpresupuesta en los proyectos de alarma y el que más frecuentemente falla en situaciones reales de evacuación. El patrón es predecible: el presupuesto se concentra en el panel y los detectores, y cuando queda poco para la notificación, se instalan sirenas de especificación mínima en las posiciones más convenientes para el instalador, no en las posiciones correctas para los ocupantes.

El resultado es un sistema que el panel puede ver como completo y conforme — todos los dispositivos reportan correctamente — pero que en campo no cumple con los requisitos de sonido y visibilidad de NFPA 72. La sala de producción con 85 dB de ruido continuo tiene una sirena de 75 dB que no se escucha sobre el ruido. El pasillo con cuatro estrobos asíncronos crea un patrón de destello que puede provocar crisis en personas con epilepsia fotosensible. El cuarto de hotel dormido tiene una sirena en el corredor que no penetra la puerta cerrada con suficiente nivel.

## El Requisito de 15 dB Sobre el Ruido Ambiental

NFPA 72 requiere que el nivel de presión sonora de la alarma en el punto de recepción — donde está el ocupante — sea 15 dB mayor que el ruido ambiental promedio del espacio, o 5 dB mayor que el pico de ruido máximo de duración de 60 segundos o más. Se usa el valor mayor de los dos.

Esto tiene consecuencias directas que muchos diseñadores no calculan correctamente:

Una oficina silenciosa tiene un ruido ambiental de aproximadamente 45 dB. La alarma necesita llegar a 60 dB en el punto del ocupante. Una sirena de 75 dB instalada a 10 metros de distancia, con la atenuación normal de la distancia (pérdida de 6 dB por duplicar la distancia), llega con aproximadamente 63 dB al ocupante — suficiente.

Una planta de producción con maquinaria pesada tiene un ruido ambiental de 85 dB. La alarma necesita llegar a 100 dB en el punto del ocupante. Una sirena estándar de 90 dB en el techo no alcanza ese nivel a la distancia del trabajador más alejado. Se necesitan sirenas de alta potencia (100-110 dB), mayor densidad de dispositivos, o bocinas de proximidad en posiciones estratégicas cerca de los puestos de trabajo.

El nivel de dB de la sirena en la ficha técnica es la medida a 3 metros de distancia de la fuente. No es el nivel en el punto del ocupante. El diseñador debe calcular la atenuación por distancia y por barreras (paredes, maquinaria, estanterías) para cada punto del espacio.

### Límite Superior: 110 dB en el Punto del Ocupante

NFPA 72 también establece un límite máximo de 110 dB en el punto del ocupante para evitar daño auditivo. En espacios pequeños y confinados donde se instalan sirenas de alta potencia, este límite puede superarse — especialmente en tableros de control, cabinas de operación y cuartos de servidores pequeños. El diseño de notificación en estos espacios puede requerir sirenas de menor potencia en posiciones más cercanas, en lugar de sirenas potentes en posiciones lejanas.

## Sincronización de Estrobos: El Requisito que Salva Vidas de Otra Manera

Los estrobos de notificación visual en un sistema de alarma deben estar sincronizados. Esta no es una preferencia estética — es un requisito de NFPA 72 con fundamento médico directo.

La epilepsia fotosensible afecta a aproximadamente el 3% de las personas con epilepsia — que es alrededor del 0.05% de la población general. Las crisis fotosensibles son inducidas por destellos a frecuencias entre 3 y 30 Hz. Los estrobos de alarma no sincronizados en un espacio pueden crear patrones de destello compuesto en el rango de frecuencias de riesgo.

Un escenario concreto: corredor con cuatro estrobos, cada uno parpadeando a 2 Hz (el estándar de NFPA 72), pero con desfase de fase entre ellos. Un observador en el corredor ve los cuatro estrobos desde diferentes ángulos y su sistema visual percibe una frecuencia de destello compuesta que puede estar en el rango de 6 a 8 Hz — el rango de mayor riesgo para epilepsia fotosensible.

Con sincronización, todos los estrobos del edificio parpadean en el mismo instante. El observador en cualquier punto del corredor ve un solo evento de destello por ciclo, no cuatro desfasados. La frecuencia percibida es 2 Hz — bajo el umbral de riesgo.

La sincronización se logra con el módulo de sincronización del fabricante (SpectralAlert tiene su propio protocolo de sincronización) o mediante la señal del panel. Los dispositivos de diferentes fabricantes generalmente no se sincronizan entre sí — este es un problema frecuente en ampliaciones de sistemas donde se mezclan dispositivos de diferentes marcas.

## Notificación en Cuartos de Hotel: El Dormido Escucha Menos

NFPA 72 tiene requisitos específicos para habitaciones de hotel porque el escenario presenta una combinación de factores difícil: ocupantes dormidos, puerta cerrada entre la sirena del corredor y el ocupante, y posiblemente tapones de oídos, medicamentos o alcohol que reducen la percepción auditiva.

La atenuación de una puerta de madera cerrada es de aproximadamente 20 a 25 dB. Si la sirena del corredor produce 75 dB en el punto de la puerta, el nivel dentro de la habitación con la puerta cerrada es de 50 a 55 dB — insuficiente para despertar a un adulto dormido en sueño profundo (requiere entre 75 y 85 dB en la oreja del durmiente).

NFPA 72 resuelve esto de dos maneras:

**Opción 1**: instalar sirenas dentro de cada habitación, no solo en el corredor. El nivel requerido dentro de la habitación, con el ocupante dormido, es de 75 dB a la altura de la cabecera de la cama. Esto requiere una sirena de nivel moderado instalada dentro de la habitación, frecuentemente integrada en el mismo dispositivo que el detector de humo del cuarto.

**Opción 2**: sistema de notificación con parlante de baja impedancia integrado en la habitación, que puede también transmitir mensaje de voz. Este sistema permite notificación por voz con instrucciones específicas — más efectivo para la respuesta de evacuación que una sirena sin mensaje.

La situación más crítica es el hotel con corredor largo y habitaciones con puerta sólida, sin ningún dispositivo de notificación dentro de las habitaciones. En ese escenario, los ocupantes en el extremo más alejado de la sirena del corredor, dormidos con la puerta cerrada, pueden no escuchar la alarma.

### Tabla de Espaciado de Estrobos por Candela en Pasillos y Espacios Abiertos

| Potencia del Estrobo | Espaciado Máximo en Pasillo | Espaciado Máximo Espacio Abierto | Aplicación |
|---|---|---|---|
| 15 cd | 6 m entre estrobos | 6 m × 6 m | Pasillos residenciales, cuartos pequeños |
| 30 cd | 9 m entre estrobos | 9 m × 9 m | Pasillos comerciales, habitaciones de hotel |
| 75 cd | 14 m entre estrobos | 14 m × 14 m | Espacios de oficinas abiertos, salas |
| 110 cd | 18 m entre estrobos | 18 m × 18 m | Espacios industriales grandes |
| 177 cd | 23 m entre estrobos | 23 m × 23 m | Almacenes, plantas de producción |

Los valores de la tabla corresponden a espacios con altura de techo estándar (hasta 3 metros). Para techos más altos, la potencia del estrobo requerida aumenta porque la distancia a la zona de visión del ocupante es mayor.

## Diseño para Áreas Industriales Ruidosas

El diseño de notificación para plantas industriales con ruido ambiental elevado es el escenario más complejo y el que más frecuentemente se diseña mal porque se aplica la misma especificación que para un edificio de oficinas.

Los componentes correctos para áreas industriales con ruido de 80-100 dB:

- **Bocinas de alta potencia**: potencia de 100-120 dB a 1 metro, proyectan sonido en dirección específica — orientan la notificación hacia las áreas de trabajo sin saturar toda la planta
- **Estrobos de alta candela a baja altura**: en lugar de solo en el techo donde la maquinaria puede bloquear la visibilidad, se complementan con estrobos a nivel de vista (1.5-2 metros de altura) en pasillos de circulación entre maquinaria
- **Señal de texto en pantallas de proceso**: en plantas con sistemas DCS o SCADA, la integración del sistema de alarma con las pantallas de proceso permite notificación visible donde el operador siempre tiene la vista
- **Señal táctil en puestos de trabajo críticos**: para operadores con protección auditiva permanente, los dispositivos de notificación táctil (vibración en el asiento o superficie de trabajo) son el único medio efectivo de notificación
- **Combinación de medios**: el diseño correcto usa al menos dos tipos de notificación simultánea — auditiva + visual, o visual + táctil — para garantizar detección independientemente de las condiciones del puesto de trabajo

Para el contexto normativo que rige los requisitos de notificación, consulta [NFPA 72 en México: sistemas de alarma](/blog/nfpa-72-mexico-sistemas-alarma). La [estación manual BG12LX](/blog/estaciones-manuales-bg12lx-normativa) es el dispositivo que activa el sistema cuya notificación diseñamos aquí. Y la programación de las secuencias de notificación desde el panel está en [panel Notifier NFS2-3030](/blog/panel-notifier-nfs2-3030-programacion).

Consulta disponibilidad de dispositivos SpectralAlert y configuraciones para tu proyecto en [detección y alarma](/productos/deteccion-alarma).
