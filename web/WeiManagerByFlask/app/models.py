# encoding=utf-8
from . import db


class Role(db.Model):
    __tablename__ = 'roles'  # 定义表名
    id = db.Column(db.Integer, primary_key=True)  # 定义列对象
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role', lazy='dynamic')  # 建立两表之间的关系，其中backref是定义反向关系，lazy是禁止自动执行查询

    def __repr__(self):
        return '<Role {}> '.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)