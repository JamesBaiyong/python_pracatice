#encoding=utf-8

from flask import render_template, flash, url_for, redirect
from flask_login import login_required, current_user
from ..models import *
from . import manager
from froms import UsersForm, UsersChangeForm, LostAndFoundForm, InformInfoForm, NoticeInfoForm, DocForm, ChangeDegreeForm
import datetime

@manager.route('/manager_index')
@login_required
def manger_index():
    return render_template('manager/index.html')

# 用户模块
@manager.route('/manager_users',methods=['GET', 'POST'])
@login_required
def manger_users():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
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


@manager.route('/delete_user/<user_id>',methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))

    user = User.query.filter_by(id=int(user_id)).first_or_404()
    db.session.delete(user)
    db.session.commit()
    flash(u'你已经成功删除该用户所有信息')
    return render_template('manager/index.html')

# 通知模块
@manager.route('/manager_notice')
@login_required
def manger_notice():
    return render_template('manager/manager_notice.html')

@manager.route('/manager_change_lost')
@login_required
def manger_lost():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    lost = LostAndFoundInfo.query.all()
    return render_template('manager/manager_change_lost.html',lostlists=lost)

@manager.route('/change_lost/<lost_id>',methods=['GET', 'POST'])
@login_required
def change_lost(lost_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = LostAndFoundForm()
    lost = LostAndFoundInfo.query.filter_by(id=int(lost_id)).first_or_404()
    if form.validate_on_submit():
        lost.lost_content = form.lost_content.data
        lost.pub_time =form.date_time.data
        db.session.commit()
        flash(u'你已经成功更新失物招领信息')
        lost_list = LostAndFoundInfo.query.all()
        return render_template('manager/manager_change_lost.html',lostlists=lost_list)
    return render_template('manager/change_lost_info.html', form=form)

@manager.route('/delete_lost/<lost_id>',methods=['GET', 'POST'])
@login_required
def delete_lost(lost_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    lost = LostAndFoundInfo.query.filter_by(id=int(lost_id)).first_or_404()
    db.session.delete(lost)
    db.session.commit()
    flash(u'你已经成功该条失物招领信息')
    lost_list = LostAndFoundInfo.query.all()
    return render_template('manager/manager_change_lost.html', lostlists=lost_list)

@manager.route('/add_lost',methods=['GET', 'POST'])
@login_required
def add_lost():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = LostAndFoundForm()
    lost = LostAndFoundInfo()
    if form.validate_on_submit():
        lost.lost_content = form.lost_content.data
        lost.pub_time =form.date_time.data
        db.session.add(lost)
        db.session.commit()
        flash(u'你已经成功增加失物招领信息')
        lost_list = LostAndFoundInfo.query.all()
        return render_template('manager/manager_change_lost.html',lostlists=lost_list)
    return render_template('manager/change_lost_info.html', form=form)

@manager.route('/manager_change_inform')
@login_required
def manger_inform():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    inform = InformInfo.query.all()
    return render_template('manager/manager_change_inform.html',informlists=inform)

@manager.route('/change_inform/<inform_id>',methods=['GET', 'POST'])
@login_required
def change_inform(inform_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = InformInfoForm()
    inform = InformInfo.query.filter_by(id=int(inform_id)).first_or_404()
    if form.validate_on_submit():
        inform.inform_title = form.title.data
        inform.inform_content =form.content.data
        inform.create_time = datetime.datetime.now()
        db.session.commit()
        flash(u'你已经成功更新信息')
        inform_list = InformInfo.query.all()
        return render_template('manager/manager_change_inform.html',informlists=inform_list)
    return render_template('manager/change_inform_info.html', form=form)

@manager.route('/delete_inform/<lost_id>',methods=['GET', 'POST'])
@login_required
def delete_inform(lost_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    inform = InformInfo.query.filter_by(id=int(lost_id)).first_or_404()
    db.session.delete(inform)
    db.session.commit()
    flash(u'你已经成功该条失物招领信息')
    inform_list = InformInfo.query.all()
    return render_template('manager/manager_change_inform.html', informlists=inform_list)

@manager.route('/add_inform',methods=['GET', 'POST'])
@login_required
def add_inform():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = InformInfoForm()
    inform = InformInfo()
    if form.validate_on_submit():
        inform.inform_title = form.title.data
        inform.inform_content =form.content.data
        inform.create_time = datetime.datetime.now()
        db.session.add(inform)
        db.session.commit()
        flash(u'你已经成功增加失物招领信息')
        inform_list = InformInfo.query.all()
        return render_template('manager/manager_change_inform.html', informlists=inform_list)
    return render_template('manager/change_inform_info.html', form=form)

@manager.route('/manager_change_notice')
@login_required
def manger_change_notice():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    notice = NoticeInfo.query.all()
    return render_template('manager/manager_change_notice.html',noticelists=notice)

@manager.route('/change_notice/<notice_id>',methods=['GET', 'POST'])
@login_required
def change_notice(notice_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = NoticeInfoForm()
    notice = NoticeInfo.query.filter_by(id=int(notice_id)).first_or_404()
    if form.validate_on_submit():
        notice.notice_title = form.title.data
        notice.notice_content =form.content.data
        notice.create_time = datetime.datetime.now()
        db.session.commit()
        flash(u'你已经成功更新信息')
        notice_list = NoticeInfo.query.all()
        return render_template('manager/manager_change_notice.html',noticelists=notice_list)
    return render_template('manager/change_notice_info.html', form=form)

@manager.route('/delete_notice/<notice_id>',methods=['GET', 'POST'])
@login_required
def delete_notice(notice_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    notice = NoticeInfo.query.filter_by(id=int(notice_id)).first_or_404()
    db.session.delete(notice)
    db.session.commit()
    flash(u'你已经成功删除该条失物招领信息')
    notice_list = NoticeInfo.query.all()
    return render_template('manager/manager_change_notice.html', noticelists=notice_list)

@manager.route('/add_notice',methods=['GET', 'POST'])
@login_required
def add_notice():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = NoticeInfoForm()
    notice = NoticeInfo()
    if form.validate_on_submit():
        notice.notice_title = form.title.data
        notice.notice_content =form.content.data
        notice.create_time = datetime.datetime.now()
        db.session.add(notice)
        db.session.commit()
        flash(u'你已经成功增加公告信息')
        notice_list = NoticeInfo.query.all()
        return render_template('manager/manager_change_notice.html', noticelists=notice_list)
    return render_template('manager/change_notice_info.html', form=form)


# 图书信息
@manager.route('/manager_docinfo', methods=['GET', 'POST'])
@login_required
def degree_info():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = DocForm()
    if form.validate_on_submit():
        degree = DegreeInfo.query.filter_by(degree_title=form.title.data).first()
        if degree:
            flash(u'学位论文信息如下,请谨慎操作')
            degree_info = DegreeInfo.query.filter_by(id=degree.id).first_or_404()
            return render_template('manager/manager_degree_info.html', form=form, degree=degree_info)
        flash(u'数据库中不存在该论文')
    return render_template('manager/manager_degree_info.html', form=form)

# 图书信息
@manager.route('/change_degree/<degree_id>', methods=['GET', 'POST'])
@login_required
def change_degree(degree_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = ChangeDegreeForm()
    degree = DegreeInfo.query.filter_by(id=int(degree_id)).first_or_404()
    if form.validate_on_submit():
        degree.degree_title = form.degree_title.data
        degree.author = form.author.data
        degree.from_where = form.from_where.data
        degree.content = form.content.data
        db.session.commit()
        flash(u'你已经成功更新学位论文所有信息')
        return render_template('manager/index.html')
    return render_template('manager/change_degree_info.html', form=form)

@manager.route('/add_degree',methods=['GET', 'POST'])
@login_required
def add_degree():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = ChangeDegreeForm()
    degree = DegreeInfo()
    if form.validate_on_submit():
        degree.degree_title = form.degree_title.data
        degree.author = form.author.data
        degree.from_where = form.from_where.data
        degree.content = form.content.data
        db.session.add(degree)
        db.session.commit()
        flash(u'你已经成功添加学位论文所有信息')
        return render_template('manager/index.html')
    return render_template('manager/change_degree_info.html', form=form)

@manager.route('/delete_degree/<notice_id>',methods=['GET', 'POST'])
@login_required
def delete_degree(notice_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))

    form = DocForm()
    degree = DegreeInfo.query.filter_by(id=int(notice_id)).first_or_404()
    db.session.delete(degree)
    db.session.commit()
    flash(u'你已经成功删除该条学位论文信息')
    inform_list = InformInfo.query.all()
    return render_template('manager/change_degree_info.html', form=form)


@manager.route('/manager_paper', methods=['GET', 'POST'])
@login_required
def paper_info():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = DocForm()
    if form.validate_on_submit():
        paper = PaperInfo.query.filter_by(paper_title=form.title.data).first()
        if paper:
            flash(u'期刊论文信息如下,请谨慎操作')
            paper = PaperInfo.query.filter_by(id=paper.id).first_or_404()
            return render_template('manager/manager_paper_info.html', form=form, paper=paper)
        flash(u'数据库中不存在该论文')
    return render_template('manager/manager_paper_info.html', form=form)


@manager.route('/change_paper/<paper_id>', methods=['GET', 'POST'])
@login_required
def change_paper(paper_id):
    print(type(paper_id))
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = ChangeDegreeForm()
    paper = DegreeInfo.query.filter_by(id=int(paper_id)).first_or_404()
    if form.validate_on_submit():
        paper.paper_title = form.degree_title.data
        paper.author = form.author.data
        paper.from_where = form.from_where.data
        paper.content = form.content.data
        db.session.commit()
        flash(u'你已经成功更新期刊论文信息')
        return render_template('manager/index.html')
    return render_template('manager/change_degree_info.html', form=form)

@manager.route('/add_paper',methods=['GET', 'POST'])
@login_required
def add_paper():
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))
    form = ChangeDegreeForm()
    degree = PaperInfo()
    if form.validate_on_submit():
        degree.paper_title = form.degree_title.data
        degree.author = form.author.data
        degree.from_where = form.from_where.data
        degree.content = form.content.data
        db.session.add(degree)
        db.session.commit()
        flash(u'你已经成功添加期刊论文所有信息')
        return render_template('manager/index.html')
    return render_template('manager/change_degree_info.html', form=form)

@manager.route('/delete_paper/<notice_id>',methods=['GET', 'POST'])
@login_required
def delete_paper(notice_id):
    # 增加角色判断,以防普通用户对别的用户做修改
    if current_user.role_id != 1:
        flash(u'很抱歉,只有管理员才能访问相应页面')
        return redirect(url_for('main.index'))

    paper = PaperInfo.query.filter_by(id=int(notice_id)).first_or_404()
    db.session.delete(paper)
    db.session.commit()
    flash(u'你已经成功删除该条期刊论文信息')
    return render_template('manager/index.html')