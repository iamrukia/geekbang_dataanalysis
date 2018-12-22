# coding: utf8
import numpy as np

print('你好')
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

b[1][1] = 10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)

persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']
})

peoples = np.array([
    ("Zhangfei", 32, 75, 100, 90),
    ("Guanyu", 33, 77, 100, 91),
    ("Zhaoyun", 33, 88, 99, 88),
    ("Huangzhong", 35, 89, 88, 77)
], dtype=persontype)

ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(ages)
print('chinese', chineses)
print(maths)
print(englishs)
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))

x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(x1)
print(x2)

print('x1 + x2 = ', np.add(x1, x2))
print('x1 - x2 = ', np.subtract(x1, x2))
print('x1 * x2 = ', np.multiply(x1, x2))
print('x1 / x2 = ', np.divide(x1, x2))
print('x1 ^ x2 = ', np.power(x1, x2))
print('x1 % x2 = ', np.remainder(x1, x2))

c = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(c)

print('min = ', np.amin(c))
print('max = ', np.amax(c))
print('横轴-x-最小', np.amin(c, 0))
print('纵轴-y-最小', np.amin(c, 1))

print('横轴-x-最大', np.amax(c, 0))
print('纵轴-y-最大', np.amax(c, 1))

print('ptp = ', np.ptp(c))
print('ptp over x axis ', np.ptp(c, 0))
print('ptp over y axis ', np.ptp(c, 1))

print('percentile', np.percentile(c, 50))
print('percentile over axis 0', np.percentile(c, 50, axis=0))
print('percentile over axix 1', np.percentile(c, 50, axis=1))
print(c)

print('median', np.median(c))
print('median over axis 0', np.median(c, 0))
print('median over axis 1', np.median(c, 1))
print('mean', np.mean(c))
print('mean over axis 0', np.mean(c, 0))
print('mean over axis 1', np.mean(c, 1))

a = np.array(
    [1, 2, 3, 4]
)
awts = np.array(
    [1, 2, 3, 4]
)

print('average over a', np.average(a))
print('average over a with weights awts', np.average(a, weights=awts))

print(' standard deviation of array = ', np.std(a))
print(' variance of array = ', np.var(a))

b = np.array(
    [
        [1, 5, 3],
        [6, 2, 4]
    ]
)

print('quicksort', np.sort(b, kind='quicksort'))
print('heapsort', np.sort(b, kind='heapsort'))
print('sort Non axis', np.sort(b))
print('sort over axis=0', np.sort(b, axis=0))
print('sort over axis=1', np.sort(b, axis=1))
print('sort over axis=-1', np.sort(b, axis=-1))
