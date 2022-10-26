from pymongo import MongoClient
client = MongoClient('mongodb+srv://mino:mino@hanghae.hfuwmwd.mongodb.net/?retryWrites=true&w=majority')
db = client.hanghae

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

doc = {
    'count_pk': 0,
    'user_count': 0,
    'bookmark_count': 0,
    'postwrite_count': 0,
    'like_count': 0,
    'comment_count': 0,
}
db.Counts.insert_one(doc)
