from flask import Blueprint, render_template, url_for
from flask import request, jsonify
from flask import session, g

bp = Blueprint('mypage', __name__, url_prefix='/mypage')

# DB : pymongo, certifi import
from pymongo import MongoClient
import certifi
client = MongoClient("mongodb+srv://admin:admin@cluster0.uuxjj5e.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.teamproj

@bp.route('/')
def index():
    # Variables for TEST
    session['ID'] = "JeekLee"
    session['img'] = "https://spnimage.edaily.co.kr/images/photo/files/NP/S/2019/03/PS19032200090.jpg"

    g.userid = session['ID']
    g.userimg = session['img']
    # if name == '':
    #     return render_template('login.index') # 나중에 로그인 페이지로 돌아가게 경로 설정
    return render_template('mypage.html')
