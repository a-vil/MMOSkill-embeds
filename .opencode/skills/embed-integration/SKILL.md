---
name: embed-integration
description: Crea los 4 archivos necesarios para integrar un nuevo tree de skills (embeds module, storage, bot.py, .env.example) siguiendo el patrón de shot, magic y blade.
---

# Integración de nuevo tree de skills

## Flujo completo

```
data/es_<tree>.py  →  embeds/<tree>.py  →  storage/<tree>_index.py  →  bot.py  +  .env.example
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

## 3. bot.py — Integración

### Imports (3 bloques)

```python
from embeds.<tree> import (
    SKILL_KEYS as <TREE>_SKILL_KEYS,
    TIERS as <TREE>_TIERS,
    SKILL_TIER as <TREE>_SKILL_TIER,
    get_skill_embeds as get_<tree>_skill_embeds,
    get_tier_embeds as get_<tree>_tier_embeds,
    get_tier_skill_keys as get_<tree>_tier_skill_keys,
    get_skills_index_embed as get_<tree>_skills_index_embed,
    resolve_skill as resolve_<tree>_skill,
)
from storage.<tree>_index import (
    get_guild_data as get_<tree>_guild_data,
    save_index_message as save_<tree>_index_message,
    save_skill as save_<tree>_skill,
    load_index as load_<tree>_index,
    save_index as save_<tree>_index,
)
```

### TITLE_TO_KEY

```python
TITLE_TO_KEY_<TREE>: dict[str, str] = {st.title: sk for sk, st in <TREE>_SKILL_KEYS.items()}
```

### Helper functions

```python
def _tier_from_<tree>_key(skill_key: str) -> str:
    return <TREE>_SKILL_TIER.get(skill_key, "T?")

async def _update_index_<tree>(ctx: commands.Context, guild: discord.Guild) -> None:
    guild_data = get_<tree>_guild_data(guild.id)
    if not guild_data["skills"]:
        return
    if guild_data["index"]:
        try:
            channel = guild.get_channel(guild_data["index"]["channel_id"])
            if isinstance(channel, discord.TextChannel):
                index_msg = await channel.fetch_message(guild_data["index"]["message_id"])
                index_embed = get_<tree>_skills_index_embed(guild.id, guild_data["skills"])
                await index_msg.edit(embed=index_embed)
                return
        except discord.NotFound:
            pass
    index_embed = get_<tree>_skills_index_embed(guild.id, guild_data["skills"])
    index_msg = await ctx.send(embed=index_embed)
    save_<tree>_index_message(guild.id, index_msg.channel.id, index_msg.id)
```

### Comando

```python
@bot.command(name="sk<tree>")
async def sk<tree>(ctx: commands.Context, *args: str) -> None:
    guild = ctx.guild
    if guild is None:
        await ctx.send("Este comando solo puede usarse en un servidor.")
        return

    if not args:
        await _send_help_<tree>(ctx)
        return

    raw = " ".join(args)
    save_flag = raw.lower().endswith(" save")
    if save_flag:
        raw = raw[:-5].strip()

    cmd = raw.strip().lower()

    if cmd in ("list",):
        await _send_list_<tree>(ctx)
        return

    if cmd in ("index",):
        await _send_index_<tree>(ctx, guild)
        return

    if cmd in ("nuke",):
        await _nuke_channel_<tree>(ctx, guild)
        return

    if cmd in ("scan",):
        await _scan_channel_<tree>(ctx, guild)
        return

    if cmd in <TREE>_TIERS:
        await _send_tier_<tree>(ctx, guild, cmd, save=save_flag)
        return

    if cmd == "all":
        await _send_all_<tree>(ctx, guild)
        return

    skill_key = resolve_<tree>_skill(cmd)
    if skill_key is None:
        await ctx.send(
            f'Skill no encontrada: "{raw}". Usa `!sk<tree> list` para ver las disponibles.'
        )
        return

    embeds, extra_embeds, files = get_<tree>_skill_embeds(skill_key)
    msg = await ctx.send(embeds=embeds, files=files)
    for extra in extra_embeds:
        await ctx.send(embeds=[extra])

    if save_flag:
        skill = <TREE>_SKILL_KEYS[skill_key]
        save_<tree>_skill(
            guild.id,
            skill_key,
            skill.title,
            _tier_from_<tree>_key(skill_key),
            msg.channel.id,
            msg.id,
        )
        await _update_index_<tree>(ctx, guild)
```

### Sub-funciones necesarias

- `_send_help_<tree>` — mensaje de ayuda
- `_send_list_<tree>` — lista de skills por tier
- `_send_index_<tree>` — muestra/actualiza índice
- `_send_tier_<tree>` — envía un tier completo (con save opcional)
- `_send_all_<tree>` — envía todas las skills y las guarda
- `_nuke_channel_<tree>` — elimina mensajes + índice en el canal (usa `TITLE_TO_KEY_<TREE>` para identificar skills por título)
- `_scan_channel_<tree>` — escanea el canal y registra skills existentes

## 4. .env.example

Agregar al final del archivo:

```env
# Weapon icons for <tree> skills
<TREE>_EMOJI=

# Skill icons for the <Tree> Skills Index
SKILL_1_EMOJI=
SKILL_2_EMOJI=
# ... una por skill
```

## 5. Verificación: Límite de descripciones

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
| `bot.py` (bloque blade) | Template de integración |
| `.env.example` | Template de emoji vars |
