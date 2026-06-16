---
title: "Supresión automática en datacentros: un incendio con fecha desconocida y consecuencias calculables"
description: "Un datacentro sin sistema de supresión limpia no es un riesgo de incendio — es una certeza con fecha desconocida. Por qué los sprinklers son incorrectos, cómo funciona VESDA, la secuencia de supresión correcta y la comparativa honesta de agentes limpios para TI."
pubDate: 2026-05-20
author: "FIREFIGHTER México"
tags: ["datacentro", "supresión automática", "FM-200", "Novec 1230", "VESDA", "sala de servidores"]
draft: false
---

Un datacentro sin sistema de supresión limpia no es un riesgo de incendio — es una certeza de incendio con fecha desconocida. La carga eléctrica constante, el polvo que se acumula en semanas, el cableado que envejece, y el calor que nunca se disipa completamente hacen que el "si" de un incendio sea solo cuestión de cuándo.

En 2014 diseñamos el sistema de supresión para un centro de datos de una institución financiera en Ciudad de México. Cinco años después de la instalación, el sistema de detección temprana VESDA reportó concentración de partículas de combustión en el piso de servidores. El incendio incipiente —sobrecalentamiento de un cable de poder con aislante en proceso de degradación— fue detectado antes de que hubiera llama visible. El operador inhibió la descarga automática, aisló el servidor afectado y cortó el circuito. El costo total del incidente: el cable de poder y dos horas de trabajo técnico. La pérdida potencial, con un incendio declarado en ese piso de equipos: la valuación estimada de la operación afectada era de $80 millones de pesos en el primer día de interrupción.

La detección temprana no ocurrió por suerte. Ocurrió por diseño.

## Por qué los sprinklers de agua son inadecuados para TI: no es solo el daño del agua

La objeción más frecuente al uso de sprinklers en salas de TI es el daño que el agua causa en los equipos. Es una objeción válida. Pero no es la más importante.

**El tiempo de activación**: los sprinklers se activan por temperatura. La ampolla de 57°C (naranja) activa cuando el aire en contacto con la cabeza del rociador alcanza esa temperatura. En una sala de servidores con enfriamiento activo de precisión que mantiene temperatura entre 18°C y 24°C, para que la temperatura local en la zona de un incendio incipiente alcance 57°C, el fuego ya tiene que estar en una etapa avanzada.

El tiempo entre el inicio de un incendio en un servidor —un arco eléctrico, un chip en sobrecalentamiento— y la temperatura suficiente para activar el sprinkler puede ser de 2 a 5 minutos. En ese tiempo, el humo y los productos de combustión han contaminado equipos en un radio amplio, los sistemas han comenzado a fallar, y el incendio puede haberse propagado a los cables del piso técnico.

**La activación no selectiva**: cuando un sprinkler activa, descarga en su zona sin discriminación. En una sala de servidores con racks distribuidos, la activación de un sprinkler sobre el rack afectado también moja el equipo en los racks adyacentes. En el mejor escenario, el daño directo por agua se limita a una zona. En el escenario real, la activación puede contaminar toda la sala.

**El riesgo de activación accidental**: como se detalló en el artículo sobre [sprinklers NFPA 13](/blog/sprinklers-nfpa-13-guia-instalacion), una activación accidental en una sala de servidores puede causar más daño que el incendio que habría controlado. Los 1,500 litros de agua que un sprinkler descarga en 10 minutos sobre equipos de TI activos representan un daño catastrófico.

La solución correcta combina detección ultra-temprana con supresión de agente limpio que actúa antes de que el fuego alcance la escala que requiere activación de sprinklers.

## VESDA: detectar antes de que haya llama

VESDA (Very Early Smoke Detection Apparatus) es un sistema de detección por aspiración continua de aire. En lugar de esperar a que el humo llegue a un detector pasivo, el sistema aspira activamente muestras de aire de múltiples puntos de la sala y las analiza en una cámara de detección centralizada.

La sensibilidad es radicalmente diferente a los detectores convencionales. Un detector fotoeléctrico convencional activa cuando la concentración de partículas de humo en su zona supera un umbral predefinido —generalmente entre 2% y 4% de oscurecimiento por metro. El VESDA puede detectar concentraciones de 0.005% de obscurecimiento — tres órdenes de magnitud más sensible.

Esto significa que el VESDA detecta el inicio del proceso de combustión cuando hay un cable que comienza a degradarse térmicamente, antes de que haya humo visible para el ojo humano, antes de que haya temperatura elevada en el ambiente, y mucho antes de que haya llama.

La detección a esa concentración da tiempo para:
- Verificar si la condición es real o un falso positivo (el VESDA tiene niveles de alerta progresivos)
- Identificar el rack o área de origen por el patrón de distribución de concentración entre los puntos de muestreo
- Actuar preventivamente —apagar el equipo afectado, cortar el circuito— antes de que sea necesaria la supresión automática

En el datacentro descrito al inicio de este artículo, la detección VESDA permitió exactamente esa secuencia. Sin VESDA, la secuencia habría sido: llama → sprinkler activado en el punto caliente → descarga de agua → daño en servidores adyacentes → evaluación de cuánto se perdió.

## La secuencia de supresión correcta en un datacentro bien diseñado

El protocolo de supresión en una sala de servidores bien diseñada tiene etapas definidas con tiempos específicos:

**Etapa 1: Pre-alarma VESDA** (concentración menor al umbral de alarma)
El sistema registra la condición y la muestra en el panel de control. No activa dispositivos de notificación. El operador de turno puede investigar.

**Etapa 2: Alarma VESDA** (concentración en umbral de alarma)
El sistema activa dispositivos de notificación en la sala (luz de alarma, señal audible). El panel de alarma registra la condición. El operador tiene tiempo para inspeccionar y determinar si hay emergencia real. El tiempo disponible puede ser de 2 a 5 minutos dependiendo del desarrollo del incendio incipiente.

**Etapa 3: Confirmación de segundo detector o activación manual**
Cuando un segundo detector —VESDA en umbral de descarga, detector convencional, o detector de calor lineal— confirma la condición, el sistema inicia la secuencia de pre-descarga.

**Etapa 4: Cuenta regresiva de 30 segundos**
Se activan los dispositivos de notificación de evacuación (luz estroboscópica roja, alarma de pre-descarga con tono específico diferente al de alarma). El sistema apaga el HVAC de la sala para prevenir ventilación del agente. El personal en la sala tiene 30 segundos para evacuar.

**Etapa 5: Inhibición opcional**
Si un operador autorizado está presente y determina que no hay emergencia real (falso positivo confirmado), puede presionar el botón de inhibición que detiene la cuenta regresiva. Esta acción se registra en el panel y requiere autorización posterior.

**Etapa 6: Descarga**
Si la cuenta regresiva completa sin inhibición, el sistema abre la válvula de descarga y el agente limpio se libera en la sala en 10 segundos (HFC-227ea o FK-5-1-12) o en mayor tiempo para gases inertes.

**Etapa 7: Post-descarga**
El panel registra la descarga. El acceso a la sala requiere verificación de concentración de agente antes de la entrada sin equipo de protección (para CO₂ o gases inertes a alta concentración). Para FM-200 y Novec a concentraciones de diseño dentro del NOAEL, la entrada es segura pero se verifica por monitoreo.

## Tabla comparativa de agentes limpios para TI

| Agente | Concentración de diseño | GWP | NOAEL | Costo relativo | Estatus regulatorio |
|---|---|---|---|---|---|
| HFC-227ea (FM-200) | 6.25 - 9% | 3,350 | 9% | Medio | Sujeto a Kigali |
| FK-5-1-12 (Novec 1230) | 5.9 - 8% | 1 | 10% | Alto | Favorable |
| IG-541 (Inergen, 52/40/8%) | 37.5 - 43% | 0 | 43% | Medio | Muy favorable |
| CO₂ | 34 - 75% | 1 | 5% | Bajo | Solo sin ocupación |

La lectura correcta de esta tabla para una decisión de compra:

El FM-200 sigue siendo la solución más instalada por costo-desempeño en instalaciones nuevas en México al momento de escribir este artículo, pero su perfil bajo la Enmienda de Kigali crea incertidumbre sobre disponibilidad futura del agente de recarga.

El Novec 1230 tiene el mejor perfil ambiental de los agentes halocarburados con GWP de 1 — prácticamente sin impacto de efecto invernadero. El costo mayor se justifica en instalaciones con horizonte de vida de 15-20 años donde la regulación futura es un factor.

El IG-541 opera a concentraciones que reducen el oxígeno pero dentro del NOAEL para humanos, sin GWP, sin riesgo regulatorio futuro. La limitación es la mayor presión de almacenamiento —los cilindros son más pesados y el sistema requiere más espacio— y la mayor cantidad de agente necesaria por volumen a proteger.

El CO₂ no es adecuado para salas con ocupación. Punto ya establecido en el artículo sobre [FM-200 vs CO₂](/blog/fm200-vs-co2-supresion-limpia).

## NFPA 75: el estándar específico para TI que muchos proyectos ignoran

NFPA 75 es la norma para la Protección de Equipos de Tecnología Informática por Medios de Extinción de Incendios. Complementa NFPA 13 y NFPA 2001 con criterios específicos para salas de TI, incluyendo:

- Protección del piso técnico elevado (espacio bajo el piso donde se concentra el cableado y el flujo de aire frío)
- Protección del espacio de pleno superior
- Criterios para salas de TI dentro de edificios de ocupación mixta

El piso técnico es frecuentemente ignorado en el diseño de supresión. El espacio entre el piso elevado y el piso real acumula polvo, cable, y tiene flujo de aire que puede propagar humo y combustión a velocidades que el sistema de detección en el espacio de rack no detecta hasta que el fuego ya se propagó.

Un sistema de supresión para datacenter correcto tiene cobertura en el espacio de rack, en el espacio del piso técnico elevado, y en el plenum superior si existe. La cobertura solo en el espacio de rack es una protección parcial.

Para el cálculo de la cantidad de agente necesaria en el espacio total —incluyendo piso técnico y plenum—, el artículo sobre [agentes limpios NFPA 2001](/blog/nfpa-2001-agentes-limpios-mexico) cubre la metodología de cálculo y los factores de corrección por hermeticidad.

Para el diseño completo del sistema — incluyendo la selección de detección, la lógica de activación, la selección del agente y la integración con los sistemas de control del datacenter — consulta nuestra área técnica en [productos/sistemas-fijos](/productos/sistemas-fijos).

El costo de un sistema de supresión limpia bien diseñado para un datacenter de 200 m² está en el rango de $600,000 a $1,500,000 pesos dependiendo del agente y la complejidad. El costo de un incendio en ese datacenter, en términos de equipos perdidos, datos irrecuperables, tiempo de reconstitución y costo de reputación para el negocio que dependía de esa infraestructura, es un número que justifica el sistema con margen amplio.

La pregunta no es si el sistema de supresión es caro. La pregunta es en comparación con qué.
