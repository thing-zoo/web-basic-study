from .. import config
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient(config.mongodb_client_url)
db = client.dbsparta

URL = "https://movie.daum.net/ranking/reservation"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

video_list = soup.select("#mainContent > div > div.box_ranking > ol > li")
for v in video_list:
    # 영화 순위, 제목, 평점 가져오기
    rank = v.select_one(".rank_num").text
    title = v.select_one(".tit_item").text.strip("\n")
    star = v.select_one(".txt_grade").text
    doc = {
        'title': title,
        'rank': rank,
        'star': star
    }
    # db에 넣기
    db.movies.insert_one(doc)