from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
# DB : pymongo, certifi import
from pymongo import MongoClient

client = MongoClient('mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority')
db = client.hanghae

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/')
def index():
    if 'id' in session:
        return redirect(url_for('main.main'))
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/login', methods=["GET"])
def login_get():
    user_list = list(db.user.find({}, {'_id': False}))
    return jsonify({'user': user_list})


@bp.route('/login/session', methods=["GET", "POST"])
def login_session():
    if request.method == 'POST':
        # 사용자 아이디를 세션에 저장 및  main으로 리다이렉트
        session.clear();
        session['id'] = request.form['id_give']
        return redirect(url_for('main.main'))


@bp.route('/logout')
def logout():
    # 사용자 아이디를 세션에서 제거하고 /로 리다이렉트
    session.pop('id', None)
    return redirect(url_for('login.index'))
