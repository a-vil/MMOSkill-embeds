---
name: embed-integration
description: Crea los 5 archivos necesarios para integrar un nuevo tree de skills (embeds, storage, branch, __init__, .env.example) siguiendo el patrón de shot, magic y blade.
---

# Integración de nuevo tree de skills

## Flujo completo

```
data/es_<tree>.py  →  embeds/<tree>.py  →  storage/<tree>_index.py  →  branches/<tree>.py  →  branches/__init__.py  →  bot.py  +  .env.example
```

## 1. storage/<tree>_index.py

Copia exacta de `storage/shot_index.py` cambiando solo:

| Template | Cambiar |
|----------|---------|
| `INDEX_FILE = ... / "shot_index.json"` | `"<tree>_index.json"` |
| `logger.error("shot_index.json ...")` | `"<tree>_index.json ..."` |

Mismas 5 funciones: `load_index`, `save_index`, `save_skill`, `save_index_message`, `get_guild_data`.

## 2. embeds/<tree>.py

### Imports

```python
from pathlib import Path
import os
import re

import discord

from data.es_<tree> import (
    FOOTER,
    INDEX_HEADER,
    SkillText,
    SKILL_NAME_1,
    SKILL_NAME_2,
    # ... todos los SkillText
)
```

### Helper functions (idénticas en todos los trees)

```python
BASE_IMG_PATH = Path(__file__).resolve().parent.parent / "imgs" / "<tree>"

def _emoji(env_name: str, fallback: str) -> str:
    return os.getenv(env_name) or fallback

def _fmt(text: str, kwargs: dict) -> str:
    placeholders = set(re.findall(r"\{(\w+)\}", text))
    needed = {k: v for k, v in kwargs.items() if k in placeholders}
    return text.format(**needed)
```

### SKILL_KEYS

```python
SKILL_KEYS: dict[str, SkillText] = {
    "skillkey1": SKILL_NAME_1,
    "skillkey2": SKILL_NAME_2,
    # ...
}
```

Las keys se generan con `_normalize()` sobre el nombre en inglés: minúsculas, sin espacios, guiones ni guiones bajos.

### ALIASES

```python
ALIASES: dict[str, str] = {
    "alias1": "skillkey1",
    "alias2": "skillkey2",
    # ...
}
```

Cada skill debe tener al menos un alias corto (3-6 chars) para búsqueda rápida.

### TIERS

```python
TIERS: dict[str, list[str]] = {
    "t1": ["skillkey1", "skillkey2"],
    "t2": [...],
    # ...
}

SKILL_TIER: dict[str, str] = {}
for tier_key, skill_list in TIERS.items():
    for sk in skill_list:
        SKILL_TIER[sk] = tier_key.upper()
```

### SKILL_IMAGES

```python
SKILL_IMAGES: dict[str, str] = {
    "skillkey1": "filename.png",
    # ...
}
```

Mapea skill_key → filename en `imgs/<tree>/`. Si no hay imágenes aún, dejar `SKILL_IMAGES: dict[str, str] = {}`.

### SKILL_EMOJIS

```python
SKILL_EMOJIS: dict[str, str] = {
    SKILL_NAME_1.title: "SKILL_NAME_1_EMOJI",
    SKILL_NAME_2.title: "SKILL_NAME_2_EMOJI",
    # ...
}
```

Estos son los emojis que aparecen en el índice al lado de cada skill name. Las env vars van en `.env.example`.

### TIER_ORDER

```python
TIER_ORDER = {"T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4}
```

Si hay un tier T0 (skills especiales como `ELEMENTAL_NAMES`), se ordena al final con un índice alto:
```python
TIER_ORDER = {"T0": 5, "T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4}
```

### OPCIONAL: SKILL_EMOJI_KEYS (emojis en fmt)

Solo si alguna skill usa placeholders de otras skills en su texto (ej: Qadal usa `{arrows}` para referenciar Magic: Arrows).

```python
SKILL_EMOJI_KEYS: dict[str, str] = {
    name.lower().replace(": ", "").replace(" ", ""): env
    for name, env in SKILL_EMOJIS.items()
}
```

Luego en `get_skill_embeds` se agregan al fmt:
```python
fmt.update({k: _emoji(v, "") for k, v in SKILL_EMOJI_KEYS.items()})
```

Verificar si `es_<tree>.py` contiene placeholders `{palabra}` que no sean de armas — si no, este paso es innecesario.

### OPCIONAL: SKILL_EXTRA (contenido extra)

Solo si alguna skill tiene más texto del que cabe en un embed y necesita un mensaje follow-up.

```python
SKILL_EXTRA: dict[str, str] = {
    "skillkey": SKILL_NAME_EXTRA,
}
```

Donde `SKILL_NAME_EXTRA` es una variable string definida en `es_<tree>.py`.

### OPCIONAL: SKILL_DIAGRAMS (imagen inline)

Solo si alguna skill necesita una imagen inline en el embed de detalles (no thumbnail, sino `set_image()`).

```python
SKILL_DIAGRAMS: dict[str, str] = {
    "skillkey": "diagram.png",
}
```

### Funciones públicas requeridas

```python
def _normalize(name: str) -> str:
    return re.sub(r"[\s_-]+", "", name.lower()).strip()

def _get_image_path(skill_key: str) -> Path | None:
    fname = SKILL_IMAGES.get(skill_key)
    if fname is None:
        return None
    p = BASE_IMG_PATH / fname
    return p if p.exists() else None

def resolve_skill(name: str) -> str | None:
    raw = name.strip()
    norm = _normalize(raw)
    if norm in SKILL_KEYS:
        return norm
    if norm in ALIASES:
        return ALIASES[norm]
    return None
```

### get_skill_embeds

```python
def get_skill_embeds(skill_key: str) -> tuple[list[discord.Embed], list[discord.Embed], list[discord.File]]:
    skill = SKILL_KEYS[skill_key]

    # Resolver placeholders de armas
    weapon_emoji = _emoji("WEAPON_EMOJI", "Weapon")
    all_emoji = _emoji("ALL_EMOJI", "")
    all_weapons = f"{weapon_emoji}" if not all_emoji else all_emoji
    fmt = {"all": all_weapons}
    # Agregar más placeholders según el tree

    # OPCIONAL: emojis de skills en fmt
    # fmt.update({k: _emoji(v, "") for k, v in SKILL_EMOJI_KEYS.items()})

    overview = discord.Embed(
        title=skill.title,  # OPCIONAL: title=None si skill_key == "especial"
        description=skill.description,
        color=discord.Color.blue(),
    )

    img_path = _get_image_path(skill_key)
    files: list[discord.File] = []
    if img_path:
        filename = img_path.name
        overview.set_thumbnail(url=f"attachment://{filename}")
        files.append(discord.File(img_path, filename=filename))

    details = discord.Embed(
        description=_fmt(skill.details, fmt),
        color=discord.Color.blue(),
    )

    # OPCIONAL: diagrama inline
    # diagram_fname = SKILL_DIAGRAMS.get(skill_key)
    # if diagram_fname:
    #     ...

    details.set_footer(text=FOOTER)

    embeds = [overview, details]

    # OPCIONAL: extra embeds
    extra_embeds: list[discord.Embed] = []
    # extra_text = SKILL_EXTRA.get(skill_key)
    # if extra_text is not None:
    #     ...

    return embeds, extra_embeds, files
```

### get_tier_embeds / get_tier_skill_keys

```python
def get_tier_embeds(tier_key: str) -> list[tuple[list[discord.Embed], list[discord.Embed], list[discord.File]]]:
    skill_keys = TIERS.get(tier_key)
    if skill_keys is None:
        return []
    return [get_skill_embeds(sk) for sk in skill_keys]

def get_tier_skill_keys(tier_key: str) -> list[str]:
    return TIERS.get(tier_key, [])
```

### get_skills_index_embed

```python
def get_skills_index_embed(guild_id: int, skills: dict) -> discord.Embed:
    embed = discord.Embed(color=discord.Color.blue())
    description_lines = list(INDEX_HEADER)
    sorted_skills = sorted(
        skills.values(),
        key=lambda s: (TIER_ORDER.get(s["tier"], 99), s["name"]),
    )
    for skill in sorted_skills:
        # OPCIONAL: saltar T0 para procesarlo aparte
        # if skill["tier"] == "T0":
        #     continue
        link = f"https://discord.com/channels/{guild_id}/{skill['channel_id']}/{skill['message_id']}"
        emoji_env = SKILL_EMOJIS.get(skill["name"])
        skill_emoji = _emoji(emoji_env, "") if emoji_env else ""
        emoji_part = f" {skill_emoji}" if skill_emoji else ""
        description_lines.append(f"{skill['tier']}{emoji_part} [{skill['name']}]({link})")

    # OPCIONAL: procesar T0 aparte con prefijo "Otros:"
    # if t0_skills:
    #     ...

    embed.description = "\n".join(description_lines)
    embed.set_footer(text="📌Nota: Puedes usar el mensaje fijado, para volver aquí.")
    return embed
```

## 3. branches/<tree>.py

> La lógica de comandos (list, index, nuke, scan, etc.) ya está implementada en `_base.py`.
> El branch solo configura los parámetros específicos del tree.

### Imports

```python
from embeds.<tree> import (
    SKILL_KEYS,
    TIERS,
    SKILL_TIER,
    get_skill_embeds,
    get_tier_skill_keys,
    get_skills_index_embed,
    resolve_skill,
)
from storage.<tree>_index import (
    get_guild_data,
    save_index_message,
    save_skill,
    load_index,
    save_index,
)
from ._base import BranchConfig, BranchHandlers
```

### TITLE_TO_KEY

```python
TITLE_TO_KEY: dict[str, str] = {st.title: sk for sk, st in SKILL_KEYS.items()}
```

### HELP

```python
HELP = [
    f"**!sk<tree> <skill>** — Muestra una skill",
    f"**!sk<tree> <skill> save** — Muestra y registra en el índice",
    f"**!sk<tree> <tier>** — Muestra un tier completo (t1-t5)",
    f"**!sk<tree> all** — Muestra todas las skills",
    f"**!sk<tree> list** — Lista de skills disponibles",
    f"**!sk<tree> index** — Muestra el índice actual",
    f"**!sk<tree> nuke** — Elimina mensajes del bot e índice en este canal",
    f"**!sk<tree> scan** — Escanea el canal y registra skills ya enviadas",
]
```

### BranchConfig

5 tiers (estándar):

```python
config = BranchConfig(
    command_name="sk<tree>",
    display_name="<Tree>",
    skill_keys=SKILL_KEYS,
    tiers=TIERS,
    skill_tier=SKILL_TIER,
    title_to_key=TITLE_TO_KEY,
    tier_order={"T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4},
    tier_list=("t1", "t2", "t3", "t4", "t5"),
    get_skill_embeds=get_skill_embeds,
    get_tier_skill_keys=get_tier_skill_keys,
    get_skills_index_embed=get_skills_index_embed,
    resolve_skill=resolve_skill,
    get_guild_data=get_guild_data,
    save_skill=save_skill,
    save_index_message=save_index_message,
    load_index=load_index,
    save_index=save_index,
    help_lines=HELP,
)
```

Con T0 (skills especiales como `ELEMENTAL_NAMES`):

```python
config = BranchConfig(
    ...
    tier_order={"T0": 5, "T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4},
    tier_list=("t0", "t1", "t2", "t3", "t4", "t5"),
    ...
)
```

### Registro

```python
handlers = BranchHandlers(config)


def register(bot):
    handlers.register(bot)
```

### Opcionales de BranchConfig

| Campo | Uso | Ejemplo |
|-------|-----|---------|
| `nuke_method` | `"purge"` para limpiar por autor, `"title_scan"` (default) por título | `nuke_method="purge"` |
| `resolve_embeds` | Callable para post-procesar embeds (ej: resolver links) | `resolve_embeds=my_func` |
| `send_all_direct` | `True` si `resolve_embeds` necesita aplicarse en `all` | `send_all_direct=True` |
| `display_name` | Nombre mostrado en listas de ayuda | `display_name="Shot"` |

Los mensajes (`index_updated_msg`, `index_created_msg`, etc.) tienen defaults en `BranchConfig`. Solo se sobrescriben si se necesita texto personalizado.

## 4. branches/__init__.py

Añadir el import y el registro en `register_all()`:

```python
from . import shot, magic, sblade, martial, halberd, <tree>


def register_all(bot):
    shot.register(bot)
    magic.register(bot)
    sblade.register(bot)
    martial.register(bot)
    halberd.register(bot)
    <tree>.register(bot)
```

> `bot.py` ya importa `register_all` de `branches` y lo ejecuta. No necesita modificaciones.

## 5. .env.example

Agregar al final del archivo:

```env
# Weapon icons for <tree> skills
<TREE>_EMOJI=

# Skill icons for the <Tree> Skills Index
SKILL_1_EMOJI=
SKILL_2_EMOJI=
# ... una por skill
```

## 6. Verificación: Límite de descripciones

Discord limita `description` de un embed a **4096 caracteres**. El build
actual crea un embed de overview con `skill.description` y un embed de
details con `skill.details` — cualquiera de los dos puede exceder el límite.

Después de generar `data/es_<tree>.py`, ejecutar:

```bash
python -c "
import sys; sys.path.insert(0, '.')
import data.es_<tree> as mod
from data.es_<tree> import SkillText

LIMIT = 4096
for name in dir(mod):
    obj = getattr(mod, name)
    if isinstance(obj, SkillText):
        desc_len = len(obj.description)
        dets_len = len(obj.details)
        if desc_len > LIMIT:
            print(f'  ⚠️  {obj.title}: description={desc_len} (excede {LIMIT})')
        if dets_len > LIMIT:
            print(f'  ⚠️  {obj.title}: details={dets_len} (excede {LIMIT})')
        if desc_len <= LIMIT and dets_len <= LIMIT:
            print(f'  ✅ {obj.title}: desc={desc_len}, details={dets_len}')
"
```

Si alguna skill aparece con ⚠️, el usuario debe decidir cómo dividir el texto
y añadir el contenido extra al diccionario `SKILL_EXTRA: dict[str, str]` en
`embeds/<tree>.py`, importando la variable extra desde `data/es_<tree>.py`.

## Referencias

| Archivo | Template |
|---------|----------|
| `embeds/sblade.py` | Base — sin extras ni diagrams |
| `embeds/magic.py` | Referencia para OPCIONALES (extras, T0, diagrams, emojis en fmt) |
| `embeds/shot.py` | Alternativa simple — sin emojis en fmt |
| `storage/shot_index.py` | Template de storage (cambiar solo nombre) |
| `branches/shot.py` | Template de branch (5 tiers, purge) |
| `branches/magic.py` | Template de branch con T0 |
| `branches/halberd.py` | Template de branch con resolve_embeds |
| `branches/_base.py` | Lógica compartida de comandos |
| `.env.example` | Template de emoji vars |
