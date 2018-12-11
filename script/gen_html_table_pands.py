# encoding=utf-8
# 将数据转换为html的table
# title 是list结构,每个索引和result一一对应,
# title_list[0]对应result_list[0]的一条数据对应html表格中的一列
# result 是list嵌套的数据结果,每一列对应一列表格数据
import pandas as pd

def gen_to_html(result, title):
    d = {}
    index = 0
    for t in title:
        d[t] = result[index]
        index = index + 1
    df = pd.DataFrame(d)
    df = df[title] # 按照表头排序
    print(df[title])
    h = df.to_html(index=False)
    return h


if __name__ == '__main__':
    result = [[u'2018-12-01', u'2012-12-02', u'2012-02-03'],
              [u'张三', u'李四', u'王二'],
              [u'男',u'女',u'男']]
    title = [u'日期', u'姓名',u'性别']
    print(gen_to_html(result, title))
