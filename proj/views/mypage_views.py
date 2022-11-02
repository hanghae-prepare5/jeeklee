from flask import Blueprint, render_template, url_for
from flask import request, jsonify
from flask import session, g

bp = Blueprint('mypage', __name__, url_prefix='/mypage')

# DB : pymongo, certifi import
from pymongo import MongoClient
import certifi
client = MongoClient("mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.hanghae

@bp.route('/')
def index():
    if session.get('id') is None:
        return render_template('login.html') # 로그인 정보가 없을 때 로그인 페이지로 돌아가게 경로 설정
    g.userid = session['id']
    image = db.user.find_one({'id':session['id']})['profile']
    g.userimg = image
    return render_template('mypage.html')

@bp.route('/userpost', methods=["GET"])
def pass_user_posts() :
    if session.get('id') is None:
        return render_template('login.html')

    user_posts = list(db.postwrite.find({'user_pk':session['id']},{'_id':False}))
    return jsonify(user_posts)

@bp.route('/bookmark', methods=["GET"])
def pass_user_bookmarks() :
    if session.get('id') is None:
        return render_template('login.html')
    postwrite_list = list(db.bookmark.find({'bookmark_id':session['id']}, {'_id':False}))
    result = []
    for num in range(len(postwrite_list)):
        postwrite_pk = postwrite_list[num]['postwrite_pk']
        tmp = db.postwrite.find_one({'postwrite_pk':postwrite_pk},{'_id':False})
        result.append(tmp)
    return jsonify(result)

@bp.route('/comment', methods=["GET"])
def pass_user_comments() :
    if session.get('id') is None:
        return render_template('login.html')

    user_posts_pk = list(db.postwrite.find({'user_pk':session['id']},{'_id':False, 'postwrite_pk':True}))
    result = []
    for num in range(len(user_posts_pk)):
        postwrite_pk = user_posts_pk[num]['postwrite_pk']
        tmp = list(db.comment.find({'postwrite_pk':postwrite_pk},{'_id':False}))
        if tmp:
            db.comment.update_many({'postwrite_pk':postwrite_pk},{'$set':{'comments_flag' : False}})
            result.append(tmp)
    return jsonify(result)

@bp.route('/like', methods=["GET","POST"])
def pass_user_likes() :
    if session.get('id') is None:
        return render_template('login.html')

    user_posts_pk = list(db.postwrite.find({'user_pk':session['id']},{'_id':False, 'postwrite_pk':True}))
    result = []
    for num in range(len(user_posts_pk)):
        postwrite_pk = user_posts_pk[num]['postwrite_pk']
        tmp = list(db.like.find({'postwrite_pk':postwrite_pk},{'_id':False}))
        if tmp:
            result.append(tmp)
            db.like.update_many({'postwrite_pk':postwrite_pk},{'$set':{'like_flag' : False}})
    return jsonify(result)


@bp.route('/postpage')
def postpage() :
    if session.get('id') is None:
        return render_template('login.html')
    return render_template('postpage.html')
