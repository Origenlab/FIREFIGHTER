---
title: "Bombas contra incendio NFPA 20: pruebas semanales, no mensuales, no anuales"
description: "La bomba contra incendio es el corazón del sistema. Si falla en el momento crítico, el mejor diseño de rociadores no sirve de nada. NFPA 20 exige pruebas semanales porque la confiabilidad se verifica en operación, no en papel. Guía completa de selección, curva de rendimiento y cuarto de bombas."
pubDate: 2026-05-20
author: "FIREFIGHTER México"
tags: ["bombas contra incendio", "NFPA 20", "sistemas contra incendio", "bomba jockey", "protección hidráulica"]
draft: false
---

La bomba contra incendio es el corazón del sistema. Si falla en el momento crítico, el mejor diseño de rociadores del mundo no sirve de nada. Por eso NFPA 20 exige pruebas semanales — no anuales, no mensuales: semanales.

Esa frecuencia no existe para generar burocracia operativa. Existe porque la experiencia histórica en incendios donde los sistemas de sprinklers fallaron revela un patrón consistente: la bomba no arrancó cuando se necesitó, y el problema —falla mecánica, batería del arrancador agotada, obstrucción en la succión— habría sido detectado si se hubiera probado la semana anterior.

Una bomba contra incendio puede ser mecánicamente perfecta y fallar el día del incendio si no se arranca regularmente. Los sellos, las válvulas de retención, los arrancadores automáticos: todos dependen de operación periódica para mantenerse en condición funcional.

## Por qué se necesitan al menos dos bombas (y por qué tres es el estándar correcto)

El estándar de NFPA 20 para instalaciones que requieren bomba como parte del sistema contra incendio es:

**Bomba principal eléctrica**: la bomba de trabajo, dimensionada para proveer el caudal y la presión de diseño del sistema. Normalmente es una bomba centrífuga horizontal o vertical turbina, impulsada por motor eléctrico. Su fuente de energía es la red eléctrica normal del edificio.

**Bomba de respaldo diesel**: con capacidad equivalente a la bomba eléctrica principal. Su función es garantizar que el sistema opere si la energía eléctrica falla —que en México es precisamente el escenario más probable durante un siniestro, dado que los incendios frecuentemente afectan primero los tableros eléctricos o la subestación de la instalación—. La bomba diesel tiene su propio motor de combustión interna, su propio tanque de combustible (con autonomía mínima de 6 horas según NFPA 20), y sus propios sistemas de arranque y control.

**Bomba jockey (de presurización)**: una bomba de pequeño caudal —típicamente el 1-10% del caudal de la bomba principal— que mantiene la red de tubería del sistema bajo la presión de supervisión. Su función es detectar fugas: cuando hay una fuga en el sistema (un rociador que gotea, una unión que perdió hermeticidad), la presión en la red cae lentamente. La bomba jockey arranca para compensar esa caída. Si arranca con frecuencia inusual, indica una fuga que debe investigarse antes de que se convierta en un problema mayor.

Más importante aún: cuando ocurre un incendio y un rociador se activa, la caída de presión es súbita y de mayor magnitud. La bomba jockey no tiene caudal suficiente para compensar ese flujo — arranca, no puede mantener la presión, y esa condición de "bomba jockey no puede sostener presión" es la señal que activa el arranque automático de la bomba principal.

Si la bomba jockey no funciona correctamente —por falla mecánica, por estar apagada, por presión de supervisión mal configurada—, el sistema de arranque automático de la bomba principal puede no recibir la señal correcta en el momento del incendio.

## La curva de rendimiento: el concepto que más se malentiende en compras

La curva de rendimiento de una bomba centrífuga describe la relación entre el caudal que entrega y la presión (cabeza) que genera. A medida que aumenta el caudal demandado, la presión que la bomba puede generar disminuye. Esta relación no es lineal y varía con el diseño de la bomba.

Una bomba especificada como "750 gpm" (galones por minuto, aproximadamente 2,840 litros por minuto) genera ese caudal a una presión específica. Si el sistema demanda ese caudal a una presión mayor —porque hay más elevación, más longitud de tubería, o más pérdidas de carga de las que se calcularon en el diseño—, la bomba entregará menos de 750 gpm a esa presión mayor.

El error de compra más frecuente: especificar la bomba solo por caudal nominal (750 gpm) sin verificar que la curva de rendimiento de la bomba específica genera ese caudal a la presión de diseño del sistema.

Dos bombas con el mismo caudal nominal de 750 gpm pero curvas de rendimiento diferentes pueden tener desempeños radicalmente distintos en el sistema real. La selección correcta requiere comparar la curva de la bomba contra el punto de operación del sistema —el "punto de diseño"— que resulta del cálculo hidráulico.

Para verificar la selección correcta, NFPA 20 requiere una prueba de rendimiento con medición del caudal, presión de succión y presión de descarga en tres puntos de la curva: punto de cierre (sin flujo), punto de diseño (150% del caudal de diseño) y punto de arranque de la bomba jockey. Los resultados deben compararse contra la curva publicada del fabricante.

## Pruebas semanales obligatorias y cómo registrarlas

NFPA 20 requiere arranque semanal de las bombas. El protocolo mínimo:

- Arranque manual de la bomba principal eléctrica: arranque desde el panel de control, operación durante el tiempo mínimo especificado (típicamente 10 minutos), verificación de indicadores de presión y temperatura, registro de hora de inicio y fin, presión en succión y descarga, temperatura del motor.
- Arranque manual de la bomba diesel: mismo procedimiento, con verificación adicional de nivel de combustible en tanque.
- Verificación de frecuencia de arranque de bomba jockey en la semana anterior: si arrancó más de 2-3 veces en la semana sin demanda conocida, investigar fugas.

El registro debe ser en bitácora permanente con fecha, nombre del responsable, lecturas de los indicadores y cualquier anomalía observada. Esta bitácora es el primer documento que se revisa en una auditoría de NFPA 25 y en la investigación de siniestros.

Las anomalías más frecuentes que se detectan en las pruebas semanales y que habrían pasado inadvertidas sin ellas:

- Batería de arranque del motor diesel con carga insuficiente
- Temperatura del motor eléctrico inusualmente alta (problema de ventilación o sobrecarga)
- Vibración anormal (indicador de cavitación, desalineación o problema en rodamiento)
- Presión de succión inusualmente baja (obstrucción en la tubería de succión o nivel bajo en tanque)
- Tiempo de arranque del diesel más largo que el nominal (problema en el sistema de arranque)

## Cuarto de bombas: los requisitos de NFPA 20 que más se incumplen en México

El cuarto de bombas no es un cuarto de servicio cualquiera. NFPA 20 define condiciones específicas que frecuentemente se ignoran en proyectos, con consecuencias operativas reales.

**Temperatura**: el cuarto de bombas debe mantenerse por encima de 4°C en todo momento para proteger las tuberías y componentes del congelamiento. En zonas norte de México en invierno, esto puede requerir calefacción. El motor diesel también requiere temperatura mínima para arrancar confiablemente.

**Ventilación**: el cuarto debe tener ventilación suficiente para disipar el calor generado por los motores eléctricos y el motor diesel en operación continua. Una bomba principal eléctrica de 75 kW genera calor significativo. Sin ventilación adecuada, el motor se sobrecalienta y la protección térmica lo apaga justo cuando más se necesita.

**Drenaje**: el piso del cuarto de bombas debe tener drenaje para manejar el agua de pruebas, fugas de empaque y descargas de válvulas de alivio. Un cuarto de bombas sin drenaje adecuado acumula agua que puede generar corrosión en los componentes y riesgo eléctrico.

**Acceso**: el cuarto debe ser accesible para mantenimiento y para operación manual en emergencia. Las dimensiones deben permitir trabajo de mantenimiento en todos los componentes sin maniobras acrobáticas.

**Separación del riesgo de incendio**: el cuarto de bombas no debe estar adyacente a áreas de alto riesgo de incendio sin separación adecuada. Si el cuarto de bombas queda comprometido por el incendio antes de que la bomba pueda operar, el sistema falla.

Para las válvulas de control que determinan si el caudal de la bomba llega efectivamente a los sprinklers, el artículo sobre [válvulas OS&Y](/blog/valvulas-osy-funcionamiento-mantenimiento) cubre el componente que más frecuentemente es la causa de falla del sistema.

El sistema completo de sprinklers que la bomba alimenta está detallado en el artículo sobre [sprinklers NFPA 13](/blog/sprinklers-nfpa-13-guia-instalacion), y el programa de mantenimiento integral que incluye las pruebas de bomba dentro de un plan NFPA 25 está en el artículo sobre [revisión anual de sistemas contra incendio](/blog/revision-anual-sistemas-contra-incendio).

Para selección, suministro e instalación de conjuntos de bombas contra incendio certificados bajo NFPA 20, consulta nuestra área técnica en [productos/sistemas-fijos](/productos/sistemas-fijos).

La bomba que nunca se arranca entre una auditoría y otra es la bomba que falla el día del incendio. NFPA 20 no se equivoca al pedir pruebas semanales — se basa en décadas de evidencia de lo que ocurre cuando esas pruebas no se hacen.
