# coding: utf8
import numpy as np

"""
假设一个团队里有 5 名学员，成绩如下表所示。你可以用 NumPy 统计下这些人
在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出.

| 姓名    | 语文   | 英语   | 数学  |
| 张飞    | 66    | 65    | 30    |
| 关羽    | 95    | 85    | 98    |
| 赵云    | 93    | 92    | 96    |
| 黄忠    | 90    | 88    | 77    |
| 典韦    | 80    | 90    | 90    |

"""

# define data type
studenttype = np.dtype({
    'names': ['name', 'chinese', 'english', 'math', 'total'],
    'formats': ['U32', 'i', 'i', 'i', 'f']
})

# define and init students details
# init total with 0
students = np.array(
    [
        ("张飞", 66, 65, 30, 0),
        ("关羽", 95, 85, 98, 0),
        ("赵云", 93, 92, 96, 0),
        ("黄忠", 90, 88, 77, 0),
        ("典韦", 80, 90, 90, 0)
    ], dtype=studenttype
)

# calculate total
students[:]['total'] = students[:]['chinese'] + students[:]['english'] + students[:]['math']
# print(students[:])

# p1 统计下这些人
# 在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差
print('语文平均成绩 = ', np.mean(students[:]['chinese']))
print('英语平均成绩 = ', np.mean(students[:]['english']))
print('数学平均成绩 = ', np.mean(students[:]['math']))
print('语文最小成绩 = ', np.amin(students[:]['chinese']))
print('英语最小成绩 = ', np.amin(students[:]['english']))
print('数学最小成绩 = ', np.amin(students[:]['math']))
print('语文最大成绩 = ', np.amax(students[:]['chinese']))
print('英语最大成绩 = ', np.amax(students[:]['english']))
print('数学最大成绩 = ', np.amax(students[:]['math']))
print('语文方差 = ', np.var(students[:]['chinese']))
print('英语方差 = ', np.var(students[:]['english']))
print('数学方差 = ', np.var(students[:]['math']))
print('语文标准差 = ', np.std(students[:]['chinese']))
print('英语标准差 = ', np.std(students[:]['english']))
print('数学标准差 = ', np.std(students[:]['math']))

# p2 然后把这些人的总成绩排序，得出名次进行成绩输出.
print("按总成绩排名", np.sort(students[:]['total'])[::-1])
