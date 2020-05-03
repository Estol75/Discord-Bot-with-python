import discord
from discord.ext import commands
import os
from discord.utils import get

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
    mess = await ctx.send(embed=embed)
    
role_id = 642285249136689152

@Bot.command(pass_context=True)
async def test(ctx):
    role = get(ctx.guild.roles, id=role_id)
    await ctx.author.remove_roles(role)


redstone = 642315599237742612,
redstone_1 = 668166643633094656,
redstone_2 = 668168891880439848,
redstone_3 = 668168889619709952,

#farmer ids
farmer = 642315689151037441,
farmer_1 = 668156282003521536,
farmer_2 = 668156648535097344,
farmer_3 = 668156467488227388,
#build ids
build = 642315657102229504,
build_1 = 668166512426876946,
build_2 = 668166688985972767,
build_3 = 668166943533957120,
#decoration ids
dekor =642315763398737931,
dekor_1 = 668152257560313896,
dekor_2 = 668152395020238857,
dekor_3 = 668155885305987112,
# items farmer
item = 642315552890814464,
item_1 = 668156985920716830,
item_2 = 668166015464505344,
item_3 = 668166087963312161,

shema = 649217280617480202,
rep = 642315518644060161


@Bot.command()
@commands.has_role(642285642348494848)
async def Редстоунер_1(ctx):
    await ctx.channel.purge(limit = 1)
    redstone = get(ctx.guild.roles, id=redstone)
    redstone_1 = get(ctx.guild.roles, id=redstone_1)
    await ctx.author.add_roles(redstone, redstone_1)

@Bot.command()
@commands.has_role(642285642348494848)
async def Редстоунер_2(ctx):
    await ctx.channel.purge(limit = 1)
    redstone = get(ctx.guild.roles, id=redstone)
    redstone_2 = get(ctx.guild.roles, id=redstone_2)
    await ctx.author.add_roles(redstone, redstone_2)

@Bot.command()
@commands.has_role(642285642348494848)
async def Редстоунер_3(ctx):
    await ctx.channel.purge(limit = 1)
    redstone = get(ctx.guild.roles, id=redstone)
    redstone_3 = get(ctx.guild.roles, id=redstone_3)
    await ctx.author.add_roles(redstone, redstone_3)

@Bot.command()
@commands.has_role(642285642348494848)
async def редстоунер_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    redstone = get(ctx.guild.roles, id=redstone)
    redstone_1 = get(ctx.guild.roles, id=redstone_1)
    redstone_2 = get(ctx.guild.roles, id=redstone_2)
    redstone_3 = get(ctx.guild.roles, id=redstone_3)
    await ctx.author.remove_roles(redstone, redstone_1, redstone_2, redstone_3)


#-----------------------------------------------------------------------
@Bot.command()
@commands.has_role(642285642348494848)
async def фермер_1(ctx):
    await ctx.channel.purge(limit = 1)
    farmer = get(ctx.guild.roles, id=farmer)
    farmer_1 = get(ctx.guild.roles, id=farmer_1)
    await ctx.author.add_roles(farmer, farmer_1)

@Bot.command()
@commands.has_role(642285642348494848)
async def фермер_2(ctx):
    await ctx.channel.purge(limit = 1)
    farmer = get(ctx.guild.roles, id=farmer)
    farmer_2 = get(ctx.guild.roles, id=farmer_2)
    await ctx.author.add_roles(farmer, farmer_2)

@Bot.command()
@commands.has_role(642285642348494848)
async def фермер_3(ctx):
    await ctx.channel.purge(limit = 1)
    farmer = get(ctx.guild.roles, id=farmer)
    farmer_3 = get(ctx.guild.roles, id=farmer_3)
    await ctx.author.add_roles(farmer, farmer_3)

@Bot.command()
@commands.has_role(642285642348494848)
async def фермер_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    farmer = get(ctx.guild.roles, id=farmer)
    farmer_1 = get(ctx.guild.roles, id=farmer_1)
    farmer_2 = get(ctx.guild.roles, id=farmer_2)
    farmer_3 = get(ctx.guild.roles, id=farmer_3)
    await ctx.author.remove_roles(farmer, farmer_1, farmer_2, farmer_3)
#----------------------------------------------------------------------
@Bot.command()
@commands.has_role(642285642348494848)
async def строитель_1(ctx):
    await ctx.channel.purge(limit = 1)
    build = get(ctx.guild.roles, id=build)
    build_1 = get(ctx.guild.roles, id=build_1)
    await ctx.author.add_roles(redstone, build_1)

@Bot.command()
@commands.has_role(642285642348494848)
async def строитель_2(ctx):
    await ctx.channel.purge(limit = 1)
    build = get(ctx.guild.roles, id=build)
    build_2 = get(ctx.guild.roles, id=build_2)
    await ctx.author.add_roles(build, build_2)

@Bot.command()
@commands.has_role(642285642348494848)
async def строитель_3(ctx):
    await ctx.channel.purge(limit = 1)
    build = get(ctx.guild.roles, id=build)
    build_3 = get(ctx.guild.roles, id=build_3)
    await ctx.author.add_roles(build, build_3)

@Bot.command()
@commands.has_role(642285642348494848)
async def строитель_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    build = get(ctx.guild.roles, id=build)
    build_1 = get(ctx.guild.roles, id=build_1)
    build_2 = get(ctx.guild.roles, id=build_2)
    build_3 = get(ctx.guild.roles, id=build_3)
    await ctx.author.remove_roles(build, build_1, build_2, build_3)
#----------------------------------------------------------------------------------
@Bot.command()
@commands.has_role(642285642348494848)
async def декоратор_1(ctx):
    await ctx.channel.purge(limit = 1)
    dekor = get(ctx.guild.roles, id=dekor)
    dekor_1 = get(ctx.guild.roles, id=dekor_1)
    await ctx.author.add_roles(dekor, dekor_1)

@Bot.command()
@commands.has_role(642285642348494848)
async def декоратор_2(ctx):
    await ctx.channel.purge(limit = 1)
    dekor = get(ctx.guild.roles, id=dekor)
    dekor_2 = get(ctx.guild.roles, id=dekor_2)
    await ctx.author.add_roles(dekor, dekor_2)

@Bot.command()
@commands.has_role(642285642348494848)
async def декоратор_3(ctx):
    await ctx.channel.purge(limit = 1)
    dekor = get(ctx.guild.roles, id=dekor)
    dekor_3 = get(ctx.guild.roles, id=dekor_3)
    await ctx.author.add_roles(dekor, dekor_3)

@Bot.command()
@commands.has_role(642285642348494848)
async def декоратор_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    dekor = get(ctx.guild.roles, id=dekor)
    dekor_1 = get(ctx.guild.roles, id=dekor_1)
    dekor_2 = get(ctx.guild.roles, id=dekor_2)
    dekor_3 = get(ctx.guild.roles, id=dekor_3)
    await ctx.author.remove_roles(dekor, dekor_1, dekor_2, dekor_3)
#------------------------------------------------------------------------------
@Bot.command()
@commands.has_role(642285642348494848)
async def ресурсер_1(ctx):
    await ctx.channel.purge(limit = 1)
    item = get(ctx.guild.roles, id=item)
    item_1 = get(ctx.guild.roles, id=item_1)
    await ctx.author.add_roles(item, item_1)

@Bot.command()
@commands.has_role(642285642348494848)
async def ресурсер_2(ctx):
    await ctx.channel.purge(limit = 1)
    item = get(ctx.guild.roles, id=item)
    item_2 = get(ctx.guild.roles, id=item_2)
    await ctx.author.add_roles(item, item_2)

@Bot.command()
@commands.has_role(642285642348494848)
async def ресурсер_3(ctx):
    await ctx.channel.purge(limit = 1)
    item = get(ctx.guild.roles, id=item)
    item_3 = get(ctx.guild.roles, id=item_3)
    await ctx.author.add_roles(item, item_3)

@Bot.command()
@commands.has_role(642285642348494848)
async def ресурсер_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    item = get(ctx.guild.roles, id=item)
    item_1 = get(ctx.guild.roles, id=item_1)
    item_2 = get(ctx.guild.roles, id=item_2)
    item_3 = get(ctx.guild.roles, id=item_3)
    await ctx.author.remove_roles(item, item_1, item_2, item_3)
#-------------------------------------------------------------------
@Bot.command()
@commands.has_role(642285642348494848)
async def схематика(ctx):
    await ctx.channel.purge(limit = 1)
    shema = get(ctx.guild.roles, id=shema)
    await ctx.author.add_roles(shema)

@Bot.command()
@commands.has_role(642285642348494848)
async def схематика_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    shema = get(ctx.guild.roles, id=shema)
    await ctx.author.remove_roles(shema)

#---------------------------------------
@Bot.command()
@commands.has_role(642285642348494848)
async def рпшер(ctx):
    await ctx.channel.purge(limit = 1)
    rep = get(ctx.guild.roles, id=rep)
    await ctx.author.add_roles(rep)

@Bot.command()
@commands.has_role(642285642348494848)
async def рпшер_удалить(ctx):
    await ctx.channel.purge(limit = 1)
    rep = get(ctx.guild.roles, id=rep)
    await ctx.author.remove_roles(rep)
    
@Bot.command(pass_context=True)
async def Revolycioner_Rab(ctx):
    await ctx.send(file=discord.File('revo.jpg'))
    
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
@commands.has_role(642306802461048833)
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
    embed.add_field(name="**Айпи тест сервера**", value="213.32.6.2:25000", inline=False)
    embed.add_field(name="**Собрание**", value="Собрание каждую cоботу через неделю", inline=False)
    embed.add_field(name="**Мэр города на данный момент**", value="Revolycioner_Rab", inline=False)
    await ctx.send(embed=embed)
    
@Bot.command()
async def ава(ctx, member: discord.Member):
    await ctx.send('{}'.format(member.avatar_url))

    

token = os.environ.get('TOKEN')
Bot.run(token)
