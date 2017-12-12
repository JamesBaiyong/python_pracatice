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
	def insert_info(cls,table_name,name,type,price,state,position,area):
		sql = "INSERT INTO " + table_name +" (name,author,price,url)  \
		        VALUES (%(name)s,%(type)s,%(price)s,%(price)s,%s(state)s,%(position)s,%(area)s)"
		value = {
			'name': name,
			'type': type,
			'price': price,
			'state': state,
			'position': position,
			'area': area
		}
		cur.execute(sql,value)
		cnx.commit()

	#查重
	@classmethod
	def select_name(cls,table_name,name):
		sql = "SELECT EXISTS(SELECT 1 FROM " + table_name +" WHERE name=%(name)s)"
		value = {
			'name': name
		}
		cur.execute(sql,value)
		return cur.fetchall()[0]
