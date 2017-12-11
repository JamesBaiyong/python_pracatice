# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import  Workbook

class HouspricePipeline(object):

    wb = Workbook()
    ws = wb.active
    ws.append(['房名', '地区', '房型', '价格', '房类','出售情况'])

    def process_item(self, item, spider):


        line = [item['name'],item['position'],
                item['area'],item['price'],
                item['type'],item['state']]
        self.ws.append(line)
        self.wb.save(u'./重庆新房.xlsx')
        return item


