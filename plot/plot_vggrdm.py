# -*- coding: utf-8

"""
@File       :   plot_vggrdm.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt

rdm = np.loadtxt("../vgglayerrdm/untrained/scrop1.txt")

plt.imshow(rdm, cmap=plt.cm.jet, clim=(0, 1))

plt.axis("off")

plt.show()