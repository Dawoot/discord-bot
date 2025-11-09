import discord
import os
from discord.ext import commands
import dotenv
import logging

handler = logging.FileHandler(filename='KPS-bot2025.log', encoding= 'utf-8', mode='w')

dotenv.load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=',',  intents=intents)

@bot.event
async def on_ready():
    assert bot.user is not None
    print(f'Logged in as {bot.user} with id {bot.user.id}')
    print('------------')


@bot.command()
async def testing(ctx, message:str):
    if message is not None:
        await ctx.send(f'Why did you send {message}')
    if message is None:
        await ctx.send('Dude you need to write something too')


@bot.command()
async def points(ctx, pref:str, amount:int):
    if pref == '+':
        await ctx.send(f'So you want to add points?? huh interesting {amount} to be specific?')
    if pref == '-':
        await ctx.send(f'So you want to remove points?? huh interesting {amount} to be specific')

#ignore error here, it works if you have the .env file
bot.run(token=token, log_handler=handler)
