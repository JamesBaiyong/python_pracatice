#encoding=utf-8
from flask import render_template, flash
from froms import BookListForm
from . import doc
from ..models import BookInfo, PaperInfo, DegreeInfo

@doc.route('/book_info', methods=['GET', 'POST'])
def booksinfo():
    # 图书信息
    form = BookListForm()
    books = BookInfo.query.all()
    if form.validate_on_submit():
        book = BookInfo.query.filter_by(book_name=form.title.data).first()
        if book:
            flash(u'已找到%s'%book.book_name)
            book = BookInfo.query.filter_by(id=book.id).first_or_404()
            return render_template('docinfo/bookinfo.html', book=book, form=form)
        flash(u'暂无%s'%form.title.data)
    return render_template('docinfo/bookinfo.html', booklists=books, form=form)

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