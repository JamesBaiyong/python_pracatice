#encoding=utf-8

from flask import render_template
from flask_login import login_required
from ..models import *
from . import manager

@manager.route('/manager_index')
@login_required
def manger_index():
    return render_template('manager/index.html')

@manager.route('/manager_users')
@login_required
def manger_users():
    return render_template('manager/manager_users.html')

@manager.route('/manager_notice')
@login_required
def manger_notice():
    return render_template('manager/manager_notice.html')

@manager.route('/manager_docinfo')
@login_required
def manger_docinfo():
    return render_template('manager/manager_docinfo.html')