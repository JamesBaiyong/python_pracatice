#encoding=utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config
from flask_login import  LoginManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
# 登录管理
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 将auth部分加载到程序中
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # 将文献信息部分加载到程序中
    from .docinfo import doc as doc_blueprint
    app.register_blueprint(doc_blueprint, url_prefix='/docinfo')

    # 将通知公告信息部分加载到程序中
    from .notice import notice as notice_blueprint
    app.register_blueprint(notice_blueprint, url_prefix='/notice')

    return app