import discord
from discord import Embed, app_commands
from discord.ext import commands
from datetime import datetime

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="help",
        description="gives info about the bot"
    )
    async def help_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="AY TONY! IM MAKING THE PIZZA HERE!",
            colour=0x00b0f4,
            timestamp=datetime.now()
        )

        embed.set_author(
            name="PizzaBot",
            icon_url="https://assets.surlatable.com/m/15a89c2d9c6c1345/72_dpi_webp-REC-283110_Pizza-jpg"
        )

        embed.add_field(
            name="/Help",
            value="This command right here, shows all the commands!",
            inline=False
        )
        embed.add_field(
            name="/recipeselect",
            value="gives you the choice of 10 whole pizza recipes to choose from!\nWill display the full recipes for you to read and make!",
            inline=False
        )
        embed.add_field(
            name="/askpizza",
            value="ask an AI chatbot any question about pizza! such as ingredients substitutions or different cooking methods!",
            inline=False
        )
        embed.add_field(
            name="/customrecipes",
            value="ask an AI chatbot to make you an unique pizza recipe using your prompt such as \"Fish Pizza\" or \"Dessert Pizza\"!",
            inline=False
        )

        embed.set_thumbnail(
            url="https://c8.alamy.com/comp/HHGTR2/male-masculine-sausage-pizza-italian-pepperoni-olives-chef-man-HHGTR2.jpg"
        )

        embed.set_footer(
            text="mama mia",
            icon_url="https://thumbs.dreamstime.com/b/italian-pizza-chef-handlebar-mustache-holding-peel-52029167.jpg"
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot))