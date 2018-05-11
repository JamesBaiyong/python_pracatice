#encoding=utf-8
from flask import render_template, request
from froms import BookListForm
from . import doc
from ..models import BookInfo, PaperInfo, DegreeInfo

@doc.route('/book_info')
def booksinfo():
    # 图书信息

    books = BookInfo.query.all()
    return render_template('docinfo/bookinfo.html', booklists=books)

@doc.route('/paper_info')
def paperinfo():
    # 期刊论文信息

    paper = PaperInfo.query.all()
    return render_template('docinfo/paperinfo.html', paperlists=paper)

@doc.route('/degree_info')
def degreeinfo():
    # 期刊论文信息

    degree = DegreeInfo.query.all()
    return render_template('docinfo/degreeinfo.html', degreelists=degree)