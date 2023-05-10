import config
from pymongo import MongoClient
client = MongoClient(config.mongodb_client_url)
db = client.dbsparta

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
db.users.insert_one({'name':'영희','age':30})
db.users.insert_one({'name':'철수','age':20})
db.users.insert_one({'name':'john','age':30})