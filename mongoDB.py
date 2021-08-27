import pymongo
from pymongo import MongoClient


# Reminder to change the password 0lk0HmuOsMmrC6S1
client = MongoClient("mongodb+srv://dbAdmin:0lk0HmuOsMmrC6S1@financetrackercluster.su6qh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["FinanceTrackerCluster"]
collection = db["FinaceTrackerDB"]

post = {"_id": 0, "name": "time", "score": 5}

collection.insert_one(post)
