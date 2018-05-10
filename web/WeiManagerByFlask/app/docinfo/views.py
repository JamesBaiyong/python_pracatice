#encoding=utf-8
from flask import render_template

from . import doc

@doc.route('/book_info')
def booksinfo():
    # 图书信息

    return render_template('docinfo/bookinfo.html')

@doc.route('/paper_info')
def paperinfo():
    # 期刊论文信息

    return render_template('docinfo/paperinfo.html')

@doc.route('/degree_info')
def degreeinfo():
    # 期刊论文信息

    return render_template('docinfo/degreeinfo.html')