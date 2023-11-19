# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # Check if this bot was @'d in the message.
        if self.user in message.mentions:
            await message.channel.send("Someone @'d me...")




intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')