import discord
import os
import time
import requests

import discord
import os
import time
import requests

from discord.ext import commands
from time import sleep

prefix = ('.')
client = commands.Bot(intents=discord.Intents.all(),command_prefix=prefix,help_command=None)
token = os.environ['token']


@client.event
async def on_connect():
  os.system('clear||cls')
  print(f'CONNECTED : {client.user}\nPREFIX : {prefix}\nCOMMANDS : {prefix}imagine <prompt>')
  return

@client.event
async def on_command_error(ctx,rror):
  return

# ...

@client.command()
async def imagine(ctx, *, prompt):
    imagine = prompt
    await ctx.send(f'{ctx.author.mention} **Generating your image on the prompt:** {imagine}')
    url = f"https://image.pollinations.ai/prompt/{imagine}"
    response = requests.get(url)
    
    if response.status_code == 200:
       
        image_path = "temp_image.png"
        with open(image_path, 'wb') as file:
            file.write(response.content)

       
        file = discord.File(image_path, filename="image.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)
        embed.set_author("Imagine to Image | Unlimited Uses")
        embed.set_footer(text='Coded by Ghost Planet')
        os.remove(image_path)
    else:
        await ctx.send("Failed to generate the image.")


client.run(token)
