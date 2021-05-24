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

fdsf


user = fake_useragent.UserAgent().random
header = {'user-agent': user}



intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)
from discord.ext import commands

Bot = commands.Bot(command_prefix='q.', intents=intents)
Bot.remove_command('help')

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name="q.help v1.0.0"))

data = {}

@Bot.command()
@commands.has_permissions(administrator = True)
async def welcome_channel(ctx, arg1):

    serverid = ctx.guild.id
    serveride = f"{serverid}"
    print(serveride)
    data[serveride] = []
    data[serveride].append({
        'name': arg1,
    })


    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)


    await ctx.send(f"you add welcome message to {arg1} channel")


@Bot.event
async def on_member_join(member):

    embed = discord.Embed(title=f"Welcome to the {member.guild.name} server.⠀​⠀​⠀⠀​⠀​⠀⠀​⠀​⠀⠀​⠀​⠀", description=f"Welcome to server, {member.mention}⠀⠀​​", color=0x00eeff)
    embed.set_image(url="https://t4.ftcdn.net/jpg/03/64/94/67/360_F_364946785_HU0G0WLRpd9SjBxecLAy7En93HmdxbL5.jpg")
    embed.add_field(name="**We have amazing bot**", value="To view commands `--commands`", inline=False)
    embed.set_thumbnail(url=member.avatar_url)

    serverid = member.guild.id
    serveride = f"{serverid}"
    with open('data.txt', 'r') as json_file:
        data = json.load(json_file)
    for p in data[serveride]:
        numin = p['name']
        print(numin)


    channel = discord.utils.get(member.guild.channels, name = numin)
    await channel.send(embed=embed)


@Bot.command()
async def bot_status(ctx):
    servers = len(Bot.guilds)
    ping_ = Bot.latency
    ping =  round(ping_ * 1000)
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
    embed = discord.Embed(title = "Discord Bot QBug Invite ", description="")
    invite_link = "https://discord.com/api/oauth2/authorize?client_id=698494567007387689&permissions=8&scope=bot"
    embed.add_field(name= ":incoming_envelope: Invite link", value='[Click here to invite](' + invite_link + ')', inline = False)

    await ctx.send(embed = embed)



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
    member_count = ctx.guild.member_count
    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    membercount = str(ctx.guild.member_count)
    roles = str(ctx.guild.roles)
    icon = str(ctx.guild.icon_url)
    server_createt = str(ctx.guild.created_at.strftime("%d.%m.%Y"))

    embed = discord.Embed(title = name + "Server Information", description=description)
    embed.set_thumbnail(url=icon)
    embed.add_field(name= ":crown: Owner", value=owner, inline = False)
    embed.add_field(name= ":earth_americas: Region", value=region, inline = False)
    embed.add_field(name= ":busts_in_silhouette: Member Count", value=membercount, inline = False)

    embed.add_field(name= ":construction_site: Server Createt", value=server_createt, inline = False)

    await ctx.send(embed=embed)


@Bot.command(aliases = ['wallpaper', 'обои'])
async def __wallpaper(ctx, arg1):
    if arg1 == "help":
        embed = discord.Embed(title=f"Wallpapers information block ", description=f"", color=0x7d87f5)
        embed.add_field(name='frequent wallpapers' , value='3D, Abstract, Animals, Anime, Art, Black \n Cars, City, Dark, Fantasy, Flowers, Food \n Holidays, Love, Macro, Nature, Space, Vector', inline = False)
        embed.add_field(name='picture request' , value='--wallpaper `<name>`')
        embed.set_footer(text=f"request has done by{ctx.author}", icon_url=ctx.author.avatar_url)
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


        idsr = discord.Embed(title=f"Wallpaper about {arg1}", description=f"Click on the reaction below to scroll to the next picture ", color=0x141414)
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


                idsr = discord.Embed(title=f"Wallpaper about {arg1}", description=f"Click on the reaction below to scroll to the next picture ", color=0x141414)
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
    embed = discord.Embed(title="Anime help", description="Popular tags​", color=0xffc800)
    embed.add_field(name="**popular anime tags **", value="`boobs`,`ass`, `ero`, `Kyonyuu`, `Pussy`, `Megane`, `bdsm`", inline=False)
    await ctx.send(embed = embed)               
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
                idsrs = discord.Embed(title=f"Wallpaper Anime", description=f"Click on the reaction below to scroll to the next picture", color=0x141414)
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




@Bot.event
async def on_command_error(ctx, error):
        embed = discord.Embed(title="Error", description="The discord bot has application error⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xb80208)
        await ctx.send(embed=embed)



@Bot.command(pass_context=True)
async def den4ikpro(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send(file=discord.File('den.jpg'))




@Bot.command()
async def status(ctx, member: discord.Member):
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

    await ctx.send(embed=embed)





@Bot.command()
async def avatar(ctx, member: discord.Member):
    embed = discord.Embed(title=f"Аватарка {member}", description="", color=0x1780c2)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)



token = os.environ.get('TOKEN')
Bot.run(token)
