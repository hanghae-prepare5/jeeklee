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
    postwrite_pk_list = list(db.Postwrite.find({}, {'_id': False}))
    count = len(postwrite_pk_list)
    postwrite_list = list(db.Postwrite.find({'postwrite_pk': count, }, {'_id': False}))
    return jsonify({'post_list': postwrite_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
