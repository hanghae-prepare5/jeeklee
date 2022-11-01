from flask import Blueprint, render_template, request, jsonify
import gridfs
# DB : pymongo, certifi import
from pymongo import MongoClient

client = MongoClient('mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority')
db = client.hanghae

bp = Blueprint('auth', __name__, url_prefix='/register')


@bp.route('/')
def register():
    return render_template('register.html')


@bp.route('/post', methods=["POST"])
def register_post():
    # receive data from html
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # DB data set
    doc = {
        'ID': id_receive,
        'PW': pw_receive,
        'postwrite_pk': []

    }
    db.user.insert_one(doc)
    return jsonify({'msg': '가입 완료되었습니다!'})

@bp.route('/get', methods=["GET"])
def register_get():
    user_list = list(db.user.find({}, {'_id': False}))
    return jsonify({'user': user_list})
