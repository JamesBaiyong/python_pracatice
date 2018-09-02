#encoding=utf-8
import csv
import json
import requests
import time
from config.loggingSet import SetLog

log = SetLog()
logger = log.create_logger()

class GetPrice(object):
    def run(self):
        ids = self.get_ids()
        print(len(ids))
        for id in ids:
            logger.info('get data by id:%s'%id[2])
            res = self.get_price(id[2])
            try:
                price = json.loads(res.content[2:-4])
            except:
                logger.error('requests error :%s'%res.content)
                price = {}
            id.append(price.get("p", "Error"))
            self.save_data(id)
            time.sleep(1)

    def get_ids(self):
        file = open('output.csv')
        try:
            reader = csv.reader(file)
            data = list(reader)
        finally:
            file.close()
        return data

    def get_price(self, id):
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        url = 'https://p.3.cn/prices/mgets?callback=&skuIds=J_%s'%id
        res = requests.get(url, headers=headers)
        return res

    def save_data(self, data):
        outputFile = open('jdoutput.csv', 'a', )
        try:
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow(data)
        except:
            import traceback
            print(traceback.print_exc())
            logger.error(u"数据错误")
        finally:
            outputFile.close()

if __name__ == '__main__':
    worker = GetPrice()
    worker.run()
