# -*- coding: utf-8

"""
@File       :   plot_lycorrssm.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt

sm = np.loadtxt("../lycorrssm/sm/untrained/erp_po.txt")
sm = np.reshape(sm, [6, 11, 11])

avg_sm = np.average(sm, axis=0)

plt.imshow(avg_sm, extent=(0, 1, 0, 1), cmap="plasma", clim=(-0.2, 1))

cb = plt.colorbar()
cb.ax.tick_params(labelsize=16)
font = {'size': 18}
cb.set_label("Average Correlation Coefficient", fontdict=font)

conditions = ["Conv1", "Conv2", "Conv3", "Conv4", "Conv5", "Conv6", "Conv7", "Conv8", "Fc1", "Fc2", "Fc3"]

step = float(1 / 11)
x = np.arange(0.5 * step, 1 + 0.5 * step, step)
y = np.arange(1 - 0.5 * step, -0.5 * step, -step)
plt.xticks(x, conditions, fontsize=12, rotation=30, ha="right")
plt.yticks(y, conditions, fontsize=12)


plt.show()