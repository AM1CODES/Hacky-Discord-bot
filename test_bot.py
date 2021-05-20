import json
import discord
import requests
from pprint import pprint
from info import *

token = 'BOT_TOKEN'
client = discord.Client()

command_prefix = "!hackclub"

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = '!hackclub'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
            url = 'https://hackathons.hackclub.com/api/events/upcoming'
            try:
                data = parse_data(json.loads(requests.get(url).content))
                await message.channel.send(embed = hack_message(data))
            except KeyError:
                await message.channel.send(embed = error_message())

client.run(token)