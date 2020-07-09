# -*- coding: utf-8

"""
@File       :   rdmscorrs.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.rdm_corr import rdm_correlation_spearman

corrs = np.zeros([11, 11, 2], dtype=np.float32)

rdms1 = np.zeros([11, 18, 18], dtype=np.float32)

for i in range(11):
    rdms1[i] = np.loadtxt("../vgglayerrdm/trained/scrop"+str(i+1)+".txt")

rdms2 = np.zeros([11, 18, 18], dtype=np.float32)

for i in range(11):
    rdms2[i] = np.loadtxt("../vgglayerrdm/untrained/scrop"+str(i+1)+".txt")

for i in range(11):
    for j in range(11):
        corrs[i, j] = rdm_correlation_spearman(rdms1[i], rdms2[j], permutation=True)

print(corrs)
corrs = np.reshape(corrs, [11*11, 2])
np.savetxt("trained-untrained_rdmscorrs.txt", corrs)

corrs = np.zeros([11, 11, 2], dtype=np.float32)

for i in range(11):
    for j in range(11):
        corrs[i, j] = rdm_correlation_spearman(rdms1[i], rdms1[j], permutation=True)

print(corrs)
corrs = np.reshape(corrs, [11*11, 2])
np.savetxt("trained_rdmscorrs.txt", corrs)

corrs = np.zeros([11, 11, 2], dtype=np.float32)

for i in range(11):
    for j in range(11):
        corrs[i, j] = rdm_correlation_spearman(rdms2[i], rdms2[j], permutation=True)

print(corrs)
corrs = np.reshape(corrs, [11*11, 2])
np.savetxt("untrained_rdmscorrs.txt", corrs)