import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))) # (두수준) 상위 폴더 파일 가져올때 사용

import config

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient(config.mongodb_client_url)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
	return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
	url_receive = request.form['url_give']
	comment_receive = request.form['comment_give']
	star_receive = request.form['star_give']
	
    # url에 해당하는 meta data 가져오기
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
	data = requests.get(url_receive, headers=headers)
	
	soup = BeautifulSoup(data.text, 'html.parser')
	ogtitle = soup.select_one('meta[property="og:title"]')['content']
	ogdesc = soup.select_one('meta[property="og:description"]')['content']
	ogimage = soup.select_one('meta[property="og:image"]')['content']
	doc = {
		'title': ogtitle,
        'desc': ogdesc,
        'image': ogimage,
        'comment': comment_receive,
        'star': star_receive,
    }
	db.movies.insert_one(doc)

	return jsonify({'msg':'저장 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
	movies = list(db.movies.find({}, {'_id': False}))
	return jsonify({'result': movies})

if __name__ == '__main__':
	app.run('0.0.0.0', port=5001, debug=True)