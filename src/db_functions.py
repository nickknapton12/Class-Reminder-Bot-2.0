from discord import message
import pymongo
from pymongo import MongoClient
from pymongo import collection
from bson import ObjectId

def read_account():
    with open("./src/db_account.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()

account = read_account()

cluster = MongoClient(account)
db = cluster["Discord-Bot"]
collection = db["Users"]
collection2 = db["Reminders"]

# Adds a new user to database, assumes user is not a bot. 
def add_user(user, sign_up_message):
    user_to_insert = {"_id": user.id, "username": user.name, "nickname": user.display_name, "sign_up_message": sign_up_message.id}
    collection.insert_one(user_to_insert)

# Finds a user in the db
def find_user_by_id(user_id):
    return collection.find_one({"_id": user_id})

# Adds a class to the user in the db.
def add_class(user_id, the_class):
    collection.update_one({"_id": user_id}, {"$addToSet": {"classes": the_class}})
    
# Removes a class from the user in the db
def remove_class(user_id, the_class):
    collection.update_one({"_id": user_id}, {"$pull": {"classes": the_class}})

def sign_up_message(message_id):
    message = collection.find_one({"sign_up_message": message_id})
    if message == None:
        return False
    else: 
        return True

def add_requested_reminder(the_class, reminder, month, day, hour, minute):
    rem = collection2.insert_one({"Class": the_class, "Reminder": reminder, "Month": month, "Day": day, "Hour": hour, "Minute": minute, "Approved": False})
    return rem.inserted_id

def approve_reminder(reminder_id):
    res = collection2.update_one({"_id": ObjectId(reminder_id)}, {"$set": {"Approved": True}})

def delete_reminder(reminder_id):
    collection2.delete_one({"_id": ObjectId(reminder_id)})