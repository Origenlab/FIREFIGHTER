# Design System — FIREFIGHTER México

> Documento maestro de tokens, patrones y reglas de diseño. Aplica a todos los módulos del sitio.

---

## Stack técnico

| Elemento | Tecnología |
|---|---|
| Framework | Astro SSG |
| Estilos layout | Inline styles + clases Tailwind |
| Grid / spacing | Tailwind (`grid-cols-*`, `gap-*`) |
| Estilos propiedades visuales | Inline style siempre |
| **Regla crítica** | ❌ No usar `<style>` scoped para layout en Astro |

---

## Tokens de color

| Token | Valor HEX | Uso |
|---|---|---|
| Accent red | `#dc2626` | CTAs, badges, eyebrow, highlights, accents |
| Dark base | `#09090b` | Títulos H2/H3, texto fuerte, footer bg |
| Body gray | `#52525b` | Párrafos SEO, texto secundario |
| Muted | `#71717a` | Descripción cards, texto de apoyo |
| Subtle | `#a1a1aa` | Labels menores, sub-stats |
| Border | `#e4e4e7` | Bordes de cards, separadores de sección |
| Surface white | `#ffffff` | Fondo de cards, secciones impares |
| Surface gray | `#f8fafc` | Fondo de secciones pares |
| Pill bg | `#f4f4f5` | Pills de productos/items dentro de cards |
| Highlight bg | `#fef2f2` | Chip highlight rojo claro |
| Footer main | `#09090b` | Fondo footer columnas |
| Footer strip | `#111111` | Certs strip |
| Footer bottom | `#000000` | Bottom bar |

---

## Tipografía

| Elemento | font-size | font-weight | Notas |
|---|---|---|---|
| H2 sección | `clamp(1.9rem,2.8vw,2.7rem)` | 800 | `letter-spacing:-0.02em; line-height:1.1` |
| H3 card | `1.05rem` | 700 | `line-height:1.3` |
| Eyebrow | `0.7rem` | 700 | `letter-spacing:0.15em; text-transform:uppercase` |
| Label SEO | `0.72rem` | 700 | `letter-spacing:0.1em; text-transform:uppercase` |
| Párrafo SEO | `0.9rem` | 400 | `line-height:1.85` |
| Descripción card | `0.78rem` | 400 | `line-height:1.7; color:#71717a` |
| Badge card | `0.62rem` | 800 | `letter-spacing:0.06em; text-transform:uppercase` |
| Pill item | `0.68rem` | 400 | `color:#3f3f46; background:#f4f4f5` |
| Sector tag | `0.67rem` | 400 | `border:1px solid #e4e4e7; border-radius:99px` |
| Highlight chip | `0.68rem` | 600 | `color:#dc2626; background:#fef2f2` |
| CTA card | `0.8rem` | 600 | `color:#dc2626` |

---

## Patrón de eyebrow (universal)

```html
<div style="display:flex; align-items:center; gap:10px; margin-bottom:20px;">
  <span style="display:block; width:24px; height:2px; background:#dc2626; flex-shrink:0; border-radius:2px;"></span>
  <span style="font-size:0.7rem; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#dc2626;">
    Texto Eyebrow
  </span>
</div>
```

---

## Header 50/50 (universal — todas las secciones)

```html
<div class="grid grid-cols-1 lg:grid-cols-2 gap-16" style="align-items:center; margin-bottom:64px;">

  <!-- Columna izquierda: eyebrow + H2 -->
  <div>
    <!-- [eyebrow] -->
    <h2 style="font-size:clamp(1.9rem,2.8vw,2.7rem); font-weight:800; color:#09090b; line-height:1.1; margin:0; letter-spacing:-0.02em;">
      Título principal<br>en dos líneas
    </h2>
  </div>

  <!-- Columna derecha: dos bloques SEO -->
  <div style="display:flex; flex-direction:column; gap:28px;">
    <div>
      <span style="display:block; font-size:0.72rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#09090b; margin-bottom:10px;">
        Label SEO Primario
      </span>
      <p style="font-size:0.9rem; color:#52525b; line-height:1.85; margin:0;">
        Párrafo con <strong style="color:#09090b; font-weight:600;">keyword principal en negrita</strong> desarrollado para SEO.
      </p>
    </div>
    <div style="padding-top:28px; border-top:1px solid #f0f0f0;">
      <span style="display:block; font-size:0.72rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#09090b; margin-bottom:10px;">
        Label SEO Secundario
      </span>
      <p style="font-size:0.9rem; color:#52525b; line-height:1.85; margin:0;">
        Segundo párrafo complementario con <strong style="color:#09090b; font-weight:600;">segunda keyword</strong>.
      </p>
    </div>
  </div>

</div>
```

---

## Patrón de card (universal — homologado)

Estructura fija en todos los módulos: ProductCategories, WhyFirefighter, Sectors, ContactChannels.

```html
<div style="background:#fff; border:1px solid #e4e4e7; border-radius:14px; overflow:hidden; display:flex; flex-direction:column; transition:box-shadow 0.2s ease, transform 0.2s ease;"
     class="hover:-translate-y-1 hover:shadow-lg">

  <!-- ── Header card ── -->
  <div style="padding:24px 24px 0;">
    <!-- Badge -->
    <span style="display:inline-block; background:#dc2626; color:#fff; font-size:0.62rem; font-weight:800;
                 letter-spacing:0.06em; padding:3px 9px; border-radius:4px; text-transform:uppercase; margin-bottom:14px;">
      BADGE TEXT
    </span>
    <!-- Título -->
    <h3 style="font-size:1.05rem; font-weight:700; color:#09090b; margin:0 0 10px; line-height:1.3;">
      Título de la card
    </h3>
    <!-- Descripción -->
    <p style="font-size:0.78rem; color:#71717a; line-height:1.7; margin:0 0 18px;">
      Descripción breve de la card con detalle de lo que incluye o para qué sirve.
    </p>
  </div>

  <!-- ── Body card ── -->
  <div style="padding:0 24px 24px; display:flex; flex-direction:column; flex:1;">

    <!-- Separator: "Incluye" / "Productos" / "Equipo incluido" -->
    <div style="display:flex; align-items:center; gap:8px; margin-bottom:10px;">
      <span style="font-size:0.62rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#a1a1aa;">
        Incluye
      </span>
      <div style="flex:1; height:1px; background:#f4f4f5;"></div>
    </div>
    <!-- Pills 2 columnas (6 items) -->
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:5px; margin-bottom:18px;">
      <span style="font-size:0.68rem; color:#3f3f46; background:#f4f4f5; padding:5px 8px; border-radius:5px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; line-height:1.4;">Item 1</span>
      <span style="font-size:0.68rem; color:#3f3f46; background:#f4f4f5; padding:5px 8px; border-radius:5px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; line-height:1.4;">Item 2</span>
      <!-- ... 4 más -->
    </div>

    <!-- Separator: "Aplica para" -->
    <div style="display:flex; align-items:center; gap:8px; margin-bottom:10px;">
      <span style="font-size:0.62rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#a1a1aa;">
        Aplica para
      </span>
      <div style="flex:1; height:1px; background:#f4f4f5;"></div>
    </div>
    <!-- Sector tags (3 pills) -->
    <div style="display:flex; flex-wrap:wrap; gap:5px; margin-bottom:18px;">
      <span style="font-size:0.67rem; color:#52525b; background:#fff; border:1px solid #e4e4e7; padding:4px 9px; border-radius:99px; line-height:1.4;">Sector</span>
    </div>

    <!-- Chip highlight -->
    <div style="display:flex; align-items:center; gap:7px; padding:9px 12px; border-radius:8px; background:#fef2f2;">
      <svg width="12" height="12" fill="#dc2626" viewBox="0 0 20 20" style="flex-shrink:0;">
        <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
      </svg>
      <span style="font-size:0.68rem; font-weight:600; color:#dc2626;">Highlight diferenciador</span>
    </div>

    <!-- CTA arrow link -->
    <a
      href="[URL]"
      target="_blank"
      rel="noopener"
      style="margin-top:18px; border-top:1px solid #f4f4f5; padding-top:16px; display:flex; align-items:center; justify-content:space-between; font-size:0.8rem; font-weight:600; color:#dc2626; text-decoration:none;"
    >
      <span>Texto del CTA</span>
      <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
      </svg>
    </a>

  </div>
</div>
```

---

## Stats strip (gap:1px trick)

```html
<div class="grid grid-cols-2 lg:grid-cols-4 gap-px"
     style="background:#e4e4e7; border:1px solid #e4e4e7; border-radius:14px; overflow:hidden; margin-bottom:48px;">
  <div style="background:#fff; padding:28px 24px; text-align:center;">
    <div style="font-size:1.9rem; font-weight:800; color:#09090b; line-height:1; letter-spacing:-0.02em;">500+</div>
    <div style="font-size:0.78rem; font-weight:600; color:#3f3f46; margin-top:6px;">Proyectos entregados</div>
    <div style="font-size:0.68rem; color:#a1a1aa; margin-top:3px;">en 32 estados</div>
  </div>
  <!-- Repetir para cada stat -->
</div>
```

---

## Reglas de secciones

| Regla | Valor |
|---|---|
| Padding estándar | `padding:96px 0` |
| Fondo secciones impares | `background:#ffffff` |
| Fondo secciones pares | `background:#f8fafc` |
| Separador entre secciones | `border-top:1px solid #e4e4e7` |
| Container | clase `container-custom` |
| Gap cards 4-col | `gap-6` |
| Gap cards 3-col | `gap-6` |
| Border-radius cards | `14px` |
| Hover cards | `hover:-translate-y-1 hover:shadow-lg` |

---

## Grid layouts usados

| Módulo | Grid |
|---|---|
| ProductCategories | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4` |
| WhyFirefighter | `md:grid-cols-2 lg:grid-cols-3` |
| Sectors | `md:grid-cols-2 lg:grid-cols-3` |
| ContactChannels | `md:grid-cols-3` |
| Testimonials | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4` |
| Footer main | `grid-cols-1 md:grid-cols-2 lg:grid-cols-5` |
