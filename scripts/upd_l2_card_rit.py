#!/usr/bin/env python3
"""Corrige la card L2 del RIT y su FAQ. Traía tres sobreclaims que la L3 desmiente:

1. `norma: NFPA 1970` — el paquete no está certificado por nadie.
2. «la NFPA 1407 exige entrenamiento específico» — exige un programa a la corporación,
   no una característica del producto, y ya no es norma independiente (consolidada en
   la norma general de entrenamiento, edición 2026).
3. «manguera de transllenado universal» — el acople sí es universal; la política del
   fabricante no lo es, y hay marcas que prohíben el transllenado entre equipos.
"""
import json, collections, pathlib

RUTA = pathlib.Path(__file__).resolve().parent.parent / 'src/data/productos.json'
SLUG_CAT = 'equipos-de-respiracion'
SLUG_PROD = 'sistemas-rit-de-rescate'

NUEVO_DESC = (
    'Paquete portátil de aire para rescatar a un bombero atrapado: cilindro dedicado, reductor de '
    'presión y manguera con la conexión universal de rescate. Ningún paquete de este tipo está '
    'certificado: lo certificado es la conexión del equipo de la víctima.'
)

NUEVAS_SPECS = [
    'Conexión universal de rescate, obligatoria en el ERA desde 2002',
    'Transllenado que iguala presión, no que llena',
    'Pieza facial incluida solo en algunas configuraciones',
    'Cilindro casi siempre cotizado por separado',
]

NUEVO_INTRO = [
    'El <strong>RIT</strong> —equipo de intervención rápida— existe para un solo escenario: un bombero '
    'atrapado, desorientado o sin aire dentro de la estructura. El paquete lleva un cilindro dedicado '
    'al rescatado, reductor de presión, manguera de suministro y manguera de transllenado con la '
    'conexión universal de rescate. Según la configuración incluye también pieza facial de reemplazo, '
    'y en una de ellas viene ya conectada a la válvula de demanda para ahorrar pasos en el despliegue.',
    'Dos precisiones que ahorran problemas en una partida. La primera: <strong>ningún paquete RIT está '
    'certificado</strong>, porque la aprobación se emite solo para respiradores completos —un '
    'fabricante lo dice por escrito en su manual—; lo que está normado es la conexión del equipo al que '
    'se conecta. La segunda: el transllenado <strong>iguala presiones, no llena</strong>, y el acople '
    'universal no significa que todas las marcas autoricen las mismas maniobras. Entregamos el sistema '
    'con la compatibilidad verificada contra los equipos que ya opera la corporación y con la '
    'capacitación de despliegue incluida.',
]

FAQ_VIEJA_Q = '¿Qué es un sistema RIT y por qué lo piden las convocatorias?'
FAQ_NUEVA_A = (
    'Un RIT o equipo de intervención rápida es el paquete que se despliega cuando un bombero queda '
    'atrapado, desorientado o sin aire dentro de la estructura: cilindro dedicado al rescatado, '
    'reductor, manguera de suministro y manguera de transllenado, en un maletín listo para salir. Se '
    'pide porque tener personal equipado no basta si no hay forma de darle aire a quien se quedó sin '
    'él. Ojo con dos cosas al redactar la partida: ningún paquete RIT está certificado —la aprobación '
    'se emite solo para respiradores completos, así que pedir «RIT certificado NFPA» es pedir un '
    'documento que no existe—, y el transllenado iguala presiones en lugar de llenar. Lo que sí se '
    'exige por escrito es el certificado del equipo de respiración autónoma y la lista de contenido del '
    'paquete renglón por renglón.'
)


def main():
    datos = json.loads(RUTA.read_text(encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
    cats = datos['categorias'] if isinstance(datos, dict) else datos
    cambios = []
    for cat in cats:
        if cat.get('slug') != SLUG_CAT:
            continue
        codigos = [n['code'] for n in cat.get('normas', [])]
        if 'NFPA 1407' not in codigos:
            cat['normas'].append(collections.OrderedDict([
                ('code', 'NFPA 1407'),
                ('desc',
                 'Norma de <strong>entrenamiento</strong> de las cuadrillas de intervención rápida, no '
                 'de equipo: su propio articulado deja las herramientas de la cuadrilla a criterio de '
                 'la autoridad competente, y la mención de una fuente de aire de rescate está en el '
                 'anexo informativo. Su contenido fue consolidado en la norma general de entrenamiento '
                 'del servicio de bomberos, edición 2026, junto con otras seis normas de capacitación; '
                 'la edición 2020 sigue a la venta durante la transición. Lo exigible con numeral es la '
                 'evaluación anual del desempeño de la cuadrilla y de cada integrante.'),
            ]))
            cambios.append('norma NFPA 1407 en la categoría')
        for faq in cat.get('faqs', []):
            if faq.get('q') == FAQ_VIEJA_Q:
                faq['a'] = FAQ_NUEVA_A
                cambios.append('faq L2')
        for prod in cat.get('productos', []):
            if prod.get('slug') != SLUG_PROD:
                continue
            # El badge decía NFPA 1970 a secas, como si el paquete estuviera certificado.
            # Lo que la norma cubre es la conexión de rescate del ERA receptor.
            if prod.get('norma') == 'NFPA 1970':
                prod['norma'] = 'Conexión NFPA 1970'
                cambios.append('norma')
            prod['desc'] = NUEVO_DESC
            prod['specs'] = NUEVAS_SPECS
            prod['intro'] = NUEVO_INTRO
            cambios += ['desc', 'specs', 'intro']
    if cambios:
        RUTA.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('actualizado:', ', '.join(cambios) or 'nada')


if __name__ == '__main__':
    main()
