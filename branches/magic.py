from embeds.magic import (
    SKILL_KEYS,
    TIERS,
    SKILL_TIER,
    get_skill_embeds,
    get_tier_embeds,
    get_tier_skill_keys,
    get_skills_index_embed,
    resolve_skill,
)
from storage.magic_index import (
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
    "**!skmagic <skill>** — Muestra una skill m\u00e1gica",
    "**!skmagic <skill> save** — Muestra y registra en el \u00edndice",
    "**!skmagic <tier>** — Muestra un tier completo (t1-t5)",
    "**!skmagic all** — Muestra todas las skills m\u00e1gicas",
    "**!skmagic list** — Lista de skills m\u00e1gicas disponibles",
    "**!skmagic index** — Muestra el \u00edndice actual de magia",
    "**!skmagic nuke** — Elimina mensajes m\u00e1gicos e \u00edndice en este canal",
    "**!skmagic scan** — Escanea el canal y registra skills m\u00e1gicas ya enviadas",
]


config = BranchConfig(
    command_name="skmagic",
    display_name="Magic",
    skill_keys=SKILL_KEYS,
    tiers=TIERS,
    skill_tier=SKILL_TIER,
    title_to_key=TITLE_TO_KEY,
    tier_order={"T0": 5, "T1": 0, "T2": 1, "T3": 2, "T4": 3, "T5": 4},
    tier_list=("t0", "t1", "t2", "t3", "t4", "t5"),
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
    index_updated_msg="\u00cdndice m\u00e1gico actualizado.",
    index_created_msg="\u00cdndice m\u00e1gico creado.",
    no_skills_msg="No hay skills m\u00e1gicas registradas todav\u00eda.",
    nuke_msg="\U0001f9f9 Mensajes m\u00e1gicos eliminados e \u00edndice reseteado.",
)


handlers = BranchHandlers(config)


async def branch_handle(ctx: commands.Context, *args: str) -> None:
    await handlers.handle_command(ctx, *args)


def register(bot):
    bot.command(name=config.command_name)(branch_handle)
