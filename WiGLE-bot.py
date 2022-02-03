import discord
from discord.ext import commands
import json
import re
import requests

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('WiGLE-bot has awoken')

@client.command()
async def rank(ctx, arg1):
    req = "https://api.wigle.net/api/v2/stats/user?user={}".format(arg1)
    response = requests.get(req, headers={'Authorization': 'Basic WIGLEAPIKEY'}).json()
    badgeID = ("https://wigle.net"+(response['imageBadgeUrl']))
    await ctx.send(badgeID)
    return

client.run('TOKEN')
