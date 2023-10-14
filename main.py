
import discord
from discord.ext import commands
import os
import random
from random import choice

print(os.listdir('python/images'))
intents = discord.Intents.default()
intents.message_content = True
symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
mem_h = ["C:\\Users\\mgasanov\\Desktop\\KODLAND WEB PRO\\python\\images\\mem1.jpg", "C:\\Users\\mgasanov\\Desktop\\KODLAND WEB PRO\\python\\images\\mem2.jpg", "C:\\Users\\mgasanov\\Desktop\\KODLAND WEB PRO\\python\\images\\mem3.jpg"]

joke_book = "— Как отличить съедобные грибы от несъедобных?— С помощью будильника. Если ты съел грибы и утром услышал будильник, значит, они были съедобные."
bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def joke(ctx):
    await ctx.send(joke_book)

@bot.command()
async def mem(ctx):
    img = random.choice(mem_h)
    with open(f'{img}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def help(ctx):
    await ctx.send("Commands: heh, repeat, hello, on_ready, joke")
    
@bot.command()
async def genPassword(ctx, times: int):
    password = ""
    for i in range(times):
        symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password = password + random.choice(symbol)
    await ctx.send(password)
    

bot.run("MTE1NTE2NTU2Njc5ODE0NzcwNQ.GqcJFf.x2JRLNQleJx_mlkoq740CVvAdFHVQAWkFu2fTw")
