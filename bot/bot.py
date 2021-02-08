from discord.ext import commands, tasks
from discord import Member
import discord
import re
import json 
import time 
import random
import asyncio
import requests
import os
import datetime

# local import
from config import dev, prod
from investing import wrangle_data

message2 = 'strikes marked with * means good value'

client = commands.Bot(command_prefix=',')

@client.command()
async def test(ctx):
    await ctx.send('testing')
    pass

@client.event
async def on_ready():
    print(client.user.name)

## default calliebot
@client.command()
async def get(ctx, *arg): # <--- *arg stores arguments as tuples. Check print statements to see how it works
    print('in get')
    print(arg) # <--- tuple. access tuple like a list/array 
    if arg and len(arg) == 1:
        param = arg[0]
        data = wrangle_data()
        future = data[param] 
        if '-' in str(future['change']):
            message = f"**{future['name']}** -> `{future['last']}` `{future['change']}` `{future['change%']}`"
        else:
            message = f"**{future['name']}** -> `{future['last']}` `+{future['change']}` `{future['change%']}`"
        await ctx.send(message)

@client.command()
async def getlist(ctx, *arg):
    print('in get list')
    data = wrangle_data()
    message = list(data.keys())
    await ctx.send(message)


client.run(prod)