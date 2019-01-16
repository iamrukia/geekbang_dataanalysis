# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data Prep
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)

# plot with matplotlib
plt.scatter(x, y, marker='o')
plt.show()

# plot with seaborn
df = pd.DataFrame({'x': x, 'y': y})
sns.jointplot(x="x", y="y", data=df, kind='scatter')
plt.show()
