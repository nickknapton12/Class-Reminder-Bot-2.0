# Class-Reminder-Bot-2.0
A discord bot to manage and remind students of upcoming assignments, labs, tests, exams and anything else school related!

Currently has served over **200 students** in my software engineering cohort. and sent **tens of thousands of reminders** to students about upcoming assignments, tasks, exams and quizzes!

Written in Python using [discord.py rewrite](https://discordpy.readthedocs.io/en/rewrite/) and uses a mongoDB database to store reminders, users, and statistics.

## Features
- Sends daily morning reminders to students via discord DMs of all their upcoming assignments, labs, tests, exams etc.
- Users can sign up for specific classes and control which classes they need reminding for and which they don't.
- Users can request the bot for the current reminders at any point and the bot will send a tailored response, depending on where the message was sent.
- Users can request current reminders at any time, tailored responses depending if requested in a DM or a class specific channel.
- Collects info relating to how many users are signed up, how many reminders have been sent, etc.

## Commands
`!reminders`

- If sent in a DM to the bot, this will return a list of all reminders for each class the user has signed up for. <br>
- If sent in a Class channel, it will send a list of all reminders relavent to that class. For example, if sent in "MATH101" it will send all reminders for the class "MATH101".

`!remind <Class> <Thing to Remind> <Month> <Day> <Hour> <Minute> <amOrPm>`

- This add a reminder for the stated class, thing to remind, and time. Note before added, it will need get approved by admins to check for legitimency.
- Month and day are in numerical format, Hour is in 24hour format.


## Setup

1) Register a Discord Application and create a bot in the Discord Dev Portal
2) Create token.txt file in src directory and paste bots token to it.
3) Create db_account.txt file in src directory and paste the connection to the mongodb atlas database, should look something like this: **mongodb+srv://username:<password\>@cluster0.ukkj3.mongodb.net/dbname?retryWrites=true&w=majority**
4) Create collections for users, reminders and stats and change classes in the classes array
5) Run bot py file