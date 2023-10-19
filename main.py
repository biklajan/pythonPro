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
    await ctx.send("Commands: heh, henPassword, howSave, degrad(plasick, glass),\nrepeat, hello, on_ready, joke")
    
@bot.command()
async def genPassword(ctx, times: int):
    password = ""
    for i in range(times):
        symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password = password + random.choice(symbol) 
    await ctx.send(password)
    

@bot.command()
async def howSave(ctx):
    await ctx.send(f'1.ЭКОНОМЬТЕ РЕСУРСЫ\n'
                     '2.РАЗДЕЛЯЙТЕ МУСОР\n'
                     '3.СДАВАЙТЕ ВТОРСЫРЬЁ\n'
                     '4.ВЫБИРАЙТЕ ЭКОЛОГИЧНЫЙ ТРАНСПОРТ\n'
                     '5.ИСПОЛЬЗУЙТЕ ПОВТОРНО И НЕ БЕРИТЕ ЛИШНЕЕ\n'
                     '6.ВНЕДРЯЙТЕ ЭКО-ПРИВЫЧКИ НА РАБОТЕ\n'
                     '7.ОБРАТИТЕ ВНИМАНИЕ НА ПИТАНИЕ\n'
                     '8.ПОСТАРАЙТЕСЬ ОТВЫКНУТЬ ОТ ПЛАСТИКА\n'
                )

@bot.command()
async def degrad(ctx, trash):
    dict = {"plastick": "Сдать пластик можно в «Перекресток»,\n"
            "«Карусель», «Ашан», «Мега» и др.\n"
            "\n"
            "ЧЕМ ОПАСЕН ПЛАСТИК ДЛЯ ОКРУЖАЮЩЕЙ СРЕДЫ?\n"
            "Основные опасения связаны с тем, что пластмассы, попадая в землю,\n"
            "распадаются на мелкие частицы и могут выбрасывать в окружающую среду\n"
            "химические вещества, добавленные в них при производстве.\n"
            "Это может быть хлор, различные химикаты, например токсичные или канцерогенные антивоспламенители.",
            
            "glass": "Стеклянные банки, бутылки можно сдать в экоцентры проектов\n"
            "«Сборка», «Собиратор» (принимают также стеклянную и хрустальную посуду),\n"
            "«Переработкинская» (берут и оконные стекла) и т. д.\n"
            "\n"
            "На первом месте оказались стеклянные бутылки, которые,\n"
            "по расчётам исследователей, способствует глобальному\n"
            "потеплению сильнее, чем пластиковая упаковка и алюминиевые банки.\n"
            "Как отмечают учёные, для их производства нужно больше ресурсов и энергии,\n"
            "а в процессе изготовления стекла выделяется много углекислого газа.\n"
            }
    await ctx.send(dict[trash])
    

bot.run("ТВОЙ ЛИЧНЫЙ ТОКЕН")
