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

cluster = MongoClient("mongodb://Estol:JWTZW7UrQSeTFYVY@cluster0-shard-00-00.bjidh.mongodb.net:27017,cluster0-shard-00-01.bjidh.mongodb.net:27017,cluster0-shard-00-02.bjidh.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-12d4np-shard-0&authSource=admin&retryWrites=true&w=majority")

db = cluster["discord"]
collection = db["data"]

@Bot.command()
async def test(ctx):
    guild_id = str(ctx.guild.id)
    serverid = guild_id
    serveride = f"{serverid}"

    # PASS = os.environ.get('PASSW')


    db = cluster["discord"]
    collection = db["data"]

    post = {"_id": serveride, "name": "en"}

    collection.insert_one(post)


@Bot.command()
async def change(ctx, arg1):
    guild_id = str(ctx.guild.id)
    serverid = guild_id
    serveride = f"{serverid}"
    result = collection.update_one({"_id": serveride}, {"$set": {"name": arg1}})


@Bot.command()
async def lag(ctx):
    await ctx.send("lagaet")

token = os.environ.get('TOKEN')
Bot.run(token)
