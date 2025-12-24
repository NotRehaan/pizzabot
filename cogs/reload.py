import discord
from discord.ext import commands
from discord import app_commands

class ReloadCog(commands.Cog):
    """Reloads other cogs without restarting the bot"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

 
    @app_commands.command(
        name="reload",
        description="Reload a specified cog"
    )
    @app_commands.describe(cog_name="The name of the cog to reload (without .py)")
    async def reload(self, interaction: discord.Interaction, cog_name: str):
        try:
            await self.bot.reload_extension(f"cogs.{cog_name}")
            await interaction.response.send_message(
                f"✅ Successfully reloaded `{cog_name}`",
                ephemeral=True
            )
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Failed to reload `{cog_name}`\nError: `{e}`",
                ephemeral=True
            )

    @app_commands.command(
        name="cogs",
        description="List all currently loaded cogs"
    )
    async def list_cogs(self, interaction: discord.Interaction):
        loaded = list(self.bot.extensions.keys())
        if loaded:
            await interaction.response.send_message(
                "**Loaded cogs:**\n" + "\n".join(loaded),
                ephemeral=True
            )
        else:
            await interaction.response.send_message(
                "No cogs are currently loaded.",
                ephemeral=True
            )

async def setup(bot: commands.Bot):
    await bot.add_cog(ReloadCog(bot))
