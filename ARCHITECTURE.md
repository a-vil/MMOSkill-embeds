# 🏗 Architecture

Este documento describe la arquitectura del proyecto y sirve como la **única fuente de verdad** para entender su funcionamiento interno.

---

## Visión General

Sistema modular de gestión y entrega de contenido para habilidades de un MMO.
Flujo asistido por IA: fuente en inglés → localización al español → embeds de Discord.

---

## Principios de diseño

### Model First

Toda la información se transforma primero a un modelo (`SkillText`).

Nunca se generan embeds directamente desde texto plano.

### Separation of Concerns

Cada módulo tiene una responsabilidad específica.

```
Input                       ← data/*.txt (fuente EN)
  │
  ▼
Localization                ← translate-en-es (skill IA)
  │                           + words_custom.txt / words_excluded.txt
  ▼                           + STYLE_GUIDE.md
Normalization
  │
  ▼
Domain Model                ← SkillText (datos estructurados)
  │
  ▼
Presentation                ← embed-integration (skill IA)
                                → embeds/*.py → branches/*.py → bot.py
```

### Localización Determinista

La skill translate-en-es genera el SkillText en dos fases:

**Fase 1 — Restricciones durante la generación:**
- Diccionarios personalizados (words_custom.txt) — prioridad máxima
- Términos excluidos (words_excluded.txt) — se preservan en inglés
- Guía de estilo (STYLE_GUIDE.md) — naturalidad, terminología, formato

**Fase 2 — Verificación post-generación:**
- Evaluación contra el checklist completo de STYLE_GUIDE.md (§1–§8)
- Confirmación de que palabras excluidas no se localizaron
- Confirmación de que traducciones custom se aplicaron correctamente
- Documentación de hallazgos para corrección manual

sort_lists.py mantiene los diccionarios ordenados alfabéticamente tras cada edición.

### Modular Branches

Cada rama implementa exactamente la misma estructura:

```
data/*.txt (EN) → data/es_*.py (SkillText ES) → embeds/*.py (builder) → branches/*.py (comando) → branches/__init__.py (registro) → bot.py
```

Además del módulo `branches/X.py`, cada rama debe registrarse en `branches/__init__.py` — importar el módulo y añadir `nueva_rama.register(bot)` en `register_all()`.

Para los contratos exactos que debe cumplir cada módulo, consultar [REQUIREMENTS.md](./REQUIREMENTS.md).

### AI Skills

El proceso de creación de ramas se apoya en dos skills de opencode:

- **translate-en-es** — genera `data/es_*.py` desde texto fuente, aplicando diccionarios, exclusiones y guía de estilo con verificación post-generación
- **embed-integration** — genera los módulos de embeds, storage y branch siguiendo el patrón de las ramas existentes

Estas skills no forman parte del runtime del bot; asisten durante el desarrollo.

---

## Ramas

| Rama | Skills | Comando | Estado |
|------|-------:|---------|--------|
| Shot | 25 | `!skshot` | ✅ |
| Magic | 24 | `!skmagic` | ✅ |
| Blade | 24 | `!skblade` | ✅ |
| Martial | 23 | `!skmartial` | ✅ |
| Halberd | 24 | `!skhalberd` | ✅ |
| Katana | 24+ | `!skkatana` | WIP |
| Dual | — | `!skdual` | WIP |

---

## Sistema de Embeds

Cada skill produce **2 embeds** en 1 mensaje:
1. **Overview** — título + descripción + thumbnail
2. **Details** — stats, fórmulas, efectos, bonuses

El modelo de dominio:

```python
@dataclass(frozen=True)
class SkillText:
    title: str        # Nombre de la habilidad
    description: str  # Descripción del juego
    details: str      # Stats, fórmulas, efectos y bonuses
```

Halberd usa `SKILL_EXTRA` para skills cuyo contenido no entra en 2 embeds (ej: Draconic Charge).

Los builders resuelven emojis, imágenes y placeholders, devolviendo `list[discord.Embed]` + `list[discord.File]`.

---

## Sistema de Índice

- Se actualiza automáticamente con `all`, `<skill> save`, `scan`, `index`
- Genera links clickeables a los mensajes de Discord
- Edita el índice existente en vez de crear uno nuevo
- Almacenamiento JSON por guild (multi-server safe)

---

## Flujo de Localización

1. `data/skill.txt` — fuente en inglés
2. `words_excluded.txt` — palabras que no se localizan
3. `words_custom.txt` — traducciones personalizadas (prioridad máxima)
4. `data/es_skill.py` — `SkillText` en español (generado por la skill translate-en-es)
5. `sort_lists.py` — mantiene los diccionarios ordenados alfabéticamente

Reglas:
- Custom > Excluidas > Localización IA
- Las variables `{placeholder}` se preservan
- La skill translate-en-es verifica el output contra STYLE_GUIDE.md post-generación

---

## Dependencias entre módulos

```text
branches
    │
    ▼
embeds
    │
    ▼
SkillText
    ▲
    │
data
```

La dirección de las dependencias debe mantenerse.

---

## Estructura del proyecto

```text
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

## Decisiones importantes

### ¿Por qué SkillText?

Porque desacopla completamente:

- procesamiento
- almacenamiento
- presentación

Esto permite reutilizar la información para otros exportadores sin modificar el flujo de localización.

### ¿Por qué no traducir directamente?

La IA puede producir resultados inconsistentes.

Por eso existe una etapa de normalización basada en reglas del dominio (diccionarios, exclusiones, terminología).

---

## Tecnologías

- Python 3.10+
- discord.py 2.x
- python-dotenv
- pathlib
- dataclasses
- JSON storage

---

## Posibles extensiones

El modelo podría exportarse a:

- Discord (actual)
- JSON
- Markdown
- HTML
- Wiki
- API REST

Sin modificar el flujo de localización.

---

> 📋 Para los contratos y convenciones de implementación, ver [REQUIREMENTS.md](./REQUIREMENTS.md).