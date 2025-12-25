import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

class RecipeView(discord.ui.View):
    def __init__(self, recipe_name):
        super().__init__(timeout=180)
        self.recipe_name = recipe_name
        self.current_page = "notes"
    
    @discord.ui.button(label="📝 Notes", style=discord.ButtonStyle.secondary, custom_id="notes")
    async def notes_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = self.get_notes_embed()
        await interaction.response.edit_message(embed=embed, view=self)
    
    @discord.ui.button(label="🛒 Ingredients", style=discord.ButtonStyle.primary, custom_id="ingredients")
    async def ingredients_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = self.get_ingredients_embed()
        await interaction.response.edit_message(embed=embed, view=self)
    
    @discord.ui.button(label="👨‍🍳 Instructions", style=discord.ButtonStyle.success, custom_id="instructions")
    async def instructions_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = self.get_instructions_embed()
        await interaction.response.edit_message(embed=embed, view=self)
    
    def get_notes_embed(self):
        embeds = {
            "margherita": discord.Embed(
                title="🍅 Margherita Pizza - Notes!",
                colour=0xf50000,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot - The OG Pizza",
                icon_url="https://ca.ooni.com/cdn/shop/articles/20220211142645-margherita-9920.jpg?v=1737367039&width=1080"
            ).add_field(
                name="Nutrition (Approx. per pizza)",
                value="Calories: ~1,200–1,300 kcal\nProtein: ~45 g\nCarbohydrates: ~140 g\nFat: ~55 g",
                inline=False
            ).add_field(
                name="⏱️ Prep Time",
                value="Prep: 10 minutes\nCook: 12 minutes\nTotal: ~22 minutes",
                inline=False
            ).add_field(
                name="🎯 Difficulty Level",
                value="**Easy** - Perfect for beginners!\nTechnique-focused, not ingredient-heavy",
                inline=False
            ).add_field(
                name="💡 Extra Notes",
                value="• Ingredient quality matters more than technique\n• Fresh mozzarella must be patted dry (nobody likes soggy pizza!)\n• Ideal for pizza stones or steel\n• Less is more - don't overload it!",
                inline=False
            ).set_footer(text="The pizza that started it all! 🇮🇹"),
            
            "pepperoni": discord.Embed(
                title="🍕 Pepperoni Pizza - Notes!",
                colour=0xff4500,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot - America's Favorite",
                icon_url="https://www.allrecipes.com/thmb/0zgX8uV3f5rqjDrSJY2mCEPXv7Y=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/240376-homemade-pepperoni-pizza-Beauty-3x4-1-6ae54059c23348b3b9a703b6a3067a44.jpg"
            ).add_field(
                name="Nutrition (Approx. per pizza)",
                value="Calories: ~1,800–2,000 kcal\nProtein: ~75 g\nCarbohydrates: ~160 g\nFat: ~85 g",
                inline=False
            ).add_field(
                name="⏱️ Prep Time",
                value="Prep: 8 minutes\nCook: 14 minutes\nTotal: ~22 minutes",
                inline=False
            ).add_field(
                name="🎯 Difficulty Level",
                value="**Very Easy** - Even easier than Margherita!\nHard to mess this one up, folks",
                inline=False
            ).add_field(
                name="💡 Extra Notes",
                value="• Use quality pepperoni (trust me, it matters)\n• Layer pepperoni AFTER cheese for crispy edges\n• Some pepperoni will cup up and get crispy (that's the good stuff)\n• Double pepperoni? No judgment here 👀",
                inline=False
            ).set_footer(text="The crowd pleaser! Can't go wrong with this classic 🇺🇸"),
            
            "hawaiian": discord.Embed(
                title="🍍 Hawaiian Pizza - Notes!",
                colour=0xffd700,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot - The Controversial One",
                icon_url="https://www.sargento.com/assets/Uploads/Recipe/Image/Sargento11501__FillWzExNzAsNTgzXQ.jpg"
            ).add_field(
                name="Nutrition (Approx. per pizza)",
                value="Calories: ~1,600–1,700 kcal\nProtein: ~65 g\nCarbohydrates: ~180 g\nFat: ~60 g",
                inline=False
            ).add_field(
                name="⏱️ Prep Time",
                value="Prep: 10 minutes\nCook: 13 minutes\nTotal: ~23 minutes",
                inline=False
            ).add_field(
                name="🎯 Difficulty Level",
                value="**Easy** - The hardest part is defending your choice\nSeriously though, it's simple to make",
                inline=False
            ).add_field(
                name="💡 Extra Notes",
                value="• Drain pineapple WELL (seriously, pat it dry)\n• Use canned pineapple chunks, not fresh\n• The sweet + salty combo is *chef's kiss*\n• Haters gonna hate, but you'll love it\n• Canadian bacon works better than regular ham",
                inline=False
            ).set_footer(text="Don't knock it till you try it! 🍍🍕 (Fight me)"),
            
            "bbq_chicken": discord.Embed(
                title="🌶️ BBQ Chicken Pizza - Notes!",
                colour=0x8b4513,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot - The BBQ Lover's Dream",
                icon_url="https://www.jocooks.com/wp-content/uploads/2012/03/bbq-chicken-pizza-1-7.jpg"
            ).add_field(
                name="Nutrition (Approx. per pizza)",
                value="Calories: ~1,700–1,900 kcal\nProtein: ~85 g\nCarbohydrates: ~175 g\nFat: ~70 g",
                inline=False
            ).add_field(
                name="⏱️ Prep Time",
                value="Prep: 15 minutes\nCook: 14 minutes\nTotal: ~29 minutes",
                inline=False
            ).add_field(
                name="🎯 Difficulty Level",
                value="**Medium** - Requires pre-cooking chicken\nBut worth every minute!",
                inline=False
            ).add_field(
                name="💡 Extra Notes",
                value="• Pre-cook and season your chicken well\n• Don't skimp on the BBQ sauce (it's the star!)\n• Red onions add a nice bite\n• Cilantro at the end is a game-changer\n• Mix mozzarella with a bit of cheddar for extra flavor",
                inline=False
            ).set_footer(text="When regular pizza just won't cut it! 🔥"),
        }
        return embeds.get(self.recipe_name)
    
    def get_ingredients_embed(self):
        embeds = {
            "margherita": discord.Embed(
                title="🍅 Margherita Pizza - Ingredients!",
                description="**The Simple & Classic**\n\n"
                            "• Pizza dough (1 ball, ~250g)\n"
                            "• San Marzano tomatoes (200g, crushed)\n"
                            "• Fresh mozzarella (150g, sliced)\n"
                            "• Fresh basil leaves (handful)\n"
                            "• Extra virgin olive oil (1–2 tbsp)\n"
                            "• Salt (to taste)\n"
                            "• Optional: Parmesan for finishing",
                colour=0xf50000,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot",
                icon_url="https://ca.ooni.com/cdn/shop/articles/20220211142645-margherita-9920.jpg?v=1737367039&width=1080"
            ).set_footer(text="Quality over quantity! 🇮🇹"),
            
            "pepperoni": discord.Embed(
                title="🍕 Pepperoni Pizza - Ingredients!",
                description="**The All-American Classic**\n\n"
                            "• Pizza dough (1 ball, ~250g)\n"
                            "• Pizza sauce or marinara (250ml)\n"
                            "• Mozzarella cheese (200g, shredded)\n"
                            "• Pepperoni slices (100g, about 30-40 slices)\n"
                            "• Dried oregano (1 tsp)\n"
                            "• Garlic powder (1/2 tsp)\n"
                            "• Red pepper flakes (optional, for heat)\n"
                            "• Olive oil (for brushing crust)",
                colour=0xff4500,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot",
                icon_url="https://www.allrecipes.com/thmb/0zgX8uV3f5rqjDrSJY2mCEPXv7Y=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/240376-homemade-pepperoni-pizza-Beauty-3x4-1-6ae54059c23348b3b9a703b6a3067a44.jpg"
            ).set_footer(text="More pepperoni = more happiness 🍕"),
            
            "hawaiian": discord.Embed(
                title="🍍 Hawaiian Pizza - Ingredients!",
                description="**The Sweet & Savory Rebel**\n\n"
                            "• Pizza dough (1 ball, ~250g)\n"
                            "• Pizza sauce (200ml)\n"
                            "• Mozzarella cheese (180g, shredded)\n"
                            "• Canadian bacon or ham (150g, diced)\n"
                            "• Pineapple chunks (200g, WELL DRAINED)\n"
                            "• Optional: bacon bits for extra flavor\n"
                            "• Optional: jalapeños if you're feeling spicy\n"
                            "• Red pepper flakes (to taste)",
                colour=0xffd700,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot",
                icon_url="https://www.sargento.com/assets/Uploads/Recipe/Image/Sargento11501__FillWzExNzAsNTgzXQ.jpg"
            ).set_footer(text="Pineapple DOES belong on pizza! 🍍✨"),
            
            "bbq_chicken": discord.Embed(
                title="🌶️ BBQ Chicken Pizza - Ingredients!",
                description="**The Flavor Bomb**\n\n"
                            "• Pizza dough (1 ball, ~250g)\n"
                            "• BBQ sauce (150ml, your favorite brand)\n"
                            "• Cooked chicken breast (200g, diced or shredded)\n"
                            "• Mozzarella cheese (150g, shredded)\n"
                            "• Cheddar cheese (50g, shredded)\n"
                            "• Red onion (1/2, thinly sliced)\n"
                            "• Fresh cilantro (handful, for topping)\n"
                            "• Smoked paprika (1/2 tsp)",
                colour=0x8b4513,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot",
                icon_url="https://www.jocooks.com/wp-content/uploads/2012/03/bbq-chicken-pizza-1-7.jpg"
            ).set_footer(text="BBQ sauce makes everything better! 🔥"),
        }
        return embeds.get(self.recipe_name)
    
    def get_instructions_embed(self):
        embeds = {
            "margherita": discord.Embed(
                title="🍅 Margherita Pizza - Instructions!",
                description="**Let's Make Some Magic**\n\n"
                            "1️⃣ Preheat oven to 475°F / 245°C (crank it HIGH!)\n\n"
                            "2️⃣ Stretch dough into a 12-inch circle (don't roll it, stretch gently from the center)\n\n"
                            "3️⃣ Spread crushed tomatoes evenly, leaving a 1-inch border for that perfect crust\n\n"
                            "4️⃣ Add mozzarella slices (tear them if they're too big)\n\n"
                            "5️⃣ Drizzle olive oil and sprinkle salt like you mean it\n\n"
                            "6️⃣ Bake 10–14 minutes until crust is golden and cheese is bubbly\n\n"
                            "7️⃣ Top with fresh basil AFTER baking (heat kills the flavor!)\n\n"
                            "**Pro tip:** The basil should wilt slightly from the heat but stay bright green!",
                colour=0xf50000,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot",
                icon_url="https://ca.ooni.com/cdn/shop/articles/20220211142645-margherita-9920.jpg?v=1737367039&width=1080"
            ).set_footer(text="Simplicity at its finest! Mangia! 🇮🇹"),
            
            "pepperoni": discord.Embed(
                title="🍕 Pepperoni Pizza - Instructions!",
                description="**The Easiest Pizza You'll Ever Make**\n\n"
                            "1️⃣ Preheat oven to 475°F / 245°C\n\n"
                            "2️⃣ Stretch dough into a 12-inch circle (use your fists like a real pizza maker!)\n\n"
                            "3️⃣ Spread pizza sauce evenly, leaving a border\n\n"
                            "4️⃣ Sprinkle mozzarella cheese generously\n\n"
                            "5️⃣ Layer pepperoni slices on top (overlap them if you're hungry)\n\n"
                            "6️⃣ Sprinkle oregano and garlic powder\n\n"
                            "7️⃣ Bake 12–15 minutes until pepperoni edges curl up and get crispy\n\n"
                            "8️⃣ Add red pepper flakes if you like it spicy\n\n"
                            "**Pro tip:** Brush the crust with garlic butter before baking for extra flavor!",
                colour=0xff4500,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot",
                icon_url="https://www.allrecipes.com/thmb/0zgX8uV3f5rqjDrSJY2mCEPXv7Y=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/240376-homemade-pepperoni-pizza-Beauty-3x4-1-6ae54059c23348b3b9a703b6a3067a44.jpg"
            ).set_footer(text="Can't mess this up! Enjoy! 🍕"),
            
            "hawaiian": discord.Embed(
                title="🍍 Hawaiian Pizza - Instructions!",
                description="**Embrace The Controversy**\n\n"
                            "1️⃣ Preheat oven to 475°F / 245°C\n\n"
                            "2️⃣ Stretch dough into a 12-inch circle\n\n"
                            "3️⃣ Spread pizza sauce evenly\n\n"
                            "4️⃣ Add mozzarella cheese\n\n"
                            "5️⃣ Distribute ham/Canadian bacon pieces evenly\n\n"
                            "6️⃣ Add pineapple chunks (make sure they're DRY or your pizza will be soggy!)\n\n"
                            "7️⃣ Optional: Add jalapeños for a spicy-sweet kick\n\n"
                            "8️⃣ Bake 12–15 minutes until crust is golden\n\n"
                            "9️⃣ Let cool for 2 minutes before slicing (resist the urge!)\n\n"
                            "**Pro tip:** The pineapple will caramelize slightly - that's the good stuff!",
                colour=0xffd700,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot",
                icon_url="https://www.sargento.com/assets/Uploads/Recipe/Image/Sargento11501__FillWzExNzAsNTgzXQ.jpg"
            ).set_footer(text="Haters gonna hate! 🍍🍕"),
            
            "bbq_chicken": discord.Embed(
                title="🌶️ BBQ Chicken Pizza - Instructions!",
                description="**Let's Get Saucy**\n\n"
                            "1️⃣ Preheat oven to 475°F / 245°C\n\n"
                            "2️⃣ Cook and season chicken breast, then dice or shred it\n\n"
                            "3️⃣ Toss chicken in half the BBQ sauce\n\n"
                            "4️⃣ Stretch dough into a 12-inch circle\n\n"
                            "5️⃣ Spread remaining BBQ sauce as your base (instead of tomato sauce)\n\n"
                            "6️⃣ Mix mozzarella and cheddar, sprinkle on pizza\n\n"
                            "7️⃣ Add BBQ chicken pieces evenly\n\n"
                            "8️⃣ Top with sliced red onions\n\n"
                            "9️⃣ Bake 12–15 minutes until cheese is melted and bubbly\n\n"
                            "🔟 Top with fresh cilantro immediately after removing from oven\n\n"
                            "**Pro tip:** A light drizzle of ranch dressing on top? *Chef's kiss* 💋",
                colour=0x8b4513,
                timestamp=datetime.now()
            ).set_author(
                name="PizzaBot",
                icon_url="https://www.jocooks.com/wp-content/uploads/2012/03/bbq-chicken-pizza-1-7.jpg"
            ).set_footer(text="You just leveled up your pizza game! 🔥"),
        }
        return embeds.get(self.recipe_name)


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
        app_commands.Choice(name="🌶️ BBQ Chicken", value="bbq_chicken"),
    ])
    async def recipes(self, interaction: discord.Interaction, pizza: app_commands.Choice[str]):
        selected = pizza.value
        view = RecipeView(selected)
        embed = view.get_notes_embed()
        await interaction.response.send_message(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(recipes(bot))