#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length

class BookListForm(FlaskForm):
    title = StringField(u'标题', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField(u'检索')