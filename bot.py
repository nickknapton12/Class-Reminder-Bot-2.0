import discord
import time
import asyncio

print(discord.__version__)

def read_token():
    with open("./src/token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents,activity=discord.Activity(type=discord.ActivityType.watching, name="out for you!"))

@client.event
async def on_ready():
    guild = client.get_guild(802294668913410129)
    for member in guild.members:
        if not member.bot:
            await member.send('Welcome Message')
            print(f"Sending {member.name}")
        else:
            print(f"Bot acount: {member.name}")


@client.event
async def on_message(message):
    if message.author != client.user:
        #Should send a list of all current reminders to user based on their subscritptions
        #if in a DM or reminders related to class if in a class related massage
        if message.content == "!reminders":
            print()
        if message.content[0,6] == "!remind":
            print()
        

client.run(token)