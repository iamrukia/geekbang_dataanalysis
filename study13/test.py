# coding:utf-8
from sklearn import preprocessing
import numpy as np

# 初始化数据，每一行表示一个样本，每一列表示一个特征

FFF = np.array([
    [0., -3., 1.],
    [3., 1., 2.],
    [0., 1., -1.]
])

X = np.array([
    [2., 4., 6.],
    [1., 2., 3.],
    [3., 6., 9.]
])

# 将数据进行[0, 1]规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(X)
print(minmax_x)

# 将数据进行 Z-score 规范化
# a - avg(A)/var(a)
scaled_x = preprocessing.scale(X)
print(scaled_x)

# 标准差标准化
j = np.ceil(np.log10(np.max(abs(X))))
scaled_y = X / (10 ** j)
print(scaled_y)

money = np.array([[5000.], [58000.], [16000.]])

minmax_money = min_max_scaler.fit_transform(money)
print(minmax_money)
