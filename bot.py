import discord
import requests
import json
import random as ran
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("DISCORD_TOKEN")


def get_meme():
    response = requests.get("https://api.realinspire.live/v1/quotes")
    json_data = json.loads(response.text)
    contents = [item["content"] for item in json_data["results"]]
    quote = ran.choice(contents)
    return quote


class MyClient(discord.Client):

    async def on_ready(self):

        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("$inspire"):
            await message.channel.send(get_meme())


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)  # Replace with your own token.
