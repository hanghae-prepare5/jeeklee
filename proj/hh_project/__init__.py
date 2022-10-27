# Proj : flask import
from flask import Flask, session


def create_app():
    app = Flask(__name__)
    # session 암호화
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    # main_views의 bp 객체 등록
    from .views import register_views, login_views
    app.register_blueprint(login_views.bp)
    app.register_blueprint(register_views.bp)

    return app
