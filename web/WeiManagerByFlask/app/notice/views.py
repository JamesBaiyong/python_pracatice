#encoding=utf-8
from flask import render_template
from . import notice
from ..models import NoticeInfo, InformInfo, LostAndFoundInfo

@notice.route('/notice_info')
def noticeinfo():
    # 通知信息

    notice = NoticeInfo.query.all()
    print(notice)
    return render_template('notice/noticeinfo.html', noticelists=notice)

@notice.route('/inform_info')
def infominfo():
    # 公告信息信息

    inform = InformInfo.query.all()
    return render_template('notice/informinfo.html', informlists=inform)

@notice.route('/lost_info')
def lostinfo():
    # 失物招领信息

    lost = LostAndFoundInfo.query.all()
    return render_template('notice/lostinfo.html', lostlists=lost)