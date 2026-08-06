#!/usr/bin/env python3
"""
Auditoría de la malla de enlaces internos de /cumplimiento sobre dist/.

Por qué existe: la sección es una malla de tres ejes (norma, giro, estado) más el
cruce estado x giro. Es fácil agregar páginas que nadie enlaza —las 320 fichas de
cruce nacieron huérfanas— y eso no lo detecta el build. Este script mide entrantes
y salientes por grupo y falla si algo baja del piso acordado.

Reglas de medición, todas deliberadas:
  * Solo cuenta enlaces dentro de <main>. El header y el footer enlazan a
    /cumplimiento desde las 810 páginas y taparían cualquier hueco real.
  * Quita <script> y <style> antes de leer hrefs. El popup de Leaflet de /mapa
    contiene un template literal que el navegador interpola en cliente y que si
    no, aparece como enlace roto.
  * Ignora la barra final: este sitio no la usa en los href.

Uso:
    python3 scripts/audit_cumplimiento.py            # audita ./dist
    python3 scripts/audit_cumplimiento.py otro/dist

Sale con código 1 si hay huérfanas, enlaces rotos o algún grupo bajo el piso.
"""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict

DIST = sys.argv[1] if len(sys.argv) > 1 else "dist"

# Piso de enlaces por grupo. Bajarlos requiere una razón escrita, no un ajuste.
PISOS = {
    "hub": {"out": 20, "in": 20},
    "norma": {"out": 8, "in": 50},
    "giro nacional": {"out": 40, "in": 40},
    "estado": {"out": 20, "in": 10},
    "cruce estado x giro": {"out": 12, "in": 8},
}

GRUPOS = {
    "hub": lambda u: u == "/cumplimiento",
    "norma": lambda u: u.startswith("/cumplimiento/normas/"),
    "giro nacional": lambda u: u.startswith("/cumplimiento/giro/"),
    "estado": lambda u: re.fullmatch(r"/cumplimiento/estado/[^/]+", u) is not None,
    "cruce estado x giro": lambda u: re.fullmatch(r"/cumplimiento/estado/[^/]+/[^/]+", u) is not None,
}

# Rutas que no son páginas HTML y por tanto no cuentan como enlace roto.
NO_ES_PAGINA = re.compile(r"\.(xml|txt|webp|png|jpe?g|svg|ico|pdf|webmanifest|js|css|avif|woff2?)$")
PREFIJOS_ESTATICOS = ("/_astro", "/fonts", "/img", "/images", "/assets")

RE_SCRIPT_STYLE = re.compile(r"<(script|style)\b.*?</\1>", re.S | re.I)
RE_MAIN = re.compile(r"<main\b[^>]*>(.*?)</main>", re.S | re.I)
RE_HREF = re.compile(r'href="(/[^"#?]*)')


def normaliza(url: str) -> str:
    return url.rstrip("/") or "/"


def cargar(dist: str) -> dict[str, str]:
    """Mapea ruta publicada -> HTML del <main>, sin scripts ni estilos."""
    paginas: dict[str, str] = {}
    for carpeta, _, archivos in os.walk(dist):
        if "index.html" not in archivos:
            continue
        ruta = os.path.relpath(carpeta, dist).replace(os.sep, "/")
        url = "/" if ruta == "." else "/" + ruta
        html = open(os.path.join(carpeta, "index.html"), encoding="utf8").read()
        html = RE_SCRIPT_STYLE.sub("", html)
        m = RE_MAIN.search(html)
        paginas[normaliza(url)] = m.group(1) if m else html
    return paginas


def main() -> int:
    if not os.path.isdir(DIST):
        print(f"No existe {DIST}/. Corre `npm run build` primero (en la Mac, no en la VM Linux).")
        return 1

    paginas = cargar(DIST)
    salientes: dict[str, set[str]] = defaultdict(set)
    entrantes: dict[str, set[str]] = defaultdict(set)

    for origen, cuerpo in paginas.items():
        for href in RE_HREF.findall(cuerpo):
            destino = normaliza(href)
            if destino == origen:
                continue
            salientes[origen].add(destino)
            entrantes[destino].add(origen)

    fallos: list[str] = []

    # ── Enlaces rotos ─────────────────────────────────────────────────────
    rotos: dict[str, set[str]] = defaultdict(set)
    for origen, destinos in salientes.items():
        for destino in destinos:
            if destino in paginas:
                continue
            if destino.startswith(PREFIJOS_ESTATICOS) or NO_ES_PAGINA.search(destino):
                continue
            rotos[destino].add(origen)

    print(f"Páginas analizadas: {len(paginas)}\n")
    print("=== ENLACES INTERNOS ROTOS ===")
    if rotos:
        for destino, origenes in sorted(rotos.items()):
            print(f"  {destino}  <- {len(origenes)} página(s), p.ej. {sorted(origenes)[0]}")
        fallos.append(f"{len(rotos)} destino(s) roto(s)")
    else:
        print("  ninguno")

    # ── Cobertura por grupo ───────────────────────────────────────────────
    print("\n=== ENLACES POR GRUPO (solo dentro de <main>) ===")
    print(f"{'grupo':24}{'n':>5}   {'out mín/med/máx':>18}   {'in mín/med/máx':>18}")
    for grupo, pertenece in GRUPOS.items():
        urls = [u for u in paginas if pertenece(u)]
        if not urls:
            continue
        outs = sorted(len(salientes[u]) for u in urls)
        ins = sorted(len(entrantes[u]) for u in urls)
        med = lambda xs: xs[len(xs) // 2]
        print(
            f"{grupo:24}{len(urls):>5}   "
            f"{outs[0]:>5}/{med(outs):>5}/{outs[-1]:>5}   "
            f"{ins[0]:>5}/{med(ins):>5}/{ins[-1]:>5}"
        )
        piso = PISOS.get(grupo)
        if piso and outs[0] < piso["out"]:
            fallos.append(f"{grupo}: salientes mínimas {outs[0]} < piso {piso['out']}")
        if piso and ins[0] < piso["in"]:
            fallos.append(f"{grupo}: entrantes mínimas {ins[0]} < piso {piso['in']}")

    # ── Huérfanas dentro de la sección ────────────────────────────────────
    huerfanas = [
        u for u in paginas
        if u.startswith("/cumplimiento") and not entrantes[u]
    ]
    print(f"\n=== HUÉRFANAS EN /cumplimiento === {len(huerfanas)}")
    for u in sorted(huerfanas):
        print("  ", u)
    if huerfanas:
        fallos.append(f"{len(huerfanas)} página(s) huérfana(s)")

    # ── Puentes desde fuera de la sección ─────────────────────────────────
    print("\n=== PUENTES DESDE FUERA DE /cumplimiento ===")
    for seccion in ("/productos", "/directorio", "/blog"):
        origenes = {
            u for u in paginas
            if u.startswith(seccion)
            and any(d.startswith("/cumplimiento") for d in salientes[u])
        }
        total = sum(1 for u in paginas if u.startswith(seccion))
        estado = "ok" if origenes else "SIN PUENTE"
        print(f"  {seccion:14} {len(origenes):>4} de {total:>4} páginas enlazan a /cumplimiento   {estado}")
        if not origenes:
            fallos.append(f"{seccion} no enlaza a /cumplimiento")

    print()
    if fallos:
        print("FALLA la auditoría:")
        for f in fallos:
            print("  -", f)
        return 1
    print("Auditoría OK: sin rotos, sin huérfanas y todos los grupos sobre su piso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
