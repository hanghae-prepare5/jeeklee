from pymongo import MongoClient
client = MongoClient('mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority')
db = client.hanghae

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('noticewrite.html')


@app.route('/Postwrite', methods=["post"])
def Postwrite():
    image_receive = request.form['image_give']
    tags_receive = request.form['tags_give']
    text_receive = request.form['text_give']
    write_date_receive = request.form['write_date_give']



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
def bucket_get():
    User_list = list(db.User.find({'user_pk': 5}, {'_id': False}))
    return jsonify({'User' : User_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
