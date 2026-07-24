from pathlib import Path
import os
import re

import discord

from data.es_smartial import (
    FOOTER,
    INDEX_HEADER,
    SkillText,
    SMASH,
    BASH,
    SHELL_BREAK,
    HEAVY_SMASH,
    CHARIOT,
    SONIC_WAVE,
    EARTHBIND,
    TRIPLE_KICK,
    RUSH,
    MARTIAL_MASTERY,
    MARTIAL_DISCIPLINE,
    CHAKRA,
    AGGRAVATE,
    STRONG_CHASE_ATTACK,
    SLIDE,
    ABSTRACT_ARMS,
    ASURA_AURA,
    ASURA_AURA_EXTRA,
    FLASH_BLINK,
    ENERGY_CONTROL,
    MOUNTAIN_PRESS,
    SEISMIC_STOMP,
    SPIN_SWEEP,
)


BASE_IMG_PATH = Path(__file__).resolve().parent.parent / "imgs" / "martial"


def _emoji(env_name: str, fallback: str) -> str:
    return os.getenv(env_name) or fallback


def _fmt(text: str, kwargs: dict) -> str:
    placeholders = set(re.findall(r"\{(\w+)\}", text))
    needed = {k: v for k, v in kwargs.items() if k in placeholders}
    return text.format(**needed)


SKILL_KEYS: dict[str, SkillText] = {
    "smash": SMASH,
    "bash": BASH,
    "shellbreak": SHELL_BREAK,
    "heavysmash": HEAVY_SMASH,
    "chariot": CHARIOT,
    "sonicwave": SONIC_WAVE,
    "earthbind": EARTHBIND,
    "triplekick": TRIPLE_KICK,
    "rush": RUSH,
    "martialmastery": MARTIAL_MASTERY,
    "martialdiscipline": MARTIAL_DISCIPLINE,
    "chakra": CHAKRA,
    "aggravate": AGGRAVATE,
    "strongchaseattack": STRONG_CHASE_ATTACK,
    "slide": SLIDE,
    "abstractarms": ABSTRACT_ARMS,
    "asuraaura": ASURA_AURA,
    "flashblink": FLASH_BLINK,
    "energycontrol": ENERGY_CONTROL,
    "mountainpress": MOUNTAIN_PRESS,
    "seismicstomp": SEISMIC_STOMP,
    "spinsweep": SPIN_SWEEP,
}

ALIASES: dict[str, str] = {
    "smash": "smash",
    "bash": "bash",
    "swave": "sonicwave",
    "agg": "aggravate",
    "mmast": "martialmastery",
    "sbreak": "shellbreak",
    "ebind": "earthbind",
    "schase": "strongchaseattack",
    "hsmash": "heavysmash",
    "tkick": "triplekick",
    "slide": "slide",
    "marti": "martialdiscipline",
    "chariot": "chariot",
    "rush": "rush",
    "chakra": "chakra",
    "abstract": "abstractarms",
    "aarms": "abstractarms",
    "asura": "asuraaura",
    "fblink": "flashblink",
    "energy": "energycontrol",
    "econtrol": "energycontrol",
    "mpress": "mountainpress",
    "stomp": "seismicstomp",
    "sweep": "spinsweep",
}

TIERS: dict[str, list[str]] = {
    "t1": ["smash", "bash", "sonicwave", "aggravate", "martialmastery"],
    "t2": ["shellbreak", "earthbind", "strongchaseattack"],
    "t3": ["heavysmash", "triplekick", "slide", "martialdiscipline"],
    "t4": ["chariot", "rush", "chakra"],
    "t5": [
        "abstractarms", "asuraaura", "flashblink", "energycontrol",
        "mountainpress", "seismicstomp", "spinsweep",
    ],
}

SKILL_TIER: dict[str, str] = {}
for tier_key, skill_list in TIERS.items():
    for sk in skill_list:
        SKILL_TIER[sk] = tier_key.upper()

SKILL_IMAGES: dict[str, str] = {
    "smash": "smash.png",
    "bash": "bash.png",
    "shellbreak": "shellbreak.png",
    "heavysmash": "heavysmash.png",
    "chariot": "chariot.png",
    "sonicwave": "sonicwave.png",
    "earthbind": "earthbind.png",
    "triplekick": "triplekick.png",
    "rush": "rush.png",
    "slide": "slide.png",
    "martialmastery": "martialmastery.png",
    "martialdiscipline": "martialdiscipline.png",
    "chakra": "chakra.png",
    "aggravate": "aggravate.png",
    "strongchaseattack": "strongchaseattack.png",
    "abstractarms": "abstractarms.png",
    "asuraaura": "asuraaura.png",
    "flashblink": "flashblink.png",
    "energycontrol": "energycontrol.png",
    "mountainpress": "mountainpress.png",
    "seismicstomp": "seismicstomp.png",
    "spinsweep": "spinsweep.png",
}

SKILL_EMOJIS: dict[str, str] = {
    SMASH.title: "SMASH_EMOJI",
    BASH.title: "BASH_EMOJI",
    SHELL_BREAK.title: "SHELL_BREAK_EMOJI",
    HEAVY_SMASH.title: "HEAVY_SMASH_EMOJI",
    CHARIOT.title: "CHARIOT_EMOJI",
    SONIC_WAVE.title: "SONIC_WAVE_EMOJI",
    EARTHBIND.title: "EARTHBIND_EMOJI",
    TRIPLE_KICK.title: "TRIPLE_KICK_EMOJI",
    RUSH.title: "RUSH_EMOJI",
    MARTIAL_MASTERY.title: "MARTIAL_MASTERY_EMOJI",
    MARTIAL_DISCIPLINE.title: "MARTIAL_DISCIPLINE_EMOJI",
    CHAKRA.title: "CHAKRA_EMOJI",
    AGGRAVATE.title: "AGGRAVATE_EMOJI",
    STRONG_CHASE_ATTACK.title: "STRONG_CHASE_ATTACK_EMOJI",
    SLIDE.title: "SLIDE_EMOJI",
    ABSTRACT_ARMS.title: "ABSTRACT_ARMS_EMOJI",
    ASURA_AURA.title: "ASURA_AURA_EMOJI",
    FLASH_BLINK.title: "FLASH_BLINK_EMOJI",
    ENERGY_CONTROL.title: "ENERGY_CONTROL_EMOJI",
    MOUNTAIN_PRESS.title: "MOUNTAIN_PRESS_EMOJI",
    SEISMIC_STOMP.title: "SEISMIC_STOMP_EMOJI",
    SPIN_SWEEP.title: "SPIN_SWEEP_EMOJI",
}

TIER_ORDER = {"T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4}

SKILL_EXTRA: dict[str, str] = {
    "asuraaura": ASURA_AURA_EXTRA,
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
    knuckle = _emoji("KNUCKLE_EMOJI", "Knuckle")
    barehand = _emoji("BAREHAND_EMOJI", "Barehand")
    all_emoji = _emoji("ALL_EMOJI", "")
    all_weapons = f"{knuckle}" if not all_emoji else all_emoji
    fmt = {"knuckle": knuckle, "barehand": barehand, "all": all_weapons}

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
    details.set_footer(text=FOOTER)

    embeds = [overview, details]

    extra_embeds: list[discord.Embed] = []
    extra_text = SKILL_EXTRA.get(skill_key)
    if extra_text is not None:
        extra_embed = discord.Embed(
            description=_fmt(extra_text, fmt),
            color=discord.Color.blue(),
        )
        extra_embed.set_footer(text=FOOTER)
        extra_embeds.append(extra_embed)

    return embeds, extra_embeds, files


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
