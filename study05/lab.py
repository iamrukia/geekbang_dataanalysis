# coding: utf8
import pandas as pd

from pandas import Series, DataFrame
from pandasql import sqldf, load_meat, load_births

x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)

print("Series")
print('x1[0] = ', x1[0])
print('x2[0] = ', x2[0])
print('x2["a"] = ', x2['a'])

# create series from dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
x3 = Series(d)
print('create Series from dictionary: ', x3)

# DataFrame
data = {
    'chinese': [66, 95, 93, 90, 80],
    'english': [65, 85, 92, 88, 90],
    'math': [30, 98, 96, 77, 90]
}
df1 = DataFrame(data)
df2 = DataFrame(
    data,
    index=[
        'Zhangfei',
        'Guanyu',
        'Zhaoyun',
        'Huangzhong',
        'Dianwei'
    ],
    columns=[
        'english',
        'math',
        'chinese'
    ]
)

print('df1')
print(df1)
print('df2')
print(df2)

# import and export
score = DataFrame(pd.read_excel('book1.xlsx'))
print(score)
score.to_excel('book2.xlsx')

# data cleaning
df2 = df2.drop(columns=['chinese'])
print(df2)
df2 = score.copy()

df2 = df2.drop(index=['Zhangfei'])
print(df2)
df2 = score.copy()

df2.rename(columns={'chinese': 'YuWen', 'english': 'YingYu', 'math': 'ShuXue'}, inplace=True)
print(df2)

# remove duplicate
df2 = DataFrame(pd.read_excel('bookduplicate.xlsx'))
print(df2)
df2 = df2.drop_duplicates()
print(df2)
df2 = score.copy()

# format
df2['chinese'].astype('str')
print(df2)
df2 = score.copy()

# strip
print(df2)
df2['gender'].astype('str')
df2['gender'] = df2['gender'].map(str.strip)
print(df2)
df2 = score.copy()

# 大小写转换
df2.columns = df2.columns.str.upper()
df2['GENDER'] = df2['GENDER'].str.upper()
print(df2)
df2 = score.copy()

# 查找空值
print(df2.isnull())
print(df2.isnull().any())
df2 = score.copy()

# 使用 apply 函数对数据进行清洗
score2 = DataFrame(pd.read_excel('book3.xlsx'))
df = score2.copy()
df['name'] = df['name'].apply(str.upper)
print(df)


def double_df(x):
    return 2 * x


df['english'] = df['english'].apply(double_df)
print(df)


# 新增列
def plus(df, n, m):
    df['new1'] = (df['english'] + df['chinese']) * m
    df['new2'] = (df['english'] + df['chinese']) * n
    return df


df1 = df.apply(plus, axis=1, args=(2, 3,))
print(df1)

# 数据统计
print(df.describe())

# 数据表合并
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})
print(df1)
print(df2)

# 基于指定列
df3 = pd.merge(df1, df2, on='name')
print(df3)

# inner内连接
df3 = pd.merge(df1, df2, how='inner')
print(df3)

# left join
df3 = pd.merge(df1, df2, how='left')
print(df3)

# right join
df3 = pd.merge(df1, df2, how='right')
print(df3)

# outer join
df3 = pd.merge(df1, df2, how='outer')
print(df3)

# using SQL
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name = 'ZhangFei'"
print(pysqldf(sql))
