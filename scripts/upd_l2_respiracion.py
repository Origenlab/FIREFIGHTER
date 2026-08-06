#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abre la categoria de equipos de respiracion y corrige lo que la investigacion desmintio.

Seis correcciones, todas verificadas en fuente primaria el 2026-08-06:

 1. MARCA INEXISTENTE. `marcas` decia "Scott Safety". Esa marca ya no existe: la division se
    llama **3M Scott Fire & Safety**. Y faltaba Drager, que si publica linea NFPA para EE. UU.
 2. NORMA CONSOLIDADA. NFPA 1852 (seleccion, cuidado y mantenimiento de ERA de circuito
    abierto) fue consolidada en **NFPA 1850 (2026)** junto con NFPA 1851, con fecha efectiva
    del 9 de septiembre de 2025.
 3. FALTABA LA MITAD DEL MARCO. Un ERA para combate estructural necesita DOS cosas:
    certificacion NFPA y **aprobacion NIOSH bajo 42 CFR Parte 84**. La categoria no mencionaba
    NIOSH en ninguna parte, y es la mitad que en Mexico casi nadie pide.
 4. ERROR DE CATEGORIA EN EL RIT. El producto de sistemas RIT declaraba **NFPA 1407**, que es
    norma de ENTRENAMIENTO de tripulaciones de intervencion rapida —titulo 2020: "Standard for
    Training Fire Service Rapid Intervention Crews"— y que desde 2026 ni existe con ese numero:
    fue absorbida en NFPA 1400, capitulos 26 a 30. Un pack de aire de rescate no se certifica
    con una norma de entrenamiento.
 5. NORMA QUE NO APLICA. La mascara declaraba **NOM-116-STPS**, que cubre respiradores
    purificadores de aire de **presion negativa** contra particulas: no aplica a una pieza
    facial de ERA de presion positiva. La entrada de la categoria ya lo aclaraba; la del
    producto no.
 6. NOM CANCELADA. NOM-017-STPS-2008 fue **cancelada** por NOM-017-STPS-2024 (DOF 28-mar-2025,
    en vigor 28-sep-2025). Se corrige la descripcion sin afirmar que cambio de fondo, porque
    el texto del DOF no se pudo leer todavia.

Y activa `l3ok` para que la categoria genere fichas L3.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

MARCAS = ['MSA Safety', '3M Scott', 'Dräger']

NORMAS = collections.OrderedDict([
    ('NFPA 1970',
     'Desde 2025 incorpora los requisitos de ERA de circuito abierto (antes NFPA 1981, hoy '
     'capítulos 15 a 19) y de dispositivos PASS (antes NFPA 1982). El plazo de transición para '
     'ERA y PASS fue de 18 meses, no de 12 como en el resto del ensamble.'),
    ('NIOSH 42 CFR 84',
     'Aprobación federal estadounidense del aparato respiratorio. Es la otra mitad del marco: '
     'NIOSH aprueba el equipo COMPLETAMENTE ENSAMBLADO y no aprueba componentes ni subensambles. '
     'El número de aprobación empieza con el prefijo TC.'),
    ('NFPA 1850',
     'Selección, cuidado y mantenimiento. Desde la edición 2026 consolida NFPA 1851 (ensamble) '
     'y NFPA 1852 (ERA de circuito abierto), con fecha efectiva del 9 de septiembre de 2025.'),
    ('NFPA 1989',
     'Calidad del aire respirable para servicios de emergencia: qué debe cumplir el aire del '
     'compresor que llena los cilindros y cada cuándo se analiza.'),
    ('NOM-017-STPS',
     'Selección, uso y manejo del equipo de protección personal. La edición 2008 fue cancelada '
     'por la NOM-017-STPS-2024, publicada en el DOF el 28 de marzo de 2025 y en vigor desde el '
     '28 de septiembre de 2025.'),
    ('NOM-033-STPS',
     'Condiciones de seguridad para trabajos en espacios confinados: exige equipo de respiración '
     'autónomo o con línea de aire cuando no se puede confirmar atmósfera respirable, y monitoreo '
     'continuo en los espacios de mayor riesgo.'),
    ('NOM-116-STPS',
     'Respiradores purificadores de aire de presión negativa contra partículas. Se incluye para '
     'decir qué NO cubre: no aplica a una pieza facial de ERA, que trabaja con presión positiva.'),
])

DOCUMENTACION = [
    'Certificado de cumplimiento NFPA 1970 con edición y organismo certificador nombrado',
    'Etiqueta de aprobación NIOSH con número TC y la configuración aprobada',
    'Número de serie del regulador, del arnés y del cilindro',
    'Designación DOT del cilindro, prueba hidrostática vigente y fecha de la próxima',
    'Registro de prueba de ajuste facial cuantitativa por usuario',
    'Manual de operación y mantenimiento en español, con el programa de servicio',
    'Factura desglosada por número de parte del fabricante',
]

# slug -> (nombre nuevo o None, norma nueva o None)
PRODUCTOS = {
    'scba-scott-air-pak': ('Equipos de respiración autónoma', 'NFPA 1970'),
    'mascaras-completas-3m': ('Piezas faciales y máscaras completas', 'NFPA 1970'),
    'cilindros-30-45-60-min': (None, 'DOT / NFPA 1970'),
    'sistemas-rit-de-rescate': ('Sistemas RIT de aire de rescate', 'NFPA 1970'),
    'reguladores-y-valvulas': (None, 'NFPA 1970'),
    'maletines-de-mantenimiento': (None, 'NFPA 1850'),
}


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    cat = next(c for c in data if c['slug'] == 'equipos-de-respiracion')
    cambios = []

    if cat.get('marcas') != MARCAS:
        cat['marcas'] = MARCAS
        cambios.append('marcas')

    normas = [collections.OrderedDict([('code', c), ('desc', d)]) for c, d in NORMAS.items()]
    if cat.get('normas') != normas:
        cat['normas'] = normas
        cambios.append('normas (%d)' % len(normas))

    if cat.get('documentacion') != DOCUMENTACION:
        cat['documentacion'] = DOCUMENTACION
        cambios.append('documentacion')

    if not cat.get('l3ok'):
        cat['l3ok'] = True
        cambios.append('l3ok')

    for slug, (nombre, norma) in PRODUCTOS.items():
        prod = next(p for p in cat['productos'] if p['slug'] == slug)
        if nombre and prod['nombre'] != nombre:
            print('   nombre: «%s» → «%s»' % (prod['nombre'], nombre))
            prod['nombre'] = nombre
            cambios.append('%s/nombre' % slug)
        if norma and prod.get('norma') != norma:
            print('   norma:  %-26s %s → %s' % (slug, prod.get('norma'), norma))
            prod['norma'] = norma
            cambios.append('%s/norma' % slug)

    if cambios:
        with io.open(RUTA, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

    print('\ncambios:', ', '.join(cambios) if cambios else 'ninguno, ya estaba')
    print('l3ok:', cat.get('l3ok'), '| productos:', len(cat['productos']))


if __name__ == '__main__':
    main()
