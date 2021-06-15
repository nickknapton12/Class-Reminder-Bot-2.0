from discord import message
import pymongo
from pymongo import MongoClient
from pymongo import collection

def read_account():
    with open("./src/db_account.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()

account = read_account()

cluster = MongoClient(account)
db = cluster["Discord-Bot"]
collection = db["Users"]

# Adds a new user to database, assumes user is not a bot. 
def add_user(user, sign_up_message):
    user_to_insert = {"_id": user.id, "username": user.name, "nickname": user.display_name, "sign_up_message": sign_up_message.id}
    collection.insert_one(user_to_insert)

# Finds a user in the db
def find_user_by_id(user):
    return collection.find_one({"_id": user})

# Adds a class to the user in the db.
def add_class(user, the_class):
    collection.update_one({"_id": user.id}, {"$addToSet": {"classes": the_class}})
    
# Removes a class from the user in the db
def remove_class(user, the_class):
    collection.update_one({"_id": user.id}, {"$pull": {"classes": the_class}})

def sign_up_message(message_id):
    message = collection.find_one({"sign_up_message": message_id})
    if message == None:
        return False
    else: 
        return True
