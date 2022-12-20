# Author: Marcos Pereyra
# Github: MarkeZito3


import os
from tracemalloc import start
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv # Create a .env file

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #put here the discord token, duh

bot = commands.Bot(command_prefix='f!') #prefijo del bot

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
@bot.command(name='furry', description='make a random furry image')
async def furro(ctx):
    # await ctx.send(f"{ctx.author.name}")
    print(ctx.author.name)
    print(ctx.me)
    # await ctx.send(f"https://nal.one/img/{random.choice(new_contents)}.webp")

    embed = discord.Embed(title='Furry', description=f"{ctx.author.name} ha traido un furrito OwO 👉👈", color=0x00ff00)
    embed.set_image(url=f"https://nal.one/img/{random.choice(new_contents)}.webp")
    embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)

    # Envía el embed al canal
    await ctx.send(embed=embed)


# this function is to send a random fox image in discord :D
@bot.command(name='fox', description='make a random fox image')
async def fox(ctx):
    r_n_fox = random.randint(1,123)
    # await ctx.send(f"https://randomfox.ca/images/{r_n_fox}.jpg")

    embed = discord.Embed(title='Fox', description=f'{ctx.author.name} ha generado una imagen random de un zorro', color=0x00ff00)
    embed.set_image(url=f"https://randomfox.ca/images/{r_n_fox}.jpg")
    # embed.add_field(name='Campo 2', value='Valor del campo 2', inline=False)
    embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)

    # Envía el embed al canal
    await ctx.send(embed=embed)

    print(ctx.message.mentions)
    print("--------------------------------")
    for men in ctx.message.mentions:
        print("message: ",men)
        print("\tid: ",men.id)
        print("\tname: ",men.name)
        print("\tdiscriminator: ",men.discriminator)
        print("\tbot: ",men.bot)
        print("\tguild: ",men.guild)
    print("--------------------------------")
    print(ctx.message.created_at)

# I want to return the avatar of the user:
@bot.command(name="avatar", description="Return the avatar of the user")
async def avatar(ctx):
    user = await bot.fetch_user(ctx.message.mentions[0].id)
    embed = discord.Embed(title='Avatar', description=f"{ctx.author.name} quiere ver cómo es el avatar de {user.name}", color=0x0000ff)
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)
    await ctx.send(embed=embed)

##################################################################

@bot.command(name="random", description="Fetch a random value from a list")
async def rand(ctx, *args):
    
    # Setup
    random_args_from_random = random.choice(args)
    random_args_from_random = random_args_from_random.replace(",","")

    embed = discord.Embed(title='Random Choice', description=f'{ctx.author.name} generate a random choice', color=0x00ff00)
    embed.add_field(name='and the winner is....', value=f'||{random_args_from_random}||', inline=False)
    embed.set_image(url="https://cdn.dribbble.com/users/6059148/screenshots/14425859/media/3f67e0e620f3818a68a03fdb874b7a56.gif")
    embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)
    await ctx.send(embed=embed)
    print("random function works :D")
##################################################################

# @bot.command(name="secret_msg", description="You'll watch a secret message 🤫")
# async def secret(ctx):
#     embed = discord.Embed(title='Secret Message', description=f'{ctx.author.name} has revealed the secret message', color=0x00ff00)
#     embed.set_image(file=discord.File("./Sin título-2.png"))
#     embed.set_footer(text=FOOTER_MSG, icon_url=ICON_URL)
#     await ctx.send(embed=embed)

# this event start when the script is executed
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='FurryBot OwO 🦊 | f!help for more information'))
    print('ready')


bot.run(TOKEN)