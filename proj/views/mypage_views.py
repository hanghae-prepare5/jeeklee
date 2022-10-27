from flask import Blueprint, render_template, url_for
from flask import request, jsonify
from flask import session, g

bp = Blueprint('mypage', __name__, url_prefix='/mypage')

# DB : pymongo, certifi import
from pymongo import MongoClient
import certifi
client = MongoClient("mongodb+srv://admin:admin@cluster0.fy9ver8.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.teamproj

@bp.route('/')
def index():
    # Variables for TEST
    session['ID'] = "testid_02"
    session['img'] = "https://miro.medium.com/max/640/1*xmotaE0PMsf3eCAM7mQCvA.jpeg"

    g.userid = session['ID']
    g.userimg = session['img']
    if session['ID'] == '':
        return render_template('login.index') # 로그인 정보가 없을 때 로그인 페이지로 돌아가게 경로 설정
    return render_template('mypage.html')

@bp.route('/userpost', methods=["GET"])
def pass_user_posts() :
    user_posts = list(db.postwrite.find({'user_id':session['ID']},{'_id':False}))
    return jsonify(user_posts)

@bp.route('/bookmark', methods=["GET"])
def pass_user_bookmarks() :
    postwrite_list = list(db.bookmark.find({'bookmark_id':session['ID']}, {'_id':False}))
    result = [];
    for num in range(len(postwrite_list)):
        postwrite_pk = postwrite_list[num]['postwrite_pk']
        tmp = db.postwrite.find_one({'postwrite_pk':postwrite_pk},{'_id':False})
        result.append(tmp)
    return jsonify(result)

@bp.route('/comment', methods=["GET"])
def pass_user_comments() :
    user_posts_pk = list(db.postwrite.find({'user_id':session['ID']},{'_id':False, 'postwrite_pk':True}))
    result = [];
    for num in range(len(user_posts_pk)):
        postwrite_pk = user_posts_pk[num]['postwrite_pk']
        tmp = db.comment.find_one({'postwrite_pk':postwrite_pk},{'_id':False})
        db.comment.update_one({'postwrite_pk':postwrite_pk},{'$set':{'comments_flag' : True}})
        result.append(tmp)
    return jsonify(result)

@bp.route('/like', methods=["GET","POST"])
def pass_user_likes() :
    user_posts_pk = list(db.postwrite.find({'user_id':session['ID']},{'_id':False, 'postwrite_pk':True}))
    result = [];
    for num in range(len(user_posts_pk)):
        postwrite_pk = user_posts_pk[num]['postwrite_pk']
        tmp = db.like.find_one({'postwrite_pk':postwrite_pk},{'_id':False})
        result.append(tmp)
        db.like.update_one({'postwrite_pk':postwrite_pk},{'$set':{'like_flag' : True}})
    return jsonify(result)


@bp.route('/postpage')
def postpage() :
    return render_template('postpage.html')
