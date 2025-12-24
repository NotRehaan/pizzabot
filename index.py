import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))

intents = discord.Intents.default()

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",  # unused but REQUIRED
            intents=intents
        )

    async def setup_hook(self):
        # Load cogs/extensions
        await self.load_extension("cogs.ping")
        await self.load_extension("cogs.reload")
        await self.load_extension("cogs.DoughBot")
        await self.load_extension("cogs.help")
        

        # Fast guild sync (dev)
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

bot = MyBot()
bot.run(TOKEN)