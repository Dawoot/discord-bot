import discord
import os
import sqlite3
from sqlite3 import Error
from discord.ext import commands
import dotenv
import logging

handler = logging.FileHandler(filename='KPS-bot2025.log', encoding= 'utf-8', mode='w')

dotenv.load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
#TODO: FIXA POÄNGEN FÖR EN GÅNGS SKULL!!!!



bot = commands.Bot(command_prefix=',',  intents=intents)
connection = None
try:
    connection = sqlite3.connect('discord.db')
    print('Success connecting to the db and connecting the cursor')
except Error as e:
    print(f'the error {e} has occured')

cursor = connection.cursor()

create_table = """CREATE TABLE IF NOT EXISTS
scores(user_id INTEGER PRIMARY KEY, score DOUBLE)"""


cursor.execute(create_table)


@bot.event
async def on_ready():
    assert bot.user is not None
    print(f'Logged in as {bot.user} with id {bot.user.id}')
    print('------------')
    members = bot.get_all_members()
    for member in members:
        cursor.execute(f"INSERT INTO scores VALUES ({member.id}, 0)")
    print('Success!!!!?')
    cursor.execute('SELECT * FROM scores')
    results = cursor.fetchall()
    print(results)
@bot.command()
async def testing(ctx, message:str):
    if message is not None:
        await ctx.send(f'Why did you send {message}')
    if message is None:
        await ctx.send('Dude you need to write something too')


@bot.command()
async def points(ctx, pref:str, amount:float, user:discord.User):
    if pref == '+':
        id = user.id
        read_score = f"""SELECT score FROM scores WHERE user_id ={id}"""
        cursor.execute(read_score)
        result = cursor.fetchone()
        new_score = result[0] + amount
        cursor.execute(f"Update scores set score = {new_score} where user_id = {id}")
        
        await ctx.send(f'added {amount} to {user} !!!!')
    if pref == '-':
        id = user.id
        read_score = f"""SELECT score FROM scores WHERE user_id ={id}"""
        cursor.execute(read_score)
        result = cursor.fetchone()
        new_score = result[0] + amount
        cursor.execute(f"Update scores set score = {new_score} where user_id = {id}")
        
        await ctx.send(f'removed{amount} from {user} sadface :/ ')

#ignore error here, it works if you have the .env file
bot.run(token=token, log_handler=handler)
connection.commit()
connection.close()
