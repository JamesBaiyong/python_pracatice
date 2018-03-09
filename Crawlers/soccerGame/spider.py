# encoding=utf-8
from conf.SimpleWorker import Worker
from conf.util import get_random_ua,soccer_hupu_extractors_dict
import requests
import datetime
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Spider(Worker):
    def __init__(self):
        super(Spider, self).__init__()
        self.url = 'https://soccer.hupu.com/home/ajax-match'
        self.ua = get_random_ua()
        self.when = self.get_time()

    def get_web(self):
        self.logger.info("获取网页信息...")
        session = requests.get(self.url, self.ua)
        # http_content = session.content
        http_dict_content = session.json()
        return http_dict_content

    def get_message(self):
        http_content = self.get_web()
        messages = soccer_hupu_extractors_dict(http_content)
        for message in messages:
            self.logger.debug(json.dumps(message,ensure_ascii=False,))
        return messages

    def run(self):
        messages = self.get_message()
        self.logger.info("正在将信息写到本地...")
        for message in messages:
            with open('reslut.txt','a') as f :
                f.write("="*20)
                f.write("\n")
            for k,v in message.iteritems():
                with open('reslut.txt','a') as f:
                    f.write(k+" : "+v)
                    f.write('\n')

    @staticmethod
    def get_time():
            #暂时没用
        return datetime.datetime.now().strftime("%Y.%m.%d").replace('.', '-')

if __name__ == '__main__':
    sp = Spider()
    sp.run()
