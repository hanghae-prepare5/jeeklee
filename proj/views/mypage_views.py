from flask import Blueprint, render_template, url_for
from flask import request, jsonify
from flask import session, g

bp = Blueprint('mypage', __name__, url_prefix='/mypage')

# DB : pymongo, certifi import
from pymongo import MongoClient
import certifi
client = MongoClient('mongodb+srv://admin:admin@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.hanghae

@bp.route('/')
def index():
    # Variables for TEST
    session['ID'] = "test01"
    session['img'] = "https://miro.medium.com/max/640/1*xmotaE0PMsf3eCAM7mQCvA.jpeg"

    g.userid = session['ID']
    g.userimg = session['img']
    # if name == '':
    #     return render_template('login.index') # 나중에 로그인 페이지로 돌아가게 경로 설정
    return render_template('mypage.html')

@bp.route('/userpost', methods=["GET"])
def pass_user_posts() :
    user_posts = list(db.Postwrite.find({'user_pk':session['ID']},{'_id':False}))
    return jsonify(user_posts)

@bp.route('/bookmark', methods=["GET"])
def pass_user_bookmarks() :
    user = db.users.find_one({'name':session['ID']})
    bookmarks = user['bookmarks']
    result = []
    for num in range(len(bookmarks)):
        tmp = db.users.find_one({'_id':bookmarks[num]})
        result.append(tmp)

    return jsonify(result)

@bp.route('/test')
def test1():
    return render_template('test1.html')
