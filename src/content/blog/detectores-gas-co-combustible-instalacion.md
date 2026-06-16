---
title: "Detectores de Gas CO y Combustible: Lo que el Cuerpo No Puede Detectar, el Sensor Sí"
description: "Guía técnica de detectores de CO y gas combustible: bioquímica del CO, TLV-TWA 25 ppm vs IDLH, altura de instalación, gas natural vs LP, salida de relé para acción automática y calibración semestral obligatoria."
pubDate: 2026-05-20
author: "FIREFIGHTER México"
tags: ["detectores-co", "monoxido-carbono", "gas-combustible", "seguridad-industrial"]
draft: false
---

El monóxido de carbono es inodoro, incoloro e indetectable por los sentidos humanos hasta que ya hay intoxicación. En México, los accidentes por CO en instalaciones sin detector representan una fracción estadísticamente significativa de los ingresos a urgencias por "intoxicación de causa desconocida" — denominación que se usa cuando la causa del deterioro del paciente no se identifica hasta después, si es que se identifica. El CO no da señal de advertencia perceptible para el ocupante. El primer síntoma puede ser dolor de cabeza leve y somnolencia — estados que en contexto de trabajo o de descanso nocturno se interpretan como cansancio o estrés, no como intoxicación.

Para cuando el nivel de CO en sangre produce síntomas inequívocos — confusión, incapacidad para moverse, pérdida de conciencia — el ocupante ya no tiene capacidad de autoevacuación. El detector es el único mecanismo de alerta temprana disponible. No es un accesorio de seguridad: es el sistema de alerta.

## La Bioquímica del CO: Por Qué No Da Tiempo a Reaccionar

La hemoglobina tiene una afinidad por el monóxido de carbono 240 veces mayor que por el oxígeno. Cuando hay CO presente en el aire respirado, la hemoglobina lo absorbe preferentemente sobre el oxígeno, formando carboxihemoglobina (COHb). La carboxihemoglobina no puede transportar oxígeno.

El problema crítico es la cinética de la absorción: en concentraciones de CO que el olfato no puede detectar, la hemoglobina va acumulando COHb progresivamente. A 200 ppm de CO ambiental, una persona en reposo alcanza niveles de COHb del 20-30% en una hora — suficiente para causar dolor de cabeza severo y mareo. A esa concentración, tampoco hay olor ni señal perceptible.

La progresión es traicionera porque los síntomas tempranos no se distinguen de malestar común, especialmente en personas que están durmiendo — cuando más muertes por CO ocurren. La persona que duerme con una caldera con combustión deficiente puede no despertar.

### TLV-TWA y IDLH: Los Dos Números que Importan

**TLV-TWA 25 ppm**: nivel de exposición promedio durante 8 horas que no debería causar efectos adversos en trabajadores sanos. Es el umbral para exposición ocupacional crónica.

**IDLH 1,200 ppm**: nivel de CO que constituye amenaza inmediata para la vida — exposición de 30 minutos puede ser fatal.

En la práctica, los detectores de CO tienen dos niveles de alarma configurables:

- **Primer nivel**: 35-50 ppm — activa alarma audible/visual y ventilación forzada si está integrada. Permite evacuación organizada.
- **Segundo nivel**: 150-200 ppm — activa alarma de máxima urgencia y puede activar corte automático de la fuente de CO.

La diferencia entre el detector que "suena cuando hay CO" y el que tiene dos niveles con acciones específicas es la diferencia entre un dispositivo de alerta y un sistema de respuesta.

## Altura de Instalación: El Parámetro Técnico que Más Confunde

La intuición dice: "el CO es más ligero que el aire, así que el detector debe estar en el techo". El problema es que el CO tiene una densidad de 0.967 g/L frente a 1.204 g/L del aire — es ligeramente más ligero, pero la diferencia es pequeña. En condiciones normales de un espacio con ventilación, el CO no estratifica significativamente — se mezcla.

NFPA 720 y la mayoría de los fabricantes recomiendan la instalación a altura respiratoria: entre 1.0 y 1.5 metros sobre el piso. Para dormitorios donde las personas están acostadas, la instalación debe estar cerca de la cabecera de la cama, no a 3 metros de altura en el techo.

El detector de CO a 3 metros de altura detecta CO — pero lo detecta cuando la concentración ya es alta en todo el espacio, incluida la zona respiratoria del ocupante. Si el objetivo es detectar temprano para dar tiempo a la evacuación, la altura respiratoria es la correcta.

## Gas Natural vs LP: Misma Amenaza, Diferente Posición del Detector

Los detectores de gas combustible para gas natural y para gas LP son similares en tecnología pero se instalan en posiciones diferentes porque los dos gases tienen comportamientos físicos opuestos.

**Gas natural (metano)**: densidad de 0.717 g/L — significativamente más ligero que el aire. Una fuga asciende y se acumula en las partes más altas del espacio. El detector debe instalarse a 30 cm o menos del techo.

**Gas LP (propano-butano)**: densidad del propano de 1.88 g/L — más pesado que el aire. Una fuga se acumula en el piso y en depresiones. El detector debe instalarse a 30 cm o menos del piso.

El error que se repite: un edificio que operaba con gas natural y tenía detectores en el techo cambia a gas LP. Los detectores quedan en la posición incorrecta para el nuevo gas — las fugas de LP se acumulan en el piso y los detectores en el techo no detectan hasta que la concentración es alta en todo el espacio.

### Tabla de Gases con Propiedades Físicas, TLV y Niveles de Alarma

| Gas | Densidad vs Aire | Posición Detector | LIE | Alarma nivel 1 | TLV-TWA | IDLH |
|---|---|---|---|---|---|---|
| Monóxido de carbono (CO) | Ligeramente más ligero | Altura respiratoria 1-1.5 m | N/A | 35-50 ppm | 25 ppm | 1,200 ppm |
| Gas natural (metano) | Más ligero | Techo (30 cm) | 5% vol | 10-20% LIE | 1,000 ppm | 1,200 ppm |
| Gas LP-propano | Más pesado | Piso (30 cm) | 2.1% vol | 10-20% LIE | 1,000 ppm | 2,100 ppm |
| Gas LP-butano | Más pesado | Piso (30 cm) | 1.8% vol | 10-20% LIE | 800 ppm | 1,600 ppm |

LIE = Límite Inferior de Explosividad.

## La Salida de Relé: Lo Que Hace al Detector Realmente Útil

Un detector que solo produce una alarma sonora/visual tiene utilidad limitada en instalaciones desatendidas o cuando los ocupantes no pueden responder. La salida de relé transforma el detector en un actuador del sistema de seguridad.

Las acciones que puede activar mediante el relé:

- **Ventilación forzada**: cuando el detector alcanza el primer nivel de alarma, activa el extractor del espacio. La dilución del gas por ventilación forzada puede reducir la concentración antes de que alcance niveles peligrosos.
- **Corte automático de suministro de gas**: en instalaciones con válvula solenoidal, el segundo nivel activa el cierre automático. Interrumpe la fuente de CO o gas combustible incluso si no hay nadie en el edificio.
- **Señal al panel de alarma o BMS**: para generar una alarma supervisada con historial de eventos.

La combinación correcta para instalaciones de alto riesgo es: detector + ventilación automática + señal al panel. La combinación mínima aceptable es: detector + señal al panel. Un detector standalone sin integración solo funciona si hay alguien presente que escuche y pueda responder.

## Calibración Semestral Obligatoria

Los detectores de gas no se mantienen por inspección visual. Se mantienen por calibración funcional con gas patrón certificado.

A diferencia de los detectores de humo, los de gas y CO requieren exposición a una concentración conocida para verificar que el sensor responde dentro de especificación. La calibración con gas patrón verifica:

- Que el sensor responde al gas correcto
- Que la concentración de respuesta está dentro del rango especificado (más o menos 10% de la concentración nominal)
- Que el tiempo de respuesta está dentro del especificado (T90 menor a 60 segundos para CO)

El intervalo de calibración recomendado es semestral. Los sensores electroquímicos de CO tienen vida útil de 5 a 7 años y la sensibilidad declina gradualmente. La calibración semestral detecta esta degradación antes de que el sensor quede fuera de especificación.

El detector que no ha sido calibrado en dos años puede estar activando ante concentraciones diez veces mayores a las especificadas — o puede haber perdido sensibilidad al punto de no activar en concentraciones peligrosas. Sin calibración documentada, no hay forma de saber.

Para el contexto normativo de los detectores de gas en sistemas integrados, consulta [NFPA 72 en México: sistemas de alarma](/blog/nfpa-72-mexico-sistemas-alarma). La selección entre tipos de detector para los demás espacios está en [detectores de calor vs detectores de humo](/blog/detectores-calor-vs-detectores-humo). Para proyectos hospitalarios con requisitos adicionales, consulta [diseño de detección de incendio en hospitales](/blog/diseno-deteccion-incendio-hospitales).

Consulta detectores disponibles y opciones de integración en [detección y alarma](/productos/deteccion-alarma).
