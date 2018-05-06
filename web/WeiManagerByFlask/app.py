#encoding=utf-8
from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import abort # 处理错误
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

def load_user(id):
    user_dict = {
        1:'Jake',
        2:'James'
        }
    return user_dict.get(id,None)

@app.route('/')
def index():
 response = make_response('<h1>This document carries a cookie!</h1>')
 response.set_cookie('answer', '42')
 return render_template('index.html')

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
