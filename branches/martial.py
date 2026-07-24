from embeds.martial import (
    SKILL_KEYS,
    TIERS,
    SKILL_TIER,
    get_skill_embeds,
    get_tier_embeds,
    get_tier_skill_keys,
    get_skills_index_embed,
    resolve_skill,
)
from storage.martial_index import (
    get_guild_data,
    save_index_message,
    save_skill,
    load_index,
    save_index,
)
from ._base import BranchConfig, BranchHandlers


TITLE_TO_KEY: dict[str, str] = {st.title: sk for sk, st in SKILL_KEYS.items()}


HELP = [
    "**!skmartial <skill>** — Muestra una skill marcial",
    "**!skmartial <skill> save** — Muestra y registra en el \u00edndice",
    "**!skmartial <tier>** — Muestra un tier completo (t1-t5)",
    "**!skmartial all** — Muestra todas las skills marciales",
    "**!skmartial list** — Lista de skills marciales disponibles",
    "**!skmartial index** — Muestra el \u00edndice actual marcial",
    "**!skmartial nuke** — Elimina mensajes marciales e \u00edndice en este canal",
    "**!skmartial scan** — Escanea el canal y registra skills marciales ya enviadas",
]


config = BranchConfig(
    command_name="skmartial",
    display_name="Martial",
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
    index_updated_msg="\u00cdndice marcial actualizado.",
    index_created_msg="\u00cdndice marcial creado.",
    no_skills_msg="No hay skills marciales registradas todav\u00eda.",
    nuke_msg="\U0001f9f9 Mensajes marciales eliminados e \u00edndice reseteado.",
)


handlers = BranchHandlers(config)


def register(bot):
    handlers.register(bot)
