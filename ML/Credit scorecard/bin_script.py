# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @createTime: 19-4-10 下午2:18
# @author: scdev030

import pandas as pd
import numpy as np
import scipy.stats.stats as stats

def read_data(data_type='train'):
    """
    加载数据
    """
    data = pd.read_csv('./data/02_data_exploration/%s_data.csv'%data_type)
    return data

def auto_bin(Y, X, n=20):
    """
    单调分箱(连续变量分箱)
    """
    r = 0
    good = Y.sum()
    bad = Y.count() - good
    while np.abs(r)<1:
        d1 = pd.DataFrame({"X":X, "Y":Y, "BIN":pd.qcut(X, n)})
        d2 = d1.groupby('BIN', as_index=True)
        r, p = stats.spearmanr(d2.mean().X, d2.mean().Y)
        print('-' * 80)
        print('r',r)
        print('p',p)
        print('n',n)
        print('-' * 80)
        n = n - 1
    d3 = pd.DataFrame()
    d3['min'] = d2.min().X
    d3['max'] = d2.max().X
    d3['total'] = d2.count().Y # 总数
    d3['sum'] = d2.sum().Y # 响应的数量
    d3['mean'] = d2.mean().Y
    # d3['woe'] = np.log((d3['rate']/(1-d3['rate']))/(good/bad))
    d3['woe'] = np.log((d3['sum'] / (d3['total'] - d3['sum'])) / (good / bad))
    d3['good_attribute'] = d3['sum'] / good
    d3['bad_attribute'] = (d3['total'] - d3['sum']) / bad
    iv = ((d3['good_attribute']-d3['bad_attribute'])*d3['woe']).sum()
    d4 = (d3.sort_values(by='min'))
    print("=" * 80)
    print(d4)
    print(iv)
    return d4, iv

data = read_data()
auto_bin(data['SeriousDlqin2yrs'], data['age'], n=10)



