# -*- coding: utf-8

"""
@File       :   avg_corrs_stats_trained_vs_untrained.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from neurora.stuff import permutation_test

# erp-po

# convs

avgcorrs_trained = np.loadtxt("avg_corrs/convs/trained/erp_po.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/convs/untrained/erp_po.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/convs/trained-untrained/erp_po.txt", ps)

# fcs

avgcorrs_trained = np.loadtxt("avg_corrs/fcs/trained/erp_po.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/fcs/untrained/erp_po.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/fcs/trained-untrained/erp_po.txt", ps)


# erp-fp

# convs

avgcorrs_trained = np.loadtxt("avg_corrs/convs/trained/erp_fp.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/convs/untrained/erp_fp.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/convs/trained-untrained/erp_fp.txt", ps)

# fcs

avgcorrs_trained = np.loadtxt("avg_corrs/fcs/trained/erp_fp.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/fcs/untrained/erp_fp.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/fcs/trained-untrained/erp_fp.txt", ps)

# theta-po

# convs

avgcorrs_trained = np.loadtxt("avg_corrs/convs/trained/theta_power_po.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/convs/untrained/theta_power_po.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/convs/trained-untrained/theta_power_po.txt", ps)

# fcs

avgcorrs_trained = np.loadtxt("avg_corrs/fcs/trained/theta_power_po.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/fcs/untrained/theta_power_po.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/fcs/trained-untrained/theta_power_po.txt", ps)

# theta-fp

# convs

avgcorrs_trained = np.loadtxt("avg_corrs/convs/trained/theta_power_fp.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/convs/untrained/theta_power_fp.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/convs/trained-untrained/theta_power_fp.txt", ps)

# fcs

avgcorrs_trained = np.loadtxt("avg_corrs/fcs/trained/theta_power_fp.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/fcs/untrained/theta_power_fp.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/fcs/trained-untrained/theta_power_fp.txt", ps)


# alpha-po

# convs

avgcorrs_trained = np.loadtxt("avg_corrs/convs/trained/alpha_power_po.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/convs/untrained/alpha_power_po.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/convs/trained-untrained/alpha_power_po.txt", ps)

# fcs

avgcorrs_trained = np.loadtxt("avg_corrs/fcs/trained/alpha_power_po.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/fcs/untrained/alpha_power_po.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/fcs/trained-untrained/alpha_power_po.txt", ps)

# alpha-fp

# convs

avgcorrs_trained = np.loadtxt("avg_corrs/convs/trained/alpha_power_fp.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/convs/untrained/alpha_power_fp.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/convs/trained-untrained/alpha_power_fp.txt", ps)

# fcs

avgcorrs_trained = np.loadtxt("avg_corrs/fcs/trained/alpha_power_fp.txt")
print(avgcorrs_trained.shape)
avgcorrs_untrained = np.loadtxt("avg_corrs/fcs/untrained/alpha_power_fp.txt")
print(avgcorrs_untrained.shape)

ps = np.zeros([851], dtype=np.float)
for t in range(851):
    ps[t] = permutation_test(avgcorrs_trained[:, t], avgcorrs_untrained[:, t])

np.savetxt("avg_stats_results/fcs/trained-untrained/alpha_power_fp.txt", ps)

