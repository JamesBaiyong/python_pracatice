# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeimenghuanbaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 项目名称
    project_name = scrapy.Field()
    # 建设地点
    location = scrapy.Field()
    # 建设单位
    company = scrapy.Field()
    # 环境影响评价机构
    institution = scrapy.Field()
    # 受理日期
    accept_date = scrapy.Field()
    # 当前页面
    url = scrapy.Field()
    
