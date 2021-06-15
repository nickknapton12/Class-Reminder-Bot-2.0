from os import name
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
                await send_back_up_message(client, member)
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
            if matches.__len__() == 7:
                rem_id = add_requested_reminder(matches[1],matches[2],matches[3],matches[4],matches[5],matches[6])
                channel = await client.fetch_channel(reminder_request_channel)
                response = await channel.send(f"{rem_id}\nClass: {matches[1]}\nReminder: {matches[2]}\nMonth: {matches[3]}\nDay: {matches[4]}\nHour: {matches[5]}\nMinute: {matches[6]}")
                await response.add_reaction("☑️")
                await response.add_reaction("❌")
            else:
                response = discord.Embed(title="Wrong Format", description="Hey! Sorry but your submitted reminder seems to be incorrect, try resubmitting!")
                await message.author.send(embed=response)

        elif message.content == "!help":
            response = discord.Embed(title="Commands", description="Here is a list of commands you can use, any other questions should be sent to the creator @CoronaTime")
            response.add_field(name="!reminders", value="Sends all the current reminders for your classes, or if sent in a class channel, the reminders specific for that class!", inline=False)
            response.add_field(name="Add Classes", value="See pinned message in your DM with CoronaTime BOT", inline=False)


@client.event
async def on_raw_reaction_add(payload):
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if payload.user_id != client.user.id:
        if message.author == client.user:
            if sign_up_message(payload.message_id):
                if payload.emoji.name == "0️⃣":
                    add_class(payload.user_id, major_classes[0])
                if payload.emoji.name == "1️⃣":
                    add_class(payload.user_id, major_classes[1])
                if payload.emoji.name == "2️⃣":
                    add_class(payload.user_id, major_classes[2])
                if payload.emoji.name == "3️⃣":
                    add_class(payload.user_id, major_classes[3])
                if payload.emoji.name == "4️⃣":
                    add_class(payload.user_id, minor_classes[0])
                if payload.emoji.name == "5️⃣":
                    add_class(payload.user_id, minor_classes[1])
                if payload.emoji.name == "6️⃣":
                    add_class(payload.user_id, minor_classes[2])
                if payload.emoji.name == "7️⃣":
                    add_class(payload.user_id, minor_classes[3])
                if payload.emoji.name == "8️⃣":
                    add_class(payload.user_id, minor_classes[4])
            elif payload.channel_id == int(reminder_request_channel):
                if payload.emoji.name == "☑️":
                    parts = re.split("\n", message.content)
                    approve_reminder(parts[0])
                    await message.delete()
                if payload.emoji.name == "❌":
                    parts = re.split("\n", message.content)
                    delete_reminder(parts[0])
                    await message.delete()
            else:
                if payload.emoji.name == "☑️":
                    await message.delete()


# Starts Bot
client.run(token)