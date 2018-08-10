#encoding=utf-8
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User, db
from froms import LoginForm, RegistrationForm
from ..email import send_email

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # 判定登录
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            user_id = user.id
            # 判定邮箱和密码正确则登录账户
            login_user(user, form.remember_me.data)
            # 登录成功后的请求
            next = request.args.get('next')
            print(current_user.username)

            if current_user.role_id == 1:
                # 判断登录后的账户是否确认
                if not current_user.confirmed:
                    return render_template('auth/unconfirmed.html')
                next = url_for('manager.manger_index')
                return redirect(next)

            if next is None or not next.startswith('/'):
                # 判断登录后的账户是否确认
                if not current_user.confirmed:
                    return render_template('auth/unconfirmed.html')
                next = url_for('auth.users_info', id=user_id)
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

@auth.route('/register', methods=['GET', 'POST'])
def register():
    # 用户注册
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(u'请登录邮箱确认账户')
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account',
                   'auth/email/confirm', user=user, token=token)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    # 处理确认账号链接
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash(u'您的账号已确认成功,感谢您的注册.')
    else:
        flash(u'确认连接已失效,请重新确认')
    return redirect(url_for('main.index'))


@auth.route('/confirm')
@login_required
def resend_confirmation():
    # 重发确认账户链接
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash(u'一封新的账户确认链接已经发送到您的邮箱')
    return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
    # 重定向未注册用户访问链接
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint \
            and request.endpoint[:5] != 'auth.' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    # 重定向未确认账户
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

@auth.route('/users')
def users_info():
    userid = request.args.get('id')
    if userid:
        users_info = User.query.filter_by(id=userid).first_or_404()
        return render_template('auth/users.html', user_info=users_info, userid=int(userid))
    return redirect(url_for('main.index'))