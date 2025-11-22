import discord
from discord import app_commands
from openrouter import OpenRouter
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_GUILD_ID = (os.getenv("DISCORD_GUILD_ID"))

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=int(DISCORD_GUILD_ID)))
    print("Ready!")


@tree.command(
    name="testcommand",
    description="My first application Command",
    guild=discord.Object(id=DISCORD_GUILD_ID)
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")


bot.run(DISCORD_BOT_TOKEN)