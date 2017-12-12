#coding=utf-8
from scrapy.cmdline import execute

# execute(['scrapy','crawl','HouseSpider_ChongQing'])
execute(['scrapy','crawl','HousePrice'])

# execute(['scrapy','crawl','HousePrice',u'-o 成都新房信息.csv'])