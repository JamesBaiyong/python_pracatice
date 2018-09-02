#encoding=utf-8
import sqlite3
class Sqlite3(object):
    def save_data(self, data):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        data_value = tuple(data)
        save_sql = """INSERT INTO price (id,name,title,bank_price,jd_price) 
                  VALUES (%s,%s,%s,%s,%s)"""%(data_value)
        c.execute(save_sql)
        conn.commit()
        print "Records created successfully"
        conn.close()

    def create_db(self):
        conn = sqlite3.connect('jdPrice.db')
        print "Opened database successfully"
        c = conn.cursor()
        c.execute('''CREATE TABLE price
               ( id PRIMARY KEY     NOT NULL,
               name           TEXT    NOT NULL,
               title            INT     NOT NULL,
               bank_price        text,
               jd_price         text);''')
        print "Table created successfully"
        conn.commit()
        conn.close()

if __name__ == '__main__':
    worker = Sqlite3()
    worker.create_db()
    worker.get_conn()