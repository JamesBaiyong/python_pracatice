# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @createTime: 2019/4/01 11:28
# @author: scdev030

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def build_histogram():
    """
    创建柱状图
    """
    df = pd.read_csv('./data/02_data_exploration/train_data.csv')
    monthly_income_values = df['MonthlyIncome'].values
    count_reslt = all_np(monthly_income_values)
    x = []
    y = []
    # print (type(count_reslt))
    # import ipdb; ipdb.set_trace()
    for k,v in count_reslt.items():
        x.append(k)
        y.append(v)
    # print(y)
    plt.bar(x, y,facecolor='#9999ff',edgecolor='white')
    plt.show()


def all_np(arr):
    """
    获取每个元素的出现次数，使用Numpy
    """
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result


def main():
    build_histogram()
    # array = [1, 2, 3, 3, 2, 1, 0, 2]
    # print(all_np(array))


if __name__ == '__main__':
    main()