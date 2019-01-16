# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data Prep
# Generate 0-1 10*4 dimension data
data = np.random.normal(size=(10, 4))
xlabels = ['A', 'B', 'C', 'D']

# plot wiht Matplotlib
plt.boxplot(data, labels=xlabels)
plt.show()

# plot with seaborn
df = pd.DataFrame(data, columns=xlabels)
sns.boxplot(data=df)
plt.show()
