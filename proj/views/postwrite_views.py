from pymongo import MongoClient
client = MongoClient('mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority')
db = client.hanghae

from flask import render_template, request, jsonify
from flask import Blueprint, url_for, session, g

bp = Blueprint('postwrite', __name__, url_prefix='/postwrite')


@bp.route('/page', methods=["POST","GET"])
def page():
    if session.get('id') is None:
        return render_template('login.html')

    return render_template('postwrite.html')


@bp.route('/', methods=["POST"])
def postwrite():
    if session.get('id') is None:
        return render_template('login.html')

    image_receive = request.form['image_give']
    tags_receive = request.form['tags_give']
    text_receive = request.form['text_give']
    write_date_receive = request.form['write_date_give']

    # pk용 카운트 만들기
    box = list(db.counts.find({}))
    num = box[0]['count_pk']
    db.counts.update_one({}, {'$set': {'count_pk': num + 1}})

    doc = {
        'postwrite_pk': num+1,
        'user_pk': session['id'],
        'tags': tags_receive.split('-'),
        'text': text_receive,
        'image': image_receive,
        'write_date': write_date_receive,
        'like':0
    }
    db.postwrite.insert_one(doc)

    return jsonify({'msg': '게시완료!'})


@bp.route("/", methods=["GET"])
def bucket_get():
    if session.get('id') is None:
        return render_template('login.html')

    user_list = list(db.user.find({'id': session['id']}, {'_id': False}))
    return jsonify({'user': user_list})
