# -*- coding: utf-8

"""
@File       :   corrs_stats.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.stats_cal import stats

corrs = np.zeros([6, 11, 851, 2], dtype=np.float)

for sub in range(6):
    subcorrs = np.loadtxt("corrs/trained/erp_fp/sub" + str(sub+1) + ".txt")
    subcorrs = np.reshape(subcorrs, [11, 851, 2])

    corrs[sub] = subcorrs

stats = stats(corrs)
stats = np.reshape(stats, [11*851, 2])

np.savetxt("stats_results/trained/erp_fp.txt", stats)