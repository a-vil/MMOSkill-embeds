import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from branches import register_all


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    if bot.user:
        print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


class CleanView(discord.ui.View):
    message: discord.Message

    def __init__(self, ctx: commands.Context):
        super().__init__(timeout=30)
        self.ctx = ctx

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.ctx.author.id:
            await interaction.response.send_message(
                "Solo quien us\u00f3 el comando puede responder.", ephemeral=True
            )
            return False
        return True

    async def on_timeout(self):
        try:
            await self.message.delete()
        except (discord.NotFound, discord.HTTPException):
            pass

    @discord.ui.button(label="S\u00ed, limpiar", style=discord.ButtonStyle.danger)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        channel = self.ctx.channel
        if isinstance(channel, discord.TextChannel):
            await channel.purge(limit=50, check=lambda m: len(m.embeds) > 0)
        try:
            await self.message.delete()
        except (discord.NotFound, discord.HTTPException):
            pass

    @discord.ui.button(label="No", style=discord.ButtonStyle.secondary)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        try:
            await self.message.delete()
        except (discord.NotFound, discord.HTTPException):
            pass


@bot.command(name="clean")
async def clean(ctx: commands.Context) -> None:
    view = CleanView(ctx)
    msg = await ctx.send(
        "\u00bfEliminar todos los mensajes con embeds en este canal (m\u00e1x. 50)?",
        view=view,
    )
    view.message = msg


register_all(bot)


if __name__ == "__main__":
    if not TOKEN:
        msg = "DISCORD_TOKEN not found in .env file."
        raise ValueError(msg)
    bot.run(TOKEN)
