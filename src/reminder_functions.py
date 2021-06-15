import discord
from src.db_functions import *

major_classes = ["ENSF480","ENCM511","CPSC471","CPSC457"]
minor_classes = ["COMS363", "ENGG209", "ENGG481", "ENGG513", "BMEN401"]

# Should query db for all reminders and users, cache them, then go through
# all users and send their reminders. Could store reminders in hashmap and
# when looping through users, just search for each reminder the user is subed
# to making only one loop necassary.
def send_morning_reminders(client):
    print("")

# Sends a welcome message to a new user with signup info, then caches and saves to db
async def send_welcome_message(client, user):
    message = discord.Embed(title="Welcome To Corona Time Reminders!", description="this is the description\n", colour=discord.Colour.teal())
    message.add_field(name="Major Classes", value="\u200B", inline=False)
    message.add_field(name=major_classes[0], value="2")
    message.add_field(name=major_classes[1], value="3")
    message.add_field(name=major_classes[2], value="4")
    message.add_field(name=major_classes[3], value="4")
    message.add_field(name="\u200B", value="\u200B", inline=False)
    message.add_field(name="Minors and Comp Studies", value="\u200B", inline=False)
    message.add_field(name=minor_classes[0], value="2")
    message.add_field(name=minor_classes[1], value="3")
    message.add_field(name=minor_classes[2], value="4")
    message.add_field(name=minor_classes[3], value="4")
    message.add_field(name=minor_classes[4], value="4")
    message.set_footer(text="\nReminders should be just an aid, don't soley rely on them!")
    message.set_author(name="CoronaTime Bot", icon_url="https://s.barnetnetwork.com/img/t/260/bc_lrs/000055/0000550764.jpg")
    sign_up_message = await user.send(embed=message)
    add_user(user, sign_up_message)

# Sends a "Back Up" to existing users when the bot comes back online.
def send_back_up_message(client, user):
    print("")

# Sends a DM to User with personilized reminders.
def send_user_current_reminders(client, user):
    print("")

# Sends a message of all the current reminders specific to the channel.
def send_channel_reminders(client, channel):
    print("")

# Adds a reminder to the db
def request_reminder(the_class, the_reminder, month, day, hour, minute):
    print("")