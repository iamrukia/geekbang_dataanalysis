# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

a = np.random.randn(100)
s = pd.Series(a)

# plot with matplotlib
plt.hist(s)
plt.show()

# plot with seaborn
sns.distplot(s, kde=False)
plt.show()

sns.distplot(s, kde=True)
plt.show()
