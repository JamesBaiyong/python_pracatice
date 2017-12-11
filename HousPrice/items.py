# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouspriceItem(scrapy.Item):
    #房产名
    name = scrapy.Field()
    #地理位置
    position = scrapy.Field()
    #房型
    type = scrapy.Field()
    #房价
    price = scrapy.Field()
    #区域空间
    area = scrapy.Field()
    #销售情况
    state = scrapy.Field()
