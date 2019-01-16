# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data Prep
tips = sns.load_dataset('tips')
print(tips.head(10))

# plot with seaborn (scatter, kde, hex)
sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
plt.show()

