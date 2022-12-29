# Author: Marcos Pereyra
# Github: MarkeZito3


import discord
from discord import app_commands
from discord.ext import commands

import os
import random
from tracemalloc import start
from dotenv import load_dotenv # Create a .env file
from urllib import parse, request
import re #regular expression 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #put here the discord token, duh

# bot = commands.Bot(command_prefix='f!') #prefijo del bot
bot = commands.Bot(command_prefix= "f!", intents = discord.Intents.default()) #prefijo del bot

# Define constants for the future:
ICON_URL = "https://openailabsprodscus.blob.core.windows.net/private/user-uMFoUHUSFwcwOl0cgqqdmfVf/generations/generation-ml0BEf53eeELFdKlRnHGjLvB/image.webp?st=2022-12-18T06%3A10%3A56Z&se=2022-12-18T08%3A08%3A56Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-18T02%3A26%3A47Z&ske=2022-12-25T02%3A26%3A47Z&sks=b&skv=2021-08-06&sig=8puyp6h01TWXSMxQfNNynJif75D0FdoUfTvHeGeQIVU%3D"
AUTHOR = "MarkeZito3"
FOOTER_MSG = "Bot created by MarkeZito3"

# Here I transform a file into a string list
f = open('outputfile', 'r')
if f.mode == 'r':
    contents = f.read().replace(" ","%20")
new_contents = contents.split("\n")

# this function is to send a random furry image in discord :D
@bot.tree.command(name="furry", description="make a random furry image")
async def furro(interaction: discord.Interaction):
    # await ctx.send(f"{ctx.author.name}")
    # print(ctx.author.name)
    # print(ctx.me)
    # await ctx.send(f"https://nal.one/img/{random.choice(new_contents)}.webp")

    embed = discord.Embed(title='Furry', description=f"{interaction.user.mention} ha traido un furrito OwO 👉👈", color=0x00ff00)
    embed.set_image(url=f"https://nal.one/img/{random.choice(new_contents)}.webp")
    embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)

    # Envía el embed al canal
    await interaction.response.send_message(embed=embed,ephemeral=False)


# this function is to send a random fox image in discord :D
@bot.tree.command(name="fox", description="Return an image of a fox")
async def fox(interaction: discord.Interaction):
    r_n_fox = random.randint(1,123)
    # await ctx.send(f"https://randomfox.ca/images/{r_n_fox}.jpg")

    embed = discord.Embed(title='Fox', description=f'{interaction.user.mention} ha generado una imagen random de un zorro', color=0x00ff00)
    embed.set_image(url=f"https://randomfox.ca/images/{r_n_fox}.jpg")
    # embed.add_field(name='Campo 2', value='Valor del campo 2', inline=False)
    embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)
    await interaction.response.send_message(embed=embed,ephemeral=False)

    # Envía el embed al canal

# I want to return the avatar of the user:
@bot.tree.command(name="avatar", description="Return the avatar of the user")
@app_commands.describe(mention = "Mention someone")
async def avatar(interaction: discord.Interaction,mention: str):
    
    try:
        mention = mention.replace('<','')
        mention = mention.replace('>','')
        mention = mention.replace('@','')
        user = await bot.fetch_user(mention)
        print(f"user: {user}")
        embed = discord.Embed(title='Avatar', description=f"{interaction.user.mention} quiere ver cómo es el avatar de {user.name}", color=0x0000ff)
        embed.set_image(url=user.avatar.url)
        embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)

        await interaction.response.send_message(embed=embed,ephemeral=False)
        

    except Exception as e:
        try:
            user = await bot.fetch_user(mention)
            print("user.url: ",user.avatar.url)
        except:
            pass
        print("==================================================")
        print("no se pudo recolectar el user :c")
        print(e)
        await interaction.response.send_message("no se pudo hacer lo querías hermanito :c, intenta de nuevo pero siguiendo las especificaciones :3",ephemeral=True)

@bot.tree.command(name="random", description="Fetch a random value from a list")
@app_commands.describe(lista = "listar elementos separados por comas ( , )")
async def rand(interaction: discord.Interaction,lista: str):
    try:
        lista = lista.split(",")
        random_args_from_random = random.choice(lista)
        # random_args_from_random = random_args_from_random.replace(",","")

        embed = discord.Embed(title='Random Choice', description=f'{interaction.user.mention} generate a random choice', color=0x00ff00)
        embed.add_field(name='and the winner is....', value=f'||{random_args_from_random}||', inline=False)
        embed.set_image(url="https://cdn.dribbble.com/users/6059148/screenshots/14425859/media/3f67e0e620f3818a68a03fdb874b7a56.gif")
        embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)
        await interaction.response.send_message(embed=embed)
        print("random function works :D")
    except:
        print("no se pudo mi rey :c")
        await interaction.response.send_message("no se pudo mi rey :c")

# @bot.command(name="youtube",description="This command fetch the first youtube search")
# async def youtube(ctx, *,search):
#     query_search = parse.urlencode({'search_query': search})
#     html_search = request.urlopen('http://www.youtube.com/results?'+query_search)
#     id_search = re.findall('\\/watch\\?v=(.{11})', html_search.read().decode()) # when the request fetch responses only extract the video ID
#     await ctx.send('https://www.youtube.com/watch?v='+id_search[0])

@bot.tree.command(name="jihyo", description='only work with the user: "Gambito"')
async def jihyo(interaction: discord.Interaction):
    if (interaction.user.id == 607039170472574999):
        embed = discord.Embed(title='Jihyo', description=f'Hola, soy la Jihyo, y tengo que confesar que amo a {interaction.user.mention} :hand_with_index_finger_and_thumb_crossed:', color=0xff8000)
        # embed.add_field(name='Hola gambito, soy la Jihyo.', inline=False)
        embed.set_image(url="https://www.nacionrex.com/__export/1617916652993/sites/debate/img/2021/04/08/twice-jihyo-una-de-las-mejores-lideres-grupos-k-pop-ranking_crop1617916587896.jpg_1902800913.jpg")
        embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)
        await interaction.response.send_message(embed=embed,ephemeral=False)
    else:
        embed = discord.Embed(title='Jihyo', description=f'{interaction.user.mention}, vos no sos Gambito!!! 😡', color=0xff0000)
        # embed.add_field(name='Hola gambito, soy la Jihyo.', inline=False)
        embed.set_image(url="https://pbs.twimg.com/media/FYlW-yOXgAAycTd.jpg:large")
        embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)
        await interaction.response.send_message(embed=embed,ephemeral=False)

# this event start when the script is executed
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='FurryBot OwO 🦊 | f!help for more information'))
    print('ready')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

bot.run(TOKEN)