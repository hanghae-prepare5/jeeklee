# Proj : flask import
from flask import Flask, session

def create_app():
    app = Flask(__name__)
    # session 암호화
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    from .views import mypage_views, login_views, register_views, postwrite_views, post_views, main_views
    app.register_blueprint(mypage_views.bp)
    app.register_blueprint(login_views.bp)
    app.register_blueprint(register_views.bp)
    app.register_blueprint(postwrite_views.bp)
    app.register_blueprint(post_views.bp)
    app.register_blueprint(main_views.bp)

    return app
