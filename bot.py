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
intents.guilds = True

client = discord.Client(intents=intents)
from discord.ext import commands

Bot = commands.Bot(command_prefix='q.', intents=intents)
Bot.remove_command('help')

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name="q.help v1.0.4"))


@Bot.event
async def on_guild_join(guild):
    with open('lang.txt', 'r') as f:
        data = json.load(f)
        guild_id = str(guild.id)
        serverid = guild_id
        serveride = f"{serverid}"
        print(serveride)
        data[serveride] = []
        data[serveride].append({
            'name': "en",
        })

        with open('lang.txt', 'w') as outfile:
            json.dump(data, outfile)


@Bot.command()
async def test(ctx):
    user_serv_id = f"{ctx.guild.id}"
    with open('lang.txt') as json_file:
        data = json.load(json_file)
    for p in data[user_serv_id]:
        numin = p['name']

    if numin == "ru":
        await ctx.send("russian")
    else:
        await ctx.send("english")





token = os.environ.get('TOKEN')
Bot.run(token)
