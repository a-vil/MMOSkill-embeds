# MMOSkill-embeds — Documentación Técnica

## Visión General

Sistema modular de gestión y entrega de contenido para habilidades de un MMO.
Pipeline completo: fuente en inglés → traducción al español → embeds de Discord.

---

## Arquitectura

Cada rama de habilidades sigue el mismo patrón:

```
data/*.txt (EN) → data/es_*.py (SkillText ES) → embeds/*.py (builder) → branches/*.py (comando) → bot.py
```

### Ramas Completadas

| Rama | Skills | Comando |
|------|--------|---------|
| Shot | 25 | `!skshot` |
| Magic | 24 | `!skmagic` |
| Blade | 24 | `!skblade` |
| Martial | 23 | `!skmartial` |
| Halberd | 24 | `!skhalberd` |
| **Katana** (WIP) | 24+ | `!skkatana` |
| **Dual** (WIP) | — | `!skdual` |

---

## Estructura del Proyecto

```
MMOSkill-embeds/
├── bot.py                    # Entry point, !clean command
├── branches/
│   ├── _base.py              # BranchHandlers genérico (BranchConfig, comandos)
│   ├── shot.py               # Registro !skshot
│   ├── magic.py              # Registro !skmagic
│   ├── sblade.py             # Registro !skblade
│   ├── martial.py            # Registro !skmartial
│   └── halberd.py            # Registro !skhalberd
├── embeds/
│   ├── shot.py               # Builder Shot (SKILL_KEYS, TIERS, ALIASES)
│   ├── magic.py              # Builder Magic
│   ├── sblade.py             # Builder Blade
│   ├── martial.py            # Builder Martial
│   └── halberd.py            # Builder Halberd (con SKILL_EXTRA)
├── data/
│   ├── es_sshot.py           # SkillText ES — plantilla de referencia
│   ├── es_smagic.py
│   ├── es_sblade.py
│   ├── es_smartial.py
│   ├── es_shalberd.py
│   ├── es_skatana.py         # WIP — traducida, sin implementar
│   ├── sshot.txt / sblade.md / smagic.txt / smartial.md / shalberd.txt / sdual.txt / skatana.txt
│   ├── words_excluded.txt    # Palabras no traducidas
│   └── words_custom.txt      # Traducciones personalizadas con {n}
├── storage/
│   ├── shot_index.py         # Persistencia JSON por guild
│   ├── magic_index.py
│   ├── sblade_index.py
│   ├── martial_index.py
│   └── halberd_index.py
├── imgs/                     # Assets por rama (shot/, magic/, blade/, martial/, halberd/)
├── sort_lists.py             # Ordena listas de traducción
├── .env.example
├── requirements.txt
└── .gitignore
```

---

## Sistema de Embeds

Cada skill produce **2 embeds** en 1 mensaje:
1. **Overview** — título + descripción + thumbnail
2. **Details** — stats, fórmulas, efectos, bonuses

Usa `@dataclass(frozen=True)` con `SkillText(title, description, details)`.

Halberd usa `SKILL_EXTRA` para skills cuyo contenido no entra en 2 embeds (ej: Draconic Charge).

---

## Sistema de Índice

- Se actualiza automáticamente con `all`, `<skill> save`, `scan`, `index`
- Genera links clickeables a los mensajes de Discord
- Edita el índice existente en vez de crear uno nuevo
- Almacenamiento JSON por guild (multi-server safe)

---

## Flujo de Traducción

1. `data/skill.txt` — fuente en inglés
2. `words_excluded.txt` — palabras que no se traducen
3. `words_custom.txt` — traducciones forzadas (prioridad máxima)
4. `data/es_skill.py` — `SkillText` en español (generado con asistencia de IA)
5. `sort_lists.py` — mantiene los diccionarios ordenados alfabéticamente

Reglas:
- Custom > Excluidas > Traducción IA
- Las variables `{placeholder}` se preservan

---

## Sistema de Embeds (detalle)

```python
@dataclass(frozen=True)
class SkillText:
    title: str        # Nombre de la habilidad
    description: str  # Descripción del juego (markdown)
    details: str      # Stats, fórmulas, bonuses (con placeholders {bow}, {arrow}, etc.)
```

Los builders resuelven emojis, imágenes y placeholders, devuelven `list[discord.Embed]` + `list[discord.File]`.

---

## Tecnologías

- Python 3.10+
- discord.py 2.x
- python-dotenv
- pathlib
- dataclasses
- JSON storage