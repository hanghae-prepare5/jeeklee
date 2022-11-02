from flask import Flask, render_template, request, jsonify , session, Blueprint, redirect, url_for

from pymongo import MongoClient
client = MongoClient('mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority')
db = client.hanghae

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def home():
    if session.get('id') is None:
        return render_template('login.html')
    image = db.user.find_one({'id': session['id']})['profile']
    return render_template('main.html', user_id=session['id'], profile =image)
   # if 'id' in session :
   #     return render_template('main.html')
   # return render_template('login.html')

#피드게시물표기
@bp.route("/main", methods=["GET"])
def postwrite_get():
    if session.get('id') is None:
        return render_template('login.html')

    postwrite_pk_list = list(db.postwrite.find({}, {'_id': False}))

    return jsonify({'post_list': postwrite_pk_list})

@bp.route("/like/count", methods=["GET"])
def like_count_get():
    if session.get('id') is None:
        return render_template('login.html')

    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
    like_list = list(db.like.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))
    like_count = len(like_list)

    return jsonify({'like_count': like_count})




# 최신순 좋아요순 정렬 정리
#def home(request):
#   sort = request.GET.get('sort', '')
#   if sort == 'likes':
#      content_list = Content.objects.all().order_by('-like_count', '-date')
#   elif sort == 'comments':
#      content_list = Content.objects.all().order_by('-comment_count', '-date')
#   else:
#      content_list = Content.objects.all().order_by('-date')
#
#   paginator = Paginator(content_list, 5)
#   page = request.GET.get('page', '')
#   posts = paginator.get_page(page)
#   board = Board.objects.all()

#   return render(request, 'home.html', {'posts': posts, 'Board': board, 'sort': sort})






#   import gridfs

   # Create an object of GridFs for the above database.
#   fs = gridfs.GridFS(db)

   # define an image object with the location.
#   file = "testphoto.jpeg"

   # Open the image in read-only format.
#   with open(file, 'rb') as f:
#       contents = f.read()

   # Now store/put the image via GridFs object.
#   fs.put(contents, filename="testphoto")


## 좋아요 갯수 표시
#@app.route("/like/count", methods=["GET"])
#def like_count_get():
#    postwrite_pk_receive = request.args.get('postwrite_pk1_give')
#    like_list = list(db.Like.find({'postwrite_pk': int(postwrite_pk_receive)}, {'_id': False}))
#    like_count = len(like_list)

#    return jsonify({'like_count': like_count})