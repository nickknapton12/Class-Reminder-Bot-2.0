# Class-Reminder-Bot-2.0
A discord bot to manage and remind students of upcoming assignments, labs, tests, exams and anything else school related!

## Features
- Sends daily morning reminders to students via discord DMs of all there upcoming assignments, labs, tests, exams etc.
- Users can sign up for specific classes and control which classes they need reminding for and which they dont!
- Users can request the bot for the current reminders at any point and the bot will send a tailored response, depending on where the message was sent.

## Commands
`!reminders`

- If sent in a DM to the bot, this will return a list of all reminders for each class the user has signed up for. <br>
- If sent in a class channel, it will send a list of all reminders relavent to that class. For example, if sent in "ENSF409" it will send all reminders for the class "ENSF409".

`!remind <Class> <Thing to Remind> <Month> <Day> <Hour> <Minute>`

- This add a reminder for the stated class, thing to remind, and time. Note before added, it will need get approved by admins to check for legitimency.
- Month and day are in numerical format, Hour is in 24hour format.


## Setup

mongodb+srv://nickknapton:<password>@cluster0.ukkj3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority