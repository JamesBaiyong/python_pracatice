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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you never can guess it'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


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
    old_name = session.get('name')
    if old_name is not None and old_name != form.name.data:
        flash(u'修改名称成功！')
    session['name'] = form.name.data
    return redirect(url_for('index'))
 return render_template('index.html', form=form, name=session.get('name'))

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


if __name__ == '__main__':
    manager.run()
