# -*- coding: utf-8

"""
@File       :   sub_avg_corrs.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
import matplotlib.pyplot as plt

corrs = np.zeros([6, 11, 851], dtype=np.float)

# trained

for sub in range(6):
    subcorrs = np.loadtxt("corrs/trained/erp_po/sub" + str(sub+1) +".txt")[:, 0]
    subcorrs = np.reshape(subcorrs, [11, 851])
    corrs[sub] = subcorrs

# convs

avg_corrs = np.average(corrs[:, :8], axis=1)

cv = np.zeros([6, 851], dtype=np.float)

for sub in range(6):
    for t in range(851):
        sd = np.std(corrs[sub, :8, t], ddof=1)
        avg = np.average(corrs[sub, :8, t])
        cv[sub, t] = sd/avg

np.savetxt("avg_corrs/convs/trained/erp_po.txt", avg_corrs)
np.savetxt("corrs_cv/convs/trained/erp_po.txt", cv)

# fcs

avg_corrs = np.average(corrs[:, 8:], axis=1)

cv = np.zeros([6, 851], dtype=np.float)

for sub in range(6):
    for t in range(851):
        sd = np.std(corrs[sub, 8:, t], ddof=1)
        avg = np.average(corrs[sub, 8:, t])
        cv[sub, t] = sd/avg

np.savetxt("avg_corrs/fcs/trained/erp_po.txt", avg_corrs)
np.savetxt("corrs_cv/fcs/trained/erp_po.txt", cv)

# untrained

for sub in range(6):
    subcorrs = np.loadtxt("corrs/untrained/erp_po/sub" + str(sub+1) +".txt")[:, 0]
    subcorrs = np.reshape(subcorrs, [11, 851])
    corrs[sub] = subcorrs

# convs

avg_corrs = np.average(corrs[:, :8], axis=1)

cv = np.zeros([6, 851], dtype=np.float)

for sub in range(6):
    for t in range(851):
        sd = np.std(corrs[sub, :8, t], ddof=1)
        avg = np.average(corrs[sub, :8, t])
        cv[sub, t] = sd/avg

np.savetxt("avg_corrs/convs/untrained/erp_po.txt", avg_corrs)
np.savetxt("corrs_cv/convs/untrained/erp_po.txt", cv)

# fcs

avg_corrs = np.average(corrs[:, 8:], axis=1)

cv = np.zeros([6, 851], dtype=np.float)

for sub in range(6):
    for t in range(851):
        sd = np.std(corrs[sub, 8:, t], ddof=1)
        avg = np.average(corrs[sub, 8:, t])
        cv[sub, t] = sd/avg

np.savetxt("avg_corrs/fcs/untrained/erp_po.txt", avg_corrs)
np.savetxt("corrs_cv/fcs/untrained/erp_po.txt", cv)