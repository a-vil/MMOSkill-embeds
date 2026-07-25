# 📋 REQUIREMENTS.md

Requisitos técnicos para implementar y extender ramas en MMOSkill-embeds.

Este archivo es **complementario** a [ARCHITECTURE.md](./ARCHITECTURE.md). Describe los contratos exactos que debe cumplir cada módulo.

---

## 1. Registro de ramas

Cada rama debe registrarse en dos lugares:

**`branches/__init__.py`** — importar el módulo y añadirlo a `register_all()`:

```python
from . import shot, magic, sblade, martial, halberd  # + nueva_rama

def register_all(bot):
    shot.register(bot)
    magic.register(bot)
    sblade.register(bot)
    martial.register(bot)
    halberd.register(bot)
    # nueva_rama.register(bot)
```

**`branches/nueva_rama.py`** — debe exportar `register(bot)`:

```python
handlers = BranchHandlers(config)

def register(bot):
    handlers.register(bot)
```

---

## 2. Contrato de módulos

### 2.0 `data/es_nombre_rama.py`

| Export | Tipo | Obligatorio |
|--------|------|-------------|
| `SkillText` | `dataclass` | Sí (title, description, details) |
| `FOOTER` | `str` | Sí |
| `INDEX_HEADER` | `list[str]` | Sí |
| `NOMBRE_SKILL` (cada una) | `SkillText` | Sí |

`FOOTER` se usa en el embed de detalles. `INDEX_HEADER` se usa en el embed del índice.

### 2.1 `embeds/nombre_rama.py`

| Export | Tipo | Obligatorio |
|--------|------|-------------|
| `SKILL_KEYS` | `dict[str, SkillText]` | Sí |
| `TIERS` | `dict[str, list[str]]` | Sí |
| `SKILL_TIER` | `dict[str, str]` | Sí |
| `ALIASES` | `dict[str, str]` | Sí |
| `TIER_ORDER` | `dict[str, int]` | Sí |
| `SKILL_IMAGES` | `dict[str, str]` | No (opcional, thumbnail) |
| `SKILL_EMOJIS` | `dict[str, str]` | No (opcional, índice) |
| `SKILL_EXTRA` | `dict[str, SkillText]` | No (opcional, >2 embeds) |
| `resolve_skill(name)` | `str \| None` | Sí |
| `get_skill_embeds(skill_key)` | `tuple[list[Embed], list[Embed], list[File]]` | Sí |
| `get_tier_skill_keys(tier_key)` | `list[str]` | Sí |
| `get_skills_index_embed(guild_id, skills)` | `Embed` | Sí |

`SKILL_TIER` se construye automáticamente desde `TIERS`:

```python
SKILL_TIER: dict[str, str] = {}
for tier_key, skill_list in TIERS.items():
    for sk in skill_list:
        SKILL_TIER[sk] = tier_key.upper()
```

### 2.2 `storage/nombre_rama_index.py`

| Export | Tipo | Obligatorio |
|--------|------|-------------|
| `INDEX_FILE` | `Path` | Sí |
| `load_index()` | `dict` | Sí |
| `save_index(data)` | `None` | Sí |
| `save_skill(guild_id, skill_key, name, tier, channel_id, message_id)` | `None` | Sí |
| `save_index_message(guild_id, channel_id, message_id)` | `None` | Sí |
| `get_guild_data(guild_id)` | `dict` | Sí |

Convención de nombre: `storage/nombre_rama_index.py` → `storage/nombre_rama_index.json`.

### 2.3 `branches/nombre_rama.py`

| Export | Tipo | Obligatorio |
|--------|------|-------------|
| `config` | `BranchConfig` | Sí |
| `handlers` | `BranchHandlers` | Sí |
| `register(bot)` | `Callable` | Sí |

---

## 3. BranchConfig — campos

Campos requeridos al instanciar `BranchConfig`:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `command_name` | `str` | Nombre del comando (ej. `"skshot"`) |
| `display_name` | `str` | Nombre mostrado (ej. `"Shot"`) |
| `skill_keys` | `dict` | `SKILL_KEYS` del módulo embeds |
| `tiers` | `dict` | `TIERS` del módulo embeds |
| `skill_tier` | `dict` | `SKILL_TIER` del módulo embeds |
| `title_to_key` | `dict` | `{st.title: sk for sk, st in SKILL_KEYS.items()}` |
| `tier_order` | `dict` | Ej: `{"T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4}` |
| `tier_list` | `tuple[str, ...]` | Ej: `("t1", "t2", "t3", "t4", "t5")` |
| `get_skill_embeds` | `Callable` | `get_skill_embeds` del módulo embeds |
| `get_tier_skill_keys` | `Callable` | `get_tier_skill_keys` del módulo embeds |
| `get_skills_index_embed` | `Callable` | `get_skills_index_embed` del módulo embeds |
| `resolve_skill` | `Callable` | `resolve_skill` del módulo embeds |
| `get_guild_data` | `Callable` | `get_guild_data` del módulo storage |
| `save_skill` | `Callable` | `save_skill` del módulo storage |
| `save_index_message` | `Callable` | `save_index_message` del módulo storage |
| `load_index` | `Callable` | `load_index` del módulo storage |
| `save_index` | `Callable` | `save_index` del módulo storage |
| `help_lines` | `list[str]` | Lista de texto de ayuda del comando |

Campos opcionales con defaults:

| Campo | Default | Descripción |
|-------|---------|-------------|
| `nuke_method` | `"title_scan"` | `"title_scan"` o `"purge"` |
| `resolve_embeds` | `None` | Callable para resolver emojis en los embeds |
| `send_all_direct` | `False` | Enviar `all` sin agrupar por tier |

---

## 4. Convenciones de embeds

### 4.1 Ruta de imágenes

```python
BASE_IMG_PATH = Path(__file__).resolve().parent.parent / "imgs" / "nombre_rama"
```

### 4.2 SKILL_IMAGES

Mapea `skill_key` → nombre de archivo:

```python
SKILL_IMAGES: dict[str, str] = {
    "powershot": "powershot.webp",
    "bullseye": "bullseye.png",
    ...
}
```

### 4.3 SKILL_EMOJIS

Mapea `SkillText.title` → nombre de variable de entorno:

```python
SKILL_EMOJIS: dict[str, str] = {
    POWER_SHOT.title: "POWER_SHOT_EMOJI",
    BULLSEYE.title: "BULLSEYE_EMOJI",
    ...
}
```

### 4.4 Funciones helper

```python
def _emoji(env_name: str, fallback: str) -> str:
    return os.getenv(env_name) or fallback

def _fmt(text: str, kwargs: dict) -> str:
    placeholders = set(re.findall(r"\{(\w+)\}", text))
    needed = {k: v for k, v in kwargs.items() if k in placeholders}
    return text.format(**needed)

def _normalize(name: str) -> str:
    return re.sub(r"[\s_-]+", "", name.lower()).strip()

def _get_image_path(skill_key: str) -> Path | None:
    fname = SKILL_IMAGES.get(skill_key)
    if fname is None:
        return None
    p = BASE_IMG_PATH / fname
    return p if p.exists() else None
```

### 4.5 SKILL_EXTRA (skills con >2 embeds)

Para skills cuyo contenido no cabe en 2 embeds, definir un `SkillText` extra en `data/es_nombre_rama.py` y referenciarlo en `embeds/nombre_rama.py`:

```python
SKILL_EXTRA: dict[str, SkillText] = {
    "draconiccharge": DRACONIC_CHARGE_EXTRA,
}
```

El builder `get_skill_embeds` lo incluye en la segunda tupla del return:

```python
extra_embeds: list[discord.Embed] = []
extra_text = SKILL_EXTRA.get(skill_key)
if extra_text:
    extra = discord.Embed(description=_fmt(extra_text, fmt), color=...)
    extra_embeds.append(extra)
return embeds, extra_embeds, files
```

---

## 5. Assets de imagen

Crear carpeta `imgs/nombre_rama/` y agregar los archivos de imagen para cada skill.

---

## 6. Variables de entorno

Al añadir una rama, agregar al `.env.example`:

- Variables de emoji de arma (si aplica un tipo de arma nuevo)
- Variables de emoji para cada skill en el índice

Ejemplo para una skill llamada `"Power Shot"`:

```env
POWER_SHOT_EMOJI=
```