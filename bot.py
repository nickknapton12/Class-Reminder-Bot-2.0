import discord
import time
import asyncio

from src.db_functions import *
from src.reminder_functions import *

#Reads token from a token.txt file placed in the .src directory. Token should be the token
#given when discord bot is registered and should remane secret at all times!
def read_token():
    with open("./src/token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

# Specifys intent and gives access to all discord members in a server
intents = discord.Intents.default()
intents.members = True

# Setup for Client
client = discord.Client(intents = intents,activity=discord.Activity(type=discord.ActivityType.watching, name="out for you!"))

# OnReady Definition, runs every time bot is started up and ready
@client.event
async def on_ready():
    guild = client.get_guild(802294668913410129)

    for member in guild.members:
        if not member.bot:
            if find_user(member) == None:
                add_user(member)
                send_welcome_message(client, member)
            else:
                send_back_up_message(client, member)
        else:
            print(f"Bot acount: {member.name}")
    print("done setup")

# OnMessage Definition, runs everytime bot detects a message
@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content == "!reminders":
            if type(message.channel) == discord.DMChannel:
                send_user_current_reminders(client, message.author)
            else:
                send_channel_reminders(client, message.channel.name)
        elif message.content[0:6] == "!remind":
            print("")
        

# Starts Bot
client.run(token)