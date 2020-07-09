# -*- coding: utf-8

"""
@File       :   plot_modeleegcorrs_curve.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt

con_str = "theta_power_po"

corrs = np.zeros([738, 6], dtype=np.float)

for sub in range(6):
    subcorrs = np.loadtxt("../codingmodeleeg_cal/corrs/"+con_str+"/ori_subs" + str(sub+1) + ".txt")[113:, 0]
    corrs[:, sub] = subcorrs

print(corrs)

avg = np.average(corrs, axis=1)
err = np.zeros([738], dtype=np.float)
for t in range(738):
    err[t] = np.std(corrs[t], ddof=1)/np.sqrt(6)

#stats = np.loadtxt("../eegvggcorrs_cal/stats_results/trained/"+con_str+".txt")
#stats = np.reshape(stats, [11, 851, 2])
#p = stats[layerid, 113:, 1]

x = np.arange(0, 2.952, 0.004)

plt.fill_between(x, avg-err, avg+err, label='Trained', alpha=0.9)

plt.xlim(0, 2.952)
plt.ylim(-0.2, 0.6)
plt.tick_params(labelsize=20)
ax = plt.gca()
plt.legend(loc='center', bbox_to_anchor=(0.8, 0.9), numpoints=1)
leg = ax.get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize="18")

plt.show()