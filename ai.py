from openrouter import OpenRouter
import os
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

message = input("You: ")

with OpenRouter(api_key=OPENROUTER_API_KEY) as client:
    response = client.chat.send(
        model=OPENROUTER_MODEL,
        messages=[{"role": "user", "content": message}]
    )
reply = response.choices[0]
print("AI:", reply)


# @tree.command(
#     name="ai",
#     description="Test the AI response",
#     guild=discord.Object(id=1452508670532391024)
# )
# async def say(interaction: discord.Interaction, message: str):
#     with OpenRouter(api_key="OPENROUTER_API_KEY") as client:
#         response = client.chat.send(
#             model="OPENROUTER_MODEL",
#             messages=[{"role": "user", "content": message}]
#         )
#     reply = response.choices[0].message.content
#     await interaction.response.send_message(reply)

# discord ai bot command example, should work but its all theory. needs to be pasted into index.js file