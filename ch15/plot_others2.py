# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data Prep
iris = sns.load_dataset('iris')

# plot with seaborn
sns.pairplot(iris)
plt.show()
