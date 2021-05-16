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
from bs4 import BeautifulSoup
import re
import random
from random import choice




intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
from discord.ext import commands
Bot = commands.Bot(command_prefix='--', intents=intents)
Bot.remove_command('help')


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name = '❗-писать-тут')
    await channel.send(f"Зиег ХАЙЛЬ Доброе уро девочки вы зашли на сервер **{member.guild.name}**, вы теперь секс машина {member.mention}")


@Bot.command(pass_context= True)
async def корды(ctx):
    embed = discord.Embed(title="Все координаты", description="Tут вы найдёте все координаты ферм​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0x0384fc)
    embed.add_field(name="**Ферма скелетов:**", value="(По метро): -7844 -5753", inline=False)
    embed.add_field(name="**Ферма гвардов:**", value="(по метро): -8000 -6435", inline=False)
    embed.add_field(name="**Ферма золота и яма:**", value="-7777 -6460", inline=False)
    embed.add_field(name="**Ферма зомби и пауков :**", value="(По метро): -7430 -5895", inline=False)
    embed.add_field(name="**Городская ферма ифритов (В аду):**", value="(В аду): -1200 -630", inline=False)
    embed.add_field(name="**Портал в энд (В аду):**", value="-1100 -950", inline=False)
    embed.add_field(name="Портал в Техноград (В аду)", value="-918 -750", inline=False)
    embed.add_field(name="Портал в хаб Технограда:", value="-7400 -6085", inline=False)
    embed.add_field(name="Остров На Хп Технограда ", value="-490", inline=False)
    embed.add_field(name="Корды острова в обычном мире ", value="-6983 -3923", inline=False)
    embed.add_field(name="Склад:", value="-7470 -6015", inline=False)
    await ctx.send(embed=embed)
#add role command

@Bot.command()
async def role_help(ctx):
    embed = discord.Embed(title="Выдача роли по выбору", description="При помоще команд ниже вы можете выдавать себе роли или забирать​⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xff19d1)
    embed.add_field(name="**Выдать себе роль редстоунера:**", value="--редстоунер_уровень", inline=False)
    embed.add_field(name="**Выдать себе роль фермер:**", value="--фермер_уровень", inline=False)
    embed.add_field(name="**Выдать себе роль строитель:**", value="--строитель_уровень", inline=False)
    embed.add_field(name="**Выдать себе роль декоратор:**", value="--декоратор_уровень", inline=False)
    embed.add_field(name="**Выдать себе роль ресурсер:**", value="--ресурсер_уровень", inline=False)
    embed.add_field(name="**Выдать себе роль схематика:**", value="--схематика", inline=False)
    embed.add_field(name="**Выдать себе роль рпшер:**", value="--рпшер", inline=False)
    embed.add_field(name="**Пример выдачи роли:**", value="--редстоунер_3", inline=False)
    embed.add_field(name="**Что бы удалить роль:**", value="--имя роли_удалить", inline=False)
    mess = await ctx.send(embed=embed)


role_id = 642306802461048833
@Bot.command(pass_context=True)
@commands.has_role(707212021791326241)
async def remove(ctx):
    await ctx.channel.purge(limit = 1)
    role = get(ctx.guild.roles, id=role_id)
    await ctx.author.remove_roles(role)

role = 642306802461048833
@Bot.command(pass_context=True)
@commands.has_role(707212021791326241)
async def ülöß(ctx):
    await ctx.channel.purge(limit = 1)
    rogle = get(ctx.guild.roles, id=role_id)
    await ctx.author.add_roles(rogle)


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
    
@Bot.event
async def on_command_error(ctx, error):
        embed = discord.Embed(title="ОШИБКА", description="Извините но такая команда не найдена⠀или была неправильно выполнена⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xb80208)
        await ctx.send(embed=embed)


@Bot.command(pass_context=True)
async def Revolycioner_Rab(ctx):
    await ctx.send(file=discord.File('revo.jpg'))

@Bot.command(pass_context=True)
async def den4ikpro(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send(file=discord.File('den.jpg'))

@Bot.command()
async def ping(ctx):
    ping_ = Bot.latency
    ping =  round(ping_ * 1000)
    await ctx.send(f"my ping is {ping}ms")


@Bot.command(pass_context=True)
async def ФАШИСТЫ(ctx):
    await ctx.send("КТО ФАШИСТ ГДЕ ФАШИСТ ТЫ ФАШИСТ У СУКА")


@Bot.command()
async def status(ctx, member: discord.Member):
    roles = [role for role in member.roles]

    embe = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embe.set_author(name=f"Информация о пользователи - {member}")
    embe.set_thumbnail(url=member.avatar_url)
    embe.set_footer(text=f"Запрос был сделан {ctx.author}", icon_url=ctx.author.avatar_url)

    embe.add_field(name="айди", value=member.id, inline=False)
    embe.add_field(name="Никнейм", value=member.display_name)
    embe.add_field(name="аккаунт был создан", value=member.created_at.strftime("%a, %#d %B %Y"))
    embe.add_field(name="Присоединился к Дискорд серверу", value=member.joined_at.strftime("%a, %#d %B %Y"), inline=False)
    embe.add_field(name=f"Роли игрока({len(roles)})", value=" ".join({role.mention for role in roles}))
    await ctx.send(embed=embe)

@Bot.command(pass_context = True)
@commands.has_role(620623023296348180)
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)

@Bot.command(pass_context = True)
@commands.has_role(620623023296348180)
async def moreclear(ctx, amount = 50):
    await ctx.channel.purge(limit = amount)


@Bot.command(pass_context=True)
async def япутин(ctx):
    await ctx.send(file=discord.File('putin.jpg'))

@Bot.command(pass_context=True)
async def дааашка(ctx):
    await ctx.send(file=discord.File('Dashka.png'))


@Bot.command(pass_context=True)
async def рита(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send(file=discord.File('rita.jpg'))
    
@Bot.command(pass_context=True)
async def киска(ctx):
    await ctx.send("у твоей мамы")



@Bot.command(pass_context=True)
async def гусь_даун(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send(file=discord.File('gdfgdfg.mp4'))


@Bot.command(pass_context=True)
async def дашка(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send(file=discord.File('MbdRbgS8VWU.png'))

    
@Bot.command(pass_context= True)
async def commands(ctx):
    embed = discord.Embed(title="Техноград Бот", description="Tут вы найдёте все команды бота​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xeee657)
    embed.add_field(name="**Команда что бы посмотреть все координаты:**", value="--корды", inline=False)
    embed.add_field(name="**Если нужны команды бота:**", value="--help", inline=False)
    embed.add_field(name="**Oчистить текст:**", value="--clear число сообщений лимит 10 команда тока для Велоцераптор", inline=False)
    embed.add_field(name="**Oчистить многа текста:**", value="--moreclear число сообщений лимит 50 команда тока для Велоцераптор", inline=False)
    embed.add_field(name="**Узнать болше информацией о городе:**", value="--info", inline=False)
    embed.add_field(name="**Забирать и добавлять себе роли:**", value="--role_help", inline=False)
    embed.add_field(name="**Узнать информацию о пользователе:**", value="--status @ник", inline=False)
    embed.add_field(name="**Посмотреть аватарку игрока в дискорде:**", value="--ава @ник", inline=False)
    embed.add_field(name="**Нашел баг или хочешь предложить идею:**", value="пиши Estol#7368 в лс", inline=False)
    embed.add_field(name="Author", value="Estol", inline=False)
    mess = await ctx.send(embed=embed)
    await mess.add_reaction('👍🏻')
    await mess.add_reaction('👎🏻')

@Bot.command(pass_context= True)
async def info(ctx):
    embed = discord.Embed(title="Полезная информация о городе", description="В этом списке вы найдёте всю необходимую информацию о городе​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0x00eeff)
    embed.add_field(name="**Айпи тест сервера**", value="95.217.46.155:25516", inline=False)
    embed.add_field(name="**Собрание**", value="Собрание каждую cоботу через неделю", inline=False)
    embed.add_field(name="**Мэр города на данный момент**", value="DoryGG а убрим не человек она обезьяна! ну бот и хуйня", inline=False)
    await ctx.send(embed=embed)

@Bot.command(pass_context= True)
async def свадьба(ctx):
    embed = discord.Embed(title="Расписание свадеб", description="В этом списке вы найдёте время и датут свадеб​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0x5adb7c)
    embed.add_field(name="**Свадьба**", value="убрима и БЛАККУРТАЧКИИИИ 22.05.2020 в 18:00", inline=False)
    embed.add_field(name="**Свадьба**", value="Утки и Революционера 22.05.2020 в 19:00", inline=False)
    embed.add_field(name="**Свадьба**", value="Твентезера и бон завтра в 18:00", inline=False)
    embed.add_field(name="**Свадьба**", value="Эстола и Ангелочки будет тогда когда она будет", inline=False)
    embed.add_field(name="**под каблуком**", value="мафиозник у риверсонк! чё могу сказать помянем", inline=False)
    await ctx.send(embed=embed)

@Bot.command()
async def ава(ctx, member: discord.Member):
    await ctx.send('{}'.format(member.avatar_url))




token = os.environ.get('TOKEN')
Bot.run(token)
