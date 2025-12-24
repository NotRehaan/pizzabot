import discord
from discord import app_commands
from discord.ext import commands

class recipes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(
        name="recipes",
        description="View a pizza recipe"
    )
    @app_commands.describe(pizza="Choose a pizza recipe")
    @app_commands.choices(pizza=[
        app_commands.Choice(name="🍅 Margherita", value="margherita"),
        app_commands.Choice(name="🍕 Pepperoni", value="pepperoni"),
        app_commands.Choice(name="🍍 Hawaiian", value="hawaiian"),
        app_commands.Choice(name="🍗 BBQ Chicken", value="bbq_chicken"),
        app_commands.Choice(name="🥦 Veggie Supreme", value="veggie"),

    ])
    async def recipes(self, interaction: discord.Interaction, pizza: app_commands.Choice[str]):
        selected = pizza.value
        
        if selected == "margherita":
            await interaction.response.send_message("WIP")
        elif selected == "pepperoni":
            await interaction.response.send_message("WIP")

async def setup(bot):
    await bot.add_cog(recipes(bot))