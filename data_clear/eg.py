# encoding=utf-8
import pandas as pd

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
# 例子例子大例子

# 对销售状态做去重,查看有多少种销售状态
# for i in tables:
#     df = pd.read_csv('./data_table/%s.csv'%i,encoding='utf-8')
#     state_num = df.drop_duplicates(['state'])['state']
#     print(state_num)

# 对房屋类型去重
for i in tables:
    df = pd.read_csv('./data_table/%s.csv' % i, encoding='utf-8')
    type_num = df.drop_duplicates(['type'])['type']  # 对指定列去重
    print(type_num)

# 计数
# print len(df[df.type == "住宅"])

# df = pd.read_csv('./data_table/count_city.csv',encoding='utf-8')
# print df
