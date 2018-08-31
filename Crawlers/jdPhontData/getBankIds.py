# encoding=utf-8
import requests
import csv
import json
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")
from config.loggingSet import SetLog
log = SetLog()
logger = log.create_logger()

class GetBankIds(object):
    def __init__(self):
        self.url = 'https://wx.cq.abchina.com/jd/mall/Product/GetList'
        self.headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
            " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def get_req(self, url, send_data):
        res = requests.post(url, headers=self.headers, data=send_data)
        return res

    def get_data(self, res_content):
        source_data = json.loads(res_content)
        ids = source_data["result"]["hitResult"]
        for id in ids:
            temp_data = {}
            temp_data["brand"] = str(id["brand"])
            temp_data["wareName"] = str(id["wareName"])
            temp_data["wareId"] = str(id["wareId"])
            temp_data["price"] = str(id["price"])
            self.save_data(temp_data)

    def save_data(self, temp_data):
        logger.info(u"写入数据%s"%temp_data.get("wareId",None))
        outputFile = open('output.csv', 'a', )
        try:
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow([temp_data["brand"].encode("utf8"),temp_data["wareName"].encode("utf8"),
                                   temp_data["wareId"].encode("utf8"),temp_data["price"].encode("utf8")])
        except:
            import traceback
            print(traceback.print_exc())
            logger.error(u"数据错误")
        finally:
            outputFile.close()

    def run(self):
        send_data = {"catId": "655", "brands": "", "min": "", "max": "", "pageIndex": 1, "pageSize": 12}
        res = self.get_req(self.url, json.dumps(send_data))
        if res.status_code == 200:
            total_page = int(json.loads(res.content)['result']['pageCount'])
            for i in range(1,(total_page+1)):
                logger.debug(u"抓取第%s页,总共%s页"%(i,total_page))
                res = self.get_req(self.url, json.dumps(send_data))
                send_data["pageIndex"] = i
                self.get_data(res.content)
                time.sleep(1)
        else:
            print(res.content)



if __name__ == '__main__':
    worker = GetBankIds()
    worker.run()
