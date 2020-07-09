# -*- coding: utf-8

"""
@File       :   plot_eegrdmscorrs.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import matplotlib.pyplot as plt
import numpy as np

corrs = np.zeros([6, 851, 851], dtype=np.float)

for sub in range(6):
    corrs[sub] = np.loadtxt("../eeg_cal/rdmscorrs/alpha_power_fp/sub" + str(sub+1) + ".txt")

avg_corrs = np.average(corrs, axis=0)[113:, 113:]

ps = np.loadtxt("../eeg_cal/rdmscorrs/alpha_power_fp/p.txt")[113:, 113:]

for i in range(738):
    for j in range(738):
        if ps[i, j] >= 0.05:
            ps[i, j] = 0
        else:
            if avg_corrs[i, j] > 0:
                ps[i, j] = 1
            if avg_corrs[i, j] < 0:
                ps[i, j] = -1

newps = np.zeros([740, 740], dtype=np.float)
newps[1:739, 1:739] = ps

x = np.linspace(-0.002, 2.952+0.002, 740)
y = np.linspace(-0.002, 2.952+0.002, 740)
X, Y = np.meshgrid(x, y)
plt.contour(X, Y, newps, (-0.5, 0.5), cmap="seismic", linewidths=1)

plt.imshow(avg_corrs, extent=(0, 2.952, 0, 2.952), cmap=plt.cm.seismic, clim=(-0.75, 0.75), origin='low')

cb = plt.colorbar(ticks=[-0.7, 0, 0.7])
cb.ax.tick_params(labelsize=18)
font = {'size': 20}
cb.set_label("Similarity", fontdict=font)
x = [0, 0.5, 1, 1.5, 2, 2.5]
y = ["0.0", "0.5", "1.0", "1.5", "2.0", "2.5"]
plt.tick_params(labelsize=18)
plt.yticks(x, y, fontsize=18)
plt.xticks(x, y, fontsize=18)
plt.xlabel("Time (s)", fontsize=20)
plt.ylabel("Time (s)", fontsize=20)

plt.show()