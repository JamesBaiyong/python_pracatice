#encoding=utf-8
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
import os, xlrd
from werkzeug.security import generate_password_hash, check_password_hash

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
    content = db.Column(db.Text())

class DegreeInfo(db.Model):
    __tablename__ = 'degree_info'
    id = db.Column(db.Integer, primary_key=True)
    degree_title = db.Column(db.String(128), unique=True, index=True)
    author= db.Column(db.String(128),index=True)
    from_where = db.Column(db.String(128),index=True)
    content = db.Column(db.Text())


def create_users():
    admin_role = Role(name='Admin')  # 实例化
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    u = User()
    u.password = 'cat'
    user_john = User(username='john', role=admin_role, email='john@flask.com', password_hash=u.password_hash)  # role属性也可使用，虽然他不是真正的数据库列，但却是一对多关系的高级表示
    user_susan = User(username='susan', role=user_role, email='susan@flask.com', password_hash=u.password_hash)
    user_david = User(username='david', role=user_role, email='david@flask.com', password_hash=u.password_hash)
    # 写入会话中
    db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan,
                        user_david])  # 准备把对象写入数据库之前，先要将其添加到会话中，数据库会话db.session和Flask session对象没有关系，数据库会话也称事物
    db.session.commit()  # 提交会话到数据库

def create_books():
    # 从excel中读取数据,存入到数据库中
    def read_excel():
        # 打开文件
        workbook = xlrd.open_workbook(u'./password/小知数据库.xlsx')
        # 获取所有sheet
        workbook.sheet_names()  # [u'sheet1', u'sheet2']
        '''
        sheet_book = workbook.sheet_by_index(1)
        sheet_user = workbook.sheet_by_index(0)
        sheet_dissertion = workbook.sheet_by_index(2)
        sheet_paper = workbook.sheet_by_index(3)
        sheet_notice = workbook.sheet_by_index(4)
        sheet_inform = workbook.sheet_by_index(5)
        sheet_lost = workbook.sheet_by_index(6)
        '''
        # 根据sheet索引或者名称获取sheet内容
        book = workbook.sheet_by_index(1)
        # sheet的名称，行数，列数
        print book.name, book.nrows, book.ncols

        # # 获取整行和整列的值（数组）
        for nrows in range(79, book.nrows):
            rows = book.row_values(nrows)  # 获取每一行内容
            for i in rows:
                print(i)
            one_data = BookInfo(
                id=int(rows[0]), book_name=rows[1].encode('utf8'),
                author=rows[2].encode('utf8'), number=int(rows[3]),
                type=rows[4].encode('utf8')
            )
            db.session.add_all([one_data])
            db.session.commit()

    read_excel()

def create_paper():
    # 期刊数据写入

    def read_excel():
        # 打开文件
        workbook = xlrd.open_workbook(u'./password/小知数据库.xlsx')
        # 获取所有sheet
        workbook.sheet_names()  # [u'sheet1', u'sheet2']
        '''
        sheet_book = workbook.sheet_by_index(1)
        sheet_user = workbook.sheet_by_index(0)
        sheet_dissertion = workbook.sheet_by_index(2)
        sheet_paper = workbook.sheet_by_index(3)
        sheet_notice = workbook.sheet_by_index(4)
        sheet_inform = workbook.sheet_by_index(5)
        sheet_lost = workbook.sheet_by_index(6)
        '''
        # 根据sheet索引或者名称获取sheet内容
        paper = workbook.sheet_by_index(3)
        # sheet的名称，行数，列数
        print paper.name, paper.nrows, paper.ncols

        # # 获取整行和整列的值（数组）
        for nrows in range(9, paper.nrows):
            rows = paper.row_values(nrows)  # 获取每一行内容
            for i in rows:
                print(i)
            one_data = PaperInfo(
                id=int(rows[0]), paper_title=rows[1].encode('utf8'),
                author=rows[2].encode('utf8'), from_where=rows[3].encode('utf8'),
                content=rows[4].encode('utf8')
            )
            db.session.add_all([one_data])
            db.session.commit()
    read_excel()

def create_degree():
    # 期刊数据写入

    def read_excel():
        # 打开文件
        workbook = xlrd.open_workbook(u'./password/小知数据库.xlsx')
        # 获取所有sheet
        workbook.sheet_names()  # [u'sheet1', u'sheet2']
        '''
        sheet_book = workbook.sheet_by_index(1)
        sheet_user = workbook.sheet_by_index(0)
        sheet_dissertion = workbook.sheet_by_index(2)
        sheet_paper = workbook.sheet_by_index(3)
        sheet_notice = workbook.sheet_by_index(4)
        sheet_inform = workbook.sheet_by_index(5)
        sheet_lost = workbook.sheet_by_index(6)
        '''
        # 根据sheet索引或者名称获取sheet内容
        paper = workbook.sheet_by_index(2)
        # sheet的名称，行数，列数
        print paper.name, paper.nrows, paper.ncols

        # # 获取整行和整列的值（数组）
        for nrows in range(1, paper.nrows):
            rows = paper.row_values(nrows)  # 获取每一行内容
            for i in rows:
                print(i)
            one_data = DegreeInfo(
                id=int(rows[0]), degree_title=rows[1].encode('utf8'),
                author=rows[2].encode('utf8'), from_where=rows[3].encode('utf8'),
                content=rows[4].encode('utf8')
            )
            db.session.add_all([one_data])
            db.session.commit()
    read_excel()

if __name__ == '__main__':
    # manager.run()
    # db.drop_all() # 删除有表
    # db.create_all() # 创建表,表名为class名
    # create_users() # 添加表中的数据
    # create_books() #　写入书籍信息到表
    # create_paper() # 写入期刊信息
    create_degree() # 写入论文信息
