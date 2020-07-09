# -*- coding: utf-8

"""
@File       :   corrs_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import math
from scipy.stats import spearmanr

cls_trained = np.zeros([6], dtype=np.float)
cls_untrained = np.zeros([6], dtype=np.float)

for sub in range(6):

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/trained/alpha_power_fp/sub" + str(sub+1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    conv_rs = corrs[:8, 113:, 0]
    fc_rs = corrs[8:, 113:, 0]

    n = 8*3

    rcorrs = np.zeros([n], dtype=np.float)

    index = 0

    for i in range(8):
        for j in range(3):
            rcorrs[index] = spearmanr(conv_rs[i], fc_rs[j])[0]
            index = index + 1

    print(np.average(rcorrs))

    cls_trained[sub] = np.average(rcorrs)

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/untrained/alpha_power_fp/sub" + str(sub + 1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    conv_rs = corrs[:8, 113:, 0]
    fc_rs = corrs[8:, 113:, 0]

    n = 8 * 3

    rcorrs = np.zeros([n], dtype=np.float)

    index = 0

    for i in range(8):
        for j in range(3):
            rcorrs[index] = spearmanr(conv_rs[i], fc_rs[j])[0]
            index = index + 1

    print(np.average(rcorrs))

    cls_untrained[sub] = np.average(rcorrs)

    print("***")

np.savetxt("cls/trained/alpha_power_fp.txt", cls_trained)
np.savetxt("cls/untrained/alpha_power_fp.txt", cls_untrained)