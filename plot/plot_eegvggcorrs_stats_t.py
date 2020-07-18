# -*- coding: utf-8

"""
@File       :   plot_eegvggcorrs_stats_t.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy.interpolate import interp1d
from scipy import signal

from neurora.rsa_plot import plot_stats_hotmap

stats = np.loadtxt("/Users/zitonglu/Desktop/Neuro_Computation/newcodes/eegvggcorrs_cal/stats_results/trained/theta_power_fp.txt")
stats = np.reshape(stats, [11, 851, 2])
t = stats[:, 113:, 0]


p = stats[:, 113:, 1]


"""for i in range(11):
    for j in range(738):
        if p[i, j] >= 0.05:
            p[i, j] = 0
        else:
            if t[i, j] > 0:
                p[i, j] = 1
            if t[i, j] < 0:
                p[i, j] = -1"""

for i in range(11):
    for j in range(738):
        if p[i, j] >= 0.05:
            p[i, j] = 0
        else:
            if t[i, j] > 0:
                p[i, j] = 1
            if t[i, j] < 0:
                p[i, j] = 0

for i in range(11):
    pid = set(())
    for j in range(738):
        if p[i, j] != 0:
            pid.add(j)
    pid_list = list(pid)
    pid_list.sort()
    pid_set = set()
    for j in pid_list:
        index = 0
        for k in range(25):
            if j+k in pid_list:
                index = index
            else:
                index = index + 1
        if index == 0:
            for k in range(25):
                pid_set.add(j+k)
    pid_list = list(pid_set)
    pid_list.sort()
    for j in range(738):
        index = j in pid_list
        if index is False:
            p[i, j] = 0


newp = np.zeros([13, 740], dtype=np.float)
newp[1:12, 1:739] = p

x = np.linspace(-0.002, 2.952+0.002, 740)
y = np.linspace(-0.08, 1.76+0.08, 13)
X, Y = np.meshgrid(x, y)
plt.contour(X, Y, newp, (-0.5, 0.5), cmap="bwr", linewidths=3)

fig = plt.gcf()
fig.set_size_inches(6, 3)
plt.imshow(t, extent=(0, 2.952, 0, 1.76), clim=(-6, 6), origin='low', cmap="bwr")

cb = plt.colorbar(ticks=[-5, 0, 5])
cb.ax.tick_params(labelsize=18)
font = {'size': 20}
cb.set_label("t", fontdict=font)
x = [0.08, 0.24, 0.4, 0.56, 0.72, 0.88, 1.04, 1.2, 1.36, 1.52, 1.68]
y = ["Conv1", "Conv2", "Conv3", "Conv4", "Conv5", "Conv6", "Conv7", "Conv8", "Fc1", "Fc2", "Fc3"]
plt.tick_params(labelsize=18)
plt.yticks(x, y, fontsize=18)
plt.xlabel("Time (s)", fontsize=20)
plt.ylabel("VGG Layer", fontsize=20)
plt.show()

x = np.linspace(-0.452+0.002, 2.952-0.002, 851)
y = np.linspace(0.08, 1.76-0.08, 11)
print(y[:3])
print(x[:3])
