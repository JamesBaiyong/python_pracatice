#encoding=utf-8
import pandas as pd
import csv
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ClearMoney(object):
    def __init__(self):
        self.tables = [
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
    def run(self):
        # for city_name in self.tables:
        #     self.clear(city_name)
        self.clear("chongqing")

    def clear(self,city_name):
        df = pd.read_csv('./data_table/%s.csv' % city_name, encoding='utf-8')
        # 房屋面积
        house_area = df.area.values
        # 提取出房价列
        house_price = df.price.values
        print(len(house_price))
        self.extract_money(house_price,house_area)
        # 提取出房类型
        house_type = df.type
        # 提取地方
        house_addres = df.position
        # 楼盘名
        house_name = df.name

    def extract_money(self,house_price,house_area):
        # 清洗钱的格式,包括计算超预期数据
        money_list = []
        house_info = len(house_price)
        for item in range(house_info):
            money_com=re.compile('(\d+)')
            try:
                area = re.findall(money_com,house_area[item])[0]
            except IndexError:
                area = 100
            try:
                money = re.match(money_com,house_price[item]).group(1)
                if money <= 2000:
                    print(area)
                    money = ((money * 10000) / area)
            except AttributeError:
                money=pd.NaT
            money_list.append(money)
        print(len(money_list))
        print(money_list)


    def extract_address(self):
        pass

if __name__ == '__main__':
    worker = ClearMoney()
    worker.run()
