import discord
from discord.ext import commands
import os


Bot = commands.Bot(command_prefix= "!")

@Bot.event
async def on_ready():
    print("The Bot is ready")


@Bot.command(pass_context=True) #разрешаем передавать агрументы
async def test(ctx): #создаем асинхронную фунцию бота
    await ctx.send("2") #отправляем обратно аргумент

token = os.environ.get('TOKEN')
Bot.run(token)
