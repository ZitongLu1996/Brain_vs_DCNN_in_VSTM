# -*- coding: utf-8

"""
@File       :   plot_sub_eegvggcorrs.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt

corrs = np.loadtxt("../eegvggcorrs_cal/corrs/trained/theta_power_po/sub1.txt")
corrs = np.reshape(corrs, [11, 851, 2])
r = corrs[:, 113:, 0]
fig = plt.gcf()
fig.set_size_inches(8, 4)
plt.imshow(r, extent=(0, 2.952, 0, 1.76), clim=(-0.4, 0.4), origin='low', cmap='bwr')
cb = plt.colorbar()
cb.ax.tick_params(labelsize=18)
font = {'size': 20}
cb.set_label("r", fontdict=font)
x = [0.08, 0.24, 0.4, 0.56, 0.72, 0.88, 1.04, 1.2, 1.36, 1.52, 1.68]
y = ["Conv1", "Conv2", "Conv3", "Conv4", "Conv5", "Conv6", "Conv7", "Conv8", "Fc1", "Fc2", "Fc3"]
plt.tick_params(labelsize=18)
plt.yticks(x, y, fontsize=18)
plt.xlabel("Time (s)", fontsize=20)
plt.ylabel("VGG Layer", fontsize=20)
plt.show()

print(r[0])