#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CORRECCION DE DATO en la ficha del ERA: si hay una NOM que exige prueba de ajuste.

Al publicar la ficha del ERA (commit 98fd8eb) escribimos que "no localizamos requisito de prueba
de ajuste en la NOM verificada". Era cierto respecto de lo revisado entonces —NOM-017 y NOM-116—,
pero la investigacion de la ficha de piezas faciales encontro el requisito donde no lo habiamos
buscado:

  **NOM-033-STPS-2015, apartado 6.4** — obligaciones de los trabajadores:
  "Realizar pruebas de ajuste, cuando utilicen como equipo de proteccion personal respiradores
   con linea de suministro de aire o equipo de respiracion autonomo."

  Y el apartado 9.4, inciso b) numeral 5: el procedimiento de seguridad debe contener
  "El procedimiento de revision de ajuste y prueba de hermeticidad de los respiradores".

El alcance es el trabajo en espacios confinados, no todo centro de trabajo, y asi se redacta.
Pero decir "no localizamos requisito" cuando si existe es exactamente el tipo de dato que esta
ficha le reprocha a los fabricantes. Se corrige.

Idempotente.
"""
import collections
import io
import json
import os

RUTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'src', 'data', 'productos.json')

VIEJO_P = ('Del lado mexicano hay que decirlo con precisión, sin exagerar en ninguna dirección: '
           '<strong>no localizamos requisito de prueba de ajuste en la NOM verificada</strong>.')
NUEVO_P = ('Del lado mexicano hay un requisito y conviene citarlo con numeral, porque casi nadie '
           'lo hace: la <strong>NOM-033-STPS-2015, en su apartado 6.4</strong>, obliga a los '
           'trabajadores a <em>“realizar pruebas de ajuste, cuando utilicen como equipo de '
           'protección personal respiradores con línea de suministro de aire o equipo de '
           'respiración autónomo”</em>. Su alcance es el trabajo en espacios confinados, no todo '
           'centro de trabajo, pero es el único requisito mexicano de prueba de ajuste que '
           'localizamos.')

VIEJO_Q = ('Del lado mexicano hay que decirlo con precisión: no localizamos requisito de prueba '
           'de ajuste en la NOM verificada.')

VIEJO_NOTA = ('Que no esté exigido explícitamente no lo hace opcional en la práctica:')
NUEVO_NOTA = ('Y fuera del espacio confinado, que no esté exigido de forma general no lo hace '
              'opcional en la práctica:')


def main():
    with io.open(RUTA, encoding='utf-8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    cat = next(c for c in data if c['slug'] == 'equipos-de-respiracion')
    prod = next(p for p in cat['productos'] if p['slug'] == 'scba-scott-air-pak')
    sec = next(s for s in prod['l3']['secciones'] if s['id'] == 'ajuste')

    n = 0
    if NUEVO_P.split('.')[0] not in sec['parrafos'][1]:
        assert VIEJO_P in sec['parrafos'][1], 'no se encontró el párrafo a corregir'
        sec['parrafos'][1] = sec['parrafos'][1].replace(VIEJO_P, NUEVO_P, 1)
        n += 1
        print('  ok  ajuste.parrafos[1] — se cita NOM-033-STPS 6.4')
    else:
        print('  --  ajuste.parrafos[1] ya estaba corregido')

    if VIEJO_NOTA in sec['parrafos'][2]:
        sec['parrafos'][2] = sec['parrafos'][2].replace(VIEJO_NOTA, NUEVO_NOTA, 1)
        n += 1
        print('  ok  ajuste.parrafos[2] — se acota el alcance')

    # La FAQ del ERA sobre normas mexicanas tampoco puede decir que no hay ninguna.
    for f in prod['l3']['faqs']:
        if 'NOM mexicana que certifique equipos de respiración' in f['q']:
            viejo = ('Lo que sí aplica es obligación de proceso')
            nuevo = ('Lo que sí hay, y conviene citarlo con numeral, es la NOM-033-STPS-2015, que '
                     'en su apartado 6.4 obliga a realizar pruebas de ajuste a quien use equipo '
                     'de respiración autónomo o línea de aire en espacios confinados. Y hay '
                     'obligación de proceso')
            if nuevo.split(',')[0] not in f['a']:
                assert viejo in f['a'], 'no se encontró el texto de la FAQ'
                f['a'] = f['a'].replace(viejo, nuevo, 1)
                n += 1
                print('  ok  faq sobre NOM mexicanas')
            else:
                print('  --  faq ya estaba corregida')

    if n:
        with io.open(RUTA, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
    print('correcciones aplicadas:', n)


if __name__ == '__main__':
    main()
