import discord
from discord.ext import commands
import os
from discord.utils import get
import sqlite3
import requests
import responses
import aiohttp
from aiohttp import request
import time
import asyncio
from mojang import MojangAPI
import json
import urllib, json
import maya
from datetime import date
from random import choice
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re
import random
from random import choice








from discord.ext import commands
Bot = commands.Bot(command_prefix='--')
Bot.remove_command('help')








@Bot.command()
async def profile(ctx, *, message:str=None):


   uuid = MojangAPI.get_uuid(f"{message}")
   profile = MojangAPI.get_profile(uuid)
   people = requests.get('https://api.mojang.com/user/profiles/' + uuid + '/names' )
   people_json  = people.json()
   length = len(people_json)
   request = requests.get('https://api.namemc.com/profile/' + uuid + '/friends')
   friends  = request.json()
   lengtth = len(friends)

   friendss = ""
   names = ""
   daters = ""
   skin_url = f"https://mc-heads.net/download/{uuid}"

   number = 1
   info = people_json[int(length) - int(number)]["name"]
   embed = discord.Embed(title=f"Minecraft info about {info}", description="User information",
   color=discord.Color.blue())
   embed.set_footer(text=f"request by {ctx.author}", icon_url=ctx.author.avatar_url)


   nikchanged = int(length) - int(number)
   embed.add_field(name='Skin download' ,value='[Click here for download](' + skin_url + ')')
   embed.add_field(name='Information' ,value="nickname changed: " + str(nikchanged), inline=False)
   requesttt = requests.get(f'https://api.ashcon.app/mojang/v2/user/{uuid}')
   dater  = requesttt.json()
   daserts = dater["username_history"]
   num = 1
   numr = 0
   # test if  nicknames more than 1
   if length == num :
       firstnamess = "**1. **" + people_json[0]["name"]
       embed.add_field(name="Nicknames", value = firstnamess, inline=True)
       if lengtth == numr:
            embed.add_field(name="Friends", value = " 0 friends", inline=True) #add the field
            embed.set_thumbnail(url="https://visage.surgeplay.com/full/512/" + uuid + ".png")
            await ctx.send(embed=embed)

       else:
           for i in range(lengtth):
               friendss = friendss +"\n" + f"**{i + 1}.** " + friends[i]["name"]
           embed.add_field(name="Friends", value = friendss, inline=True) #add the field
           embed.set_thumbnail(url="https://visage.surgeplay.com/full/512/" + uuid + ".png")
           await ctx.send(embed=embed)

   else:
       for i in range(1, length):
           daters = ""
           daters = daters + dater["username_history"][i]["changed_at"]
           dt = maya.parse(daters).datetime()
           changed = dt.strftime(' %d.%m.%Y')
           today = date.today()
           first = today.strftime('%Y')
           second = dt.strftime('%Y')
           dateresult  = int(first) - int(second)
           names = names +"\n" + f"**{i + 1}.** " + people_json[i]["name"] +" |" + changed + "​⠀"
       firstname = "**1. **" + people_json[0]["name"]
       if lengtth == numr:
           embed.add_field(name="Nicknames", value =firstname + names, inline=True)
           embed.add_field(name="Friends", value = "0 Friends", inline=True) #add the field
           embed.set_thumbnail(url="https://visage.surgeplay.com/full/512/" + uuid + ".png")
           await ctx.send(embed=embed)
       else:
           for i in range(lengtth):
               friendss = friendss +"\n" + f"**{i + 1}.** " + friends[i]["name"]
           embed.add_field(name="Nicknames", value = firstname + names, inline=True)
           embed.add_field(name="Friends", value = friendss, inline=True) #add the field
           embed.set_thumbnail(url="https://visage.surgeplay.com/full/512/" + uuid + ".png")

           await ctx.send(embed=embed)
    

    
    
@Bot.command()
async def wallpaper(ctx, arg1):
    array = []
    intt = arg1

    len_link = f"https://wallpaperscraft.com/search/?query={intt}"
    len_response = requests.get(len_link).text
    len_soup = BeautifulSoup(len_response, 'lxml')
    len_block = len_soup.find('ul', class_ = "pager__list").find('li', class_ = "pager__item pager__item_last-page")
    images_link = len_block.find('a').get('href')

    str = images_link
    #search using regex
    numbers = re.findall('[0-9]+', images_link)

    ranger = int(numbers[0])
    ranger_result = ranger - 1

    np = random.randint(1, ranger_result)


    link = f'https://wallpaperscraft.com/search/?order=&page={np}&query={intt}&size=1920x1080'
    response = requests.get(link).text

    soup = BeautifulSoup(response, 'lxml')
    download_block = soup.find('div', class_ = "wallpapers wallpapers_zoom wallpapers_main").find_all('li', class_ = "wallpapers__item")
        # result_link = download_block.page_number.find('a').get('href')
    for imagerr in download_block:
        images_link = imagerr.find('a').get('href')
        array += [images_link]
        # img=random.choice(images_link)
    second_link = f"https://wallpaperscraft.com{choice(array)}"
    second_response = requests.get(second_link).text
    second_soup = BeautifulSoup(second_response, 'lxml')
    download_src = second_soup.find('div', class_ = "wallpaper__placeholder").find('img', class_ = "wallpaper__image").get('src')


    embed = discord.Embed(title=f"Обои на тему {arg1}", description=f"Надеюсь вам нравится подобранные обои", color=0x141414)
    embed.add_field(name='Open Image in Browser' ,value='[Click here to open](' + download_src + ')')
    embed.set_image(url=download_src)


    await ctx.send(embed=embed)    
    



token = os.environ.get('TOKEN')
Bot.run(token)
