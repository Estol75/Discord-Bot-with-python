import discord
from discord.ext import commands
import os
from discord.utils import get
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
import fake_useragent

from discord.ext import commands
import pymongo
from pymongo import MongoClient


user = fake_useragent.UserAgent().random
header = {'user-agent': user}



intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)
from discord.ext import commands

Bot = commands.Bot(command_prefix='q.', intents=intents)
Bot.remove_command('help')

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name="q.help v1.0.89"))


mongo = os.environ.get('MONGO')
cluster = MongoClient(mongo)

db = cluster["discord"]
collection = db["data"]

@Bot.event
async def on_guild_join(guild):
    guild_id = str(guild.id)
    serverid = guild_id
    serveride = f"{serverid}"

    # PASS = os.environ.get('PASSW')


    db = cluster["discord"]
    collection = db["data"]

    post = {"_id": serveride, "name": "en"}

    collection.insert_one(post)


@Bot.command()
@commands.has_permissions(administrator = True)
async def set_lang(ctx, arg1):
    guild_id = str(ctx.guild.id)
    serverid = guild_id
    serveride = f"{serverid}"
    result = collection.update_one({"_id": serveride}, {"$set": {"name": arg1}})


@Bot.command()
async def lang(ctx):
    guild_id = str(ctx.guild.id)
    serverid = guild_id
    serveride = f"{serverid}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]




data = {}

@Bot.command()
@commands.has_permissions(administrator = True)
async def welcome_channel(ctx, arg1):
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]
    with open('data.json', 'r') as f:
        data = json.load(f)
        guild_id = ctx.author.id
        serverid = guild_id
        serveride = f"{serverid}"
        data[serveride] = []
        data[serveride].append({
            'name': arg1,
        })

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
    if numin == "ru":
        await ctx.send(f"Вы добавляете приветственное сообщение в {arg1} канал")
    else:
        await ctx.send(f"you add welcome message to {arg1} channel")



@Bot.event
async def on_member_join(member):
    #check language
    serveride = f"{member.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]
    #command

    serverid = member.guild.id
    serveride = f"{serverid}"
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
    for p in data[serveride]:
        numin = p['name']
        print(numin)


    if numin == "ru":
        embed = discord.Embed(title=f"Добро пожаловать на {member.guild.name} сервер.⠀​⠀​⠀⠀​⠀​⠀⠀​⠀​⠀⠀​⠀​⠀", description=f"приветствую тебя, {member.mention}⠀⠀​​", color=0x00eeff)
        embed.set_image(url="https://t4.ftcdn.net/jpg/03/64/94/67/360_F_364946785_HU0G0WLRpd9SjBxecLAy7En93HmdxbL5.jpg")
        embed.add_field(name="**У нас на сервере приветствую прекрасны бот**", value="для просмотра команд`--commands`", inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        channel = discord.utils.get(member.guild.channels, name = numin)
        await channel.send(embed=embed)
    else:
        embed = discord.Embed(title=f"Welcome to the {member.guild.name} server.⠀​⠀​⠀⠀​⠀​⠀⠀​⠀​⠀⠀​⠀​⠀", description=f"Welcome to server, {member.mention}⠀⠀​​", color=0x00eeff)
        embed.set_image(url="https://t4.ftcdn.net/jpg/03/64/94/67/360_F_364946785_HU0G0WLRpd9SjBxecLAy7En93HmdxbL5.jpg")
        embed.add_field(name="**We have amazing bot**", value="To view commands `--commands`", inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        channel = discord.utils.get(member.guild.channels, name = numin)
        await channel.send(embed=embed)

@Bot.command()
async def sex(ctx, member: discord.Member):
    img = [
        "https://wetgif.com/wp-content/uploads/gif-hentai-incest-19-1.gif",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4q5Q1GC9L9LZG-28yP7uIIa_mK5qdgmN1qgdPRvwnzvERlOc&s",
        "https://www.eroticaingif.com/upload/2019/01/12/20190112041432-babece34.gif",
        "https://cdn.xxxhentaipics.com/images/533/files/f040e159526459ceab32e7322beba486/gif-hentai-gifs_0.gif",
        "https://lh3.googleusercontent.com/proxy/MsWv7sK3KDewBjIG4JdTHyfC-5H-PV57QoTthW-_-B6_2MGuhynlsXZE_gk4oBTM6MocES2VkDTJaMPaSodoIR9vZ1gVALSmSg",
        "https://cdn.xxxhentaipics.com/images/533/files/f040e159526459ceab32e7322beba486/gif-hentai-gifs_0.gif",
        "https://cdn.hentaihand.com/assets/images/531302/4.gif",
        "http://i.redd.it/k37eby6s0q641.gif",
        "https://www.xxx-3d.com/thumb/176/769_rose.jpg",
        "https://thehentaigif.com/wp-content/uploads/2020/10/22688886-81.gif",
        "https://lh3.googleusercontent.com/proxy/cdnBWyXQkGbDzbMj9zzwoy5uaC_FXeY3ZZDLjRIAS2Wgp06fskzjQEro6bAbXE-kG-LHABqiVrLwBI-M-OZswi0napnpi2XCuZDClgEQXkvfw12Pz7-ze6CPOXBs9_UdmyUsp27Iz0F3",
        "https://static.hentai-gif-anime.com/upload/20200717/76/153902/detail.gif",
        "https://i0.wp.com/uncensored-hentai.top/wp-content/uploads/2020/07/my-hero-academia-9.gif?ssl=1",
        "http://i.redd.it/0f80ek7tis851.gif",


    ]
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
    #command
    if numin == "ru":
        num = random.randint(0,14)
        embed = discord.Embed(title=f"{ctx.author.name} шрекнул(ся) с {member.name}⠀", description=f":heart: :heart: :heart:  ", color=0x00eeff)

        embed.set_image(url=img[num])
        await ctx.send(embed = embed)
    else:
        num = random.randint(0,23)
        embed = discord.Embed(title=f"{ctx.author.name} sex {member.name}⠀", description=f":heart: :heart: :heart:  ", color=0x00eeff)

        embed.set_image(url=img[num])
        await ctx.send(embed = embed)

@Bot.command()
async def bot_status(ctx):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
    #command
    servers = len(Bot.guilds)
    ping_ = Bot.latency
    ping =  round(ping_ * 1000)
    if numin == "ru":
        await ctx.send(f"число серверов {servers}, мой пинг{ping} мс")
    else:
        await ctx.send(f"Server count {servers}, My ping is {ping} ms")

@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name = '❗-писать-тут')
    msg = f"{member.mention} leave discord server "
    await channel.send(msg)



@Bot.command()
async def user_agent(ctx):
    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}
    await ctx.send(header)



@Bot.command()
async def invite(ctx):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
    #command
    if numin == "ru":
        embed = discord.Embed(title = "Приглашения бота QBug ", description="")
        invite_link = "https://discord.com/api/oauth2/authorize?client_id=698494567007387689&permissions=8&scope=bot"
        embed.add_field(name= ":incoming_envelope: ссылка на приглашение", value='[нажми на меня для приглашения](' + invite_link + ')', inline = False)
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title = "Discord Bot QBug Invite ", description="")
        invite_link = "https://discord.com/api/oauth2/authorize?client_id=698494567007387689&permissions=8&scope=bot"
        embed.add_field(name= ":incoming_envelope: Invite link", value='[Click here to invite](' + invite_link + ')', inline = False)
        await ctx.send(embed = embed)





@Bot.command()
async def profile(ctx, *, message:str=None):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]

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
    if numin == "en":
        #start up
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

    #last
    if numin == "ru":
        embed = discord.Embed(title=f"Майнкрафт профиль {info}", description="Информация о пользователе",
        color=discord.Color.blue())
        embed.set_footer(text=f"запрос сделан {ctx.author}", icon_url=ctx.author.avatar_url)


        nikchanged = int(length) - int(number)
        embed.add_field(name='скачать скин' ,value='[нажми на меня для скачивания](' + skin_url + ')')
        embed.add_field(name='информация' ,value="никнейм изменён: " + str(nikchanged) +" раз(а)", inline=False)
        requesttt = requests.get(f'https://api.ashcon.app/mojang/v2/user/{uuid}')
        dater  = requesttt.json()
        daserts = dater["username_history"]
        num = 1
        numr = 0
        # test if  nicknames more than 1
        if length == num :
           firstnamess = "**1. **" + people_json[0]["name"]
           embed.add_field(name="никнеймы", value = firstnamess, inline=True)
           if lengtth == numr:
                embed.add_field(name="друзья/подружки", value = " 0 друзей", inline=True) #add the field
                embed.set_thumbnail(url="https://visage.surgeplay.com/full/512/" + uuid + ".png")
                await ctx.send(embed=embed)

           else:
               for i in range(lengtth):
                   friendss = friendss +"\n" + f"**{i + 1}.** " + friends[i]["name"]
               embed.add_field(name="друзья/подружки", value = friendss, inline=True) #add the field
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
               embed.add_field(name="Никнеймы", value =firstname + names, inline=True)
               embed.add_field(name="друзья/подружки", value = "0 друзья", inline=True) #add the field
               embed.set_thumbnail(url="https://visage.surgeplay.com/full/512/" + uuid + ".png")
               await ctx.send(embed=embed)
           else:
               for i in range(lengtth):
                   friendss = friendss +"\n" + f"**{i + 1}.** " + friends[i]["name"]
               embed.add_field(name="Никнеймы", value = firstname + names, inline=True)
               embed.add_field(name="друзья/подружки", value = friendss, inline=True) #add the field
               embed.set_thumbnail(url="https://visage.surgeplay.com/full/512/" + uuid + ".png")

               await ctx.send(embed=embed)


@Bot.command()
async def kiss(ctx, member: discord.Member):
    img = [
        "https://i.imgur.com/i1PIph3.gif",
        "https://i.imgur.com/WVSwvm6.gif",
        "https://i.imgur.com/sZhtvBR.gif",
        "https://i.imgur.com/So3TIVK.gif",
        "https://i.imgur.com/q340AoA.gif",
        "https://i.imgur.com/o9MMMeW.gif",
        "https://i.imgur.com/OjTBV8G.gif",
        "https://i.imgur.com/SeCRpPp.gif",
        "https://i.imgur.com/LRPJt19.gif",
        "https://i.imgur.com/9R4XQIv.gif",
        "https://i.imgur.com/FVlX0Vs.gif",
        "https://i.imgur.com/9758cJX.gif",
        "https://i.imgur.com/b3KBV8i.gif",
        "https://i.imgur.com/YLkDu7a.gif",

        "https://i.imgur.com/AOpGwmX.gif",
        "https://i.imgur.com/hwrhrWZ.gif",
        "https://i.imgur.com/KAmjoLO.gif",
        "https://i.imgur.com/yP3W3pH.gif",
        "https://i.imgur.com/SS7sQpj.gif",
        "https://i.imgur.com/ltDNY6b.gif",
        "https://i.imgur.com/THyefKo.gif",
        "https://i.imgur.com/QETjUCT.gif",
        "https://i.imgur.com/L0ujw2R.gif"


    ]
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
    #command
    if numin == "ru":
        num = random.randint(0,23)
        embed = discord.Embed(title=f"{ctx.author.name} поцеловал(а) {member.name}⠀", description=f":heart: :heart: :heart:  ", color=0x00eeff)

        embed.set_image(url=img[num])
        await ctx.send(embed = embed)
    else:
        num = random.randint(0,23)
        embed = discord.Embed(title=f"{ctx.author.name} kiss {member.name}⠀", description=f":heart: :heart: :heart:  ", color=0x00eeff)

        embed.set_image(url=img[num])
        await ctx.send(embed = embed)


@Bot.command()
async def windows10(ctx):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command

    if numin == "ru":
        embed = discord.Embed(title=f"Windows 10 Темы 1/5", description=f"сделай свой виндовс лучше", color=0x4e4759)
        download_src = "https://www.youtube.com/watch?v=wzpjnFQ030M&ab_channel=LinkVegasLinkVegas"
        embed.add_field(name='Туториал' ,value='[нажми на меня чтобы открыть видео](' + download_src + ')', inline = False)
        embed.set_image(url="http://i3.ytimg.com/vi/wzpjnFQ030M/maxresdefault.jpg")


        page2 = discord.Embed(title=f"Windows 10 Темы 2/5", description=f"сделай свой виндовс лучше", color=0xab55a9)
        page_img = "https://www.youtube.com/watch?v=DRyGOkD9ouU&ab_channel=LinkVegasLinkVegas"
        page2.add_field(name='Туториал' ,value='[нажми на меня чтобы открыть видео](' + page_img + ')', inline = False)
        page2.set_image(url="https://img.youtube.com/vi/DRyGOkD9ouU/maxresdefault.jpg")

        page3 = discord.Embed(title=f"Windows 10 Темы 3/5", description=f"сделай свой виндовс лучше", color=0x457573)
        page_imfg = "https://www.youtube.com/watch?v=4tvwEISJryY&ab_channel=TanjimTheTechGuyTanjimTheTechGuyBest%C3%A4tigt"
        page3.add_field(name='Туториал' ,value='[нажми на меня чтобы открыть видео](' + page_imfg + ')', inline = False)
        page3.set_image(url="https://img.youtube.com/vi/4tvwEISJryY/maxresdefault.jpg")

        page4 = discord.Embed(title=f"Windows 10 Темы 4/5", description=f"сделай свой виндовс лучше", color=0xe09346)
        page_imfsg = "https://www.youtube.com/watch?v=StnfG80ZvXY&ab_channel=TanjimTheTechGuyTanjimTheTechGuyBest%C3%A4tigt"
        page4.add_field(name='Туториал' ,value='[нажми на меня чтобы открыть видео](' + page_imfsg + ')', inline = False)
        page4.set_image(url="https://img.youtube.com/vi/StnfG80ZvXY/maxresdefault.jpg")

        page5 = discord.Embed(title=f"Windows 10 Темы 5/5", description=f"сделай свой виндовс лучше", color=0x2e3b7d)
        pagse_imfsg = "https://www.youtube.com/watch?v=_xSSbLQ_-0A&ab_channel=ViralHattrixViralHattrix"
        page5.add_field(name='Туториал' ,value='[нажми на меня чтобы открыть видео](' + pagse_imfsg + ')', inline = False)
        page5.set_image(url="https://img.youtube.com/vi/_xSSbLQ_-0A/maxresdefault.jpg")
    else:

        embed = discord.Embed(title=f"Windows 10 Theme 1/5", description=f"Make your Windows better", color=0x4e4759)
        download_src = "https://www.youtube.com/watch?v=wzpjnFQ030M&ab_channel=LinkVegasLinkVegas"
        embed.add_field(name='Tutorial' ,value='[Click here to open YT video](' + download_src + ')', inline = False)
        embed.set_image(url="http://i3.ytimg.com/vi/wzpjnFQ030M/maxresdefault.jpg")


        page2 = discord.Embed(title=f"Windows 10 Theme 2/5", description=f"Make your Windows better", color=0xab55a9)
        page_img = "https://www.youtube.com/watch?v=DRyGOkD9ouU&ab_channel=LinkVegasLinkVegas"
        page2.add_field(name='Tutorial' ,value='[Click here to open YT video](' + page_img + ')', inline = False)
        page2.set_image(url="https://img.youtube.com/vi/DRyGOkD9ouU/maxresdefault.jpg")

        page3 = discord.Embed(title=f"Windows 10 Theme 3/5", description=f"Make your Windows better", color=0x457573)
        page_imfg = "https://www.youtube.com/watch?v=4tvwEISJryY&ab_channel=TanjimTheTechGuyTanjimTheTechGuyBest%C3%A4tigt"
        page3.add_field(name='Tutorial' ,value='[Click here to open YT video](' + page_imfg + ')', inline = False)
        page3.set_image(url="https://img.youtube.com/vi/4tvwEISJryY/maxresdefault.jpg")

        page4 = discord.Embed(title=f"Windows 10 Theme 4/5", description=f"Make your Windows better", color=0xe09346)
        page_imfsg = "https://www.youtube.com/watch?v=StnfG80ZvXY&ab_channel=TanjimTheTechGuyTanjimTheTechGuyBest%C3%A4tigt"
        page4.add_field(name='Tutorial' ,value='[Click here to open YT video](' + page_imfsg + ')', inline = False)
        page4.set_image(url="https://img.youtube.com/vi/StnfG80ZvXY/maxresdefault.jpg")

        page5 = discord.Embed(title=f"Windows 10 Theme 5/5", description=f"Make your Windows better", color=0x2e3b7d)
        pagse_imfsg = "https://www.youtube.com/watch?v=_xSSbLQ_-0A&ab_channel=ViralHattrixViralHattrix"
        page5.add_field(name='Tutorial' ,value='[Click here to open YT video](' + pagse_imfsg + ')', inline = False)
        page5.set_image(url="https://img.youtube.com/vi/_xSSbLQ_-0A/maxresdefault.jpg")

    pages = [embed, page2, page3, page4, page5]

    message = await ctx.send(embed = embed)
    await message.add_reaction('⏮')
    await message.add_reaction('◀️')
    await message.add_reaction('▶️')
    await message.add_reaction('⏭')
    msgtr = message.id



    def check(reaction, user):
            if reaction.message != message:
                return False
                # SOLUTION: Checks if the message reacted on is the same as the one the bot sent

            return user == ctx.author and str(reaction.emoji) in ["⏮","◀️","▶️","⏭"]

    i = 0
    reaction = None
    times = 0
    while True:
        try:
            reaction, user = await Bot.wait_for('reaction_add', check=check)
            if str(reaction) == '⏮':
                i = 0
                await message.edit(embed = pages[i])
                await message.remove_reaction(reaction, user)
            elif str(reaction) == '◀️':
                if i > 0:
                    i -= 1
                    await message.edit(embed = pages[i])
                    await message.remove_reaction(reaction, user)
            elif str(reaction) == '▶️':
                if i < 4:
                    i += 1
                    await message.edit(embed = pages[i])
                    await message.remove_reaction(reaction, user)
            elif str(reaction) == '⏭':
                i = 4
                await message.edit(embed = pages[i])
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x seconds

@Bot.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    member_count = ctx.guild.member_count
    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    membercount = str(ctx.guild.member_count)
    roles = str(ctx.guild.roles)
    icon = str(ctx.guild.icon_url)
    server_createt = str(ctx.guild.created_at.strftime("%d.%m.%Y"))
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command
    if numin == "ru":
        embed = discord.Embed(title = " информация о сервере " + name , description=description)
        embed.set_thumbnail(url=icon)
        embed.add_field(name= ":crown: владелец сервера", value=owner, inline = False)
        embed.add_field(name= ":earth_americas: Регион", value=region, inline = False)
        embed.add_field(name= ":busts_in_silhouette: число участников", value=membercount, inline = False)

        embed.add_field(name= ":construction_site: сервер создан", value=server_createt, inline = False)
        embed.set_footer(text=f"запрос сделан {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title = name + "Server Information " + name, description=description)
        embed.set_thumbnail(url=icon)
        embed.add_field(name= ":crown: Owner", value=owner, inline = False)
        embed.add_field(name= ":earth_americas: Region", value=region, inline = False)
        embed.add_field(name= ":busts_in_silhouette: Member Count", value=membercount, inline = False)

        embed.add_field(name= ":construction_site: Server Createt", value=server_createt, inline = False)
        embed.set_footer(text=f"request by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


@Bot.command(aliases = ['wallpaper', 'обои'])
async def __wallpaper(ctx, arg1):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command

    if arg1 == "help":
        if numin == "ru":
            embed = discord.Embed(title=f"Информационный блок о обоях ", description=f"", color=0x7d87f5)
            embed.add_field(name='Популярные обои' , value='3D, Abstract, Animals, Anime, Art, Black \n Cars, City, Dark, Fantasy, Flowers, Food \n Holidays, Love, Macro, Nature, Space, Vector', inline = False)
            embed.add_field(name='Запросить картинку' , value='--wallpaper `<имя>`')
            embed.set_footer(text=f"запрос сделан {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:

            embed = discord.Embed(title=f"Wallpapers information block ", description=f"", color=0x7d87f5)
            embed.add_field(name='frequent wallpapers' , value='3D, Abstract, Animals, Anime, Art, Black \n Cars, City, Dark, Fantasy, Flowers, Food \n Holidays, Love, Macro, Nature, Space, Vector', inline = False)
            embed.add_field(name='picture request' , value='--wallpaper `<имя>`')
            embed.set_footer(text=f"request has done by {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        array = []
        intt = arg1

        len_link = f"https://wallpaperscraft.com/search/?query={intt}"
        len_response = requests.get(len_link).text
        len_soup = BeautifulSoup(len_response, 'lxml')
        len_block = len_soup.find('ul', class_ = "pager__list").find('li', class_ = "pager__item pager__item_last-page")
        images_link = len_block.find('a').get('href')

        #search using regex
        numbers = re.findall('[0-9]+', images_link)

        ranger = int(numbers[0])
        ranger_result = ranger - 1
        if ranger_result == 0:
            ranger_result + int(2)
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

        if numin == "ru":
            idsr = discord.Embed(title=f"Обои на тему {arg1}", description=f"Нажми на реакцию для переключения картинки ▶", color=0x141414)
            idsr.add_field(name='Открыть обои в браузере' ,value='[Нажми чтобы открыть](' + download_src + ')')
            idsr.set_image(url=download_src)

        else:
            idsr = discord.Embed(title=f"Wallpaper about {arg1}", description=f"Click on the reaction below to scroll to the next picture ▶", color=0x141414)
            idsr.add_field(name='Open Image in Browser' ,value='[Click here to open](' + download_src + ')')
            idsr.set_image(url=download_src)
        message = await ctx.send(embed = idsr)
        await message.add_reaction('▶')
        await message.add_reaction('❌')

        def check(reaction, user):
                if reaction.message != message:
                    return False
                    # SOLUTION: Checks if the message reacted on is the same as the one the bot sent

                return user == ctx.author and str(reaction.emoji) in ["▶", "❌"]
        i = 0
        reaction = None

        while True:
            if str(reaction) == '▶':
                array = []
                intt = arg1

                len_link = f"https://wallpaperscraft.com/search/?query={intt}"
                len_response = requests.get(len_link).text
                len_soup = BeautifulSoup(len_response, 'lxml')
                len_block = len_soup.find('ul', class_ = "pager__list").find('li', class_ = "pager__item pager__item_last-page")
                images_link = len_block.find('a').get('href')

                #search using regex
                numbers = re.findall('[0-9]+', images_link)

                ranger = int(numbers[0])
                ranger_result = ranger - 1
                if ranger_result == 0:
                    ranger_result + int(2)
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


            if numin == "ru":
                idsr = discord.Embed(title=f"Обои на тему {arg1}", description=f"Нажми на реакцию для переключения картинки ▶", color=0x141414)
                idsr.add_field(name='Открыть обои в браузере' ,value='[Нажми чтобы открыть](' + download_src + ')')
                idsr.set_image(url=download_src)
                await message.edit(embed = idsr)

            else:
                idsr = discord.Embed(title=f"Wallpaper about {arg1}", description=f"Click on the reaction below to scroll to the next picture ▶", color=0x141414)
                idsr.add_field(name='Open Image in Browser' ,value='[Click here to open](' + download_src + ')')
                idsr.set_image(url=download_src)
                await message.edit(embed = idsr)

            if str(reaction) == '❌':
                msggsss = await ctx.fetch_message(msg)
                await msggsss.delete()
            try:

                reaction, user = await Bot.wait_for('reaction_add', check = check)
                await message.remove_reaction(reaction, user)
            except:
                break




@Bot.command()
async def anime(ctx, *args):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command

    slot = '{}'.format('+'.join(args))

    arraysst = []

    lenter_link = f"http://anime.reactor.cc/search/{slot}"
    print( lenter_link)
    lenter_response = requests.get(lenter_link).text
    lenter_soup = BeautifulSoup(lenter_response, 'lxml')
    lenter_block = lenter_soup.find('div', class_ = "pagination_expanded").find_all('a')

    for imgrt in lenter_block:
        imgsftr = imgrt.text
        arraysst += [imgsftr]

    numbr = len(arraysst)

    numbrfdf =  numbr - int(1)

    imaperter_lent = arraysst[numbrfdf]



    array = []
    nps = random.randint(1, int(imaperter_lent))
    len_link = f"http://anime.reactor.cc/search/{slot}/{nps}"

    len_response = requests.get(len_link).text
    len_soup = BeautifulSoup(len_response, 'lxml')
    len_block = len_soup.find('div', id = "contentinner").find('div', id = "post_list")
    images_link = len_block.find_all('div', class_ = 'image')

    for imagerr in images_link:
        images_linkss = imagerr.find('img').get("src")
        array += [images_linkss]
    img_pictur_url = choice(array)

    if numin == "ru":
        idsr = discord.Embed(title=f"Обои на тему Аниме", description=f"Нажми на реакцию для переключения картинки ▶", color=0x141414)
        idsr.add_field(name='Открыть обои в браузере' ,value='[Нажми чтобы открыть](' + img_pictur_url + ')')
        idsr.set_image(url=img_pictur_url)

    else:
        idsr = discord.Embed(title=f"Wallpaper Anime", description=f"Click on the reaction below to scroll to the next picture ", color=0x141414)
        idsr.add_field(name='Open Image in Browser' ,value='[Click here to open](' + img_pictur_url + ')')
        idsr.set_image(url=img_pictur_url)
    message = await ctx.send(embed=idsr)
    await message.add_reaction('▶')
    await message.add_reaction('❌')
    msg = message.id
    print(msg)



    def check(reaction, user):
            if reaction.message != message:
                return False
                # SOLUTION: Checks if the message reacted on is the same as the one the bot sent

            return user == ctx.author and str(reaction.emoji) in ["▶", "❌"]
    i = 0
    reaction = None

    while True:
        if str(reaction) == '▶':
            i = 0
            arrays = []

            nps = random.randint(1, int(imaperter_lent))
            len_link = f"http://anime.reactor.cc/search/{slot}/{nps}"
            len_response = requests.get(len_link).text
            len_soup = BeautifulSoup(len_response, 'lxml')
            len_block = len_soup.find('div', id = "contentinner").find('div', id = "post_list")
            images_link = len_block.find_all('div', class_ = 'image')

            for imagerr in images_link:
                    images_linksss = imagerr.find('img').get("src")
                    arrays += [images_linksss]

            img_pictur_url = choice(arrays)
            print(img_pictur_url)
            if numin == "ru":
                idsrs = discord.Embed(title=f"Обои на тему Аниме", description=f"Нажми на реакцию для переключения картинки ▶", color=0x141414)
                idsrs.add_field(name='Открыть обои в браузере' ,value='[Нажми чтобы открыть](' + img_pictur_url + ')')
                idsrs.set_image(url=img_pictur_url)
                await message.edit(embed = idsrs)
            else:
                idsrs = discord.Embed(title=f"Wallpaper Anime", description=f"Click on the reaction below to scroll to the next picture ", color=0x141414)
                idsrs.add_field(name='Open Image in Browser' ,value='[Click here to open](' + img_pictur_url + ')')
                idsrs.set_image(url=img_pictur_url)
                await message.edit(embed = idsrs)

        if str(reaction) == '❌':
            msggsss = await ctx.fetch_message(msg)
            await msggsss.delete()
        try:

            reaction, user = await Bot.wait_for('reaction_add', check = check)
            await message.remove_reaction(reaction, user)
        except:
            break


@Bot.command()
async def anime_help(ctx):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command
    if numin == "ru":
        embed = discord.Embed(title="Аниме информация", description="Популярные теги​", color=0xffc800)
        embed.add_field(name="**Популярные теги **", value="`boobs`,`ass`, `ero`, `Kyonyuu`, `Pussy`, `Megane`, `bdsm`", inline=False)
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title="Anime help", description="Popular tags​", color=0xffc800)
        embed.add_field(name="**popular anime tags **", value="`boobs`,`ass`, `ero`, `Kyonyuu`, `Pussy`, `Megane`, `bdsm`", inline=False)
        await ctx.send(embed = embed)
@Bot.command()
async def animes(ctx):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command
    array = []
    np = random.randint(1, 3000)
    len_link = f"http://anime.reactor.cc/{np}"
    len_response = requests.get(len_link).text
    len_soup = BeautifulSoup(len_response, 'lxml')
    len_block = len_soup.find('div', id = "contentinner").find('div', id = "post_list")
    images_link = len_block.find_all('div', class_ = 'image')

    for imagerr in images_link:
        images_linkss = imagerr.find('img').get("src")
        array += [images_linkss]
    img_pictur_url = choice(array)


    if numin == "ru":
        idsr = discord.Embed(title=f"Обои на тему Аниме", description=f"Нажми на реакцию для переключения картинки ▶", color=0x141414)
        idsr.add_field(name='Открыть обои в браузере' ,value='[Нажми чтобы открыть](' + img_pictur_url + ')')
        idsr.set_image(url=img_pictur_url)

    else:
        idsr = discord.Embed(title=f"Wallpaper Anime", description=f"Click on the reaction below to scroll to the next picture ", color=0x141414)
        idsr.add_field(name='Open Image in Browser' ,value='[Click here to open](' + img_pictur_url + ')')
        idsr.set_image(url=img_pictur_url)

    message = await ctx.send(embed=idsr)
    await message.add_reaction('▶')
    await message.add_reaction('❌')
    msg = message.id
    print(msg)


    def check(reaction, user):
            if reaction.message != message:
                return False
                # SOLUTION: Checks if the message reacted on is the same as the one the bot sent

            return user == ctx.author and str(reaction.emoji) in ["▶", "❌"]
    i = 0
    reaction = None

    while True:
        if str(reaction) == '▶':
            i = 0
            arrays = []

            nps = random.randint(1, 30000)
            len_link = f"http://anime.reactor.cc/{nps}"
            len_response = requests.get(len_link).text
            len_soup = BeautifulSoup(len_response, 'lxml')
            len_block = len_soup.find('div', id = "contentinner").find('div', id = "post_list")
            images_link = len_block.find_all('div', class_ = 'image')

            for imagerr in images_link:
                    images_linksss = imagerr.find('img').get("src")
                    arrays += [images_linksss]

            img_pictur_url = choice(arrays)
            print(img_pictur_url)
            if numin == "ru":
                idsr = discord.Embed(title=f"Обои на тему Аниме", description=f"Нажми на реакцию для переключения картинки ▶", color=0x141414)
                idsr.add_field(name='Открыть обои в браузере' ,value='[Нажми чтобы открыть](' + img_pictur_url + ')')
                idsr.set_image(url=img_pictur_url)
                await message.edit(embed = idsr)
            else:
                idsr = discord.Embed(title=f"Wallpaper Anime", description=f"Click on the reaction below to scroll to the next picture ", color=0x141414)
                idsr.add_field(name='Open Image in Browser' ,value='[Click here to open](' + img_pictur_url + ')')
                idsr.set_image(url=img_pictur_url)
                await message.edit(embed = idsr)

        if str(reaction) == '❌':
            msggsss = await ctx.fetch_message(msg)
            await msggsss.delete()
        try:

            reaction, user = await Bot.wait_for('reaction_add', check = check)
            await message.remove_reaction(reaction, user)
        except:
            break




@Bot.event
async def on_command_error(ctx, error):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command
    if numin == "ru":
        embed = discord.Embed(title="Ошибка", description="Ошибка 503⠀⠀⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xb80208)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="The discord bot has application error⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xb80208)
        await ctx.send(embed=embed)


@Bot.command()
async def status(ctx, member: discord.Member):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command
    if numin == "ru":

        roles = [role for role in member.roles]

        embe = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embe.set_author(name=f"Информация о профели - {member}")
        embe.set_thumbnail(url=member.avatar_url)
        embe.set_footer(text=f"запрос сделан {ctx.author}", icon_url=ctx.author.avatar_url)

        embe.add_field(name="Айди", value=member.id, inline=False)
        embe.add_field(name="Никнеймы", value=member.display_name)
        embe.add_field(name="аккаун создан", value=member.created_at.strftime("%a, %#d %B %Y"))
        embe.add_field(name="присоединился к серверу", value=member.joined_at.strftime("%a, %#d %B %Y"), inline=False)
        embe.add_field(name=f"Роли игрока ({len(roles)})", value=" ".join({role.mention for role in roles}))
        await ctx.send(embed=embe)
    else:
        roles = [role for role in member.roles]

        embe = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embe.set_author(name=f"Information about User - {member}")
        embe.set_thumbnail(url=member.avatar_url)
        embe.set_footer(text=f"request has done by {ctx.author}", icon_url=ctx.author.avatar_url)

        embe.add_field(name="ID", value=member.id, inline=False)
        embe.add_field(name="Nickname", value=member.display_name)
        embe.add_field(name="Account was created", value=member.created_at.strftime("%a, %#d %B %Y"))
        embe.add_field(name="Joined server on", value=member.joined_at.strftime("%a, %#d %B %Y"), inline=False)
        embe.add_field(name=f"User roles({len(roles)})", value=" ".join({role.mention for role in roles}))
        await ctx.send(embed=embe)


@Bot.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)



@Bot.command(pass_context=True)
async def дашка(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send(file=discord.File('MbdRbgS8VWU.png'))


@Bot.command(pass_context= True)
async def help(ctx):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command

    if numin == "ru":
        embed = discord.Embed(title="QBut Bot Команды", description="здесь вы можете найти все команды бота​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xffc800)
        embed.add_field(name="**Добавить приветствующее письмо **", value="`welcome_channel <названия канала>`, нужен админ", inline=False)
        embed.add_field(name="**:frame_photo: Просмотр аватарки**", value="`avatar <@никнейм>`", inline=False)
        embed.add_field(name="**Статус пользователя**", value="`status <@никнейм>`", inline=False)

        embed.add_field(name="**Аниме картинки**", value="`anime_help` или `<anime тег>`", inline=False)
        embed.add_field(name="**Рандомная аниме картика**", value="`animes`", inline=False)
        embed.add_field(name=":wales: **Обои**", value="`wallpaper help` или `wallpaper <тег>`", inline=False)
        embed.add_field(name="**Статус сервера**", value="`server`", inline=False)
        embed.add_field(name="**QBot приглашения бота**", value="`invite`", inline=False)

        embed.add_field(name=":milky_way: Windows 10 Темы", value="`windows10`", inline=False)
        embed.add_field(name="Майнкрафт профиль", value="`profile <никнейм>`", inline=False)
        embed.add_field(name=":tools: Команда очистить", value="`clear <число>`, нужен админ", inline=False)

        embed.add_field(name=":roller_coaster: Поцеловать игрока", value="`kiss <@user>`", inline=False)
        embed.add_field(name=":roller_coaster: секс", value="`sex <@user>`", inline=False)

        embed.add_field(name=":earth_americas: Выбрать язык на сервере", value="`set_lang <en или ru>`, нужен админ", inline=False)
        embed.add_field(name=":musical_note: Музыкальный бот помощь", value="`music`", inline=False)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="QBut Bot comamnds", description="In thist message can you find all commands​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xffc800)
        embed.add_field(name="**Add Welcome message to channel **", value="`welcome_channel <Channel name>`, need administrator", inline=False)
        embed.add_field(name="**:frame_photo: Show User avatar**", value="`avatar <@user>`", inline=False)
        embed.add_field(name="**Show user discord status**", value="`status <@user>`", inline=False)

        embed.add_field(name="**Anime Pictures**", value="`anime_help` or `<anime tag>`", inline=False)
        embed.add_field(name="**Second anime command random anime picture**", value="`animes`", inline=False)
        embed.add_field(name=":wales: **Wallpaper**", value="`wallpaper help` or `wallpaper <tag>`", inline=False)
        embed.add_field(name="**Server status**", value="`server`", inline=False)
        embed.add_field(name="**QBot invite link**", value="`invite`", inline=False)

        embed.add_field(name=":milky_way: Windows 10 themes", value="`windows10`", inline=False)
        embed.add_field(name="Minecraft profile information", value="`profile <nickname>`", inline=False)
        embed.add_field(name=":tools: Clear command", value="`clear <amount>`, need administrator", inline=False)

        embed.add_field(name=":roller_coaster: kiss a user", value="`kiss <@user>`", inline=False)
        embed.add_field(name=":roller_coaster: sex", value="`sex <@user>`", inline=False)

        embed.add_field(name=":earth_americas: Select language on server", value="`set_lang <en or ru>`, need administrator", inline=False)
        embed.add_field(name=":musical_note: Music help", value="`music`", inline=False)

        await ctx.send(embed=embed)





@Bot.command()
async def avatar(ctx, member: discord.Member):
    #check language
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
        #command

    if numin == "ru":
        embed = discord.Embed(title=f"Аватарка {member}", description="", color=0x1780c2)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"Avatar {member}", description="", color=0x1780c2)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)


# Read the Data files and store them in a variable


OWNERID = 249182889386704897

# Define "Bot"

# Let us Know when the Bot is ready and has started

# A simple and small ERROR handler
@Bot.event
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title='',
    color=discord.Color.red())
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Invalid Permissions', value=f'You dont have {error.missing_perms} permissions.')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name = f':x: Terminal Error', value = f"```{error}```")
        await ctx.send(embed = embed)
        raise error

# Load command to manage our "Cogs" or extensions
@Bot.command()
async def load(ctx, extension):
    # Check if the user running the command is actually the owner of the Bot
    if ctx.author.id == OWNERID:
        Bot.load_extension(f'Cogs.{extension}')
        await ctx.send(f"Enabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Unload command to manage our "Cogs" or extensions
@Bot.command()
async def unload(ctx, extension):
    # Check if the user running the command is actually the owner of the Bot
    if ctx.author.id == OWNERID:
        Bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"Disabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Reload command to manage our "Cogs" or extensions
@Bot.command(name = "reload")
async def reload_(ctx, extension):
    # Check if the user running the command is actually the owner of the Bot
    if ctx.author.id == OWNERID:
        Bot.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"Reloaded the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Automatically load all the .py files in the Cogs folder
for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        try:
            Bot.load_extension(f'Cogs.{filename[:-3]}')
        except Exception:
            raise Exception

token = os.environ.get('TOKEN')
Bot.run(token)
