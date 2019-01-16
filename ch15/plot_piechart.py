# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data Prep
nums = [25, 37, 33, 27, 6]
xlabels = ['Highschool', 'Bachelor', 'Master', 'Ph.d', 'Others']

# plot with Matplotlib
plt.pie(x=nums, labels=xlabels)
plt.show()

