import mysql.connector

#mysql info
MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'dog'
MYSQL_PASSWORD = 'mysqlpass'
MYSQL_PORT = '3389'
MYSQL_DB = 'spider'

cnx = mysql.connector.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class SQL(object):
	def create_table(self,table_name):
		sql = "create table "+table_name+"(" \
		    "id int(11) NOT NULL AUTO_INCREMENT," \
		    "name varchar(255) DEFAULT NULL," \
		    "type varchar(255) DEFAULT NULL," \
			"price varchar(255) DEFAULT NULL," \
		    "state varchar(255) DEFAULT NULL," \
		    "position varchar(255) DEFAULT NULL," \
		    "area TEXT," \
			"hash_data TEXT,"\
		    "PRIMARY KEY (id)" \
		    ")ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;"
		cur.execute(sql)
		cnx.commit()

	def delete_table(self,table_name):
		sql = "drop table "+table_name+" ;"
		cur.execute(sql)
		cnx.commit()

	# def insert_info(self,name,author,price,url):
	def insert_info(self,name,type,price,state,position,area):
		# sql = 'INSERT INTO baiduyuedu (name,author,price,url)  \
		# 		                    VALUES (%(name)s,%(author)s,%(price)s,%(url)s)'
		# value = {
		# 	'name': name,
		# 	'author': author,
		# 	'price': price,
		# 	'url': url
		# }

		sql1 = 'INSERT INTO chongqing (name,type,price,state,position,area)  \
				                    VALUES (%(name)s,%(type)s,%(price)s,%(state)s,%(position)s,%(area)s)'
		values1 = {
			'name': name,
			'type': type,
			'price': price,
			'state': state,
			'position': position,
			'area': area
		}

		cur.execute(sql1, values1)
		cnx.commit()

if __name__ == '__main__':
	sql = SQL()
	# table_name = ['suzhou','xian','zhongshan','tianjin','nanjing','kunming','chongqing','chengdu','hangzhou','dalian','wuhan']
	# for i in table_name:
	# 	sql.create_table(i)
	# sql.delete_table('chongqing')
	sql.create_table('changsha')
	# sql.insert_info('name','author','price','url','yy','sm')