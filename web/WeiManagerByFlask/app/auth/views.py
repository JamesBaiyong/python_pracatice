#encoding=utf-8
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from froms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # 判定登录
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            # 判定邮箱和密码正确则登录账户
            login_user(user, form.remember_me.data)
            # 登录成功后的请求
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash(u'用户名或密码错误.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    # 退出登录
    logout_user()
    flash(u'已经退出登录.')
    return redirect(url_for('main.index'))