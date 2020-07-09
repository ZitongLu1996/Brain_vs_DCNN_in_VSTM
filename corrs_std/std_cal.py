# -*- coding: utf-8

"""
@File       :   cv_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt

# for convs layers

"""std_trained = np.zeros([6, 851], dtype=np.float)
std_untrained = np.zeros([6, 851], dtype=np.float)

for sub in range(6):

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/trained/theta_power_fp/sub" + str(sub+1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[:8, :, 0]

    for t in range(851):
        std = np.std(rs[:, t], ddof=1)
        std_trained[sub, t] = std

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/untrained/theta_power_fp/sub" + str(sub + 1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[:8, :, 0]

    for t in range(851):
        std = np.std(rs[:, t], ddof=1)
        std_untrained[sub, t] = std

np.savetxt("std/convs/trained/theta_power_fp.txt", std_trained)
np.savetxt("std/convs/untrained/theta_power_fp.txt", std_untrained)"""


# for convs layers

std_trained = np.zeros([6, 851], dtype=np.float)
std_untrained = np.zeros([6, 851], dtype=np.float)

for sub in range(6):

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/trained/erp_po/sub" + str(sub+1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[8:, :, 0]

    for t in range(851):
        std = np.std(rs[:, t], ddof=1)
        std_trained[sub, t] = std

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/untrained/erp_po/sub" + str(sub + 1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[8:, :, 0]

    for t in range(851):
        std = np.std(rs[:, t], ddof=1)
        std_untrained[sub, t] = std

np.savetxt("std/fcs/trained/erp_po.txt", std_trained)
np.savetxt("std/fcs/untrained/erp_po.txt", std_untrained)