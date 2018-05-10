# encoding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    # 用户登录
    email = StringField(u'请输入用户邮箱', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField(u'请输入密码', validators=[DataRequired()])
    remember_me = BooleanField(u'保持登录')
    submit = SubmitField(u'登录')

class RegistrationForm(FlaskForm):
    # 用户注册
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField(u'用户名', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               u'用户名必须是英文小写,数字,句号,或则下划线')])
    password = PasswordField(u'密码', validators=[
        DataRequired(), EqualTo('password2', message=u'两次密码不相同')])
    password2 = PasswordField(u'确认密码', validators=[DataRequired()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'此邮箱已注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户已存在')