import discord
import os
import dotenv

dotenv.load_dotenv()

token = os.getenv('TOKEN')
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'loggen in as {self.user}')
    async def on_message(self, message):
        print(f'message from {message.author}: message content {message.content}')

intents = discord.Intents.default()
intents = discord.Intents.all()
intents.message_content = True
client = MyClient(intents=intents)

client.run(token=token, log_handler=None)
