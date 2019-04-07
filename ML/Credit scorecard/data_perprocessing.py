# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @createTime: 2019/3/30 16:49
# @author: scdev030

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split



def pandas_decribe():
    """
    使用pandas做简单数据分布分析
    """
    data = pd.read_csv('./data/cs-training.csv')
    data_describe = data.describe()
    data_describe.to_csv('data/data_describe.csv')
    return data

def set_missing_value(df):
    """
    用随机森林对缺失值预测填充函数
    """
    process_df = df.ix[:,[5,0,1,2,3,4,6,7,8,9]] # 选取所有的行和指定的列
    # 分为已知该特征(MonthlyIncome)和未知该特征两部分
    known = process_df[process_df.MonthlyIncome.notnull()].values
    unknown = process_df[process_df.MonthlyIncome.isnull()].values

    # X为特征属性值
    X = known[:, 1:]
    # y为结果标签值
    y = known[:, 0]
    print (y)
    # 使用随机森林(RandomForestRegressor)训练
    print('使用随机森林训练')
    rfr = RandomForestRegressor(random_state=0, n_estimators=200,max_depth=3,n_jobs=-1)
    rfr.fit(X,y)
    # 用得到的模型进行未知特征值预测
    predicted = rfr.predict(unknown[:, 1:]).round(0)
    print(predicted)
    # 用得到的预测结果填补原缺失数据
    df.loc[(df.MonthlyIncome.isnull()), 'MonthlyIncome'] = predicted
    return df

    # unknown = process_df[process_df.MonthlyIncome.isnull()].as_matrix()

def data_test(df):
    """
    测试使用的方法的方法
    """
    print(df.loc[(df.MonthlyIncome.isnull()), 'MonthlyIncome'])
    # print (type(df.ix[:,[5,0,1,2,3,4,6,7,8,9]]))
    # process_df_test = df.ix[:,[5,0,1,2,3,4,6,7,8,9]]
    # print (process_df_test[process_df_test.MonthlyIncome.notnull()]).as_matrix()
    # print (process_df_test.MonthlyIncome.isnull()) 

def data_deal_missing():
    """
    数据缺失值处理
    """
    data = pd.read_csv('./data/cs-training.csv')
    # data_test(data)

    # 用随机森林填补笔记多的缺失值
    data_rtf_missing_df = set_missing_value(data)
    # 删除较少的缺失值
    data_rtf_missing_drop_na_df = data_rtf_missing_df.dropna()
    # 删除重复项
    data_rtf_missing_drop_dup_df = data_rtf_missing_drop_na_df.drop_duplicates()
    # 保持处理完缺失值的数据
    print('另存数据')
    data_rtf_missing_drop_dup_df.to_csv('./data/01_data_perproces/missing_data_tring.csv', index=False)
    # 保存一份处理完缺失值的分布情况的数据
    data_rtf_missing_drop_dup_df.describe().to_csv('./data/01_data_perproces/missing_data_describe.csv')

def data_deal_abnormal():
    """
    数据异常值处理
    """
    data_raw_df = pd.read_csv('./data/01_data_perproces/missing_data_tring.csv')
    # 删除年龄异常
    data_drop_age_abnormal_df = data_raw_df[data_raw_df['age']>0]
    # 箱型图查看指定列的元素异常值
    # data_379_column = data_drop_age_abnormal_df[['NumberOfTime30-59DaysPastDueNotWorse','NumberOfTimes90DaysLate','NumberOfTime60-89DaysPastDueNotWorse']]
    # data_379_column.boxplot()
    # 去掉大于90的异常值
    data_drop_abnormal = data_drop_age_abnormal_df[data_drop_age_abnormal_df['NumberOfTime30-59DaysPastDueNotWorse'] < 90]
    # 交换好客户和坏客户的值，好客户为1
    data_drop_abnormal['SeriousDlqin2yrs'] = 1 - data_drop_abnormal['SeriousDlqin2yrs']
    return data_drop_abnormal

def tran_test_data_split(data):
    """
    切分训练和测试集
    """
    # import ipdb; ipdb.set_trace()
    Y = data['SeriousDlqin2yrs']
    X = data.ix[:, 1:]
    #测试集占比30%
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    # print(Y_train)
    train = pd.concat([Y_train, X_train], axis=1)
    test = pd.concat([Y_test, X_test], axis=1)
    # clasTest = test.groupby('SeriousDlqin2yrs')['SeriousDlqin2yrs'].count()
    train.to_csv('./data/02_data_exploration/train_data.csv', index=False)
    test.to_csv('./data/02_data_exploration/test_data.csv', index=False)



if __name__ == '__main__':
    # pandas_decribe()
    data_deal_missing()
    df_to_split = data_deal_abnormal()
    tran_test_data_split(df_to_split)

