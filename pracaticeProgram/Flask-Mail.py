import os
from flask import Flask
from flask_mail import Mail, Message
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.163.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER = 'JamesBy <youremail@163.com>'
))

mail = Mail(app)


@app.route('/')
def index():
        msg = Message("EmailTest" ,recipients=['someone@outlook.com'])
        msg.body = "Hello World! This  Email from Web"
        mail.send(msg)
        return '<h3>Sended  email to U! ^^</h3>'

if __name__=='__main__':
        manager.run()