#encoding=utf-8
import pandas as pd
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
province = {
    'zhongshan':'中山',
    'chongqing':'重庆',
    'changsha':'长沙',
    'chengdu':'成都',
    'dalian':'大连',
    'hangzhou':'杭州',
    'kunming':'昆明',
    'nanjing':'南京',
    'suzhou':'苏州',
    'tianjin':'天津',
    'wuhan':'武汉',
    'xian':'西安'
}
type_house = {
    '商业类':'business',
    '住宅':'residence',
    '写字楼':'office',
    '商铺':'shops',
    '别墅':'villa',
    '底商':'dishang'

}

class Count(object):
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
        csvfile = file('./data_table/count_city.csv', 'ab')
        writers = csv.writer(csvfile)
        writers.writerow(
            ['city', 'house_num', 'business', 'residence', 'office', 'shops', 'villa', 'dishang', 'sell_out', 'sell',
             'sell_ing'])
        csvfile.close()

    def count_num(self,city_name):
        csvfile = file('./data_table/count_city.csv', 'ab')
        writers = csv.writer(csvfile)
        self.df = pd.read_csv('./data_table/%s.csv' % city_name, encoding='utf-8')
        #总计
        house_num = len(self.df) - 1
        #售房类型
        business = len(self.df[self.df.type == "商业类"])
        residence = len(self.df[self.df.type == "住宅"])
        office = len(self.df[self.df.type == "写字楼"])
        shops = len(self.df[self.df.type == "商铺"])
        villa = len(self.df[self.df.type == "别墅"])
        dishang = len(self.df[self.df.type == "底商"])

        #出售情况
        sell_out = len(self.df[self.df.state == "售罄"])
        sell = len(self.df[self.df.state == "待售"])
        sell_ing = len(self.df[self.df.state == "在售"])
        writers.writerow(
            (province[city_name], house_num, business, residence, office, shops, villa, dishang,sell_out,sell,sell_ing))
        csvfile.close()

    def main(self):
        for i in self.tables:
            self.count_num(i)

if __name__ == '__main__':
    count = Count()
    count.main()
