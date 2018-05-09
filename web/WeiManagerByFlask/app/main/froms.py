# encoding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField(u'请输入你的姓名?', validators=[DataRequired()])
    submit = SubmitField(u'提交')
