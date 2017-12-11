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
		    "area varchar(255) DEFAULT NULL," \
		    "PRIMARY KEY (id)" \
		    ")ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;"
		cur.execute(sql)
		cnx.commit()

if __name__ == '__main__':
	sql = SQL()
	# sql.create_table('chongqing')
	sql.create_table('chengdu')
