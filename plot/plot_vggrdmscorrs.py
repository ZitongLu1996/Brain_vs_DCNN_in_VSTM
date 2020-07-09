# -*- coding: utf-8

"""
@File       :   plot_vggrdms.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import matplotlib.pyplot as plt
import numpy as np
from neurora.rsa_plot import plot_rdm

corrs = np.loadtxt("../vgg_cal/untrained_rdmscorrs.txt")

corrs = np.reshape(corrs, [11, 11, 2])
rs = corrs[:, :, 0]
ps = corrs[:, :, 1]

conditions = ["Conv1", "Conv2", "Conv3", "Conv4", "Conv5", "Conv6", "Conv7", "Conv8", "Fc1", "Fc2", "Fc3"]

"""plt.imshow(rs, cmap=plt.cm.Greens, clim=(0, 1))

plt.axis("off")

for i in range(11):
    for j in range(11):
        if ps[i, j] < 0.001:
            ps[i, j] = 0
            print(i, j)
        else:
            ps[i, j] = 1

cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
font = {'size': 18}
cb.set_label('Correlation Coefficient r', fontdict=font)

step = float(1 / 11)
x = np.arange(0.5 * step, 1 + 0.5 * step, step)
y = np.arange(1 - 0.5 * step, -0.5 * step, -step)
plt.xticks(x, conditions, fontsize=12, rotation=30, ha="right")
plt.yticks(y, conditions, fontsize=12)"""

"""for i in range(11):
    for j in range(11):
        print(i, j)
        text = plt.text(i * step + 0.5 * step, 1 - j * step - 0.5 * step, float('%.4f' % rs[i, j]),
                        ha="center", va="center", color="blue", fontsize=6)"""

plot_rdm(rs, conditions=conditions, cmap="Greens")