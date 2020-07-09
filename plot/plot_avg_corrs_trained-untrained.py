# -*- coding: utf-8

"""
@File       :   plot_avg_corrs_trained_vs_untrained.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# convs

rs_convs = np.loadtxt("../eegvggcorrs_cal/avg_corrs/convs/trained/theta_power_fp.txt")[:, 113:]
rs_fcs = np.loadtxt("../eegvggcorrs_cal/avg_corrs/convs/untrained/theta_power_fp.txt")[:, 113:]
diff = rs_convs-rs_fcs

for sub in range(6):
    b, a = signal.butter(2, 2*20/738, "lowpass")
    diff[sub] = signal.filtfilt(b, a, diff[sub])

avg = np.average(diff, axis=0)

err = np.zeros([738], dtype=np.float)

for t in range(738):
    err[t] = np.std(diff[:, t], ddof=1)/np.sqrt(6)

ps = np.loadtxt("../eegvggcorrs_cal/avg_stats_results/convs/trained-untrained/theta_power_fp.txt")[113:]

t = 0
ps[737] = 1
while t < 738:
    if ps[t] < 0.05 and avg[t] > 0:
        index = 0
        while ps[t+index] < 0.05 and avg[t+index] > 0:
            index = index + 1
        if index > 25:
            t = t + index
        if index <= 25:
            ps[t:t+index] = 1
    else:
        t = t + 1

for t in range(738):
    if ps[t] < 0.05 and avg[t] > 0:
        plt.plot(t*0.004+0.002, 0.34, "o", color="green", markersize=4)

x = np.arange(0, 2.952, 0.004)

plt.fill_between(x, avg-err, avg+err, alpha=0.7, color="green", label="Covs")

# fcs

rs_convs = np.loadtxt("../eegvggcorrs_cal/avg_corrs/fcs/trained/theta_power_fp.txt")[:, 113:]
rs_fcs = np.loadtxt("../eegvggcorrs_cal/avg_corrs/fcs/untrained/theta_power_fp.txt")[:, 113:]
diff = rs_convs-rs_fcs

for sub in range(6):
    b, a = signal.butter(2, 2*20/738, "lowpass")
    diff[sub] = signal.filtfilt(b, a, diff[sub])

avg = np.average(diff, axis=0)

err = np.zeros([738], dtype=np.float)

for t in range(738):
    err[t] = np.std(diff[:, t], ddof=1)/np.sqrt(6)

ps = np.loadtxt("../eegvggcorrs_cal/avg_stats_results/fcs/trained-untrained/theta_power_fp.txt")[113:]

t = 0
ps[737] = 1
while t < 738:
    if ps[t] < 0.05 and avg[t] > 0:
        index = 0
        while ps[t+index] < 0.05 and avg[t+index] > 0:
            index = index + 1
        if index > 25:
            t = t + index
        if index <= 25:
            ps[t:t+index] = 1
    else:
        t = t + 1

for t in range(738):
    if ps[t] < 0.05 and avg[t] > 0:
        plt.plot(t*0.004+0.002, 0.32, "o", color="greenyellow", markersize=4)

x = np.arange(0, 2.952, 0.004)

plt.fill_between(x, avg-err, avg+err, alpha=0.7, color="greenyellow", label="Fcs")

plt.axhline(y=0, c="darkgrey", alpha=0.3, ls='--', linewidth="5")

plt.xlim(0, 2.952)
plt.ylim(-0.15, 0.35)
plt.tick_params(labelsize=18)
ax = plt.gca()
plt.legend(loc='center', bbox_to_anchor=(0.86, 0.83), numpoints=1)
leg = ax.get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize="18")
x = [-0.1, 0, 0.1, 0.2, 0.3]
y = ["-0.1", "0.0", "0.1", "0.2", "0.3"]
plt.yticks(x, y, fontsize=16)
plt.xlabel("Time (s)", fontsize=18)
plt.ylabel("Correlation Coefficient\n(Trained-Untrained)", fontsize=18)

plt.show()

