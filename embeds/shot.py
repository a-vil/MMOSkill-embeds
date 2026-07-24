from pathlib import Path
import os
import re

import discord

from data.es_sshot import (
    FOOTER,
    INDEX_HEADER,
    SkillText,
    POWER_SHOT,
    BULLSEYE,
    MOEBA_SHOT,
    SHOT_MASTERY,
    SNEAK_ATTACK,
    ARROW_RAIN,
    PARALYSIS_SHOT,
    LONG_RANGE,
    SNIPE,
    SMOKE_DUST,
    QUICK_DRAW,
    FATAL_SHOT,
    CROSS_FIRE,
    ARM_BREAK,
    DECOY_SHOT,
    HUNTING_BUDDY,
    PIERCING_SHOT,
    VANQUISHER,
    TWIN_STORM,
    QUICK_LOADER,
    RETROGRADE_SHOT,
    PARABOLA_CANNON,
    SPREAD_SHOT,
    ELEMENT_STARTER,
    SAMURAI_ARCHERY,
)


BASE_IMG_PATH = Path(__file__).resolve().parent.parent / "imgs" / "shot"


def _emoji(env_name: str, fallback: str) -> str:
    return os.getenv(env_name) or fallback


def _fmt(text: str, kwargs: dict) -> str:
    placeholders = set(re.findall(r"\{(\w+)\}", text))
    needed = {k: v for k, v in kwargs.items() if k in placeholders}
    return text.format(**needed)


SKILL_KEYS: dict[str, SkillText] = {
    "powershot": POWER_SHOT,
    "bullseye": BULLSEYE,
    "moebashot": MOEBA_SHOT,
    "shotmastery": SHOT_MASTERY,
    "sneakattack": SNEAK_ATTACK,
    "arrowrain": ARROW_RAIN,
    "paralysisshot": PARALYSIS_SHOT,
    "longrange": LONG_RANGE,
    "snipe": SNIPE,
    "smokedust": SMOKE_DUST,
    "quickdraw": QUICK_DRAW,
    "fatalshot": FATAL_SHOT,
    "crossfire": CROSS_FIRE,
    "armbreak": ARM_BREAK,
    "decoyshot": DECOY_SHOT,
    "huntingbuddy": HUNTING_BUDDY,
    "piercingshot": PIERCING_SHOT,
    "vanquisher": VANQUISHER,
    "twinstorm": TWIN_STORM,
    "quickloader": QUICK_LOADER,
    "retrogradshot": RETROGRADE_SHOT,
    "parabolacannon": PARABOLA_CANNON,
    "spreadshot": SPREAD_SHOT,
    "elementstarter": ELEMENT_STARTER,
    "samuraiarchery": SAMURAI_ARCHERY,
}

ALIASES: dict[str, str] = {
    "pshot": "powershot",
    "bull": "bullseye",
    "moeba": "moebashot",
    "mastery": "shotmastery",
    "sneak": "sneakattack",
    "arain": "arrowrain",
    "prs": "paralysisshot",
    "range": "longrange",
    "smoke": "smokedust",
    "qdraw": "quickdraw",
    "fatal": "fatalshot",
    "cross": "crossfire",
    "arm": "armbreak",
    "decoy": "decoyshot",
    "hunter": "huntingbuddy",
    "pierce": "piercingshot",
    "vanq": "vanquisher",
    "tstorm": "twinstorm",
    "qloader": "quickloader",
    "retro": "retrogradshot",
    "cannon": "parabolacannon",
    "spread": "spreadshot",
    "starter": "elementstarter",
    "samurai": "samuraiarchery",
}

TIERS: dict[str, list[str]] = {
    "t1": ["bullseye", "moebashot", "powershot", "shotmastery", "sneakattack"],
    "t2": ["arrowrain", "longrange", "paralysisshot"],
    "t3": ["fatalshot", "quickdraw", "smokedust", "snipe"],
    "t4": ["armbreak", "crossfire", "decoyshot", "huntingbuddy"],
    "t5": [
        "elementstarter", "parabolacannon", "piercingshot", "quickloader",
        "retrogradshot", "samuraiarchery", "spreadshot",
        "twinstorm", "vanquisher",
    ],
}

SKILL_TIER: dict[str, str] = {}
for tier_key, skill_list in TIERS.items():
    for sk in skill_list:
        SKILL_TIER[sk] = tier_key.upper()

SKILL_IMAGES: dict[str, str] = {
    "powershot": "powershot.webp",
    "bullseye": "bullseye.png",
    "moebashot": "moebashot.png",
    "shotmastery": "s-mastery.webp",
    "sneakattack": "sneakattack.png",
    "arrowrain": "arrowrain.png",
    "paralysisshot": "paralysisshot.png",
    "longrange": "longrange.png",
    "snipe": "snipe.png",
    "smokedust": "smokedust.png",
    "quickdraw": "quickdraw.png",
    "fatalshot": "fatalshot.png",
    "crossfire": "crossfire.png",
    "armbreak": "armbreak.png",
    "decoyshot": "decoyshot.png",
    "huntingbuddy": "huntingbuddy.png",
    "piercingshot": "piercingshot.png",
    "vanquisher": "vanquisher.png",
    "twinstorm": "twinstorm.png",
    "quickloader": "quickloader.png",
    "retrogradshot": "retrograde.png",
    "parabolacannon": "parabolacannon.png",
    "spreadshot": "spreadshot.png",
    "elementstarter": "elementstarter.png",
    "samuraiarchery": "samuraiarchery.png",
}

SKILL_EMOJIS: dict[str, str] = {
    POWER_SHOT.title: "POWER_SHOT_EMOJI",
    BULLSEYE.title: "BULLSEYE_EMOJI",
    MOEBA_SHOT.title: "MOEBA_SHOT_EMOJI",
    SHOT_MASTERY.title: "SHOT_MASTERY_EMOJI",
    SNEAK_ATTACK.title: "SNEAK_ATTACK_EMOJI",
    ARROW_RAIN.title: "ARROW_RAIN_EMOJI",
    PARALYSIS_SHOT.title: "PARALYSIS_SHOT_EMOJI",
    LONG_RANGE.title: "LONG_RANGE_EMOJI",
    SNIPE.title: "SNIPE_EMOJI",
    SMOKE_DUST.title: "SMOKE_DUST_EMOJI",
    QUICK_DRAW.title: "QUICK_DRAW_EMOJI",
    FATAL_SHOT.title: "FATAL_SHOT_EMOJI",
    CROSS_FIRE.title: "CROSS_FIRE_EMOJI",
    ARM_BREAK.title: "ARM_BREAK_EMOJI",
    DECOY_SHOT.title: "DECOY_SHOT_EMOJI",
    HUNTING_BUDDY.title: "HUNTING_BUDDY_EMOJI",
    PIERCING_SHOT.title: "PIERCING_SHOT_EMOJI",
    VANQUISHER.title: "VANQUISHER_EMOJI",
    TWIN_STORM.title: "TWIN_STORM_EMOJI",
    QUICK_LOADER.title: "QUICK_LOADER_EMOJI",
    RETROGRADE_SHOT.title: "RETROGRADE_SHOT_EMOJI",
    PARABOLA_CANNON.title: "PARABOLA_CANNON_EMOJI",
    SPREAD_SHOT.title: "SPREAD_SHOT_EMOJI",
    ELEMENT_STARTER.title: "ELEMENT_STARTER_EMOJI",
    SAMURAI_ARCHERY.title: "SAMURAI_ARCHERY_EMOJI",
}

TIER_ORDER = {"T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4}


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
    bow = _emoji("BOW_EMOJI", "Bow")
    bowgun = _emoji("BOWGUN_EMOJI", "Bowgun")
    arrow = _emoji("ARROW_EMOJI", "Arrow")
    all_emoji = _emoji("ALL_EMOJI", "")
    all_weapons = f"{bow} / {bowgun} / {arrow}" if not all_emoji else all_emoji
    fmt = {"bow": bow, "bowgun": bowgun, "arrow": arrow, "all": all_weapons}

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
