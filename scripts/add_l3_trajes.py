# -*- coding: utf-8 -*-
"""Agrega el bloque l3 a trajes-estructurales-nomex-pbi y marca la categoria EPP como l3ok."""
import json, io, collections

RUTA = 'src/data/productos.json'

L3 = collections.OrderedDict([
  ("seoTitle", "Trajes estructurales Nomex y PBI NFPA 1970"),
  ("seoDescription", "Chaquetón y pantalón de tres capas en Nomex IIIA o PBI Matrix certificados NFPA 1970. Tallas XS a 4XL, corte hombre y mujer y cotización en 24 horas."),
  ("h1", "Trajes estructurales para bombero en Nomex y PBI"),
  ("subtitulo", "Chaquetón y pantalón de tres capas certificados NFPA 1970: capa exterior en Nomex IIIA o PBI Matrix, barrera de humedad y barrera térmica, en tallas de XS a 4XL con corte para hombre y mujer."),
  ("heroImg", {
    "src": "/images/catalogo/1592235905030-1000x750.webp",
    "alt": "Bombero con traje estructural completo, casco y equipo de respiración autónoma certificado NFPA 1970",
    "caption": "Ensamble estructural completo en operación"
  }),
  ("heroDatos", [
    {"label": "Certificación", "valor": "NFPA 1970, edición vigente"},
    {"label": "Retiro obligatorio", "valor": "10 años desde fabricación"}
  ]),
  ("specStrip", [
    {"label": "Capa exterior", "valor": "Nomex IIIA o PBI Matrix"},
    {"label": "Barrera de humedad", "valor": "Membrana laminada ePTFE"},
    {"label": "Barrera térmica", "valor": "Fieltro aramídico multicapa"},
    {"label": "Costura", "valor": "Hilo aramídico, doble pespunte"},
    {"label": "Visibilidad", "valor": "Cinta reflejante trilaminada"},
    {"label": "Tallas", "valor": "XS a 4XL, hombre y mujer"}
  ]),
  ("secciones", [
    {
      "id": "anatomia",
      "eyebrow": "Anatomía del ensamble",
      "titulo": "Las tres capas que definen el traje",
      "parrafos": [
        "Un <strong>traje estructural para bombero</strong> no es una prenda gruesa: es un sistema de tres capas que trabajan juntas y que fallan por separado. Cuando un comprador especifica solo “Nomex” está describiendo la capa exterior y dejando sin definir las dos que realmente determinan cuánto tiempo aguanta el elemento adentro. La mayoría de las quemaduras dentro de un traje certificado no vienen de la llama directa, vienen del <strong>vapor sobrecalentado</strong> que atraviesa una barrera de humedad vencida.",
        "Cada capa se puede especificar y cotizar de forma independiente, y ahí es donde una propuesta técnica seria se distingue de una cotización copiada del catálogo del fabricante."
      ],
      "lista": [
        {"t": "Capa exterior", "d": "Nomex IIIA o PBI Matrix. Resiste llama directa, abrasión y desgarre. No se funde ni gotea: carboniza. Es la capa que se ve, la que recibe el golpe mecánico y la que lleva las cintas reflejantes."},
        {"t": "Barrera de humedad", "d": "Membrana laminada de ePTFE. Impide que el agua de la propia línea de ataque y el vapor sobrecalentado lleguen a la piel, sin bloquear la salida del sudor. Es la capa que se degrada primero y la que casi nadie inspecciona."},
        {"t": "Barrera térmica", "d": "Fieltro aramídico multicapa. Define el tiempo real de tolerancia térmica antes de sentir el calor. Más barrera es más protección y también más carga térmica acumulada sobre el elemento."}
      ]
    },
    {
      "id": "nomex-vs-pbi",
      "eyebrow": "Decisión de material",
      "titulo": "Nomex IIIA o PBI Matrix: cuál especificar",
      "parrafos": [
        "No hay un material mejor en abstracto, hay un material correcto para un perfil de uso. La pregunta útil no es “¿cuál protege más?” sino “¿cuántas salidas estructurales reales tiene este cuerpo al año y con qué presupuesto de reposición cuenta?”."
      ],
      "tabla": {
        "head": ["Criterio", "Nomex IIIA", "PBI Matrix"],
        "rows": [
          ["Comportamiento ante llama", "No se funde ni gotea, carboniza", "Carboniza conservando la estructura del tejido"],
          ["Tras exposición severa", "Puede encoger y perder integridad", "Mantiene integridad aunque quede carbonizado"],
          ["Peso del ensamble", "Menor, ensamble más ligero", "Ligeramente mayor"],
          ["Tolerancia a ciclos térmicos", "Buena con lavado controlado", "Mayor en exposición repetida"],
          ["Costo relativo", "Menor", "Mayor"],
          ["Perfil de uso típico", "Municipal y brigada industrial con alto volumen de salidas", "Cuerpos con exposición estructural intensa y reposición programada"]
        ]
      },
      "nota": "En la práctica mexicana la mayoría de los cuerpos municipales especifican Nomex IIIA por costo total de flota, y reservan PBI para el turno de intervención o para la unidad de rescate. Es una decisión de asignación, no de calidad."
    },
    {
      "id": "tpp-thl",
      "eyebrow": "Cómo leer la etiqueta",
      "titulo": "TPP y THL: los dos números que hay que pedir",
      "parrafos": [
        "Todo ensamble certificado se mide en dos escalas que jalan en direcciones opuestas. El <strong>TPP</strong> (Thermal Protective Performance) mide cuánto calor aguanta el conjunto antes de provocar quemadura de segundo grado; NFPA exige un mínimo de <strong>35</strong>. El <strong>THL</strong> (Total Heat Loss) mide cuánto calor metabólico puede evacuar el traje, es decir cuánto tarda el elemento en agotarse por estrés térmico; el mínimo es <strong>205 W/m²</strong>.",
        "Subir el TPP agregando barrera térmica baja el THL, y un traje con THL bajo saca al elemento de operación por fatiga antes de que el fuego lo toque. Un proveedor que solo presume el TPP está mostrando la mitad del dato. Pide siempre los dos valores del ensamble armado —no de cada capa por separado— y el número de certificado del organismo que lo evaluó."
      ],
      "nota": "Los dos valores se certifican sobre el ensamble completo. Cambiar la barrera térmica por una equivalente “compatible” invalida la certificación del conjunto, aunque cada capa por sí sola esté aprobada."
    },
    {
      "id": "tallaje",
      "eyebrow": "Ajuste y tallaje",
      "titulo": "El ajuste también es protección",
      "parrafos": [
        "Un traje que no ajusta no protege menos por el material, protege menos por geometría: al levantar los brazos el chaquetón sube y descubre la cintura, y la norma exige un traslape mínimo entre chaquetón y pantalón que se pierde con dos tallas de más. El corte diferenciado para mujer no es un tema comercial: un patrón masculino sobre torso femenino genera holgura en el pecho y presión en el hombro, y ahí empieza la pérdida de movilidad.",
        "Para un pedido de brigada tomamos cuatro medidas por elemento y enviamos un juego de tallas de muestra antes de cerrar el pedido. Es el paso que evita la escena clásica de la entrega: veinte trajes correctos y cinco imposibles de usar."
      ],
      "lista": [
        {"t": "Pecho", "d": "Contorno sobre la ropa de trabajo, no sobre camiseta. Define la talla del chaquetón."},
        {"t": "Cintura y cadera", "d": "Define la talla del pantalón y el tipo de sujeción: tirantes o pretina."},
        {"t": "Entrepierna", "d": "Determina el largo del pantalón sobre la bota. Un pantalón corto expone el empeine."},
        {"t": "Estatura y largo de manga", "d": "Define el traslape con el guante y la posición de la cinta reflejante."}
      ]
    },
    {
      "id": "configuracion",
      "eyebrow": "Configuración del pedido",
      "titulo": "Lo que se define antes de fabricar",
      "parrafos": [
        "Dos cuerpos pueden comprar el mismo material y recibir trajes distintos. Estas son las opciones que se definen en el pedido y que conviene fijar por escrito en la requisición o en las bases de licitación, porque después no se modifican."
      ],
      "lista": [
        {"t": "DRD integrado", "d": "Drag Rescue Device: arnés de arrastre cosido dentro del chaquetón para extraer a un elemento inconsciente. Exigido por la norma en ensambles estructurales."},
        {"t": "Bolsillos y portarradio", "d": "Configuración de bolsas de carga, portarradio con solapa y anillo de sujeción según el protocolo del cuerpo."},
        {"t": "Refuerzos", "d": "Rodilla, codo y hombro en material de mayor abrasión para operación en gateo y arrastre prolongado."},
        {"t": "Patrón de cintas", "d": "Distribución de cinta reflejante trilaminada y color: alta visibilidad nocturna o perfil táctico."},
        {"t": "Identificación", "d": "Bordado o parche de institución, apellido y número de elemento, con material y costura que no comprometan la barrera."},
        {"t": "Cierre frontal", "d": "Combinación de cierre, velcro y broches. Define la velocidad de vestido y la hermeticidad del frente."}
      ]
    },
    {
      "id": "vida-util",
      "eyebrow": "Ciclo de vida",
      "titulo": "Vida útil, NFPA 1851 y reposición programada",
      "parrafos": [
        "NFPA obliga a retirar el ensamble a los <strong>10 años de la fecha de fabricación</strong>, no de la fecha de compra ni de la de puesta en servicio. Ese detalle mueve presupuesto: un lote adquirido con dos años de inventario del fabricante entra a la estación con ocho años de vida útil, y nadie lo nota hasta la auditoría.",
        "Entre la compra y el retiro, <strong>NFPA 1851</strong> pide inspección rutinaria por el propio elemento después de cada uso e inspección avanzada documentada al menos una vez al año, además de lavado especializado. Lavadora doméstica, cloro y suavizante destruyen la barrera de humedad sin dejar señal visible. Entregamos cada prenda con número de serie y fecha de fabricación en bitácora para que la reposición se escalone por año y no llegue toda junta."
      ],
      "nota": "El hollín que queda en el traje después de un incendio contiene compuestos asociados a cáncer ocupacional en bomberos. El lavado posterior a la intervención no es mantenimiento del equipo, es protección del elemento —y es la razón por la que un segundo juego por elemento dejó de ser un lujo."
    },
    {
      "id": "pfas",
      "eyebrow": "Tendencia del mercado",
      "titulo": "PFAS en la barrera de humedad: qué preguntar",
      "parrafos": [
        "Las barreras de humedad y los tratamientos repelentes que se usaron durante décadas se construyeron con fluoropolímeros de la familia <strong>PFAS</strong>. Varios cuerpos en Estados Unidos y Europa ya especifican ensambles PFAS-free en sus bases de compra, y los fabricantes están lanzando líneas alternas mientras la normativa se mueve. En México todavía no es un requisito, pero sí es una conversación que ya está ocurriendo dentro de las áreas de seguridad e higiene.",
        "Nuestra postura es simple: te decimos qué barrera trae el ensamble que estás cotizando y si el fabricante tiene una declaración vigente al respecto. Un traje con barrera convencional sigue siendo certificable y seguro hoy; lo que no conviene es comprar a diez años sin saber qué estás comprando."
      ]
    }
  ]),
  ("galeria", [
    {"src": "/images/catalogo/1776648120640-1000x750.webp", "alt": "Trajes estructurales y cascos colgados en el vestidor de la estación", "caption": "Ensamble completo listo por turno"},
    {"src": "/images/catalogo/1669209285616-600x450.webp", "alt": "Chaquetones estructurales en rack de estación", "caption": "Chaquetón y pantalón por elemento"},
    {"src": "/images/catalogo/1563062067-77-600x450.webp", "alt": "Bombero con traje estructural completo frente a un incendio", "caption": "Desempeño en intervención"},
    {"src": "/images/catalogo/1662121396496-600x400.webp", "alt": "Chaquetones estructurales colgados en el vestidor de la estación", "caption": "Control de tallas por turno"}
  ]),
  ("aplicaciones", [
    {"sector": "Cuerpos de bomberos", "desc": "Ensamble completo por elemento con control de tallas por turno, DRD integrado y bitácora por número de serie para escalonar la reposición a diez años."},
    {"sector": "Brigadas industriales", "desc": "Dotación conforme a NOM-002-STPS dimensionada por carga de fuego de la planta, con expediente listo para auditoría interna y de cliente."},
    {"sector": "Protección civil", "desc": "Trajes con ficha técnica en español, número de serie trazable y factura desglosada por partida y talla para comprobación de recurso público."}
  ]),
  ("datoClave", {
    "titulo": "El dato que mueve el presupuesto",
    "texto": "Los 10 años de vida útil corren desde la <strong>fecha de fabricación</strong>, no desde la compra. Pide la fecha por número de serie antes de firmar: un lote con dos años de inventario llega con ocho de servicio."
  }),
  ("normasRef", ["NFPA 1970", "NFPA 1971", "NFPA 1851", "NOM-017-STPS", "EN 469"]),
  ("blog", [
    "guia-trajes-estructurales-nfpa-1971",
    "traje-bombero-nomex-guia-completa",
    "marcas-trajes-bomberos-comparativa-mexico",
    "equipar-brigada-trajes-bomberos-tallaje-licitacion",
    "mantenimiento-epp-estructural-nfpa-1851",
    "precio-trajes-bomberos-mexico-2026"
  ]),
  ("faqs", [
    {
      "q": "¿Qué incluye un traje estructural y qué se cotiza aparte?",
      "a": "El ensamble estructural es chaquetón y pantalón con sus tres capas y el DRD integrado. Casco, botas, guantes, capucha y equipo de respiración autónoma son piezas independientes con su propia certificación y se cotizan por separado, aunque las entregamos como paquete por elemento si así conviene a tu requisición. Lo aclaramos partida por partida en la propuesta para que nadie descubra el faltante el día de la entrega."
    },
    {
      "q": "¿Cuánto pesa un ensamble estructural completo?",
      "a": "El chaquetón y el pantalón juntos rondan entre 4.5 y 6 kg según material, configuración de barreras y talla. Sumando casco, botas, guantes, capucha y equipo de respiración autónoma con cilindro, el elemento carga por encima de 20 kg. Ese número importa más de lo que parece: es la razón por la que el THL del traje decide cuánto tiempo real puede operar antes de rotar."
    },
    {
      "q": "¿Cómo verifico que un traje sí cumple NFPA 1970 y no es solo “tipo NFPA”?",
      "a": "Un ensamble certificado trae etiqueta permanente cosida al interior con el nombre del fabricante, el modelo, la fecha de fabricación, el número de serie, la composición de las tres capas y la marca del organismo certificador que lo evaluó. Sin esa etiqueta no hay certificación, por bonito que esté el catálogo. Pide además el certificado del laboratorio y la carta de distribuidor autorizado: los dos documentos viajan con nuestros envíos."
    },
    {
      "q": "¿Se puede reparar un traje estructural o hay que reemplazarlo?",
      "a": "Sí se repara, pero no en cualquier taller. NFPA 1851 exige que la reparación la haga el fabricante o un taller verificado por él, con material e hilo del mismo tipo certificado. Un parche cosido con hilo común abre un puente térmico y anula la certificación del ensamble. Rasgaduras en la capa exterior suelen ser reparables; daño en la barrera de humedad casi siempre significa reemplazo de la prenda."
    },
    {
      "q": "¿Cuántos juegos por elemento debe tener un cuerpo de bomberos?",
      "a": "El estándar operativo al que apuntan los cuerpos bien equipados es dos juegos por elemento: uno en servicio y uno disponible mientras el otro se lava o se inspecciona. Con un solo juego, el traje contaminado después de un incendio regresa a la salida siguiente sin lavarse, y eso convierte el hollín en exposición crónica. Si el presupuesto no alcanza para duplicar la flota, se puede escalonar por turno de intervención."
    },
    {
      "q": "¿Un traje forestal o de aproximación sirve para incendio estructural?",
      "a": "No. El overall forestal se certifica bajo NFPA 1950 —que consolidó la 1977— y está diseñado para exposición radiante prolongada con máxima transpirabilidad, sin barrera de humedad ni barrera térmica estructural. El traje de aproximación atiende otro escenario. Usar cualquiera de los dos en un incendio estructural deja al elemento sin la protección contra vapor sobrecalentado, que es justo lo que quema dentro de una estructura."
    },
    {
      "q": "¿Cuánto tarda la entrega de un pedido de trajes?",
      "a": "Depende de si las tallas salen de inventario o entran a fabricación. Configuraciones estándar en tallas medias suelen salir en días; pedidos con corte diferenciado, bordado institucional o tallas extremas entran a programa de producción del fabricante. En la propuesta te damos la fecha comprometida por partida y te decimos de qué depende, en lugar de prometer un plazo único que después no se cumple."
    },
    {
      "q": "¿Qué documentación entregan para una licitación de trajes?",
      "a": "Certificado del ensamble por fabricante, certificado del laboratorio que lo evaluó, carta de distribuidor autorizado, ficha técnica en español con composición de las tres capas, listado de número de serie y fecha de fabricación por prenda, procedimiento de lavado y retiro de servicio, y factura desglosada por partida y talla. Va completo y sin costo adicional; si la convocatoria pide un formato específico, lo armamos con ese formato."
    }
  ])
])

with io.open(RUTA, encoding='utf-8') as f:
    data = json.load(f, object_pairs_hook=collections.OrderedDict)

cat = next(c for c in data if c['slug'] == 'epp-para-bomberos')
cat['l3ok'] = True
prod = next(p for p in cat['productos'] if p['slug'] == 'trajes-estructurales-nomex-pbi')
prod['l3'] = L3

with io.open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('l3ok en', cat['slug'])
print('l3 agregado a', prod['slug'], '| secciones:', len(L3['secciones']), '| faqs:', len(L3['faqs']))
print('seoTitle len:', len(L3['seoTitle']) + len(' | Firefighter.com.mx'))
print('seoDescription len:', len(L3['seoDescription']))
