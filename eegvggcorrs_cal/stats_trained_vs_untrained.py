# -*- coding: utf-8

"""
@File       :   stats_trained_vs_untrained.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.stats_cal import stats_stps

corrs1 = np.zeros([6, 11, 851], dtype=np.float)
corrs2 = np.zeros([6, 11, 851], dtype=np.float)

for sub in range(6):
    subcorrs = np.loadtxt("corrs/trained/erp_fp/sub" + str(sub+1) + ".txt")
    subcorrs = np.reshape(subcorrs, [11, 851, 2])

    corrs1[sub] = subcorrs[:, :, 0]

    subcorrs = np.loadtxt("corrs/untrained/erp_fp/sub" + str(sub + 1) + ".txt")
    subcorrs = np.reshape(subcorrs, [11, 851, 2])

    corrs2[sub] = subcorrs[:, :, 0]

stats = stats_stps(corrs1, corrs2)
stats = np.reshape(stats, [11*851, 2])

np.savetxt("stats_results/trained-untrained/erp_fp.txt", stats)