from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]

# Example collections
users_collection = db["users"]
teams_collection = db["teams"]
activities_collection = db["activity"]
leaderboard_collection = db["leaderboard"]
workouts_collection = db["workouts"]

# Functions to interact with collections
def create_user(username, email, password):
    users_collection.insert_one({"username": username, "email": email, "password": password})

def create_team(name, members):
    teams_collection.insert_one({"name": name, "members": members})

def create_activity(user_id, activity_type, duration):
    activities_collection.insert_one({"user_id": user_id, "activity_type": activity_type, "duration": duration})

def create_leaderboard_entry(user_id, score):
    leaderboard_collection.insert_one({"user_id": user_id, "score": score})

def create_workout(name, description):
    workouts_collection.insert_one({"name": name, "description": description})
