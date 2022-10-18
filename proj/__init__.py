# Proj : flask import
from flask import Flask, session

def create_app():
    app = Flask(__name__)
    # session 암호화
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    from .views import mypage_views
    app.register_blueprint(mypage_views.bp)

    return app
