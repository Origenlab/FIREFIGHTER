#!/usr/bin/env python3
"""La FAQ del ERA sobre NOM quedó citando la NOM-033 dos veces en la misma respuesta
al aplicar fix_l3_era_fit_test.py. Se fusionan en una sola mención."""
import json, collections, pathlib

RUTA = pathlib.Path(__file__).resolve().parent.parent / 'src/data/productos.json'

VIEJO = ("No localizamos ninguna. No hay NOM que fije el desempeño de un ERA ni que reconozca o "
         "equipare las certificaciones NFPA o NIOSH, y tampoco encontramos NOM que establezca "
         "límites de calidad de aire comprimido respirable. Lo que sí hay, y conviene citarlo con "
         "numeral, es la NOM-033-STPS-2015, que en su apartado 6.4 obliga a realizar pruebas de "
         "ajuste a quien use equipo de respiración autónomo o línea de aire en espacios confinados. "
         "Y hay obligación de proceso —la NOM-017-STPS, en su edición 2024 vigente desde septiembre "
         "de 2025, obliga a analizar el riesgo, determinar el equipo, entregarlo y capacitar— y la "
         "NOM-033-STPS para espacios confinados, que sí exige equipo autónomo o con línea de aire "
         "cuando no se puede confirmar atmósfera respirable. Y ojo: la NOM-116-STPS no aplica, "
         "porque cubre respiradores purificadores de presión negativa.")

NUEVO = ("No localizamos ninguna que fije el desempeño. No hay NOM que establezca los requisitos de "
         "un ERA ni que reconozca o equipare las certificaciones NFPA o NIOSH, y tampoco encontramos "
         "NOM que fije límites de calidad de aire comprimido respirable. Lo que sí hay es obligación "
         "de proceso: la NOM-017-STPS, en su edición 2024 vigente desde septiembre de 2025, obliga a "
         "analizar el riesgo, determinar el equipo, entregarlo y capacitar. Y la NOM-033-STPS-2015, "
         "para espacios confinados, exige equipo autónomo o con línea de aire cuando no se puede "
         "confirmar atmósfera respirable y, en su apartado 6.4, obliga además a realizar pruebas de "
         "ajuste a quien lo use. Ojo con la NOM-116-STPS: no aplica, porque cubre respiradores "
         "purificadores de presión negativa.")


def main():
    datos = json.loads(RUTA.read_text(encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    tocados = 0
    cats = datos['categorias'] if isinstance(datos, dict) else datos
    for cat in cats:
        for prod in cat.get('productos', []):
            l3 = prod.get('l3')
            if not l3:
                continue
            for faq in l3.get('faqs', []):
                if faq.get('a') == VIEJO:
                    faq['a'] = NUEVO
                    tocados += 1
    if tocados:
        RUTA.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'FAQs corregidas: {tocados}')


if __name__ == '__main__':
    main()
