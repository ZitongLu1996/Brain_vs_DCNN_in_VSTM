# -*- coding: utf-8

"""
@File       :   noise_ceiling_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.rdm_corr import rdm_correlation_spearman

noise_ceiling = np.zeros([6, 2, 851], dtype=np.float)

eegrdms = np.zeros([6, 851, 18, 18], dtype=np.float)

for sub in range(6):

    subeegrdms = np.loadtxt("../eegrdm/erp_po/sub" + str(sub + 1) + ".txt")
    subeegrdms = np.reshape(subeegrdms, [851, 18, 18])

    eegrdms[sub] = subeegrdms

for sub in range(6):

    # low bound

    eegrdms_extr = np.zeros([5, 851, 18, 18], dtype=np.float)
    index = 0
    for i in range(6):
        if i != sub:
            eegrdms_extr[index] = eegrdms[i]
            index = index + 1
    avg_eegrdms_extr = np.average(eegrdms_extr, axis=0)

    # upper bound

    avg_eegrdms = np.average(eegrdms, axis=0)

    for t in range(851):
        noise_ceiling[sub, 0, t] = rdm_correlation_spearman(eegrdms[sub, t], avg_eegrdms_extr[t])[0]
        noise_ceiling[sub, 1, t] = rdm_correlation_spearman(eegrdms[sub, t], avg_eegrdms[t])[0]

noise_ceiling = np.reshape(noise_ceiling, [6*2, 851])
np.savetxt("noise_ceiling/erp_po.txt", noise_ceiling)