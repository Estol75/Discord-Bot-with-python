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
    
role_id = 642315518644060161

@Bot.command(pass_context=True)
async def test(ctx):

    role = get(ctx.guild.roles, id=role_id)
    await ctx.author.add_roles(role)
    
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
