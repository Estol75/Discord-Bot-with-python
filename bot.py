import discord
from discord.ext import commands
import os


Bot = commands.Bot(command_prefix= "--")

@Bot.event
async def on_ready():
    await Bot.change_presence(status=discord.Status.idle, activity=discord.Game('--com | Все команды'))
    print("The Bot is ready")

text = ('**Вот тебе полезные координаты:**\r\n'
                  '```Ферма скелетов (По метро): -7844 -5753```'
                  '```Ферма гвардов (по метро): -8000 -6435```'
                  '```Ферма золота и яма: -7777 -6460```'
                  '```Ферма зомби и пауков (По метро): -7430 -5895```'
                  '```Городская ферма ифритов (В аду): -1200 -630```'
                  '```Портал в энд (В аду): -1100 -950```'
                  '```Портал в Техноград (В аду): -918 -750```'
                  '```Портал в хаб Технограда: -7400 -6085```'
                  '```Склад: -7470 -6015```')

@Bot.command(pass_context=True)
async def корды(ctx):
    await ctx.send(text)
    
@Bot.command(pass_context=True)
async def rjhls(ctx):
    await ctx.send(text)
    
@Bot.command(pass_context=True)
async def ФАШИСТЫ(ctx):
    await ctx.send("КТО ФАШИСТ ГДЕ ФАШИСТ ТЫ ФАШИСТ У СУКА")
    

@Bot.command(pass_context=True)
async def бог(ctx):
    await ctx.send(file=discord.File('putin.jpg'))
    
@Bot.command(pass_context=True)
async def дааашка(ctx):
    await ctx.send(file=discord.File('daska.png'))

@Bot.command(pass_context= True)
async def com(ctx):
    embed = discord.Embed(title="Техноград Бот", description="Tут вы найдёте все команды бота​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀​⠀​⠀⠀​​⠀​⠀⠀​⠀​⠀​⠀​⠀​⠀⠀​", color=0xeee657)
    embed.add_field(name="**Команда что бы посмотреть все координаты:**", value="--корды", inline=False)
    embed.add_field(name="**Если нужны команды бота:**", value="--com", inline=False)
    embed.add_field(name="**Посмотреть аватарку игрока в дискорде:**", value="--ава @ник", inline=False)
    embed.add_field(name="Author", value="Estol", inline=False)
    mess = await ctx.send(embed=embed)
    await mess.add_reaction('👍🏻')
    await mess.add_reaction('👎🏻')
    
@Bot.command()
async def ава(ctx, member: discord.Member):
    await ctx.send('{}'.format(member.avatar_url))

    

token = os.environ.get('TOKEN')
Bot.run(token)
