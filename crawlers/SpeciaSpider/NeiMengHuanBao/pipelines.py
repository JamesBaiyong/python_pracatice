# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
class NeimenghuanbaoPipeline(object):
    wb = Workbook()
    ws = wb.active
    ws.append(['项目名称','建设地点','建设单位','环境影响评价机构','受理日期','当前页URL'])  # 设置表头

    def process_item(self, item, spider):
        line = [item['project_name'], item['location'],
                item['company'], item['institution'],
                item['accept_date'], item['url']]  # 把数据中每一项整理出来

        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        name = u'****数据.csv'
        self.wb.save(name)  # 保存xlsx文件
        return item
