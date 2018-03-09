#coding=utf-8
from scrapy.cmdline import execute
# execute(['scrapy','crawl','NeiMengHuanBao','-o ******.csv']) #直接输出CSV格式，office打开会有乱码
execute(['scrapy','crawl','NeiMengHuanBao'])
