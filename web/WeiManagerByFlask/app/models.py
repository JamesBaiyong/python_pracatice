# encoding=utf-8
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import  login_manager, db
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class Role(db.Model):
    __tablename__ = 'roles'  # 定义表名
    id = db.Column(db.Integer, primary_key=True)  # 定义列对象
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role', lazy='dynamic')  # 建立两表之间的关系，其中backref是定义反向关系，lazy是禁止自动执行查询

    def __repr__(self):
        return '<Role {}> '.format(self.name)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    confirmed = db.Column(db.Boolean, default=False)


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def __repr__(self):
        return '<User {}>'.format(self.username)

class BookInfo(db.Model):
    __tablename__ = 'book_info'
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(128), unique=True, index=True)
    author= db.Column(db.String(128),index=True)
    number = db.Column(db.Integer)
    type = db.Column(db.String(128))

class PaperInfo(db.Model):
    __tablename__ = 'paper_info'
    id = db.Column(db.Integer, primary_key=True)
    paper_title = db.Column(db.String(128), unique=True, index=True)
    author= db.Column(db.String(128),index=True)
    from_where = db.Column(db.String(128),index=True)
    content = db.Column(db.String(128))

class DegreeInfo(db.Model):
    __tablename__ = 'degree_info'
    id = db.Column(db.Integer, primary_key=True)
    degree_title = db.Column(db.String(128), unique=True, index=True)
    author= db.Column(db.String(128),index=True)
    from_where = db.Column(db.String(128),index=True)
    content = db.Column(db.String(128))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
