# Sistema de Diseño - Cards

Este documento define el diseño estándar de cards para todo el sitio Firefighter México.

## Principios de Diseño

1. **Claridad** - Información esencial sin distracciones
2. **Consistencia** - Mismo patrón visual en todo el sitio
3. **Accesibilidad** - Contraste adecuado y elementos clickeables claros
4. **Rendimiento** - Sin animaciones pesadas ni elementos decorativos innecesarios

---

## Estructura Base de Card

```
┌─────────────────────────────────────┐
│ ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔ │  ← Barra de acento (4px)
│                                     │
│  [Contenido]                        │
│                                     │
└─────────────────────────────────────┘
```

---

## Estilos CSS Base

```css
/* Card Container */
.card {
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 0.75rem;        /* 12px */
  overflow: hidden;
  transition: box-shadow 0.2s ease;
}

.card:hover {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

/* Barra de Acento Superior */
.card-accent {
  height: 4px;
  width: 100%;
  background-color: #dc2626;     /* Rojo para estaciones */
}

/* Padding Estándar */
.card-content {
  padding: 1.25rem;              /* 20px */
}
```

---

## Paleta de Colores

### Colores de Acento (Barra Superior)

| Tipo | Color | Hex |
|------|-------|-----|
| Profesional | Rojo | `#dc2626` |
| Voluntario | Azul | `#2563eb` |
| Industrial | Ámbar | `#d97706` |
| Aeroportuario | Púrpura | `#9333ea` |
| Protección Civil | Verde | `#059669` |

### Colores de Texto

| Elemento | Color | Hex |
|----------|-------|-----|
| Título | Slate 900 | `#0f172a` |
| Subtítulo | Slate 600 | `#475569` |
| Texto secundario | Slate 500 | `#64748b` |
| Texto muted | Slate 400 | `#94a3b8` |

### Colores de UI

| Elemento | Color | Hex |
|----------|-------|-----|
| Fondo card | Blanco | `#ffffff` |
| Borde | Slate 200 | `#e2e8f0` |
| Separador | Slate 100 | `#f1f5f9` |
| Fondo sección | Slate 50 | `#f8fafc` |
| Estado activo | Verde 600 | `#16a34a` |

---

## Tipos de Cards

### 1. Station Card (Estación de Bomberos)

Uso: Listados de estaciones en directorio y búsqueda.

```html
<article class="bg-white rounded-xl overflow-hidden"
         style="border: 1px solid #e2e8f0;">
  <!-- Barra de acento -->
  <div class="h-1 w-full" style="background-color: #dc2626;"></div>

  <div class="p-5">
    <!-- Badge + Estado -->
    <div class="flex items-center justify-between mb-3">
      <span class="px-2.5 py-1 rounded text-xs font-semibold"
            style="background-color: #dc262612; color: #dc2626;">
        Profesional
      </span>
      <span class="flex items-center gap-1.5 text-xs font-medium"
            style="color: #16a34a;">
        <span class="w-1.5 h-1.5 rounded-full"
              style="background-color: #16a34a;"></span>
        Activa
      </span>
    </div>

    <!-- Nombre -->
    <h3 class="font-bold text-lg mb-2" style="color: #0f172a;">
      Nombre de Estación
    </h3>

    <!-- Ubicación -->
    <p class="text-sm font-medium mb-1" style="color: #475569;">
      Municipio, Estado
    </p>
    <p class="text-sm mb-4" style="color: #64748b;">
      Dirección completa
    </p>

    <!-- Servicios -->
    <div class="flex flex-wrap gap-1.5 mb-4 pb-4"
         style="border-bottom: 1px solid #f1f5f9;">
      <span class="px-2 py-0.5 rounded text-xs font-medium"
            style="background-color: #f1f5f9; color: #475569;">
        Servicio
      </span>
    </div>

    <!-- Acciones -->
    <div class="flex gap-3">
      <a href="tel:..." class="flex-1 flex items-center justify-center gap-2
                               py-2.5 rounded-lg text-sm font-semibold"
         style="background-color: #f8fafc; color: #334155; border: 1px solid #e2e8f0;">
        Llamar
      </a>
      <a href="..." class="flex-1 flex items-center justify-center
                          py-2.5 rounded-lg text-sm font-semibold"
         style="background-color: #dc2626; color: white;">
        Ver detalles
      </a>
    </div>
  </div>
</article>
```

### 2. State Card (Estado)

Uso: Grid de estados en la página principal.

```html
<a href="/directorio/estado"
   class="group bg-white rounded-xl overflow-hidden transition-shadow hover:shadow-md"
   style="border: 1px solid #e2e8f0;">
  <div class="h-1 w-full" style="background-color: #dc2626;"></div>
  <div class="p-4">
    <div class="flex items-center justify-between gap-2">
      <div class="min-w-0">
        <h3 class="font-semibold text-sm truncate" style="color: #0f172a;">
          Nombre del Estado
        </h3>
        <p class="text-xs mt-0.5" style="color: #64748b;">
          X estaciones
        </p>
      </div>
      <svg class="w-4 h-4 flex-shrink-0" style="color: #94a3b8;">
        <!-- Chevron right -->
      </svg>
    </div>
  </div>
</a>
```

### 3. Featured Station Card (Estación Destacada)

Uso: Sección de estaciones destacadas en home.

Igual que Station Card pero puede incluir información adicional como estadísticas.

---

## Reglas de Diseño

### Hacer

- Usar la barra de color superior para identificar tipo
- Mantener padding consistente (20px)
- Usar bordes sutiles (#e2e8f0)
- Hover simple con sombra suave
- Botones claros: secundario (gris) y primario (rojo)

### No Hacer

- No usar emojis
- No usar animaciones complejas
- No usar sombras excesivas
- No usar gradientes decorativos
- No agregar elementos que no aporten información

---

## Componentes Relacionados

- `src/components/ui/Card.astro` - Componente base
- `src/components/directory/StationCard.astro` - Card de estación
- `src/components/home/FeaturedStations.astro` - Cards destacadas
- `src/components/home/StatesGrid.astro` - Grid de estados

---

## Breakpoints

| Nombre | Ancho | Cards por fila |
|--------|-------|----------------|
| Mobile | < 640px | 1-2 |
| Tablet | 640-1024px | 2-3 |
| Desktop | > 1024px | 3-4 |

---

## Accesibilidad

- Contraste mínimo de texto: 4.5:1
- Elementos clickeables con área mínima de 44x44px
- Estados hover visibles
- Links con underline en hover
- Semántica correcta (article, h3, etc.)
