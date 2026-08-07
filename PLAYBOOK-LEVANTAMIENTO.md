# Playbook: levantar un estado del directorio de bomberos

Este documento es el estándar. Quien levante un estado lo sigue al pie de la letra.
No es una guía flexible: la consistencia entre los 32 estados es parte del producto.

Proyecto: `/Users/frankoropeza/Documents/Claude/Projects/FIREFIGHTERCOMMX`
Ruta montada para editar archivos: `/sessions/rcw-01myw9qruuvyjbjl2cokhxwj/mnt/FIREFIGHTERCOMMX`

---

## 0. La regla que manda sobre todas

**Publicamos solo datos verificables.** Si un domicilio, teléfono o coordenada no tiene
una fuente pública comprobable, el campo va **vacío** y se marca como pendiente en la
ficha. Nunca se inventan teléfonos, domicilios ni coordenadas. Nunca se "completa por
deducción" un número de teléfono ni se estima una coordenada.

Un teléfono equivocado en un directorio de emergencia es peor que un campo en blanco.

Corolarios:
- Si Maps da un teléfono a 7 dígitos, se le antepone la clave LADA de la ciudad **y se
  anota esa reserva** en la tabla de fuentes.
- Si dos fuentes dan teléfonos distintos, gana la oficial y **la discrepancia se
  documenta** en la ficha.
- Si no se puede resolver a qué municipio pertenece un punto, **se excluye** y se
  documenta con coordenadas y teléfono en la bitácora.

## Fuentes prohibidas

`bombero.mx` y `firefighter.mx` publican estaciones fabricadas, con teléfonos de dígitos
secuenciales. **No usar jamás como fuente**, ni para confirmar.

## Dominios caducados y reutilizados — verifícalo siempre

Varios cuerpos de bomberos dejaron caer su dominio y alguien más lo compró. El sitio
sigue apareciendo en Google con el nombre correcto, pero el contenido ya no es suyo.
Casos confirmados en este proyecto:

- `bomberoscajeme.mx` (Sonora) → portal de apuestas en España.
- `guerreronegro.org/bomberos.html` (BCS) → reseñas de casinos en azerbaiyano.

**Antes de tomar un dato de cualquier portal, confirma que el contenido de la página
sea realmente sobre bomberos de ese municipio.** Si el texto no corresponde, descarta la
fuente completa y anótalo en la bitácora. Un teléfono sacado de un dominio secuestrado
es exactamente el tipo de error que este directorio no se puede permitir.

---

## 1. Orden de trabajo

### Paso 1 — Fuentes oficiales primero, siempre

Ha sido la mejor fuente en todos los estados. Antes de tocar Maps, busca:

- `bomberos <capital> estaciones directorio sitio oficial`
- `bomberos <ciudad grande 2> estaciones directorio sitio oficial`
- `protección civil <estado> directorio unidades municipales`
- `<estado> teléfonos de emergencia protección civil pdf`

Usa `WebSearch` y `WebFetch` con `blocked_domains: ["bombero.mx","firefighter.mx"]`.

Lo que más ha rendido:
- Portales municipales de bomberos con página "Estaciones" (Tijuana, Torreón).
- Directorios estatales de unidades municipales de PC (Tamaulipas).
- PDF estatales de teléfonos de emergencia.

Si un portal está bloqueado por robots o con SSL vencido, **inténtalo en Claude in
Chrome** antes de rendirte. Si sigue sin abrir, anótalo como pendiente en la bitácora.

### Paso 2 — Barrido en Google Maps con Claude in Chrome

Carga las herramientas con **una sola** llamada a ToolSearch:

```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__javascript_tool
```

El navegador ya está seleccionado a nivel de sesión. **No llames a
`list_connected_browsers`** ni a `select_browser`: llama directo a
`tabs_context_mcp` con `createIfEmpty: true` y usa ese `tabId`.

Barre **por región, no por estado completo**. Una búsqueda por zona metropolitana o por
grupo de municipios vecinos. Maps devuelve como máximo ~20 resultados por búsqueda, así
que un solo barrido estatal siempre deja fuera estaciones.

Patrones de URL que funcionan:

```
https://www.google.com/maps/search/bomberos/@<lat>,<lon>,12z?hl=es
https://www.google.com/maps/search/estaci%C3%B3n+de+bomberos/@<lat>,<lon>,12z?hl=es
https://www.google.com/maps/search/bomberos+protecci%C3%B3n+civil+<Muni1>+<Muni2>/@<lat>,<lon>,10z?hl=es
```

Consejo: para una ciudad grande usa `bomberos` a 12z centrado en ella (la consulta corta
devuelve más); para municipios chicos, nómbralos en la consulta a 9-10z.

Tras navegar, corre este script (define el harvester y hace scroll hasta el final):

```js
window.__H = async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  await sleep(3500);
  let feed = document.querySelector('div[role="feed"]');
  for (let i = 0; i < 15 && !feed; i++) { await sleep(1000); feed = document.querySelector('div[role="feed"]'); }
  if (feed) { let last=-1,stable=0; for (let i=0;i<50;i++){ feed.scrollTop=feed.scrollHeight; await sleep(1300); const n=document.querySelectorAll('a.hfpxzc').length; if(n===last){stable++;if(stable>=3)break;}else{stable=0;last=n;} } }
  const a=[...document.querySelectorAll('a.hfpxzc')];
  if(!a.length){ window.__d=['SOLO-FICHA:: '+document.body.innerText.replace(/\n{2,}/g,'\n').slice(0,700)]; return 'FICHA'; }
  window.__d=a.map(x=>{const h=x.getAttribute('href')||'';const m=h.match(/!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)/);const c=x.closest('.Nv2PK');return (x.getAttribute('aria-label')||'').replace('·Enlace visitado','').trim()+' @@ '+(m?m[1]+','+m[2]:'SIN-GPS')+' @@ '+(c?c.innerText.split('\n').map(s=>s.trim()).filter(Boolean).join(' | '):'');});
  return window.__d.length;
};
window.__e=(a,b)=>window.__d.slice(a,b).join('\n###\n');
window.__n=()=>window.__d.map((x,i)=>i+' '+x.split(' @@ ')[0]+' | '+x.split(' @@ ')[1]).join('\n');
await window.__H();
```

Luego lee con `window.__n()` (nombres + GPS) y `window.__e(0,4)`, `window.__e(4,8)`…
para el detalle. **Limitaciones conocidas:**
- La salida se trunca cerca de 1000 caracteres: pide de 3 o 4 en 4.
- Si el resultado contiene URLs completas, la herramienta lo bloquea: devuelve solo
  valores extraídos, nunca `location.href` completo.
- `window.__H` y `window.__d` **se pierden al navegar**: hay que redefinirlos en cada
  página nueva.
- `window.history.back()` mata el contexto JS. No lo uses.

Para confirmar municipio, colonia y CP de un registro dudoso, navega a
`https://www.google.com/maps/search/<Nombre+del+lugar>/@<lat>,<lon>,17z?hl=es` y lee:

```js
await new Promise(r=>setTimeout(r,5000));
const t=document.body.innerText.replace(/\n{2,}/g,'\n');
const m=t.match(/[^\n]*(Coah|Tamps|B\.C|Son|Sin|Jal|Mich|Ver|Oax|Chis|Yuc|Q\. Roo|Camp|Tab|Gro|Mor|Hgo|Qro|S\.L\.P|Dgo|Zac|Nay|Col|Tlax|B\.C\.S)\.[^\n]*/);
const p=t.match(/[A-Z0-9]{4}\+[A-Z0-9]{2,3}[^\n]*/);
(m?m[0]:'?')+' || '+(p?p[0]:'?')
```

### Paso 3 — Reglas de depuración

**Se incluyen:** parques y estaciones de bomberos, cuerpos voluntarios y patronatos con
sede propia, y unidades municipales de protección civil (en municipios chicos suelen ser
las que dan el servicio de bomberos).

**Se excluyen — y se documentan en la bitácora con el motivo:**
- Brigadas industriales de empresa (refinerías, siderúrgicas, minas, maquiladoras).
- Servicios privados de ambulancias y grupos de rescate que no sean bomberos.
- Registros marcados como cerrados permanente o temporalmente.
- Tiendas, talleres y negocios que solo tengan "bomberos" en el nombre.
- Hidrantes, torres de agua, plazas y parques llamados "de los bomberos".
- Estaciones de otro estado o de Estados Unidos que caigan en el viewport.

**Duplicados:** dos registros a menos de **~150 m** que comparten domicilio o teléfono
son la misma corporación (estación + patronato, o central + unidad municipal). Se
fusionan en una ficha y se menciona el segundo registro en el cuerpo.

**Ambigüedad de municipio:** si una coordenada cae en un límite municipal y no se puede
resolver ni por CP, ni por LADA, ni por el panel de Maps, **se excluye** y se documenta.

### Paso 4 — Escribir las fichas

Una ficha por estación, en
`src/content/stations/<slug-del-estado>/<slug-de-la-estacion>.md`.

Para un cuerpo con muchas estaciones homogéneas (más de 8), escribe un script de Python
con los datos en una lista y genera los archivos; ahorra errores de copiado. Para pocas,
escríbelas a mano con heredoc `<<'EOF'`.

#### Frontmatter

Campos del esquema (`src/content.config.ts`). Los opcionales **se omiten si no hay
dato**; nunca se ponen vacíos ni inventados.

```yaml
---
name: "Estación Central de Bomberos de <Ciudad>"     # obligatorio
stationCode: "EB-<XXX>-001"                          # prefijo de 3 letras del estado, correlativo
serviceType: "profesional"   # profesional | voluntario | mixto | industrial | aeroportuario | proteccion-civil
status: "activa"
state: "<Nombre del estado>"
stateSlug: "<slug>"
municipality: "<Municipio>"
city: "<Localidad>"
address: "Calle Tal 123"        # opcional
neighborhood: "Col. Tal"        # opcional
postalCode: "12345"             # opcional
latitude: 20.1234567            # opcional, número sin comillas
longitude: -100.1234567         # opcional
phone: "+52 442 123 4567"       # opcional
adminPhone: "+52 442 123 4568"  # opcional
website: "https://…"            # opcional
emergencyPhone: "911"
operatingHours: "24/7"
services:                       # solo del enum permitido
  - combate-incendios
  - atencion-medica
  - rescate-vehicular
  - proteccion-civil
verified: false                 # true SOLO si domicilio y teléfono vienen de fuente oficial
lastUpdated: "2026-08-06"
metaTitle: "Bomberos <Ciudad> <distintivo>"
metaDescription: "…"
---
```

Enum de `services`: `combate-incendios`, `atencion-medica`, `rescate-vehicular`,
`rescate-acuatico`, `rescate-forestal`, `rescate-montaña`, `materiales-peligrosos`,
`rescate-alturas`, `proteccion-civil`, `capacitacion`, `prevencion`, `explosivos`.

#### Reglas de SEO — se auditan, no son sugerencias

- **`metaTitle` ≤ 44 caracteres.** Empieza por lo distintivo. **Nunca** uses `:`,
  ` — `, ` – ` ni ` | `: `src/lib/seoText.ts` trunca el título en el primer separador y
  colapsaría decenas de títulos en uno solo. Usa `·` si necesitas separar.
- **`metaDescription` entre 110 y 160 caracteres.** Fuera de ese rango la auditoría falla.
- **Todos los `metaTitle` y todas las `metaDescription` del sitio deben ser únicos.**
  Con estaciones numeradas del mismo cuerpo esto se rompe fácil: incluye siempre el
  número o el nombre distintivo de la estación.

#### Cuerpo de la ficha

Estructura fija:

```markdown
## <name>

<Frase de identificación: qué es y dónde está. Una línea.>

<Uno a tres párrafos de contexto REAL del municipio: por qué esa corporación trabaja
como trabaja. Industria dominante, geografía, clima, riesgo característico, historia.
Nada de relleno genérico. Si el municipio es minero, di qué implica; si es costero,
di qué implica. Usa negritas con moderación para el dato que importa.>

## Servicios registrados

- <lista legible de los services del frontmatter>

## Cómo contactarla

| Necesidad | Número |
|---|---|
| **Emergencia en curso** | **911** |
| <Estación> | <teléfono> |

El **911** es gratuito, opera las 24 horas y es el que despacha la unidad más cercana.
Los teléfonos de estación sirven para trámites, capacitación, licitaciones o contacto
administrativo.

---

### Fuentes y estado del dato

| Dato | Estado | Origen |
|---|---|---|
| Domicilio | Verificado | <fuente exacta> |
| Coordenadas GPS | Verificado | Ficha pública de Google Maps del establecimiento |
| Teléfono <número> | Verificado | <fuente exacta> |
| Personal y unidades | **Pendiente** | Sin fuente pública localizada |

Publicamos solo lo que pudimos comprobar. Los campos vacíos lo están porque no
encontramos una fuente que los respalde, no porque no existan. Si detectas un dato
incorrecto o conoces el que falta, [avísanos](/agregar-estacion) y lo corregimos.

*Última revisión: agosto de 2026. Para una emergencia en curso, marca 911.*
```

Si falta el teléfono, en "Cómo contactarla" va una línea explícita:
`**No localizamos un teléfono directo publicado** para esta estación. Marca 911 para
cualquier emergencia.`

Estados posibles en la tabla de fuentes: `Verificado`, `Verificado con reserva`
(con la reserva explicada), y `**Pendiente**` (con el porqué).

#### Tono

Profesional y concreto. Es un directorio de emergencia leído por empresas que necesitan
el dato para su Programa Interno de Protección Civil. Sin adjetivos de folleto, sin
"maravilloso", sin promesas. El contexto del municipio tiene que aportar información
real, no ambiente.

### Paso 5 — Publicar y auditar

```bash
# 1) Conteo real por estado en states.json (usa la ruta MONTADA)
cd /sessions/rcw-01myw9qruuvyjbjl2cokhxwj/mnt/FIREFIGHTERCOMMX
python3 - <<'PY'
import json, os
base='src/content/stations'
counts={d:len([f for f in os.listdir(os.path.join(base,d)) if f.endswith('.md')])
        for d in os.listdir(base) if os.path.isdir(os.path.join(base,d))}
data=json.load(open('src/data/states.json'))
for s in data:
    r=counts.get(s['slug'],0)
    if r and s.get('totalStations')!=r: s['totalStations']=r
json.dump(data,open('src/data/states.json','w'),ensure_ascii=False,indent=2)
print(sum(counts.values()),'fichas en',len(counts),'estados')
PY
```

```bash
# 2) Build y auditoría (usa Desktop_Commander: node_modules es de macOS, NO corre en device_bash)
cd /Users/frankoropeza/Documents/Claude/Projects/FIREFIGHTERCOMMX && rm -rf .astro dist && npm run build 2>&1 | tail -6 && python3 scripts/auditoria/audit-directorio.py <slug-del-estado>
```

La auditoría **debe** terminar en:
`titles duplicados: 0`, `descriptions duplicadas: 0`, `problemas: 0`.
Si no, corrige y vuelve a correr. No se entrega un estado con la auditoría en rojo.

### Paso 6 — Bitácora

Agrega el bloque del estado a `DIRECTORIO-LEVANTAMIENTO.md`, antes de
`## Pendientes de otros estados`, y actualiza la tabla de estados y el total. El bloque
lleva: conteo por municipio, fuentes oficiales encontradas (y las que fallaron),
ambigüedades resueltas, tabla de registros descartados con motivo, municipios buscados
sin resultado, y pendientes.

---

## Notas de entorno

- **`device_bash`** edita el proyecto en la ruta montada. **No corre `npm`** (los
  `node_modules` son binarios de macOS, arquitectura distinta).
- **`Desktop_Commander__start_process`** es la shell real de macOS: ahí van `npm run
  build`, `python3 scripts/…` y todo lo que toque `node_modules`.
- Los heredoc de Python dentro de `Desktop_Commander` a veces se bloquean; si pasa,
  escribe el script a un archivo con `device_bash` y ejecútalo con Desktop_Commander.
- Reescribir `src/content.config.ts` vacía el store de contenido de Astro. Si pasa:
  `pkill -f "astro dev"; rm -rf .astro node_modules/.vite; npm run dev`.
- Nunca reordenes bloques de un `.astro` cortando strings por índice: reescribe el
  archivo completo o usa reemplazos exactos.
