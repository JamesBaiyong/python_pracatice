#coding=utf-8
import mysql.connector
from .. import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class SQL(object):

	#执行插入数据库语句
	@classmethod
	def insert_info(cls,table_name,name,type,price,state,position,area,hash_data):
		sql = 'INSERT INTO '+table_name+' (name,type,price,state,position,area,hash_data)  \
						                    VALUES (%(name)s,%(type)s,%(price)s,%(state)s,%(position)s,%(area)s,%(hash_data)s)'
		values = {
			'name': name,
			'type': type,
			'price': price,
			'state': state,
			'position': position,
			'area': area,
			'hash_data':hash_data
		}
		cur.execute(sql,values)
		cnx.commit()

	#查重
	@classmethod
	def select_name(cls,table_name,hash_data):
		sql = "SELECT EXISTS(SELECT 1 FROM "+ table_name +" WHERE hash_data=%(hash_data)s)"
		value = {
			'hash_data': hash_data
		}
		cur.execute(sql,value)
		return cur.fetchall()[0]
