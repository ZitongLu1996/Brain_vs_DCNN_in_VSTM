# -*- coding: utf-8

"""
@File       :   sub_corrs.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.rdm_corr import rdm_correlation_spearman

for sub in range(6):
    corrs = np.zeros([11, 851, 2], dtype=np.float32)

    vggrdms = np.zeros([11, 18, 18], dtype=np.float32)

    for i in range(11):
        filename = "../vgglayerrdm/untrained/scrop" + str(i + 1) + ".txt"
        vggrdms[i] = np.loadtxt(filename)

    eegrdms = np.loadtxt("../eegrdm/theta_power_po/sub" + str(sub + 1) + ".txt")
    eegrdms = np.reshape(eegrdms, [851, 18, 18])

    for i in range(11):
        for j in range(851):
            corrs[i, j] = rdm_correlation_spearman(vggrdms[i], eegrdms[j])

    corrs = np.reshape(corrs, [11 * 851, 2])
    np.savetxt("corrs/untrained/theta_power_po/sub" + str(sub + 1) + ".txt", corrs)

for sub in range(6):
    corrs = np.zeros([11, 851, 2], dtype=np.float32)

    vggrdms = np.zeros([11, 18, 18], dtype=np.float32)

    for i in range(11):
        filename = "../vgglayerrdm/untrained/scrop" + str(i + 1) + ".txt"
        vggrdms[i] = np.loadtxt(filename)

    eegrdms = np.loadtxt("../eegrdm/theta_power_fp/sub" + str(sub + 1) + ".txt")
    eegrdms = np.reshape(eegrdms, [851, 18, 18])

    for i in range(11):
        for j in range(851):
            corrs[i, j] = rdm_correlation_spearman(vggrdms[i], eegrdms[j])

    corrs = np.reshape(corrs, [11 * 851, 2])
    np.savetxt("corrs/untrained/theta_power_fp/sub" + str(sub + 1) + ".txt", corrs)

for sub in range(6):
    corrs = np.zeros([11, 851, 2], dtype=np.float32)

    vggrdms = np.zeros([11, 18, 18], dtype=np.float32)

    for i in range(11):
        filename = "../vgglayerrdm/untrained/scrop" + str(i + 1) + ".txt"
        vggrdms[i] = np.loadtxt(filename)

    eegrdms = np.loadtxt("../eegrdm/alpha_power_po/sub" + str(sub + 1) + ".txt")
    eegrdms = np.reshape(eegrdms, [851, 18, 18])

    for i in range(11):
        for j in range(851):
            corrs[i, j] = rdm_correlation_spearman(vggrdms[i], eegrdms[j])

    corrs = np.reshape(corrs, [11 * 851, 2])
    np.savetxt("corrs/untrained/alpha_power_po/sub" + str(sub + 1) + ".txt", corrs)

for sub in range(6):
    corrs = np.zeros([11, 851, 2], dtype=np.float32)

    vggrdms = np.zeros([11, 18, 18], dtype=np.float32)

    for i in range(11):
        filename = "../vgglayerrdm/untrained/scrop" + str(i + 1) + ".txt"
        vggrdms[i] = np.loadtxt(filename)

    eegrdms = np.loadtxt("../eegrdm/alpha_power_fp/sub" + str(sub + 1) + ".txt")
    eegrdms = np.reshape(eegrdms, [851, 18, 18])

    for i in range(11):
        for j in range(851):
            corrs[i, j] = rdm_correlation_spearman(vggrdms[i], eegrdms[j])

    corrs = np.reshape(corrs, [11 * 851, 2])
    np.savetxt("corrs/untrained/alpha_power_fp/sub" + str(sub + 1) + ".txt", corrs)

for sub in range(6):
    corrs = np.zeros([11, 851, 2], dtype=np.float32)

    vggrdms = np.zeros([11, 18, 18], dtype=np.float32)

    for i in range(11):
        filename = "../vgglayerrdm/untrained/scrop" + str(i + 1) + ".txt"
        vggrdms[i] = np.loadtxt(filename)

    eegrdms = np.loadtxt("../eegrdm/erp_po/sub" + str(sub + 1) + ".txt")
    eegrdms = np.reshape(eegrdms, [851, 18, 18])

    for i in range(11):
        for j in range(851):
            corrs[i, j] = rdm_correlation_spearman(vggrdms[i], eegrdms[j])

    corrs = np.reshape(corrs, [11 * 851, 2])
    np.savetxt("corrs/untrained/erp_po/sub" + str(sub + 1) + ".txt", corrs)

for sub in range(6):
    corrs = np.zeros([11, 851, 2], dtype=np.float32)

    vggrdms = np.zeros([11, 18, 18], dtype=np.float32)

    for i in range(11):
        filename = "../vgglayerrdm/untrained/scrop" + str(i + 1) + ".txt"
        vggrdms[i] = np.loadtxt(filename)

    eegrdms = np.loadtxt("../eegrdm/erp_fp/sub" + str(sub + 1) + ".txt")
    eegrdms = np.reshape(eegrdms, [851, 18, 18])

    for i in range(11):
        for j in range(851):
            corrs[i, j] = rdm_correlation_spearman(vggrdms[i], eegrdms[j])

    corrs = np.reshape(corrs, [11 * 851, 2])
    np.savetxt("corrs/untrained/erp_fp/sub" + str(sub + 1) + ".txt", corrs)