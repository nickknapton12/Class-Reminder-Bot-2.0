import discord
import time
import asyncio

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
            await member.send('Welcome Message')
            print(f"Sending {member.name}")
        else:
            print(f"Bot acount: {member.name}")

# OnMessage Definition, runs everytime bot detects a message
@client.event
async def on_messages(message):
    if message.author != client.user:
        #Should send a list of all current reminders to user based on their subscritptions
        #if in a DM or reminders related to class if in a class related massage
        if message.content == "!reminders":
            print()
        if message.content[0,6] == "!remind":
            print()
        

# Starts Bot
client.run(token)