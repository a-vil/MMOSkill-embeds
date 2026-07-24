from dataclasses import dataclass, field
from typing import Callable, Optional

import discord
from discord.ext import commands


@dataclass
class BranchConfig:
    command_name: str
    skill_keys: dict
    tiers: dict
    skill_tier: dict
    title_to_key: dict
    tier_order: dict
    tier_list: tuple[str, ...]
    get_skill_embeds: Callable
    get_tier_skill_keys: Callable
    get_skills_index_embed: Callable
    resolve_skill: Callable
    get_guild_data: Callable
    save_skill: Callable
    save_index_message: Callable
    load_index: Callable
    save_index: Callable
    help_lines: list[str]
    display_name: str = ""
    index_updated_msg: str = "\u00cdndice actualizado."
    index_created_msg: str = "\u00cdndice creado."
    no_skills_msg: str = "No hay skills registradas todav\u00eda."
    nuke_msg: str = "\U0001f9f9 Mensajes eliminados e \u00edndice reseteado."
    resolve_embeds: Optional[Callable] = None
    send_all_direct: bool = False
    nuke_method: str = "title_scan"


class BranchHandlers:
    def __init__(self, cfg: BranchConfig):
        self.cfg = cfg

    def register(self, bot: commands.Bot) -> None:
        bot.command(name=self.cfg.command_name)(self.handle_command)

    async def handle_command(self, ctx: commands.Context, *args: str) -> None:
        guild = ctx.guild
        if guild is None:
            await ctx.send("Este comando solo puede usarse en un servidor.")
            return

        if not args:
            await self._send_help(ctx)
            return

        raw = " ".join(args)
        save_flag = raw.lower().endswith(" save")
        if save_flag:
            raw = raw[:-5].strip()

        cmd = raw.strip().lower()

        if cmd == "list":
            await self._send_list(ctx)
            return

        if cmd == "index":
            await self._send_index(ctx, guild)
            return

        if cmd == "nuke":
            await self._nuke_channel(ctx, guild)
            return

        if cmd == "scan":
            await self._scan_channel(ctx, guild)
            return

        if cmd in self.cfg.tiers:
            await self._send_tier(ctx, guild, cmd, save=save_flag)
            return

        if cmd == "all":
            await self._send_all(ctx, guild)
            return

        skill_key = self.cfg.resolve_skill(cmd)
        if skill_key is None:
            await ctx.send(
                f'Skill no encontrada: "{raw}". Usa `!{self.cfg.command_name} list` para ver las disponibles.'
            )
            return

        await self._send_skill(ctx, guild, skill_key, save_flag)

    async def _send_help(self, ctx: commands.Context) -> None:
        await ctx.send("\n".join(self.cfg.help_lines))

    async def _send_list(self, ctx: commands.Context) -> None:
        cfg = self.cfg
        lines = [f"**{cfg.display_name} Skills por Tier:**\n"]
        for tier_key in cfg.tier_list:
            tier_label = tier_key.upper()
            skill_keys = cfg.tiers[tier_key]
            skill_names = [cfg.skill_keys[sk].title for sk in skill_keys]
            lines.append(f"**{tier_label}:** {', '.join(skill_names)}")
        lines.append("")
        lines.append(f"Usa `!{cfg.command_name} <nombre>` para ver una skill.")
        await ctx.send("\n".join(lines))

    async def _send_index(self, ctx: commands.Context, guild: discord.Guild) -> None:
        cfg = self.cfg
        guild_data = cfg.get_guild_data(guild.id)
        if not guild_data["skills"]:
            await ctx.send(
                f"{cfg.no_skills_msg} "
                f"Usa `!{cfg.command_name} <skill> save` para registrar una."
            )
            return

        if guild_data["index"]:
            try:
                channel = guild.get_channel(guild_data["index"]["channel_id"])
                if isinstance(channel, discord.TextChannel):
                    index_msg = await channel.fetch_message(guild_data["index"]["message_id"])
                    index_embed = cfg.get_skills_index_embed(guild.id, guild_data["skills"])
                    await index_msg.edit(embed=index_embed)
                    await ctx.send(cfg.index_updated_msg)
                    return
            except discord.NotFound:
                pass

        index_embed = cfg.get_skills_index_embed(guild.id, guild_data["skills"])
        index_msg = await ctx.send(embed=index_embed)
        cfg.save_index_message(guild.id, index_msg.channel.id, index_msg.id)
        await ctx.send(cfg.index_created_msg)

    async def _update_index(self, ctx: commands.Context, guild: discord.Guild) -> None:
        cfg = self.cfg
        guild_data = cfg.get_guild_data(guild.id)
        if not guild_data["skills"]:
            return
        if guild_data["index"]:
            try:
                channel = guild.get_channel(guild_data["index"]["channel_id"])
                if isinstance(channel, discord.TextChannel):
                    index_msg = await channel.fetch_message(guild_data["index"]["message_id"])
                    index_embed = cfg.get_skills_index_embed(guild.id, guild_data["skills"])
                    await index_msg.edit(embed=index_embed)
                    return
            except discord.NotFound:
                pass
        index_embed = cfg.get_skills_index_embed(guild.id, guild_data["skills"])
        index_msg = await ctx.send(embed=index_embed)
        cfg.save_index_message(guild.id, index_msg.channel.id, index_msg.id)

    async def _send_skill(
        self, ctx: commands.Context, guild: discord.Guild, skill_key: str, save_flag: bool
    ) -> None:
        cfg = self.cfg
        embeds, extra_embeds, files = cfg.get_skill_embeds(skill_key)

        if cfg.resolve_embeds:
            guild_data = cfg.get_guild_data(guild.id)
            cfg.resolve_embeds(embeds, extra_embeds, guild.id, guild_data)

        msg = await ctx.send(embeds=embeds, files=files)
        for extra in extra_embeds:
            await ctx.send(embeds=[extra])

        if save_flag:
            skill = cfg.skill_keys[skill_key]
            tier = cfg.skill_tier.get(skill_key, "T?")
            cfg.save_skill(guild.id, skill_key, skill.title, tier, msg.channel.id, msg.id)
            await self._update_index(ctx, guild)

    async def _send_tier(
        self, ctx: commands.Context, guild: discord.Guild, tier_key: str, *, save: bool = False
    ) -> None:
        cfg = self.cfg
        skill_keys = cfg.get_tier_skill_keys(tier_key)
        sent_messages: list[discord.Message] = []
        for sk in skill_keys:
            embeds, extra_embeds, files = cfg.get_skill_embeds(sk)

            if cfg.resolve_embeds:
                guild_data = cfg.get_guild_data(guild.id)
                cfg.resolve_embeds(embeds, extra_embeds, guild.id, guild_data)

            msg = await ctx.send(embeds=embeds, files=files)
            for extra in extra_embeds:
                await ctx.send(embeds=[extra])
            sent_messages.append(msg)

        if not save:
            return

        for msg, sk in zip(sent_messages, skill_keys):
            skill = cfg.skill_keys[sk]
            cfg.save_skill(
                guild.id, sk, skill.title, cfg.skill_tier.get(sk, "T?"), msg.channel.id, msg.id
            )

        await self._update_index(ctx, guild)

    async def _send_all(self, ctx: commands.Context, guild: discord.Guild) -> None:
        cfg = self.cfg
        skill_registry: list[tuple[str, str, str, discord.Message]] = []

        if cfg.send_all_direct:
            guild_data = None
            if cfg.resolve_embeds:
                guild_data = cfg.get_guild_data(guild.id)

            for sk in cfg.skill_keys:
                embeds, extra_embeds, files = cfg.get_skill_embeds(sk)
                if cfg.resolve_embeds and guild_data is not None:
                    cfg.resolve_embeds(embeds, extra_embeds, guild.id, guild_data)
                msg = await ctx.send(embeds=embeds, files=files)
                for extra in extra_embeds:
                    await ctx.send(embeds=[extra])
                skill = cfg.skill_keys[sk]
                skill_registry.append((sk, skill.title, cfg.skill_tier.get(sk, "T?"), msg))
        else:
            for tier_key in cfg.tier_list:
                skill_keys = cfg.get_tier_skill_keys(tier_key)
                for sk in skill_keys:
                    embeds, extra_embeds, files = cfg.get_skill_embeds(sk)
                    msg = await ctx.send(embeds=embeds, files=files)
                    for extra in extra_embeds:
                        await ctx.send(embeds=[extra])
                    skill = cfg.skill_keys[sk]
                    skill_registry.append((sk, skill.title, cfg.skill_tier.get(sk, "T?"), msg))

        for sk, title, tier, msg in skill_registry:
            cfg.save_skill(guild.id, sk, title, tier, msg.channel.id, msg.id)

        await self._update_index(ctx, guild)

    async def _nuke_channel(self, ctx: commands.Context, guild: discord.Guild) -> None:
        channel = ctx.channel
        if not isinstance(channel, discord.TextChannel):
            return

        cfg = self.cfg
        guild_data = cfg.get_guild_data(guild.id)

        for info in guild_data.get("skills", {}).values():
            if info.get("channel_id") == channel.id:
                try:
                    msg = await channel.fetch_message(info["message_id"])
                    await msg.delete()
                except (discord.NotFound, discord.Forbidden):
                    pass

        idx = guild_data.get("index")
        if idx and idx.get("channel_id") == channel.id:
            try:
                msg = await channel.fetch_message(idx["message_id"])
                await msg.delete()
            except (discord.NotFound, discord.Forbidden):
                pass

        if cfg.nuke_method == "purge":
            try:
                await channel.purge(check=lambda m: m.author == ctx.bot.user)
            except (discord.Forbidden, discord.HTTPException):
                pass
        else:
            titles_set = set(cfg.title_to_key.keys())
            async for msg in channel.history(limit=200):
                if msg.author != ctx.bot.user:
                    continue
                if not msg.embeds:
                    continue
                title = msg.embeds[0].title
                if title and title in titles_set:
                    try:
                        await msg.delete()
                    except (discord.Forbidden, discord.HTTPException):
                        pass

        data = cfg.load_index()
        data["guilds"].pop(str(guild.id), None)
        cfg.save_index(data)
        await ctx.send(cfg.nuke_msg)

    async def _scan_channel(self, ctx: commands.Context, guild: discord.Guild) -> None:
        cfg = self.cfg
        found_skills: dict[str, dict] = {}

        async for msg in ctx.channel.history(limit=200):
            if msg.author != ctx.bot.user:
                continue
            if not msg.embeds:
                continue
            title = msg.embeds[0].title
            if not title:
                continue
            sk = cfg.title_to_key.get(title)
            if sk is None:
                continue
            if sk in found_skills:
                await ctx.send(
                    f"Error: La skill **{title}** est\u00e1 repetida "
                    f"(mensaje {found_skills[sk]['message_id']} y {msg.id}). "
                    "Escaneo cancelado."
                )
                return
            found_skills[sk] = {"channel_id": msg.channel.id, "message_id": msg.id}

        data = cfg.load_index()
        gid = str(guild.id)
        if gid not in data["guilds"]:
            data["guilds"][gid] = {"index": None, "skills": {}}
        data["guilds"][gid]["skills"] = {}

        for sk, info in found_skills.items():
            st = cfg.skill_keys[sk]
            data["guilds"][gid]["skills"][sk] = {
                "name": st.title,
                "tier": cfg.skill_tier.get(sk, "T?"),
                "channel_id": info["channel_id"],
                "message_id": info["message_id"],
            }

        cfg.save_index(data)
        await self._update_index(ctx, guild)
