# -*- coding: utf-8

"""
@File       :   avgsd_corrs_stats.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.stuff import permutation_test

# trained

# convs

avgcorrs_convs = np.loadtxt("avg_corrs/convs/trained/erp_po.txt")
print(avgcorrs_convs.shape)

"""zeros = np.zeros([6])

p_convs = np.zeros([851], dtype=np.float)
for t in range(851):
    p_convs[t] = permutation_test(avgcorrs_convs[:, t], zeros)

np.savetxt("avg_stats_results/convs/trained/theta_power_po.txt", p_convs)"""

# fcs

avgcorrs_fcs = np.loadtxt("avg_corrs/fcs/trained/erp_po.txt")
print(avgcorrs_convs.shape)

"""zeros = np.zeros([6])

p_fcs = np.zeros([851], dtype=np.float)
for t in range(851):
    p_fcs[t] = permutation_test(avgcorrs_fcs[:, t], zeros)

np.savetxt("avg_stats_results/fcs/trained/alpha_power_fp.txt", p_fcs)"""

# convs-fcs

p_convsfcs = np.zeros([851], dtype=np.float)
for t in range(851):
    p_convsfcs[t] = permutation_test(avgcorrs_convs[:, t], avgcorrs_fcs[:, t])

np.savetxt("avg_stats_results/convs-fcs/trained/erp_po.txt", p_convsfcs)


# untrained

# convs

avgcorrs_convs = np.loadtxt("avg_corrs/convs/untrained/erp_po.txt")
print(avgcorrs_convs.shape)

"""zeros = np.zeros([6])

p_convs = np.zeros([851], dtype=np.float)
for t in range(851):
    p_convs[t] = permutation_test(avgcorrs_convs[:, t], zeros)

np.savetxt("avg_stats_results/convs/untrained/alpha_power_fp.txt", p_convs)"""

# fcs

avgcorrs_fcs = np.loadtxt("avg_corrs/fcs/untrained/erp_po.txt")
print(avgcorrs_convs.shape)

"""zeros = np.zeros([6])

p_fcs = np.zeros([851], dtype=np.float)
for t in range(851):
    p_fcs[t] = permutation_test(avgcorrs_fcs[:, t], zeros)

np.savetxt("avg_stats_results/fcs/untrained/alpha_power_fp.txt", p_fcs)"""

# convs-fcs

"""p_convsfcs = np.zeros([851], dtype=np.float)
for t in range(851):
    p_convsfcs[t] = permutation_test(avgcorrs_convs[:, t], avgcorrs_fcs[:, t])

np.savetxt("avg_stats_results/convs-fcs/untrained/erp_po.txt", p_convsfcs)"""