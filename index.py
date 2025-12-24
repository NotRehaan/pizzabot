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
        # Automatically load all cogs from the cogs folder
        print("Loading cogs...")
        loaded_cogs = []
        failed_cogs = []
        
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                cog_name = f"cogs.{filename[:-3]}"
                try:
                    await self.load_extension(cog_name)
                    loaded_cogs.append(cog_name)
                    print(f"✅ Loaded: {cog_name}")
                except Exception as e:
                    failed_cogs.append(cog_name)
                    print(f"❌ Failed to load {cog_name}: {e}")
        
        print(f"\n{'='*50}")
        print(f"Total cogs loaded: {len(loaded_cogs)}/{len(loaded_cogs) + len(failed_cogs)}")
        if loaded_cogs:
            print(f"Loaded cogs: {', '.join([cog.split('.')[-1] for cog in loaded_cogs])}")
        if failed_cogs:
            print(f"Failed cogs: {', '.join([cog.split('.')[-1] for cog in failed_cogs])}")
        print(f"{'='*50}\n")

        # Fast guild sync (dev)
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        print(f"✅ Commands synced to guild {GUILD_ID}")

    async def on_ready(self):
        print(f"\n{'='*50}")
        print(f"🍕 Bot is online as {self.user}")
        print(f"Bot ID: {self.user.id}")
        print(f"Guilds: {len(self.guilds)}")
        print(f"{'='*50}\n")

bot = MyBot()
bot.run(TOKEN)