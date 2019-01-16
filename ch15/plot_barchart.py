# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data Prep
x = ['Cat1', 'Cat2', 'Catt', 'Cat4', 'Cat5']
y = [5, 4, 8, 12, 7]

# plot with Matplotlib
plt.bar(x, y)
plt.show()

# plot with seaborn
sns.barplot(x, y)
plt.show()
