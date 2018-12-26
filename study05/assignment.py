# coding: utf8
import pandas as pd

from pandas import Series, DataFrame
from pandasql import sqldf, load_meat, load_births

"""
对于下表的数据，请使用 Pandas 中的 DataFrame 进行创建，并对数据进行清洗。同时新增一列“总和”计算每个人的三科成绩之和。
"""


def total(df):
    df[u'总和'] = (df[u'语文'] + df[u'英语'] + df[u'数学'])
    return df


# 导入并初始化数据到DataFrame中
df = pd.read_excel('Book.xlsx')

# 消除重复行
df = df.drop_duplicates()

# 添加并计算总成绩列
dfnew = df.apply(total, axis=1)

# 排序
dfnew = dfnew.sort_values([u'总和'], ascending=False)

# 输出
print(dfnew)
