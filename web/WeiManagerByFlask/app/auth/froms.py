# encoding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField(u'请输入用户邮箱', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField(u'请输入密码', validators=[DataRequired()])
    remember_me = BooleanField(u'保持登录')
    submit = SubmitField(u'登录')
