#encoding=utf-8

from ..items import HouspriceItem
from sql import SQL

class HousePricePipeline(object):

	def process_item(self, item, spider):
		if isinstance(item, HouspriceItem):
			name = item['name']
			# TODO 带数据库表名
			ret = SQL.select_name(name)
			if ret[0] == 1:
				print ('数据已存在。')
			else:
				name = item['name']
				type = item['type']
				price = item['price']
				state = item['state']
				position = item['position']
				area = item['area']
				SQL.insert_info(name, type, price,state,position,area)
				print ('入库中...')