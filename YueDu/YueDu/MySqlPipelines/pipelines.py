#coding=utf-8
from .sql import SQL
from ..items import YueduItem

class YueDuPipeline(object):
	'''
	将数据存入数据库
	'''
	def process_item(self,item,spider):
		if isinstance(item,YueduItem):
			name = item['name']
			ret = SQL.select_name(name)
			if ret[0] == 1:
				print ('数据已存在。')
				pass
			else:
				name = item['name']
				author = item['author']
				price = item['price']
				url = item['url']
				SQL.insert_info(name,author,price,url)
				print ('入库中...')

