# encoding=utf-8
import MySQLdb
import csv
from utils.util import mysql_db, mysql_port, mysql_pass, mysql_user, mysql_host
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Db2csv(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
            host=mysql_host,
            user=mysql_user,
            passwd=mysql_pass,
            port=mysql_port,
            db=mysql_db,
            charset='utf8')
        self.cur = self.conn.cursor()

    def release_db(self):
        self.cur.close()
        self.conn.close()

    def read_data(self, table_name):
        select_sql = """select name,type,price,state,position,area from {};""".format(
            table_name)
        self.cur.execute(select_sql)
        csvfile = file('./data_table/%s.csv' % table_name, 'wb')
        writers = csv.writer(csvfile)
        writers.writerow(['name', 'type', 'price', 'state', 'position','area'])
        while True:
            lines = self.cur.fetchmany(50)
            if len(lines) == 0:
                break
            for i in lines:
                writers.writerows([i])
        csvfile.close()

    def main(self):
        tables = [
            'zhongshan',
            'chongqing',
            'changsha',
            'chengdu',
            'dalian',
            'hangzhou',
            'kunming',
            'nanjing',
            'tianjin',
            'wuhan',
            'xian']
        try:
            for table in tables:
                self.read_data(table_name=table)
        finally:
            self.release_db()


clear = Db2csv()
clear.main()
