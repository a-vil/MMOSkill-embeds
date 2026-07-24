from pathlib import Path
import os
import re

import discord

from data.es_sblade import (
    FOOTER,
    INDEX_HEADER,
    SkillText,
    HARD_HIT,
    ASTUTE,
    TRIGGER_SLASH,
    RAMPAGE,
    METEOR_BREAKER,
    SONIC_BLADE,
    SPIRAL_AIR,
    SWORD_TEMPEST,
    BUSTER_BLADE,
    SWORD_MASTERY,
    QUICK_SLASH,
    SWORD_TECHNIQUES,
    WAR_CRY,
    BERSERK,
    SWIFT_ATTACK,
    SHUTOUT,
    LUNAR_SLASH,
    AURA_BLADE,
    GLADIATE,
    HAMMER_SLAM,
    CLEAVING_ATTACK,
    STORM_BLAZE,
    GARDE_BLADE,
    OGRE_SLASH,
)


BASE_IMG_PATH = Path(__file__).resolve().parent.parent / "imgs" / "blade"


def _emoji(env_name: str, fallback: str) -> str:
    return os.getenv(env_name) or fallback


def _fmt(text: str, kwargs: dict) -> str:
    placeholders = set(re.findall(r"\{(\w+)\}", text))
    needed = {k: v for k, v in kwargs.items() if k in placeholders}
    return text.format(**needed)


SKILL_KEYS: dict[str, SkillText] = {
    "hardhit": HARD_HIT,
    "astute": ASTUTE,
    "triggerslash": TRIGGER_SLASH,
    "rampage": RAMPAGE,
    "meteorbreaker": METEOR_BREAKER,
    "sonicblade": SONIC_BLADE,
    "spiralair": SPIRAL_AIR,
    "swordtempest": SWORD_TEMPEST,
    "busterblade": BUSTER_BLADE,
    "swordmastery": SWORD_MASTERY,
    "quickslash": QUICK_SLASH,
    "swordtechniques": SWORD_TECHNIQUES,
    "warcry": WAR_CRY,
    "berserk": BERSERK,
    "swiftattack": SWIFT_ATTACK,
    "shutout": SHUTOUT,
    "lunarslash": LUNAR_SLASH,
    "aurablade": AURA_BLADE,
    "gladiate": GLADIATE,
    "hammerslam": HAMMER_SLAM,
    "cleavingattack": CLEAVING_ATTACK,
    "stormblaze": STORM_BLAZE,
    "gardeblade": GARDE_BLADE,
    "ogreslash": OGRE_SLASH,
}

ALIASES: dict[str, str] = {
    "hard": "hardhit",
    "ast": "astute",
    "trig": "triggerslash",
    "ramp": "rampage",
    "meteor": "meteorbreaker",
    "sonic": "sonicblade",
    "spiral": "spiralair",
    "tempest": "swordtempest",
    "buster": "busterblade",
    "mastery": "swordmastery",
    "quick": "quickslash",
    "techniques": "swordtechniques",
    "warcry": "warcry",
    "berserk": "berserk",
    "swift": "swiftattack",
    "shut": "shutout",
    "lunar": "lunarslash",
    "aura": "aurablade",
    "glad": "gladiate",
    "hammer": "hammerslam",
    "cleave": "cleavingattack",
    "storm": "stormblaze",
    "garde": "gardeblade",
    "ogre": "ogreslash",
}

TIERS: dict[str, list[str]] = {
    "t1": ["hardhit", "astute", "swordmastery", "quickslash", "sonicblade", "hammerslam"],
    "t2": ["triggerslash", "spiralair", "swordtechniques", "cleavingattack"],
    "t3": ["rampage", "warcry", "swordtempest", "swiftattack", "stormblaze"],
    "t4": ["meteorbreaker", "busterblade", "berserk", "gardeblade"],
    "t5": ["shutout", "lunarslash", "aurablade", "gladiate", "ogreslash"],
}

SKILL_TIER: dict[str, str] = {}
for tier_key, skill_list in TIERS.items():
    for sk in skill_list:
        SKILL_TIER[sk] = tier_key.upper()

SKILL_EMOJIS: dict[str, str] = {
    HARD_HIT.title: "HARD_HIT_EMOJI",
    ASTUTE.title: "ASTUTE_EMOJI",
    TRIGGER_SLASH.title: "TRIGGER_SLASH_EMOJI",
    RAMPAGE.title: "RAMPAGE_EMOJI",
    METEOR_BREAKER.title: "METEOR_BREAKER_EMOJI",
    SONIC_BLADE.title: "SONIC_BLADE_EMOJI",
    SPIRAL_AIR.title: "SPIRAL_AIR_EMOJI",
    SWORD_TEMPEST.title: "SWORD_TEMPEST_EMOJI",
    BUSTER_BLADE.title: "BUSTER_BLADE_EMOJI",
    SWORD_MASTERY.title: "SWORD_MASTERY_EMOJI",
    QUICK_SLASH.title: "QUICK_SLASH_EMOJI",
    SWORD_TECHNIQUES.title: "SWORD_TECHNIQUES_EMOJI",
    WAR_CRY.title: "WAR_CRY_EMOJI",
    BERSERK.title: "BERSERK_EMOJI",
    SWIFT_ATTACK.title: "SWIFT_ATTACK_EMOJI",
    SHUTOUT.title: "SHUTOUT_EMOJI",
    LUNAR_SLASH.title: "LUNAR_SLASH_EMOJI",
    AURA_BLADE.title: "AURA_BLADE_EMOJI",
    GLADIATE.title: "GLADIATE_EMOJI",
    HAMMER_SLAM.title: "HAMMER_SLAM_EMOJI",
    CLEAVING_ATTACK.title: "CLEAVING_ATTACK_EMOJI",
    STORM_BLAZE.title: "STORM_BLAZE_EMOJI",
    GARDE_BLADE.title: "GARDE_BLADE_EMOJI",
    OGRE_SLASH.title: "OGRE_SLASH_EMOJI",
}

TIER_ORDER = {"T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4}

SKILL_EMOJI_KEYS: dict[str, str] = {
    name.lower().replace(": ", "").replace(" ", ""): env
    for name, env in SKILL_EMOJIS.items()
}


def _normalize(name: str) -> str:
    return re.sub(r"[\s_-]+", "", name.lower()).strip()


SKILL_IMAGES: dict[str, str] = {
    "hardhit": "hardhit.PNG",
    "astute": "astute.PNG",
    "triggerslash": "triggerslash.PNG",
    "rampage": "rampage.PNG",
    "meteorbreaker": "meteorbreaker.PNG",
    "sonicblade": "sonicblade.PNG",
    "spiralair": "spiralair.PNG",
    "swordtempest": "swordtempest.PNG",
    "busterblade": "busterblade.PNG",
    "swordmastery": "SwordMastery.PNG",
    "quickslash": "QuickSlash.PNG",
    "swordtechniques": "swordtechniques.png",
    "warcry": "warcry.png",
    "berserk": "berserk.png",
    "swiftattack": "swiftattack.png",
    "shutout": "shutout.png",
    "lunarslash": "lunarslash.png",
    "aurablade": "aurablade.png",
    "gladiate": "gladiate.png",
    "hammerslam": "hammerslam.png",
    "cleavingattack": "cleavingattack.png",
    "stormblaze": "storm_blaze.png",
    "gardeblade": "gardeblade.png",
    "ogreslash": "ogreslash.png",
}


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
    ohs = _emoji("OHS_EMOJI", "OHS")
    ths = _emoji("THS_EMOJI", "THS")
    all_emoji = _emoji("ALL_EMOJI", "")
    all_weapons = f"{ohs} / {ths}" if not all_emoji else all_emoji
    fmt = {"ohs": ohs, "ths": ths, "all": all_weapons}
    fmt.update({k: _emoji(v, "") for k, v in SKILL_EMOJI_KEYS.items()})

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


