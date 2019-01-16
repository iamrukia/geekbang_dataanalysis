# coding:utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data prep
from matplotlib.font_manager import FontProperties

xlabels = np.array([u"推进", "KDA", u"生存", u"团战", u"发育", u"输出"])
xstats = [83, 61, 95, 67, 76, 88]

# plot data prep, angle and status
angles = np.linspace(0, 2 * np.pi, len(xlabels), endpoint=False)
stats = np.concatenate((xstats, [xstats[0]]))
angles = np.concatenate((angles, [angles[0]]))

# plot with Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)

# setup chinese font
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
ax.set_thetagrids(angles * 180 / np.pi, xlabels, FontProperties=font)
plt.show()
