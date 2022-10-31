from pymongo import MongoClient
client = MongoClient('mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority')
db = client.hanghae

from flask import Flask, render_template, request, jsonify, session, Blueprint, url_for, g

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/<post>', methods=["GET","POST"])
def home(post):
    post_pk = post
    return render_template('post.html', post_pk = post_pk)

# 포스트 불러오기
@bp.route("/get", methods=["GET"])
def post_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    postwrite_list = list(db.postwrite.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))

    return jsonify({'post_list': postwrite_list}), render_template('post.html')

# 댓글 데이터 저장
@bp.route('/comment', methods=["POST"])
def comment():
    postwrite_pk_receive = request.form['postwrite_pk_give']
    comments_receive = request.form['comments_give']
    comments_date_receive = request.form['comments_date_give']

    # pk용 카운트 만들기
    box = list(db.counts.find({}))
    num = box[0]['comment_count']
    db.counts.update_one({}, {'$set': {'comment_count': num + 1}})

    doc = {
        'postwrite_pk': int(postwrite_pk_receive),
        'comments_pk': num+1,
        'comments': comments_receive,
        'comments_flag': True,
        # 접속유저 pk(세션)
        'comments_id': session['id'],
        'comments_date': comments_date_receive,
    }
    db.comment.insert_one(doc)

    return jsonify({'msg': '댓글 작성 완료!'})

# 댓글 불러오기
@bp.route("/comment", methods=["GET"])
def comment_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    comment_list = list(db.comment.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))

    return jsonify({'comment_list': comment_list})

# 댓글 갯수 표시
@bp.route("/comment_count", methods=["GET"])
def comment_count_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    comment_list = list(db.comment.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))

    comment_count = len(comment_list)
    return jsonify({'comment_count': comment_count})

# 댓글 삭제
@bp.route('/comment/delete', methods=["POST"])
def comment_delete():
    postwrite_pk_receive = request.form['postwrite_pk_give']
    comment_pk_receive = request.form['comment_pk_give']
    print(comment_pk_receive)


    # 포스트작성자권한
    postwrite_pk1 = db.postwrite.find_one({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False})
    postwrite_pk2=postwrite_pk1['user_pk']

    # 댓글작성자권한
    if (db.comment.find_one({'comments_pk': int(comment_pk_receive),'comment_id':session['id']})):
        db.comment.delete_one({'comments_pk': int(comment_pk_receive)})
        return jsonify({'msg': '댓글 삭제!'})
    # 포스트작성자권한
    elif (session['id'] == postwrite_pk2['user_pk']):
        db.comment.delete_one({'comments_pk': int(comment_pk_receive)})
        return jsonify({'msg': '댓글 삭제!'})
    else:
        return jsonify({'msg': '권한이 없습니다!'})


# 좋아요 데이터 저장
@bp.route('/like', methods=["POST"])
def like():
    postwrite_pk_receive = request.form['postwrite_pk_give']

    # pk용 카운트 만들기, 좋아요 데이터 저장
    box = list(db.counts.find({}))
    num = box[0]['like_count']
    db.counts.update_one({}, {'$set': {'like_count': num + 1}})

    doc = {
        'postwrite_pk': int(postwrite_pk_receive),
        'like_pk': num+1,
        'like_flag': True,
        # 접속유저 pk값(세션)
        'like_id': session['id']
    }
    db.like.insert_one(doc)

    # 좋아요 갯수 추가

    post = db.postwrite.find_one({'postwrite_pk': int(postwrite_pk_receive)})
    db.postwrite.update_one({'postwrite_pk':int(postwrite_pk_receive)},{'$set':{'like':post['like']+1}})

    return jsonify({'msg': '좋아요!'})

# 좋아요 눌럿으면 채운하트 아니면 빈하트
@bp.route("/like", methods=["GET"])
def like_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')

    if db.like.find_one({'like_id': session['id'],'postwrite_pk': int(postwrite_pk_receive)}):
        return jsonify({'result': 1})
    else:
        return jsonify({'result': 0})

# 좋아요 갯수 표시
@bp.route("/like/count", methods=["GET"])
def like_count_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    like_list = list(db.like.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))
    like_count = len(like_list)

    return jsonify({'like_count': like_count})

# 좋아요 취소
@bp.route('/like/delete', methods=["POST"])
def like_delete():
    postwrite_pk_receive = request.form['postwrite_pk_give']

    db.like.delete_one({'like_id': session['id'],'postwrite_pk': int(postwrite_pk_receive)})
    return jsonify({'msg': '좋아요 취소!'})

# 북마크 데이터 저장
@bp.route('/bookmark', methods=["POST"])
def bookmark():
    postwrite_pk_receive = request.form['postwrite_pk_give']

    # pk용 카운트 만들기
    box = list(db.counts.find({}))
    num = box[0]['bookmark_count']
    db.counts.update_one({}, {'$set': {'bookmark_count': num + 1}})

    doc = {
        'bookmark_pk': num+1,
        'postwrite_pk': int(postwrite_pk_receive),
        # 접속유저 pk값(세션)
        'bookmark_id': session['id']
    }
    db.bookmark.insert_one(doc)

    return jsonify({'msg': '북마크!'})

# 북마크 눌렀으면 채운 북마크 아니면 빈 북마크
@bp.route("/bookmark", methods=["GET"])
def bookmark_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')

    if db.bookmark.find_one({'bookmark_id': session['id'], 'postwrite_pk': int(postwrite_pk_receive)}):
        return jsonify({'result': 1})
    else:
        return jsonify({'result': 0})
# 북마크 취소
@bp.route('/bookmark/delete', methods=["POST"])
def bookmark_delete():
    postwrite_pk_receive = request.form['postwrite_pk_give']

    db.bookmark.delete_one({'bookmark_id': session['id'],'postwrite_pk':int(postwrite_pk_receive)})
    return jsonify({'msg': '북마크 취소!'})
