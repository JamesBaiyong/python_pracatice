# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @createTime: 19-4-8 下午1:04
# @author: scdev030
import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.metrics import roc_curve, auc


def logistic_model_by_stats_models():
    """
    使用statsmodels实现
    """
    data = pd.read_csv('./data/03_data_model/train_data_woe.csv')
    # 应变量
    Y = data['SeriousDlqin2yrs']
    # 自变量，剔除对因变量影响不明显的变量
    X = data.drop(['SeriousDlqin2yrs', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans',
                   'NumberRealEstateLoansOrLines', 'NumberOfDependents'], axis=1)
    X1 = sm.add_constant(X)
    logit = sm.Logit(Y, X1)
    result = logit.fit()
    print(result.summary())
    return result

def logistic_model_by_sk_learn():
    """
    使用sklearn实现
    """
    data = pd.read_csv('./data/03_data_model/train_data_woe.csv')
    # 应变量
    Y = data['SeriousDlqin2yrs']
    # 自变量，剔除对因变量影响不明显的变量
    X = data.drop(['SeriousDlqin2yrs', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans',
                   'NumberRealEstateLoansOrLines', 'NumberOfDependents'], axis=1)
    logistic = LogisticRegression()
    logistic.fit(X, Y, sample_weight=(np.array(X['RevolvingUtilizationOfUnsecuredLines'],X['NumberOfTimes90DaysLate'])))
    print(logistic.coef_[0])
    return logistic

def test_model_by_auc(model_result, sklearn=True):
    """
    测试数据,检查数据拟合情况
    """
    test = pd.read_csv('./data/03_data_model/test_data_woe.csv')
    Y_test = test['SeriousDlqin2yrs']
    X_test = test.drop(['SeriousDlqin2yrs', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans',
                        'NumberRealEstateLoansOrLines', 'NumberOfDependents'], axis=1)
    if not sklearn:
        X_test = sm.add_constant(X_test)
    resu = model_result.predict(X_test)
    fpr, tpr, _ = roc_curve(Y_test, resu)
    rocauc = auc(fpr, tpr)
    # 生成ROC曲线
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % rocauc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('真正率')
    plt.xlabel('假正率')
    plt.show()

# model_result = logistic_model_by_sk_learn()
# test_model_by_auc(model_result)

model_result = logistic_model_by_stats_models()
test_model_by_auc(model_result, sklearn=False)
