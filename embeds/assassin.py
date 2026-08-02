from pathlib import Path
import os
import re

import discord

from data.es_sassassin import (
    FOOTER,
    INDEX_HEADER,
    SkillText,
    ASSASSIN_STAB,
    EVASION,
    BACKSTEP,
    SERUM,
    ARCANE_STRIKE,
    FORESIGHT,
    SICARIUS,
    SHADOW_WALK,
    VENOM_INJECTION,
    CORROSIVE_POISON,
    VENOM_THIEF,
    DEATH_RECEPTION,
    SECRET_ASSASSIN,
    ASSAULT_CHASE,
    POISON_MASTER,
)


BASE_IMG_PATH = Path(__file__).resolve().parent.parent / "imgs" / "assassin"


def _emoji(env_name: str, fallback: str) -> str:
    return os.getenv(env_name) or fallback


def _fmt(text: str, kwargs: dict) -> str:
    placeholders = set(re.findall(r"\{(\w+)\}", text))
    needed = {k: v for k, v in kwargs.items() if k in placeholders}
    return text.format(**needed)


SKILL_KEYS: dict[str, SkillText] = {
    "assassinstab": ASSASSIN_STAB,
    "evasion": EVASION,
    "backstep": BACKSTEP,
    "serum": SERUM,
    "arcanestrike": ARCANE_STRIKE,
    "foresight": FORESIGHT,
    "sicarius": SICARIUS,
    "shadowwalk": SHADOW_WALK,
    "venominjection": VENOM_INJECTION,
    "corrosivepoison": CORROSIVE_POISON,
    "venomthief": VENOM_THIEF,
    "deathreception": DEATH_RECEPTION,
    "secretassassin": SECRET_ASSASSIN,
    "assaultchase": ASSAULT_CHASE,
    "poisonmaster": POISON_MASTER,
}

ALIASES: dict[str, str] = {
    "stab": "assassinstab",
    "evas": "evasion",
    "back": "backstep",
    "serum": "serum",
    "arcane": "arcanestrike",
    "fore": "foresight",
    "sic": "sicarius",
    "shadow": "shadowwalk",
    "venom": "venominjection",
    "corr": "corrosivepoison",
    "vthief": "venomthief",
    "death": "deathreception",
    "secret": "secretassassin",
    "chase": "assaultchase",
    "pmast": "poisonmaster",
}

TIERS: dict[str, list[str]] = {
    "t1": ["assassinstab", "evasion", "venominjection"],
    "t2": ["backstep", "serum", "corrosivepoison"],
    "t3": ["arcanestrike", "foresight", "venomthief"],
    "t4": ["sicarius", "shadowwalk", "deathreception"],
    "t5": ["secretassassin", "assaultchase", "poisonmaster"],
}

SKILL_TIER: dict[str, str] = {}
for tier_key, skill_list in TIERS.items():
    for sk in skill_list:
        SKILL_TIER[sk] = tier_key.upper()

SKILL_EMOJIS: dict[str, str] = {
    ASSASSIN_STAB.title: "ASSASSIN_STAB_EMOJI",
    EVASION.title: "EVASION_EMOJI",
    BACKSTEP.title: "BACKSTEP_EMOJI",
    SERUM.title: "SERUM_EMOJI",
    ARCANE_STRIKE.title: "ARCANE_STRIKE_EMOJI",
    FORESIGHT.title: "FORESIGHT_EMOJI",
    SICARIUS.title: "SICARIUS_EMOJI",
    SHADOW_WALK.title: "SHADOW_WALK_EMOJI",
    VENOM_INJECTION.title: "VENOM_INJECTION_EMOJI",
    CORROSIVE_POISON.title: "CORROSIVE_POISON_EMOJI",
    VENOM_THIEF.title: "VENOM_THIEF_EMOJI",
    DEATH_RECEPTION.title: "DEATH_RECEPTION_EMOJI",
    SECRET_ASSASSIN.title: "SECRET_ASSASSIN_EMOJI",
    ASSAULT_CHASE.title: "ASSAULT_CHASE_EMOJI",
    POISON_MASTER.title: "POISON_MASTER_EMOJI",
}

TIER_ORDER = {"T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4}

SKILL_IMAGES: dict[str, str] = {
    "assassinstab": "assassinstab.png",
    "evasion": "evasion.png",
    "backstep": "backstep.png",
    "serum": "serum.png",
    "arcanestrike": "arcanestrike.png",
    "foresight": "foresight.png",
    "sicarius": "sicarius.png",
    "shadowwalk": "shadowwalk.png",
    "venominjection": "venominjection.png",
    "corrosivepoison": "corrosivepoison.png",
    "venomthief": "venomthief.png",
    "deathreception": "deathreception.png",
    "secretassassin": "secretassassin.png",
    "assaultchase": "assaultchase.png",
    "poisonmaster": "poisonmaster.png",
}

SKILL_DIAGRAMS: dict[str, str] = {
    "assassinstab": "assass.png",
}


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


def get_skill_embeds(skill_key: str) -> tuple[list[discord.Embed], list[discord.Embed], list[discord.File]]:
    skill = SKILL_KEYS[skill_key]
    all_emoji = _emoji("ALL_EMOJI", "")
    fmt = {"all": all_emoji, "image": ""}

    overview = discord.Embed(
        title=skill.title,
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

    diagram_fname = SKILL_DIAGRAMS.get(skill_key)
    if diagram_fname:
        diagram_path = BASE_IMG_PATH / diagram_fname
        if diagram_path.exists():
            files.append(discord.File(diagram_path, filename=diagram_fname))
            details.set_image(url=f"attachment://{diagram_fname}")
    details.set_footer(text=FOOTER)

    return [overview, details], [], files


def get_tier_embeds(tier_key: str) -> list[tuple[list[discord.Embed], list[discord.Embed], list[discord.File]]]:
    skill_keys = TIERS.get(tier_key)
    if skill_keys is None:
        return []
    return [get_skill_embeds(sk) for sk in skill_keys]


def get_tier_skill_keys(tier_key: str) -> list[str]:
    return TIERS.get(tier_key, [])


def get_skills_index_embed(guild_id: int, skills: dict) -> discord.Embed:
    embed = discord.Embed(color=discord.Color.blue())
    description_lines = list(INDEX_HEADER)
    sorted_skills = sorted(
        skills.values(),
        key=lambda s: (TIER_ORDER.get(s["tier"], 99), s["name"]),
    )
    for skill in sorted_skills:
        link = f"https://discord.com/channels/{guild_id}/{skill['channel_id']}/{skill['message_id']}"
        emoji_env = SKILL_EMOJIS.get(skill["name"])
        skill_emoji = _emoji(emoji_env, "") if emoji_env else ""
        emoji_part = f" {skill_emoji}" if skill_emoji else ""
        description_lines.append(f"{skill['tier']}{emoji_part} [{skill['name']}]({link})")
    embed.description = "\n".join(description_lines)
    embed.set_footer(text="📌Nota: Puedes usar el mensaje fijado, para volver aquí.")
    return embed
