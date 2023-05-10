import config
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient(config.mongodb_client_url)
db = client.dbsparta

# 영화제목 '가디언즈 오브 갤럭시: Volume 3'의 평점을 가져오기
movie = db.movies.find_one({'title': '가디언즈 오브 갤럭시: Volume 3'})
target_star = movie['star']

# '가디언즈 오브 갤럭시: Volume 3'의 평점과 같은 평점의 영화 제목들을 가져오기
movies = db.movies.find({'star': target_star})
for m in movies:
    print(m['title'])

# '가디언즈 오브 갤럭시: Volume 3' 영화의 평점을 0으로 만들기
db.movies.update_one({'title': '가디언즈 오브 갤럭시: Volume 3'}, {'$set': {'star': '0'}})