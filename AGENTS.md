# 🤖 AGENTS.md

Este documento contiene instrucciones para agentes de IA que colaboren en el proyecto.

---

## Antes de comenzar

Leer obligatoriamente:

1. [ARCHITECTURE.md](./ARCHITECTURE.md)
2. [REQUIREMENTS.md](./REQUIREMENTS.md)

No asumir comportamientos que no estén documentados.

---

## Objetivo

Ayudar en el desarrollo manteniendo la arquitectura existente.

El objetivo **no** es reescribir el proyecto.

---

## Principios

### Respetar el modelo

`SkillText` es la fuente de verdad.

No generar embeds directamente desde texto.

### No mezclar responsabilidades

Mantener separadas las siguientes capas:

- localización
- normalización
- modelo
- presentación

### Mantener el patrón existente

Nuevas ramas deben seguir exactamente esta estructura:

```
data/*.txt → data/es_*.py → embeds/*.py → branches/*.py → branches/__init__.py → bot.py
```

No introducir arquitecturas distintas para resolver el mismo problema.

### Cambios mínimos

Preferir modificaciones pequeñas antes que grandes refactorizaciones.

---

## Ramas

### Completadas

- Shot (25 skills, `!skshot`)
- Magic (24 skills, `!skmagic`)
- Blade (24 skills, `!skblade`)
- Martial (23 skills, `!skmartial`)
- Halberd (24 skills, `!skhalberd`)

### En progreso (WIP)

- Katana (`data/es_skatana.py` traducida, faltan embeds/storage/branches)
- Dual (solo existe `data/sdual.txt` fuente)

---

## Traducción

Al trabajar en traducciones, **vuelve a leer** `.opencode/skills/translate-en-es/STYLE_GUIDE.md`,
`.opencode/skills/translate-en-es/SKILL.md`,
`data/words_custom.txt` y `data/words_excluded.txt` por completo antes de traducir.

- Las traducciones personalizadas (`words_custom.txt`) tienen prioridad (incluso sobre palabras excluidas).
- Las palabras excluidas (`words_excluded.txt`) nunca se traducen (a menos que tengan una personalizada).
- El resto usa traducción asistida por IA.
- Las variables `{placeholder}` en details deben preservarse exactamente.
- Después de editar `words_custom.txt` o `words_excluded.txt`, ejecutar `sort_lists.py` para mantenerlos ordenados.

---

## Restricciones

No:

- mover archivos sin motivo
- duplicar lógica
- romper compatibilidad
- modificar la estructura de carpetas sin aprobación
- asumir decisiones que afecten al usuario sin preguntar

---

## Flujo recomendado

1. Leer ARCHITECTURE.md
2. Identificar el módulo afectado
3. Implementar únicamente el cambio solicitado
4. Mantener la arquitectura existente
5. Verificar que no se rompe ninguna rama

---

## Al añadir una rama

Seguir este orden consultando [REQUIREMENTS.md](./REQUIREMENTS.md) para los contratos exactos:

1. **Data** — crear `data/es_nombre.py` con `SkillText` de cada skill
2. **Embeds** — crear `embeds/nombre.py` con `SKILL_KEYS`, `TIERS`, `ALIASES`, builders
3. **Storage** — crear `storage/nombre_index.py` con persistencia JSON
4. **Branch** — crear `branches/nombre.py` con `BranchConfig` + `register(bot)`
5. **Registro** — añadir import y `register(bot)` en `branches/__init__.py`
6. **Assets** — crear `imgs/nombre/` con imágenes de cada skill
7. **Entorno** — añadir emoji vars al `.env.example`

No copiar lógica que ya exista en `_base.py`.

---

## Verificación

Después de implementar una rama, verificar:

- `python -c "from branches.nombre import register; print('OK')"` — el módulo importa sin errores
- `branches/__init__.py` importa el nuevo módulo y lo registra en `register_all()`
- `.env.example` tiene las variables de emoji de la nueva rama
- `imgs/nombre/` existe con los assets necesarios
- Las ramas existentes siguen funcionando (verificar imports)

---

## Buenas prácticas

Preferir:

- reutilización
- composición
- funciones pequeñas
- nombres descriptivos
- tipado cuando sea posible

Evitar:

- lógica duplicada
- funciones excesivamente largas
- dependencias circulares
- acoplamiento entre módulos

---

## Objetivo final

El proyecto debe seguir siendo:

- modular
- fácil de extender
- fácil de mantener
- consistente

Toda decisión debe alinearse con los principios descritos en **ARCHITECTURE.md**.