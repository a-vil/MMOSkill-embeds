from pathlib import Path
import os
import re

import discord

from data.es_shalberd import (
    FOOTER,
    INDEX_HEADER,
    SkillText,
    FLASH_STAB,
    CANNON_SPEAR,
    DRAGON_TAIL,
    DIVE_IMPACT,
    DRAGON_TOOTH,
    DEADLY_SPEAR,
    PUNISH_RAY,
    STRIKE_STAB,
    CHRONOS_DRIVE,
    HALBERD_MASTERY,
    CRITICAL_SPEAR,
    QUICK_AURA,
    WAR_CRY_OF_STRUGGLE,
    GODSPEED_WIELD,
    BUSTER_LANCE,
    GRAND_BUSTER_LANCE,
    DRACONIC_CHARGE,
    INFINITE_DIMENSION,
    TORNADO_LANCE,
    ALMIGHTY_WIELD,
    HALBERD_MATK_EXPLANATION,
    BLITZ_SPIKE,
    LIGHTNING_HAIL,
    THORS_HAMMER,
    DRACONIC_CHARGE_EXTRA,
)


BASE_IMG_PATH = Path(__file__).resolve().parent.parent / "imgs" / "halberd"


def _emoji(env_name: str, fallback: str) -> str:
    return os.getenv(env_name) or fallback


def _fmt(text: str, kwargs: dict) -> str:
    placeholders = set(re.findall(r"\{(\w+)\}", text))
    for k, v in kwargs.items():
        if k in placeholders:
            text = text.replace(f"{{{k}}}", v)
    return text


SKILL_KEYS: dict[str, SkillText] = {
    "flashstab": FLASH_STAB,
    "cannonspear": CANNON_SPEAR,
    "dragontail": DRAGON_TAIL,
    "diveimpact": DIVE_IMPACT,
    "dragontooth": DRAGON_TOOTH,
    "deadlyspear": DEADLY_SPEAR,
    "punishray": PUNISH_RAY,
    "strikestab": STRIKE_STAB,
    "chronosdrive": CHRONOS_DRIVE,
    "halberdmastery": HALBERD_MASTERY,
    "criticalsper": CRITICAL_SPEAR,
    "quickaura": QUICK_AURA,
    "warcryofstruggle": WAR_CRY_OF_STRUGGLE,
    "godspeedwield": GODSPEED_WIELD,
    "busterlance": BUSTER_LANCE,
    "grandbusterlance": GRAND_BUSTER_LANCE,
    "draconiccharge": DRACONIC_CHARGE,
    "infinitedimension": INFINITE_DIMENSION,
    "tornadolance": TORNADO_LANCE,
    "almightywield": ALMIGHTY_WIELD,
    "halberdmatkexplanation": HALBERD_MATK_EXPLANATION,
    "blitzspike": BLITZ_SPIKE,
    "lightninghail": LIGHTNING_HAIL,
    "thorshammer": THORS_HAMMER,
}

ALIASES: dict[str, str] = {
    "fstab": "flashstab",
    "flash": "flashstab",
    "cspear": "cannonspear",
    "cannon": "cannonspear",
    "dtail": "dragontail",
    "dt": "dragontail",
    "dimpact": "diveimpact",
    "dive": "diveimpact",
    "dtooth": "dragontooth",
    "dspear": "deadlyspear",
    "deadly": "deadlyspear",
    "pray": "punishray",
    "punish": "punishray",
    "sstab": "strikestab",
    "strike": "strikestab",
    "cdrive": "chronosdrive",
    "chronos": "chronosdrive",
    "hmast": "halberdmastery",
    "hmastery": "halberdmastery",
    "cspear": "criticalsper",
    "cs": "criticalsper",
    "qaura": "quickaura",
    "qa": "quickaura",
    "warcry": "warcryofstruggle",
    "wcos": "warcryofstruggle",
    "gsw": "godspeedwield",
    "godspeed": "godspeedwield",
    "blance": "busterlance",
    "buster": "busterlance",
    "gblance": "grandbusterlance",
    "gb": "grandbusterlance",
    "dcharge": "draconiccharge",
    "draconic": "draconiccharge",
    "idimension": "infinitedimension",
    "id": "infinitedimension",
    "tlance": "tornadolance",
    "tl": "tornadolance",
    "awield": "almightywield",
    "almighty": "almightywield",
    "hmatk": "halberdmatkexplanation",
    "halberdmatk": "halberdmatkexplanation",
    "blitz": "blitzspike",
    "bspike": "blitzspike",
    "lhail": "lightninghail",
    "lightning": "lightninghail",
    "thor": "thorshammer",
    "thammer": "thorshammer",
}

TIERS: dict[str, list[str]] = {
    "t0": ["grandbusterlance", "halberdmatkexplanation"],
    "t1": ["flashstab", "cannonspear", "deadlyspear", "halberdmastery", "quickaura"],
    "t2": ["dragontail", "punishray", "warcryofstruggle"],
    "t3": ["diveimpact", "strikestab", "criticalsper", "busterlance", "blitzspike"],
    "t4": ["dragontooth", "chronosdrive", "godspeedwield", "lightninghail"],
    "t5": [
        "draconiccharge", "infinitedimension", "tornadolance",
        "almightywield", "thorshammer",
    ],
}

SKILL_TIER: dict[str, str] = {}
for tier_key, skill_list in TIERS.items():
    for sk in skill_list:
        SKILL_TIER[sk] = tier_key.upper()

SKILL_IMAGES: dict[str, str] = {
    "flashstab": "flashstab.png",
    "cannonspear": "cannonspear.png",
    "dragontail": "dragontail.png",
    "diveimpact": "diveimpact.png",
    "dragontooth": "dragontooth.png",
    "deadlyspear": "deadlyspear.png",
    "punishray": "punishray.png",
    "strikestab": "strikestab.png",
    "chronosdrive": "chronosdrive.png",
    "halberdmastery": "halberdmastery.png",
    "criticalsper": "criticalspear.png",
    "quickaura": "quickaura.png",
    "warcryofstruggle": "warcryofstruggle.png",
    "godspeedwield": "godspeedwield.png",
    "busterlance": "busterlance.png",
    "draconiccharge": "draconiccharge.png",
    "infinitedimension": "infinitedimension.png",
    "tornadolance": "tornadolance.png",
    "almightywield": "godspeedwield.png",
    "blitzspike": "blitzspike.png",
    "lightninghail": "lightninghail.png",
    "thorshammer": "thorshammer.png",
}

SKILL_EXTRA: dict[str, str] = {
    "draconiccharge": DRACONIC_CHARGE_EXTRA,
}

SKILL_EMOJIS: dict[str, str] = {
    FLASH_STAB.title: "FLASH_STAB_EMOJI",
    CANNON_SPEAR.title: "CANNON_SPEAR_EMOJI",
    DRAGON_TAIL.title: "DRAGON_TAIL_EMOJI",
    DIVE_IMPACT.title: "DIVE_IMPACT_EMOJI",
    DRAGON_TOOTH.title: "DRAGON_TOOTH_EMOJI",
    DEADLY_SPEAR.title: "DEADLY_SPEAR_EMOJI",
    PUNISH_RAY.title: "PUNISH_RAY_EMOJI",
    STRIKE_STAB.title: "STRIKE_STAB_EMOJI",
    CHRONOS_DRIVE.title: "CHRONOS_DRIVE_EMOJI",
    HALBERD_MASTERY.title: "HALBERD_MASTERY_EMOJI",
    CRITICAL_SPEAR.title: "CRITICAL_SPEAR_EMOJI",
    QUICK_AURA.title: "QUICK_AURA_EMOJI",
    WAR_CRY_OF_STRUGGLE.title: "WAR_CRY_OF_STRUGGLE_EMOJI",
    GODSPEED_WIELD.title: "GODSPEED_WIELD_EMOJI",
    BUSTER_LANCE.title: "BUSTER_LANCE_EMOJI",
    GRAND_BUSTER_LANCE.title: "GRAND_BUSTER_LANCE_EMOJI",
    DRACONIC_CHARGE.title: "DRACONIC_CHARGE_EMOJI",
    INFINITE_DIMENSION.title: "INFINITE_DIMENSION_EMOJI",
    TORNADO_LANCE.title: "TORNADO_LANCE_EMOJI",
    ALMIGHTY_WIELD.title: "ALMIGHTY_WIELD_EMOJI",
    HALBERD_MATK_EXPLANATION.title: "HALBERD_MATK_EXPLANATION_EMOJI",
    BLITZ_SPIKE.title: "BLITZ_SPIKE_EMOJI",
    LIGHTNING_HAIL.title: "LIGHTNING_HAIL_EMOJI",
    THORS_HAMMER.title: "THORS_HAMMER_EMOJI",
}

TIER_ORDER = {"T0": 5, "T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4}


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
    ohs = _emoji("OHS_EMOJI", "OHS")
    halberd = _emoji("HALBERD_EMOJI", "Halberd")
    all_emoji = _emoji("ALL_EMOJI", "")
    all_weapons = f"{ohs} / {halberd}" if not all_emoji else all_emoji
    fmt = {"ohs": ohs, "halberd": halberd, "all": all_weapons}

    overview = discord.Embed(
        title=skill.title,
        description=skill.description,
        color=discord.Color.blue(),
    )

    t0_keys = TIERS.get("t0", [])
    is_t0 = skill_key in t0_keys
    files: list[discord.File] = []
    if not is_t0:
        img_path = _get_image_path(skill_key)
        if img_path:
            filename = img_path.name
            overview.set_thumbnail(url=f"attachment://{filename}")
            files.append(discord.File(img_path, filename=filename))

    embeds = [overview]

    if skill.details:
        details = discord.Embed(
            description=_fmt(skill.details, fmt),
            color=discord.Color.blue(),
        )
        details.set_footer(text=FOOTER)
        embeds.append(details)

    extra_embeds: list[discord.Embed] = []
    extra_text = SKILL_EXTRA.get(skill_key)
    if extra_text:
        extra = discord.Embed(
            description=_fmt(extra_text, fmt),
            color=discord.Color.blue(),
        )
        extra.set_footer(text=FOOTER)
        extra_embeds.append(extra)

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
        if skill["tier"] == "T0":
            continue
        link = f"https://discord.com/channels/{guild_id}/{skill['channel_id']}/{skill['message_id']}"
        emoji_env = SKILL_EMOJIS.get(skill["name"])
        skill_emoji = _emoji(emoji_env, "") if emoji_env else ""
        emoji_part = f" {skill_emoji}" if skill_emoji else ""
        description_lines.append(f"{skill['tier']}{emoji_part} [{skill['name']}]({link})")

    t0_skills = [s for s in sorted_skills if s["tier"] == "T0"]
    if t0_skills:
        description_lines.append("")
        description_lines.append("**Otros:**")
        for skill in t0_skills:
            link = f"https://discord.com/channels/{guild_id}/{skill['channel_id']}/{skill['message_id']}"
            emoji_env = SKILL_EMOJIS.get(skill["name"])
            skill_emoji = _emoji(emoji_env, "") if emoji_env else ""
            emoji_part = f" {skill_emoji}" if skill_emoji else ""
            description_lines.append(f"{emoji_part}[{skill['name']}]({link})")

    embed.description = "\n".join(description_lines)
    embed.set_footer(text="📌Nota: Puedes usar el mensaje fijado, para volver aquí.")
    return embed
