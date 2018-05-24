#encoding=utf-8

from flask import render_template, flash, url_for, redirect
from flask_login import login_required, current_user
from ..models import *
from . import manager
from froms import UsersForm, UsersChangeForm

@manager.route('/manager_index')
@login_required
def manger_index():
    return render_template('manager/index.html')

@manager.route('/manager_users',methods=['GET', 'POST'])
@login_required
def manger_users():
    form = UsersForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.title.data).first()
        if user:
            flash(u'用户信息如下,请谨慎操作')
            user_info = User.query.filter_by(id=user.id).first_or_404()
            return render_template('manager/manager_users.html', form=form, user_info=user_info)
        flash(u'数据库中不存在该用户')
    return render_template('manager/manager_users.html',form=form)

@manager.route('/change_user/<user_id>',methods=['GET', 'POST'])
@login_required
def chage_user(user_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))

    form = UsersChangeForm()
        # 按照查询出的用户id去修改用户信息,确保修改的用户为特定用户
    user = User.query.filter_by(id=int(user_id)).first_or_404()
    u = User()
    if form.validate_on_submit():
        user.email=form.user_email.data,
        user.username=form.name.data,
        # 需要实例化用户表,调用计算password的hash方法
        u.password = form.password.data
        user.password_hash=u.password_hash,

        user.borrownum=form.b_number.data,
        user.borrowing=form.b_status.data,
        user.borrowTime=form.b_date.data,
        user.returnTime=form.r_date.data,
        user.cost=form.cost.data
        db.session.commit()
        flash(u'你已经成功更新用户所有信息')
        return render_template('manager/index.html')
    return render_template('manager/change_users.html', form=form, user=user)

@manager.route('/manager_notice')
@login_required
def manger_notice():
    return render_template('manager/manager_notice.html')

@manager.route('/manager_docinfo')
@login_required
def manger_docinfo():
    return render_template('manager/manager_docinfo.html')