# -*- coding: utf-8

"""
@File       :   corrs_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.rdm_corr import rdm_correlation_spearman

model_rdm = np.loadtxt("../codingmodel_rdm/ori_rdm.txt")

for sub in range(6):
    eegrdms = np.loadtxt("../eegrdm/theta_power_po/sub" + str(sub+1) + ".txt")
    eegrdms = np.reshape(eegrdms, [851, 18, 18])

    sub_corrs = np.zeros([851, 2], dtype=np.float)

    for i in range(851):
        sub_corrs[i] = rdm_correlation_spearman(model_rdm, eegrdms[i])

    np.savetxt("corrs/theta_power_po/ori_subs"+str(sub+1)+".txt", sub_corrs)

model_rdm = np.loadtxt("../codingmodel_rdm/pos_rdm.txt")

for sub in range(6):
    eegrdms = np.loadtxt("../eegrdm/theta_power_po/sub" + str(sub+1) + ".txt")
    eegrdms = np.reshape(eegrdms, [851, 18, 18])

    sub_corrs = np.zeros([851, 2], dtype=np.float)

    for i in range(851):
        sub_corrs[i] = rdm_correlation_spearman(model_rdm, eegrdms[i])

    np.savetxt("corrs/theta_power_po/pos_subs"+str(sub+1)+".txt", sub_corrs)


