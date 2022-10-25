from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority')
db = client.hanghae

@app.route('/')
def home():
   return render_template('test2.html')


@app.route("/Post", methods=["GET"])
def Postwrite_get():
    user_pk_list = list(db.Postwrite.find({}, {'_id': False}))

    return jsonify({'post_list': user_pk_list})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)




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