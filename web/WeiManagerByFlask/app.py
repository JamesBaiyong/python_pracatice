#encoding=utf-8
from flask import Flask, render_template, session, redirect, url_for, flash
from flask import request
from flask import make_response
from flask import abort # 处理错误
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from create_db import User,Role
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message
from password.password import  MAIL_PASSWORD, MAIL_USERNAME, FLASK_ADMIN
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you never can guess it'
# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dog:dogpass@localhost:3306/wei_manager'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 邮件配置
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['FLASKY_MAIL_SENDER'] = 'Wei-Manager Admin <robotinfo@126.com>'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = u'[小知]'
app.config['FLASKY_ADMIN'] = FLASK_ADMIN

db = SQLAlchemy(app)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

mail = Mail(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


def load_user(id):
    user_dict = {
        1:'Jake',
        2:'James'
        }
    return user_dict.get(id,None)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], u'新用户',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

# 注册了程序、数据库实例以及模型
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(int(id))
    # if not user:
    #     abort(404)
    return render_template('user.html', name=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

if __name__ == '__main__':
    manager.run()
