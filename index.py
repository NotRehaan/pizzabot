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
    await tree.sync(guild=discord.Object(id=(1452508670532391024)))
    print("Ready!")


@tree.command(
    name="testcommand",
    description="My first application Command",
    guild=discord.Object(id=1452508670532391024)
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(
    name="ai",
    description="Test the AI response",
    guild=discord.Object(id=1452508670532391024)
)
async def say(interaction: discord.Interaction, message: str):
    prompttest = "You are a pizza-only assistant: every response must be strictly about pizza (ingredients, recipes, dough, ovens, styles, history, ordering, or pizza-related humor); if a user asks anything not related to pizza, politely redirect the conversation back to pizza without answering the off-topic request. The prompt is " + message
    # ACK within 3 seconds
    await interaction.response.defer(thinking=True)

    try:
        with OpenRouter(api_key="") as client:
            response = client.chat.send(
                model="cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
                messages=[{"role": "user", "content": prompttest}]
            )
            reply = response.choices[0].message.content
    except Exception as e:
        reply = f"OpenRouter error: {e}"

    # Send the response properly
    await interaction.followup.send(reply)


bot.run("")
