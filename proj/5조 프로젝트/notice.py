from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.bkcsdxn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('notice.html')


@app.route("/Post", methods=["GET"])
def post_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    postwrite_list = list(db.Postwrite.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))

    return jsonify({'post_list': postwrite_list})


@app.route('/Comment', methods=["post"])
def Comment():
    postwrite_pk_receive = request.form['postwrite_pk_give']
    comments_receive = request.form['comments_give']
    comments_date_receive = request.form['comments_date_give']

    comment_count = db.Counts.find_one({'count_pk': 0}, {'_id': False})
    count = comment_count['comment_count'] + 1

    doc = {
        'postwrite_pk': postwrite_pk_receive,
        'comments_pk': count,
        'comments': comments_receive,
        'comments_flag': 0,
        # 접속유저 pk(세션)
        'comments_id': db.User.find_one({'user_pk': 5}, {'_id': False}),
        'comments_date': comments_date_receive,
    }
    db.Comment.insert_one(doc)
    db.Counts.update_one({'count_pk': 0}, {'$set': {'comment_count': count}})

    return jsonify({'msg': '댓글 작성 완료!'})


@app.route("/Comment", methods=["GET"])
def Comment_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    comment_list = list(db.Comment.find({'postwrite_pk': postwrite_pk_receive}, {'_id': False}))

    return jsonify({'comment_list': comment_list})


@app.route("/post/Comment_count", methods=["GET"])
def Comment_count_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    comment_list = list(db.Comment.find({'postwrite_pk': postwrite_pk_receive}, {'_id': False}))

    comment_count = len(comment_list)
    return jsonify({'comment_count': comment_count})


@app.route('/comment/delete', methods=["post"])
def comment_delete():
    postwrite_pk_receive = request.form['postwrite_pk_give']
    comment_pk_receive = request.form['comment_pk_give']
    print(comment_pk_receive)
    comment_list = list(db.Comment.find({'postwrite_pk': postwrite_pk_receive}, {'_id': False}))
    # 접속유저 pk(세션)
    user_id = db.User.find_one({'user_pk': 5}, {'_id': False})

    # 포스트작성자권한
    postwrite_pk1 = db.Postwrite.find_one({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False})
    postwrite_pk2 = postwrite_pk1['user_pk']
    print(postwrite_pk2['user_pk'])

    # 댓글작성자권한
    comment_id1 = comment_list[0]
    comment_id2 = comment_id1['comments_id']
    print(comment_id2['user_pk'])

    if (user_id['user_pk'] == comment_id2['user_pk']):
        db.Comment.delete_one({'comments_pk': int(comment_pk_receive)})
        return jsonify({'msg': '댓글 삭제!'})
    elif (user_id['user_pk'] == postwrite_pk2['user_pk']):
        return jsonify({'msg': '댓글 삭제!'})
    else:
        return jsonify({'msg': '권한이 없습니다!'})


@app.route('/like', methods=["post"])
def Like():
    postwrite_pk_receive = request.form['postwrite_pk_give']

    like_count = db.Counts.find_one({'count_pk': 0}, {'_id': False})
    count = like_count['like_count'] + 1

    doc = {
        'postwrite_pk': postwrite_pk_receive,
        'like_pk': count,
        'like_flag': 0,
        # 접속유저 pk값(세션)
        'like_id': 5
    }
    db.Like.insert_one(doc)
    db.Counts.update_one({'count_pk': 0}, {'$set': {'like_count': count}})

    return jsonify({'msg': '좋아요!'})


@app.route("/like", methods=["GET"])
def Like_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    like_list = list(db.Like.find({'postwrite_pk': postwrite_pk_receive}, {'_id': False}))

    # 접속유저 pk(세션)
    user_id = db.User.find_one({'user_pk': 5}, {'_id': False})

    if (like_list):
        like_id2 = like_list[0]
        like_id1 = like_id2['like_id']
        if (user_id['user_pk'] == like_id1):
            return jsonify({'result': 1})
        else:
            return jsonify({'result': 0})
    else:
        return jsonify({'result': 0})


@app.route("/like/count", methods=["GET"])
def like_count_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    like_list = list(db.Like.find({'postwrite_pk': postwrite_pk_receive}, {'_id': False}))

    like_count = len(like_list)
    return jsonify({'like_count': like_count})


@app.route('/like/delete', methods=["post"])
def Like_delete():
    postwrite_pk_receive = request.form['postwrite_pk_give']
    like_list = list(db.Like.find({'postwrite_pk': postwrite_pk_receive}, {'_id': False}))
    # 접속유저 pk(세션)
    user_id = db.User.find_one({'user_pk': 5}, {'_id': False})

    like_id = like_list[0]
    if (user_id['user_pk'] == like_id['like_id']):
        db.Like.delete_one({'like_id': user_id['user_pk']})
        return jsonify({'msg': '좋아요 취소!'})


@app.route('/bookmark', methods=["post"])
def bookmark():
    postwrite_pk_receive = request.form['postwrite_pk_give']
    bookmark_count = db.Counts.find_one({'count_pk': 0}, {'_id': False})
    count = bookmark_count['bookmark_count'] + 1

    doc = {
        'bookmark_pk': count,
        'postwrite_pk': postwrite_pk_receive,
        # 접속유저 pk값(세션)
        'bookmark_id': 5
    }
    db.Bookmark.insert_one(doc)
    db.Counts.update_one({'count_pk': 0}, {'$set': {'bookmark_count': count}})

    return jsonify({'msg': '북마크!'})


@app.route("/bookmark", methods=["GET"])
def bookmark_get():
    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    bookmark_list = list(db.Bookmark.find({'postwrite_pk': postwrite_pk_receive}, {'_id': False}))

    # 접속유저 pk(세션)
    user_id = db.User.find_one({'user_pk': 5}, {'_id': False})

    if (bookmark_list):
        bookmark_list2 = bookmark_list[0]
        bookmark_id1 = bookmark_list2['bookmark_id']
        if (user_id['user_pk'] == bookmark_id1):
            return jsonify({'result': 1})
        else:
            return jsonify({'result': 0})
    else:
        return jsonify({'result': 0})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
