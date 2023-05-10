# 지니뮤직의 1~50위 곡의 순위 / 곡 제목 / 가수를 크롤링하기
import requests
from bs4 import BeautifulSoup

URL = "https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20230101"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    rank = song.select_one('.number').text[:2].strip()
    title = song.select_one('.title').text.strip()
    artist = song.select_one('.artist').text.strip()
    print(rank, title, artist)