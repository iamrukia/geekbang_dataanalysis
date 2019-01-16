# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data prep
flights = sns.load_dataset("flights")
data = flights.pivot('year', 'month', 'passengers')

# plot with seaborn
sns.heatmap(data)
plt.show()
