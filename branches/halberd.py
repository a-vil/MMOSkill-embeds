from embeds.halberd import (
    SKILL_KEYS,
    TIERS,
    SKILL_TIER,
    get_skill_embeds,
    get_tier_embeds,
    get_tier_skill_keys,
    get_skills_index_embed,
    resolve_skill,
)
from storage.halberd_index import (
    get_guild_data,
    save_index_message,
    save_skill,
    load_index,
    save_index,
)
from discord.ext import commands

from ._base import BranchConfig, BranchHandlers


TITLE_TO_KEY: dict[str, str] = {st.title: sk for sk, st in SKILL_KEYS.items()}


def _resolve_halberdmatk_link(
    embeds: list, extra_embeds: list, guild_id: int, guild_data: dict
) -> None:
    matk = guild_data["skills"].get("halberdmatkexplanation")
    if matk:
        url = f"https://discord.com/channels/{guild_id}/{matk['channel_id']}/{matk['message_id']}"
    else:
        url = "https://discord.com/channels/0/0/0"
    repl = f"[Halberd MATK]({url})"
    for e in embeds + extra_embeds:
        if e.description:
            e.description = e.description.replace("{halberdmatk_link}", repl)


HELP = [
    "**!skhalberd <skill>** — Muestra una skill de alabarda",
    "**!skhalberd <skill> save** — Muestra y registra en el \u00edndice",
    "**!skhalberd <tier>** — Muestra un tier completo (t1-t5)",
    "**!skhalberd all** — Muestra todas las skills de alabarda",
    "**!skhalberd list** — Lista de skills de alabarda disponibles",
    "**!skhalberd index** — Muestra el \u00edndice actual de alabarda",
    "**!skhalberd nuke** — Elimina mensajes de alabarda e \u00edndice en este canal",
    "**!skhalberd scan** — Escanea el canal y registra skills de alabarda ya enviadas",
]


config = BranchConfig(
    command_name="skhalberd",
    display_name="Halberd",
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
    resolve_embeds=_resolve_halberdmatk_link,
    send_all_direct=True,
    nuke_method="title_scan",
    index_updated_msg="\u00cdndice de alabarda actualizado.",
    index_created_msg="\u00cdndice de alabarda creado.",
    no_skills_msg="No hay skills de alabarda registradas todav\u00eda.",
    nuke_msg="\U0001f9f9 Mensajes de alabarda eliminados e \u00edndice reseteado.",
)


handlers = BranchHandlers(config)


async def branch_handle(ctx: commands.Context, *args: str) -> None:
    await handlers.handle_command(ctx, *args)


def register(bot):
    bot.command(name=config.command_name)(branch_handle)
