from pymongo import MongoClient
client = MongoClient('mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority')
db = client.hanghae

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('notice.html')

# 포스트 불러오기
@app.route("/Post", methods=["GET"])
def post_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    postwrite_list = list(db.Postwrite.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))

    return jsonify({'post_list': postwrite_list})

# 댓글 데이터 저장
@app.route('/Comment', methods=["post"])
def Comment():
    postwrite_pk_receive = request.form['postwrite_pk_give']
    comments_receive = request.form['comments_give']
    comments_date_receive = request.form['comments_date_give']

    comment_count = db.Counts.find_one({'count_pk': 0}, {'_id': False})
    count = comment_count['comment_count'] + 1

    doc = {
        'postwrite_pk': int(postwrite_pk_receive),
        'comments_pk': count,
        'comments': comments_receive,
        'comments_flag': 0,
        # 접속유저 pk(세션)
        'comments_id': 5,
        'comments_date': comments_date_receive,
    }
    db.Comment.insert_one(doc)
    db.Counts.update_one({'count_pk': 0}, {'$set': {'comment_count': count}})

    return jsonify({'msg': '댓글 작성 완료!'})

# 댓글 불러오기
@app.route("/Comment", methods=["GET"])
def Comment_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    comment_list = list(db.Comment.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))

    return jsonify({'comment_list': comment_list})

# 댓글 갯수 표시
@app.route("/post/Comment_count", methods=["GET"])
def Comment_count_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    comment_list = list(db.Comment.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))

    comment_count = len(comment_list)
    return jsonify({'comment_count': comment_count})

# 댓글 삭제
@app.route('/comment/delete', methods=["post"])
def comment_delete():
    postwrite_pk_receive = request.form['postwrite_pk_give']
    comment_pk_receive = request.form['comment_pk_give']
    print(comment_pk_receive)

    # 접속유저 pk(세션)
    user_id = db.User.find_one({'user_pk': 5}, {'_id': False})

    # 포스트작성자권한
    postwrite_pk1 = db.Postwrite.find_one({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False})
    print(postwrite_pk1['user_pk'])

    # 댓글작성자권한
    if (db.Comment.find_one({'comments_pk': int(comment_pk_receive),'comment_id':user_id['user_pk']})):
        db.Comment.delete_one({'comments_pk': int(comment_pk_receive)})
        return jsonify({'msg': '댓글 삭제!'})
    # 포스트작성자권한
    elif (user_id['user_pk'] == postwrite_pk1['user_pk']):
        db.Comment.delete_one({'comments_pk': int(comment_pk_receive)})
        return jsonify({'msg': '댓글 삭제!'})
    else:
        return jsonify({'msg': '권한이 없습니다!'})

# 좋아요 데이터 저장
@app.route('/like', methods=["post"])
def Like():
    postwrite_pk_receive = request.form['postwrite_pk_give']

    like_count = db.Counts.find_one({'count_pk': 0}, {'_id': False})
    count = like_count['like_count'] + 1

    doc = {
        'postwrite_pk': int(postwrite_pk_receive),
        'like_pk': count,
        'like_flag': 0,
        # 접속유저 pk값(세션)
        'like_id': 5
    }
    db.Like.insert_one(doc)
    db.Counts.update_one({'count_pk': 0}, {'$set': {'like_count': count}})

    return jsonify({'msg': '좋아요!'})

# 좋아요 눌럿으면 채운하트 아니면 빈하트
@app.route("/like", methods=["GET"])
def Like_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')

    # 접속유저 pk(세션)
    user_id = db.User.find_one({'user_pk': 5}, {'_id': False})

    if db.Like.find_one({'like_id': user_id['user_pk'],'postwrite_pk': int(postwrite_pk_receive)}):
        return jsonify({'result': 1})
    else:
        return jsonify({'result': 0})

# 좋아요 갯수 표시
@app.route("/like/count", methods=["GET"])
def like_count_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    like_list = list(db.Like.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))
    like_count = len(like_list)

    return jsonify({'like_count': like_count})

# 좋아요 취소
@app.route('/like/delete', methods=["post"])
def Like_delete():
    postwrite_pk_receive = request.form['postwrite_pk_give']

    # 접속유저 pk(세션)
    user_id = db.User.find_one({'user_pk': 5}, {'_id': False})

    db.Like.delete_one({'like_id': user_id['user_pk'],'postwrite_pk': int(postwrite_pk_receive)})
    return jsonify({'msg': '좋아요 취소!'})

# 북마크 데이터 저장
@app.route('/bookmark', methods=["post"])
def bookmark():
    postwrite_pk_receive = request.form['postwrite_pk_give']
    bookmark_count = db.Counts.find_one({'count_pk': 0}, {'_id': False})
    count = bookmark_count['bookmark_count'] + 1

    doc = {
        'bookmark_pk': count,
        'postwrite_pk': int(postwrite_pk_receive),
        # 접속유저 pk값(세션)
        'bookmark_id': 5
    }
    db.Bookmark.insert_one(doc)
    db.Counts.update_one({'count_pk': 0}, {'$set': {'bookmark_count': count}})

    return jsonify({'msg': '북마크!'})

# 북마크 눌렀으면 채운 북마크 아니면 빈 북마크
@app.route("/bookmark", methods=["GET"])
def bookmark_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')

    # 접속유저 pk(세션)
    user_id = db.User.find_one({'user_pk': 5}, {'_id': False})

    if db.Bookmark.find_one({'bookmark_id': user_id['user_pk'], 'postwrite_pk': int(postwrite_pk_receive)}):
        return jsonify({'result': 1})
    else:
        return jsonify({'result': 0})
# 북마크 취소
@app.route('/bookmark/delete', methods=["post"])
def bookmark_delete():
    postwrite_pk_receive = request.form['postwrite_pk_give']

    # 접속유저 pk(세션)
    user_id = db.User.find_one({'user_pk': 5}, {'_id': False})

    db.Bookmark.delete_one({'bookmark_id': user_id['user_pk'],'postwrite_pk':int(postwrite_pk_receive)})
    return jsonify({'msg': '북마크 취소!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
