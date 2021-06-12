import discord

# Should query db for all reminders and users, cache them, then go through
# all users and send their reminders. Could store reminders in hashmap and
# when looping through users, just search for each reminder the user is subed
# to making only one loop necassary.
def send_morning_reminders(client):
    print("")

# Sends a welcome message to a new user
def send_welcome_message(client, user):
    print("")

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
def add_reminder(the_class, the_reminder, month, day, hour, minute):
    print("")