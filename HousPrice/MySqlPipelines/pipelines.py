#encoding=utf-8

from ..items import HouspriceItem
from sql import SQL

class HousePricePipeline(object):

	def process_item(self, item, spider):
		if isinstance(item, HouspriceItem):
			hash_data = item['hash_data']
			table_name = item['table']
			# TODO 带数据库表名
			ret = SQL.select_name(table_name,hash_data)
			if ret[0] == 1:
				print ('数据已存在。')
			else:
				name = item['name']
				type = item['type']
				price = item['price']
				state = item['state']
				position = item['position']
				area = item['area']
				SQL.insert_info(table_name,name,type,price,state,position,area,hash_data)
				print ('一条数据入库中...')