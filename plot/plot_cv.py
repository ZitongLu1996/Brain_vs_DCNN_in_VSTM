# -*- coding: utf-8

"""
@File       :   plot_sd.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

sd_trained = np.loadtxt("../eegvggcorrs_cal/corrs_cv/convs/trained/erp_fp.txt")[:, 113:]
sd_untrained = np.loadtxt("../eegvggcorrs_cal/corrs_cv/convs/untrained/erp_fp.txt")[:, 113:]

for sub in range(6):
    b, a = signal.butter(2, 2*20/738, "lowpass")
    sd_trained[sub] = signal.filtfilt(b, a, sd_trained[sub])
    sd_untrained[sub] = signal.filtfilt(b, a, sd_untrained[sub])

avg_sd_trained = np.average(sd_trained, axis=0)
avg_sd_untrained = np.average(sd_untrained, axis=0)

err_sd_trained = np.zeros([738], dtype=np.float)
err_sd_untrained = np.zeros([738], dtype=np.float)

for t in range(738):
    err_sd_trained = np.std(sd_trained[:, t], ddof=1)/np.sqrt(6)
    err_sd_untrained = np.std(sd_untrained[:, t], ddof=1)/np.sqrt(6)

p = np.loadtxt("../eegvggcorrs_cal/cv_stats_results/convs/erp_fp.txt")[113:]

for t in range(738):
    if p[t] < 0.05 and avg_sd_trained[t] < avg_sd_untrained[t]:
        plt.plot(t*0.004+0.002, 0.07, "o", color="red", markersize=4)

x = np.arange(0, 2.952, 0.004)

plt.fill_between(x, avg_sd_trained-err_sd_trained, avg_sd_trained+err_sd_trained, label='Trained', alpha=0.9)
plt.fill_between(x, avg_sd_untrained-err_sd_untrained, avg_sd_untrained+err_sd_untrained, label='Untrained', alpha=0.9)

plt.xlim(0, 2.952)
plt.ylim(0, 2)
plt.tick_params(labelsize=18)
ax = plt.gca()
plt.legend(loc='center', bbox_to_anchor=(0.8, 0.9), numpoints=1)
leg = ax.get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize="18")
x = [0.0, 0.5, 1, 1.5, 2]
y = ["0.0", "0.5", "1.0", "1.5", "2.0"]
plt.yticks(x, y, fontsize=16)
plt.xlabel("Time (s)", fontsize=18)
plt.ylabel("Coefficient of Variation", fontsize=18)

plt.show()