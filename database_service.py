
# we create helper fuctions to interact with the database 
# I chose HarperDB for the database -> can use sql and no sql: Cloud/edge device

'''
Steps:
First install HarperDB: pip install harperdb
'''

import harperdb

url = "https://cloud-1-tuski.harperdbcloud.com"
username = "george"
password = "skyGeorge9$"

#Connect to database
db = harperdb.HarperDB(
    url = url,
    username = username,
    password = password
)

#Put data into the database

#get ifo from the harper repo and the tables created
SCHEMA = "workout_repo"
TABLE = "workouts"
TABLE_TODAY = "workout_today"

#insert data
#the key values are the columns and the value is the data that was passed
# data = {
#     "video_id": "12345",  
#     "title": "Test 1", 
#     "channel": "Test channel"
# }

#we passed the date into the database
# res = db.insert(SCHEMA, TABLE, [data])
# print(res)

#methods for each verb action 
# def insert_workout(workout_data):
#     return db.insert(SCHEMA, TABLE, [workout_data])

# def delete_workout(workout_id):
#     return db.delete(SCHEMA, TABLE, [workout_id])

# def get_all_workouts():
#     return db.sql(f"select video_id, channel, title, duration from {SCHEMA}.{TABLE}")

# def get_workout_today():
#     return db.sql(f"select * from {SCHEMA}.{TABLE_TODAY} where id = 0")

# def update_workout_today(workout_data, insert=False):
#     workout_data[0] = 0 
#     if insert:
#         return db.insert(SCHEMA, TABLE_TODAY, [workout_data])
#     return db.update(SCHEMA, TABLE_TODAY, [workout_data])

# from yt_extractor import get_info

# infos = get_info("https://youtu.be/prtu-Tx8fv4")
# print(infos)

# insert_workout(infos)

# workouts = get_all_workouts()
# print(workouts)


def insert_workout(workout_data):
    return db.insert(SCHEMA, TABLE, [workout_data])


def delete_workout(workout_id):
    return db.delete(SCHEMA, TABLE, [workout_id])


def get_all_workouts():
    try:
        return db.sql(f"select video_id,channel,title,duration from {SCHEMA}.{TABLE}")
    except harperdb.exceptions.HarperDBError:
        return []


def get_workout_today():
    try:
        return db.sql(f"select * from {SCHEMA}.{TABLE_TODAY} where id = 0")
    except harperdb.exceptions.HarperDBError:
        return []


def update_workout_today(workout_data, insert=False):
    workout_data['id'] = 0
    if insert:
        return db.insert(SCHEMA, TABLE_TODAY, [workout_data])
    return db.update(SCHEMA, TABLE_TODAY, [workout_data])
