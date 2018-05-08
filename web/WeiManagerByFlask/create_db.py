#encoding=utf-8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
# 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dog:dogpass@localhost:3306/wei_manager'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)


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

def create_users():
    admin_role = Role(name='Admin')  # 实例化
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_john = User(username='john', role=admin_role)  # role属性也可使用，虽然他不是真正的数据库列，但却是一对多关系的高级表示
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)
    # 写入会话中
    db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan,
                        user_david])  # 准备把对象写入数据库之前，先要将其添加到会话中，数据库会话db.session和Flask session对象没有关系，数据库会话也称事物
    db.session.commit()  # 提交会话到数据库

if __name__ == '__main__':
    manager.run()
    # db.drop_all() # 删除有表
    # db.create_all() # 创建表,表名为class名
    # create_users() # 添加表中的数据
