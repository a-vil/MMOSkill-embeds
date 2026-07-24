from pathlib import Path
import os
import re

import discord

from data.es_smagic import (
    FOOTER,
    INDEX_HEADER,
    SkillText,
    ELEMENTAL_NAMES,
    MAGIC_ARROWS,
    MAGIC_JAVELIN,
    MAGIC_LANCES,
    MAGIC_IMPACT,
    MAGIC_FINALE,
    MAGIC_WALL,
    MAGIC_BLAST,
    MAGIC_STORM,
    MAGIC_BURST,
    MAGIC_MASTERY,
    MP_CHARGE,
    CHAIN_CAST,
    POWER_WAVE,
    MAXIMIZER,
    GUARDIAN_BEAM,
    CHRONOS_SHIFT,
    MAGIC_CANNON,
    MAGIC_CANNON_EXTRA,
    MAGIC_CRASH,
    RAPID_CHARGE,
    ENCHANTED_BARRIERS,
    ENCHANTED_BARRIERS_EXTRA,
    MAGIC_KNIFE,
    QADAL,
    QADAL_EXTRA,
    SPELL_CALIBRATION,
    MAGIC_LASER,
)


BASE_IMG_PATH = Path(__file__).resolve().parent.parent / "imgs" / "magic"


def _emoji(env_name: str, fallback: str) -> str:
    return os.getenv(env_name) or fallback


def _fmt(text: str, kwargs: dict) -> str:
    placeholders = set(re.findall(r"\{(\w+)\}", text))
    needed = {k: v for k, v in kwargs.items() if k in placeholders}
    return text.format(**needed)


SKILL_KEYS: dict[str, SkillText] = {
    "magicarrows": MAGIC_ARROWS,
    "magicjavelin": MAGIC_JAVELIN,
    "magiclances": MAGIC_LANCES,
    "magicimpact": MAGIC_IMPACT,
    "magicfinale": MAGIC_FINALE,
    "magicwall": MAGIC_WALL,
    "magicblast": MAGIC_BLAST,
    "magicstorm": MAGIC_STORM,
    "magicburst": MAGIC_BURST,
    "magicmastery": MAGIC_MASTERY,
    "mpcharge": MP_CHARGE,
    "chaincast": CHAIN_CAST,
    "powerwave": POWER_WAVE,
    "maximizer": MAXIMIZER,
    "guardianbeam": GUARDIAN_BEAM,
    "chronosshift": CHRONOS_SHIFT,
    "magiccannon": MAGIC_CANNON,
    "magiccrash": MAGIC_CRASH,
    "rapidcharge": RAPID_CHARGE,
    "enchantedbarriers": ENCHANTED_BARRIERS,
    "magicknife": MAGIC_KNIFE,
    "qadal": QADAL,
    "spellcalibration": SPELL_CALIBRATION,
    "magiclaser": MAGIC_LASER,
    "elementalnames": ELEMENTAL_NAMES,
}

ALIASES: dict[str, str] = {
    "marrows": "magicarrows",
    "mjavelin": "magicjavelin",
    "mlances": "magiclances",
    "mimpact": "magicimpact",
    "mfinale": "magicfinale",
    "mwall": "magicwall",
    "mblast": "magicblast",
    "mstorm": "magicstorm",
    "mburst": "magicburst",
    "mmast": "magicmastery",
    "mpc": "mpcharge",
    "ccast": "chaincast",
    "pwave": "powerwave",
    "max": "maximizer",
    "gbeam": "guardianbeam",
    "cshift": "chronosshift",
    "mcannon": "magiccannon",
    "mcrash": "magiccrash",
    "rcharge": "rapidcharge",
    "ebarriers": "enchantedbarriers",
    "mknife": "magicknife",
    "qadal": "qadal",
    "scalib": "spellcalibration",
    "mlaser": "magiclaser",
    "elements": "elementalnames",
    "ele": "elementalnames",
}

TIERS: dict[str, list[str]] = {
    "t0": ["elementalnames"],
    "t1": ["magicarrows", "magicjavelin", "magicwall", "magicmastery", "mpcharge"],
    "t2": ["magiclances", "magicblast", "chaincast", "magicknife"],
    "t3": ["magicimpact", "magicstorm", "powerwave", "guardianbeam", "qadal"],
    "t4": ["magicfinale", "magicburst", "maximizer", "spellcalibration"],
    "t5": [
        "chronosshift", "magiccannon", "magiccrash", "rapidcharge",
        "enchantedbarriers", "magiclaser",
    ],
}

SKILL_TIER: dict[str, str] = {}
for tier_key, skill_list in TIERS.items():
    for sk in skill_list:
        SKILL_TIER[sk] = tier_key.upper()

SKILL_IMAGES: dict[str, str] = {
    "magicarrows": "arrows.png",
    "magicjavelin": "javelin.png",
    "magiclances": "lances.png",
    "magicimpact": "impact.png",
    "magicfinale": "finale.png",
    "magicwall": "wall.png",
    "magicblast": "blast.png",
    "magicstorm": "storm.png",
    "magicburst": "burst.png",
    "magicmastery": "magicmastery.png",
    "mpcharge": "mpcharge.png",
    "chaincast": "chaincast.png",
    "powerwave": "powerwave.png",
    "maximizer": "maximizer.png",
    "guardianbeam": "guardianbeam.png",
    "chronosshift": "chronosshift.png",
    "magiccannon": "magiccannon.png",
    "magiccrash": "magiccrash.png",
    "rapidcharge": "rapidcharge.png",
    "enchantedbarriers": "enchantedbarriers.png",
    "magicknife": "magicknife.png",
    "qadal": "qadal.png",
    "spellcalibration": "spellcalibration.png",
    "magiclaser": "laser.png",
}

SKILL_DIAGRAMS: dict[str, str] = {
    "magicburst": "image.png",
}

SKILL_EMOJIS: dict[str, str] = {
    ELEMENTAL_NAMES.title: "ELEMENTAL_NAMES_EMOJI",
    MAGIC_ARROWS.title: "MAGIC_ARROWS_EMOJI",
    MAGIC_JAVELIN.title: "MAGIC_JAVELIN_EMOJI",
    MAGIC_LANCES.title: "MAGIC_LANCES_EMOJI",
    MAGIC_IMPACT.title: "MAGIC_IMPACT_EMOJI",
    MAGIC_FINALE.title: "MAGIC_FINALE_EMOJI",
    MAGIC_WALL.title: "MAGIC_WALL_EMOJI",
    MAGIC_BLAST.title: "MAGIC_BLAST_EMOJI",
    MAGIC_STORM.title: "MAGIC_STORM_EMOJI",
    MAGIC_BURST.title: "MAGIC_BURST_EMOJI",
    MAGIC_MASTERY.title: "MAGIC_MASTERY_EMOJI",
    MP_CHARGE.title: "MP_CHARGE_EMOJI",
    CHAIN_CAST.title: "CHAIN_CAST_EMOJI",
    POWER_WAVE.title: "POWER_WAVE_EMOJI",
    MAXIMIZER.title: "MAXIMIZER_EMOJI",
    GUARDIAN_BEAM.title: "GUARDIAN_BEAM_EMOJI",
    CHRONOS_SHIFT.title: "CHRONOS_SHIFT_EMOJI",
    MAGIC_CANNON.title: "MAGIC_CANNON_EMOJI",
    MAGIC_CRASH.title: "MAGIC_CRASH_EMOJI",
    RAPID_CHARGE.title: "RAPID_CHARGE_EMOJI",
    ENCHANTED_BARRIERS.title: "ENCHANTED_BARRIERS_EMOJI",
    MAGIC_KNIFE.title: "MAGIC_KNIFE_EMOJI",
    QADAL.title: "QADAL_EMOJI",
    SPELL_CALIBRATION.title: "SPELL_CALIBRATION_EMOJI",
    MAGIC_LASER.title: "MAGIC_LASER_EMOJI",
}

SKILL_EMOJI_KEYS: dict[str, str] = {
    name.lower().replace("magic: ", "").replace(" ", ""): env
    for name, env in SKILL_EMOJIS.items()
}

TIER_ORDER = {"T0": 5, "T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4}

SKILL_EXTRA: dict[str, str] = {
    "magiccannon": MAGIC_CANNON_EXTRA,
    "enchantedbarriers": ENCHANTED_BARRIERS_EXTRA,
    "qadal": QADAL_EXTRA,
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
    staff = _emoji("STAFF_EMOJI", "Staff")
    magicdevice = _emoji("MAGICDEVICE_EMOJI", "Magic Device")
    ohs = _emoji("OHS_EMOJI", "OHS")
    all_emoji = _emoji("ALL_EMOJI", "")
    all_weapons = f"{staff} / {magicdevice}" if not all_emoji else all_emoji
    fmt = {"staff": staff, "magicdevice": magicdevice, "ohs": ohs, "all": all_weapons, "image": ""}
    fmt.update({k: _emoji(v, "") for k, v in SKILL_EMOJI_KEYS.items()})

    overview = discord.Embed(
        title=None if skill_key == "elementalnames" else skill.title,
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
        if skill["tier"] != "T0":
            link = f"https://discord.com/channels/{guild_id}/{skill['channel_id']}/{skill['message_id']}"
            emoji_env = SKILL_EMOJIS.get(skill["name"])
            skill_emoji = _emoji(emoji_env, "") if emoji_env else ""
            emoji_part = f" {skill_emoji}" if skill_emoji else ""
            label = f"{skill['tier']}{emoji_part} [{skill['name']}]({link})"
            description_lines.append(label)

    t0_skills = [s for s in sorted_skills if s["tier"] == "T0"]
    if t0_skills:
        description_lines.append("")
        for skill in t0_skills:
            link = f"https://discord.com/channels/{guild_id}/{skill['channel_id']}/{skill['message_id']}"
            emoji_env = SKILL_EMOJIS.get(skill["name"])
            skill_emoji = _emoji(emoji_env, "") if emoji_env else ""
            emoji_part = f" {skill_emoji}" if skill_emoji else ""
            label = f"Otros:{emoji_part} [{skill['name']}]({link})"
            description_lines.append(label)
    embed.description = "\n".join(description_lines)
    embed.set_footer(text="📌Nota: Puedes usar el mensaje fijado, para volver aquí.")
    return embed
