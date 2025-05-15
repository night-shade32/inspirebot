import discord
import requests
import json
import random as ran


def get_meme():
    response = requests.get("https://api.realinspire.live/v1/quotes")
    json_data = json.loads(response.text)
    contents = [item["content"] for item in json_data["results"]]
    quote = ran.choice(contents)
    print(quote)
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
client.run(
    "MTM3MjQ5MDQ0NjA1OTYwNjA5Ng.GAFEtO.eoKqfNLnue7WmYDJx5jSoQ1sLN1w_Ih02z1b8c"
)  # Replace with your own token.
