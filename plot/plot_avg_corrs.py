# -*- coding: utf-8

"""
@File       :   plot_convsfcs_avg_corrs.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

rs_convs = np.loadtxt("../eegvggcorrs_cal/avg_corrs/convs/untrained/erp_po.txt")[:, 113:]
rs_fcs = np.loadtxt("../eegvggcorrs_cal/avg_corrs/fcs/untrained/erp_po.txt")[:, 113:]

for sub in range(6):
    b, a = signal.butter(2, 2*20/738, "lowpass")
    rs_convs[sub] = signal.filtfilt(b, a, rs_convs[sub])
    rs_fcs[sub] = signal.filtfilt(b, a, rs_fcs[sub])

avg_rs_convs = np.average(rs_convs, axis=0)
avg_rs_fcs = np.average(rs_fcs, axis=0)

err_convs = np.zeros([738], dtype=np.float)
err_fcs = np.zeros([738], dtype=np.float)

for t in range(738):
    err_convs[t] = np.std(rs_convs[:, t], ddof=1)/np.sqrt(6)
    err_fcs[t] = np.std(rs_fcs[:, t], ddof=1) / np.sqrt(6)

ps_convs = np.loadtxt("../eegvggcorrs_cal/avg_stats_results/convs/untrained/theta_power_po.txt")[113:]
ps_fcs = np.loadtxt("../eegvggcorrs_cal/avg_stats_results/fcs/untrained/theta_power_po.txt")[113:]
ps_convsfcs = np.loadtxt("../eegvggcorrs_cal/avg_stats_results/convs-fcs/untrained/theta_power_po.txt")[113:]

t = 0
ps_convs[737] = 1
while t < 738:
    if ps_convs[t] < 0.05:
        index = 0
        while ps_convs[t+index] < 0.05:
            index = index + 1
        if index > 25:
            t = t + index
        if index <= 25:
            ps_convs[t:t+index] = 1
    else:
        t = t + 1

t = 0
ps_fcs[737] = 1
while t < 738:
    if ps_fcs[t] < 0.05:
        index = 0
        print(t)
        while ps_fcs[t+index] < 0.05 and t+index < 738:
            index = index + 1
        if index > 25:
            t = t + index
        if index <= 25:
            ps_fcs[t:t+index] = 1
            t = t + index
    else:
        t = t + 1

t = 0
ps_convsfcs[737] = 1
while t < 738:
    if ps_convsfcs[t] < 0.05:
        index = 0
        while ps_convsfcs[t+index] < 0.05:
            index = index + 1
        if index > 25:
            t = t + index
        if index <= 25:
            ps_convsfcs[t:t+index] = 1
    else:
        t = t + 1

for t in range(738):
    if ps_convs[t] < 0.05:
        plt.plot(t*0.004+0.002, 0.59, "o", color="green", markersize=4)
    if ps_fcs[t] < 0.05:
        plt.plot(t*0.004+0.002, 0.575, "o", color="greenyellow", markersize=4)
    if ps_convsfcs[t] < 0.05:
        plt.plot(t*0.004+0.002, 0.56, "o", color="olive", markersize=4)

fig = plt.gcf()
fig.set_size_inches(7, 6)

x = np.arange(0, 2.952, 0.004)

plt.fill_between(x, avg_rs_convs-err_convs, avg_rs_convs+err_convs, label='Convs', alpha=0.7, color="green")
plt.fill_between(x, avg_rs_fcs-err_fcs, avg_rs_fcs+err_fcs, label='Fcs', alpha=0.7, color="greenyellow")

noise_ceiling = np.loadtxt("../noise_ceiling/noise_ceiling/theta_power_po.txt")
noise_ceiling = np.reshape(noise_ceiling, [6, 2, 851])
"""low = noise_ceiling[:, 0, 113:]
upper = noise_ceiling[:, 1, 113:]
avg_low = np.average(low, axis=0)
avg_upper = np.average(upper, axis=0)
plt.fill_between(x, avg_low, avg_upper, label='noise ceiling', alpha=0.4, color="lightgrey")"""

plt.axhline(y=0, c="darkgrey", alpha=0.3, ls='--', linewidth="5")

plt.xlim(0, 2.952)
plt.ylim(-0.15, 0.6)
plt.tick_params(labelsize=18)
ax = plt.gca()
plt.legend(loc='center', bbox_to_anchor=(0.86, 0.83), numpoints=1)
leg = ax.get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize="18")
x = [-0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5]
y = ["-0.1", "0.0", "0.1", "0.2", "0.3", "0.4", "0.5"]
plt.yticks(x, y, fontsize=16)
plt.xlabel("Time (s)", fontsize=18)
plt.ylabel("Correlation Coefficient", fontsize=18)

plt.show()

