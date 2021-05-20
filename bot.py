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




user = fake_useragent.UserAgent().random
header = {'user-agent': user}



intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
from discord.ext import commands
Bot = commands.Bot(command_prefix='--', intents=intents)
Bot.remove_command('help')

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name="мой бот сделан при поддержки 1x бет"))
    
@Bot.event
async def on_member_join(member):
    embed = discord.Embed(title=f"Приветствую тебя на сервере {member.guild.name}.⠀​⠀​⠀⠀​⠀​⠀⠀​⠀​⠀⠀​⠀​⠀", description=f"Добро Пожаловать на сервер {member.mention}⠀⠀​​", color=0x00eeff)
    embed.set_image(url="https://t4.ftcdn.net/jpg/03/64/94/67/360_F_364946785_HU0G0WLRpd9SjBxecLAy7En93HmdxbL5.jpg")
    embed.add_field(name="**У нас присутствует замечательный бот**", value="Для просмотра комманд `--commands`", inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    channel = discord.utils.get(member.guild.channels, name = '❗-писать-тут')
    await channel.send(embed=embed)
    
    
@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name = '❗-писать-тут')
    msg = f"{member.mention} съебался нахуй "
    await channel.send(msg)
    


@Bot.command()
async def user_agent(ctx):
    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}
    await ctx.send(header)







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
async def windows10(ctx):
    embed = discord.Embed(title=f"Windows 10 Theme 1/5", description=f"Make your Windows better", color=0x141414)
    download_src = "https://www.youtube.com/watch?v=wzpjnFQ030M&ab_channel=LinkVegasLinkVegas"
    embed.add_field(name='Tutorial' ,value='[Click here to open YT video](' + download_src + ')', inline = False)
    embed.set_image(url="http://i3.ytimg.com/vi/wzpjnFQ030M/maxresdefault.jpg")


    page2 = discord.Embed(title=f"Windows 10 Theme 2/5", description=f"Make your Windows better", color=0x141414)
    page_img = "https://www.youtube.com/watch?v=DRyGOkD9ouU&ab_channel=LinkVegasLinkVegas"
    page2.add_field(name='Tutorial' ,value='[Click here to open YT video](' + page_img + ')', inline = False)
    page2.set_image(url="https://img.youtube.com/vi/DRyGOkD9ouU/maxresdefault.jpg")

    page3 = discord.Embed(title=f"Windows 10 Theme 3/5", description=f"Make your Windows better", color=0x141414)
    page_imfg = "https://www.youtube.com/watch?v=4tvwEISJryY&ab_channel=TanjimTheTechGuyTanjimTheTechGuyBest%C3%A4tigt"
    page3.add_field(name='Tutorial' ,value='[Click here to open YT video](' + page_imfg + ')', inline = False)
    page3.set_image(url="https://img.youtube.com/vi/4tvwEISJryY/maxresdefault.jpg")

    page4 = discord.Embed(title=f"Windows 10 Theme 4/5", description=f"Make your Windows better", color=0x141414)
    page_imfsg = "https://www.youtube.com/watch?v=StnfG80ZvXY&ab_channel=TanjimTheTechGuyTanjimTheTechGuyBest%C3%A4tigt"
    page4.add_field(name='Tutorial' ,value='[Click here to open YT video](' + page_imfsg + ')', inline = False)
    page4.set_image(url="https://img.youtube.com/vi/StnfG80ZvXY/maxresdefault.jpg")

    page5 = discord.Embed(title=f"Windows 10 Theme 5/5", description=f"Make your Windows better", color=0x141414)
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

    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    membercount = str(ctx.guild.member_count)
    roles = str(ctx.guild.roles)
    icon = str(ctx.guild.icon_url)
    server_createt = str(ctx.guild.created_at.strftime("%d.%m.%Y"))


    embed = discord.Embed(title = name + "Server Information", description=description)
    embed.set_thumbnail(url=icon)
    embed.add_field(name= "Owner", value=owner, inline = True)
    embed.add_field(name= "Region", value=region, inline = True)
    embed.add_field(name= "Member Count", value=membercount, inline = True)

    embed.add_field(name= "Server Createt", value=server_createt, inline = True)

    await ctx.send(embed=embed)
    
@Bot.command(aliases = ['wallpaper', 'обои'])
async def __wallpaper(ctx, arg1):
    if arg1 == "help":
        embed = discord.Embed(title=f"Информационный блок команды wallpaper", description=f"", color=0x7d87f5)
        embed.add_field(name='популярные жанры' , value='3D, Abstract, Animals, Anime, Art, Black \n Cars, City, Dark, Fantasy, Flowers, Food \n Holidays, Love, Macro, Nature, Space, Vector', inline = False)
        embed.add_field(name='запрос картинки' , value='--wallpaper `<названия>`')
        embed.set_footer(text=f"Запрос был сделан{ctx.author}", icon_url=ctx.author.avatar_url)
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


        idsr = discord.Embed(title=f"Обои на тему {arg1}", description=f"Надеюсь вам нравится подобранные обои", color=0x141414)
        idsr.add_field(name='Open Image in Browser' ,value='[Click here to open](' + download_src + ')')
        idsr.set_image(url=download_src)


        message = await ctx.send(embed = idsr)
        await message.add_reaction('▶')
        msg = message.id
        print(msg)
        if msg == msg:
            def check(reaction, user):
                return user == ctx.author

            i = 0
            reaction = None

            while True:
                if str(reaction) == '▶':
                    i = 0
                    numbers = re.findall('[0-9]+', images_link)

                    ranger = int(numbers[0])
                    ranger_result = ranger - 1

                    np = random.randint(1, ranger_result)


                    link = f'https://wallpaperscraft.com/search/?order=&page={np}&query={intt}&size=1920x1080'
                    response = requests.get(link).text

                    soup = BeautifulSoup(response, 'lxml')
                    download_block = soup.find('div', class_ = "wallpapers wallpapers_zoom wallpapers_main").find_all('li', class_ = "wallpapers__item")
                    for imagerr in download_block:
                        images_link = imagerr.find('a').get('href')
                        array += [images_link]
                        # img=random.choice(images_link)
                    second_link = f"https://wallpaperscraft.com{choice(array)}"
                    second_response = requests.get(second_link).text
                    second_soup = BeautifulSoup(second_response, 'lxml')
                    download_src = second_soup.find('div', class_ = "wallpaper__placeholder").find('img', class_ = "wallpaper__image").get('src')


                    idsr = discord.Embed(title=f"Обои на тему {arg1}", description=f"используйте ▶ чтобы получить следующую картинку", color=0x141414)
                    idsr.add_field(name='Open Image in Browser' ,value='[Click here to open](' + download_src + ')')
                    idsr.set_image(url=download_src)
                    dfsf = await ctx.fetch_message(msg)
                    await dfsf.edit(embed = idsr)

                try:

                    reaction, user = await Bot.wait_for('reaction_add', timeout = 400.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break







@Bot.command()
async def anime(ctx, *args):
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


        idsr = discord.Embed(title=f"Обои на тему Anime", description=f"Надеюсь вам нравится подобранные обои", color=0x141414)
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
                idsrs = discord.Embed(title=f"Обои на тему Anime", description=f"Надеюсь вам нравится подобранные обои", color=0x141414)
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
async def animes(ctx):
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


        idsr = discord.Embed(title=f"Обои на тему Anime", description=f"Надеюсь вам нравится подобранные обои", color=0x141414)
        idsr.add_field(name='Open Image in Browser' ,value='[Click here to open](' + img_pictur_url + ')')
        idsr.set_image(url=img_pictur_url)
        message = await ctx.send(embed=idsr)
        await message.add_reaction('▶')
        msg = message.id
        print(msg)


        if msg == msg:
            def check(reaction, user):
                return user == ctx.author

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
                    idsrs = discord.Embed(title=f"Обои на тему Anime", description=f"Надеюсь вам нравится подобранные обои", color=0x141414)
                    idsrs.add_field(name='Open Image in Browser' ,value='[Click here to open](' + img_pictur_url + ')')
                    idsrs.set_image(url=img_pictur_url)


                    await message.edit(embed = idsrs)

                try:

                    reaction, user = await Bot.wait_for('reaction_add', check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break


    
    

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
    embed = discord.Embed(title=f"Аватарка {member}", description="", color=0x1780c2)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

token = os.environ.get('TOKEN')
Bot.run(token)
