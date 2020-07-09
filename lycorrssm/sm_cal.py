# -*- coding: utf-8

"""
@File       :   rdm_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import math
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

sm = np.zeros([6, 11, 11], dtype=np.float)

for sub in range(6):

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/trained/alpha_power_po/sub" + str(sub+1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[:, 113:, 0]

    subsm = np.zeros([11, 11], dtype=np.float)

    for i in range(11):
        for j in range(11):

            r = spearmanr(rs[i], rs[j])[0]
            subsm[i, j] = r

    sm[sub] = subsm

sm = np.reshape(sm, [6, 11*11])
np.savetxt("sm/trained/alpha_power_po.txt", sm)

sm = np.zeros([6, 11, 11], dtype=np.float)

for sub in range(6):

    corrs = np.loadtxt("../eegvggcorrs_cal/corrs/untrained/alpha_power_po/sub" + str(sub + 1) + ".txt")
    corrs = np.reshape(corrs, [11, 851, 2])

    rs = corrs[:, 113:, 0]

    subsm = np.zeros([11, 11], dtype=np.float)

    for i in range(11):
        for j in range(11):
            r = spearmanr(rs[i], rs[j])[0]
            subsm[i, j] = r

    sm[sub] = subsm

sm = np.reshape(sm, [6, 11*11])
np.savetxt("sm/untrained/alpha_power_po.txt", sm)