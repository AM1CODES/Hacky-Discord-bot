import discord
from discord.embeds import Embed

color = 0xFF6500
key_features = {
    'name' : 'Name',
    'website':'Website',
    'start': 'Start Time',
    'end': 'End Time',
    'city': 'City',
    'state':'State',
    'country': 'Country',
    'virtual':'Virtual Hack?',
    'mlhAssociated':'MLH Partnered?'
}

def parse_data(data):
    del data['id']
    del data['createdAt']
    del data['logo']
    del data['banner']
    del data['countryCode']
    del data['latitude']
    del data['longitude']
    return data

def hack_message(data):
    message = discord.Embed(
        title = f"Hack Club Hackthon Details",
        description = "Here is the data for all the hackathons that are currently live on The Hack Club",
        color = color
    )
    for key in data:
        message.add_field(
            name = key_features[key],
            value= str(data[key]),
            inline = False
        )
    return message

def error_message():
    return discord.Embed(
        title = "Error",
        description = "Sorry an error occured",
        color  = color
    )

