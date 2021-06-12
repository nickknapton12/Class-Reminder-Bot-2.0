import pymongo
from pymongo import MongoClient
from pymongo import collection

cluster = MongoClient("mongodb+srv://nickknapton:Whicket1@cluster0.ukkj3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Discord-Bot"]
collection = db["Users"]

# Adds a new user to database, assumes user is not a bot. 
def add_user(user):
    user_to_insert = {"_id": user.id, "username": user.name, "nickname": user.display_name}
    print(user_to_insert)
    collection.insert_one(user_to_insert)

def find_user(user):
    return collection.find_one({"_id": user.id})

def add_class(user, the_class):
    collection.update_one({"_id": user.id}, {"$addToSet": {"classes": the_class}})
    
def remove_class(user, the_class):
    collection.update_one({"_id": user.id}, {"$pull": {"classes": the_class}})
