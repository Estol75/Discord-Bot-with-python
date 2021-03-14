import discord
from discord.ext import commands
import os
from discord.utils import get
import sqlite3

Bot = commands.Bot(command_prefix= "--")
Bot.remove_command('help')

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game('--help | Все команды'))
    print("The Bot is ready")

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


fdsfdsf = 642285642348494848
@Bot.command()
@commands.has_role(642306802461048833)
async def leninn_gay(ctx):
    await ctx.channel.purge(limit = 1)
    red2ffs = get(ctx.guild.roles, id=fdsfdsf)
    await ctx.author.add_roles(red2ffs)
    
    
lenin = 673856663299817472
@Bot.command()
@commands.has_role(642306802461048833)
async def lenin_gay(ctx):
    await ctx.channel.purge(limit = 1)
    red2s = get(ctx.guild.roles, id=lenin)
    await ctx.author.add_roles(red2s)


lener = 673856663299817472
@Bot.command(pass_context=True)
@commands.has_role(642306802461048833)
async def remove_gay(ctx):
    await ctx.channel.purge(limit = 1)
    rolge = get(ctx.guild.roles, id=lener)
    await ctx.author.remove_roles(rolge)


@Bot.event
async def on_command_error(ctx, error):
        embed = discord.Embed(title="ОШИБКА", description="Извините но такая команда не найдена⠀⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xb80208)
        await ctx.send(embed=embed)

redstone = 642315599237742612
redstone_1 = 668166643633094656
@Bot.command()
@commands.has_role(642285642348494848)
async def редстоунер_1(ctx):
    await ctx.channel.purge(limit = 1)
    reds = get(ctx.guild.roles, id=redstone)
    redst = get(ctx.guild.roles, id=redstone_1)
    await ctx.author.add_roles(reds, redst)

redstone = 642315599237742612
redstone_2 = 668168891880439848
@Bot.command()
@commands.has_role(642285642348494848)
async def редстоунер_2(ctx):
    await ctx.channel.purge(limit = 1)
    redstonplay = get(ctx.guild.roles, id=redstone)
    redstonepla = get(ctx.guild.roles, id=redstone_2)
    await ctx.author.add_roles(redstonplay, redstonepla)



viloze = 642306802461048833
@Bot.command()
@commands.has_role(707212021791326241)
async def sendte(ctx):
    await ctx.channel.purge(limit = 1)
    gdfgdfgdfg = get(ctx.guild.roles, id=viloze)
    await ctx.author.add_roles(gdfgdfgdfg)



redstone = 642315599237742612
redstone_3 = 668168889619709952
@Bot.command()
@commands.has_role(642285642348494848)
async def редстоунер_3(ctx):
    await ctx.channel.purge(limit = 1)
    redstonelay = get(ctx.guild.roles, id=redstone)
    redstonela = get(ctx.guild.roles, id=redstone_3)
    await ctx.author.add_roles(redstonelay, redstonela)

redstone = 642315599237742612
redstone_1 = 668166643633094656
redstone_2 = 668168891880439848
redstone_3 = 668168889619709952
@Bot.command()
@commands.has_role(642285642348494848)
async def редстоунер_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    lay = get(ctx.guild.roles, id=redstone)
    lay3 = get(ctx.guild.roles, id=redstone_1)
    lay2 = get(ctx.guild.roles, id=redstone_2)
    lay1 = get(ctx.guild.roles, id=redstone_3)
    await ctx.author.remove_roles(lay, lay3, lay2, lay1)

@Bot.command()
async def join(ctx):
    channelf = ctx.author.voice.channel
    await channelf.connect()
@Bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
#-----------------------------------------------------------------------
farmer = 642315689151037441
farmer_1 = 668156282003521536
@Bot.command()
@commands.has_role(642285642348494848)
async def фермер_1(ctx):
    await ctx.channel.purge(limit = 1)
    farme = get(ctx.guild.roles, id=farmer)
    farmer = get(ctx.guild.roles, id=farmer_1)
    await ctx.author.add_roles(farme, farmer)

farmer = 642315689151037441
farmer_2 = 668156648535097344
@Bot.command()
@commands.has_role(642285642348494848)
async def фермер_2(ctx):
    await ctx.channel.purge(limit = 1)
    farmerlay = get(ctx.guild.roles, id=farmer)
    farmerli = get(ctx.guild.roles, id=farmer_2)
    await ctx.author.add_roles(farmerlay, farmerli)

farmer = 64215689151037441
farmer_3 = 668156467488227388
@Bot.command()
@commands.has_role(642285642348494848)
async def фермер_3(ctx):
    await ctx.channel.purge(limit = 1)
    farmerpla = get(ctx.guild.roles, id=farmer)
    farmerplayl = get(ctx.guild.roles, id=farmer_3)
    await ctx.author.add_roles(farmerpla, farmerplayl)

farmer = 642315689151037441
farmer_1 = 668156282003521536
farmer_2 = 668156648535097344
farmer_3 = 668156467488227388
@Bot.command()
@commands.has_role(642285642348494848)
async def фермер_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    farmerrel = get(ctx.guild.roles, id=farmer)
    farmerlil = get(ctx.guild.roles, id=farmer_1)
    farmirt = get(ctx.guild.roles, id=farmer_2)
    farmerlayli = get(ctx.guild.roles, id=farmer_3)
    await ctx.author.remove_roles(farmerrel, farmerlil, farmirt, farmerlayli)
#----------------------------------------------------------------------
build = 642315657102229504
build_1 = 668166512426876946
@Bot.command()
@commands.has_role(642285642348494848)
async def строитель_1(ctx):
    await ctx.channel.purge(limit = 1)
    buildlay = get(ctx.guild.roles, id=build)
    buildtr = get(ctx.guild.roles, id=build_1)
    await ctx.author.add_roles(buildlay, buildtr)

build = 642315657102229504
build_2 = 668166688985972767
@Bot.command()
@commands.has_role(642285642348494848)
async def строитель_2(ctx):
    await ctx.channel.purge(limit = 1)
    buildpip = get(ctx.guild.roles, id=build)
    buildpila = get(ctx.guild.roles, id=build_2)
    await ctx.author.add_roles(buildpip, buildpila)

build = 642315657102229504
build_3 = 668166943533957120
@Bot.command()
@commands.has_role(642285642348494848)
async def строитель_3(ctx):
    await ctx.channel.purge(limit = 1)
    buildlepr = get(ctx.guild.roles, id=build)
    buildtrz = get(ctx.guild.roles, id=build_3)
    await ctx.author.add_roles(buildlepr, buildtrz)

build = 642315657102229504
build_1 = 668166512426876946
build_2 = 668166688985972767
build_3 = 668166943533957120
@Bot.command()
@commands.has_role(642285642348494848)
async def строитель_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    buildrt = get(ctx.guild.roles, id=build)
    buildfgh = get(ctx.guild.roles, id=build_1)
    buildlop = get(ctx.guild.roles, id=build_2)
    buildghtfs = get(ctx.guild.roles, id=build_3)
    await ctx.author.remove_roles(buildrt, buildfgh, buildlop, buildghtfs)
#----------------------------------------------------------------------------------
dekor =642315763398737931
dekor_1 = 668152257560313896
@Bot.command()
@commands.has_role(642285642348494848)
async def декоратор_1(ctx):
    await ctx.channel.purge(limit = 1)
    dekorat = get(ctx.guild.roles, id=dekor)
    dekorlipe = get(ctx.guild.roles, id=dekor_1)
    await ctx.author.add_roles(dekorat, dekorlipe)

dekor =642315763398737931
dekor_2 = 668152395020238857
@Bot.command()
@commands.has_role(642285642348494848)
async def декоратор_2(ctx):
    await ctx.channel.purge(limit = 1)
    dekotzuf = get(ctx.guild.roles, id=dekor)
    dekorfds = get(ctx.guild.roles, id=dekor_2)
    await ctx.author.add_roles(dekotzuf, dekorfds)

dekor =642315763398737931
dekor_3 = 668155885305987112
@Bot.command()
@commands.has_role(642285642348494848)
async def декоратор_3(ctx):
    await ctx.channel.purge(limit = 1)
    dekofdsfr = get(ctx.guild.roles, id=dekor)
    dssdersd = get(ctx.guild.roles, id=dekor_3)
    await ctx.author.add_roles(dekofdsfr, dssdersd)

dekor =642315763398737931
dekor_1 = 668152257560313896
dekor_2 = 668152395020238857
dekor_3 = 668155885305987112
@Bot.command()
@commands.has_role(642285642348494848)
async def декоратор_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    dekofsdr = get(ctx.guild.roles, id=dekor)
    dekorzzztr = get(ctx.guild.roles, id=dekor_1)
    dekoroikoi = get(ctx.guild.roles, id=dekor_2)
    üplöüp = get(ctx.guild.roles, id=dekor_3)
    await ctx.author.remove_roles(dekofsdr, dekorzzztr, dekoroikoi, üplöüp)
#------------------------------------------------------------------------------
item = 642315552890814464
item_1 = 668156985920716830
@Bot.command()
@commands.has_role(642285642348494848)
async def ресурсер_1(ctx):
    await ctx.channel.purge(limit = 1)
    itefdstd = get(ctx.guild.roles, id=item)
    itemgdfg = get(ctx.guild.roles, id=item_1)
    await ctx.author.add_roles(itefdstd, itemgdfg)

item = 642315552890814464
item_2 = 668166015464505344
@Bot.command()
@commands.has_role(642285642348494848)
async def ресурсер_2(ctx):
    await ctx.channel.purge(limit = 1)
    itefdsm = get(ctx.guild.roles, id=item)
    itefdsfsdf = get(ctx.guild.roles, id=item_2)
    await ctx.author.add_roles(itefdsm, itefdsfsdf)

item = 642315552890814464
item_3 = 668166087963312161
@Bot.command()
@commands.has_role(642285642348494848)
async def ресурсер_3(ctx):
    await ctx.channel.purge(limit = 1)
    itefdsfdsm = get(ctx.guild.roles, id=item)
    itfdsfsdf = get(ctx.guild.roles, id=item_3)
    await ctx.author.add_roles(itefdsfdsm, itfdsfsdf)

item = 642315552890814464
item_1 = 668156985920716830
item_2 = 668166015464505344
item_3 = 668166087963312161
@Bot.command()
@commands.has_role(642285642348494848)
async def ресурсер_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    itefdsfm = get(ctx.guild.roles, id=item)
    itemggggfff = get(ctx.guild.roles, id=item_1)
    igdfgdfgdfgdfttt = get(ctx.guild.roles, id=item_2)
    hhhhhhhgffffd = get(ctx.guild.roles, id=item_3)
    await ctx.author.remove_roles(itefdsfm, itemggggfff, igdfgdfgdfgdfttt, hhhhhhhgffffd)
#------------------------------------------------------------------
shema = 649217280617480202,
@Bot.command()
@commands.has_role(642285642348494848)
async def схематика(ctx):
    await ctx.channel.purge(limit = 1)
    shfdsema = get(ctx.guild.roles, id=shema)
    await ctx.author.add_roles(shfdsema)

shema = 649217280617480202
@Bot.command()
@commands.has_role(642285642348494848)
async def схематика_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    shefdma = get(ctx.guild.roles, id=shema)
    await ctx.author.remove_roles(shefdma)

pod = 706574774075260948
@Bot.command()
@commands.has_role(642285642348494848)
async def подкидыш_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    podfs = get(ctx.guild.roles, id=pod)
    await ctx.author.remove_roles(podfs)
#---------------------------------------
rep = 642315518644060161
@Bot.command()
@commands.has_role(642285642348494848)
async def рпшер(ctx):
    await ctx.channel.purge(limit = 1)
    rephh = get(ctx.guild.roles, id=rep)
    await ctx.author.add_roles(rephh)
rep = 642315518644060161
@Bot.command()
@commands.has_role(642285642348494848)
async def рпшер_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    repfdg = get(ctx.guild.roles, id=rep)
    await ctx.author.remove_roles(repfdg)

@Bot.command(pass_context=True)
async def Revolycioner_Rab(ctx):
    await ctx.send(file=discord.File('revo.jpg'))

@Bot.command(pass_context=True)
async def den4ikpro(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send(file=discord.File('den.jpg'))


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
@commands.has_role(622213645610254336)
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)

@Bot.command(pass_context = True)
@commands.has_role(642306802461048833)
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
async def даун(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send(file=discord.File('gdfgdfg.mp4'))


@Bot.command(pass_context= True)
async def help(ctx):
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





connction = sqlite3.connect('server.db')
cursor = connction.cursor()

@Bot.event
async def on_ready():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        id INT,
        cash BIGINT,
        rep INT,
        lvl INT
    )""")
    connction.commit()

    for guild in Bot.guilds:
        for member in guild.members:
            if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
                cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0 , 0, 1)")
            else:
                pass
    connction.commit()
    print('Bot connected')

@Bot.event
async def on_member_join(member):
    if cursor.execute(f"SELECT is FROM user WHERE id = {member.id}").fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0 , 0, 1)")
        connction.commit()
    else:
        pass


@Bot.command(aliases = ['balance', 'cash'])
async def __balance(ctx,member: discord.Member = None):
    if member is None:
        await ctx.send(embed = discord.Embed(
        description = f"""Баланс пользователя **{ctx.author}** составляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]}** тенге""",color=0xfcec03
        ))
    else:
        await ctx.send(embed = discord.Embed(
        description = f"""Баланс пользователся **{member}** составляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(member.id)).fetchone()[0]}** тенге""",color=0xfcec03
        ))

@Bot.command(aliases = ['set'])
@commands.has_role(622213645610254336)
async def __award(ctx, member: discord.Member = None, amount: int = None):
    if member is None:
        await ctx.send(f"**{ctx.author}**, укажите пользователя, которому желайте выдать определенную сумму")
    else:
        if amount is None:
            await ctx.send(f"***{ctx.author}, укажите сумму, которую желайте начислить на счет пользователя")
        elif amount < 1:
            await ctx.send(f"**{ctx.author}**, укажите сумму больше 1")
        else:
            cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(amount, member.id))
            connction.commit()

            await ctx.message.add_reaction('✅')

amountt = 200
frozent = 642315871448072203
@Bot.command(aliases = ['frozen'])
@commands.has_role(642285642348494848)
async def __frozen(ctx):
    if 200 > cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]:
        await ctx.send("Извините сэр но вы бомж")
    else:
        cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(amountt, ctx.author.id))
        connction.commit()
        frozen = get(ctx.guild.roles, id=frozent)
        await ctx.author.add_roles(frozen)
        await ctx.message.add_reaction('✅')



revfrozen = 642315871448072203
@Bot.command()
@commands.has_role(642285642348494848)
async def rev_frozen(ctx):
    await ctx.channel.purge(limit = 1)
    frozerev = get(ctx.guild.roles, id=revfrozen)
    await ctx.author.remove_roles(frozerev)



@Bot.command(aliases = ['rev_cash'])
@commands.has_role(642285249136689152)
async def __rev_cash(ctx, member: discord.Member = None, amount: int = None):
    if member is None:
        await ctx.send(f"**{ctx.author}**, укажите пользователя, которому желайте украсть определенную сумму")
    else:
        if amount is None:
            await ctx.send(f"***{ctx.author}, укажите сумму, которую желайте украсть с счета пользователя")

        else:
            cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(amount, member.id))
            connction.commit()

            await ctx.message.add_reaction('✅')










@Bot.command()
@commands.has_role(642306802461048833)
async def warn(ctx, member: discord.Member, arg):
    embed = discord.Embed(title=(f'{member.name }, был выдан варн игроком {ctx.author.name} причина: '+ arg), description="⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0x5adb7c)
    await member.send( f'{member.name }, Вам был кинут варн игроком, {ctx.author.name} содержание, '+ arg)
    await ctx.send(embed=embed)


token = os.environ.get('TOKEN')
Bot.run(token)
