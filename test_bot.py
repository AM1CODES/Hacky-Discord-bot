  
import json
import discord
import requests
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
            r = requests.get(url)
            result = r.json()
            result1 = {}
            for d in result:
                result1.update(d)
                break
            print(result1)
            try:
                data = parse_data(result1)
                await message.channel.send(embed = hack_message(data))
            except KeyError:
                await message.channel.send(embed = error_message())

client.run(token)