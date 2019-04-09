# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @createTime: 19-4-9 下午8:12
# @author: scdev030

import math

import pandas as pd
import numpy as np
import scipy.stats.stats as stats

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

def read_data(data_type='train'):
    """
    加载数据
    """
    data = pd.read_csv('./data/02_data_exploration/%s_data.csv'%data_type)
    return data

def get_score(coe, woe, factor):
    """
    计算分数函数
    """
    scores = []
    for w in woe:
        score = round(coe * w * factor, 0)
        scores.append(score)
    return scores

def compute_score(series,cut,score):
    """
    根据变量计算分数
    """
    list = []
    i = 0
    while i < len(series):
        value = series[i]
        j = len(cut) - 2
        m = len(cut) - 2
        while j >= 0:
            if value >= cut[j]:
                j = -1
            else:
                j -= 1
                m -= 1
        list.append(score[m])
        i += 1
    return list

data = read_data(data_type='train')

# 最优分箱
df_x2, iv_x2, cut_x2, woe_x2 = auto_build_bin(data['SeriousDlqin2yrs'], data['age'], n=10)  # 年龄
df_x1, iv_x1, cut_x1, woe_x1 = auto_build_bin(data['SeriousDlqin2yrs'], data['RevolvingUtilizationOfUnsecuredLines'], n=10)  # 无担保放款的循环利用
df_x4, iv_x4, cut_x4, woe_x4 = auto_build_bin(data['SeriousDlqin2yrs'], data['DebtRatio'], n=20)  # 负债情况
df_x5, iv_x5, cut_x5, woe_x5 = auto_build_bin(data['SeriousDlqin2yrs'], data['MonthlyIncome'], n=10)  # 月收入

# 自定义分箱
pinf = float('inf')  # 正无穷大
ninf = float('-inf')  # 负无穷大
cut_x3 = [ninf, 0, 1, 3, 5, pinf]
cut_x6 = [ninf, 1, 2, 3, 5, pinf]
cut_x7 = [ninf, 0, 1, 3, 5, pinf]
cut_x8 = [ninf, 0, 1, 2, 3, pinf]
cut_x9 = [ninf, 0, 1, 3, pinf]
cut_x10 = [ninf, 0, 1, 2, 3, 5, pinf]
df_x3, iv_x3, woe_x3 = self_build_bin(data.SeriousDlqin2yrs, data['NumberOfTime30-59DaysPastDueNotWorse'], cut_x3)
df_x6, iv_x6, woe_x6 = self_build_bin(data.SeriousDlqin2yrs, data['NumberOfOpenCreditLinesAndLoans'], cut_x6)
df_x7, iv_x7, woe_x7 = self_build_bin(data.SeriousDlqin2yrs, data['NumberOfTimes90DaysLate'], cut_x7)
df_x8, iv_x8, woe_x8 = self_build_bin(data.SeriousDlqin2yrs, data['NumberRealEstateLoansOrLines'], cut_x8)
df_x9, iv_x9, woe_x9 = self_build_bin(data.SeriousDlqin2yrs, data['NumberOfTime60-89DaysPastDueNotWorse'], cut_x9)
df_x10, iv_x10, woe_x10 = self_build_bin(data.SeriousDlqin2yrs, data['NumberOfDependents'], cut_x10)

# 计算分数
# coe为逻辑回归模型的系数
coe = [9.7388, 0.6380, 0.5060, 1.0322, 1.7900, 1.1320]
# 我们取600分为基础分值，PDO为20（每高20分好坏比翻一倍），好坏比取20。
p = 20 / math.log(2)
q = 600 - 20 * math.log(20) / math.log(2)
baseScore = round(q + p * coe[0], 0)

# 各项部分分数
x1 = get_score(coe[1], woe_x1, p)
x2 = get_score(coe[2], woe_x2, p)
x3 = get_score(coe[3], woe_x3, p)
x7 = get_score(coe[4], woe_x7, p)
x9 = get_score(coe[5], woe_x9, p)
print(x1, x2, x3, x7, x9)

test1 = read_data(data_type='test')
test1['BaseScore'] = pd.Series(np.zeros(len(test1))) + baseScore
test1['x1'] = pd.Series(compute_score(test1['RevolvingUtilizationOfUnsecuredLines'], cut_x1, x1))
test1['x2'] = pd.Series(compute_score(test1['age'], cut_x2, x2))
test1['x3'] = pd.Series(compute_score(test1['NumberOfTime30-59DaysPastDueNotWorse'], cut_x3, x3))
test1['x7'] = pd.Series(compute_score(test1['NumberOfTimes90DaysLate'], cut_x7, x7))
test1['x9'] = pd.Series(compute_score(test1['NumberOfTime60-89DaysPastDueNotWorse'], cut_x9, x9))
test1['Score'] = test1['x1'] + test1['x2'] + test1['x3'] + test1['x7'] + test1['x9'] + baseScore
test1.to_csv('ScoreData.csv', index=False)