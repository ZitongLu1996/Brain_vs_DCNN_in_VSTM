# -*- coding: utf-8

"""
@File       :   plot_avg_corrs_po-fp.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# convs

rs_po = np.loadtxt("../eegvggcorrs_cal/avg_corrs/convs/trained/alpha_power_po.txt")[:, 113:]
rs_fp = np.loadtxt("../eegvggcorrs_cal/avg_corrs/convs/trained/alpha_power_fp.txt")[:, 113:]
diff = rs_po-rs_fp

for sub in range(6):
    b, a = signal.butter(2, 2*20/738, "lowpass")
    diff[sub] = signal.filtfilt(b, a, diff[sub])

avg = np.average(diff, axis=0)

err = np.zeros([738], dtype=np.float)

for t in range(738):
    err[t] = np.std(diff[:, t], ddof=1)/np.sqrt(6)

ps = np.loadtxt("../eegvggcorrs_cal/avg_stats_results/po-fp/convs_alpha_power.txt")[113:]

t = 0
ps[737] = 1
while t < 738:
    if ps[t] < 0.05:
        index = 0
        while ps[t+index] < 0.05:
            index = index + 1
        if index > 25:
            t = t + index
        if index <= 25:
            ps[t:t+index] = 1
    else:
        t = t + 1

for t in range(738):
    if ps[t] < 0.05:
        plt.plot(t*0.004+0.002, -0.23, "o", color="blueviolet", markersize=4)
        xt = [t*0.004-0.002, t*0.004+0.002]
        ytmin = [0]
        if avg[t] > 0:
            ytmax = [avg[t]-err[t]]
            plt.fill_between(xt, ytmax, ytmin, facecolor='blueviolet', alpha=0.15)
        if avg[t] < 0:
            ytmax = [avg[t]+err[t]]
            plt.fill_between(xt, ytmax, ytmin, facecolor='blueviolet', alpha=0.15)

x = np.arange(0, 2.952, 0.004)

plt.fill_between(x, avg-err, avg+err, alpha=0.7, color="blueviolet", label="Convs")

# fcs

"""rs_po = np.loadtxt("../eegvggcorrs_cal/avg_corrs/fcs/trained/alpha_power_po.txt")[:, 113:]
rs_fp = np.loadtxt("../eegvggcorrs_cal/avg_corrs/fcs/trained/alpha_power_fp.txt")[:, 113:]
diff = rs_po-rs_fp

for sub in range(6):
    b, a = signal.butter(2, 2*20/738, "lowpass")
    diff[sub] = signal.filtfilt(b, a, diff[sub])

avg = np.average(diff, axis=0)

err = np.zeros([738], dtype=np.float)

for t in range(738):
    err[t] = np.std(diff[:, t], ddof=1)/np.sqrt(6)

ps = np.loadtxt("../eegvggcorrs_cal/avg_stats_results/po-fp/fcs_alpha_power.txt")[113:]

t = 0
ps[737] = 1
while t < 738:
    if ps[t] < 0.05:
        index = 0
        while ps[t+index] < 0.05:
            index = index + 1
        if index > 25:
            t = t + index
        if index <= 25:
            ps[t:t+index] = 1
    else:
        t = t + 1

for t in range(738):
    if ps[t] < 0.05:
        plt.plot(t*0.004+0.002, -0.23, "o", color="violet", markersize=4)
        xt = [t*0.004-0.002, t*0.004+0.002]
        ytmin = [0]
        if avg[t] > 0:
            ytmax = [avg[t]-err[t]]
            plt.fill_between(xt, ytmax, ytmin, facecolor='violet', alpha=0.15)
        if avg[t] < 0:
            ytmax = [avg[t]+err[t]]
            plt.fill_between(xt, ytmax, ytmin, facecolor='violet', alpha=0.15)

x = np.arange(0, 2.952, 0.004)

plt.fill_between(x, avg-err, avg+err, alpha=0.7, color="violet", label="Fcs")"""

plt.axhline(y=0, c="darkgrey", alpha=0.3, ls='--', linewidth="5")

plt.xlim(0, 2.952)
plt.ylim(-0.25, 0.55)
plt.tick_params(labelsize=18)
x = [-0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5]
y = ["-0.2", "-0.1", "0.0", "0.1", "0.2", "0.3", "0.4", "0.5"]
plt.yticks(x, y, fontsize=16)
plt.xlabel("Time (s)", fontsize=18)
plt.ylabel("Correlation Coefficient\n(Occipitoparietal-Frontal)", fontsize=18)

plt.show()
