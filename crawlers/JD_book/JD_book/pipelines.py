# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import  Workbook

class JdBookPipeline(object):

    wb = Workbook()
    ws = wb.active
    ws.append(['销售排名','书名','作者','现价','原价','出版社'])  # 设置表头

    def process_item(self, item, spider):
        line = [item['number'], item['book_name'],
                item['author'],item['preferential_price'],
                item['price'],item['press']]  # 把数据中每一项整理出来

        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('./JD_book1.xlsx')  # 保存xlsx文件
        return item