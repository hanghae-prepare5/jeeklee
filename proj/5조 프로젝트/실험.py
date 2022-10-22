from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.bkcsdxn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('test1.html')


@app.route('/Postwrite', methods=["post"])
def Postwrite():
    image_receive = request.form['image_give']
    tags_receive = request.form['tags_give']
    text_receive = request.form['text_give']
    write_date_receive = request.form['write_date_give']

    postwrite_pk_list = list(db.Postwrite.find({}, {'_pk': False}))
    count = len(postwrite_pk_list) + 1

    doc = {
        'postwrite_pk': count,
        'user_pk': db.User.find_one({'user_pk': 5}, {'_id': False}),
        'tags': tags_receive.split(' '),
        'text': text_receive,
        'image': image_receive,
        'write_date': write_date_receive,
    }
    db.Postwrite.insert_one(doc)

    return jsonify({'msg': '게시완료!'})

@app.route("/Postwrite", methods=["GET"])
def post_get():
    all_users = list(db.Postwrite.find({},{'_id':False}))
    return jsonify({'post_1': all_users})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
