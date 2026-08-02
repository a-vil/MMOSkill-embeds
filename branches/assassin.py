from embeds.assassin import (
    SKILL_KEYS,
    TIERS,
    SKILL_TIER,
    get_skill_embeds,
    get_tier_embeds,
    get_tier_skill_keys,
    get_skills_index_embed,
    resolve_skill,
)
from storage.assassin_index import (
    get_guild_data,
    save_index_message,
    save_skill,
    load_index,
    save_index,
)
from discord.ext import commands

from ._base import BranchConfig, BranchHandlers


TITLE_TO_KEY: dict[str, str] = {st.title: sk for sk, st in SKILL_KEYS.items()}


HELP = [
    "**!skassassin <skill>** — Muestra una skill de asesino",
    "**!skassassin <skill> save** — Muestra y registra en el \u00edndice",
    "**!skassassin <tier>** — Muestra un tier completo (t1-t5)",
    "**!skassassin all** — Muestra todas las skills de asesino",
    "**!skassassin list** — Lista de skills de asesino disponibles",
    "**!skassassin index** — Muestra el \u00edndice actual de asesino",
    "**!skassassin nuke** — Elimina mensajes de asesino e \u00edndice en este canal",
    "**!skassassin scan** — Escanea el canal y registra skills de asesino ya enviadas",
]


config = BranchConfig(
    command_name="skassassin",
    display_name="Assassin",
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
    nuke_method="purge",
)


handlers = BranchHandlers(config)


async def branch_handle(ctx: commands.Context, *args: str) -> None:
    await handlers.handle_command(ctx, *args)


def register(bot):
    bot.command(name=config.command_name)(branch_handle)
