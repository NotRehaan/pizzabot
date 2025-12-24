import discord
from discord import app_commands
from discord.ext import commands
from openrouter import OpenRouter  
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GUILD_ID = 1453205366203748453

class DoughBot(commands.Cog):
    """Pizza-only AI cog"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="askpizza",
        description="Ask a pizza-related question"
    )
    @app_commands.describe(message="Your pizza question")
    async def askpizza(self, interaction: discord.Interaction, message: str):
        prompt = "You are a pizza-only assistant: every response must be strictly about pizza (ingredients, recipes, dough, ovens, styles, history, ordering, or pizza-related humor); if a user asks anything not related to pizza, politely redirect the conversation back to pizza without answering the off-topic request. The prompt is " + message

        # ACK immediately
        await interaction.response.defer(thinking=True)

        try:
            client = OpenRouter(api_key="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")
            response = client.chat.send(
                model="cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"OpenRouter error: {e}"

        await interaction.followup.send(reply)


async def setup(bot: commands.Bot):
    await bot.add_cog(DoughBot(bot))
