# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @createTime: 2019/4/01 11:28
# @author: scdev030

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats.stats as stats
import seaborn as sns

def auto_build_bin(Y, X, n=20):
    """
    最优分箱函数
    """
    r = 0
    good = Y.sum()
    bad = Y.count() - good
    while np.abs(r) < 1:
        d1 = pd.DataFrame({"X":X, "Y":Y, "Bucket":pd.qcut(X, n)})
        d2 = d1.groupby('Bucket', as_index=True)
        r, p = stats.spearmanr(d2.mean().X, d2.mean().Y)
        n = n - 1
    d3 = pd.DataFrame(d2.X.min(), columns=['min'])
    d3['min'] = d2.min().X
    d3['max'] = d2.max().X
    d3['sum'] = d2.sum().Y
    d3['total'] = d2.count().Y
    d3['rate'] = d2.mean().Y
    d3['woe'] = np.log((d3['rate']/(1-d3['rate']))/(good/bad))
    d3['goodattribute']=d3['sum']/good
    d3['badattribute']=(d3['total']-d3['sum'])/bad
    iv=((d3['goodattribute']-d3['badattribute'])*d3['woe']).sum()
    d4 = (d3.sort_index(by='min')).reset_index(drop=True)
    print("="*80)
    print(d4)
    cut=[]
    cut.append(float('-inf'))
    for i in range(1,n+1):
        qua=X.quantile(i/(n+1))
        cut.append(round(qua,4))
    cut.append(float('inf'))
    print(cut)
    woe=list(d4['woe'].round(3))
    return d4,iv,cut,woe

def self_build_bin(Y, X, cut):
    """
    自定义分箱
    """
    good = Y.sum()
    bad = Y.count() - good
    d1 = pd.DataFrame({'X':X, 'Y':Y, 'Bucket':pd.cut(X, cut)})
    d2 = d1.groupby('Bucket', as_index=True)
    d3 = pd.DataFrame(d2.X.min(), columns=['min'])
    d3['min'] = d2.min().X
    d3['max'] = d2.max().X
    d3['total'] = d2.count().Y
    d3['sum'] = d2.sum().Y
    d3['rate'] = d2.mean().Y
    d3['woe'] = np.log((d3['rate']/(1 - d3['rate'])) / (good / bad))
    d3['goodattribute'] = d3['sum'] / good
    d3['badattribute'] = (d3['total'] - d3['sum']) / bad
    iv = ((d3['goodattribute'] - d3['badattribute']) * d3['woe']).sum()
    d4 = (d3.sort_index(by='min')).reset_index(drop=True)
    print('=' * 80)
    print(d4)
    woe = list(d4['woe'].round(3))
    return d4, iv ,woe
    

def build_histogram(iv_list, index_list):
    """
    创建柱状图
    """

    fig1 = plt.figure(1)
    ax1 = fig1.add_subplot(1, 1, 1)
    x = np.arange(len(index_list)) + 1
    ax1.bar(x, iv_list, width=0.4)  # 生成柱状图
    ax1.set_xticks(x)
    ax1.set_xticklabels(index_list, rotation=0, fontsize=12)
    ax1.set_ylabel('IV(Information Value)', fontsize=14)
    # 在柱状图上添加数字标签
    for a, b in zip(x, iv_list):
        plt.text(a, b + 0.01, '%.4f' % b, ha='center', va='bottom', fontsize=10)
    plt.show()

def build_correlations():
    """
    绘制相关性图
    """
    data = read_data()
    corr = data.corr()  # 计算各变量的相关性系数
    xticks = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']  # x轴标签
    yticks = list(corr.index) # y轴标签
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    sns.heatmap(corr, annot=True, cmap='rainbow', ax=ax1,
                annot_kws={'size': 9, 'weight': 'bold', 'color': 'blue'}) # 绘制相关性系数热力图
    ax1.set_xticklabels(xticks, rotation=0, fontsize=10)
    ax1.set_yticklabels(yticks, rotation=0, fontsize=10)
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

def read_data():
    """
    加载数据
    """
    data = pd.read_csv('./data/02_data_exploration/train_data.csv')
    return data


def main():
    # 绘制相关性图
    # build_correlations()
    data = read_data()

    # 最优分箱
    df_x2, iv_x2, cut_x2, woe_x2 = auto_build_bin(data['SeriousDlqin2yrs'], data['age'], n=10) # 年龄
    df_x1, iv_x1, cut_x1, woe_1 = auto_build_bin(data['SeriousDlqin2yrs'], data['RevolvingUtilizationOfUnsecuredLines'], n=10) # 无担保放款的循环利用
    df_x4, iv_x4, cut_x4, woe_4 = auto_build_bin(data['SeriousDlqin2yrs'], data['DebtRatio'], n=20) # 负债情况
    df_x5, iv_x5, cut_x5, woe_5 = auto_build_bin(data['SeriousDlqin2yrs'], data['MonthlyIncome'], n=10) # 月收入

    # 自定义分箱
    pinf = float('inf')#正无穷大
    ninf = float('-inf')#负无穷大
    cutx3 = [ninf, 0, 1, 3, 5, pinf]
    cutx6 = [ninf, 1, 2, 3, 5, pinf]
    cutx7 = [ninf, 0, 1, 3, 5, pinf]
    cutx8 = [ninf, 0,1,2, 3, pinf]
    cutx9 = [ninf, 0, 1, 3, pinf]
    cutx10 = [ninf, 0, 1, 2, 3, 5, pinf]
    df_x3, iv_x3, woe_x3 = self_build_bin(data.SeriousDlqin2yrs, data['NumberOfTime30-59DaysPastDueNotWorse'], cutx3)
    df_x6, iv_x6, woe_x6= self_build_bin(data.SeriousDlqin2yrs, data['NumberOfOpenCreditLinesAndLoans'], cutx6)
    df_x7, iv_x7, woe_x7 = self_build_bin(data.SeriousDlqin2yrs, data['NumberOfTimes90DaysLate'], cutx7)
    df_x8, iv_x8, woe_x8 = self_build_bin(data.SeriousDlqin2yrs, data['NumberRealEstateLoansOrLines'], cutx8)
    df_x9, iv_x9, woe_x9 = self_build_bin(data.SeriousDlqin2yrs, data['NumberOfTime60-89DaysPastDueNotWorse'], cutx9)
    df_x10, iv_x10, woe_x10 = self_build_bin(data.SeriousDlqin2yrs, data['NumberOfDependents'], cutx10)
    iv_list= [iv_x1,iv_x2, iv_x3, iv_x4, iv_x5, iv_x6, iv_x7, iv_x8, iv_x9, iv_x10]
    index_list = ['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']

    # 绘制IV值柱状图
    build_histogram(iv_list, index_list)


if __name__ == '__main__':
    main()