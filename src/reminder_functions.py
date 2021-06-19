import discord
from datetime import datetime
from src.db_functions import *

major_classes = ["ENSF480","ENCM511","CPSC471","CPSC457"]
minor_classes = ["COMS363", "ENGG209", "ENGG481", "ENGG513", "BMEN401"]

reminder_request_channel = "854207771666153472"

dates = {
    '1': 'Jan',
    '2': 'Feb',
    '3': 'Mar',
    '4': 'Apr',
    '5': 'May',
    '6': 'Jun',
    '7': 'Jul',
    '8': 'Aug',
    '9': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec',
}

# Should query db for all reminders and users, cache them, then go through
# all users and send their reminders. Could store reminders in hashmap and
# when looping through users, just search for each reminder the user is subed
# to making only one loop necassary.
async def send_morning_reminders(client):
    users_return = get_all_users()
    reminders_return = get_all_reminders()
    users = list(users_return)
    reminders = list(reminders_return)

    for user in users:
        the_user = await client.fetch_user(user["_id"])
        message = discord.Embed(title="Your Morning Reminders:")
        reminder_count = 0
        for reminder in reminders:
            if (reminder["Class"].upper()) in (user["classes"]):
                reminder_count += 1
                message.add_field(name=(f"{reminder['Class']} {reminder['Reminder']}"), value=(f"{dates[reminder['Month']]} {reminder['Day']} at {reminder['Hour']}:{reminder['Minute']} {reminder['amOrPm']}"),inline=False)
        if reminder_count == 0:
            message.add_field(name="Nothing coming up!", value="Take a break and have a brew, you deserve it!")
        sent_message = await the_user.send(embed=message)
        await sent_message.add_reaction("☑️")
        update_morning_reminder_count()

                

# Sends a welcome message to a new user with signup info, then caches and saves to db
async def send_welcome_message(client, user):
    sign_up_description = "This is the sign up for CoronaTime's class reminders! \n\nHave you ever found yourself trying to cram for a assignment or test that snuck up on you too fast? \n\nThats where I come in, Daily reminders in the morning via DM of assignments due in the future, tests coming up or any other important events! \n\nSimply react to the classes you are in. Never miss another assignment! \n\nUsers should use the request-reminder channel submit reminders for a class using the specified format. I rely on YOU to submit reminders when you can, do your part! \n\n Type !help for helpful commands and please feel free to DM the creator @CoronaTime if you have any problems or to request new features!!"
    message = discord.Embed(title="Welcome To Corona Time Reminders!", description=sign_up_description, colour=discord.Colour.teal())
    message.add_field(name=major_classes[0], value="React: 0️⃣")
    message.add_field(name=major_classes[1], value="React: 1️⃣")
    message.add_field(name=major_classes[2], value="React: 2️⃣")
    message.add_field(name=major_classes[3], value="React: 3️⃣")
    message.add_field(name=minor_classes[0], value="React: 4️⃣")
    message.add_field(name=minor_classes[1], value="React: 5️⃣")
    message.add_field(name=minor_classes[2], value="React: 6️⃣")
    message.add_field(name=minor_classes[3], value="React: 7️⃣")
    message.add_field(name=minor_classes[4], value="React: 8️⃣")
    message.set_footer(text="Disclamer: This is in no way a substitute for not knowing when things are due. This is only a additional tool to remind you when a class has something due. If you miss an assignment because my bot did not remind you it is in no way my responsibility.")
    message.set_author(name="CoronaTime Bot", icon_url="https://s.barnetnetwork.com/img/t/260/bc_lrs/000055/0000550764.jpg")
    sign_up_message = await user.send(embed=message)
    await sign_up_message.add_reaction("0️⃣")
    await sign_up_message.add_reaction("1️⃣")
    await sign_up_message.add_reaction("2️⃣")
    await sign_up_message.add_reaction("3️⃣")
    await sign_up_message.add_reaction("4️⃣")
    await sign_up_message.add_reaction("5️⃣")
    await sign_up_message.add_reaction("6️⃣")
    await sign_up_message.add_reaction("7️⃣")
    await sign_up_message.add_reaction("8️⃣")
    add_user(user, sign_up_message)
    update_user_count()

# Sends a "Back Up" to existing users when the bot comes back online.
async def send_back_up_message(client, user):
    message = discord.Embed(title="Sorry I was taking a Corona Time!", colour=discord.Colour.teal(), description="I apologize for being down, everyone needs a break every once and a while! On a serious note, this happens every once and a while and could be due to updates, power/internet outages, but most likely because @CoronaTime had one too many and kicked the powerplug! \n\n Again sorry but we are back up again, just react with a ☑️ to delete this!")
    back_up_message = await user.send(embed=message)
    await back_up_message.add_reaction("☑️")

# Sends a DM to User with personilized reminders.
async def send_user_current_reminders(client, user):
    user_info = find_user_by_id(user.id)
    classes = user_info["classes"]
    classes_processed = []
    for x in classes:
        classes_processed.append(x.lower())
    results = get_specific_reminders(classes_processed)
    message = discord.Embed(title="Your Reminders:")
    for docs in results:
        message.add_field(name=(f"{docs['Class']} {docs['Reminder']}"), value=(f"{dates[docs['Month']]} {docs['Day']} at {docs['Hour']}:{docs['Minute']} {docs['amOrPm']}"), inline=False)
    sent_message = await user.send(embed=message)
    await sent_message.add_reaction("☑️")
    update_user_requested_reminder_count()
    
    

# Sends a message of all the current reminders specific to the channel.
async def send_channel_reminders(client, channel):
    results = get_specific_reminders([channel.name])
    message = discord.Embed(title=f"{channel.name.upper()} Reminders:")
    for docs in results:
        message.add_field(name=(f"{docs['Class'].upper()} {docs['Reminder']}"), value=(f"{dates[docs['Month']]} {docs['Day']} at {docs['Hour']}:{docs['Minute']} {docs['amOrPm']}"), inline=False)
    sent_message = await channel.send(embed=message)
    await sent_message.add_reaction("☑️")
    update_user_requested_reminder_count()


# Go's through all reminders and checks if they have past or not.
def check_for_expired_reminders():
    current_month = datetime.now().month
    current_day = datetime.now().day

    reminders = get_all_reminders()

    for reminder in reminders:
        if int(reminder["Month"]) < current_month:
            delete_reminder(reminder["_id"])
        else:
            if int(reminder["Day"]) < current_day:
                delete_reminder(reminder["_id"])