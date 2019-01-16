# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns

# Data Prep
car_crashes = sns.load_dataset('car_crashes')
sns.pairplot(car_crashes)
plt.show()

# plot with seaborn (scatter, kde, hex)
sns.jointplot(x='alcohol', y='speeding', data=car_crashes, kind='scatter')
sns.jointplot(x='alcohol', y='speeding', data=car_crashes, kind='kde')
sns.jointplot(x='alcohol', y='speeding', data=car_crashes, kind='hex')
plt.show()
