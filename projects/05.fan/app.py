import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))) # (두수준) 상위 폴더 파일 가져올때 사용

import config

from pymongo import MongoClient
client = MongoClient(config.mongodb_client_url)
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }

    db.fan.insert_one(doc)

    return jsonify({'msg': '응원 완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    fan_list = list(db.fan.find({}, {'_id': False}))
    return jsonify({'result': fan_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)