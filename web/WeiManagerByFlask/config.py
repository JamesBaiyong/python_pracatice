#encoding=utf-8
import os
from password.password import  MAIL_PASSWORD, MAIL_USERNAME, FLASK_ADMIN

class Config(object):
    # 通用配置
    SECRET_KEY = 'you never can guess it'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_USERNAME = MAIL_USERNAME
    MAIL_PASSWORD = MAIL_PASSWORD
    FLASKY_MAIL_SENDER = 'Wei-Manager Admin <robotinfo@126.com>'
    FLASKY_MAIL_SUBJECT_PREFIX = u'[小知]'
    FLASKY_ADMIN = FLASK_ADMIN
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = MAIL_USERNAME
    MAIL_PASSWORD = MAIL_PASSWORD

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://dog:dogpass@localhost:3306/wei_manager'

class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://dog:dogpass@localhost:3306/wei_manager'


config = {
    'development': DevelopmentConfig,
    'production':ProductionConfig
}