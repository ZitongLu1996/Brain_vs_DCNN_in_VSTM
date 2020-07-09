# -*- coding: utf-8

"""
@File       :   get_codingmodel_rdm.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.rsa_plot import plot_rdm

labels = ["left 10°", "left 30°", "left 50°", "left 70°", "left 90°", "left 110°", "left 130°", "left 150°", "left 170°",
          "right 10°", "right 30°", "right 50°", "right 70°", "right 90°", "right 110°", "right 130°", "right 150°", "right 170°"]

ori_codingrdm = np.ones([18, 18], dtype=np.float)

for i in range(9):
    for j in range(9):
        ori_codingrdm[i, j] = np.abs(i-j)/8
ori_codingrdm[9:, 9:] = ori_codingrdm[:9, :9]
ori_codingrdm[:9, 9:] = ori_codingrdm[:9, :9]
ori_codingrdm[9:, :9] = ori_codingrdm[:9, :9]

plot_rdm(ori_codingrdm, conditions=labels, con_fontsize=10)

np.savetxt("ori_rdm.txt", ori_codingrdm)

pos_codingrdm = np.ones([18, 18], dtype=np.int)

for i in range(9):
    for j in range(9):
        pos_codingrdm[i, j] = 0
        pos_codingrdm[i+9, j+9] = 0

plot_rdm(pos_codingrdm, conditions=labels, con_fontsize=10)

np.savetxt("pos_rdm.txt", pos_codingrdm)



