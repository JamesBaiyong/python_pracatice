#encoding=utf-8
import pandas as pd
import csv
import re
import sys
import json
from collections import defaultdict
reload(sys)
sys.setdefaultencoding('utf-8')

class ClearMoney(object):
    def __init__(self):
        self.csv_file = open('./data_table/house_price.csv','w')
        self.writers = csv.writer(self.csv_file)
        self.writers.writerow(['city_name', 'house_price_list'])
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
        for city_name in self.tables:
            self.clear(city_name)
        # self.clear("chongqing")
        self.csv_file.close()

    def clear(self,city_name):
        df = pd.read_csv('./data_table/%s.csv' % city_name, encoding='utf-8')
        # 房屋面积
        house_area = df.area.values
        # 提取出房价列
        house_price = df.price.values
        print(len(house_price))
        # 提取出房类型
        house_type = df.type
        # 提取地方
        house_addres = df.position
        # 楼盘名
        house_name = df.name.values
        house_price_list = self.extract_money(house_price, house_area, house_name)
        try:
            self.writers.writerow([city_name,house_price_list])
        except:
            self.csv_file.close()

    def extract_money(self,house_price, house_area, house_name):
        # 清洗房价的格式,包括计算超预期数据
        money_list = []
        # money_dict = defaultdict(list)
        house_info = len(house_price)
        for item in range(house_info):
            money_com = re.compile('(\d+)')
            try:
                area = re.findall(money_com,house_area[item])[0]
            except:
                area = 80
            try:
                money = int(re.match(money_com,house_price[item]).group(1))
                if money <= 2000:
                    money = ((money * 10000) / area)
                money_list.append(money)
                # money_dict[house_name[item]].append(money)
            except:
                pass
        return money_list
        # money_json = json.dumps(money_dict, ensure_ascii = False, indent = 4)
        # return money_json

    def extract_address(self):
        pass

if __name__ == '__main__':
    worker = ClearMoney()
    worker.run()
