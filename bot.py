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
from datetime import datetime

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import fake_useragent
from time import sleep
import urllib.request
import requests
from PIL import Image
import os
from PIL import Image
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

user = fake_useragent.UserAgent().random
header = {'user-agent': user}



intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)
from discord.ext import commands

mongo = os.environ.get('MONGO')
cluster = MongoClient(mongo)

db = cluster["discord"]
collection = db["data"]

collections = db["server"]

def get_prefix(clients, message):
    serveride = f"{message.guild.id}"
    result = collections.find({"_id": serveride})

    for result in result:
        prefixs = result[serveride]

    return str(prefixs)


Bot = commands.Bot(command_prefix=get_prefix, intents=intents)
Bot.remove_command('help')

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name="q.help v1.0.13"))
    s=Service(ChromeDriverManager().install())

mongo = os.environ.get('MONGO')
cluster = MongoClient(mongo)

db = cluster["discord"]
collection = db["data"]

collections = db["server"]

@Bot.event
async def on_guild_join(guild):
    guild_id = str(guild.id)
    serverid = guild_id
    serveride = f"{serverid}"

    db = cluster["discord"]
    collection = db["data"]

    post = {"_id": serveride, "name": "en"}

    collection.insert_one(post)
    
    db = cluster["discord"]
    collections = db["server"]
    
    post_two = {"_id": serveride, serveride: "q." }
    collections.insert_one(post_two)

    
@Bot.command()
@commands.has_permissions(administrator = True)
async def prefix(ctx, arg1: str = None):


    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]

    if arg1 is None:
        if numin == "ru":
            await ctx.send("Пожалуйста, добавьте префикс например `prefix -`")
        else:
            await ctx.send("Please add the prefix eg `prefix -`")


    else:
        serveride = f"{serveride}"
        resultssss = collections.update_one({"_id": serveride}, {"$set": {serveride: arg1}})

        if numin == "ru":
            await ctx.send(f"Префикс изменён на {arg1}")
        else:
            await ctx.send(f"prefix change to {arg1}")
        
@Bot.command()
@commands.has_permissions(administrator = True)
async def say(ctx, *, msg: str = None):
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]
    if msg is None:
        if numin == "ru":
            await ctx.send("Пожалуйста, добавьте text `say text`")
        else:
            await ctx.send("Please add the text `say text`")
    else:
        await ctx.channel.purge(limit = 1)
        await ctx.send(msg)
        
        

                        

@Bot.command()
@commands.has_permissions(manage_channels = True)
async def mute(ctx, user : discord.Member, duration = 0,*, unit = None):
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        autoroles = result["mute_role"]
        numin = result["name"]


    sym = len(autoroles)
    last = int(sym) - int(1)
    von = autoroles[3: last]
    print(von)

    roleobject = discord.utils.get(ctx.message.guild.roles, id=int(von))

    if numin == "ru":
        await ctx.send(f":white_check_mark: {user} замучен  {duration}{unit}")
    else:
        await ctx.send(f":white_check_mark: {user} Muted {duration}{unit}")
    await user.add_roles(roleobject)
    if unit == "s":
        wait = 1 * duration
        await asyncio.sleep(wait)
    elif unit == "m":
        wait = 60 * duration
        await asyncio.sleep(wait)
    await user.remove_roles(roleobject)
    if numin == "ru":
        await ctx.send(f":white_check_mark: {user} размучен")
        embed = discord.Embed(title = "Мут", description = f":warning:  вам был выдан мут на сервере {ctx.guild.name}", color =0xffc800)
        await user.send(embed = embed)
    else:
        await ctx.send(f":white_check_mark: {user} was unmuted")
        embed = discord.Embed(title = "Mute notification", description = f":warning:  you was muted on {ctx.guild.name} server", color =0xffc800)
        await user.send(embed = embed)
        
        
@Bot.event
async def on_voice_state_update(member, before, after):
    serveride = f"{member.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]

    if numin == "ru":
        channel_lang = "создать голосовой [+]"
        name = 'Свой голосовой канал'
    else:
        channel_lang = "create voice channel [+]"
        name = "Own voice channel"
    categorys = discord.utils.get(member.guild.categories, name=name)
    try:
        if after.channel.name == channel_lang:

            guild = member.guild

            id_channel = await guild.create_voice_channel(f'{member.name}', category=categorys)

            channel = Bot.get_channel(id_channel.id)
            everyone = member
            perm = channel.overwrites_for(everyone)
            perm.manage_channels = True

            await id_channel.set_permissions(everyone, overwrite=perm)

            existing_channel = discord.utils.get(guild.channels, id=int(id_channel.id))
            await member.move_to(channel)
    except AttributeError:
        pass

    if before.channel is None and after.channel is not None:
        if after.channel.name == channel_lang:

            guild = member.guild

            id_channel = await guild.create_voice_channel(f'{member.name}', category=categorys)

            channel = Bot.get_channel(id_channel.id)

            existing_channel = discord.utils.get(guild.channels, id=int(id_channel.id))
            await member.move_to(channel)


    if before.channel is not None:
        try:
            if before.channel.category.id == categorys.id:

                if len(before.channel.members) == 0:

                    if before.channel.name == channel_lang:
                        return

                    else:
                        await before.channel.delete()
        except AttributeError:
            return

token = os.environ.get('TOKEN')        
@Bot.command()
async def youtube(ctx):
    data =  {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 755600276941176913,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/Json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send("Зайдите в канал")
    else:
        await ctx.send("Зайдите в канал")

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data = json.dumps(data), headers = headers)
    link = json.loads(response.content)

    await ctx.send(f"https://discord.com/invite/{link['code']}")      
    

    
    
@Bot.event
async def on_message(msg):
    await Bot.process_commands(msg)
    print(msg.content[12:24])
    if msg.content[12:24] == 'tiktok.com/@':
        if int(28) < len(msg.content):
            messages_id = msg.id
            channel = msg.channel
            await channel.delete_messages([discord.Object(id=messages_id)])

        #подключения драйвера
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)



        #склейка сылки на тикток и сайта
        driver.get(f'https://ttsave.app/#{msg.content}')
        ava_url = str()
        #пойск сыллки на скачивания тикток
        num = 0
        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            ekfar = elem.get_attribute("href")


            if num <= 0:
                if ekfar[0:9] == f'https://v':
                    num = num + 1
                    found_video_url = elem.get_attribute("href")
                    print(found_video_url)

                    #рандомную цифру для разнах названий
                    n = random.randint(0,999)


                    #скачать видео тикток
                    urllib.request.urlretrieve(found_video_url, f'Estol{n}.mp4')

                    try:
                        await msg.channel.send(file=discord.File(f"Estol{n}.mp4"))
                        os.remove(f"Estol{n}.mp4")
                    except discord.errors.HTTPException:
                        await msg.channel.send("The video is to long")

                if ekfar[0:9] == f'https://p':
                    author_url = elem.get_attribute("href")
                    print(author_url)
                    ava_url = ava_url + author_url


                    #отправка видео
        for elem in elems:
            embe = discord.Embed()
            ekfar = elem.get_attribute("href")
            if ekfar[0:24] == f'https://www.tiktok.com/@':
                nickname = elem.get_attribute("href")
                num = len(nickname)
                print(nickname[23:num-1])  



#         embe.set_author(name=f"ТиТок - {nickname[23:num-1]}", icon_url=ava_url)
        embe.set_author(name=f"ТиТок", icon_url=ava_url)
        plays = driver.find_elements_by_xpath('(.//span[@class = "text-gray-500"])[1]')[0].text
        likes = driver.find_elements_by_xpath('(.//span[@class = "text-gray-500"])[2]')[0].text
        comments = driver.find_elements_by_xpath('(.//span[@class = "text-gray-500"])[3]')[0].text

        embe.set_footer(text=f"запрос сделан {msg.author}", icon_url=msg.author.avatar_url)


        embe.add_field(name="Plays :arrow_forward:", value=plays)
        embe.add_field(name="Likes :heart:", value=likes)
        embe.add_field(name="comments :incoming_envelope:", value=comments)
        embe.add_field(name="video on TikTok", value='[click to open in browser](' + msg.content + ')', inline = False)
        await msg.channel.send(embed=embe)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
@Bot.command()
@commands.has_permissions(administrator = True)
async def own_voice(ctx):

    #land check
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]

    guild = ctx.message.guild

    if numin == "ru":
        name = "Свой голосовой канал"

        await ctx.guild.create_category("Свой голосовой канал")
        categorys = discord.utils.get(ctx.guild.categories, name=name)
        await guild.create_voice_channel("создать голосовой [+]", category=categorys)
        await ctx.send(":ballot_box_with_check: выполнено" )
    else:
        name = "Own voice channel"

        await ctx.guild.create_category("Own voice channel")
        categorys = discord.utils.get(ctx.guild.categories, name=name)
        await guild.create_voice_channel("create voice channel [+]", category=categorys)
        await ctx.send(":ballot_box_with_check: complete" )
        
@Bot.command()
@commands.has_permissions(administrator = True)
async def bye_channel(ctx, arg1: str = None):
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]

    if arg1 is None:
        if numin == "ru":
            await ctx.send("Пожалуйста, добавьте названия канала например `bye_channel bye`")
        else:
            await ctx.send("Please add the channel name eg `bye_channel bye`")

    else:
        serveride = f"{str(ctx.guild.id)}"
        result = collection.update_one({"_id": serveride}, {"$set": {"remove": arg1}})


        if numin == "ru":
            await ctx.send(f"Вы добавили прощальное сообщение в {arg1} канал")
        else:
            await ctx.send(f"you add bye message to {arg1} channel")
            
            
@Bot.event
async def on_guild_remove(guild):
    guild_id = str(guild.id)
    serverid = guild_id
    serveride = f"{serverid}"
    db = cluster["discord"]
    collections = db["data"]
    collection = db["server"]
    results = collection.delete_one({"_id": serveride})    
    results_two = collections.delete_one({"_id": serveride})    
    
@Bot.command()
async def feedback(ctx, *, msg: str = None):

    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]

    collectionst = db["bugs"]
    if msg is None:
        if numin == "ru":
            await ctx.send("Пожалуйста, допишите роль текст")
        else:
            await ctx.send("Please add feedback text")
    else:
        serveride = f"{str(ctx.guild.id)}"
        author = f"{ctx.author}"
        id_ran = random.randint(0,9999)
        post = {"_id": id_ran, "user": author, "bug": msg}
        collectionst.insert_one(post)

        serveride = f"{ctx.guild.id}"
        result = collection.find({"_id": serveride})

        for result in result:
            numin = result["name"]

        if numin == "ru":
            await ctx.send(f"спасибо вам за поддержку бота")
        else:
            await ctx.send(f"Thank you for helping make bot better")



        
@Bot.command()
@commands.has_permissions(administrator = True)
async def autoroleoff(ctx):
    guild_id = str(ctx.guild.id)
    serverid = guild_id
    serveride = f"{serverid}"
    result = collection.update_one({"_id": serveride}, {"$set": {"autorole": "delete$1"}})


    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]

    if numin == "ru":
        await ctx.send("Автороль было успешно выключена")
    else:
        await ctx.send("Autorole was desable")        
 
@Bot.command()
@commands.has_permissions(administrator = True)
async def autorole(ctx, arg1: str = None):

    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]


    if arg1 is None:
        if numin == "ru":
            await ctx.send("Пожалуйста, допишите роль `@role`")
        else:
            await ctx.send("Please add role `@role`")
    else:
        serveride = f"{str(ctx.guild.id)}"
        result = collection.update_one({"_id": serveride}, {"$set": {"autorole": arg1}})



        if numin == "ru":
            await ctx.send(f" Роль {arg1} добавлена в автороли")
        else:
            await ctx.send(f"Role {arg1} add to autorole")

@Bot.command()
@commands.has_permissions(administrator = True)
async def set_lang(ctx, msg: str = None):


    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]

    if msg is None:
        if numin == "ru":
            await ctx.send("Пожалуйста, добавьте язык en или ru `set_lang ru/en`")
        else:
            await ctx.send("Please add language `set_lang en/ru`")
    else:

        if msg == "ru":
            result = collection.update_one({"_id": serveride}, {"$set": {"name": msg}})
            await ctx.send("на сервере успешно установлен русский язык")


        elif msg == "en":
            result = collection.update_one({"_id": serveride}, {"$set": {"name": msg}})
            await ctx.send("Server language was set to English")


        else:
            if numin == "ru":
                await ctx.send("Пожалуйста выберети между ru и en")
            else:
                await ctx.send("please select ru or en")




@Bot.command()
@commands.has_permissions(administrator = True)
async def welcome_channel(ctx, arg1: str = None):
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]

    if arg1 is None:
        if numin == "ru":
            await ctx.send("Пожалуйста, добавьте названия канала например `welcome_channel general`")
        else:
            await ctx.send("Please add the channel name eg `welcome_channel general`")

    else:
        serveride = f"{str(ctx.guild.id)}"
        result = collection.update_one({"_id": serveride}, {"$set": {"channel": arg1}})



        if numin == "ru":
            await ctx.send(f"Вы добавляете приветственное сообщение в {arg1} канал")
        else:
            await ctx.send(f"you add welcome message to {arg1} channel")



@Bot.event
async def on_member_join(member):
    serveride = f"{member.guild.id}"
    resultsss = collection.find({"_id": serveride})

    embed_ru = discord.Embed(title=f"▬▬▬▬▬[{member.guild.name}]▬▬▬▬▬ \nДобро пожаловать на сервер \n└{member.guild.name}.", description=f":hand_splayed: Приветствую тебя, {member.mention}⠀\n :fireworks: Надеюсь тебе понравится у нас​​", color=0xffc800)
    embed_ru.set_image(url="https://media1.tenor.com/images/83f1d91029dc0a158e2d27b8535d3b7d/tenor.gif?itemid=21103469")
    embed_ru.add_field(name=f"информация о {member.name}", value=":arrow_forward: " + member.created_at.strftime("%a, %#d %B %Y") + f" \n :id: {member.id}")
    embed_ru.set_thumbnail(url=member.avatar_url)
    embed_ru.set_footer(text=f"новый игрок {member.name}", icon_url=member.avatar_url)

    embed_en = discord.Embed(title=f"▬▬▬▬▬[{member.guild.name}]▬▬▬▬▬ \n Welcome to server \n└{member.guild.name}.", description=f":hand_splayed: Hello, {member.mention}⠀\n :fireworks: I hope you like ours server", color=0xffc800)
    embed_en.set_image(url="https://media1.tenor.com/images/83f1d91029dc0a158e2d27b8535d3b7d/tenor.gif?itemid=21103469")
    embed_en.add_field(name=f"Information about {member.name}", value=":arrow_forward: " + member.created_at.strftime("%a, %#d %B %Y") + f" \n :id: {member.id}")
    embed_en.set_thumbnail(url=member.avatar_url)
    embed_en.set_footer(text=f"new user {member.name}", icon_url=member.avatar_url)

    try:
        for resultsss in resultsss:
            channel = resultsss["channel"]
            lang = resultsss["name"]

        channel = discord.utils.get(member.guild.channels, name = channel)

        if lang == "ru":
            await channel.send(embed=embed_ru)
        else:
            await channel.send(embed=embed_en)

    except KeyError:
        print("канал не добавлен")
    except AttributeError as channel:
        print("данный канал ненайден")

    print("autorole")
    result = collection.find({"_id": serveride})

    for result in result:
        autoroles = result["autorole"]
        print(autoroles)

    sym = len(autoroles)
    last = int(sym) - int(1)
    von = autoroles[3: last]
    print(von)


    role = discord.utils.get(member.guild.roles, id=int(von))
    await member.add_roles(role)

@Bot.command()
async def sex(ctx, member: discord.Member):
    if ctx.channel.nsfw == False:
        await ctx.send("need/нужно NSFW")
    else:
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

    serveride = f"{member.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]
    base_date = member.joined_at.strftime("%Y-%m-%d")

    today = date.today()

    data = [today.strftime("%Y-%m-%d")]

    format = "%Y-%m-%d"

    base = datetime.strptime(base_date, format)
    diff = [(datetime.strptime(d, format) - base).days for d in data]

    embed_ru = discord.Embed(title = f"{member.display_name} покинул(а) сервер", description = f":hand_splayed: пока {member.display_name}", color=0xffc800)
    embed_ru.add_field(name = "Время провождения на сервере", value = f"└{diff[0]} дней")
    embed_ru.set_image(url="https://media1.tenor.com/images/56976dab54f0f14b5d9b87d100091858/tenor.gif?itemid=17441907")
    embed_ru.set_thumbnail(url=member.avatar_url)

    embed_en = discord.Embed(title = f"{member.display_name} leave server", description = f":hand_splayed: bye {member.display_name}", color=0xffc800)
    embed_en.add_field(name = "Time stayed on server", value = f"└{diff[0]} days")
    embed_en.set_image(url="https://media1.tenor.com/images/56976dab54f0f14b5d9b87d100091858/tenor.gif?itemid=17441907")
    embed_en.set_thumbnail(url=member.avatar_url)


    serveride = f"{member.guild.id}"
    resultsss = collection.find({"_id": serveride})
    for resultsss in resultsss:
        channel = resultsss["remove"]

    channel = discord.utils.get(member.guild.channels, name = channel)
    if numin == "ru":
        await channel.send(embed = embed_ru)
    else:
        await channel.send(embed = embed_en)


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




# @Bot.command()
# async def aktie(ctx, arg1):

#     #подключения драйвера
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--no-sandbox")
#     driver = webdriver.Chrome(service=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)


    
#     len_link = f"https://www.google.com/search?q={arg1}+aktie"
#     driver.get(f"https://www.google.com/search?q={arg1}+aktie")
#     sleep(2)
#     driver.find_element(By.ID, "L2AGLb").click()

#     screenshot = driver.save_screenshot(r'my_screenshot.png')
#     sleep(2)

#     sleep(2)
#     im = Image.open(r'my_screenshot.png')
#     sleep(2)
#     im_crop = im.crop((20, 365, 700, 550))

#     im_crop.save(r'guido_pillow_crop.png', quality=95)
#     sleep(1)


#     elem= driver.find_element_by_css_selector(".NprOob")
#     elems= driver.find_element_by_css_selector(".WlRRw")

#     textil = elems.text
#     lents = len(elems.text)
#     bin = int(lents) - int(5)
#     rel = textil[0:bin]
#     print(textil[0:1])

#     if str(textil[0:1]) == str("+"):
#         embed_en = discord.Embed(title=f"▬▬▬▬▬▬▬▬[Акции {arg1}]▬▬▬▬▬▬▬▬", description=f"**Стоимость:** {elem.text} │ **просадок:** {rel}", color=0x3cd126)
#     else:
#         embed_en = discord.Embed(title=f"▬▬▬▬▬▬▬▬[Акции {arg1}]▬▬▬▬▬▬▬▬", description=f"**Стоимость:** {elem.text} │ **просадок:** {rel}", color=0xea4335)



#     file = discord.File(r"guido_pillow_crop.png", filename="guido_pillow_crop.png")
#     embed_en.set_image(url="attachment://guido_pillow_crop.png")

#     await ctx.send(file=file, embed=embed_en)
#     os.remove(r"my_screenshot.png")
#     os.remove(r"guido_pillow_crop.png")

# #     .find('li', class_ = "pager__item pager__item_last-page")



@Bot.command()
async def aktie(ctx, arg1):
    #подключения драйвера
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    
    
    driver.get(f"https://www.google.com/search?q={arg1}+aktie")

    sleep(1)
    elem= driver.find_element_by_css_selector(".NprOob")
    print(elem.text)
    
    screenshot = driver.save_screenshot('my_screenshot.png')
    await ctx.send(file=discord.File("my_screenshot.png"))
    os.remove("my_screenshot.png")
    await ctx.send(elem.text)
    




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
    if ctx.channel.nsfw == False:
        await ctx.send("need/нужно NSFW")
    else:
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

        embed.add_field(name="**Аниме картинки**", value="`anime_help` или `anime <тег>`", inline=False)
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
        embed.add_field(name=" Выбрать префикс бота", value="`prefix <Символ или слова>`, нужен админ", inline=False)

        embed.add_field(name="Сказать от имени бота", value="`say <текст>`, нужен админ", inline=False)
        embed.add_field(name="Добавить автороль", value="`autorole <@role>`, нужен админ", inline=False)
        embed.add_field(name="Отключить автороль", value="`autoroleoff`, нужен админ", inline=False)

        embed.add_field(name="Отправить варн игроку", value="`warn <@user> <сообщение>`, нужен модер", inline=False)
        embed.add_field(name="добавить роль замучен", value="`mute_role <@role>`, нужен админ", inline=False)
        embed.add_field(name="Замутить пользователя", value="`mute <@user> <цифру> <s или m>`, нужен модер", inline=False)

        embed.add_field(name="Создавать свои голосовые каналы", value="`own_voice`, нужен админ", inline=False)
        embed.add_field(name="Сообщения после покидание сервера", value="`bye_channel <названия канала>`, нужен админ", inline=False)
        embed.add_field(name="Отправить баг", value="`feedback <Описать найденный баг>`", inline=False)

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="QBut Bot comamnds", description="In thist message can you find all commands​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xffc800)
        embed.add_field(name="**Add Welcome message to channel **", value="`welcome_channel <Channel name>`, need administrator", inline=False)
        embed.add_field(name="**:frame_photo: Show User avatar**", value="`avatar <@user>`", inline=False)
        embed.add_field(name="**Show user discord status**", value="`status <@user>`", inline=False)

        embed.add_field(name="**Anime Pictures**", value="`anime_help` or `anime <tag>`", inline=False)
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
        embed.add_field(name=" Select Bot prefix", value="`prefix <Symbol or word>`, need administrator", inline=False)

        embed.add_field(name="Say message from bot", value="`say <text>`, need administrator", inline=False)
        embed.add_field(name="add Autorole", value="`autorole <@role>`, need administrator", inline=False)
        embed.add_field(name="disable Autorole", value="`autoroleoff`, need administrator", inline=False)


        embed.add_field(name="warn a member", value="`warn <@user> <message>`, need Moderator", inline=False)
        embed.add_field(name="add mute role", value="`mute_role <@role>`, need administrator", inline=False)
        embed.add_field(name="mute a member", value="`mute <@user> <number> <s or m>`, need Moderator", inline=False)

        embed.add_field(name="create own voice channel", value="`own_voice`, need administrator", inline=False)
        embed.add_field(name="message if member leave server", value="`bye_channel <channel name>`, need administrator", inline=False)
        embed.add_field(name="send a bug", value="`feedback <Problem Text>`", inline=False)

        await ctx.send(embed=embed)




@Bot.command()
async def music(ctx):
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]
    if numin == "ru":
        embed = discord.Embed(title= ":musical_note: Музыка помощь", description ="Команды для проигрывания музыки")

        embed.add_field(name="**Играть музыку**", value="`play, sing, p <названия песни или YT ссылку>`", inline=False)
        embed.add_field(name="**Пропустить песню**", value="`skip`", inline=False)
        embed.add_field(name="**Изменить громкость музыки**", value="`vol <1 - 100>`", inline=False)
        embed.add_field(name="**Названия песни которая сейчас играет**", value="`np`", inline=False)
        embed.add_field(name="**Поставить песню на паузу**", value="`pause`", inline=False)
        embed.add_field(name="**Продолжить песню**", value="`resume`", inline=False)
        embed.add_field(name="**Песни в плейлисте**", value="`queue или q`", inline=False)
        embed.add_field(name="**Остановить бота**", value="`stop`", inline=False)

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title= ":musical_note:  Music Help", description ="commands to play music")

        embed.add_field(name="**Play music**", value="`play, sing, p <song name or YT URL>`", inline=False)
        embed.add_field(name="**Song skip**", value="`skip`", inline=False)
        embed.add_field(name="**Change Music bot value**", value="`vol <1 - 100>`", inline=False)
        embed.add_field(name="**Song now playing**", value="`np`", inline=False)
        embed.add_field(name="**Pause song**", value="`pause`", inline=False)
        embed.add_field(name="**Resume song**", value="`resume`", inline=False)
        embed.add_field(name="**Songs in playlist**", value="`queue or q`", inline=False)
        embed.add_field(name="**Stop music bot**", value="`stop`", inline=False)

        await ctx.send(embed=embed)

        
@Bot.command()
@commands.has_permissions(manage_channels = True)
async def warn(ctx, member: discord.Member, *, msg):
    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]
    if numin == "ru":
        embed = discord.Embed(title = "Warn внимания", description = f":warning:  вам был выдан варн на сервере {ctx.guild.name}", color =0xffc800)
        embed.add_field(name = "причина", value =f":page_facing_up: {msg}" )
        await member.send(embed = embed)
        await ctx.send(f"вы отправели варн {member}")
    else:
        embed = discord.Embed(title = "Warn notification", description = f":warning:  you was warn on  {ctx.guild.name} server", color =0xffc800)
        embed.add_field(name = "cause", value =f":page_facing_up: {msg}" )
        await member.send(embed = embed)
        await ctx.send(f"you warn {member}")
        
@Bot.command()
@commands.has_permissions(administrator = True)
async def mute_role(ctx, arg1: str = None):

    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})

    for result in result:
        numin = result["name"]


    if arg1 is None:
        if numin == "ru":
            await ctx.send("Пожалуйста, допишите роль `@role`")
        else:
            await ctx.send("Please add Mute role `@role`")
    else:
        serveride = f"{str(ctx.guild.id)}"
        result = collection.update_one({"_id": serveride}, {"$set": {"mute_role": arg1}})



        if numin == "ru":
            await ctx.send(f" Роль {arg1} добавлена в мьют роль")
        else:
            await ctx.send(f"Role {arg1} add to mute role")
       
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

    serveride = f"{ctx.guild.id}"
    result = collection.find({"_id": serveride})
    for result in result:
        numin = result["name"]


    if isinstance(error, commands.CommandNotFound):
        if numin == "ru":
            embed.add_field(name=f'даная команда не найдена', value=f'Проверти команду на наличие ошибок')
            await ctx.send(embed=embed)
        else:
            embed.add_field(name=f'Command Not Found', value=f'check your command')
            await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        if numin == "ru":
            embed.add_field(name=f'Недостаточно прав', value=f'у вас нет прав{error.missing_perms}.')
            await ctx.send(embed=embed)
        else:
            embed.add_field(name=f'Invalid Permissions', value=f'You dont have {error.missing_perms} permissions.')
            await ctx.send(embed=embed)


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
