# -*- coding: utf-8

"""
@File       :   avg_corrs_stats_po_vs_fp.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.stuff import permutation_test

# convs

# erp

avgcorrs_po = np.loadtxt("avg_corrs/convs/trained/erp_po.txt")
print(avgcorrs_po.shape)
avgcorrs_fp = np.loadtxt("avg_corrs/convs/trained/erp_fp.txt")
print(avgcorrs_fp.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_po[:, t], avgcorrs_fp[:, t])

np.savetxt("avg_stats_results/po-fp/convs_erp.txt", ps)

# theta_power

avgcorrs_po = np.loadtxt("avg_corrs/convs/trained/theta_power_po.txt")
print(avgcorrs_po.shape)
avgcorrs_fp = np.loadtxt("avg_corrs/convs/trained/theta_power_fp.txt")
print(avgcorrs_fp.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_po[:, t], avgcorrs_fp[:, t])

np.savetxt("avg_stats_results/po-fp/convs_theta_power.txt", ps)

# alpha_power

avgcorrs_po = np.loadtxt("avg_corrs/convs/trained/alpha_power_po.txt")
print(avgcorrs_po.shape)
avgcorrs_fp = np.loadtxt("avg_corrs/convs/trained/alpha_power_fp.txt")
print(avgcorrs_fp.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_po[:, t], avgcorrs_fp[:, t])

np.savetxt("avg_stats_results/po-fp/convs_alpha_power.txt", ps)

# fcs

# erp

avgcorrs_po = np.loadtxt("avg_corrs/fcs/trained/erp_po.txt")
print(avgcorrs_po.shape)
avgcorrs_fp = np.loadtxt("avg_corrs/fcs/trained/erp_fp.txt")
print(avgcorrs_fp.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_po[:, t], avgcorrs_fp[:, t])

np.savetxt("avg_stats_results/po-fp/fcs_erp.txt", ps)

# theta_power

avgcorrs_po = np.loadtxt("avg_corrs/fcs/trained/theta_power_po.txt")
print(avgcorrs_po.shape)
avgcorrs_fp = np.loadtxt("avg_corrs/fcs/trained/theta_power_fp.txt")
print(avgcorrs_fp.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_po[:, t], avgcorrs_fp[:, t])

np.savetxt("avg_stats_results/po-fp/fcs_theta_power.txt", ps)

# alpha_power

avgcorrs_po = np.loadtxt("avg_corrs/fcs/trained/alpha_power_po.txt")
print(avgcorrs_po.shape)
avgcorrs_fp = np.loadtxt("avg_corrs/fcs/trained/alpha_power_fp.txt")
print(avgcorrs_fp.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_po[:, t], avgcorrs_fp[:, t])

np.savetxt("avg_stats_results/po-fp/fcs_alpha_power.txt", ps)