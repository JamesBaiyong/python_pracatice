# encoding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, ValidationError, \
    TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from ..models import User

class UsersForm(FlaskForm):
    title = StringField(u'用户检索', validators=[DataRequired(), Length(1, 64),Email()])
    # status = RadioField(u'是否完成', validators=[DataRequired()],  choices=[("1", u'是'),("0",u'否')])
    submit = SubmitField(u'提交')

class UsersChangeForm(FlaskForm):
    name = StringField(u'用户名修改', validators=[DataRequired(), Length(1, 64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,u'用户名必须是英文小写,数字,句号,或则下划线')])
    user_email = StringField(u'用户邮箱', validators=[DataRequired(), Length(1, 64),Email()])
    password = PasswordField(u'密码', validators=[
        DataRequired(), EqualTo('password2', message=u'两次密码不相同')])
    password2 = PasswordField(u'确认密码', validators=[DataRequired()])
    b_number = IntegerField(u'借阅数：')
    b_status = StringField(u'借阅情况：')
    b_date = DateField(u'借阅时间')
    r_date = DateField(u'归还时间')
    cost = IntegerField(u'资费')
    submit = SubmitField(u'更新用户状态')

    # 以validate_开头后面跟字段名,做检验
    def validate_user_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'此邮箱已存在')

    def validate_name(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'此用户已存在')

class LostAndFoundForm(FlaskForm):
    lost_content = TextAreaField(u'失误招领正文')
    date_time = DateField(u'发布时间')
    submit = SubmitField(u'提交')