import discord
import time
import asyncio
import re

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
intents.messages

# Setup for Client
client = discord.Client(intents = intents,activity=discord.Activity(type=discord.ActivityType.watching, name="out for you!"))

# OnReady Definition, runs every time bot is started up and ready
@client.event
async def on_ready():
    guild = client.get_guild(802294668913410129)
    for member in guild.members:
        if not member.bot:
            if find_user_by_id(member.id) == None:
                await send_welcome_message(client, member)
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

        elif message.content[0:7] == "!remind":
            matches = re.split("\s", message.content)
            print(matches.__len__())
            if matches.__len__() == 7:
                request_reminder(matches[1], matches[2], matches[3], matches[4], matches[5], matches[6])
            else:
                await message.author.send("Please correct the format")


@client.event
async def on_raw_reaction_add(payload):
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    if message.author == client.user:
        if sign_up_message(payload.message_id):
            if payload.emoji.name == "0️⃣":
                print("0")
            if payload.emoji.name == "1️⃣":
                print("1")
            if payload.emoji.name == "2️⃣":
                print("2")
            if payload.emoji.name == "3️⃣":
                print("3")
            if payload.emoji.name == "4️⃣":
                print("4")
            if payload.emoji.name == "5️⃣":
                print("5")
            if payload.emoji.name == "6️⃣":
                print("6")
            if payload.emoji.name == "7️⃣":
                print("7")
            if payload.emoji.name == "8️⃣":
                print("8")
            if payload.emoji.name == "9️⃣":
                print("9")
        else:
            if payload.emoji.name == "☑️":
                await message.delete()


# Starts Bot
client.run(token)